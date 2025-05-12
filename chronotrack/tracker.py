import json

from datetime import datetime, timedelta
from pathlib import Path

from rich.table import Table
from rich.console import Console

import csv

from collections import defaultdict




LOG_FILE = Path("session_log.json")

def start_session(task: str, tag: str = "General"):

    start_time = datetime.now().isoformat()


    entry = {
        
        "task": task,
        "tag": tag,
        "start": start_time
    }

    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"⏱️ Started task: {task} | Tag: {tag} | Time: {start_time}")
        



def stop_session():


    if not LOG_FILE.exists():
        print("⚠️ No active session to stop.")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)
    

    # Finding the latest session without any end

    for session in reversed(data):

        if "end" not in session:
            end_time = datetime.now()
            
            session["end"] = end_time.isoformat()


        start_time = datetime.fromisoformat(session["start"])
        session["duration_minutes"] = round((end_time - start_time).total_seconds() / 60, 2)

        with open(LOG_FILE, "w") as f:
            json.dump(data, f, indent=4)

        print(f"✅ Stopped task: {session['task']} | Duration: {session['duration_minutes']} min")
        return

    
    print("⚠️ All sessions already stopped.")





def log_sessions(time_range="today"):
    if not LOG_FILE.exists():
        print("📭 No session log found.")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    now = datetime.now()
    filtered = []

    for session in data:
        start_str = session.get("start")
        if not start_str:
            continue
        start_time = datetime.fromisoformat(start_str)

        # Filter based on time_range
        if time_range == "today":
            if start_time.date() != now.date():
                continue
        elif time_range == "yesterday":
            if start_time.date() != (now.date() - timedelta(days=1)):
                continue
        elif time_range == "week":
            if (now - start_time).days > 7:
                continue
        elif time_range == "all":
            pass
        else:
            print("❌ Invalid time range. Use: today, yesterday, week, or all")
            return

        filtered.append(session)

    if not filtered:
        print("📭 No tasks for selected range.")
        return

    title_map = {
        "today": "Today's Log",
        "yesterday": "Yesterday's Log",
        "week": "This Week's Log",
        "all": "All Time Log"
    }

    table = Table(title=f"📜 ChronoTrack – {title_map[time_range]}")

    table.add_column("Task", style="cyan", no_wrap=True)
    table.add_column("Tag", style="magenta")
    table.add_column("Start", style="green")
    table.add_column("End", style="red")
    table.add_column("Duration (min)", justify="right", style="yellow")

    for session in filtered:
        task = session["task"]
        tag = session.get("tag", "—")

        start_time = datetime.fromisoformat(session["start"])
        start_fmt = start_time.strftime("%I:%M %p")  # e.g., 09:45 AM

        end_str = session.get("end")
        if end_str:
            end_time = datetime.fromisoformat(end_str)
            end_fmt = end_time.strftime("%I:%M %p")
        else:
            end_fmt = "—"

        duration = str(session.get("duration_minutes", "—"))

        table.add_row(task, tag, start_fmt, end_fmt, duration)

    console = Console()
    console.print(table)










def export_data(format: str = "json"):
    if not LOG_FILE.exists():
        print("❌ No session log to export.")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("⚠️ Log file is empty.")
        return

    if format == "json":
        with open("export.json", "w") as f:
            json.dump(data, f, indent=4)
        print("✅ Exported as export.json")

    elif format == "csv":
        fieldnames = list(data[0].keys())  # Ensure consistent header order
        with open("export.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("✅ Exported as export.csv")

    else:
        print("❌ Unsupported format. Use --format json or --format csv.")







def tags_view(tag_filter=None):
    if not LOG_FILE.exists():
        print("📭 No tasks logged yet.")
        return

    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    tag_stats = defaultdict(lambda: {"count": 0, "duration": 0.0})

    for session in data:
        tag = session.get("tag", "Uncategorized")
        tag_stats[tag]["count"] += 1

        if "duration_minutes" in session:
            tag_stats[tag]["duration"] += session["duration_minutes"]

    if not tag_stats:
        print("📭 No tag data available.")
        return

    table = Table(title="🏷️ Tag Summary")

    table.add_column("Tag", style="cyan")
    table.add_column("Sessions", justify="right", style="magenta")
    table.add_column("Total Time (min)", justify="right", style="green")

    for tag, stats in tag_stats.items():
        if tag_filter and tag_filter != tag:
            continue
        table.add_row(tag, str(stats["count"]), f"{round(stats['duration'], 2)}")

    console = Console()
    console.print(table)
