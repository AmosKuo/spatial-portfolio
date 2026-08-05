import os, glob, shutil
from PIL import Image

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
assets_dst = os.path.join(spatial_dir, "assets", "cafe_social")
cafe_page_path = os.path.join(spatial_dir, "cafe_social.html")

base_space = "/Users/kuoamos/Library/CloudStorage/GoogleDrive-burberryamos@gmail.com/我的雲端硬碟/光盒影像—空間攝影/室內設計拍攝工作檔案夾/社群素材/咖啡廳社群素材/範例/空間氛圍"
base_food = "/Users/kuoamos/Library/CloudStorage/GoogleDrive-burberryamos@gmail.com/我的雲端硬碟/光盒影像—空間攝影/室內設計拍攝工作檔案夾/社群素材/咖啡廳社群素材/範例/食物"

# Reset assets directory
if os.path.exists(assets_dst):
    shutil.rmtree(assets_dst)
os.makedirs(assets_dst, exist_ok=True)

space_files = sorted([os.path.join(base_space, f) for f in os.listdir(base_space) if not f.startswith(".") and f.lower().endswith(('.jpg', '.png', '.jpeg'))])
food_files = sorted([os.path.join(base_food, f) for f in os.listdir(base_food) if not f.startswith(".") and f.lower().endswith(('.jpg', '.png', '.jpeg'))])

print(f"Processing {len(space_files)} space photos and {len(food_files)} food photos.")

space_processed = []
food_processed = []

# Process Space Photos
for i, fpath in enumerate(space_files):
    out_name = f"space_{i+1:02d}.jpg"
    dst_path = os.path.join(assets_dst, out_name)
    im = Image.open(fpath)
    if im.mode != "RGB":
        im = im.convert("RGB")
    im.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
    im.save(dst_path, "JPEG", quality=90)
    space_processed.append(f"assets/cafe_social/{out_name}")
    print(f"  [Space {i+1}] {os.path.basename(fpath)} -> {out_name}")

# Process Food Photos
for i, fpath in enumerate(food_files):
    out_name = f"food_{i+1:02d}.jpg"
    dst_path = os.path.join(assets_dst, out_name)
    im = Image.open(fpath)
    if im.mode != "RGB":
        im = im.convert("RGB")
    im.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
    im.save(dst_path, "JPEG", quality=90)
    food_processed.append(f"assets/cafe_social/{out_name}")
    print(f"  [Food {i+1}] {os.path.basename(fpath)} -> {out_name}")

total_count = len(space_processed) + len(food_processed)

space_cards_html = ""
for idx, src in enumerate(space_processed):
    space_cards_html += f'                    <div class="cafe-photo-item" data-cat="space" data-img="{src}">\n'
    space_cards_html += f'                        <img src="{src}" alt="空間氛圍 {idx+1}" loading="lazy">\n'
    space_cards_html += f'                    </div>\n'

food_cards_html = ""
for idx, src in enumerate(food_processed):
    food_cards_html += f'                    <div class="cafe-photo-item" data-cat="food" data-img="{src}">\n'
    food_cards_html += f'                        <img src="{src}" alt="食物與餐點 {idx+1}" loading="lazy">\n'
    food_cards_html += f'                    </div>\n'

