import os

html_dir = "/Users/kuoamos/.gemini/antigravity/scratch/spatial-portfolio/"

# 1. Update pricing.html
pricing_path = os.path.join(html_dir, "pricing.html")
if os.path.exists(pricing_path):
    with open(pricing_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix the backslash issue
    content = content.replace('class=\\"price\\"', 'class="price"')
    
    # Update title
    content = content.replace('<h3>首次合作升級方案</h3>', '<h3>設計師首次合作方案</h3>')
    
    # Update price text
    content = content.replace(
        '<div class="price" style="font-size: 42px; font-weight: 500; letter-spacing: 4px; font-family: \'Noto Sans TC\', sans-serif;">依專案需求報價</div>',
        '<div class="price" style="font-size: 42px; font-weight: 500; letter-spacing: 4px; font-family: \'Noto Sans TC\', sans-serif;">請預約洽詢</div>'
    )
    
    with open(pricing_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Update ig_story_promo.html
ig_promo_path = os.path.join(html_dir, "ig_stories/ig_story_promo.html")
if os.path.exists(ig_promo_path):
    with open(ig_promo_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update title
    content = content.replace('<h1>首次合作升級方案</h1>', '<h1>設計師首次合作方案</h1>')
    
    # Update price text
    content = content.replace(
        '<div class="price" style="font-size: 48px; font-family: \'Noto Sans TC\', sans-serif; font-weight: 500; letter-spacing: 6px;">依專案內容專屬報價</div>',
        '<div class="price" style="font-size: 48px; font-family: \'Noto Sans TC\', sans-serif; font-weight: 500; letter-spacing: 6px;">請預約洽詢</div>'
    )
    
    with open(ig_promo_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Adjustments applied successfully.")
