from turtle import update
import unittest
from task import Task
from test.t import update_task

class TestTask(unittest.TestCase):
    def test_todict_1(self):
        t=Task(task_priority=1, methods='fifo', group='Data')
        print(t.todict())

    def test_todict_2(self):
        t=Task(task_priority=2, methods='fifo', group='IT')
        self.assertEqual(t.todict()["task_priority"],2)



if __name__=='__main__':
    unittest.main()