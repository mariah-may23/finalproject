import numpy as np
import pandas as pd
import typer
from pandas import DataFrame

from visu import plot

app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command()
def main(file: str, column: str):
    df = read_file(file)
    check_col(df, column)
    plot(df, column)


# TODO how are we checking that the column is not a string OR FLOAT???

def read_file(file: str):
    try:
        df = pd.read_csv(file)
        return df
    except:
        typer.secho(
            "Incorrect file path or name", fg=typer.colors.RED
        )
        raise typer.Exit()


def check_col(df: DataFrame, column: str):
    if column not in df.columns:
        typer.secho(
            "A column with the given name does not exist", fg=typer.colors.RED
        )
        raise typer.Exit()
    elif df.dtypes[column] != np.int64:
        typer.secho(
            "The type of the column should be an integer", fg=typer.colors.RED
        )
        raise typer.Exit()


if __name__ == "__main__":
    typer.run(main)
