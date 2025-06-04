# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:34:10 2025
#2019vs2023，10科別成長百分比，長條圖(O)
@author: USER
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_remove_total_data

# 載入資料
melted_df = get_clinic_remove_total_data()

clinic_year_df = (
    melted_df
    .groupby(["科別","Year"])['家數']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)


pivot_result = clinic_year_df.pivot_table(index='科別', columns='Year', values='家數')
result = pivot_result[[2023, 2019]].rename(columns={2023: '家數_2023', 2019: '家數_2019'})
result['百分比'] = ((result['家數_2023'] - result['家數_2019']) / result['家數_2023'])

result_sorted = result.sort_values(by='家數_2023', ascending = False).head(10)
# result_sorted = result.sort_values(by='家數_2023', ascending = False).head(10)
colors = ['green' if x > 0 else 'red' for x in result_sorted['百分比']]
sns.barplot(data=result_sorted, x='科別', y='百分比', palette=colors)
plt.title('5年診所成長百分比 (以2023年為基準)', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('科別', fontsize=12)
plt.ylabel('診\n所\n成\n長\n百\n分\n比', rotation=0, labelpad=10, fontsize=12)
abs_max_percentage = abs(result_sorted['百分比']).max()
y_upper = abs_max_percentage + 5
y_lower = -abs_max_percentage - 5
yticks_values = [-0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06]
yticks_labels = [f'{y*100}%' for y in yticks_values]
plt.yticks(yticks_values, yticks_labels)

# 設定 y 軸的範圍，確保包含設定的刻度
plt.ylim(min(yticks_values) - 0.02, max(yticks_values) + 0.02) 
# 添加 y 軸的 0% 水平線
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(axis='y', linestyle='--')

plt.tight_layout()
# plt.show()

# 儲存圖片，不顯示
plt.savefig("./picture/clinic_GroupUP.png", dpi=300, bbox_inches='tight')  # 可調整解析度與邊界
plt.close()  # 關閉圖表，避免在 notebook 或其他環境自動顯示