/**
 * ghspatial 光盒影像 - 全站動態資料庫與智能比對引擎 (Site Data & Pre-Sync Diff Engine)
 */

const space_photos = [
    "assets/cafe_social/space_09.jpg",
    "assets/cafe_social/space_01.jpg",
    "assets/cafe_social/space_02.jpg",
    "assets/cafe_social/space_03.jpg",
    "assets/cafe_social/space_04.jpg",
    "assets/cafe_social/space_05.jpg",
    "assets/cafe_social/space_06.jpg",
    "assets/cafe_social/space_07.jpg",
    "assets/cafe_social/space_08.jpg",
    "assets/cafe_social/space_10.jpg",
    "assets/cafe_social/space_11.jpg",
    "assets/cafe_social/space_12.jpg",
    "assets/cafe_social/space_13.jpg",
    "assets/cafe_social/space_14.jpg",
    "assets/cafe_social/space_15.jpg",
    "assets/cafe_social/space_16.jpg"
];

const food_photos = [
    "assets/cafe_social/food_01.jpg",
    "assets/cafe_social/food_02.jpg",
    "assets/cafe_social/food_03.jpg",
    "assets/cafe_social/food_04.jpg",
    "assets/cafe_social/food_05.jpg",
    "assets/cafe_social/food_06.jpg"
];

const cafePhotoTags = {};
space_photos.forEach(p => cafePhotoTags[p] = "空間氛圍");
food_photos.forEach(p => cafePhotoTags[p] = "食物");

