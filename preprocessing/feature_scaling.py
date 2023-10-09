from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def scale_features(input_file, output_file, scaler_type, columns):
    data = pd.read_csv(input_file)

    if scaler_type == 'standard':
        scaler = StandardScaler()
    elif scaler_type == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Invalid scaler type. Use 'standard' or 'minmax'.")

    data_to_scale = data.iloc[:, columns]
    scaled_data = scaler.fit_transform(data_to_scale)

    scaled_df = pd.DataFrame(scaled_data, columns=data_to_scale.columns)

    for i, col in enumerate(columns):
        data.iloc[:, col] = scaled_df.iloc[:, i]

    data.to_csv(output_file, index=False)

