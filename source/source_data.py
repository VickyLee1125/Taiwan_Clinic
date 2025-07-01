# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:28:38 2025

功能說明:
01. load_and_process_clinic_data()  
    讀取 2019-2023 年診所資料，合併縣市資訊，回傳完整 DataFrame。
    
02. get_clinic_remove_total_data() 
    整理「各縣市 每年 各科別診所家數」的長表格，拿掉總診所家數。

03. get_clinic_with_total_data()
    整理「各縣市 每年 總診所家數」表格，無分科別。

回傳:   
    clinic_area_df (pd.DataFrame)
    melted_df (pd.DataFrame)
    city_year_summary_df (pd.DataFrame)
    
@author: USER
"""
import pandas as pd
import matplotlib.pyplot as plt

# 彙整 2019–2023 年診所統計資料，加上縣市欄位。
def load_and_process_clinic_data():     
    # 設定 matplotlib 支援中文
    plt.rcParams["font.family"] = "Microsoft JhengHei" 

    # 建立空的 DataFrame，準備累加每年的資料
    clinic_df = pd.DataFrame()
    
    # 迴圈讀取 108~112 年的診所資料 (民國)
    for year in range(108, 113):
        file_path = f"../open_data/{year}年診所科別統計/clinic_sp{year}.csv"
        try:
            # 讀取 CSV，轉為 DataFrame
            df = pd.read_csv(file_path, encoding="big5")
            
            # 插入 'Year' 欄位，民國轉西元
            df.insert(0, "Year", year + 1911) 
            
            # 把讀到的 DataFrame 加到 clinic_df 裡
            clinic_df = pd.concat([clinic_df, df], ignore_index=True)
            
        except FileNotFoundError:
            print(f"找不到檔案：{file_path}")
            
    # 補齊空值欄位，填 0，處理有些年份缺科別       
    clinic_df = clinic_df.fillna(0)
    
    # 讀取行政區碼對照表 (欄位說明檔)
    area_info_df = pd.read_csv("../open_data/112年診所科別統計/欄位說明.csv")
    # 取每個字串的前 3 個字元，並存成新欄位 '縣市'。
    area_info_df['縣市'] = area_info_df['鄉鎮市區名稱(103年以後適用)'].str[:3]
    
    # 合併2筆資料表(以鄉鎮市區碼)
    df_total = clinic_df.merge(
        area_info_df[["鄉鎮市區碼", "縣市"]],
        how='left',
        on='鄉鎮市區碼'
    )    
    return df_total

#取得「各縣市每年 各科別家數」的長表格（不含總診所家數）
def get_clinic_remove_total_data():
    # 呼叫上面 load 函數，先取得原始資料
    df_total = load_and_process_clinic_data()    

    Departments_df = df_total.copy()
    
    # 調整欄位順序，把 "縣市" 欄排到第 2 欄，並移除不需要的欄位
    cols = Departments_df.columns.tolist()
    cols.insert(1, "縣市")    # 插到第二欄位置
    Departments_df = Departments_df[cols]
    Departments_df = Departments_df.drop(columns=["鄉鎮市區碼","診所家數"])
    Departments_df = Departments_df.iloc[:, :-1] 
     
    # 寬轉長表格，melt融合各科別
    Departments_df = Departments_df.melt(
        id_vars=["Year", "縣市"],     # 這 3 欄固定保留
        var_name="科別",              # 科別名稱 → 欄位名
        value_name="家數"             # 數值 → 家數
        )
    
    return Departments_df


#取得「各縣市每年 的總診所家數」，不區分科別。
def get_clinic_with_total_data():
    df_total = load_and_process_clinic_data()
    
    # 調整欄位順序
    new_order = ["Year","縣市", "診所家數"]
    clinic_total_df = df_total[new_order].copy()
    
    # 各縣市每年診所總數
    # 依「縣市 ＋ Year」做groupby，加總診所家數
    city_year_df = (
        clinic_total_df
        .groupby(["縣市", "Year"])["診所家數"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    
    return city_year_df