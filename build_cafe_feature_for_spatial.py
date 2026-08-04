import os, glob, shutil
from PIL import Image

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
gdrive_src = "/Users/kuoamos/Library/CloudStorage/GoogleDrive-burberryamos@gmail.com/我的雲端硬碟/光盒影像—空間攝影/室內設計拍攝工作檔案夾/社群素材/咖啡廳社群素材/範例"

assets_dst = os.path.join(spatial_dir, "assets", "cafe_social")
os.makedirs(assets_dst, exist_ok=True)

# 1. Process 20 Photos from Google Drive to spatial-portfolio/assets/cafe_social/
files = sorted(glob.glob(os.path.join(gdrive_src, "*.jpg")) + glob.glob(os.path.join(gdrive_src, "*.png")))

print(f"Found {len(files)} source photos in Google Drive.")

for i, fpath in enumerate(files):
    fname = os.path.basename(fpath)
    dst_path = os.path.join(assets_dst, f"cafe_{i+1:02d}.jpg")
    try:
        im = Image.open(fpath)
        if im.mode != "RGB":
            im = im.convert("RGB")
        im.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
        im.save(dst_path, "JPEG", quality=90)
        print(f"[{i+1}/20] Saved {fname} -> cafe_{i+1:02d}.jpg ({im.size})")
    except Exception as e:
        print(f"Error {fname}: {e}")

# 2. Build cafe_social.html
cafe_page_path = os.path.join(spatial_dir, "cafe_social.html")

photo_items = [
    # 空間 Space (7)
    {"id": "cafe_01", "src": "assets/cafe_social/cafe_01.jpg", "category": "space", "cat_name": "空間", "title": "光影流動的咖啡空間", "desc": "溫潤木質與自然光交織的空間視角"},
    {"id": "cafe_02", "src": "assets/cafe_social/cafe_02.jpg", "category": "space", "cat_name": "空間", "title": "簡約建築美學角落", "desc": "通透光感與靜謐座席區"},
    {"id": "cafe_06", "src": "assets/cafe_social/cafe_06.jpg", "category": "space", "cat_name": "空間", "title": "開放式吧台設計全景", "desc": "工作區與吧台材質工藝展示"},
    {"id": "cafe_09", "src": "assets/cafe_social/cafe_09.jpg", "category": "space", "cat_name": "空間", "title": "風格燈飾與角落端景", "desc": "細緻燈光氛圍與空間氣質層次"},
    {"id": "cafe_13", "src": "assets/cafe_social/cafe_13.jpg", "category": "space", "cat_name": "空間", "title": "落地窗景空間開闊感", "desc": "戶外綠意與室內氣息無縫連結"},
    {"id": "cafe_17", "src": "assets/cafe_social/cafe_17.jpg", "category": "space", "cat_name": "空間", "title": "立面外觀與品牌門面", "desc": "強烈品牌辨識度的門面社群圖像"},
    {"id": "cafe_20", "src": "assets/cafe_social/cafe_20.jpg", "category": "space", "cat_name": "空間", "title": "全景座位區氛圍展演", "desc": "沉浸式質感咖啡館環境記錄"},

    # 商品 Product (7)
    {"id": "cafe_04", "src": "assets/cafe_social/cafe_04.jpg", "category": "product", "cat_name": "商品", "title": "手沖單品咖啡細節", "desc": "特寫琥珀色咖啡特有光澤與質地"},
    {"id": "cafe_05", "src": "assets/cafe_social/cafe_05.jpg", "category": "product", "cat_name": "商品", "title": "招牌手作甜點特寫", "desc": "誘人層次感與極致擺盤特寫"},
    {"id": "cafe_08", "src": "assets/cafe_social/cafe_08.jpg", "category": "product", "cat_name": "商品", "title": "冰滴特調層次近拍", "desc": "漸層奶霜與濃縮咖啡細緻質感"},
    {"id": "cafe_11", "src": "assets/cafe_social/cafe_11.jpg", "category": "product", "cat_name": "商品", "title": "義式濃縮油脂特寫", "desc": "飽滿Crema與典藏陶瓷杯具"},
    {"id": "cafe_14", "src": "assets/cafe_social/cafe_14.jpg", "category": "product", "cat_name": "商品", "title": "法式塔類甜點精緻視覺", "desc": "吸引顧客點擊的社群宣傳素材"},
    {"id": "cafe_16", "src": "assets/cafe_social/cafe_16.jpg", "category": "product", "cat_name": "商品", "title": "冰萃特調視覺層次", "desc": "清涼感透明玻璃杯與冰塊光影"},
    {"id": "cafe_19", "src": "assets/cafe_social/cafe_19.jpg", "category": "product", "cat_name": "商品", "title": "精品濾掛與烘豆質感", "desc": "品牌周邊商品商業特寫照片"},

    # 生活感氛圍 Lifestyle (6)
    {"id": "cafe_03", "src": "assets/cafe_social/cafe_03.jpg", "category": "lifestyle", "cat_name": "生活感氛圍", "title": "午後日光隨手紀錄", "desc": "捕捉最自然的對談與慢生活步調"},
    {"id": "cafe_07", "src": "assets/cafe_social/cafe_07.jpg", "category": "lifestyle", "cat_name": "生活感氛圍", "title": "溫暖手握咖啡杯瞬間", "desc": "具感染力的生活感手部特寫紀錄"},
    {"id": "cafe_10", "src": "assets/cafe_social/cafe_10.jpg", "category": "lifestyle", "cat_name": "生活感氛圍", "title": "窗邊閱讀漫光時刻", "desc": "透光紗簾與慢拾優閒社交素材"},
    {"id": "cafe_12", "src": "assets/cafe_social/cafe_12.jpg", "category": "lifestyle", "cat_name": "生活感氛圍", "title": "微光角落生活絮語", "desc": "極具情感溫度的社群貼文風格範例"},
    {"id": "cafe_15", "src": "assets/cafe_social/cafe_15.jpg", "category": "lifestyle", "cat_name": "生活感氛圍", "title": "好友聚餐歡笑花絮", "desc": "展現親切互動感的真實生活畫面"},
    {"id": "cafe_18", "src": "assets/cafe_social/cafe_18.jpg", "category": "lifestyle", "cat_name": "生活感氛圍", "title": "工作與咖啡隨手情境", "desc": "筆電、咖啡與質感文具的辦公氛圍"}
]

