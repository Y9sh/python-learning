#🌟 📝 POST Route Practice – Step by Step
# 💡 📌 Goal
# ✅ Make a POST route that:
# Accepts two numbers from an HTML form
# Returns their sum

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <form method="POST" action="/add">
            <input type="number" name="num1" placeholder="First number"><br>
            <input type="number" name="num2" placeholder="Second number"><br>
            <input type="text" name="name" placeholder="Name"><br>
            <input type="submit" value="Calculate Sum">
        </form>
    '''

@app.route('/add', methods=['POST'])
def sum_numbers():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    name = str(request.form['name'])
    total = num1 + num2
    return f"Welcome to {name} The sum of {num1} and {num2} is {total}"

if __name__ == "__main__":
    app.run(debug=True)
