# Currency Converter API : Flask API learning
# 💡 Task: Build a USD to MYR Converter Endpoint
# ✅ Goal: User inputs USD, output shows MYR based on fixed rate (e.g. 4.70).
 
from flask import Flask,request,jsonify
import requests

converter=Flask(__name__)

@converter.route('/api/convert')

def convert_form():
    form = '''
    <form method= "POST" action="/api/converting">
        <input type = number name="USD" placeholder="USD"><br>
        <input type = submit value= "Convert">
    </form>
    '''
    return form

@converter.route('/api/converting', methods=["POST"])
def result_convert():
    USD = float(request.form['USD'])
    rate = 4.22
    RM = USD *rate
    data = {
        "USD": USD,
        "RM" : RM,
        "Rate":rate 
    }
    return jsonify(data)


'''@converter.route('/api/bitcoin', methods=["GET"])
def bitcoin():
    api_url = 'https://api.api-ninjas.com/v1/bitcoin'
    response= requests.get(api_url,headers={'X-Api-Key':key_dummy'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    
    return jsonify(response.text) ''' 

if __name__ == '__main__':
    converter.run(debug=True)
