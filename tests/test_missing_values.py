import pandas as pd
from preprocessing import missing_values

def test_impute_missing_values(tmpdir):
    input_data = pd.DataFrame({'A': [1, 2, None, 4], 'B': [None, 2, 3, 4]})
    input_file = tmpdir.join("input_data.csv")
    output_file = tmpdir.join("output_data.csv")

    input_data.to_csv(input_file, index=False)
    missing_values.impute_missing_values(str(input_file), str(output_file))

    output_data = pd.read_csv(output_file)
    assert not output_data.isnull().any().any()

if __name__ == '__main__':
    test_impute_missing_values()
