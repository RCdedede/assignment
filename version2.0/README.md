# Task Manager
task manager is to add task in to a task queue
2 ways to add task into queue
- add as fifo
- add as priority based on priority level and start_time

## pre-request
- python 3.x
(this task manager is in memory for temporary)

## Basic usage
### task
`key()` 
- task unique id/pid
`todict()` 
- collect all parmenters into a dict
`task()` 
- create a task with all parameters 
- example: `{'pid': '532347c9-06f1-4cdd-833c-4d29dacfb7f6', 'task_priority': 0, 'methods': 0, 'started_time': '2022-09-01T17:17:59Z', 'goup': 'None'}`

## queue
`q_len()` 
- get the length of queue
`is_empty()` 
- identify if queue is empty
`is_max()` 
- identify if queue is max
`get_head():`
- get the head of the queue
`fifo_add()`
- add new task into queue by FIFO method, if queue hit the max limit, the queue pop the head at first
`priority_pop()`
- the queue pop the head based the information of task on lowest task_priority and oldest start_time
`priority_add()`
- add new task into queue by FIFO method if the queue is not ; if queue hit the max limit, the queue pop the head at first and then add into tail
`get_list()`
- return the queue
`kill`
- kill a task

## worker
3 functions:
`add()`
- add a task based on user choice of methods
`get_list()`
- the same as `get_list()` in the queue.py
`kill(task)`
- the same as `kill()` in the queue.py

## main
- user is able to trigger the function based on user choice
`python3 main.py -p -m -g`
- example of return `{'pid': '9feef417-ca6b-4125-883a-a9ae80d3370f', 'task_priority': 0, 'methods': 'fifo', 'started_time': '2022-09-01T18:40:34Z', 'goup': 'None'}`

## todo 
- add unitest