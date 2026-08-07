import os

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
cafe_page_path = os.path.join(spatial_dir, "cafe_social.html")

with open(cafe_page_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace photo order in 空間氛圍 section so space_09.jpg is first
item_space_09 = """                    <div class="cafe-photo-item" data-cat="space" data-img="assets/cafe_social/space_09.jpg">
                        <img src="assets/cafe_social/space_09.jpg" alt="空間氛圍 9" loading="lazy">
                    </div>\n"""

# Remove item_space_09 from its current position
if item_space_09 in content:
    content = content.replace(item_space_09, "")
    target = '<div class="cafe-grid">\n'
    content = content.replace(target, target + item_space_09, 1)

with open(cafe_page_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully moved space_09.jpg to be the FIRST photo in cafe_social.html gallery!")
