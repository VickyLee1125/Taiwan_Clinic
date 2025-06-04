# -*- coding: utf-8 -*-
"""
Created on Fri May 30 18:04:29 2025
讀取清理人口數據(O)
@author: ctlop
"""
def city_people_data():
    import pandas as pd
    
    # 讀取所有工作表
    xls = pd.read_excel("./open_data/鄉鎮土地面積及人口密度.xls", sheet_name=None, engine="xlrd")
    
    # 顯示所有工作表名稱
    print(xls.keys())
    area_list = [
        "新北市", "臺北市", "桃園市", "臺中市", "臺南市", "高雄市",
        "宜蘭縣", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣",
        "嘉義縣", "屏東縣", "臺東縣", "花蓮縣", "澎湖縣", "基隆市",
        "新竹市", "嘉義市", "金門縣", "連江縣"
    ]
    
    
    # 取出某一個工作表的資料，例如第一個
    df = xls[list(xls.keys())[0]]
    df.iloc[:,0] = df.iloc[:,0].astype(str).str.replace(r"\s+", "", regex=True)
    df.columns = df.iloc[1]
    df = df.iloc[3:27]
    df = df[df["區域別"].isin(area_list)].reset_index(drop=True).copy()
    # 安全轉換人口欄位為數值型態（強制清理）
    df["年底人口數"] = (
        pd.to_numeric(df["年底人口數"]
                      .astype(str)
                      .str.replace(",", "")
                      .str.replace(" ", ""),
                      errors="coerce")  # 若不能轉換為數字，會變成 NaN
    )
    
    # 若你確定沒有空值，可以再轉成 int
    df["年底人口數"] = df["年底人口數"].astype("Int64")  # 支援 NaN 的整數型
    # df["土地面積","人口密度"] = df["土地面積","人口密度"].astype("float")  # 支援 NaN 的整數型
    df["人口密度"] = df["人口密度"].astype("float")
    df["土地面積"] = df["土地面積"].astype("float")
    df = df.iloc[:,0:4].copy()
    return df


