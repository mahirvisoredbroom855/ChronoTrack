import typer
from chronotrack.tracker import (
    start_session, stop_session, log_sessions,
    export_data, tags_view, week_log
)

app = typer.Typer(help="🕒 ChronoTrack — A simple CLI-based time tracker for developers and creators.")

# ---------------------------- Commands ----------------------------

@app.command()
def start(
    task: str = typer.Argument(..., help="Task name or description (in quotes if multi-word)"),
    tag: str = typer.Argument("General", help="Tag to categorize the task (default: General)")
):
    """
    🟢 Start tracking a new task.
    Creates a new time entry and blocks overlapping sessions.
    """
    start_session(task, tag)


@app.command()
def stop():
    """
    🔴 Stop the most recent active task.
    Records end time, duration, and optionally prompts for a note.
    """
    stop_session()


@app.command()
def log(
    time_range: str = typer.Argument("today", help="Time window: today, yesterday, week, or all")
):
    """
    📜 Show a log of tracked tasks.
    Use a time range to filter results: today, yesterday, week, all.
    """
    log_sessions(time_range)


@app.command()
def export(
    format: str = typer.Argument("json", help="Export format: json or csv")
):
    """
    💾 Export your task log to a file.
    Useful for reports, analysis, or backups.
    """
    export_data(format)


@app.command()
def tags(
    tag_filter: str = typer.Argument(None, help="(Optional) View stats for a specific tag only")
):
    """
    🏷️ View tag-based summaries.
    Shows count and total time spent for each tag.
    """
    tags_view(tag_filter)


@app.command()
def week():
    """
    📊 View a 7-day summary of your work.
    Choose from visual heat maps, tag analysis, or full reports.
    """
    week_log()

# ------------------------------------------------------------------

if __name__ == "__main__":
    app()
