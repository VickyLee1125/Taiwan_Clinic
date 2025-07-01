# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:34:10 2025

2023年家數多的前10科別成長百分比(2019 vs 2023) 長條圖

@author: USER
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_remove_total_data

# 載入資料
melted_df = get_clinic_remove_total_data()

# 各科別每年診所總數
clinic_year_df = (
    melted_df
    .groupby(["科別","Year"])['家數']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# 轉換成寬格式： 每個「科別」變成 1 row，2019、2023 變成 2 個 column
pivot_result = clinic_year_df.pivot_table(index='科別', columns='Year', values='家數')

# 只取出 2019 和 2023 年，並重新命名欄位
result = pivot_result[[2023, 2019]].rename(columns={2023: '家數_2023', 2019: '家數_2019'})

# 計算成長百分比：( 2023 家數 - 2019 家數 ) / 2023 家數
result['百分比'] = ((result['家數_2023'] - result['家數_2019']) / result['家數_2023'])

# 依照 2023 家數排序，取出前 10 名科別
result_sorted = result.sort_values(by='家數_2023', ascending = False).head(10)

# 設定 bar 顏色：成長為綠色，衰退為紅色
colors = ['green' if x > 0 else 'red' for x in result_sorted['百分比']]

# 畫長條圖
sns.barplot(data=result_sorted, x='科別', y='百分比', palette=colors)
plt.title('5年診所成長百分比 (以2023年為基準)', fontsize=16)

# 設定 X 軸標籤
plt.xticks(rotation=45)
plt.xlabel('科別', fontsize=12)

# 設定 Y 軸標籤（垂直排列）
plt.ylabel('診\n所\n成\n長\n百\n分\n比', rotation=0, labelpad=10, fontsize=12)

# 設定 Y 軸刻度值 與 標籤（格式為 %）
yticks_values = [-0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06]
yticks_labels = [f'{y*100}%' for y in yticks_values]
plt.yticks(yticks_values, yticks_labels)

# 設定 Y 軸範圍，確保包含設定的刻度
plt.ylim(min(yticks_values) - 0.02, max(yticks_values) + 0.02) 

# 添加 Y 軸 0% 基準線（分隔正數/負數）
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
# Y 軸加上虛線格線
plt.grid(axis='y', linestyle='--')

plt.tight_layout()

# 儲存圖片，不顯示
# plt.savefig("../../picture/clinic_GroupUP.png", dpi=300, bbox_inches='tight')  # 可調整解析度與邊界
# plt.close()  # 關閉圖表，避免在 notebook 或其他環境自動顯示

plt.show()