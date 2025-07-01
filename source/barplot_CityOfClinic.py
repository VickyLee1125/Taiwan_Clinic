# -*- coding: utf-8 -*-
"""
Created on Tue May 27 13:50:36 2025

縣市5年診所統計 長條圖

@author: USER
"""

import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_with_total_data

# 載入資料
city_year_df = get_clinic_with_total_data()

sns.barplot(data=city_year_df,x='縣市',y='診所家數',hue='Year')
plt.title('各縣市 5年診所家數總和', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('縣市', fontsize=12)
plt.ylabel('總\n診\n所\n家\n數', rotation=0, labelpad=10, fontsize=12)
plt.grid(axis='y', linestyle='--')
plt.tight_layout() 

# 儲存圖片，不顯示
plt.savefig("../../picture/5year_City_Tclinic.png", dpi=300, bbox_inches='tight')  # 可調整解析度與邊界
plt.close()  # 關閉圖表，避免在 notebook 或其他環境自動顯示

plt.show()
