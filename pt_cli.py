#!local/bin/python
import os

"""
This is the command line version of polite tasks. It reads a todo list and
prints the top task. Once you are done with it, it will mark it as complete and
append the date to it. After that, it will show you the next task on the list.
"""


class ToDoList(object):

    def __init__(self, todo_list='tasks.todo'):
        try:
            self.todo_list = open(todo_list, 'rw')
        except IOError:
            new_location = input('What list file would you like to open?')
            self.todo_list = open(new_location, 'rw')
