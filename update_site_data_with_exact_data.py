import os, glob, re, json

spatial_dir = "/Users/kuoamos/Desktop/spatial-portfolio"

# 1. Parse all projects and photos
html_files = sorted(glob.glob(os.path.join(spatial_dir, "*.html")))

projects_list = []

category_mapping = {
    "cafe_social.html": ("cafe", "社群素材"),
    "fifi.html": ("residential", "軟裝陳設"),
    "keelung.html": ("residential", "住宅室內"),
    "kualalumpur.html": ("architecture", "建築巡禮"),
    "luoyushan.html": ("residential", "住宅豪宅"),
    "pan_pan.html": ("architecture", "建築透天"),
    "roman_holiday.html": ("residential", "住宅室內"),
    "underpass.html": ("architecture", "公共建築"),
    "xinwu.html": ("commercial", "商業展覽")
}

for hfile in html_files:
    fname = os.path.basename(hfile)
    if fname in ["index.html", "portfolio.html", "about.html", "pricing.html", "contact.html", "admin.html", "project.html"]:
        continue
    
    with open(hfile, "r", encoding="utf-8") as f:
        content = f.read()

    # Find title
    title_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else fname.replace(".html", "")

    # Find subtitle
    p_match = re.search(r"</h1>\s*<p[^>]*>(.*?)</p>", content, re.DOTALL)
    subtitle = p_match.group(1).strip() if p_match else ""

    # Find all images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    imgs = [i for i in imgs if "logo" not in i.lower() and "icon" not in i.lower()]

    cover_img = imgs[0] if imgs else ""
    if fname == "cafe_social.html":
        cover_img = "assets/cafe_social/space_09.jpg"

    cat, cat_name = category_mapping.get(fname, ("residential", "作品展示"))

    proj_id = "proj_" + fname.replace(".html", "")

    projects_list.append({
        "id": proj_id,
        "updatedAt": 1725116400000,
        "title": title,
        "subtitle": subtitle,
        "category": cat,
        "categoryName": cat_name,
        "coverImg": cover_img,
        "link": fname,
        "photos": imgs
    })

# 2. Extract exact text for About, Pricing, Contact, Index
def get_page_info(filename):
    path = os.path.join(spatial_dir, filename)
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    return c

index_c = get_page_info("index.html")
about_c = get_page_info("about.html")
pricing_c = get_page_info("pricing.html")
contact_c = get_page_info("contact.html")

# Parse index
idx_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", index_c, re.DOTALL)
idx_sub = re.search(r"<p class=[\"\']subtitle[\"\'][^>]*>(.*?)</p>", index_c, re.DOTALL)

# Parse about
ab_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", about_c, re.DOTALL)
ab_ps = re.findall(r"<p[^>]*>(.*?)</p>", about_c, re.DOTALL)

# Parse pricing
pr_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", pricing_c, re.DOTALL)
pr_sub = re.search(r"<p class=[\"\']subtitle[\"\'][^>]*>(.*?)</p>", pricing_c, re.DOTALL)

# Parse contact
ct_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", contact_c, re.DOTALL)
ct_sub = re.search(r"<p class=[\"\']subtitle[\"\'][^>]*>(.*?)</p>", contact_c, re.DOTALL)

page_content = {
    "index": {
        "updatedAt": 1725116400000,
        "title": "ghspatial 光盒影像 | Spatial Photography",
        "heroTitle": idx_h1.group(1).strip() if idx_h1 else "ghspatial 光盒影像",
        "heroSubtitle": idx_sub.group(1).strip() if idx_sub else "High-end spatial and architectural photography by ghspatial 光盒影像.",
        "scrollText": "SCROLL"
    },
    "about": {
        "updatedAt": 1725116400000,
        "title": "關於光盒 | ghspatial",
        "heading": ab_h1.group(1).strip() if ab_h1 else "關於光盒影像",
        "intro1": ab_ps[0].strip() if len(ab_ps) > 0 else "光盒影像（ghspatial）專注於高階室內設計、建築場域與商業品牌視覺攝影。",
        "intro2": ab_ps[1].strip() if len(ab_ps) > 1 else "我們的拍攝核心在於「精準控光與自然還原」。",
        "stat1Num": "100%",
        "stat1Label": "專業控光與移軸透視",
        "stat2Num": "商業 & 住宅",
        "stat2Label": "高質感空間視覺拍攝",
        "stat3Num": "設計師信任",
        "stat3Label": "國際設計大獎作品紀錄"
    },
    "pricing": {
        "updatedAt": 1725116400000,
        "title": "價目表 | ghspatial 光盒影像",
        "heading": pr_h1.group(1).strip() if pr_h1 else "拍攝服務與預算規劃",
        "subheading": pr_sub.group(1).strip() if pr_sub else "依據空間坪數、拍攝類型與視覺需求提供專屬規劃",
        "plan1Name": "住宅室內設計拍攝",
        "plan1Desc": "專為室內設計師、軟裝團隊與住宅竣工大作紀錄打造。",
        "plan2Name": "商業空間與品牌攝影",
        "plan2Desc": "適合餐廳、門市、會所、旅宿與建築外觀形象宣傳。",
        "plan3Name": "社群氛圍素材拍攝",
        "plan3Desc": "專為咖啡館與獨立品牌打造，備齊高質感社群貼文視覺。"
    },
    "contact": {
        "updatedAt": 1725116400000,
        "title": "聯絡我 | ghspatial 光盒影像",
        "heading": ct_h1.group(1).strip() if ct_h1 else "預約與檔期諮詢",
        "subheading": ct_sub.group(1).strip() if ct_sub else "請填寫以下空間資訊表單，我們將於 24 小時內主動與您聯繫。"
    }
}

