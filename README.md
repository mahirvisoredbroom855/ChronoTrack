# ⏱️ ChronoTrack

<div align="left">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/yourusername/ChronoTrack)
[![PyPI](https://img.shields.io/pypi/v/chronotrack.svg)](https://pypi.org/project/chronotrack/)

</div>

> **A Lightweight Yet Powerful CLI-based Time Tracker Engineered for Developers and Creators. Log Your Work Sessions, Breaks, Categorize with Tags, and Analyze Productivity Patterns—all From Your Terminal With Ease.**

---


## 🚀 Features

<div align="center">

![ChronoTrack Features](images/commands.png)

</div>

- **🟢 Session Management** - Start, stop, pause, and resume work sessions with precision.
- **⏱️ Break Tracking** - Automatically track break durations for better work/rest balancing.
- **🏷️ Tagging System** - Categorize your work with customizable tags for detailed reporting.
- **📊 Analytics** - Visualize productivity patterns with built-in statistics and charts.
- **📝 Session Notes** - Document context, achievements, and thoughts for each session.
- **📈 Weekly Reports** - Get insights into your productivity with comprehensive weekly summaries.
- **💹 Mail Based Github Like HTML Reports** - Track your progress more like github commits, in any frequency as your like.
- **🔄 Flexible Exports** - Export your data to JSON or CSV for external analysis.
- **🎨 Rich Terminal UI** - Enjoy a visually appealing interface with color-coding and formatting.
- **⚡ Performance** - Minimal resource usage with lightning-fast command execution.
- **🔒 Privacy-Focused** - All data stays local on your machine, no cloud sync required.

> **⚠️ WARNING: ChronoTrack does not automatically back up your data. Be sure to regularly export and back up your productivity data to prevent loss during system failures or accidental deletions.**

---


## 📦 Installation

### Via PyPI

```bash
pip install chronotrack-cli
```

### Via Conda

```bash
conda install -c conda-forge chronotrack
```

### From Source

```bash
git clone https://github.com/yourusername/ChronoTrack.git
cd ChronoTrack
pip install -e .
```

### System Requirements

- Python 3.8+
- 5MB disk space
- Linux, macOS, or Windows

> **💡 BEST PRACTICE: Always use a virtual environment when installing Python packages to avoid dependency conflicts.**
>
> ```bash
> python -m venv chronotrack-env
> source chronotrack-env/bin/activate  # On Windows: chronotrack-env\Scripts\activate
> pip install chronotrack
> ```

---

## 🚀 Quick Start

### 1. 🟢 Start tracking a task:

```bash
chronotrack start "Implement authentication module" backend
```

### 2. ⏸️ Take a break:

```bash
chronotrack pause
```

### 3. ▶️ Resume work:

```bash
chronotrack play
```

### 4. 🔴 Finish your session:

```bash
chronotrack stop "Completed user auth flow implementation"
```

### 5. 📈 View your day's progress:

```bash
chronotrack log today
```

> **⚠️ WARNING: Always stop your current session before starting a new one. Running multiple active sessions simultaneously can lead to data corruption or inaccurate time tracking.**

### 6. 📊 Setup HTML Github Like Report & Email Report:

```bash
chronotrack report
```

```bash
chronotrack setup-email-schedule
```

> **⚠️ WARNING: Make Sure You Have A Dedicated Domain inserted in email_sender.py and your specific API key in .env file inside your python package.**

---

## 💻 Command Reference

<div align="center">

![Command Help Screenshot](images/help.png)

</div>



---

## 🧪 Usage Examples

### Basic Workflow

```bash
# Start a coding session
chronotrack start "Refactor database models" database

# Take a quick break
chronotrack pause

# Resume coding
chronotrack play

# End session with a note
chronotrack stop "Completed normalization of user table"
```

### Viewing Your Progress

```bash
# See today's work
chronotrack log today

# Get weekly report
chronotrack week

# Analyze all sessions with the "frontend" tag
chronotrack log --tag frontend
```

### Managing Data

```bash
# Export to JSON
chronotrack export json

# Export to CSV with custom filename
chronotrack export csv --output my_productivity_data.csv

# Cancel a session (if you started by mistake)
chronotrack cancel
```

> **💡 BEST PRACTICE: Use descriptive task names and consistent tags to make your reports more meaningful and easier to analyze later.**
>
> Good example: `chronotrack start "Fix user authentication bug #123" backend`  
> Poor example: `chronotrack start "working" code`

---

## 📊 Productivity Reports

ChronoTrack provides powerful insights into your work patterns:

```bash
chronotrack week
```

You'll see a detailed report that includes:

- **Daily breakdown** of work hours
- **Efficiency metrics** showing focus time vs. break time
- **Tag distribution** showing where your time is allocated
- **Productivity trends** with standard deviation analysis
- **Break pattern analysis** for optimal rest scheduling
- **Comparative view** against your historical averages

### Report Options

<div align="center">

![Report Options](images/report_options.png)

</div>

Customize your reports with various options:

```bash
chronotrack week --chart          # Include visualization charts
chronotrack week --format compact # Condensed view for quick insights
chronotrack week --compare last   # Compare with previous week
```

### Report Example

<div align="center">

![Report Example](images/report_example.png)

</div>

> **💡 BEST PRACTICE: Review your weekly reports every Friday to identify productivity patterns and adjust your work habits for the following week.**

---


## 📬 Email Reports with Custom Domain (Resend Setup)

ChronoTrack allows you to **automatically send weekly productivity reports** via email using [Resend](https://resend.com). To do this properly and avoid spam issues, you'll need to verify your own domain.

![Report Example](images/htmlreport.png)


---

### ✅ Step 1: Set Up Your Domain on Resend

1. Go to [resend.com](https://resend.com) and sign up
2. Click on **"Domains"** → **"Add Domain"**
3. Enter your domain (e.g., `yourdomain.com`)
4. Add the DNS records (SPF, DKIM, Return-Path) to your domain’s registrar
5. Wait for the domain to be **verified** by Resend

---

### 🔑 Step 2: Generate API Key

1. Go to Resend → **"API Keys"**
2. Click **"Create API Key"**
3. Copy and save this key securely

---

### ⚙️ Step 3: Configure Environment Variables

Create a `.env` file:

```bash
chronotrack setup-email-schedule
```

Briefly Follow The Prompts, You Will Be Asked For Your API Key

> Your `SENDER_EMAIL` must match the verified domain.

---

### 📤 Step 4: Send a Report via CLI

You can generate and send your weekly report with:

```bash
chronotrack report --email yourname@yourdomain.com 
```

Or You Can Preview in Web

```bash
chronotrack report --preview 
```

This will:
- Build a complete HTML report of the past week
- Open it in your browser
- Send it to the specified email

---

### 🔁 Step 5: Enable Automated Weekly Reports

Run the guided setup:

```bash
chronotrack set_schedule
```

You’ll be asked:

```
📬 Enter the email to receive reports:
⏳ How often should reports be sent (in days)?
```

This creates a `user_preferences.json` file, and you can then schedule the following script to run daily:

```bash
python chronotrack_scheduled_runner.py
```

Use `crontab -e` or macOS `launchd` to schedule it.

---

> 💡 **Note**: You must keep the `.env` file available for environment access during scheduled execution.





## 💾 Data Management

### Data Storage

ChronoTrack stores your session data in a simple, human-readable JSON file:

```
YOUR_PROJECT/.chronotrack/session_log.json
```

### Data Format

Each session is stored in the following structure:

```json
{
  "task": "Write blog post",
  "tag": "writing",
  "start": "2025-05-13T12:30:00",
  "end": "2025-05-13T13:45:00",
  "duration_minutes": 65.0,
  "breaks": [
    {"start": "2025-05-13T13:00:00", "end": "2025-05-13T13:05:00", "duration_minutes": 5.0}
  ],
  "total_breaks": 1,
  "total_break_time": 5.0,
  "note": "Felt very focused",
  "note_added": true
}
```

### Exporting Data

Export your data for external analysis:

```bash
# Export to JSON
chronotrack export json

# Export to CSV
chronotrack export csv

# Specify custom output location
chronotrack export json --output ~/Documents/productivity_data.json
```

### Backup Recommendations

- Create periodic backups of your `session_log.json` file
- Consider version control for your productivity data
- Use the export functionality before major updates

> **⚠️ WARNING: The session data file can become corrupt if ChronoTrack is terminated improperly (e.g., during a system crash). Always ensure proper program termination and maintain regular backups.**
>
> **💡 BEST PRACTICE: Set up automatic backups of your `~/.chronotrack` directory using a scheduler or backup tool of your choice.**

---

## ⚙️ Customization

### Configuration File

Customize ChronoTrack behavior by creating a `~/.chronotrack/config.yaml` file:

```yaml
# Default tag when none is specified
default_tag: "general"

# Custom color scheme
colors:
  active: "green"
  paused: "yellow"
  stopped: "red"
  
# Auto-pause after inactivity (minutes)
auto_pause: 15

# Default report format
default_report: "detailed"
```

### Environment Variables

Configure behavior with environment variables:

```bash
# Set data directory
export CHRONOTRACK_DATA_DIR="/path/to/data"

# Enable debug mode
export CHRONOTRACK_DEBUG=1
```

> **💡 BEST PRACTICE: When setting a custom data directory with `CHRONOTRACK_DATA_DIR`, choose a location that's backed up by your existing backup system.**

---

## 🧠 Philosophy

ChronoTrack is built on several core principles:

1. **Terminal-First** - For developers who live in the command line
2. **Minimal Friction** - Track time without disrupting your workflow
3. **Data Ownership** - Your productivity data stays on your machine
4. **Insightful Analytics** - Measure to improve your work patterns
5. **Extensibility** - Simple data format for easy integration

ChronoTrack is designed for:
- **Developers** who prefer keyboard-driven tools
- **Writers & content creators** tracking creative output
- **Consultants & freelancers** who need accurate time logs
- **Students** managing study sessions and breaks
- Anyone seeking **actionable productivity insights**

> **💡 BEST PRACTICE: Incorporate ChronoTrack into your workflow gradual—start by tracking just one type of task before expanding to your full workday.**

---

## 🔧 Technical Details

### Project Structure

```
chronotrack/
├── cli.py          # CLI commands using Typer
├── tracker.py      # Core session logic
├── utils.py        # Shared helpers
├── __init__.py     # Versioning & packaging
├── session_log.json (autogenerated)
```

> **⚠️ WARNING: Do not manually edit the `session_log.json` file while ChronoTrack is running as this could cause data inconsistencies.**

### Best Practices

- Always **stop** a session before starting a new one
- Use **consistent tag names** for better reporting
- Add **detailed notes** for context when stopping a session
- Run **weekly reports** to identify productivity patterns
- Export data **regularly** for safekeeping

> **💡 BEST PRACTICE: Create aliases for your most commonly used ChronoTrack commands in your shell configuration file:**
>
> ```bash
> # Add to your .bashrc, .zshrc, or equivalent
> alias cts="chronotrack start"
> alias ctp="chronotrack pause"
> alias ctr="chronotrack play"  # resume
> alias cte="chronotrack stop"  # end
> alias ctl="chronotrack log today"
> alias ctl="chronotrack report --preview"
> alias ctl="chronotrack report --email <yourmail>"
> ```

---

## 🛠 Contributing

We welcome contributions from the community! Here's how to get started:

### Development Setup

```bash
git clone https://github.com/yourusername/ChronoTrack.git
cd ChronoTrack
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

> **💡 BEST PRACTICE FOR CONTRIBUTORS: Always write tests for new features and ensure all tests pass before submitting a pull request.**

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please include tests and documentation with your PR.

> **⚠️ WARNING FOR CONTRIBUTORS: Ensure your code maintains backward compatibility with existing data files to prevent users from losing their productivity data after updates.**

---

## 📄 License

ChronoTrack is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🙌 Acknowledgements

- [Typer](https://github.com/tiangolo/typer) for the elegant CLI framework
- [Rich](https://github.com/Textualize/rich) for beautiful terminal rendering
- You, for choosing ChronoTrack to boost your productivity

---

<div align="center">

> "You can't manage what you don't measure." — Peter Drucker

</div>