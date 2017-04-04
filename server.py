from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
