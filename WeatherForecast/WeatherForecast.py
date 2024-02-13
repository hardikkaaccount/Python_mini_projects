import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = '67b56047a0b98a95bd2c918e5f1b4e27' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    if not location:
        return render_template('index.html', error='Please enter a location.')

    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            return render_template('index.html', error='City not found. Please try again.')

        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        weather_info = {
            'city': city_name,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'description': description.capitalize()
        }

        return render_template('index.html', weather=weather_info)
    except Exception as e:
        return render_template('index.html', error='An error occurred while fetching weather data. Please try again.')

if __name__ == '__main__':
    app.run(debug=True)
