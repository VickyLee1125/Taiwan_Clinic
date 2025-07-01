# -*- coding: utf-8 -*-
"""
Created on Fri May 30 18:04:29 2025
讀取112年的人口與土地面積資料並清理
@author: ctlop
"""
def city_people_data():
    import pandas as pd
    
    # 讀取112年的人口與土地面積
    df_pop112 = pd.read_excel("../open_data/鄉鎮土地面積及人口密度.xls", engine="xlrd")

    #定義要保留的縣市清單    
    area_list = [
        "新北市", "臺北市", "桃園市", "臺中市", "臺南市", "高雄市",
        "宜蘭縣", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣",
        "嘉義縣", "屏東縣", "臺東縣", "花蓮縣", "澎湖縣", "基隆市",
        "新竹市", "嘉義市", "金門縣", "連江縣"
    ]
        
    #清理第一欄的欄位中的所有值空白。regex=True:啟用正則表達式模式
    df_pop112.iloc[:,0] = df_pop112.iloc[:,0].astype(str).str.replace(r"\s+", "", regex=True)

    # 第1列的內容設為 DataFrame 的欄位名稱（標題列)
    df_pop112.columns = df_pop112.iloc[1]
    df_pop112 = df_pop112.iloc[3:27]
    # 濾出"區域別"欄位屬於 area_list 中的縣市資料，重設索引值
    df_pop112 = df_pop112[df_pop112["區域別"].isin(area_list)].reset_index(drop=True)

    
    # 確定沒有空值，可以再轉成 int
    df_pop112["年底人口數"] = df_pop112["年底人口數"].astype("Int64")  # 支援 NaN 的整數型
    df_pop112["人口密度"] = df_pop112["人口密度"].astype("float")
    df_pop112["土地面積"] = df_pop112["土地面積"].astype("float")

    return df_pop112