site_data_content = f"""/**
 * ghspatial 光盒影像 - 全站動態資料庫與智能比對引擎 (Site Data & Pre-Sync Diff Engine)
 */

window.GHSpatialDataDefault = {{
    version: "1.0.0",
    lastUpdated: 1725116400000,
    adminPassword: "168",

    pageContent: {json.dumps(page_content, ensure_ascii=False, indent=8)},

    projects: {json.dumps(projects_list, ensure_ascii=False, indent=8)}
}};

/**
 * 智能比對與無損合併引擎 (Pre-Sync Smart Diff & Merge Engine)
 */
window.GHSpatialDataEngine = {{
    STORAGE_KEY: "ghspatial_site_data_v1",

    getActiveData: function() {{
        const defaultData = window.GHSpatialDataDefault;
        const cachedRaw = localStorage.getItem(this.STORAGE_KEY);
        if (!cachedRaw) {{
            return defaultData;
        }}
        try {{
            const cachedData = JSON.parse(cachedRaw);
            return this.merge(defaultData, cachedData);
        }} catch (e) {{
            console.error("Failed to parse cached site data:", e);
            return defaultData;
        }}
    }},

    saveActiveData: function(data) {{
        data.lastUpdated = Date.now();
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
        return data;
    }},

    merge: function(baseData, incomingData) {{
        if (!incomingData) return baseData;
        
        const merged = {{
            version: incomingData.version || baseData.version,
            lastUpdated: Math.max(baseData.lastUpdated || 0, incomingData.lastUpdated || 0),
            adminPassword: incomingData.adminPassword || baseData.adminPassword,
            pageContent: {{}},
            projects: []
        }};

        const baseContent = baseData.pageContent || {{}};
        const inContent = incomingData.pageContent || {{}};
        const pages = Array.from(new Set([...Object.keys(baseContent), ...Object.keys(inContent)]));

        pages.forEach(pageKey => {{
            const basePage = baseContent[pageKey] || {{}};
            const inPage = inContent[pageKey] || {{}};
            if ((inPage.updatedAt || 0) >= (basePage.updatedAt || 0)) {{
                merged.pageContent[pageKey] = {{ ...basePage, ...inPage }};
            }} else {{
                merged.pageContent[pageKey] = {{ ...inPage, ...basePage }};
            }}
        }});

        const baseProjects = baseData.projects || [];
        const inProjects = incomingData.projects || [];
        const projectMap = new Map();

        baseProjects.forEach(p => {{
            projectMap.set(p.id, {{ ...p }});
        }});

        inProjects.forEach(inP => {{
            if (!projectMap.has(inP.id)) {{
                projectMap.set(inP.id, {{ ...inP }});
            }} else {{
                const baseP = projectMap.get(inP.id);
                if ((inP.updatedAt || 0) >= (baseP.updatedAt || 0)) {{
                    projectMap.set(inP.id, {{ ...baseP, ...inP }});
                }} else {{
                    projectMap.set(inP.id, {{ ...inP, ...baseP }});
                }}
            }}
        }});

        merged.projects = Array.from(projectMap.values());
        return merged;
    }},

    exportScriptContent: function(data) {{
        return "window.GHSpatialDataDefault = " + JSON.stringify(data, null, 4) + ";\\n";
    }}
}};
"""

with open(os.path.join(spatial_dir, "site_data.js"), "w", encoding="utf-8") as f:
    f.write(site_data_content)

print("site_data.js updated with ALL photos and exact HTML texts!")
