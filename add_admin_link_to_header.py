import os, glob

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
html_files = glob.glob(os.path.join(spatial_dir, "*.html"))

header_link = '<li><a href="admin.html" style="opacity: 0.7; font-weight: 500;">⚙️ 後台管理</a></li>'

for hfile in html_files:
    if os.path.basename(hfile) == "admin.html":
        continue

    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    if '<li><a href="admin.html"' not in content:
        if '<li><a href="contact.html">聯絡我</a></li>' in content:
            content = content.replace(
                '<li><a href="contact.html">聯絡我</a></li>',
                '<li><a href="contact.html">聯絡我</a></li>\n                ' + header_link
            )
            with open(hfile, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added Admin link to header in {os.path.basename(hfile)}")
        elif '<li><a href="contact.html" class="active">聯絡我</a></li>' in content:
            content = content.replace(
                '<li><a href="contact.html" class="active">聯絡我</a></li>',
                '<li><a href="contact.html" class="active">聯絡我</a></li>\n                ' + header_link
            )
            with open(hfile, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added Admin link to header in {os.path.basename(hfile)}")

