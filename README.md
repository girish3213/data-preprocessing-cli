# data-preprocessing-cli

python cli.py missing --input-file data/input_data.csv --output-file data/output_data.csv

python cli.py encode --input-file data/input_data.csv --output-file data/encoded_data.csv --strategy onehot --columns Country,Purchased



python cli.py scale --input-file data/encoded_data.csv --output-file data/scaled_data.csv --scaler standard --columns 1,2  
python cli.py scale --input-file data/input_data.csv --output-file data/scaled_data.csv --scaler minmax --columns 1,2

