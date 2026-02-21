class DevTrackError(Exception):
    """Base exception for DevTrack domain errors."""
    pass

class SessionActiveError(DevTrackError):
    """Raised when attempting to start a session while one is already active."""
    pass

class NoActiveSessionError(DevTrackError):
    """Raised when attempting to stop or access a session when none is active."""
    pass

class StorageError(DevTrackError):
    """Raised when storage operations fail."""
    pass