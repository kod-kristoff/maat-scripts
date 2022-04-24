from pathlib import Path

import typer

from . import merge_comp_freqs

subapp = typer.Typer()


@subapp.command()
def comp_freqs(
    revs_file: Path = typer.Argument(...),
    comp_file: Path = typer.Argument(...)
):
    try:
        merge_comp_freqs.merge(revs_file, comp_file)
    except merge_comp_freqs.MergeError as err:
        typer.echo(f"Error: {str(err)}", err=True)
        raise typer.Exit(2)


def init_app(app: typer.Typer):
    app.add_typer(subapp, name="merge")

