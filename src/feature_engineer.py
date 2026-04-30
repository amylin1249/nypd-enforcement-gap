import pandas as pd
from pathlib import Path
from datatypes import FORCE_FEATURES, CLEAN_SQF, FINAL_SQF


class SQFFeatureEngineer:
    def __init__(self, df):
        self.df = df

    def consolidate_use_of_force(self):
        """
        Aggregates multiple physical force indicators into a single binary feature, 
        representing whether any form of physical escalation occurred during the stop.

        By combining specific actions such as handcuffing, drawing firearms, or using 
        OC spray, this method creates the primary dependent variable ("use_of_force") 
        for our classification model. This allows us to analyze the "escalation logic" 
        and identify systemic disparities in enforcement severity across different 
        demographic groups and precincts.

        Returns:
            self: The instance with the new 'use_of_force' target column added.

        """
        force_use_yes = (self.df[FORCE_FEATURES] == 1)
        self.df["use_of_force"] = force_use_yes.any(axis=1).astype(int)
        self.df.drop(columns=FORCE_FEATURES, inplace=True)
        

    def encode_data(self):
        """
        Converts categorical features into numerical format using One-Hot Encoding 
        to make the dataset compatible with linear models like Logistic Regression.

        This process creates individual binary columns (0 or 1) for each category 
        within features like Race, Sex, and Precinct. 
        By using 'drop_first=True', it prevents multicollinearity, which is essential 
        for the stability and interpretability of the model's coefficients.
        
        Returns:
            self: The instance with the transformed DataFrame. 
        
        """
        categorical_features = [
            "SUSPECT_RACE_DESCRIPTION", "SUSPECT_SEX", "STOP_WAS_INITIATED",
            "SUSPECTED_CRIME_DESCRIPTION"
        ]

        self.df = pd.get_dummies(self.df, columns=categorical_features, drop_first=True, dtype=float)
    
    def save_final_data(self, output_path=FINAL_SQF):
        self.df.to_csv(output_path, index=False)
    
if __name__ == "__main__":
    cleaned_df = pd.read_csv(CLEAN_SQF)
    feature_engineer = SQFFeatureEngineer(cleaned_df)
    feature_engineer.consolidate_use_of_force()
    feature_engineer.encode_data()
    feature_engineer.save_final_data()
