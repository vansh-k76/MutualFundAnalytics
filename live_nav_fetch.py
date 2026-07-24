import requests
import pandas as pd
import os

scheme_codes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

output_folder = "data/raw"

for scheme_name, scheme_code in scheme_codes.items():
    print("=" * 60)
    print(f"Fetching {scheme_name} ({scheme_code})")
    print("=" * 60)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_path = os.path.join(
            output_folder,
            f"{scheme_name}.csv"
        )

        nav_df.to_csv(file_path, index=False)

        print("Saved:", file_path)
        print(nav_df.head())

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    print()