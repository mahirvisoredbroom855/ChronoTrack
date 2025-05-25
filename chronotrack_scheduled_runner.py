
import time
import typer
from datetime import datetime, timedelta
from chronotrack.email_sender import send_email_report
from chronotrack.report_data import ReportBuilder
from chronotrack.generate_report import generate
from chronotrack.utils import load_preferences, save_preferences

def report_scheduler():
    prefs = load_preferences() # loading preferences 
    if not prefs:
        print("⚠️ No user preferences found. Please run `set_schedule` in CLI first.")
        return

    last_sent = datetime.fromisoformat(prefs["last_sent"])
    interval = timedelta(days=prefs["days"])
    now = datetime.now()

    if now - last_sent >= interval: # the full logic for troubleshooting
        print("📤 Time to send scheduled report!")
        builder = ReportBuilder()
        report_data = builder.build_full_report()
        html_path = generate(report_data)
        try:
            send_email_report(prefs["email"], html_path)
            prefs["last_sent"] = datetime.now().isoformat()
            save_preferences(prefs)
            print(f"✅ Report sent to {prefs['email']}")
        except Exception as e:
            print(f"❌ Failed to send report: {e}")
    else:
        print("🕒 Not time yet. No report sent.")





# keep this module, will be needed to run when __name__ == '__main__'


if __name__ == "__main__":
    report_scheduler()



# Good Work
