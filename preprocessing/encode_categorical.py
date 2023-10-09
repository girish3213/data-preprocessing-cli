import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def encode_categorical_values(input_file, output_file, strategy, columns):
    data = pd.read_csv(input_file)

    if not columns:
        columns = data.select_dtypes(include=['object']).columns.tolist()

    if strategy == 'onehot':
        encoder = OneHotEncoder(drop='first', sparse=False)
        encoded_data = encoder.fit_transform(data[columns].astype(str))
        encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(columns))
    elif strategy == 'label':
        encoder = LabelEncoder()
        encoded_df = data[columns].apply(encoder.fit_transform)
    else:
        raise ValueError("Invalid encoding strategy. Use 'onehot' or 'label'.")

    data = pd.concat([data, encoded_df], axis=1)
    data.drop(columns=columns, inplace=True)

    data.to_csv(output_file, index=False)