cafe_html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>咖啡廳社群氛圍素材範例 | ghspatial 光盒影像</title>
    <meta name="description" content="光盒影像專為咖啡館與餐飲品牌打造的社群氛圍素材範例，涵蓋空間、商品與生活感氛圍三大分類。">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        .filter-nav {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin: 2rem 0 4rem;
            flex-wrap: wrap;
        }

        .filter-btn {
            background: transparent;
            border: 1px solid #ddd;
            padding: 0.6rem 1.6rem;
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
            margin: 4rem 0 2rem;
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
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }

        .cafe-item {
            background: #fff;
            border: 1px solid #eee;
            overflow: hidden;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            cursor: pointer;
            display: flex;
            flex-direction: column;
        }

        .cafe-item:hover {
            transform: translateY(-6px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.08);
        }

        .cafe-item-img {
            width: 100%;
            aspect-ratio: 4/3;
            overflow: hidden;
            background: #f7f7f7;
        }

        .cafe-item-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .cafe-item:hover .cafe-item-img img {
            transform: scale(1.05);
        }

        .cafe-item-info {
            padding: 1.5rem;
            text-align: left;
        }

        .cafe-item-tag {
            font-size: 0.75rem;
            color: #888;
            letter-spacing: 2px;
            margin-bottom: 0.3rem;
            text-transform: uppercase;
        }

        .cafe-item-title {
            font-size: 1.15rem;
            font-weight: 400;
            margin-bottom: 0.4rem;
        }

        .cafe-item-desc {
            font-size: 0.85rem;
            color: #666;
            line-height: 1.5;
        }

        /* Lightbox */
        .lightbox-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(10, 10, 10, 0.92);
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
            max-width: 1100px;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .lightbox-img {
            max-width: 100%;
            max-height: 80vh;
            object-fit: contain;
        }

        .lightbox-info {
            color: #fff;
            margin-top: 1rem;
            text-align: center;
        }

        .lightbox-close {
            position: absolute;
            top: -40px;
            right: 0;
            color: #fff;
            font-size: 2rem;
            background: none;
            border: none;
            cursor: pointer;
        }

        .lightbox-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255,255,255,0.1);
            color: #fff;
            border: none;
            font-size: 1.5rem;
            padding: 0.8rem 1rem;
            cursor: pointer;
            transition: background 0.3s;
        }

        .lightbox-btn:hover {
            background: rgba(255,255,255,0.3);
        }

        .lightbox-btn.prev { left: -60px; }
        .lightbox-btn.next { right: -60px; }

        @media (max-width: 768px) {
            .lightbox-btn.prev { left: 10px; }
            .lightbox-btn.next { right: 10px; }
        }
    </style>
