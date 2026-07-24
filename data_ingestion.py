import os
import pandas as pd

DATA_FOLDER = "data/raw"

csv_files = [file for file in os.listdir(DATA_FOLDER) if file.endswith(".csv")]

for file in sorted(csv_files):
    file_path = os.path.join(DATA_FOLDER, file)

    print("=" * 60)
    print(f"Dataset: {file}")
    print("=" * 60)

    df = pd.read_csv(file_path)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\n")

    print("\n" + "=" * 70)
print("FUND MASTER ANALYSIS")
print("=" * 70)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())


print("\n" + "=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print(f"Total AMFI Codes in fund_master: {len(fund_codes)}")
print(f"Total AMFI Codes in nav_history: {len(nav_codes)}")
print(f"Missing AMFI Codes: {len(missing_codes)}")

if missing_codes:
    print("\nMissing Codes:")
    print(sorted(missing_codes))
else:
    print("\n All AMFI codes are present in nav_history.")