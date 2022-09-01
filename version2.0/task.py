import uuid
from datetime import datetime

class Task():
    #task_key is pid/uuid
    global task_key
    #task_key is created randomly
    task_key = str(uuid.uuid4())

    def __init__(self, task_priority=None, methods=None, group=None):
        """
        task_priority: priority of the task => class TaskPriority():
        methods:how the task will be added into process
        status: task status
        """
        self.pid = task_key
        self.task_priority = task_priority   
        self.s_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        self.methods = methods
        self.group = group


    def key(self):
        return self.pid

    def todict(self):
        obj = {
            "task_priority": self.task_priority,
            "methods": self.methods,
            "started_time": self.s_time,
            "goup": self.group
        }
        return obj

    def task(self):
        task = {}
        key = self.key()
        task["pid"] = key
        task.update(self.todict())
        return task