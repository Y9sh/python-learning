#  Try creating these routes on your own:
# /greet/<name> ➔ returns Good morning, <name>!
# /square/<int:num> ➔ returns square of num
# /profile/<username>/<int:age> ➔ returns username is age years old

from flask import Flask
from flask import render_template

test = Flask(__name__)


@test.route('/greet/<name>')
def greet(name):
    return f"Good Morning, {name}!"

@test.route('/square/<int:num>')
def number(num):
    return f"Square of {num} is {num*num}"

@test.route('/profile/<username>/<int:age>')
def profile(username, age):
    return f"Hi {username}, your age now is {age}"

@test.route('/home')
def home():
    return "Welcome to home page"

if __name__ == "__main__":
    test.run(debug=True)


'''
📝 Key Points
Don’t call route functions directly ➔ Flask calls them via routes.

Your use of <int:num> and multiple dynamic parameters is correct.

Your string formatting is neat and clear.


'''