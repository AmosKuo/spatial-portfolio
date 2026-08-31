import os, glob

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
html_files = glob.glob(os.path.join(spatial_dir, "*.html"))

script_tag = '<script src="site_data.js"></script>\n'

for hfile in html_files:
    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    if "site_data.js" not in content:
        if '<script src="main.js"></script>' in content:
            content = content.replace('<script src="main.js"></script>', script_tag + '    <script src="main.js"></script>')
            with open(hfile, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added site_data.js tag to {os.path.basename(hfile)}")

