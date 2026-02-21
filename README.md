# DevTrack AI

DevTrack AI is a lightweight CLI-based development session tracker designed to help developers monitor focused work sessions and generate daily productivity statistics.

---

## 🚀 Features

- Start and stop development sessions
- Real-time active session status
- Persistent session history (JSON storage)
- Daily productivity statistics
- Graceful CLI error handling (no stack traces)
- Clean separation of architecture layers

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd devtrack-ai
# Run commands from the project root
python3 -m src.cli <command>
# ▶ Start a session
python3 -m src.cli start --project <project-name> --desc "description" --tags tag1 tag2
# ⏹ Stop a session
python3 -m src.cli stop
# 📊 View active session
python3 -m src.cli status
# 📈 View today's statistics
python3 -m src.cli stats

🏗 Architecture
src/
│
├── cli.py               # CLI interface layer (user interaction + error boundary)
├── session_logger.py    # Session lifecycle management
├── analytics.py         # Aggregated statistics logic
├── logger_config.py    # System-level logging configuration
└── storage.py           # JSON persistence abstraction

💾 Data Storage
Session data is stored in:
logs/sessions.json
logs/active_session.json

---

## 📝 Logging

DevTrack AI logs unexpected system-level errors internally.

Log file location:

logs/devtrack.log

- Domain errors (e.g., starting an already active session) are handled gracefully and are not logged.
- Unexpected system errors are logged with full stack traces.
- Logging helps with debugging without exposing internal details to users.