</head>
<body class="page-body">

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

    <main class="page-content">
        <h1 class="page-title fade-up">咖啡廳社群氛圍素材範例</h1>
        <p style="text-align: center; color: #666; max-width: 600px; margin: -1.5rem auto 2.5rem; font-size: 0.95rem; letter-spacing: 1px;" class="fade-up delay-1">
            專為咖啡館與餐飲品牌打造。涵蓋「空間」、「商品」與「生活感氛圍」三大分類範例集結於同一頁面。
        </p>

        <!-- Filter Tab Buttons -->
        <div class="filter-nav fade-up delay-1">
            <button class="filter-btn active" data-filter="all">全部 ALL (20)</button>
            <button class="filter-btn" data-filter="space">01. 空間 (7)</button>
            <button class="filter-btn" data-filter="product">02. 商品 (7)</button>
            <button class="filter-btn" data-filter="lifestyle">03. 生活感氛圍 (6)</button>
        </div>

        <div style="max-width: 1200px; margin: 0 auto;">
            
            <!-- Category 1: 空間 (Space) -->
            <div class="cat-section" data-cat="space">
                <div class="category-header">
                    <div class="category-title">01. 空間</div>
                    <div class="category-badge">SPACE & INTERIOR</div>
                </div>
                <div class="cafe-grid">
"""

space_items = [p for p in photo_items if p["category"] == "space"]
for p in space_items:
    cafe_html += f"""                    <div class="cafe-item" data-cat="space" data-img="{p['src']}" data-title="{p['title']}" data-desc="{p['desc']}">
                        <div class="cafe-item-img"><img src="{p['src']}" alt="{p['title']}"></div>
                        <div class="cafe-item-info">
                            <div class="cafe-item-tag">空間 SPACE</div>
                            <div class="cafe-item-title">{p['title']}</div>
                            <div class="cafe-item-desc">{p['desc']}</div>
                        </div>
                    </div>
"""

cafe_html += """                </div>
            </div>

            <!-- Category 2: 商品 (Product) -->
            <div class="cat-section" data-cat="product">
                <div class="category-header">
                    <div class="category-title">02. 商品</div>
                    <div class="category-badge">PRODUCT & DETAIL</div>
                </div>
                <div class="cafe-grid">
"""

product_items = [p for p in photo_items if p["category"] == "product"]
for p in product_items:
    cafe_html += f"""                    <div class="cafe-item" data-cat="product" data-img="{p['src']}" data-title="{p['title']}" data-desc="{p['desc']}">
                        <div class="cafe-item-img"><img src="{p['src']}" alt="{p['title']}"></div>
                        <div class="cafe-item-info">
                            <div class="cafe-item-tag">商品 PRODUCT</div>
                            <div class="cafe-item-title">{p['title']}</div>
                            <div class="cafe-item-desc">{p['desc']}</div>
                        </div>
                    </div>
"""

cafe_html += """                </div>
            </div>

            <!-- Category 3: 生活感氛圍 (Lifestyle Ambience) -->
            <div class="cat-section" data-cat="lifestyle">
                <div class="category-header">
                    <div class="category-title">03. 生活感氛圍</div>
                    <div class="category-badge">LIFESTYLE AMBIENCE</div>
                </div>
                <div class="cafe-grid">
