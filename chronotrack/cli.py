import typer

app = typer.Typer() #creates the base CLI app



from chronotrack.tracker import start_session, stop_session, log_sessions, export_data






# Each Function Will
# 1. Parse JSON 2. Print Output



@app.command()
def start(task: str, tag: str = "General"):
    """
    Start tracking a task.
    """
    start_session(task, tag)



    typer.echo(f"⏱️ Started: {task} | Tag: {tag}")


@app.command()
def stop():
    """
    Stop the current active task.
    """
    stop_session()


    typer.echo("🛑 Task stopped.")



@app.command()
def log():
    """
    Show the log of tasks for today.
    """
    log_sessions()


    typer.echo("📜 Today's log: (stub for now)")





@app.command()
def export():
    """
    Export session logs to JSON or CSV.
    """
    export_data(format)




if __name__ == "__main__":
    app()