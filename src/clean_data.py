import pandas as pd
import numpy as np
from pathlib import Path

RAW_SQF = Path(__file__).parent.parent / "raw-data/sqf-2025.xlsx"
CLEAN_DATA_DIR = Path(__file__).parent.parent / "clean-data"
CLEAN_SQF = Path(__file__).parent.parent / "clean-data/cleaned_sqf.csv"


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
        # return self
    
    
    def select_and_clean(self):
        """
        Performs initial data cleaning by selecting relevant features and 
        handling missing values to ensure data integrity for modeling.

        Specific operations include:
        1. Subset selection: Retains only the columns necessary for demographic 
           and enforcement analysis.
        2. Age normalization: Converts reported age to numeric values and 
           imputes missing data using the median to minimize outlier impact.
        3. Row-wise deletion: Removes any remaining records with null values 
           to provide a complete dataset for the training pipeline.

        Returns:
            self: The instance with the cleaned and filtered DataFrame.
        """

        features = [
            "SUSPECT_RACE_DESCRIPTION", "SUSPECT_REPORTED_AGE", "SUSPECT_SEX",
            "STOP_LOCATION_PRECINCT", "STOP_WAS_INITIATED", 
            "SUSPECTED_CRIME_DESCRIPTION", "FRISKED_FLAG", 
            "SEARCHED_FLAG", "SUSPECT_ARRESTED_FLAG"
        ]
        self.df = self.df[features]
        
        # age: fill in missing values
        self.df["SUSPECT_REPORTED_AGE"] = pd.to_numeric(self.df["SUSPECT_REPORTED_AGE"], errors='coerce')
        self.df["SUSPECT_REPORTED_AGE"] = self.df["SUSPECT_REPORTED_AGE"].fillna(self.df["SUSPECT_REPORTED_AGE"].median())
        
        # drop missing values
        self.df = self.df.dropna()
        # return self

        ## Amanda: Proposed edits below - I uv run python-ed using the code below (also, shift features to be global or in a separate datatypes file?)
        # features = [
        #     "SUSPECT_RACE_DESCRIPTION", "SUSPECT_REPORTED_AGE", "SUSPECT_SEX",
        #     "STOP_LOCATION_PRECINCT", "STOP_WAS_INITIATED", 
        #     "SUSPECTED_CRIME_DESCRIPTION", "FRISKED_FLAG", "SEARCHED_FLAG", 
        #     "SUSPECT_ARRESTED_FLAG"]
        
        # features_force = ["PHYSICAL_FORCE_CEW_FLAG",
        #     "PHYSICAL_FORCE_DRAW_POINT_FIREARM_FLAG",
        #     "PHYSICAL_FORCE_HANDCUFF_SUSPECT_FLAG", "PHYSICAL_FORCE_OC_SPRAY_USED_FLAG",
        #     "PHYSICAL_FORCE_OTHER_FLAG", "PHYSICAL_FORCE_RESTRAINT_USED_FLAG",
        #     "PHYSICAL_FORCE_WEAPON_IMPACT_FLAG"]

        # self.df = self.df[features + features_force]

        # # Replace all "(null)"" values with NaN values
        # self.df.replace("(null)", np.nan, inplace=True)

        # # Drop missing values from suspect reported age, suspect sex, and stop location precinct
        # self.df.dropna(subset=["SUSPECT_REPORTED_AGE", "SUSPECT_SEX", "STOP_LOCATION_PRECINCT"], inplace=True)

        # # Reported age: Drop records of suspects below the age of 12 (potential record error)
        # self.df["SUSPECT_REPORTED_AGE"] = self.df["SUSPECT_REPORTED_AGE"].astype(int)
        # self.df = self.df[self.df["SUSPECT_REPORTED_AGE"] >= 12]

        # # Replace missing values in physical force columns with "N" for consistency 
        # ## NOTE TO SELF: Technically not required, but thought it'll be better to fillna since we are calling the result a "clean" dataset
        # self.df[features_force] = self.df[features_force].fillna(value="N")

        # # Also, I think we can remove "return self" for all?

    def save_cleaned_data(self, output_path=CLEAN_SQF):
        if not CLEAN_DATA_DIR.exists():
            CLEAN_DATA_DIR.mkdir()
        self.df.to_csv(output_path, index=False)

if __name__ == "__main__":
    cleaner = SQFDataCleaner()
    cleaner.load_data()
    cleaner.select_and_clean()
    cleaner.save_cleaned_data()
    