from typing import Optional

try:
    from importlib.metadata import entry_points
except ImportError:
    from importlib_metadata import entry_points

import typer



__version__ = "0.1.0"


def create_app():
    app = typer.Typer(help="maat-scripts")

    @app.command()
    def main(
        version: Optional[bool] = typer.Option(
            None, "--version", callback=version_callback, is_eager=True
        )
    ):
        pass

    load_commands(app)

    return app


def version_callback(value: bool):
    if value:
        typer.echo(f"maat-scripts version: {__version__}")
        raise typer.Exit()


def load_commands(app=None):
    for ep in entry_points().get("maat.scripts", []):
        print("Loading cli module: %s" % ep.name)
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)


app = create_app()

if __name__ == "__main__":
    # cliapp = create_app()
    app()
