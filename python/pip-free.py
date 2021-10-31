import typer
from os import system

app = typer.Typer()
URL_FOR_FREE = "--index-url http://nexus.prod.uci.cu/repository/pypi-proxy/simple/ --trusted-host nexus.prod.uci.cu"

@app.command()
def install(source: str, r: bool = False):
    if not r:
        typer.echo(typer.style(f"Installing package {source} ...", fg=typer.colors.YELLOW))
        system(f"python -m pip install {source} {URL_FOR_FREE}")
    else:
        typer.echo(typer.style(f"Installing requirements from {source} ...", fg=typer.colors.YELLOW))
        system(f"python -m pip install -r {source} {URL_FOR_FREE}")

@app.command()
def uninstall(source: str, r: bool = False):
    if not r:
        typer.echo(typer.style(f"Uninstalling package {source} ...", fg=typer.colors.YELLOW))
        system(f"python -m pip uninstall {source}")
    else:
        system(f"python -m pip uninstall -r {source}")

@app.command()
def freeze(src=""):
    typer.echo(typer.style("Freezing environment ...", fg=typer.colors.YELLOW))
    system(f"python -m pip freeze {str() if src == '' else '> ' + src}")
    
@app.command()
def list(outdated: bool = False):
    typer.echo(typer.style("Listing packages ...", fg=typer.colors.YELLOW))
    system(f"python -m pip list {'--outdated' if outdated else str()}")

@app.command()
def show(package: str):
    typer.echo(typer.style(f"Showing info about package {package} ...", fg=typer.colors.YELLOW))
    system(f"python -m pip show {package}")

@app.command()
def search(package: str):
    typer.echo(typer.style(f"Searching package {package} ...", fg=typer.colors.YELLOW))
    system(f"python -m search {package}")

if __name__ == "__main__":
    app()