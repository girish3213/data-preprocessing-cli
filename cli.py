import click
from preprocessing import missing_values

@click.group()
def main():
    pass

@main.command()
@click.option('--input-file', type=str, required=True, help='Input data file path')
@click.option('--output-file', type=str, required=True, help='Output file path')
def preprocess(input_file, output_file):
    missing_values.impute_missing_values(input_file, output_file)

if __name__ == '__main__':
    main()