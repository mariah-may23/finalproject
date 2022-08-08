# import the dependencies
import numpy as np
import pandas as pd
import typer
from pandas import DataFrame

# import the benchmark graph module
from visu import plot


# define main function in a style of the Controller pattern
# expects two CLI arguments: path to the .csv file and a name of the column in the file
def main(file: str, column: str):
    # read .csv file into a Pandas DataFrame
    df = read_file(file)
    # check that the given column exists and its datatype is integer
    check_col(df, column)
    # display the benchmark for the given data
    plot(df, column)


# reads file from the given path into a dataframe
def read_file(file: str):
    try:
        df = pd.read_csv(file)
        return df
    # catch any errors during reading the file
    except:
        # let user know that there is a mistake in the path
        typer.secho(
            "Incorrect file path or name", fg=typer.colors.RED  # displays the message in red
        )
        raise typer.Exit()


# checks that the given column exists in the dataframe
def check_col(df: DataFrame, column: str):
    # let user know that the given column does not exist
    if column not in df.columns:
        typer.secho(
            "A column with the given name does not exist", fg=typer.colors.RED  # displays the message in red
        )
        raise typer.Exit()
    # let user know that the given column's data type is not integer
    elif df.dtypes[column] != np.int64:
        typer.secho(
            "The type of the column should be an integer", fg=typer.colors.RED  # displays the message in red
        )
        raise typer.Exit()


if __name__ == "__main__":
    typer.run(main)
