# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:36:53 2025
前10科別  折線子圖，全台總數變化
目的:整體趨勢觀察，看10個「科別」的變化
@author: USER
"""
# 匯入套件
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from source_data import get_clinic_remove_total_data

# 載入資料
melted_df = get_clinic_remove_total_data()


# 各科別每年診所總數（全台加總）
clinic_year_df = (
    melted_df
    .groupby(["科別", "Year"])['家數']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# 依據"科別"分組，【總家數】排序，挑出前10大科別
top10_categories = (
    clinic_year_df
    .groupby("科別")["家數"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .index
    .tolist()
)

# 繪製折線子圖
g = sns.relplot(
    data=clinic_year_df[clinic_year_df["科別"].isin(top10_categories)],
    x='Year',         # X 軸：年度
    y='家數',         # Y 軸：診所家數
    col='科別',       # 每種科別一張小圖
    kind='line',      # 折線圖
    marker='o',       # 加上 marker
    col_wrap=5,       # 每列 5 張子圖
    height=2.5,       # 圖高 2.5
    facet_kws={'sharey': False}  # 不共用 Y 軸
)


# 設定子圖標題
g.set_titles("科別: {col_name}", size=12)


# 設定 X、Y 軸標籤
g.set_axis_labels("Year", "家數")


# ✅ 修正 X 軸刻度與 Y 軸刻度
for ax, col_name in zip(g.axes.flat, g.col_names):
    ax.set_xticks([2019, 2020, 2021, 2022, 2023])  # 設定 X 軸刻度
    ax.tick_params(axis='x', rotation=45, labelsize=7)  # ✅ X 軸字體變小


# # 儲存圖片(../到上一層)
# g.savefig("../../picture/subplot_clinic_trend.png", dpi=300, bbox_inches='tight')
# plt.close()

plt.show()