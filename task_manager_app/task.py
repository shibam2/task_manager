# task.py
# ============================
# Defines the Task class — a blueprint for all tasks managed by the app.

class Task:
    def __init__(self, name: str, description: str, priority: str):
        """Initialize a new Task object."""
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        """Return a readable string for displaying the task."""
        return f"{self.name} | {self.description} | Priority: {self.priority}"

    def to_dict(self):
        """Convert the Task object into a dictionary (for saving to JSON)."""
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Recreate a Task object from a dictionary."""
        return cls(data["name"], data["description"], data["priority"])
