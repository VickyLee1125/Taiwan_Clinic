# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:53:39 2025
# 線圖 (Line Chart)  (無用到)
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

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='家數', hue='科別', data=clinic_year_df[0:50], marker='o')
plt.title('各科別5年診所數量趨勢', fontsize=16)
plt.xlabel('年份', fontsize=12)
plt.ylabel('總\n診\n所\n家\n數', rotation=0, labelpad=10, fontsize=12)
plt.xticks(clinic_year_df['Year'].unique())
plt.legend(title='科別', bbox_to_anchor=(1, 1), loc='upper left') # 將圖例放在圖表外
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# 儲存圖片，不顯示
# plt.savefig("./picture/clinic_trend.png", dpi=300, bbox_inches='tight')  # 可調整解析度與邊界
# plt.close()  # 關閉圖表，避免在 notebook 或其他環境自動顯示