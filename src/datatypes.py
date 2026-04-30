from pathlib import Path

# Path to clean data directory
CLEAN_DATA_DIR = Path(__file__).parent.parent / "clean-data"

# Path to raw SQF data file
RAW_SQF = Path(__file__).parent.parent / "raw-data/sqf-2025.xlsx"

# Path to clean SQF data file with relevant values replaced and null rows removed
CLEAN_SQF = Path(__file__).parent.parent / "clean-data/cleaned_sqf.csv"

# Path to processed SQF data file with extracted feature and categorical data converted using OHE
FINAL_SQF = Path(__file__).parent.parent / "clean-data/final_sqf.csv"

FORCE_FEATURES = [
    "PHYSICAL_FORCE_CEW_FLAG",
    "PHYSICAL_FORCE_DRAW_POINT_FIREARM_FLAG",
    "PHYSICAL_FORCE_HANDCUFF_SUSPECT_FLAG",
    "PHYSICAL_FORCE_OC_SPRAY_USED_FLAG",
    "PHYSICAL_FORCE_OTHER_FLAG",
    "PHYSICAL_FORCE_RESTRAINT_USED_FLAG",
    "PHYSICAL_FORCE_WEAPON_IMPACT_FLAG",
]
