import os, glob, re, json

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"
html_files = sorted(glob.glob(os.path.join(spatial_dir, "*.html")))

project_details = {}

for hfile in html_files:
    fname = os.path.basename(hfile)
    if fname in ["index.html", "portfolio.html", "about.html", "pricing.html", "contact.html", "admin.html", "project.html"]:
        continue
    
    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    # Find title
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else fname.replace(".html", "")

    # Find subtitle / p tag under h1
    p_match = re.search(r"</h1>\s*<p[^>]*>(.*?)</p>", content, re.DOTALL)
    subtitle = p_match.group(1).strip() if p_match else ""

    # Find all images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    imgs = [i for i in imgs if "logo" not in i.lower() and "icon" not in i.lower()]

    project_details[fname] = {
        "title": title,
        "subtitle": subtitle,
        "photos": imgs
    }
    print(f"[{fname}] Title: {title} | Subtitle: {subtitle} | Photos count: {len(imgs)}")

# Check page texts for index, about, pricing, contact
page_texts = {}
for pfile in ["index.html", "about.html", "pricing.html", "contact.html"]:
    path = os.path.join(spatial_dir, pfile)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        page_texts[pfile] = content

with open("/Users/kuoamos/Desktop/spatial-portfolio/extracted_info.json", "w", encoding="utf-8") as f:
    json.dump(project_details, f, ensure_ascii=False, indent=2)

print("\nExtracted info saved to extracted_info.json")
