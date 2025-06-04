# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:28:38 2025
01. 讀取診所資料（2019-2023）並彙整
02. 合併鄉鎮市區碼對應的縣市與區域名稱
03. 資料轉長格式後，回傳整理後的 DataFrame 供分析使用
@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_and_process_clinic_data():
    """
    讀取多年份的診所科別統計資料，合併區域資訊並轉為長格式資料表。
    
    Returns:
        melted_df (pd.DataFrame): 轉為長格式後的診所資料（包含科別與家數）。
        city_year_summary_df (pd.DataFrame): 各縣市每年總診所家數的統計。
    """
    
    # 設定 matplotlib 支援中文
    plt.rcParams["font.family"] = "Microsoft JhengHei"
    plt.rcParams["font.size"] = 10
    plt.rcParams["axes.unicode_minus"] = False

    # 彙整各年份診所資料
    clinic_df = pd.DataFrame()
    for year in range(108, 113):
        file_path = f"./open_data/{year}年診所科別統計/clinic_sp{year}.csv"
        try:
            df = pd.read_csv(file_path, encoding="big5")
            df.insert(0, "Year", year + 1911)  # 民國轉西元
            clinic_df = pd.concat([clinic_df, df], ignore_index=True)
        except FileNotFoundError:
            print(f"找不到檔案：{file_path}")

    # 載入行政區碼對照資料，並切割出縣市與區域
    area_info_df = pd.read_csv("./open_data/112年診所科別統計/欄位說明.csv")
    area_info_df['縣市'] = area_info_df['鄉鎮市區名稱(103年以後適用)'].str[:3]
    area_info_df['區域'] = area_info_df['鄉鎮市區名稱(103年以後適用)'].str[3:]

    # 合併行政區資料
    clinic_df = clinic_df.fillna(0)
    clinic_area_df = clinic_df.merge(
        area_info_df[["鄉鎮市區碼", "縣市", "區域"]],
        how='left',
        on='鄉鎮市區碼'
    )
    
    return clinic_area_df

def get_clinic_remove_total_data():
    clinic_area_df = load_and_process_clinic_data()
    cols = clinic_area_df.columns.tolist()
    insert_pos = cols.index("鄉鎮市區碼") + 1
    
    new_order = (
        cols[:insert_pos] +
        ["縣市", "區域"] +
        [col for col in cols[insert_pos+1:] if col not in ("縣市", "區域")]
    )
    Departments_area_df = clinic_area_df[new_order].copy()
    
     
    # 寬轉長表格，將科別欄位展開
    melted_df = Departments_area_df.melt(
        id_vars=["Year", "鄉鎮市區碼", "縣市", "區域"],
        var_name="科別",
        value_name="家數"
    )
    return melted_df

def get_clinic_with_total_data():
    clinic_area_df = load_and_process_clinic_data()
    
    cols = clinic_area_df.columns.tolist()
    insert_pos = cols.index("鄉鎮市區碼") + 1
    #****
    new_order1 = (
            cols[:insert_pos] +
            ["縣市", "區域","診所家數"])
    Clinic_city_df = clinic_area_df[new_order1].copy()
    
    return Clinic_city_df