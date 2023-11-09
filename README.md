 ### Problem

The problem is to create a Flask application that allows users to create, read, update, and delete (CRUD) tasks.

### Design

The application will consist of the following HTML files:

* `index.html`: The home page of the application. This page will display a list of all the tasks in the database.
* `create_task.html`: A page that allows users to create a new task.
* `read_task.html`: A page that displays a single task.
* `update_task.html`: A page that allows users to update a task.
* `delete_task.html`: A page that allows users to delete a task.

The application will also have the following routes:

* `/`: The home page of the application.
* `/create_task`: A route that handles the creation of a new task.
* `/read_task/<int:task_id>`: A route that handles the reading of a single task.
* `/update_task/<int:task_id>`: A route that handles the updating of a task.
* `/delete_task/<int:task_id>`: A route that handles the deletion of a task.

The following code is the design for the Flask application:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/create_task", methods=["GET", "POST"])
def create_task():
    if request.method == "GET":
        return render_template("create_task.html")
    else:
        task = request.form.get("task")
        tasks.append(task)
        return redirect(url_for("index"))

@app.route("/read_task/<int:task_id>")
def read_task(task_id):
    task = tasks[task_id]
    return render_template("read_task.html", task=task)

@app.route("/update_task/<int:task_id>", methods=["GET", "POST"])
def update_task(task_id):
    if request.method == "GET":
        task = tasks[task_id]
        return render_template("update_task.html", task=task)
    else:
        task = request.form.get("task")
        tasks[task_id] = task
        return redirect(url_for("index"))

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
```