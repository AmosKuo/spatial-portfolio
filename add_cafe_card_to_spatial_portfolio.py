import os

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
portfolio_path = os.path.join(spatial_dir, "portfolio.html")
index_path = os.path.join(spatial_dir, "index.html")

cafe_card_html = """            <!-- Portfolio Item: Café Social Media Content -->
            <a href="cafe_social.html" class="gallery-item fade-up">
                <img src="assets/cafe_social/cafe_01.jpg" alt="咖啡廳社群氛圍素材範例">
                <div class="overlay">
                    <h3>咖啡廳社群氛圍素材範例</h3>
                    <p>空間 • 商品 • 生活感氛圍</p>
                </div>
            </a>"""

# 1. Update portfolio.html
with open(portfolio_path, "r", encoding="utf-8") as f:
    port_content = f.read()

if 'href="cafe_social.html" class="gallery-item' not in port_content:
    target = '<div class="gallery fade-up delay-1">'
    if target in port_content:
        port_content = port_content.replace(target, target + "\n" + cafe_card_html)
        with open(portfolio_path, "w", encoding="utf-8") as f:
            f.write(port_content)
        print("Added Cafe card to portfolio.html!")

# 2. Update index.html
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

if 'href="cafe_social.html" class="gallery-item' not in index_content:
    target = '<div class="gallery fade-up delay-2">'
    if target in index_content:
        index_content = index_content.replace(target, target + "\n" + cafe_card_html)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("Added Cafe card to index.html!")

