import logging

from queue import Queue

def add(task):
    method = task['methods']
    if method == "priority":
        try:
            Queue.priority_add(task)
        except:
            logging.info("failed add new task")

    elif method == "fifo":
        try:
            Queue.fifo_add(task)
        except:
            logging.info("failed add new task")
    else:
        print("not valid method")

def get_list():
    return Queue.get_list()

def kill(task):
    Queue.kill(task)




    


