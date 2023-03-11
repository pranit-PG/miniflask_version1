from flask import Flask, url_for

# Flask` is the class we use to instantiate an application.
app = Flask(__name__)


@app.route('/hello')
def index():
    print(f"{__name__} running")

    print(url_for('index'))           # this statements will get print in terminal,as we can see in terminal
    print(url_for('profile', username='John Doe'))
    return 'index'


@app.route('/user/<username>')   # url binding
def profile(username):
    return f'{username}\'s profile'