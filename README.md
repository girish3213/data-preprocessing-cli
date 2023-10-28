<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Preprocessing CLI</title>
</head>
<body>

<h1>Data Preprocessing CLI</h1>

<p>This is a command-line interface (CLI) tool for performing various data preprocessing tasks. It provides functionalities for handling missing data, encoding categorical variables, and scaling features. Additionally, it can generate plots to visualize the data.</p>

<h2>Usage</h2>

<h3>Missing Data Handling</h3>

<pre><code>
python cli.py missing --input-file data/input_data.csv --output-file data/output_data.csv
</code></pre>

<h3>Categorical Variable Encoding</h3>

<pre><code>
python cli.py encode --input-file data/input_data.csv --output-file data/encoded_data.csv --strategy onehot --columns Country,Purchased
</code></pre>

<h3>Feature Scaling</h3>

<h4>Standard Scaling</h4>

<pre><code>
python cli.py scale --input-file data/encoded_data.csv --output-file data/scaled_data.csv --scaler standard --columns 1,2
</code></pre>

<h4>Min-Max Scaling</h4>

<pre><code>
python cli.py scale --input-file data/input_data.csv --output-file data/scaled_data.csv --scaler minmax --columns 1,2
</code></pre>

<h3>Data Visualization</h3>

<pre><code>
python cli.py generate_plots --input-file input_data.csv --output-file output_plot.png --strategy heatmap --columns column1 column2
</code></pre>

<h2>How to Use</h2>

<ol>
    <li>Clone this repository to your local machine.</li>
    <li>Navigate to the project directory in your terminal.</li>
    <li>Run the desired commands from the examples provided above.</li>
</ol>

<h2>Dependencies</h2>

<ul>
    <li><a href="https://www.python.org/" target="_blank">Python</a> (>=3.6)</li>
    <li><a href="https://pandas.pydata.org/" target="_blank">Pandas</a></li>
    <li><a href="https://matplotlib.org/" target="_blank">Matplotlib</a></li>
</ul>


<h2>Acknowledgments</h2>

<p>Special thanks to the contributors and the open-source community for their valuable contributions.</p>

</body>
</html>
