import argparse
from task import Task
from worker import add,kill

parser = argparse.ArgumentParser(description="Please input parameters for task")
parser.add_argument('-p','--priority', type=int, choices=[0,1,2], default=0, help='the priority of task, choices => LOW = 0 MEDIUM = 1 HIGH = 2 (type=int)')
parser.add_argument('-m','--method', type=str, default='fifo', help=' the methods of add this task into queue fifo or priority (type=str)')
parser.add_argument('-g','--group', type=str, default='None', help=' the group of this task (type=str)')

if __name__=='__main__':
    args = parser.parse_args()
    priority = args.priority
    method = args.method
    group = args.group
    task1 = Task(task_priority = priority, methods=method, group=group)
    task = task1.task()
    add(task)
    print(task)
    
