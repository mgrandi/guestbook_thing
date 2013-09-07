from flask import Flask, flash, redirect, render_template, request


app = Flask(__name__)
entries = []
entry_names = []


@app.route('/')
def index():
    return render_template(
        'index.html', entries=zip(entry_names, entries))

@app.route('/submit', methods=['POST'])
def submit():
    entries.append(request.form['entry'] or '<blank>')
    if not request.form['name']:
        flash("you must provide a name!")
        return redirect('/')
    entry_names.append(request.form['name'])
    return redirect('/')


if __name__ == '__main__':
    import os
    app.secret_key = os.urandom(12)
    app.run(debug=True)
