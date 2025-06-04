# Taiwan Clinic

本專案為 Python 專案，旨在分析台灣診所的相關資料，提供有價值的見解與資訊。

## 📁 專案結構

```
Taiwan_Clinic/
├── open_data/                          # 政府開放資料（原始）
│   └── *.csv / *.xlsx
├── source/                             # Python 程式碼
│   ├── barplot_CityOfClinic.py
│   ├── barplot_ClinicGroupUp.py
│   ├── barplot_One city differentClinic.py
│   ├── barplot_year of top10 clinic.py
│   ├── barpolt_all_clinic.py
│   ├── city_people_data.py
│   ├── generate_clinic_lineplots_by_department_city.py
│   ├── lineplot_CityOfClinic.py
│   ├── one_clinic_on every city.py
│   ├── people with clinic.py
│   ├── source_data.py
│   └── subplot_ClinicOfYear.py
├── requirements.txt                    # 套件需求
├── LICENSE                             # 授權條款
├── .gitignore                          # Git 忽略設定
└── README.md                           # 專案說明
```

## 🛠️ 安裝與執行

1. 安裝必要套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 執行主程式（視分析目標選擇合適腳本）：
   ```bash
   python source/people with clinic.py
   ```

## 📊 功能

- 資料清理與預處理
- 診所分布視覺化
- 統計分析與圖表輸出

## 📄 授權

本專案採用 MIT 授權，詳見 [LICENSE](LICENSE)。

## 🙋‍♀️ 貢獻

歡迎提出 Issue 或 Pull Request，共同完善本專案。
