# 📝 Task:
# ✅ Connect your frontend HTML fetch POST to your Flask AI echo route.
# ✅ Test with different input (hello, palindrome, normal words).

from flask import Flask,request,jsonify, render_template

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/api/hello', methods =['POST'])

def hello():
    data = request.get_json()
    u = data.get('user')
    return jsonify({
        "input" : u
    })
    
@app.route('/api/palindrome', methods=['POST'])

def palindrome():
    pali = request.get_json()
    user = pali.get('user')
    palin = user == user[::-1]
    return jsonify({
        "palindrome": palin
    })
    
if __name__ == '__main__':
    app.run(debug=True)