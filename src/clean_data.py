import numpy as np
import pandas as pd
from sklearn import preprocessing
from datatypes import CLEAN_DATA_DIR, RAW_SQF, CLEAN_SQF, FORCE_FEATURES


class SQFDataCleaner:
    def __init__(self, file_path=RAW_SQF):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """
        Loads the raw NYPD SQF dataset from an Excel file into a Pandas DataFrame.

        Returns:
            self: The instance with the raw DataFrame loaded.
        """
        self.df = pd.read_excel(self.file_path, engine="openpyxl")

        return self

    def select_and_clean(self):
        """
        Performs data cleaning by selecting relevant features, handling missing
        values, and convert categorical features into numerical format to
        ensure data integrity for modeling.

        Returns:
            self: The instance with the cleaned and filtered DataFrame.
        """

        features = [
            "SUSPECT_RACE_DESCRIPTION",
            "SUSPECT_REPORTED_AGE",
            "SUSPECT_SEX",
            "STOP_WAS_INITIATED",
            "SUSPECTED_CRIME_DESCRIPTION",
            "STOP_LOCATION_PATROL_BORO_NAME",
        ] + FORCE_FEATURES

        self.df = self.df[features].copy()

        # Replace all "(null)"" values with NaN values
        self.df.replace("(null)", np.nan, inplace=True)

        # Reported age: Convert to numeric values and filter errors
        self.df["SUSPECT_REPORTED_AGE"] = pd.to_numeric(
            self.df["SUSPECT_REPORTED_AGE"], errors="coerce"
        )

        # Drop missing values from features: race, age, sex, location (patrol borough)
        self.df.dropna(
            subset=[
                "SUSPECT_RACE_DESCRIPTION",
                "SUSPECT_REPORTED_AGE",
                "SUSPECT_SEX",
                "STOP_LOCATION_PATROL_BORO_NAME",
            ],
            inplace=True,
        )

        # Reported age: Drop records of suspects below the age of 12 (potential record error)
        self.df["SUSPECT_REPORTED_AGE"] = self.df["SUSPECT_REPORTED_AGE"].astype(int)
        self.df = self.df[self.df["SUSPECT_REPORTED_AGE"] >= 12]

        # Reported age: Aggregate data into age categories: <18, 18–24, 25–44, 45–54, >=55
        age_bins = [0, 18, 25, 45, 55, np.inf]
        age_labels = ["<18", "18–24", "25–44", "45–54", ">=55"]

        self.df["SUSPECT_REPORTED_AGE"] = pd.cut(
            self.df["SUSPECT_REPORTED_AGE"],
            bins=age_bins,
            labels=age_labels,
            right=False,
        )

        # Clean all string columns
        string_features = [
            "SUSPECT_RACE_DESCRIPTION",
            "SUSPECT_SEX",
            "STOP_WAS_INITIATED",
            "SUSPECTED_CRIME_DESCRIPTION",
        ]

        self.df[string_features] = (
            self.df[string_features]
            .astype(str)
            .stack()
            .str.lower()
            .str.replace(r"\s*/\s*", "_", regex=True)
            .str.strip()
            .unstack()
        )

        # Fill missing values for features: reason why stop was initiated, suspected crime description
        self.df["STOP_WAS_INITIATED"] = self.df["STOP_WAS_INITIATED"].replace(
            "nan", "unknown"
        )
        self.df["SUSPECTED_CRIME_DESCRIPTION"] = self.df[
            "SUSPECTED_CRIME_DESCRIPTION"
        ].replace("nan", "other")

        # Replace "Y" in physical force columns with 1, and missing values with 0
        self.df[FORCE_FEATURES] = self.df[FORCE_FEATURES].replace(
            {"Y": 1, "nan": 0, np.nan: 0}
        )
        self.df[FORCE_FEATURES] = (
            self.df[FORCE_FEATURES].apply(pd.to_numeric, errors="coerce").fillna(0)
        )

        # Convert categorical features into numerical format using One-Hot Encoding
        categorical_features = [
            "SUSPECT_SEX",
            "STOP_WAS_INITIATED",
            "SUSPECTED_CRIME_DESCRIPTION",
            "SUSPECT_REPORTED_AGE",
            "STOP_LOCATION_PATROL_BORO_NAME",
        ]

        # Set white as baseline for race comparison
        races = sorted(self.df["SUSPECT_RACE_DESCRIPTION"].unique().tolist())
        if "white" in races:
            races.remove("white")
            races.insert(0, "white")

        self.df["SUSPECT_RACE_DESCRIPTION"] = pd.Categorical(
            self.df["SUSPECT_RACE_DESCRIPTION"], categories=races
        )

        self.df = pd.get_dummies(
            self.df,
            columns=categorical_features + ["SUSPECT_RACE_DESCRIPTION"],
            drop_first=True,
            dtype=float,
        )

        return self

    def consolidate_use_of_force(self):
        """
        Aggregates multiple physical force indicators into a single binary feature,
        representing whether any form of physical escalation occurred during the stop.

        Returns:
            self: The instance with the new "USE_OF_FORCE_FLAG" target column added.
        """
        force_use_yes = self.df[FORCE_FEATURES] == 1
        self.df["USE_OF_FORCE_FLAG"] = force_use_yes.any(axis=1).astype(int)
        self.df.drop(columns=FORCE_FEATURES, inplace=True)

        return self

    def save_cleaned_data(self, output_path=CLEAN_SQF):
        if not CLEAN_DATA_DIR.exists():
            CLEAN_DATA_DIR.mkdir()
        self.df.to_csv(output_path, index=False)


if __name__ == "__main__":
    (
        SQFDataCleaner()
        .load_data()
        .select_and_clean()
        .consolidate_use_of_force()
        .save_cleaned_data()
    )
