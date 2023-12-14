 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jokes = []

@app.route('/')
def home():
    return render_template('index.html', joke=random.choice(jokes))

@app.route('/create_joke', methods=['GET', 'POST'])
def create_joke():
    if request.method == 'POST':
        joke = request.form['joke']
        jokes.append(joke)
        return redirect(url_for('list_jokes'))
    else:
        return render_template('create_joke.html')

@app.route('/list_jokes')
def list_jokes():
    return render_template('list_jokes.html', jokes=jokes)

@app.route('/edit_joke/<joke_id>', methods=['GET', 'POST'])
def edit_joke(joke_id):
    joke = jokes[int(joke_id)]
    if request.method == 'POST':
        joke = request.form['joke']
        jokes[int(joke_id)] = joke
        return redirect(url_for('list_jokes'))
    else:
        return render_template('edit_joke.html', joke=joke)

@app.route('/delete_joke/<joke_id>')
def delete_joke(joke_id):
    del jokes[int(joke_id)]
    return redirect(url_for('list_jokes'))

if __name__ == '__main__':
    app.run()
