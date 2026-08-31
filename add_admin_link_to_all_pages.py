import os, glob

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
html_files = glob.glob(os.path.join(spatial_dir, "*.html"))

admin_link = '<a href="admin.html" style="opacity: 0.6; font-size: 0.85rem;">⚙️ 後台管理</a>'

for hfile in html_files:
    if os.path.basename(hfile) == "admin.html":
        continue

    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    if 'href="admin.html"' not in content:
        if '<a href="https://www.instagram.com/gh_spatial/" target="_blank">Instagram</a>' in content:
            content = content.replace(
                '<a href="https://www.instagram.com/gh_spatial/" target="_blank">Instagram</a>',
                '<a href="https://www.instagram.com/gh_spatial/" target="_blank">Instagram</a>\n            ' + admin_link
            )
            with open(hfile, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added Admin link to footer in {os.path.basename(hfile)}")

