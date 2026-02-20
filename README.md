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
# Start session
python3 -m src.cli start --project <project-name> --desc "description" --tags tag1 tag2
# Example
python3 -m src.cli start --project devtrack-ai --desc "Refactoring CLI boundary" --tags backend refactor
# Stop session
python3 -m src.cli stop
# View active session
python3 -m src.cli status
# View today's statistics
python3 -m src.cli stats
```bash 