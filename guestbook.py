from flask import Flask, flash, redirect, render_template, request, session


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

@app.route('/admin')
def admin_login():
    return render_template('login.html')

@app.route('/admin', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return admin_login()


if __name__ == '__main__':
    import os
    app.secret_key = os.urandom(12)
    app.run(debug=True)
