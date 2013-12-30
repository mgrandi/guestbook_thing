import datetime

from flask import Flask, flash, redirect, render_template, request, session


app = Flask(__name__)
entries = []
entry_names = []
entry_dates = []


@app.route('/')
def index():
    return render_template(
        'index.html', entries=zip(entry_names, entry_dates, entries))


@app.route("/logout", methods=['POST'])
def logout():

    session['logged_in'] = False
    return redirect("/")



@app.route('/submit', methods=['POST'])
def submit():

    if not request.form['name']:
        flash("you must provide a name!")
        return redirect('/')
    entries.append(request.form['entry'] or '<blank>')
    entry_names.append(request.form['name'])
    entry_dates.append(datetime.datetime.now())
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
    return redirect("/")

@app.route('/moderate', methods=['POST'])
def moderate_posts():
    
    for key in request.form:
        if not key.startswith('remove_'):
            continue
        index = int(key.partition('_')[2])

        print("entries", entries)
        print("entry names", entry_names)
        del entries[index]
        del entry_names[index]

    return redirect('/')


if __name__ == '__main__':
    import os
    app.secret_key = os.urandom(12)
    app.run(debug=True)
