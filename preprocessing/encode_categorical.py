import pandas as pd

def encode_categorical_values(input_file, output_file):
    data = pd.read_csv(input_file)

    categorical_columns = data.select_dtypes(include=['object']).columns
    data[categorical_columns] = data[categorical_columns].astype('category')
    data[categorical_columns] = data[categorical_columns].apply(lambda x: x.cat.codes)

    data.to_csv(output_file, index=False)
