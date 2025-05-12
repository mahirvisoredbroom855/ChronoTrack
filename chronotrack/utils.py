from datetime import datetime, timedelta

def format_pretty_time(iso_str: str) -> str:
    dt = datetime.fromisoformat(iso_str)
    return dt.strftime("%I:%M %p")

def is_active_session(session: dict) -> bool:
    return "start" in session and "end" not in session

def calculate_duration_minutes(start_iso: str, end_iso: str) -> float:
    start = datetime.fromisoformat(start_iso)
    end = datetime.fromisoformat(end_iso)
    return round((end - start).total_seconds() / 60, 2)

def get_week_range():
    now = datetime.now()
    week_ago = now - timedelta(days=6)
    return week_ago, now
