import os

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
index_path = os.path.join(spatial_dir, "index.html")

old_card = """            <!-- Portfolio Item: Café Social Media Content -->
            <a href="cafe_social.html" class="gallery-item fade-up">
                <img src="assets/cafe_social/cafe_01.jpg" alt="咖啡廳社群氛圍素材範例">
                <div class="overlay">
                    <h3>咖啡廳社群氛圍素材範例</h3>
                    <p>空間 • 商品 • 生活感氛圍</p>
                </div>
            </a>"""

new_card = """            <!-- Portfolio Item: Café Social Media Content -->
            <a href="cafe_social.html" class="gallery-item fade-up">
                <img src="assets/cafe_social/space_01.jpg" alt="咖啡廳社群氛圍素材">
                <div class="overlay">
                    <h3>咖啡廳社群氛圍素材</h3>
                    <p>空間氛圍 ｜ 食物與餐點</p>
                </div>
            </a>"""

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

if old_card in content:
    content = content.replace(old_card, new_card)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully fixed Cafe cover image on index.html!")
else:
    # Fallback search and replace for img src
    content = content.replace('src="assets/cafe_social/cafe_01.jpg"', 'src="assets/cafe_social/space_01.jpg"')
    content = content.replace('<h3>咖啡廳社群氛圍素材範例</h3>', '<h3>咖啡廳社群氛圍素材</h3>')
    content = content.replace('<p>空間 • 商品 • 生活感氛圍</p>', '<p>空間氛圍 ｜ 食物與餐點</p>')
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fallback fixed Cafe cover image on index.html!")

