"""
Master execution script for the Bluestock Mutual Fund Analytics pipeline.

Pipeline stages:
1. Fetch latest mutual fund NAV data.
2. Load and validate all raw datasets.
"""

from live_nav_fetch import fetch_all_nav_data
from data_ingestion import ingest_datasets


def main() -> None:
    """Execute the complete data pipeline."""

    print("Starting Bluestock Mutual Fund Analytics pipeline...")
    print()

    # Step 1: Fetch latest NAV data
    print("Step 1/2: Fetching latest NAV data...")
    saved_files = fetch_all_nav_data()
    print(f"Fetched and saved {len(saved_files)} NAV datasets.")
    print()

    # Step 2: Load and validate datasets
    print("Step 2/2: Loading and validating datasets...")
    datasets = ingest_datasets()
    print(f"Successfully loaded {len(datasets)} datasets.")
    print()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()