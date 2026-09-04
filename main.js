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
        // 1.5 動態渲染「看見竹北之美」Threads 照片連載區塊
        const zhubeiContainer = document.getElementById('zhubeiContainer');
        if (zhubeiContainer && activeData.zhubeiSeries) {
            zhubeiContainer.innerHTML = '';
            activeData.zhubeiSeries.forEach(s => {
                const card = document.createElement('article');
                card.className = 'zhubei-card fade-up';
                card.innerHTML = `
                    <div class="zhubei-card-img-wrapper">
                        <span class="zhubei-episode-tag">${s.episode || ''}</span>
                        <img src="${s.photo}" alt="${s.title}" loading="lazy">
                    </div>
                    <div class="zhubei-card-body">
                        <h3 class="zhubei-card-title">${s.title}</h3>
                        <p class="zhubei-card-excerpt">${s.excerpt}</p>
                        <div class="zhubei-card-footer">
                            <span>${s.date || ''}</span>
                            <a href="${s.threadsUrl || 'https://www.threads.net/'}" target="_blank" rel="noopener" class="zhubei-threads-btn">
                                在 Threads 閱讀 ↗
                            </a>
                        </div>
                    </div>
                `;
                zhubeiContainer.appendChild(card);
            });
        }

        // 2. 動態渲染全站頁面文字與價目表細項 (Page Text & Fine Pricing Details)
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
                    const ps = document.querySelectorAll('.about-content p');
                    if (ps.length >= 1 && pc.about.intro1) ps[0].textContent = pc.about.intro1;
                    if (ps.length >= 2 && pc.about.intro2) ps[1].textContent = pc.about.intro2;
                }
            }
            // 價目表頁面 (全細項動態綁定)
            if (window.location.pathname.endsWith('pricing.html')) {
                if (pc.pricing) {
                    const pr = pc.pricing;

                    const pageTitle = document.querySelector('.page-title');
                    if (pageTitle && pr.heading) pageTitle.textContent = pr.heading;

                    // 首次合作方案
                    const featCard = document.querySelector('.pricing-card[style*="border: 2px solid"]');
                    if (featCard && pr.featuredPlan) {
                        const h3 = featCard.querySelector('h3');
                        if (h3 && pr.featuredPlan.title) h3.textContent = pr.featuredPlan.title;
                        const price = featCard.querySelector('.price');
                        if (price && pr.featuredPlan.price) price.textContent = pr.featuredPlan.price;
                        const desc = featCard.querySelector('.plan-desc');
                        if (desc && pr.featuredPlan.desc) desc.textContent = pr.featuredPlan.desc;
                        const ul = featCard.querySelector('ul');
                        if (ul && pr.featuredPlan.items) {
                            ul.innerHTML = pr.featuredPlan.items.map((item, idx) => `
                                <li style="border-bottom: ${idx < pr.featuredPlan.items.length - 1 ? '1px solid #eee' : 'none'}; padding-bottom: 1rem;">
                                    ${item}
                                </li>
                            `).join('');
                        }
                    }

                    // 小坪數 & 大坪數方案
                    const cards = document.querySelectorAll('.pricing-container .pricing-card');
                    if (cards.length >= 2) {
                        // 小坪數
                        if (pr.planSmall) {
                            const c = cards[0];
                            if (pr.planSmall.title) c.querySelector('h3').textContent = pr.planSmall.title;
                            if (pr.planSmall.price) c.querySelector('.price').innerHTML = pr.planSmall.price + '<span> / 元</span>';
                            if (pr.planSmall.desc) c.querySelector('.plan-desc').textContent = pr.planSmall.desc;
                            if (pr.planSmall.items) {
                                c.querySelector('ul').innerHTML = pr.planSmall.items.map(item => `<li>${item}</li>`).join('');
                            }
                        }
                        // 大坪數
                        if (pr.planLarge) {
                            const c = cards[1];
                            if (pr.planLarge.title) c.querySelector('h3').textContent = pr.planLarge.title;
                            if (pr.planLarge.price) c.querySelector('.price').innerHTML = pr.planLarge.price + '<span> / 元</span>';
                            if (pr.planLarge.desc) c.querySelector('.plan-desc').textContent = pr.planLarge.desc;
                            if (pr.planLarge.items) {
                                c.querySelector('ul').innerHTML = pr.planLarge.items.map(item => `<li>${item}</li>`).join('');
                            }
                        }
                    }

                    // 注意事項
                    const infoSections = document.querySelectorAll('.info-section');
                    if (infoSections.length >= 1 && pr.notes) {
                        const ul = infoSections[0].querySelector('ul.info-list');
                        if (ul) {
                            ul.innerHTML = pr.notes.map(n => `<li>${n}</li>`).join('');
                        }
                    }

                    // 預約執行流程
                    if (infoSections.length >= 2 && pr.process) {
                        const ol = infoSections[1].querySelector('ol.process-list');
                        if (ol) {
                            ol.innerHTML = pr.process.map(step => `<li>${step}</li>`).join('');
                        }
                    }
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
