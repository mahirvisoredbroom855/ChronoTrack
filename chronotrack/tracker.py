import json

from datetime import datetime
from pathlib import Path

from rich.table import Table
from rich.console import Console

import csv

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




def log_sessions():

    if not LOG_FILE.exists():
        print("📭 No tasks logged yet.")
        return
    
    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("📭 No tasks found in the log.")
        return
    
    table = Table(title="📜 ChronoTrack - Task Log")

    table.add_column("Task", style="cyan", no_wrap=True)
    table.add_column("Tag", style="magenta")
    table.add_column("Start", style="green")
    table.add_column("End", style="red")
    table.add_column("Duration (min)", justify="right", style="yellow")

    for session in data:
        task = session["task"]
        tag = session["tag"]
        start = session["start"]

        end = session.get("end", "—")
        duration = str(session.get("duration_minutes", "—"))

        table.add_row(task, tag, start, end, duration)

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