window.GHSpatialDataDefault = {
    version: "1.1.0",
    lastUpdated: 1725116400000,
    adminPassword: "168",

    pageContent: {
        "index": {
            "updatedAt": 1725116400000,
            "title": "ghspatial 光盒影像 | Spatial Photography",
            "heroTitle": "ghspatial 光盒影像",
            "heroSubtitle": "High-end spatial and architectural photography by ghspatial 光盒影像.",
            "scrollText": "SCROLL"
        },
        "about": {
            "updatedAt": 1725116400000,
            "title": "關於光盒 | ghspatial",
            "heading": "關於光盒影像",
            "intro1": "光盒影像（ghspatial）專注於高階室內設計、建築場域與商業品牌視覺攝影。我們深知一幅優秀的空間作品，包含了設計師無數個日夜的雕琢與業主對生活的寄託。",
            "intro2": "我們的拍攝核心在於「精準控光與自然還原」。不使用誇張變形的超廣角干擾視野，而是透過專業移軸鏡頭與自然光影補光，捕捉垂直水平的結構幾何、材質紋理的微細觸感，以及空氣中流動的生活氛圍。",
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
        "heading": "拍攝方案",
        "subheading": "依據空間坪數、拍攝類型與視覺需求提供專屬規劃，歡迎預約諮詢",
        "featuredPlan": {
                "badge": "首次合作限定",
                "title": "設計師首次合作方案",
                "price": "請預約洽詢",
                "desc": "專為初次配合的設計團隊打造，以基本方案的價格，享有更充裕的拍攝時間與加碼照片。",
                "items": [
                        "現場拍攝 4 小時 (免費贈 1 小時軟裝微調)",
                        "高解析度精修圖 15 張 (加碼贈 3 張，等值 $3,600)",
                        "超時費可以折抵加挑照片之費用",
                        "專屬線上雲端圖庫供預覽與下載",
                        "10 個工作日提供挑片，挑片後 10 日交件"
                ]
        },
        "planSmall": {
                "title": "小坪數方案",
                "price": "$ 18,000",
                "desc": "我們最受歡迎的方案，適合單一空間或小型住宅案的完整紀錄，完美呈現你的設計細節。",
                "items": [
                        "現場拍攝最多 4 小時 (超時一小時 1200 元)",
                        "可挑選高解析度精修圖 15 張 (加挑張數 1200 元/張計費)",
                        "超時費可以折抵加挑照片之費用",
                        "專屬線上雲端圖庫供預覽與下載 (挑片檔僅供挑片不得轉載使用)",
                        "10 個工作日提供挑片檔案，挑片後 10 個工作日交付成品"
                ]
        },
        "planLarge": {
                "title": "大坪數方案",
                "price": "$ 36,000",
                "desc": "針對多空間、全戶設計或商業空間的深度拍攝，提供最完整的影像紀錄與最高規格的服務。",
                "items": [
                        "現場拍攝最多 8 小時 (全天超時一小時 1200 元)",
                        "可挑選高解析度精修圖 30 張 (加挑張數 1200 元/張計費)",
                        "超時費可以折抵加挑照片之費用",
                        "專屬線上雲端圖庫供預覽與下載 (挑片檔僅供挑片不得轉載使用)",
                        "含進階修圖與社群媒體適用尺寸"
                ]
        },
        "notes": [
                "上述報價為未稅價，拍攝計費以案場計算，不得多場合併計算。",
                "建築或競賽行拍攝價格另洽。",
                "檔期確認後會先預收 5000 元訂金，尾款為挑片確認張數後結算。",
                "目前僅提供平面拍攝服務，現場軟裝佈置需客戶自理，拍攝時會視情況調整現有擺設。",
                "拍攝前請客戶先行完成清潔及軟裝佈置，以免影響拍攝進度。",
                "為了維持客戶對環境顏色及燈光配置的原貌，拍攝方式會以現場光為主(不打攝影燈)，所以照片都會經過標準顏色校正及基本調光修片。但修片不包含變造及改變原拍攝物樣貌顏色或合成，如有特殊需求另行報價。",
                "交件時間約一個月內 (挑片時間不計)，實際交件期限會是淡旺季略調整。",
                "新竹市、竹北市以外車馬費另計：台南高雄 4000，台北彰雲嘉 3000，新北台中 2000，桃園苗栗 1000。宜花東其他地區及山區另洽。",
                "照片買斷版權及特殊時段外拍出機 (早上 7 點或晚上 9 點後) 費用另洽。",
                "拍攝期間如需過夜，客戶需負責提供相關工作人員食宿。",
                "攝影著作及其他著作權僅為光盒影像攝影師 郭耿宏 所有，客戶在自身行銷及宣傳等目的範圍內均可利用，但客戶不得將本著作權轉授權第三人利用。",
                "拍攝費用未付清或是票據未兌現前，攝影師保有該影像之所有權。"
        ],
        "process": [
                "填寫預約表單 (建議拍攝前一個月預約)",
                "雙方約定拍攝日期並確認相關拍攝資訊",
                "收取拍攝訂金 5000 元以保留檔期",
                "請客戶提供現場照片或影片 (手機拍攝即可)，如有模擬圖也請提供攝影師了解空間樣貌",
                "執行拍攝 (如遇不可抗力之因素需延期，請於 2 週前告知)",
                "「挑片檔」於拍攝後約 2 週提供客戶挑片使用",
                "「交件檔」於客戶挑片後約 2-3 週提雲端下載並作確認",
                "拍攝尾款請於交件前結清費用，如客戶有固定請款作業請事先告知"
        ]
},
        "contact": {
            "updatedAt": 1725116400000,
            "title": "聯絡我 | ghspatial 光盒影像",
            "heading": "預約與檔期諮詢",
            "subheading": "請填寫以下空間資訊表單，我們將於 24 小時內主動與您聯繫。"
        }
    },

    projects: [
        {
            "id": "proj_cafe_social",
            "updatedAt": 1725116400000,
            "title": "咖啡廳社群氛圍素材",
            "subtitle": "空間氛圍 ｜ 食物與餐點",
            "category": "cafe",
            "categoryName": "社群素材",
            "coverImg": "assets/cafe_social/space_09.jpg",
            "link": "cafe_social.html",
            "subcategories": ["空間氛圍", "食物"],
            "photoTags": cafePhotoTags,
            "photos": [...space_photos, ...food_photos]
        },
        {
            "id": "proj_keelung",
            "updatedAt": 1725116400000,
            "title": "兩房公寓溫馨宅_基隆",
            "subtitle": "軟裝設計",
            "category": "residential",
            "categoryName": "住宅室內",
            "coverImg": "assets/keelung/基隆櫻桃家小圖-7.jpg",
            "link": "keelung.html",
            "photos": [
                "assets/keelung/基隆櫻桃家小圖-7.jpg", "assets/keelung/基隆櫻桃家小圖-1.jpg", "assets/keelung/基隆櫻桃家小圖-2.jpg", "assets/keelung/基隆櫻桃家小圖-3.jpg", "assets/keelung/基隆櫻桃家小圖-4.jpg", "assets/keelung/基隆櫻桃家小圖-5.jpg", "assets/keelung/基隆櫻桃家小圖-6.jpg", "assets/keelung/基隆櫻桃家小圖-8.jpg", "assets/keelung/基隆櫻桃家小圖-9.jpg", "assets/keelung/基隆櫻桃家小圖-10.jpg", "assets/keelung/基隆櫻桃家小圖-11.jpg", "assets/keelung/基隆櫻桃家小圖-12.jpg", "assets/keelung/基隆櫻桃家小圖-13.jpg", "assets/keelung/基隆櫻桃家小圖-14.jpg", "assets/keelung/基隆櫻桃家小圖-15.jpg", "assets/keelung/基隆櫻桃家小圖-16.jpg", "assets/keelung/基隆櫻桃家小圖-17.jpg", "assets/keelung/基隆櫻桃家小圖-18.jpg", "assets/keelung/基隆櫻桃家小圖-19.jpg", "assets/keelung/基隆櫻桃家小圖-20.jpg", "assets/keelung/基隆櫻桃家小圖-21.jpg"
            ]
        },
        {
            "id": "proj_roman_holiday",
            "updatedAt": 1725116400000,
            "title": "精緻小宅_羅馬假期內湖",
            "subtitle": "鼎禾設計",
            "category": "residential",
            "categoryName": "住宅室內",
            "coverImg": "assets/roman_holiday/DSC02068-HDR.jpg",
            "link": "roman_holiday.html",
            "photos": [
                "assets/roman_holiday/DSC02068-HDR.jpg", "assets/roman_holiday/DSC02035-HDR.jpg", "assets/roman_holiday/DSC02044-HDR.jpg", "assets/roman_holiday/DSC02050-HDR.jpg", "assets/roman_holiday/DSC02056-HDR.jpg", "assets/roman_holiday/DSC02062-HDR.jpg", "assets/roman_holiday/DSC02074-HDR.jpg", "assets/roman_holiday/DSC02080-HDR.jpg", "assets/roman_holiday/DSC02086-HDR.jpg", "assets/roman_holiday/DSC02092-HDR.jpg", "assets/roman_holiday/DSC02098-HDR.jpg", "assets/roman_holiday/DSC02104-HDR.jpg", "assets/roman_holiday/DSC02110-HDR.jpg", "assets/roman_holiday/DSC02116-HDR.jpg", "assets/roman_holiday/DSC02122-HDR.jpg"
            ]
        },
        {
            "id": "proj_pan_pan",
            "updatedAt": 1725116400000,
            "title": "透天建案_盼盼湖口",
            "subtitle": "湖口 ｜ 立得建設",
            "category": "architecture",
            "categoryName": "建築透天",
            "coverImg": "assets/pan_pan/立得建設-盼盼-18.jpg",
            "link": "pan_pan.html",
            "photos": [
                "assets/pan_pan/立得建設-盼盼-18.jpg", "assets/pan_pan/立得建設-盼盼-1.jpg", "assets/pan_pan/立得建設-盼盼-2.jpg", "assets/pan_pan/立得建設-盼盼-3.jpg", "assets/pan_pan/立得建設-盼盼-4.jpg", "assets/pan_pan/立得建設-盼盼-5.jpg", "assets/pan_pan/立得建設-盼盼-6.jpg", "assets/pan_pan/立得建設-盼盼-7.jpg", "assets/pan_pan/立得建設-盼盼-8.jpg", "assets/pan_pan/立得建設-盼盼-9.jpg", "assets/pan_pan/立得建設-盼盼-10.jpg", "assets/pan_pan/立得建設-盼盼-11.jpg", "assets/pan_pan/立得建設-盼盼-12.jpg", "assets/pan_pan/立得建設-盼盼-13.jpg", "assets/pan_pan/立得建設-盼盼-14.jpg", "assets/pan_pan/立得建設-盼盼-15.jpg", "assets/pan_pan/立得建設-盼盼-16.jpg", "assets/pan_pan/立得建設-盼盼-17.jpg", "assets/pan_pan/立得建設-盼盼-19.jpg", "assets/pan_pan/立得建設-盼盼-20.jpg", "assets/pan_pan/立得建設-盼盼-21.jpg"
            ]
        },
        {
            "id": "proj_fifi",
            "updatedAt": 1725116400000,
            "title": "軟裝設計_台中",
            "subtitle": "FIFI DECO",
            "category": "residential",
            "categoryName": "軟裝陳設",
            "coverImg": "assets/fifi/DSC02946.jpg",
            "link": "fifi.html",
            "photos": [
                "assets/fifi/DSC02946.jpg", "assets/fifi/DSC02952.jpg", "assets/fifi/DSC02958.jpg", "assets/fifi/DSC02964.jpg", "assets/fifi/DSC02970.jpg", "assets/fifi/DSC02976.jpg"
            ]
        },
        {
            "id": "proj_luoyushan",
            "updatedAt": 1725116400000,
            "title": "豪宅_落餘山竹北",
            "subtitle": "竹北",
            "category": "residential",
            "categoryName": "住宅豪宅",
            "coverImg": "assets/luoyushan/A1_06285-編輯.jpg",
            "link": "luoyushan.html",
            "photos": [
                "assets/luoyushan/A1_06285-編輯.jpg", "assets/luoyushan/A1_06290-編輯.jpg", "assets/luoyushan/A1_06295-編輯.jpg", "assets/luoyushan/A1_06300-編輯.jpg", "assets/luoyushan/A1_06305-編輯.jpg", "assets/luoyushan/A1_06310-編輯.jpg", "assets/luoyushan/A1_06315-編輯.jpg"
            ]
        },
        {
            "id": "proj_underpass",
            "updatedAt": 1725116400000,
            "title": "中正東路地下道",
            "subtitle": "竹北 ｜ 公共工程紀錄",
            "category": "architecture",
            "categoryName": "公共建築",
            "coverImg": "assets/underpass/A1_06184.jpg",
            "link": "underpass.html",
            "photos": [
                "assets/underpass/A1_06184.jpg", "assets/underpass/A1_06189.jpg", "assets/underpass/A1_06194.jpg", "assets/underpass/A1_06199.jpg", "assets/underpass/A1_06204.jpg", "assets/underpass/A1_06209.jpg", "assets/underpass/A1_06214.jpg", "assets/underpass/A1_06219.jpg", "assets/underpass/A1_06224.jpg", "assets/underpass/A1_06229.jpg", "assets/underpass/A1_06234.jpg", "assets/underpass/A1_06239.jpg", "assets/underpass/A1_06244.jpg"
            ]
        },
        {
            "id": "proj_xinwu",
            "updatedAt": 1725116400000,
            "title": "現場展覽_桃園新屋",
            "subtitle": "展覽空間",
            "category": "commercial",
            "categoryName": "商業展覽",
            "coverImg": "assets/xinwu/A1_07932.jpg",
            "link": "xinwu.html",
            "photos": [
                "assets/xinwu/A1_07932.jpg", "assets/xinwu/A1_07937.jpg", "assets/xinwu/A1_07942.jpg", "assets/xinwu/A1_07947.jpg", "assets/xinwu/A1_07952.jpg", "assets/xinwu/A1_07957.jpg", "assets/xinwu/A1_07962.jpg", "assets/xinwu/A1_07967.jpg", "assets/xinwu/A1_07972.jpg", "assets/xinwu/A1_07977.jpg"
            ]
        },
        {
            "id": "proj_kualalumpur",
            "updatedAt": 1725116400000,
            "title": "建築巡禮_吉隆坡",
            "subtitle": "馬來西亞",
            "category": "architecture",
            "categoryName": "建築巡禮",
            "coverImg": "assets/kualalumpur/DSC06629.jpg",
            "link": "kualalumpur.html",
            "photos": [
                "assets/kualalumpur/DSC06629.jpg", "assets/kualalumpur/DSC06634.jpg", "assets/kualalumpur/DSC06639.jpg", "assets/kualalumpur/DSC06644.jpg", "assets/kualalumpur/DSC06649.jpg", "assets/kualalumpur/DSC06654.jpg", "assets/kualalumpur/DSC06659.jpg", "assets/kualalumpur/DSC06664.jpg", "assets/kualalumpur/DSC06669.jpg", "assets/kualalumpur/DSC06674.jpg", "assets/kualalumpur/DSC06679.jpg", "assets/kualalumpur/DSC06684.jpg", "assets/kualalumpur/DSC06689.jpg", "assets/kualalumpur/DSC06694.jpg", "assets/kualalumpur/DSC06699.jpg", "assets/kualalumpur/DSC06704.jpg", "assets/kualalumpur/DSC06709.jpg"
            ]
        }
    ],

    zhubeiPhotos: [
        "assets/zhubei_series/328.png",
        "assets/zhubei_series/composecoffe.png",
        "assets/zhubei_series/keu日本抹茶.jpg",
        "assets/zhubei_series/光鮮綠蔬.png",
        "assets/zhubei_series/卷卷烘焙.png",
        "assets/zhubei_series/坤山君峰.png",
        "assets/zhubei_series/客肉.png",
        "assets/zhubei_series/客肉2.png",
        "assets/zhubei_series/平室.png",
        "assets/zhubei_series/星球公園.png",
        "assets/zhubei_series/橋恩咖啡.png",
        "assets/zhubei_series/民宅樹影.png",
        "assets/zhubei_series/瓦法.png",
        "assets/zhubei_series/瓦法局部.png",
        "assets/zhubei_series/若一設計.png",
        "assets/zhubei_series/若一設計角落.png",
        "assets/zhubei_series/茶棧.png",
        "assets/zhubei_series/藍佐牛排.png",
        "assets/zhubei_series/蘭英麵食館六家店.png",
        "assets/zhubei_series/隱焱匠.png"
    ]
};

