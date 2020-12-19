import bcrypt

import data
from flask import Flask, session, url_for, render_template, request, redirect

app = Flask(__name__)
app.secret_key = bcrypt.gensalt()


LOGIN_EMAIL = 'kaszczak.jaroslaw@outlook.com'
HASH_PW = b'$2b$12$s8Qmmgn4m6eDXuq1KTdgI.Y2yF6kfoXKBl9xk0C6Bj7Z7FxSTkEsG'
#qwerty

@app.route('/')
def index():
    session['first_time'] = 'tak' #dodawwanie nowych kluczy do sesji
    user_name=''
    if 'user_name' in session:
        user_name = session['user_name']
    return render_template('index.html', user_name=user_name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == LOGIN_EMAIL:
            if bcrypt.checkpw(password.encode('UTF-8'), HASH_PW):
                session['user_name'] = LOGIN_EMAIL
                return redirect(url_for('index'))
        return render_template('login_form.html', bad_login=True)

    elif request.method == 'GET':
        return render_template('login_form.html')

@app.route('/logout')
def logout():
    session.pop('user_name')
    return redirect(url_for('index'))


if __name__ == '__app__':
    app.run()
