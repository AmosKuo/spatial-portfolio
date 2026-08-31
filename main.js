document.addEventListener('DOMContentLoaded', () => {
    // Hero loaded animation
    const hero = document.querySelector('.hero');
    if (hero) {
        setTimeout(() => {
            hero.classList.add('loaded');
        }, 100);
    }

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Dynamic Data Binding (來自 site_data.js 與後台 LocalStorage 快取)
    if (window.GHSpatialDataEngine) {
        const activeData = window.GHSpatialDataEngine.getActiveData();

        // 1. 動態渲染作品集畫廊 (portfolio.html & index.html)
        const galleryContainer = document.querySelector('.gallery');
        if (galleryContainer && activeData.projects) {
            // 保留原本特定頁面的單一專案內文，僅針對全站畫廊主容器進行動態更新
            if (window.location.pathname.endsWith('portfolio.html') || window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('spatial-portfolio/')) {
                galleryContainer.innerHTML = '';
                activeData.projects.forEach(p => {
                    const itemA = document.createElement('a');
                    itemA.href = p.link || '#';
                    itemA.className = 'gallery-item fade-up';
                    itemA.innerHTML = `
                        <img src="${p.coverImg}" alt="${p.title}" loading="lazy">
                        <div class="overlay">
                            <h3>${p.title}</h3>
                            <p>${p.subtitle || p.categoryName || ''}</p>
                        </div>
                    `;
                    galleryContainer.appendChild(itemA);
                });
            }
        }

        // 2. 動態渲染全站頁面文字 (Page Text Content)
        const pc = activeData.pageContent;
        if (pc) {
            // 首頁
            if (window.location.pathname.endsWith('index.html') || window.location.pathname === '/') {
                if (pc.index) {
                    const heroTitle = document.querySelector('.hero-content h1');
                    if (heroTitle && pc.index.heroTitle) heroTitle.textContent = pc.index.heroTitle;
                    const heroSub = document.querySelector('.hero-content p');
                    if (heroSub && pc.index.heroSubtitle) heroSub.textContent = pc.index.heroSubtitle;
                }
            }
            // 關於頁面
            if (window.location.pathname.endsWith('about.html')) {
                if (pc.about) {
                    const pageTitle = document.querySelector('.page-title');
                    if (pageTitle && pc.about.heading) pageTitle.textContent = pc.about.heading;
                }
            }
            // 價目表頁面
            if (window.location.pathname.endsWith('pricing.html')) {
                if (pc.pricing) {
                    const pageTitle = document.querySelector('.page-title');
                    if (pageTitle && pc.pricing.heading) pageTitle.textContent = pc.pricing.heading;
                }
            }
        }
    }

    // Intersection Observer for fade-up animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-up');
    fadeElements.forEach(el => observer.observe(el));
});
