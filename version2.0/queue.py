import logging
from task import Task

class Queue():
    def __init__(self,q_max=10):
        self.q = []
        self.q_max = q_max

    def q_len(self):
        return len(self.q)

    def is_empty(self):
        return self.q_len() == 0

    def is_max(self):
        return self.q_len() == self.q_max
    
    def get_head(self):
        return self.q[0]

    def fifo_add(self,task):
        if self.is_max():
            self.q.pop(0)
            self.q.append(task)
        else:
            self.q.append(task)

    #def fifo_pop(self):
        #return self.q.pop(0)

    def priority_pop(self):
        new_q = sorted(self.q,key=lambda i:(i['task_priority'],i['started_time']))
        return new_q.pop(0)

    def priority_add(self,task):
        if self.is_empty() or not self.is_max():
            self.fifo_add(task)
        else: 
            if task["task_priority"] >= self.q["task_priority"]:
                self.priority_pop()
                self.q.append(task)
            else:
                print("failed add into the queue")

    def get_list(self):
        for i,item in enumerate(self.q):
            return([i,item])

    def kill(self,task):
        if task in self.q:
            self.q.remove(task)
            logging.info(f"task {task} is killed")
        