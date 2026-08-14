"""
Data ingestion module for the Bluestock Mutual Fund Analytics project.

This module discovers CSV datasets from the raw data directory,
loads them using pandas, and performs basic validation checks.
"""

from pathlib import Path

import pandas as pd


DATA_FOLDER = Path("data/raw")


def get_csv_files(data_folder: Path = DATA_FOLDER) -> list[Path]:
    """Return all CSV files available in the raw data directory."""
    if not data_folder.exists():
        raise FileNotFoundError(
            f"Raw data directory not found: {data_folder}"
        )

    return sorted(data_folder.glob("*.csv"))


def load_dataset(file_path: Path) -> pd.DataFrame:
    """Load a CSV dataset into a pandas DataFrame."""
    return pd.read_csv(file_path)


def validate_dataset(df: pd.DataFrame, file_path: Path) -> None:
    """Validate that a dataset was loaded successfully."""
    if df.empty:
        raise ValueError(f"Dataset is empty: {file_path.name}")

    if len(df.columns) == 0:
        raise ValueError(f"Dataset contains no columns: {file_path.name}")


def ingest_datasets(data_folder: Path = DATA_FOLDER) -> dict[str, pd.DataFrame]:
    """
    Load and validate all CSV datasets from the raw data directory.

    Returns:
        Dictionary mapping each CSV filename to its DataFrame.
    """
    datasets: dict[str, pd.DataFrame] = {}

    for file_path in get_csv_files(data_folder):
        df = load_dataset(file_path)
        validate_dataset(df, file_path)
        datasets[file_path.stem] = df

    return datasets


def main() -> None:
    """Run the data ingestion process."""
    datasets = ingest_datasets()

    print(f"Successfully loaded {len(datasets)} datasets.")

    for name, df in datasets.items():
        print(f"{name}: {df.shape[0]:,} rows × {df.shape[1]:,} columns")


if __name__ == "__main__":
    main()