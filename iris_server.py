"""_summary_
We are creating a new tab for our shiny app to display the iris dataset loaded earlier.
The CSV file is loaded into a pandas DataFrame and the number of rows is counted.
The server functions are defined in the get_iris_server_functions() function.

"""


import pathlib
from shiny import render
import pandas as pd
import seaborn as sns

def get_iris_server_functions(input, output, session):
    """Define functions to create UI outputs."""

    path_to_data = pathlib.Path(__file__).parent.joinpath("iris.csv")
    original_df = pd.read_csv(path_to_data)

    # Use the len() function to get the number of rows in the DataFrame.
    total_count = len(original_df)

    @output
    @render.table
    def iris_table():
        return original_df

    @output
    @render.text
    def iris_record_count_string():
        message = f"Showing {total_count} records"
        return message

    @output
    @render.plot
    def iris_plot():
        plt = sns.scatterplot(
            data=original_df,
            x="sepal_length",
            y="sepal_width",
        )
        return plt

    # return a list of function names for use in reactive outputs
    return [
        iris_table,
        iris_record_count_string,
        iris_plot,
    ]
