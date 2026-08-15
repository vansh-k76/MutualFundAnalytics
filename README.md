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
Power BI
        ↓
Interactive Dashboard

 
## 6. Power BI Dashboard

The project includes an interactive Power BI dashboard designed to analyze mutual fund industry performance, investor behavior, SIP trends, and NAV performance.

### Industry Overview

- AUM distribution across AMCs
- Monthly SIP inflow trends
- Industry AUM trends
- Net inflow by mutual fund category
- Category-wise industry analysis

### Fund Performance

- Fund return vs risk analysis
- NAV vs benchmark comparison
- Fund performance scorecard
- Fund house, category, and plan filters

### Investor Analytics

- Investor analysis by age group
- City-tier analysis
- State-wise transaction amount
- Average SIP amount by age group
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

## 8. How to Run

### 1. Clone the Repository

 
git clone https://github.com/vansh-k76MutualFundAnalytics.git
cd MutualFundAnalytics