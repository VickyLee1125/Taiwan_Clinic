# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:36:53 2025
#折線子圖，用"科別"分子圖
#2019~2023年，六縣市(六都)不同科別診所數 (O)
@author: USER
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from source_data import get_clinic_remove_total_data

# 載入資料
melted_df = get_clinic_remove_total_data()

clinic_year_df = (
    melted_df
    .groupby(["科別", "Year", "縣市"])['家數']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

city_list = ["臺北市", "新北市", "臺中市", "桃園市","高雄市","臺南市"
#             ,"嘉義市", "新竹市","基隆市" ,"彰化縣"
]

clinic_year_df = clinic_year_df[clinic_year_df["縣市"].isin(city_list)]

# 建圖
g = sns.relplot(
    data=clinic_year_df[clinic_year_df["科別"].isin(clinic_year_df["科別"].unique()[:10])],
    x='Year',
    y='家數',
    hue ="縣市",
    col='科別',
    kind='line',
    marker='o',
    col_wrap=5,
    height=2.5,
    facet_kws={'sharey': False}
)

g.set_titles("科別: {col_name}", size=12)
g.set_axis_labels("Year", "家數")


# 儲存圖片
g.savefig("./picture/clinic_lineplots_by_department_city.png", dpi=300, bbox_inches='tight')
plt.close()
