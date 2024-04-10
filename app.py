from flask import Flask, render_template
import random

# Create Flask Instance
app = Flask(__name__)

# Create a route decorator
""" @app.route('/')
def index():
    return "<h1>Hello World!</h1>" """

@app.route('/')
def index():
    weather = ["rainy","cloudy","misty"]
    # Select a random item
    random_weather = random.choice(weather)
    #first_name = "john"
    return render_template('index.html', random_weather=random_weather, weather=weather)

    #return render_template("index.html") #Flask knows that all templates are in template directory

#localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    #return "<h1>Hello {}</h1>".format(name)
    return render_template("user.html", user_name=name)

# to hot load you can run on command line flask run --debug