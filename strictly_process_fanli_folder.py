import os, glob, shutil
from PIL import Image

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
assets_dst = os.path.join(spatial_dir, "assets", "cafe_social")
cafe_page_path = os.path.join(spatial_dir, "cafe_social.html")

target_dir = "/Users/kuoamos/Library/CloudStorage/GoogleDrive-burberryamos@gmail.com/我的雲端硬碟/光盒影像—空間攝影/室內設計拍攝工作檔案夾/社群素材/咖啡廳社群素材/範例"

# Clear destination directory completely
if os.path.exists(assets_dst):
    shutil.rmtree(assets_dst)
os.makedirs(assets_dst, exist_ok=True)

files = sorted(glob.glob(os.path.join(target_dir, "*.jpg")) + glob.glob(os.path.join(target_dir, "*.png")) + glob.glob(os.path.join(target_dir, "*.jpeg")))

print(f"Strictly processing {len(files)} photos from target folder: {target_dir}")

processed_files = []

for i, fpath in enumerate(files):
    out_name = f"cafe_{i+1:02d}.jpg"
    dst_path = os.path.join(assets_dst, out_name)
    try:
        im = Image.open(fpath)
        if im.mode != "RGB":
            im = im.convert("RGB")
        im.thumbnail((2048, 2048), Image.Resampling.LANCZOS)
        im.save(dst_path, "JPEG", quality=90)
        processed_files.append(f"assets/cafe_social/{out_name}")
        print(f"  [{i+1}/20] Processed {os.path.basename(fpath)} -> {out_name}")
    except Exception as e:
        print(f"Error {fpath}: {e}")

# Build pure photo cafe_social.html
photo_items_html = ""
for idx, rel_path in enumerate(processed_files):
    photo_items_html += f'            <div class="cafe-photo-item" data-index="{idx}" data-img="{rel_path}">\n'
    photo_items_html += f'                <img src="{rel_path}" alt="咖啡廳社群氛圍素材 {idx+1}" loading="lazy">\n'
    photo_items_html += f'            </div>\n'

pure_cafe_html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>咖啡廳社群氛圍素材 | ghspatial 光盒影像</title>
    <meta name="description" content="光盒影像咖啡廳社群氛圍素材作品展示。">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        .cafe-pure-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 1.5rem;
            max-width: 1350px;
            margin: 3rem auto 5rem;
            padding: 0 1.5rem;
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
            .cafe-pure-grid {
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

    <!-- Main Content: Pure Photography Grid -->
    <main class="page-content" style="padding-top: 2rem;">
        <h1 class="page-title fade-up">咖啡廳社群氛圍素材</h1>

        <div class="cafe-pure-grid fade-up delay-1">
""" + photo_items_html + """        </div>
    </main>

    <!-- Lightbox Modal (Pure Photo View) -->
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
            const items = Array.from(document.querySelectorAll(".cafe-photo-item"));
            const modal = document.getElementById("lightbox-modal");
            const modalImg = document.getElementById("lightbox-img");
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
    f.write(pure_cafe_html)

print("Successfully rebuilt cafe_social.html with strictly the 20 photos from the 範例 folder!")
