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