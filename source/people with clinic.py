# -*- coding: utf-8 -*-
"""
Created on Tue May 27 13:50:36 2025
Barplot_2023年，每百萬人的診所數(O)
#圓餅圖-2023年，每平方公里診所數(O)
#Barplot-2023年，每平方公里診所數(O)
@author: USER
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from source_data import get_clinic_with_total_data
from city_people_data import city_people_data

# 載入資料
clinic_city_df = get_clinic_with_total_data()
people_df = city_people_data()

# 各縣市每年診所總數
city_year_df = (
    clinic_city_df
    .groupby(["縣市", "Year"])["診所家數"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

df_2023 = city_year_df[city_year_df["Year"]==2023]

# 合併
merged_df = pd.merge(df_2023, people_df, left_on="縣市", right_on="區域別", how="left")

# 精簡欄位
merged_df = merged_df[["縣市", "Year", "診所家數", "年底人口數", "土地面積"]]

# 新增每萬人診所數
merged_df["醫病比"] =merged_df["年底人口數"] / merged_df["診所家數"]
merged_df["每平方公里診所數"] =merged_df["診所家數"] / merged_df["土地面積"]

#%%
print(merged_df["醫病比"].describe())
#%%
#每診所服務人口數(家)
sns.barplot(data=merged_df, x="醫病比", y="縣市", legend=False, palette='viridis')
plt.title('2023年診所資源分布', fontsize=16)
plt.xlabel('每診所服務人口數(人)', rotation=0, labelpad=10, fontsize=12)
plt.ylabel('縣\n市\n', rotation=0, labelpad=10, fontsize=12)
plt.grid(axis='x', linestyle='--')
plt.tight_layout() 
plt.show()


#%%
#圓餅圖-每平方公里診所數
top_n = 8
df_density = merged_df.sort_values("每平方公里診所數", ascending=False)
top_df = df_density.head(top_n)
others_df = df_density.iloc[top_n:]

labels = top_df["縣市"].tolist() + ["其他"]
sizes = top_df["每平方公里診所數"].tolist() + [others_df["每平方公里診所數"].sum()]

# 設定 explode：其他那塊拉出來（只有最後一個元素）
#explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1]
explode = [0] * top_n + [0.1]  

# 準備右側文字內容
others_labels = others_df["縣市"].tolist()
others_text = "其他包含：\n" + "\n".join(others_labels)

# 建立左右子圖
fig, ax = plt.subplots(1, 2, figsize=(12, 6))


# 左圖：圓餅圖，拉出「其他」
ax[0].pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=2,
    textprops={'fontsize': 10},
    explode=explode
)
ax[0].set_title("2023年各縣市診所密度占比\n（每平方公里診所數）", fontsize=14)
ax[0].axis('equal')

# 右圖：文字標註其他
ax[1].axis('off')
ax[1].text(0, 1, others_text, fontsize=12, va='top')

plt.tight_layout()
plt.show()
#%%
#長條圖-每平方公里診所數
sns.barplot(data=merged_df, y="縣市", x="每平方公里診所數",  palette='viridis')
plt.title('2023年診所資源分布（每平方公里診所數)', fontsize=16)
plt.ylabel('縣市', fontsize=12)
plt.xlabel('每平方公里診所數(家)', rotation=0, labelpad=10, fontsize=12)
plt.grid(axis='x', linestyle='--')
plt.tight_layout() 
plt.show()