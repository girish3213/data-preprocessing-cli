import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plots(input_file, output_file, strategy, columns):
    data = pd.read_csv(input_file)
    data = pd.get_dummies(data)
    if not columns:
        columns = data.select_dtypes(include=['object']).columns.tolist()

    if strategy == 'heatmap':
        plt.figure(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap='inferno', linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.show()
    elif strategy == 'pairplot':
        plt.figure(figsize=(10, 8))
        sns.pairplot(data)
    elif strategy == 'countplot':
        boolean_columns = df.select_dtypes(include=bool)
        melted_df = boolean_columns.melt(var_name='Column', value_name='Is_True')
        plt.figure(figsize=(12, 6))
        sns.countplot(data=melted_df, x='Column', hue='Is_True')
        plt.xlabel('Column')
        plt.ylabel('Count')
        plt.title('Count of values for categorical columns')
        plt.xticks(rotation=45)
        plt.show()
    else:
        raise ValueError("Invalid plotting strategy. Use 'heatmap' or 'pairplot' or 'countplot'.")

