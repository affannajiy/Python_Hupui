'''
Based on Bro Code Weather App
Link: https://youtu.be/Q4377DH5Jso?si=OSo58860_c8BUvvH
'''

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon("weather_icon.png"))  # Add your own icon
        self.resize(400, 500)
        
        # Initialize UI
        self.init_ui()
        
        # Dark mode by default
        self.set_dark_theme()
        
    def init_ui(self):
        # Create widgets
        self.city_label = QLabel("Enter City Name")
        self.city_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.temperature_label = QLabel()
        self.weather_icon = QLabel()
        self.description_label = QLabel()
        self.details_label = QLabel()
        self.toggle_theme_button = QPushButton("Toggle Theme")
        
        # Set widget properties
        self.setup_widgets()
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.weather_icon, alignment=Qt.AlignCenter)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.description_label)
        
        # Horizontal layout for details
        details_layout = QHBoxLayout()
        details_layout.addWidget(self.details_label)
        details_layout.addWidget(self.toggle_theme_button)
        layout.addLayout(details_layout)
        
        self.setLayout(layout)
        
        # Connect signals
        self.search_button.clicked.connect(self.get_weather)
        self.toggle_theme_button.clicked.connect(self.toggle_theme)
        self.city_input.returnPressed.connect(self.get_weather)
        
    def setup_widgets(self):
        # Fonts
        title_font = QFont("Arial", 20, QFont.Bold)
        input_font = QFont("Arial", 14)
        temp_font = QFont("Arial", 36, QFont.Bold)
        desc_font = QFont("Arial", 16)
        
        # Apply fonts
        self.city_label.setFont(title_font)
        self.city_input.setFont(input_font)
        self.search_button.setFont(input_font)
        self.temperature_label.setFont(temp_font)
        self.description_label.setFont(desc_font)
        self.details_label.setFont(QFont("Arial", 10))
        
        # Alignments
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.details_label.setAlignment(Qt.AlignLeft)
        
        # Button styling
        self.search_button.setMinimumHeight(40)
        self.toggle_theme_button.setMaximumWidth(120)
        
        # Weather icon
        self.weather_icon.setAlignment(Qt.AlignCenter)
        
    def set_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                color: #ffffff;
            }
            QLineEdit {
                background-color: #3d3d3d;
                border: 2px solid #4d4d4d;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4d4d4d;
                border: none;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #5d5d5d;
            }
        """)
        self.is_dark = True
        
    def set_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                color: #000000;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #d0d0d0;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #e0e0e0;
                border: none;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)
        self.is_dark = False
        
    def toggle_theme(self):
        if self.is_dark:
            self.set_light_theme()
        else:
            self.set_dark_theme()
    
    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            self.show_error("Please enter a city name")
            return
            
        api_key = "a64a2f0c3f1535863073a63c1b494d18"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data['cod'] == 200:
                self.display_weather(data)
            else:
                self.show_error(f"Error: {data.get('message', 'Unknown error')}")
                
        except requests.exceptions.RequestException as e:
            self.show_error(f"Network error: {str(e)}")
    
    def display_weather(self, data):
        # Extract weather data
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15
        temp_f = (temp_k * 9/5) - 459.67
        weather_id = data['weather'][0]['id']
        description = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        
        # Update UI
        self.temperature_label.setText(f"{temp_c:.1f}°C / {temp_f:.1f}°F")
        self.weather_icon.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)
        
        details_text = (f"Humidity: {humidity}%\n"
                       f"Wind: {wind_speed} m/s\n"
                       f"Pressure: {pressure} hPa")
        self.details_label.setText(details_text)
    
    def show_error(self, message):
        self.temperature_label.setText(message)
        self.weather_icon.clear()
        self.description_label.clear()
        self.details_label.clear()
    
    @staticmethod
    def get_weather_emoji(weather_id):
        emoji_map = {
            range(200, 233): "⛈️",  # Thunderstorm
            range(300, 322): "🌧️",  # Drizzle
            range(500, 532): "🌧️",  # Rain
            range(600, 623): "❄️",  # Snow
            range(701, 742): "🌫️",  # Atmosphere
            800: "☀️",             # Clear
            range(801, 805): "☁️",  # Clouds
        }
        
        for weather_range, emoji in emoji_map.items():
            if isinstance(weather_range, range):
                if weather_id in weather_range:
                    return emoji
            elif weather_id == weather_range:
                return emoji
        return "🌈"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())