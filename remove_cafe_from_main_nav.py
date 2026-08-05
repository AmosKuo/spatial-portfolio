import os, glob

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
html_files = glob.glob(os.path.join(spatial_dir, "*.html"))

nav_link_1 = '<li><a href="cafe_social.html">咖啡廳社群素材</a></li>\n'
nav_link_1_alt = '<li><a href="cafe_social.html">咖啡廳社群素材</a></li>'
nav_link_2 = '<li><a href="cafe_social.html" class="active">咖啡廳社群素材</a></li>\n'
nav_link_2_alt = '<li><a href="cafe_social.html" class="active">咖啡廳社群素材</a></li>'

updated_count = 0

for hfile in html_files:
    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    new_content = new_content.replace(nav_link_1, "")
    new_content = new_content.replace(nav_link_1_alt, "")
    new_content = new_content.replace(nav_link_2, "")
    new_content = new_content.replace(nav_link_2_alt, "")

    if new_content != content:
        with open(hfile, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_count += 1
        print(f"Removed cafe from nav in {os.path.basename(hfile)}")

print(f"Cleaned nav links across {updated_count} files.")
