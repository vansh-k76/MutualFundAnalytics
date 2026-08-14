"""
Live mutual fund NAV data fetcher.

Fetches NAV history for selected mutual funds from the MFAPI service
and saves the results as CSV files in the raw data directory.
"""

from pathlib import Path

import pandas as pd
import requests


OUTPUT_FOLDER = Path("data/raw")

SCHEME_CODES = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841",
}

API_URL = "https://api.mfapi.in/mf/{scheme_code}"


def fetch_nav_data(scheme_name: str, scheme_code: str) -> None:
    """
    Fetch NAV data for a mutual fund scheme and save it as a CSV file.

    Args:
        scheme_name: Name used for the output CSV file.
        scheme_code: MFAPI scheme code.
    """
    url = API_URL.format(scheme_code=scheme_code)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        if "data" not in data:
            raise ValueError("API response does not contain NAV data.")

        nav_df = pd.DataFrame(data["data"])

        if nav_df.empty:
            raise ValueError("API returned an empty NAV dataset.")

        OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

        file_path = OUTPUT_FOLDER / f"{scheme_name}.csv"
        nav_df.to_csv(file_path, index=False)

        print(f"{scheme_name}: {len(nav_df):,} rows saved to {file_path}")
        return file_path
    except requests.RequestException as error:
        print(f"{scheme_name}: request failed - {error}")

    except (ValueError, KeyError) as error:
        print(f"{scheme_name}: invalid API response - {error}")


def main() -> None:
    """Fetch and save NAV data for all configured mutual fund schemes."""
    for scheme_name, scheme_code in SCHEME_CODES.items():
        fetch_nav_data(scheme_name, scheme_code)

def fetch_all_nav_data() -> list[Path]:
    """Fetch NAV data for all configured mutual fund schemes."""
    saved_files = []

    for scheme_name, scheme_code in SCHEME_CODES.items():
        file_path = fetch_nav_data(scheme_name, scheme_code)

        if file_path is not None:
            saved_files.append(file_path)

    return saved_files
if __name__ == "__main__":
    fetch_all_nav_data()