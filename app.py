from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

# to hot load you can run on command line flask run --debug

# Create a route decorator
""" @app.route('/')
def index():
    return "<h1>Hello World!</h1>" """

@app.route('/')
def index():
    return render_template("index.html") #Flask knows that all templates are in template directory




#localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    return "<h1>Hello {}</h1>".format(name)