#!/usr/bin/env python3

from typing import Optional
import typer
import getPass

app = typer.Typer()


@app.command()
def hello(name: str = None):
    if not name:
        name = getpass.getuser()
    typer.echo(f"Hello {name}!")

@app.command()
def store(n: Optional[str] = None):
    try:
        num = int(n) if n is not None else 1
        typer.echo(f"You chose to store last {num} commands")
    except ValueError:
        typer.echo("bad input: please enter a valid number.")

if __name__ == "__main__":
    app(prog_name="huhcli")
