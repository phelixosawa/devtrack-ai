import uuid
from datetime import datetime
from src.storage import Storage
from src.exceptions import SessionActiveError, NoActiveSessionError

class SessionLogger:

    def __init__(self):
        self.storage = Storage()

    def start_session(self, project_name: str, description: str = "", tags=None):
        
        if self.storage.get_active_session():
            raise SessionActiveError("A session is already running.")

        session = {
            "id": str(uuid.uuid4()),
            "start_time": datetime.utcnow().isoformat(),
            "project": project_name,
            "description": description,
            "tags": tags or []
        }

        self.storage.save_active_session(session)

        print("Session started.")

    def end_session(self):

        session = self.storage.get_active_session()

        if not session:
            raise NoActiveSessionError("No active session.")

        end_time = datetime.utcnow()
        start_time = datetime.fromisoformat(session["start_time"])
        duration = (end_time - start_time).total_seconds() / 60

        session["end_time"] = end_time.isoformat()
        session["duration_minutes"] = round(duration, 2)

        self.storage.append_session(session)
        self.storage.clear_active_session()

        print("Session ended.")
        print(f"Duration: {round(duration, 2)} minutes")

    def get_active_session(self):

        session = self.storage.get_active_session()

        if not session:
            return None

        start_time = datetime.fromisoformat(session["start_time"])
        now = datetime.utcnow()
        duration = (now - start_time).total_seconds() / 60

        session["running_minutes"] = round(duration, 2)

        return session