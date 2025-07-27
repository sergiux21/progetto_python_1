import pandas as pd
def describe_columns(df):
    print(df.describe(include="all"))
    print("Valori nulli per colonna:")
    print(df.isnull().sum())