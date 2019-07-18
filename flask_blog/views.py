# flask_blog/views.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が違います')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが違います')
        else:
            flash('ログインしました')
            session['logged_in'] = True
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    flash('ログアウトしました')
    session.pop('logged_in', None)
    return redirect(url_for('show_entries'))
