 
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


main.py


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
