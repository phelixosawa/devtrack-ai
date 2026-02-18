from datetime import datetime
from src.storage import Storage


class Analytics:

    def __init__(self):
        self.storage = Storage()

    def today_stats(self):

        sessions = self.storage.get_sessions()

        today = datetime.utcnow().date()

        today_sessions = [
            s for s in sessions
            if "end_time" in s and
            datetime.fromisoformat(s["end_time"]).date() == today
        ]

        if not today_sessions:
            return None

        total_minutes = sum(s["duration_minutes"] for s in today_sessions)
        session_count = len(today_sessions)
        average = total_minutes / session_count
        longest = max(s["duration_minutes"] for s in today_sessions)

        return {
            "total_minutes": round(total_minutes, 2),
            "session_count": session_count,
            "average_minutes": round(average, 2),
            "longest_minutes": round(longest, 2)
        }