html_head = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>咖啡廳社群氛圍素材 | ghspatial 光盒影像</title>
    <meta name="description" content="光盒影像咖啡廳社群氛圍素材作品展示，涵蓋空間氛圍與食物餐點。">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        .filter-nav {
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            margin: 2rem 0 3.5rem;
            flex-wrap: wrap;
        }

        .filter-btn {
            background: transparent;
            border: 1px solid #ddd;
            padding: 0.65rem 1.8rem;
            font-size: 0.85rem;
            letter-spacing: 2px;
            color: #666;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
        }

        .filter-btn:hover, .filter-btn.active {
            background: var(--text-color);
            color: #fff;
            border-color: var(--text-color);
        }

        .category-header {
            text-align: left;
            margin: 3.5rem 0 1.8rem;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }

        .category-title {
            font-size: 1.5rem;
            font-weight: 300;
            letter-spacing: 3px;
        }

        .category-badge {
            font-size: 0.75rem;
            color: #888;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .cafe-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }

        .cafe-photo-item {
            position: relative;
            background: #f7f7f7;
            overflow: hidden;
            cursor: pointer;
            aspect-ratio: 4/3;
        }

        .cafe-photo-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
            display: block;
        }

        .cafe-photo-item:hover img {
            transform: scale(1.05);
        }

        /* Pure Minimalist Lightbox */
        .lightbox-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(10, 10, 10, 0.95);
            z-index: 10000;
            display: none;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }

        .lightbox-modal.active {
            display: flex;
        }

        .lightbox-box {
            position: relative;
            max-width: 1200px;
            max-height: 92vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .lightbox-img {
            max-width: 100%;
            max-height: 88vh;
            object-fit: contain;
            user-select: none;
        }

        .lightbox-close {
            position: absolute;
            top: -45px;
            right: 0;
            color: #fff;
            font-size: 2.2rem;
            background: none;
            border: none;
            cursor: pointer;
            opacity: 0.8;
            transition: opacity 0.3s;
        }

        .lightbox-close:hover {
            opacity: 1;
        }

        .lightbox-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255,255,255,0.08);
            color: #fff;
            border: none;
            font-size: 1.6rem;
            padding: 1.2rem 1.4rem;
            cursor: pointer;
            border-radius: 50%;
            transition: background 0.3s ease;
            user-select: none;
        }

        .lightbox-btn:hover {
            background: rgba(255,255,255,0.25);
        }

        .lightbox-btn.prev { left: -70px; }
        .lightbox-btn.next { right: -70px; }

        @media (max-width: 768px) {
            .cafe-grid {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            .lightbox-btn.prev { left: 10px; }
            .lightbox-btn.next { right: 10px; }
        }
    </style>
</head>
<body class="page-body">

    <!-- Site Header -->
    <header class="site-header fade-up">
        <div class="logo">
            <a href="index.html">ghspatial 光盒影像</a>
        </div>
        <nav class="main-nav">
            <ul class="nav-links">
                <li><a href="portfolio.html">空間作品集</a></li>
                <li><a href="cafe_social.html" class="active">咖啡廳社群素材</a></li>
                <li><a href="about.html">關於光盒</a></li>
                <li><a href="pricing.html">價目表</a></li>
                <li><a href="contact.html">聯絡我</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content -->
    <main class="page-content" style="padding-top: 2rem;">
        <h1 class="page-title fade-up">咖啡廳社群氛圍素材</h1>

        <!-- Filter Tab Buttons -->
        <div class="filter-nav fade-up delay-1">
            <button class="filter-btn active" data-filter="all">全部 ALL (""" + str(total_count) + """)</button>
            <button class="filter-btn" data-filter="space">01. 空間氛圍 (""" + str(len(space_processed)) + """)</button>
            <button class="filter-btn" data-filter="food">02. 食物 (""" + str(len(food_processed)) + """)</button>
        </div>

        <div style="max-width: 1350px; margin: 0 auto; padding: 0 1.5rem;">
            
            <!-- Category 1: 空間氛圍 -->
            <div class="cat-section" data-cat="space">
                <div class="category-header">
                    <div class="category-title">01. 空間氛圍</div>
                    <div class="category-badge">SPACE & AMBIENCE</div>
                </div>
                <div class="cafe-grid">
""" + space_cards_html + """                </div>
            </div>

            <!-- Category 2: 食物 -->
            <div class="cat-section" data-cat="food">
                <div class="category-header">
                    <div class="category-title">02. 食物</div>
                    <div class="category-badge">FOOD & DISHES</div>
                </div>
                <div class="cafe-grid">
""" + food_cards_html + """                </div>
            </div>

        </div>
    </main>

    <!-- Lightbox Modal -->
    <div class="lightbox-modal" id="lightbox-modal">
        <div class="lightbox-box">
            <button class="lightbox-close" id="lightbox-close">&times;</button>
            <button class="lightbox-btn prev" id="lightbox-prev">&#10094;</button>
            <button class="lightbox-btn next" id="lightbox-next">&#10095;</button>
            <img src="" alt="" class="lightbox-img" id="lightbox-img">
        </div>
    </div>

    <!-- Footer -->
    <footer class="site-footer">
        <p>&copy; 2026 ghspatial 光盒影像. All rights reserved.</p>
    </footer>

    <script src="main.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const filterBtns = document.querySelectorAll(".filter-btn");
            const catSections = document.querySelectorAll(".cat-section");

            filterBtns.forEach(btn => {
                btn.addEventListener("click", function() {
                    filterBtns.forEach(b => b.classList.remove("active"));
                    this.classList.add("active");

                    const filter = this.getAttribute("data-filter");

                    catSections.forEach(sec => {
                        if (filter === "all" || sec.getAttribute("data-cat") === filter) {
                            sec.style.display = "block";
                        } else {
                            sec.style.display = "none";
                        }
                    });
                });
            });

            const getVisibleItems = () => Array.from(document.querySelectorAll(".cafe-photo-item")).filter(el => el.closest(".cat-section").style.display !== "none");
            
            const modal = document.getElementById("lightbox-modal");
            const modalImg = document.getElementById("lightbox-img");
            const closeBtn = document.getElementById("lightbox-close");
            const prevBtn = document.getElementById("lightbox-prev");
            const nextBtn = document.getElementById("lightbox-next");

            let currentIndex = 0;
            let activeItems = [];

            function showLightbox(idx) {
                activeItems = getVisibleItems();
                if (!activeItems.length) return;

                if (idx < 0) idx = activeItems.length - 1;
                if (idx >= activeItems.length) idx = 0;

                currentIndex = idx;
                const item = activeItems[currentIndex];
                modalImg.src = item.getAttribute("data-img");
                modal.classList.add("active");
            }

            function hideLightbox() {
                modal.classList.remove("active");
            }

            document.querySelectorAll(".cafe-photo-item").forEach(item => {
                item.addEventListener("click", function() {
                    activeItems = getVisibleItems();
                    const idx = activeItems.indexOf(this);
                    if (idx !== -1) showLightbox(idx);
                });
            });

            closeBtn.addEventListener("click", hideLightbox);

            prevBtn.addEventListener("click", (e) => {
                e.stopPropagation();
                showLightbox(currentIndex - 1);
            });

            nextBtn.addEventListener("click", (e) => {
                e.stopPropagation();
                showLightbox(currentIndex + 1);
            });

            modal.addEventListener("click", (e) => {
                if (e.target === modal) hideLightbox();
            });

            document.addEventListener("keydown", (e) => {
                if (!modal.classList.contains("active")) return;
                if (e.key === "Escape") hideLightbox();
                if (e.key === "ArrowLeft") showLightbox(currentIndex - 1);
                if (e.key === "ArrowRight") showLightbox(currentIndex + 1);
            });
        });
    </script>
</body>
</html>
"""

with open(cafe_page_path, "w", encoding="utf-8") as f:
    f.write(html_head)

print("Successfully generated categorized cafe_social.html!")
