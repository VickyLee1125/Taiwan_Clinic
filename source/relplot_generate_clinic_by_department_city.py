# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:36:53 2025
2019~2023年，六都前10科別診所數變化   折線子圖
目的: 區域比較，看10個「科別」在6都縣市的變化
@author: USER
"""
# 匯入必要套件
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_remove_total_data

# 讀取資料
melted_df = get_clinic_remove_total_data()

# 計算各【科別】、【年度】、【縣市】的「診所總家數」
clinic_year_df = (
    melted_df
    .groupby(["科別", "Year", "縣市"])['家數']   # 依 科別、年度、縣市 分組
    .sum()                                     # 計算家數總和
    .sort_values(ascending=False)              # 由大到小排序
    .reset_index()                             # 重建索引，轉回 DataFrame
)


# 六都清單
city_list = ["臺北市", "新北市", "臺中市", "桃園市","高雄市","臺南市"]

# 篩選出六都資料
clinic_year_df = clinic_year_df[clinic_year_df["縣市"].isin(city_list)]

# 繪製折線圖 (使用子圖)
g = sns.relplot(
    data=clinic_year_df[clinic_year_df["科別"].isin(clinic_year_df["科別"].unique()[:10])],
    # 只取出【前10大】科別的資料（取出前10種不同的科別名稱）
    x='Year',                    # X 軸為年度
    y='家數',                     # Y 軸為診所家數
    hue="縣市",                   # 不同縣市分組
    col='科別',                   # 每一種「科別」作為一個子圖
    kind='line',                 # 使用折線圖
    marker='o',                  # 加入點標記
    col_wrap=5,                  # 每列放 5 張圖（超過會自動換行）
    height=2.5,                  # 每張子圖的高度
    facet_kws={'sharey': False}  # 不同子圖的 y 軸範圍獨立
)

# 設定子圖標題樣式
g.set_titles("科別: {col_name}", size=12)

# 設定 X、Y 軸標籤
g.set_axis_labels("Year", "家數")


# 儲存圖片
# g.savefig("../../picture/clinic_lineplots_by_department_city.png", dpi=300, bbox_inches='tight')
# plt.close()
plt.show()