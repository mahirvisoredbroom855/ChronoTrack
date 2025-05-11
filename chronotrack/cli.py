import typer

app = typer.Typer() #creates the base CLI app


# Each Function Will
# 1. Parse JSON 2. Print Output



@app.command()
def start(task: str, tag: str = "General"):
    """
    Start tracking a task.
    """
    
    typer.echo(f"⏱️ Started: {task} | Tag: {tag}")


@app.command()
def stop():
    """
    Stop the current active task.
    """
    typer.echo("🛑 Task stopped.")



@app.command()
def log():
    """
    Show the log of tasks for today.
    """
    typer.echo("📜 Today's log: (stub for now)")





@app.command()
def export():
    """
    Export session logs to JSON or CSV.
    """

    from chronotrack.tracker import export_data
    export_data(format)




if __name__ == "__main__":
    app()