"""

lifestyle_items = [p for p in photo_items if p["category"] == "lifestyle"]
for p in lifestyle_items:
    cafe_html += f"""                    <div class="cafe-item" data-cat="lifestyle" data-img="{p['src']}" data-title="{p['title']}" data-desc="{p['desc']}">
                        <div class="cafe-item-img"><img src="{p['src']}" alt="{p['title']}"></div>
                        <div class="cafe-item-info">
                            <div class="cafe-item-tag">生活感氛圍 LIFESTYLE</div>
                            <div class="cafe-item-title">{p['title']}</div>
                            <div class="cafe-item-desc">{p['desc']}</div>
                        </div>
                    </div>
"""

cafe_html += """                </div>
            </div>

        </div>

        <div style="text-align: center; margin: 4rem 0;">
            <a href="contact.html" class="btn">預約品牌拍攝洽詢 &rarr;</a>
        </div>
    </main>

    <!-- Lightbox Modal -->
    <div class="lightbox-modal" id="lightbox-modal">
        <div class="lightbox-box">
            <button class="lightbox-close" id="lightbox-close">&times;</button>
            <button class="lightbox-btn prev" id="lightbox-prev">&#10094;</button>
            <button class="lightbox-btn next" id="lightbox-next">&#10095;</button>
            <img src="" alt="" class="lightbox-img" id="lightbox-img">
            <div class="lightbox-info">
                <h3 id="lightbox-title" style="margin-bottom: 0.3rem;"></h3>
                <p id="lightbox-desc" style="font-size: 0.85rem; color: #ccc;"></p>
            </div>
        </div>
    </div>

    <footer class="site-footer">
        <p>&copy; 2026 ghspatial 光盒影像. All rights reserved.</p>
    </footer>

    <script src="main.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            // Interactive Category Filter
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

            // Lightbox Modal
            const items = Array.from(document.querySelectorAll(".cafe-item"));
            const modal = document.getElementById("lightbox-modal");
            const modalImg = document.getElementById("lightbox-img");
            const modalTitle = document.getElementById("lightbox-title");
            const modalDesc = document.getElementById("lightbox-desc");
            const closeBtn = document.getElementById("lightbox-close");
            const prevBtn = document.getElementById("lightbox-prev");
            const nextBtn = document.getElementById("lightbox-next");

            let currentIndex = 0;

            function showLightbox(idx) {
                if (idx < 0) idx = items.length - 1;
                if (idx >= items.length) idx = 0;

                currentIndex = idx;
                const item = items[currentIndex];

                modalImg.src = item.getAttribute("data-img");
                modalTitle.textContent = item.getAttribute("data-title");
                modalDesc.textContent = item.getAttribute("data-desc");

                modal.classList.add("active");
            }

            function hideLightbox() {
                modal.classList.remove("active");
            }

            items.forEach((item, idx) => {
                item.addEventListener("click", () => showLightbox(idx));
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
    f.write(cafe_html)

print(f"Successfully generated {cafe_page_path} for spatial-portfolio!")

# 3. Update Nav Links across all HTML files in spatial-portfolio
html_files = glob.glob(os.path.join(spatial_dir, "*.html"))

nav_item_html = '<li><a href="cafe_social.html">咖啡廳社群素材</a></li>'

for hfile in html_files:
    if os.path.basename(hfile) == "cafe_social.html":
        continue

    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    if nav_item_html not in content and '<li><a href="portfolio.html">空間作品集</a></li>' in content:
        content = content.replace('<li><a href="portfolio.html">空間作品集</a></li>', '<li><a href="portfolio.html">空間作品集</a></li>\n                <li><a href="cafe_social.html">咖啡廳社群素材</a></li>')
        content = content.replace('<li><a href="portfolio.html" class="active">空間作品集</a></li>', '<li><a href="portfolio.html" class="active">空間作品集</a></li>\n                <li><a href="cafe_social.html">咖啡廳社群素材</a></li>')

        with open(hfile, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Updated navigation bar across {len(html_files)} HTML files in spatial-portfolio!")
