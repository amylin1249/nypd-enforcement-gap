import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.exceptions import UndefinedMetricWarning
from datatypes import CLEAN_SQF
from train_linear_model import split_dataset
import warnings

# Silence warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)



if __name__ == "__main__":
    print()