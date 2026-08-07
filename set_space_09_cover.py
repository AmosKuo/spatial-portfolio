import os

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
index_path = os.path.join(spatial_dir, "index.html")
portfolio_path = os.path.join(spatial_dir, "portfolio.html")

# 1. Update index.html
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

index_content = index_content.replace('src="assets/cafe_social/space_01.jpg"', 'src="assets/cafe_social/space_09.jpg"')
index_content = index_content.replace('src="assets/cafe_social/cafe_01.jpg"', 'src="assets/cafe_social/space_09.jpg"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)
print("Updated index.html to use space_09.jpg for Cafe cover!")

# 2. Update portfolio.html
with open(portfolio_path, "r", encoding="utf-8") as f:
    port_content = f.read()

port_content = port_content.replace('src="assets/cafe_social/space_01.jpg"', 'src="assets/cafe_social/space_09.jpg"')
port_content = port_content.replace('src="assets/cafe_social/cafe_01.jpg"', 'src="assets/cafe_social/space_09.jpg"')

with open(portfolio_path, "w", encoding="utf-8") as f:
    f.write(port_content)
print("Updated portfolio.html to use space_09.jpg for Cafe cover!")

