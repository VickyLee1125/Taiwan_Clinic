# -*- coding: utf-8 -*-
"""
Created on Tue May 27 15:29:19 2025
#5年診所所有科別家數排序_長條圖(無用到)
@author: USER
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_remove_total_data

# 載入資料
melted_df = get_clinic_remove_total_data()


total_by_clinic = melted_df.groupby(["科別","Year"])['家數'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(12, 7))
sns.barplot(data=total_by_clinic, x='科別',y='家數',hue='Year')
plt.title('5年診所家數總和', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('科別', fontsize=12)
plt.ylabel('總\n診\n所\n家\n數', rotation=0, labelpad=10, fontsize=12)
plt.grid(axis='y', linestyle='--')
plt.tight_layout() 
plt.show()

# # 儲存圖片，不顯示
# plt.savefig("./picture/clinic_all.png", dpi=300, bbox_inches='tight')  # 可調整解析度與邊界
# plt.close()  # 關閉圖表，避免在 notebook 或其他環境自動顯示
