# Weather Forecast Application 🌤️

A simple weather forecasting application built with Flask that fetches weather data from OpenWeatherMap API based on user input (city name).

---

## 📋 Project Overview

The **Weather Forecast Application** allows users to get the current weather details (temperature, humidity, wind speed, and description) for a city. The data is fetched from OpenWeatherMap API and displayed on a user-friendly web interface.

---

## 🛠️ Features

- **Location Input**:
  - Users can enter a city name to fetch the weather.
- **Weather Data**:
  - Displays city name, temperature (in Celsius), humidity, wind speed, and a brief description of the weather.
- **Error Handling**:
  - Displays error messages for invalid cities or missing input.

---

## 🔧 Technologies Used

- **Backend**: Flask (Python)
- **Weather API**: OpenWeatherMap API
- **Frontend**: HTML (via Jinja2 templates), CSS for basic styling.

---

## 📂 Code Structure

- **`app.py`**: 
  - Contains the Flask application logic, including routes for displaying the weather data and handling user input.
  
- **`templates/`**: 
  - **`index.html`**: The HTML template for the main page that contains a form for input and displays the weather data.

---

## 📖 How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hardikkaaccount/Python_mini_projects.git
   cd Python_mini_projects/WeatherForecast
