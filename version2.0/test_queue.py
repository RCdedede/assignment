import unittest
from queue import Queue

task1 = {'pid': '532347c9-06f1-4cdd-833c-4d29dacfb7f3', 'task_priority': 0, 'methods': 'fifo', 'started_time': '2022-09-01T17:17:53Z', 'goup': 'None'}
test_q = [
    {'pid': '532347c9-06f1-4cdd-833c-4d29dacfb7f1', 'task_priority': 0, 'methods': 'fifo', 'started_time': '2022-09-01T17:17:54Z', 'goup': 'None'},
    {'pid': '532347c9-06f1-4cdd-833c-4d29dacfb7f2', 'task_priority': 1, 'methods': 'fifo', 'started_time': '2022-09-01T17:17:55Z', 'goup': 'None'}
]

def test_fifo_add(task1):
    print(Queue.fifo_add(task1))

def test_fifo_pop(test_q):
    print(Queue.test_q.fifo_pop(test_q))

def test_get_list(test_q):
    print(Queue.get_list(test_q))

def test_priority_pop(test_q):
    print(Queue.test_q.fifo_pop(test_q))

def test_priority_add(task1):
    print(Queue.test_q.fifo_pop(task1))