from flask import Flask, render_template, flash, redirect
from form import LoginForm
from flask.ext.googlemaps import GoogleMaps

app = Flask(__name__)
app.config.from_object('config')
user = {'nickname': 'Aaron'}
GoogleMaps(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', user=user)


@app.route('/hello')
def hello():
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
            },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
            }
    ]
    return render_template('home.html', title='Twitter', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)


if __name__ == '__main__':
    app.run()
