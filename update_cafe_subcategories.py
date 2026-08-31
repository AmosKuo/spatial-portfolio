import os, json

site_data_path = "/Users/kuoamos/Desktop/spatial-portfolio/site_data.js"

with open(site_data_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update GHSpatialDataDefault cafe project to include categorized subcategories and photo tags
space_photos = [f"assets/cafe_social/space_{i:02d}.jpg" for i in [9, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16]]
food_photos = [f"assets/cafe_social/food_{i:02d}.jpg" for i in range(1, 7)]

cafe_project_structured = {
    "id": "proj_cafe_social",
    "updatedAt": 1725116400000,
    "title": "咖啡廳社群氛圍素材",
    "subtitle": "空間氛圍 ｜ 食物與餐點",
    "category": "cafe",
    "categoryName": "社群素材",
    "coverImg": "assets/cafe_social/space_09.jpg",
    "link": "cafe_social.html",
    "subcategories": [
        { "id": "sub_space", "name": "空間氛圍", "photos": space_photos },
        { "id": "sub_food", "name": "食物", "photos": food_photos }
    ],
    "photos": space_photos + food_photos,
    "photoTags": {}
}

for p in space_photos:
    cafe_project_structured["photoTags"][p] = "空間氛圍"
for p in food_photos:
    cafe_project_structured["photoTags"][p] = "食物"

print("Categorized 16 Space photos and 6 Food photos successfully.")
