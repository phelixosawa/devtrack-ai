import json
import os

BASE_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_DIR, "..", "logs", "sessions.json")
ACTIVE_FILE = os.path.join(BASE_DIR, "..", "logs", "active_session.json")

class Storage:

    def _safe_load_json(self, path, default):
        if not os.path.exists(path):
            return default

        try:
            with open(path, "r") as f:
                content = f.read().strip()
                if not content:
                    return default
                return json.loads(content)
        except (json.JSONDecodeError, OSError):
            return default

    # sessions
    def get_sessions(self):
        return self._safe_load_json(LOG_FILE, [])

    def save_sessions(self, sessions):
        with open(LOG_FILE, "w") as f:
            json.dump(sessions, f, indent=4)

    def append_session(self, session):
        sessions = self.get_sessions()
        sessions.append(session)
        self.save_sessions(sessions)

    # active sessions
    def get_active_session(self):
        return self._safe_load_json(ACTIVE_FILE, None)

    def save_active_session(self, session):
        with open(ACTIVE_FILE, "w") as f:
            json.dump(session, f, indent=4)

    def clear_active_session(self):
        if os.path.exists(ACTIVE_FILE):
            os.remove(ACTIVE_FILE)

    def active_session_exists(self):
        return os.path.exists(ACTIVE_FILE)