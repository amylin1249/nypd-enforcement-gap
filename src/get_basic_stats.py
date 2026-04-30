import pandas as pd
import matplotlib.pyplot as plt
from datatypes import RAW_SQF


def process_sqf_xlsx():
    """
    Loads NYPD Stop, Question, and Frisk (SQF) 2025 XLSX file, and selects necessary columns.

    Returns:
        A Pandas DataFrame with relevant columns
    """
    # Load raw data
    df = pd.read_excel(RAW_SQF, engine="openpyxl")

    # Keep only necessary columns
    df = df[
        [
            "STOP_WAS_INITIATED",
            "SUSPECTED_CRIME_DESCRIPTION",
            "SUSPECT_RACE_DESCRIPTION",
            "FRISKED_FLAG",
            "SEARCHED_FLAG",
            "STOP_LOCATION_PRECINCT",
            "SUSPECT_ARRESTED_FLAG",
        ]
    ]

    return df


def generate_basic_stats(df):
    """
    Generate basic statistics from the SQF dataset
    """
    # Generate total number of samples
    total_count = len(df)

    # Generate frequency of race
    race_counts = df["SUSPECT_RACE_DESCRIPTION"].value_counts()
    max_race, max_count = race_counts.idxmax(), race_counts.max()
    min_race, min_count = race_counts.idxmin(), race_counts.min()

    # Generate average arrest rate
    avg_arrest_rate = (df["SUSPECT_ARRESTED_FLAG"] == "Y").mean() * 100

    print(f"Total Samples (Count): {total_count:,}")
    print(f"Top Group (Max Freq): {max_race} ({max_count:,} stops)")
    print(f"Min Group (Min Freq): {min_race} ({min_count:,} stops)")
    print(f"Overall Average Arrest Rate: {avg_arrest_rate:.1f}%")

    # Generate count of non-null observations, unique number of non-null observations,
    # top-occurring value, and frequency of top-occurring value for each column
    print(df.describe(include="all"))

    # Generate number of missing values for each column
    print(df.isnull().sum())


def explore_sqf_data(df):
    """
    arrest related, stop initiated visualization
    """
    # Generate arrest counts by race (frequency)
    arrest_counts = pd.crosstab(
        df["SUSPECT_RACE_DESCRIPTION"], df["SUSPECT_ARRESTED_FLAG"]
    )
    print(arrest_counts)

    # Visualize arrest counts by race
    arrest_counts.plot(kind="bar", figsize=(10, 6), width=0.8)
    plt.title("Total Number of Arrests vs. Non-Arrests by Race")
    plt.ylabel("Count of Stops")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Arrested", labels=["No (N)", "Yes (Y)"])
    plt.tight_layout()
    plt.show()

    # Generate arrest rates by race (percentage)
    arrest_rate = (
        pd.crosstab(
            df["SUSPECT_RACE_DESCRIPTION"],
            df["SUSPECT_ARRESTED_FLAG"],
            normalize="index",
        )
        * 100
    )
    print(arrest_rate.round(1))

    # Visualize arrest rates by race
    arrest_rate.plot(kind="bar", stacked=True, figsize=(10, 6), color=["red", "blue"])
    plt.title("Arrest Rate (%) by Race")
    plt.ylabel("Percentage (%)")
    plt.legend(title="Arrested", labels=["No (N)", "Yes (Y)"])
    plt.show()

    # Generate breakdown of stop initiation method by race (percentage)
    initiated_rate = (
        pd.crosstab(
            df["SUSPECT_RACE_DESCRIPTION"], df["STOP_WAS_INITIATED"], normalize="index"
        )
        * 100
    )
    print(initiated_rate.round(1))
    # Visualize breakdown of stop initiation method by race
    initiated_rate.plot(kind="barh", stacked=True, figsize=(12, 7))
    plt.title("How Stops Were Initiated by Race (%)")
    plt.xlabel("Percentage (%)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sqf_df = process_sqf_xlsx()
    print("Summary of Basic Statistics")
    generate_basic_stats(sqf_df)
    print()
    print("Breakdown of Stops and Arrests by Race and Stop Initiation Method")
    explore_sqf_data(sqf_df)
