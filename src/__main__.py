from .clean_data import SQFDataCleaner


def main():
    (
        SQFDataCleaner()
        .load_data()
        .select_and_clean()
        .consolidate_use_of_force()
        .save_cleaned_data()
    )


if __name__ == "__main__":
    print("Hello from Project NYPD Enforcement Gap!")
    print("Generation of the clean data file is now starting.")
    main()
    print(
        "The clean data file has been generated. Please load the individual Jupyter notebooks for the various models."
    )
