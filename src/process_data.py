import pandas as pd
from pathlib import Path

RAW_SQF = Path(__file__).parent.parent / "raw-data/sqf-2025.xlsx"


def process_sqf_xlsx():
    """
    Loads NYPD Stop, Question, and Frisk 2025 XLSX file, and selects necessary columns.

    Returns:
        A Pandas DataFrame with relevant columns
    """
    # Load raw data
    df = pd.read_excel(RAW_SQF, engine="openpyxl")

    # Keep only necessary columns
    df = df[["STOP_WAS_INITIATED", "SUSPECTED_CRIME_DESCRIPTION", "SUSPECT_RACE_DESCRIPTION", "FRISKED_FLAG", "SEARCHED_FLAG", "STOP_LOCATION_PRECINCT", "SUSPECT_ARRESTED_FLAG"]]

    return df


if __name__ == "__main__":
    print(process_sqf_xlsx())