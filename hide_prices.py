import os

html_dir = "/Users/kuoamos/.gemini/antigravity/scratch/spatial-portfolio/"

# 1. Update pricing.html
pricing_path = os.path.join(html_dir, "pricing.html")
if os.path.exists(pricing_path):
    with open(pricing_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(
        '<div class="price">$ 18,000<span> / 元</span></div>',
        '<div class="price" style="font-size: 42px; font-weight: 500; letter-spacing: 4px; font-family: \'Noto Sans TC\', sans-serif;">依專案需求報價</div>'
    )
    content = content.replace(
        '<div class="price">$ 36,000<span> / 元</span></div>',
        '<div class="price" style="font-size: 42px; font-weight: 500; letter-spacing: 4px; font-family: \'Noto Sans TC\', sans-serif;">依專案需求報價</div>'
    )
    
    with open(pricing_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Update ig_story_pricing.html
ig_pricing_path = os.path.join(html_dir, "ig_stories/ig_story_pricing.html")
if os.path.exists(ig_pricing_path):
    with open(ig_pricing_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(
        '<div class="item-desc" style="color: #111; font-size: 36px; margin-bottom: 10px; font-weight: 500;">$ 18,000 / 元</div>',
        '<div class="item-desc" style="color: #111; font-size: 32px; margin-bottom: 10px; font-weight: 500;">報價請私訊洽詢</div>'
    )
    content = content.replace(
        '<div class="item-desc" style="color: #111; font-size: 36px; margin-bottom: 10px; font-weight: 500;">$ 36,000 / 元</div>',
        '<div class="item-desc" style="color: #111; font-size: 32px; margin-bottom: 10px; font-weight: 500;">報價請私訊洽詢</div>'
    )
    
    with open(ig_pricing_path, "w", encoding="utf-8") as f:
        f.write(content)

# 3. Update ig_story_promo.html
ig_promo_path = os.path.join(html_dir, "ig_stories/ig_story_promo.html")
if os.path.exists(ig_promo_path):
    with open(ig_promo_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(
        '<div class="price">$ 18,000<span> / 元</span></div>',
        '<div class="price" style="font-size: 48px; font-family: \'Noto Sans TC\', sans-serif; font-weight: 500; letter-spacing: 6px;">依專案內容專屬報價</div>'
    )
    
    with open(ig_promo_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated prices successfully.")
