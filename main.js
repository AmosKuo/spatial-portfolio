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
        if (galleryContainer && activeData.projects && activeData.projects.length > 0) {
            if (window.location.pathname.endsWith('portfolio.html') || window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('spatial-portfolio/')) {
                galleryContainer.innerHTML = '';
                activeData.projects.forEach(p => {
                    const itemA = document.createElement('a');
                    itemA.href = p.link || '#';
                    itemA.className = 'gallery-item fade-up visible';
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

        // 1.5 動態渲染「看見竹北之美」相片輪播 Slider
        const sliderTrack = document.getElementById('zhubeiSliderTrack');
        if (sliderTrack && activeData.zhubeiPhotos) {
            sliderTrack.innerHTML = '';
            activeData.zhubeiPhotos.forEach((photoPath, idx) => {
                const slide = document.createElement('div');
                slide.className = 'slider-slide';
                slide.innerHTML = `
                    <div class="slider-slide-inner">
                        <img src="${photoPath}" alt="看見竹北之美 輪播相片 ${idx + 1}" loading="lazy">
                    </div>
                `;
                sliderTrack.appendChild(slide);
            });

            // Initialize Carousel Controls
            initZhubeiSlider(activeData.zhubeiPhotos.length);
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

function initZhubeiSlider(totalItems) {
    const track = document.getElementById('zhubeiSliderTrack');
    const prevBtn = document.getElementById('sliderPrevBtn');
    const nextBtn = document.getElementById('sliderNextBtn');
    const dotsContainer = document.getElementById('sliderDots');
    if (!track || totalItems === 0) return;

    let currentIndex = 0;
    function getVisibleCount() {
        if (window.innerWidth <= 768) return 1;
        if (window.innerWidth <= 1024) return 2;
        return 3;
    }

    const maxIndex = () => Math.max(0, totalItems - getVisibleCount());

    function createDots() {
        if (!dotsContainer) return;
        dotsContainer.innerHTML = '';
        const totalDots = maxIndex() + 1;
        for (let i = 0; i < totalDots; i++) {
            const dot = document.createElement('div');
            dot.className = `slider-dot ${i === currentIndex ? 'active' : ''}`;
            dot.addEventListener('click', () => goToSlide(i));
            dotsContainer.appendChild(dot);
        }
    }

    function updateSlider() {
        const visibleCount = getVisibleCount();
        const slideWidthPercent = 100 / visibleCount;
        track.style.transform = `translateX(-${currentIndex * slideWidthPercent}%)`;

        if (dotsContainer) {
            createDots();
        }
    }

    function goToSlide(idx) {
        currentIndex = Math.min(Math.max(0, idx), maxIndex());
        updateSlider();
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex <= 0) ? maxIndex() : currentIndex - 1;
            updateSlider();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex >= maxIndex()) ? 0 : currentIndex + 1;
            updateSlider();
        });
    }

    let autoPlayInterval = setInterval(() => {
        currentIndex = (currentIndex >= maxIndex()) ? 0 : currentIndex + 1;
        updateSlider();
    }, 3500);

    const container = track.closest('.zhubei-slider-container');
    if (container) {
        container.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
        container.addEventListener('mouseleave', () => {
            clearInterval(autoPlayInterval);
            autoPlayInterval = setInterval(() => {
                currentIndex = (currentIndex >= maxIndex()) ? 0 : currentIndex + 1;
                updateSlider();
            }, 3500);
        });
    }

    window.addEventListener('resize', () => {
        if (currentIndex > maxIndex()) currentIndex = maxIndex();
        updateSlider();
    });

    updateSlider();
}
