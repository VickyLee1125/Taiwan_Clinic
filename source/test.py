# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 16:15:06 2025

@author: ctlop
"""
import pandas as pd
import matplotlib.pyplot as plt

client_df = pd.DataFrame()
for year in range(108,113):
    file_path =f"../open_data/{year}年診所科別統計/clinic_sp{year}.csv"
    print(file_path)
    
    try:
        df = pd.read_csv(file_path, encoding ="big5")
        df_total = df.concat([client_df,df])
    except:
        print(f"找不到檔案：{file_path}")
    
