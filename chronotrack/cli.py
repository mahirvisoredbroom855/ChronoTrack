import typer

app = typer.Typer() #creates the base CLI app



from chronotrack.tracker import start_session, stop_session, log_sessions, export_data, tags_view, week_log






# Each Function Will
# 1. Parse JSON 2. Print Output



@app.command()
def start(
    task: str = typer.Argument(..., help="Task description in quotes"),
    tag: str = typer.Argument("General", help="Optional tag (default: General)")
):
    """
    Start tracking a task.
    """
    start_session(task, tag)




@app.command()
def stop():
    """
    Stop the current active task.
    """
    stop_session()




@app.command()
def log(time_range: str = typer.Argument("today", help="Choose from: today, yesterday, week, all")):
    """
    Show task log for a given time period.
    """
    log_sessions(time_range)







@app.command()
def export(format: str = typer.Argument("json", help="Format to export: json or csv")):
    """
    Export task log to a file (json or csv).
    """
    export_data(format)






@app.command()
def tags(tag_filter: str = typer.Argument(None, help="(Optional) Show only a specific tag")):
    """
    View all tags, or stats for a specific tag.
    """
    tags_view(tag_filter)




@app.command()
def week():
    """
    View a detailed summary report of your last 7 days.
    """
    week_log()







if __name__ == "__main__":
    app()