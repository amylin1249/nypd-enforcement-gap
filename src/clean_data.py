import pandas as pd
from pathlib import Path

RAW_SQF = Path(__file__).parent.parent / "raw-data/sqf-2025.xlsx"

class SQFDataCleaner:
    def __init__(self, file_path=RAW_SQF):
        self.file_path = file_path
        self.df = None
    
    def load_data(self):
        """
        loading all data from the file
        """
        self.df = pd.read_excel(self.file_path, engine="openpyxl")
        return self
    
    
    def select_and_clean(self):
        """data select and clean"""
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
    cleaner.load_data().select_and_clean().save_clean_data()

