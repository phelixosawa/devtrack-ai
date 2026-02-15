import json
import os
import uuid
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_DIR, "..", "logs", "sessions.json")
ACTIVE_FILE = os.path.join(BASE_DIR, "..", "logs", "active_session.json")


class SessionLogger:

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

    def start_session(self, project_name: str, description: str = "", tags=None):

        if os.path.exists(ACTIVE_FILE):
            active = self._safe_load_json(ACTIVE_FILE, None)
            if active:
                raise Exception("A session is already running.")
            else:
                # Corrupted or empty file → remove it
                os.remove(ACTIVE_FILE)

        session = {
            "id": str(uuid.uuid4()),
            "start_time": datetime.utcnow().isoformat(),
            "project": project_name,
            "description": description,
            "tags": tags or []
        }

        with open(ACTIVE_FILE, "w") as f:
            json.dump(session, f, indent=4)

        print("Session started.")

    def end_session(self):

        session = self._safe_load_json(ACTIVE_FILE, None)

        if not session:
            raise Exception("No active session.")

        end_time = datetime.utcnow()
        start_time = datetime.fromisoformat(session["start_time"])
        duration = (end_time - start_time).total_seconds() / 60

        session["end_time"] = end_time.isoformat()
        session["duration_minutes"] = round(duration, 2)

        self._save_session(session)

        if os.path.exists(ACTIVE_FILE):
            os.remove(ACTIVE_FILE)

        print("Session ended.")
        print(f"Duration: {round(duration, 2)} minutes")

    def _save_session(self, session_data):

        sessions = self._safe_load_json(LOG_FILE, [])

        sessions.append(session_data)

        with open(LOG_FILE, "w") as f:
            json.dump(sessions, f, indent=4)

    def get_active_session(self):
        session = self._safe_load_json(ACTIVE_FILE, None)

        if not session:
            return None
        
        start_time = datetime.fromisoformat(session["start_time"])
        now = datetime.utcnow()
        duration = (now - start_time).total_seconds() / 60

        session["running_minutes"] = round(duration, 2)

        return session