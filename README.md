# Bluestock Mutual Fund Analytics

## 1. Project Overview

Bluestock Mutual Fund Analytics is a data analytics and business intelligence project focused on analyzing Indian mutual fund performance, investor behavior, fund characteristics, SIP trends, and benchmark performance.

The project combines Python-based data ingestion and validation with SQL analysis and an interactive Power BI dashboard.

The objective is to transform raw mutual fund datasets into meaningful analytical insights that can support fund comparison, performance evaluation, investor analysis, and market trend analysis.

---

## 2. Project Objectives

The project aims to:

- Analyze mutual fund performance and risk.
- Compare mutual fund NAV performance with market benchmarks.
- Analyze fund categories, fund houses, and scheme characteristics.
- Study investor demographics and transaction behavior.
- Analyze SIP inflow trends.
- Analyze category-wise net inflows.
- Evaluate benchmark and market trends.
- Build an interactive Power BI dashboard.
- Create a reproducible Python data pipeline.

---

## 3. Technology Stack

### Programming and Data Processing

- Python
- Pandas
- Requests

### Database / Querying

- SQL

### Visualization

- Microsoft Power BI

### Data Sources

- Mutual fund datasets
- MFAPI for NAV data

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 4. Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── dashboard/
│
├── notebooks/
│
├── reports/
│
├── sql/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── run_pipeline.py
├── README.md
└── .gitignore
```

---

## 5. Data Pipeline

The project follows a reproducible data analytics pipeline that transforms raw mutual fund datasets into analytical insights and interactive visualizations.

```text
Raw Mutual Fund Data
        ↓
Python Data Ingestion
        ↓
Data Validation
        ↓
Live NAV Fetching from MFAPI
        ↓
CSV Datasets
        ↓
SQL Analysis
        ↓
Power BI Data Model
        ↓
Interactive Dashboard
        ↓
Business Insights
```

### Main Pipeline Components

**`data_ingestion.py`**

Discovers and loads CSV datasets from the raw data directory using Pandas and performs basic validation checks.

**`live_nav_fetch.py`**

Fetches NAV data from MFAPI and stores the retrieved data for analysis.

**`run_pipeline.py`**

Acts as the master execution script for running the project's data pipeline.

---

## 6. Power BI Dashboard

The project includes an interactive Power BI dashboard designed to analyze mutual fund industry performance, investor behavior, SIP trends, and NAV performance.

### Industry Overview

- AUM distribution across AMCs
- Monthly SIP inflow trends
- Industry AUM trends
- Net inflow by mutual fund category
- Category-wise industry analysis
- Industry-level KPIs

### Fund Performance

- Fund return vs risk analysis
- NAV vs benchmark comparison
- Fund performance scorecard
- Fund house, category, and plan filters
- Scheme-level performance analysis

### Investor Analytics

- Investor analysis by age group
- City-tier analysis
- State-wise transaction amount
- Average SIP amount by age group
- Monthly transaction volume
- Transaction type distribution

### SIP & Market Trends

- Top categories by net inflow
- Monthly category-wise SIP inflows
- SIP inflow vs NIFTY 50
- Market trend analysis

### NAV Detail

- Mutual fund NAV trends
- NAV vs benchmark analysis
- Benchmark index performance
- Fund and benchmark filtering

---

## 7. Key Insights

The analysis provides insights into:

- Mutual fund AUM distribution across different fund houses.
- Growth and movement of SIP inflows over time.
- Category-wise net inflow patterns.
- Relationship between mutual fund returns and risk.
- Investor transaction behavior across age groups and states.
- Mutual fund NAV performance relative to market benchmarks.
- Changes in SIP inflows alongside NIFTY 50 market trends.

---

## 8. How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/vansh-k76/MutualFundAnalytics.git
cd MutualFundAnalytics
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install pandas requests
```

If a `requirements.txt` file is available, use:

```bash
pip install -r requirements.txt
```

### 5. Run the Master Pipeline

```bash
python run_pipeline.py
```

Individual scripts can also be executed separately:

```bash
python data_ingestion.py
python live_nav_fetch.py
```

---

## 9. Dashboard

The final Power BI dashboard contains interactive filters, KPI cards, charts, trend analysis, and detailed performance tables.

Open the Power BI dashboard file from the `dashboard/` directory using Microsoft Power BI Desktop.

If the dashboard is published to Power BI Service, the public/viewer URL can be added below:

```text
Dashboard URL:
[Add Power BI URL here]
```

---

## 10. Deliverables

The final project submission includes:

- Final PDF Report
- 12-Slide Presentation
- Python Data Pipeline
- SQL Analysis
- Power BI Dashboard
- Mutual Fund Datasets
- Project Documentation
- GitHub Repository
- `v1.0` Git Tag

---

## 11. Limitations

- Analysis depends on the availability and quality of the underlying datasets.
- Live NAV data depends on the availability of the external data source.
- Dashboard results are based on the datasets included in the project.
- Historical mutual fund performance does not guarantee future returns.
- The project is intended for analytical and educational purposes.

---

## 12. Disclaimer

This project was developed for educational and internship/capstone purposes.

The analysis presented in this project is for informational purposes only and does not constitute financial, investment, or trading advice.

---

## 13. Project Version

**Version:** `v1.0`

**Repository:**  
https://github.com/vansh-k76/MutualFundAnalytics

---

## Author

**Vansh Kumar**

GitHub: https://github.com/vansh-k76