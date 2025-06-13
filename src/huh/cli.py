from typing import Optional
import typer

from huh.lastcmd import get_last_command

app = typer.Typer()

@app.command()
def hello(name: Optional[str] = None):
    typer.echo(f"Hello {name}" if name else "Hello World!")

@app.command()
def bye(name: Optional[str] = None):
    typer.echo(f"Bye {name}" if name else "Goodbye!")

@app.command()
def lastcmd(n: Optional[str] = None):
    try:
        num = int(n) if n is not None else 1
        typer.echo(f"You chose to see {num} last commands")
        print(get_last_command(num))
    except ValueError:
        typer.echo("bad input: please enter a valid number.")