/**
 * 智能比對與無損合併引擎 (Pre-Sync Smart Diff & Merge Engine)
 */
window.GHSpatialDataEngine = {
    STORAGE_KEY: "ghspatial_site_data_v1",

    getActiveData: function() {
        const defaultData = window.GHSpatialDataDefault;
        const cachedRaw = localStorage.getItem(this.STORAGE_KEY);
        if (!cachedRaw) {
            return defaultData;
        }
        try {
            const cachedData = JSON.parse(cachedRaw);
            return this.merge(defaultData, cachedData);
        } catch (e) {
            console.error("Failed to parse cached site data:", e);
            return defaultData;
        }
    },

    saveActiveData: function(data) {
        data.lastUpdated = Date.now();
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
        return data;
    },

    merge: function(baseData, incomingData) {
        if (!incomingData) return baseData;
        
        const merged = {
            version: incomingData.version || baseData.version,
            lastUpdated: Math.max(baseData.lastUpdated || 0, incomingData.lastUpdated || 0),
            adminPassword: incomingData.adminPassword || baseData.adminPassword,
            pageContent: {},
            projects: [],
            zhubeiPhotos: baseData.zhubeiPhotos || []
        };

        const baseContent = baseData.pageContent || {};
        const inContent = incomingData.pageContent || {};
        const pages = Array.from(new Set([...Object.keys(baseContent), ...Object.keys(inContent)]));

        pages.forEach(pageKey => {
            const basePage = baseContent[pageKey] || {};
            const inPage = inContent[pageKey] || {};
            if ((inPage.updatedAt || 0) >= (basePage.updatedAt || 0)) {
                merged.pageContent[pageKey] = { ...basePage, ...inPage };
            } else {
                merged.pageContent[pageKey] = { ...inPage, ...basePage };
            }
        });

        const baseProjects = baseData.projects || [];
        const inProjects = incomingData.projects || [];
        const projectMap = new Map();

        baseProjects.forEach(p => {
            projectMap.set(p.id, { ...p });
        });

        inProjects.forEach(inP => {
            if (!projectMap.has(inP.id)) {
                projectMap.set(inP.id, { ...inP });
            } else {
                const baseP = projectMap.get(inP.id);
                if ((inP.updatedAt || 0) >= (baseP.updatedAt || 0)) {
                    projectMap.set(inP.id, { ...baseP, ...inP });
                } else {
                    projectMap.set(inP.id, { ...inP, ...baseP });
                }
            }
        });

        merged.projects = Array.from(projectMap.values());

        // Merge zhubeiSeries
        const baseSeries = baseData.zhubeiSeries || [];
        const inSeries = incomingData.zhubeiSeries || [];
        const seriesMap = new Map();

        baseSeries.forEach(s => seriesMap.set(s.id, { ...s }));
        inSeries.forEach(inS => {
            if (!seriesMap.has(inS.id)) {
                seriesMap.set(inS.id, { ...inS });
            } else {
                const baseS = seriesMap.get(inS.id);
                if ((inS.updatedAt || 0) >= (baseS.updatedAt || 0)) {
                    seriesMap.set(inS.id, { ...baseS, ...inS });
                } else {
                    seriesMap.set(inS.id, { ...inS, ...baseS });
                }
            }
        });
        merged.zhubeiSeries = Array.from(seriesMap.values());

        return merged;
    },

    exportScriptContent: function(data) {
        return "window.GHSpatialDataDefault = " + JSON.stringify(data, null, 4) + ";\n";
    }
};
