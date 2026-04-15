import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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


def basic_stats_summary(df):
    """
    basic stats
    """
    # total number of samples
    total_count = len(df)
    # frequency of race
    race_counts = df['SUSPECT_RACE_DESCRIPTION'].value_counts()
    max_race, max_count = race_counts.idxmax(), race_counts.max()
    min_race, min_count = race_counts.idxmin(), race_counts.min()

    # average arrest =rate
    avg_arrest_rate = (df['SUSPECT_ARRESTED_FLAG'] == 'Y').mean() * 100
    
    print(f"Total Samples (Count): {total_count:,}")
    print(f"Top Group (Max Freq): {max_race} ({max_count:,} stops)")
    print(f"Min Group (Min Freq): {min_race} ({min_count:,} stops)")
    print(f"Overall Average Arrest Rate: {avg_arrest_rate:.1f}%")

    # count, unique, top, freq on every columns
    print(df.describe(include='all'))
    
    # missing values
    print(df.isnull().sum())

def explore_sqf_data(df):
    """
    arrest related, stop initiated visualization
    """
    # arrest_counts by race(frequency)
    arrest_counts = pd.crosstab(df["SUSPECT_RACE_DESCRIPTION"], df["SUSPECT_ARRESTED_FLAG"])
    print(arrest_counts)
    ## visualize
    arrest_counts.plot(kind='bar', figsize=(10, 6), width=0.8)
    plt.title("Total Number of Arrests vs. Non-Arrests by Race")
    plt.ylabel("Count of Stops")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Arrested", labels=["No (N)", "Yes (Y)"])
    plt.tight_layout()
    plt.show()

    # arrest_rate by race(percentage)
    arrest_rate = pd.crosstab(df["SUSPECT_RACE_DESCRIPTION"], df["SUSPECT_ARRESTED_FLAG"], normalize="index") * 100
    print(arrest_rate.round(1))
    ## visualize
    arrest_rate.plot(kind='bar', stacked=True, figsize=(10, 6), color=["red","blue"])
    plt.title("Arrest Rate (%) by Race")
    plt.ylabel("Percentage")
    plt.legend(title="Arrested", labels=["No (N)", "Yes (Y)"])
    plt.show()

    # cause of stop initated by race
    initiated_rate = pd.crosstab(df["SUSPECT_RACE_DESCRIPTION"], df["STOP_WAS_INITIATED"], normalize="index") * 100
    print(initiated_rate.round(1))
    ## visualize
    initiated_rate.plot(kind="barh", stacked=True, figsize=(12, 7))
    plt.title("How Stops Were Initiated by Race (%)")
    plt.xlabel("Percentage (%)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    #print(process_sqf_xlsx())
    sqf_df=process_sqf_xlsx()
    basic_stats_summary(sqf_df)
    explore_sqf_data(sqf_df)