import pandas as pd
from pathlib import Path

RAW_SQF = Path(__file__).parent.parent / "raw-data/sqf-2025.xlsx"

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
        return self

    def save_cleaned_data(self, output_path="data/cleaned_sqf.csv"):
        self.df.to_csv(output_path, index=False)

if __name__ == "__main__":
    cleaner = SQFDataCleaner()
    cleaner.load_data().select_and_clean().save_cleaned_data()
    