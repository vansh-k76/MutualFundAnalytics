import sqlite3
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
DB_DIR = BASE_DIR / "data" / "db"

DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "bluestock_mf.db"

# CSV files and SQLite table names
datasets = {
    "01_fund_master.csv": "fund_master",
    "02_nav_history.csv": "nav_history",
    "03_aum_by_fund_house.csv": "aum_by_fund_house",
    "04_monthly_sip_inflows.csv": "monthly_sip_inflows",
    "05_category_inflows.csv": "category_inflows",
    "06_industry_folio_count.csv": "industry_folio_count",
    "07_scheme_performance.csv": "scheme_performance",
    "08_investor_transactions.csv": "investor_transactions",
    "09_portfolio_holdings.csv": "portfolio_holdings",
    "10_benchmark_indices.csv": "benchmark_indices",
}

# Remove old database if it exists
if DB_PATH.exists():
    DB_PATH.unlink()

conn = sqlite3.connect(DB_PATH)

for csv_file, table_name in datasets.items():

    file_path = RAW_DIR / csv_file

    if not file_path.exists():
        print(f"WARNING: {csv_file} not found")
        continue

    df = pd.read_csv(file_path)

    # Convert dates where applicable
    for col in df.columns:
        if "date" in col.lower() or col.lower() == "month":
            try:
                df[col] = pd.to_datetime(df[col], errors="ignore")
            except Exception:
                pass

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}: {len(df):,} rows")

conn.close()

print("\nDatabase created successfully!")
print(f"Location: {DB_PATH}")