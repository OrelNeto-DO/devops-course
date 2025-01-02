from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your API Key
API_KEY = '40392cb50e8faa1b5dd5822ab9e06913'

@app.route('/', methods=['GET', 'POST'])
def home():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')
        if city and country:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                weather = response.json()
            else:
                weather = {'error': 'City not found'}
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
