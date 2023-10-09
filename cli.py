import click
from preprocessing import missing_values, encode_categorical, feature_scaling

@click.group()
def main():
    pass

@main.command()
@click.option('--input-file', type=click.Path(exists=True), help='Input file path')
@click.option('--output-file', type=click.Path(), help='Output file path')
def preprocess(input_file, output_file):
    if not output_file:
        output_file = click.prompt('Enter output file name (include .csv extension)')
    missing_values.impute_missing_values(input_file, output_file)

@main.command()
@click.option('--input-file', type=click.Path(exists=True), help='Input file path')
@click.option('--output-file', type=click.Path(), help='Output file path')
def encode(input_file, output_file):
    if not output_file:
        output_file = click.prompt('Enter output file name (include .csv extension)')
    encode_categorical.encode_categorical_values(input_file, output_file)

@main.command()
@click.option('--input-file', type=click.Path(exists=True), help='Input file path')
@click.option('--output-file', type=click.Path(), help='Output file path')
@click.option('--scaler', type=click.Choice(['standard', 'minmax']), default='standard', help='Type of scaler')
@click.option('--columns', type=str, help='Columns to scale (comma-separated)')
def scale(input_file, output_file, scaler, columns):
    if not output_file:
        output_file = click.prompt('Enter output file name (include .csv extension)')
    columns = list(map(int, columns.split(',')))
    feature_scaling.scale_features(input_file, output_file, scaler, columns)



if __name__ == '__main__':
    main()
