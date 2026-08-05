import os

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
portfolio_path = os.path.join(spatial_dir, "portfolio.html")

cafe_item_html = """            <a href="cafe_social.html" class="gallery-item fade-up">
                <img src="assets/cafe_social/space_01.jpg" alt="咖啡廳社群氛圍素材">
                <div class="overlay">
                    <h3>咖啡廳社群氛圍素材</h3>
                    <p>空間氛圍 ｜ 食物與餐點</p>
                </div>
            </a>"""

with open(portfolio_path, "r", encoding="utf-8") as f:
    content = f.read()

if 'href="cafe_social.html"' not in content:
    target = '<div class="gallery">'
    if target in content:
        content = content.replace(target, target + "\n" + cafe_item_html)
        with open(portfolio_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully added 咖啡廳社群素材 card to portfolio.html!")

