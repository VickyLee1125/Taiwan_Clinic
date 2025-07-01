# Taiwan Clinic  台灣診所

本專案使用 Python 分析台灣診所的統計與地理分布資料，並透過視覺化圖表揭示趨勢與比較結果。

## 📁 專案結構

```
Taiwan_Clinic/
├── open_data/                                    # 原始開放資料 （原始）
│   └── *.csv / *.xlsx
├── source/                                       # Python 程式碼
│   ├── barplot_CityOfClinic.py
│   ├── barplot_ClinicGroupUp.py
│   ├── barplot_year of top10 clinic.py
│   ├── city_people_data.py
│   ├── people with clinic.py
│   ├── relplot_ClinicOfYear.py
│   ├── relplot_generate_clinic_by_department_city.py
│   ├── source_data.py
│   └── no_use/                                   # 暫未使用的程式
│       └── ...
├── requirements.txt                              # 套件需求
├── LICENSE                                       # 授權條款
├── .gitignore                                    # Git 忽略設定
└── README.md                                     # 專案說明
```

## 🛠️ 安裝與執行

1. 安裝必要套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 執行主程式（根據分析需求選擇腳本）：
   ```bash
   python source/people with clinic.py
   ```

## 📊 功能說明

- 資料清理與預處理
- 診所分布視覺化
- 統計分析與圖表輸出

## 📄 授權

本專案採用 MIT 授權，詳見 [LICENSE](LICENSE)。

## 🙋‍♀️ 貢獻方式

歡迎提出 Issue 或 Pull Request，協助改善此專案。
