import pandas as pd

def impute_missing_values(input_file, output_file):
    data = pd.read_csv(input_file)
    numeric_columns = data.select_dtypes(include=['number']).columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
    data.to_csv(output_file, index=False)
