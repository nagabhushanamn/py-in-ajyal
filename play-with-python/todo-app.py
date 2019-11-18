import random

# data modeling in python

"""
    data-model : Todo = { id , title , compelted }
"""


class Todo:
    def __init__(self, title):
        self.id = random.randint(1, 100)
        self.title = title
        self.completed = False


class TodoService:

    def __init__(self):
        self.todos = []

    def addTodo(self, title):
        new_todo = Todo(title)
        self.todos.append(new_todo)

    def editTodo(self,id,new_title):
        print("..")

    def completeTodo(self,id):
        print("..")

    def completeAll(self):
        print("..")

    def deleteTodo(self, id):
        print("..")

    def clearCompleted(self, id):
        print("..")

    def viewTodos(self):
        for todo in self.todos:
            print(f"{todo.id} - {todo.title} - {todo.completed}")


service = TodoService()
service.addTodo("item1")
service.addTodo("item2")
service.viewTodos()
