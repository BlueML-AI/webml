"""Console script for webml."""
import sys
import click
from webml.webml import run_app


@click.command()
@click.option("--port",default=5000,help="Port number to run WebML on")
def main(port):
    """Console script for webml."""
    run_app(port)
    # click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
