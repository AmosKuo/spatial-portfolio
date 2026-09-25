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
            "updatedAt": 1789750000000,
            "title": "價目表 | GH Spatial 空間攝影",
            "heading": "GH Spatial｜空間攝影專案報價",
            "subheading": "專業空間與建築攝影服務，依據空間坪數與視覺需求提供專屬規劃",
            "featuredPlan": {
                "badge": "首次合作限定",
                "title": "設計師首次合作｜打樣方案",
                "price": "NT$12,000",
                "desc": "限首次合作之設計團隊，每個團隊限使用一次。",
                "items": [
                    "拍攝時間：4 小時內",
                    "交付照片：15 張精修圖"
                ]
            },
            "planSmall": {
                "title": "25 坪內｜標準方案",
                "price": "NT$18,000",
                "desc": "適合 25 坪內單一空間或小型住宅案完整紀錄。",
                "items": [
                    "拍攝時間：4 小時內",
                    "交付照片：15 張精修圖"
                ]
            },
            "planMedium": {
                "title": "26–49 坪｜經典方案",
                "price": "NT$25,000",
                "desc": "完整紀錄標準三至四房空間設計細節。",
                "items": [
                    "拍攝時間：6 小時內",
                    "交付照片：20–25 張精修圖"
                ]
            },
            "planLarge": {
                "title": "50 坪以上｜旗艦方案",
                "price": "NT$32,000",
                "desc": "針對大坪數豪宅與多空間深度拍攝，確保角落光影極致呈現。",
                "items": [
                    "拍攝時間：8 小時內",
                    "交付照片：30–40 張精修圖"
                ]
            },
            "notes": [
                "【加購與超時】精修照片加購：NT$1,200／張。超過方案拍攝時間後，超時費為 NT$1,200／小時。若產生超時費，可全額折抵加購照片費用，將超時成本轉為照片資產。若案場坪數略超過方案範圍，但空間動線單純、拍攝進度順利，且未超過方案時數，將視現場狀況評估是否維持原方案價格。",
                "【拍攝方式】以自然光及現場燈光為主要拍攝基礎，透過現場光影調整，呈現空間的材質、比例與氛圍。拍攝前請完成：空間清潔、軟裝配置、物件整理。如需空間短影音或其他動態影像，另行報價。",
                "【照片交付】拍攝完成後 10 個工作日內提供照片預覽。確認照片後，於 10 個工作日內交付最終精修大檔。基本修圖包含：曝光與白平衡調整、色彩校正、明暗與光影調整、透視及垂直線校正。如需移除物件、改變空間樣貌或特殊合成，另行報價。",
                "【使用授權】攝影著作權歸 GH Spatial／耿宏所有。客戶於付清款項後，可無限期使用交付照片於自身品牌、作品集、網站及社群等行銷用途。不得將照片轉授權予第三方使用。如有建築競賽、出版、媒體使用或著作權買斷需求，另行洽談。"
            ],
            "process": [
                "建議於拍攝前 1 個月預約。",
                "確認檔期後，收取 NT$5,000 訂金以保留拍攝時段。",
                "拍攝前請提供：現場手機照片、平面圖／配置圖（如有）、3D 模擬圖（如有）。",
                "執行專案拍攝與現場光影調度。",
                "拍攝完成後 10 個工作日內提供照片預覽。",
                "確認照片後，於 10 個工作日內交付最終精修大檔。",
                "尾款於最終照片交付前結清 (如有企業固定請款流程，請於預約時提前告知)。",
                "交通費說明：新竹縣市 免費 ｜ 桃園／苗栗 NT$1,000 ｜ 新北／台中 NT$2,000 ｜ 台北／彰化／雲林／嘉義 NT$3,000 ｜ 台南／高雄 NT$4,000 (其他地區另行報價)。"
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
        "assets/zhubei_series/RD理髮.png",
        "assets/zhubei_series/composecoffe.png",
        "assets/zhubei_series/keu日本抹茶.jpg",
        "assets/zhubei_series/sejr1.png",
        "assets/zhubei_series/sejr2.png",
        "assets/zhubei_series/sejr3.png",
        "assets/zhubei_series/光明六路夕陽黑白.png",
        "assets/zhubei_series/光鮮綠蔬.png",
        "assets/zhubei_series/出口咖啡1.png",
        "assets/zhubei_series/出口咖啡2.png",
        "assets/zhubei_series/出口咖啡3.png",
        "assets/zhubei_series/出口咖啡4.png",
        "assets/zhubei_series/卷卷烘焙.png",
        "assets/zhubei_series/坤山君峰.png",
        "assets/zhubei_series/客肉.png",
        "assets/zhubei_series/客肉2.png",
        "assets/zhubei_series/巢二居理髮.png",
        "assets/zhubei_series/平室.png",
        "assets/zhubei_series/德鑫當代.png",
        "assets/zhubei_series/星球公園.png",
        "assets/zhubei_series/時代花園側.png",
        "assets/zhubei_series/時代花園大廈.png",
        "assets/zhubei_series/普林司肯咖啡.png",
        "assets/zhubei_series/椰林掬.png",
        "assets/zhubei_series/橋恩咖啡.png",
        "assets/zhubei_series/民宅樹影.png",
        "assets/zhubei_series/瓦法.png",
        "assets/zhubei_series/瓦法局部.png",
        "assets/zhubei_series/田厝街華廈.png",
        "assets/zhubei_series/白色花崗岩公寓.png",
        "assets/zhubei_series/空間攝影貼文.png",
        "assets/zhubei_series/竹北清潔車.png",
        "assets/zhubei_series/縣福公園1.png",
        "assets/zhubei_series/縣福公園2.png",
        "assets/zhubei_series/若一設計.png",
        "assets/zhubei_series/若一設計角落.png",
        "assets/zhubei_series/茶棧.png",
        "assets/zhubei_series/藍佐牛排.png",
        "assets/zhubei_series/蘭英麵食館六家店.png",
        "assets/zhubei_series/隘口新房子1.png",
        "assets/zhubei_series/隘口新房子2.png",
        "assets/zhubei_series/隘口新房子3.png",
        "assets/zhubei_series/隱焱匠.png",
        "assets/zhubei_series/馥邸橫.png",
        "assets/zhubei_series/馥邸直.png"
],

    cafePackagePhotos: [
        "assets/zhubei_series/composecoffe.png",
        "assets/zhubei_series/keu日本抹茶.jpg",
        "assets/zhubei_series/橋恩咖啡.png",
        "assets/zhubei_series/卷卷烘焙.png",
        "assets/zhubei_series/瓦法.png",
        "assets/zhubei_series/瓦法局部.png",
        "assets/zhubei_series/藍佐牛排.png",
        "assets/zhubei_series/隱焱匠.png",
        "assets/cafe_social/space_09.jpg",
        "assets/cafe_social/space_02.jpg",
        "assets/cafe_social/food_01.jpg",
        "assets/cafe_social/food_04.jpg"
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
            zhubeiPhotos: Array.from(new Set([...(baseData.zhubeiPhotos || []), ...(incomingData.zhubeiPhotos || [])])),
            cafePackagePhotos: incomingData.cafePackagePhotos || baseData.cafePackagePhotos || []
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
