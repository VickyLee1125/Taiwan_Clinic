# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:36:53 2025
#折線子圖，用"科別"分子圖
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
    .groupby(["科別", "Year"])['家數']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)


# 建圖
g = sns.relplot(
    data=clinic_year_df[clinic_year_df["科別"].isin(clinic_year_df["科別"].unique()[:10])],
    x='Year',
    y='家數',
    col='科別',
    kind='line',
    marker='o',
    col_wrap=5,
    height=2.5,
    facet_kws={'sharey': False}
)

g.set_titles("科別: {col_name}", size=12)
g.set_axis_labels("Year", "家數")


# ✅ 修正 X 軸刻度與 Y 軸刻度
for ax, col_name in zip(g.axes.flat, g.col_names):
    ax.set_xticks([2019, 2020, 2021, 2022, 2023])  # 設定 X 軸刻度
    ax.tick_params(axis='x', rotation=45, labelsize=7)  # ✅ X 軸字體變小
    ax.tick_params(axis='y', labelsize=7)              # ✅ Y 軸字體變小
    
    y_min, y_max = ax.get_ylim()
    if col_name in ["眼科", "外科","耳鼻喉科"] and (y_max - y_min) < 30:
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# 儲存圖片
g.savefig("./picture/subplot_clinic_trend.png", dpi=300, bbox_inches='tight')
plt.close()
