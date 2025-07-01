# -*- coding: utf-8 -*-
"""
Created on Wed May 28 14:58:21 2025
同一縣市不同科別分布(無使用)
@author: USER
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_remove_total_data

# 載入資料
melted_df = get_clinic_remove_total_data()
# melted_df.to_excel("clinic_data.xlsx", index=False)

clinic_year_df = (
    melted_df
    .groupby(["科別","Year"])['家數']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)


   
Top10=(clinic_year_df["科別"].unique())[:10]
cities = melted_df.groupby(["縣市", "Year"])["家數"].sum().sort_values(ascending=False).reset_index().loc[:,"縣市"].unique()
print(cities)

for city in cities:
    place_df = melted_df[(melted_df['縣市'] == city)].copy()
    
    grouped_df = place_df.groupby(['Year','科別'])['家數'].sum().reset_index()
    
    # 6. 繪製長條圖
    plt.figure(figsize=(12, 6))
    sns.barplot(x='科別', y='家數', hue='Year', data=grouped_df, order=Top10)  # 加入 hue 參數
    # plt.gca().set_ylim(0, 6000)
    plt.title(city+' 5年間各科別診所家數', fontsize=16)
    plt.xlabel('科別', fontsize=12)
    plt.ylabel('總\n診\n所\n家\n數', rotation=0, labelpad=10, fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='年份', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
# plt.show()
    
    # 儲存圖片，不顯示
    plt.savefig(f"./picture/city_{city}.png", dpi=300, bbox_inches='tight')  # 可調整解析度與邊界
    plt.close()  # 關閉圖表，避免在 notebook 或其他環境自動顯示



# for x in Top10:
#     clinic_df = melted_df[melted_df['科別'] == x].copy()
    
#     grouped_df = clinic_df.groupby(['Year','縣市'])['家數'].sum().sort_values(ascending=False).head(100).reset_index()
    
#     # 6. 繪製長條圖
#     plt.figure(figsize=(12, 6))
#     sns.barplot(x='縣市', y='家數', hue='Year',  order=city, data=grouped_df)  # 加入 hue 參數
#     plt.title(x+' 2019-2023 年診所家數', fontsize=16)
#     plt.xlabel('縣市', fontsize=12)
#     plt.ylabel('總\n診\n所\n家\n數', rotation=0, labelpad=10, fontsize=12)
#     plt.xticks(rotation=45)
#     plt.legend(title='年份', fontsize=10)
#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.tight_layout()
#     plt.show()
