import sys
import random
import heapq
from collections import deque
from datetime import datetime
import matplotlib.pyplot as plt
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QLineEdit, QPushButton, QComboBox, QTextEdit, QGroupBox)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class WeatherPredictionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.current_month = datetime.now().month
        self.api_key = "a64a2f0c3f1535863073a63c1b494d18"  # OpenWeatherMap API key
        self.countries = {
            'USA': {'lat': 37.09, 'lon': -95.71},
            'Japan': {'lat': 36.20, 'lon': 138.25},
            'Australia': {'lat': -25.27, 'lon': 133.78},
            'France': {'lat': 46.23, 'lon': 2.21},
            'Brazil': {'lat': -14.24, 'lon': -51.93},
            'Malaysia': {'lat': 4.21, 'lon': 101.98}
        }
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Advanced Weather Prediction App")
        self.setGeometry(100, 100, 1000, 800)

        # Main layout
        main_layout = QHBoxLayout()
        
        # Left panel for controls
        control_panel = QVBoxLayout()
        
        # Country selection
        country_group = QGroupBox("Country Selection")
        country_layout = QVBoxLayout()
        
        self.country_label = QLabel("Select Country:")
        self.country_combo = QComboBox()
        self.country_combo.addItems(self.countries.keys())
        
        country_layout.addWidget(self.country_label)
        country_layout.addWidget(self.country_combo)
        country_group.setLayout(country_layout)
        control_panel.addWidget(country_group)
        
        # Month selection
        month_group = QGroupBox("Month Selection")
        month_layout = QVBoxLayout()
        
        self.month_label = QLabel("Select Month:")
        self.month_combo = QComboBox()
        self.month_combo.addItems([datetime(2023, i, 1).strftime('%B') for i in range(1, 13)])
        
        month_layout.addWidget(self.month_label)
        month_layout.addWidget(self.month_combo)
        month_group.setLayout(month_layout)
        control_panel.addWidget(month_group)
        
        # Buttons
        self.predict_button = QPushButton("Get Weather Prediction")
        self.bfs_button = QPushButton("Find Best Month (BFS)")
        self.astar_button = QPushButton("Find Best Month (A*)")
        self.visualize_button = QPushButton("Visualize Weather Data")
        self.city_button = QPushButton("Get Current Weather")
        
        control_panel.addWidget(self.predict_button)
        control_panel.addWidget(self.bfs_button)
        control_panel.addWidget(self.astar_button)
        control_panel.addWidget(self.visualize_button)
        control_panel.addWidget(self.city_button)
        
        # City input for current weather
        self.city_label = QLabel("Or enter city for current weather:")
        self.city_input = QLineEdit()
        control_panel.addWidget(self.city_label)
        control_panel.addWidget(self.city_input)
        
        # Output area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        control_panel.addWidget(self.output_text)
        
        # Right panel for visualization
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        main_layout.addLayout(control_panel, 40)
        main_layout.addWidget(self.canvas, 60)
        self.setLayout(main_layout)
        
        # Connect signals
        self.predict_button.clicked.connect(self.get_weather_prediction)
        self.bfs_button.clicked.connect(self.bfs_search_best_month)
        self.astar_button.clicked.connect(self.astar_search_best_month)
        self.visualize_button.clicked.connect(self.visualize_weather_data)
        self.city_button.clicked.connect(self.get_current_weather)
        
        # Style
        self.setStyleSheet("""
            QWidget {
                font-family: Arial;
                font-size: 14px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                margin: 5px 0;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTextEdit {
                background-color: #f8f8f8;
                border: 1px solid #ddd;
            }
            QGroupBox {
                border: 1px solid #ddd;
                margin-top: 10px;
                padding-top: 15px;
            }
            QLabel {
                margin: 5px 0;
            }
        """)
    
    def get_historical_weather(self, lat, lon, month):
        """Get historical weather data from OpenWeather API (using current data as proxy)"""
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data['cod'] == 200:
                temp_k = data["main"]["temp"]
                temp_c = temp_k - 273.15
                humidity = data["main"]["humidity"]
                weather_id = data["weather"][0]["id"]
                
                # Adjust values based on month (simulating seasonal variation)
                if month in [12, 1, 2]:  # Winter in northern hemisphere
                    if lat > 0:  # Northern hemisphere
                        temp_c += random.uniform(-10, 5)
                    else:  # Southern hemisphere
                        temp_c += random.uniform(5, 10)
                elif month in [6, 7, 8]:  # Summer in northern hemisphere
                    if lat > 0:  # Northern hemisphere
                        temp_c += random.uniform(5, 15)
                    else:  # Southern hemisphere
                        temp_c += random.uniform(-5, 5)
                
                # Estimate rainfall based on weather condition
                if weather_id >= 500 and weather_id <= 531:  # Rain
                    rainfall = random.uniform(10, 50)
                elif weather_id >= 300 and weather_id <= 321:  # Drizzle
                    rainfall = random.uniform(5, 15)
                else:
                    rainfall = random.uniform(0, 5)
                
                # Estimate sunshine hours (more in summer)
                if month in [6, 7, 8] and lat > 0:  # Northern summer
                    sunshine = random.uniform(8, 12)
                elif month in [12, 1, 2] and lat > 0:  # Northern winter
                    sunshine = random.uniform(4, 8)
                elif month in [12, 1, 2] and lat < 0:  # Southern summer
                    sunshine = random.uniform(8, 12)
                else:
                    sunshine = random.uniform(6, 10)
                
                return temp_c, rainfall, sunshine
            
        except requests.exceptions.RequestException:
            pass
        
        # Fallback values if API fails
        return random.uniform(10, 30), random.uniform(0, 20), random.uniform(5, 10)
    
    def calculate_weather_score(self, temp, rain, humidity, wind_speed):
        """Calculate a weather score based on real-time weather parameters"""
        # Normalize parameters (weights can be adjusted)
        temp_score = min(max((20 - abs(temp - 22)) / 20 * 10, 0), 10)  # Ideal around 22°C
        rain_score = min(max((100 - rain) / 100 * 10, 0), 10)  # Less rain is better
        humidity_score = min(max((100 - humidity) / 100 * 10, 0), 10)  # Lower humidity is better
        wind_score = min(max((20 - wind_speed) / 20 * 10, 0), 10)  # Less wind is better
        
        # Combine scores and scale to 20-25 range
        total = temp_score * 0.4 + rain_score * 0.3 + humidity_score * 0.2 + wind_score * 0.1
        return round(20 + (total / 10) * 5, 1)
    
    def get_weather_prediction(self):
        """Get weather prediction for selected country and month"""
        country = self.country_combo.currentText()
        month = self.month_combo.currentIndex() + 1
        
        if country not in self.countries:
            self.output_text.append(f"No data available for {country}")
            return
            
        lat, lon = self.countries[country]['lat'], self.countries[country]['lon']
        temp, rain, sunshine = self.get_historical_weather(lat, lon, month)
        
        # Get additional weather data for score calculation
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
        except:
            humidity = random.uniform(40, 80)
            wind_speed = random.uniform(0, 10)
        
        score = self.calculate_weather_score(temp, rain, humidity, wind_speed)
        
        result = (f"\nWeather prediction for {country} in {datetime(2023, month, 1).strftime('%B')}:\n"
                 f"Temperature: {round(temp, 1)}°C\n"
                 f"Rainfall: {round(rain, 1)}mm\n"
                 f"Humidity: {round(humidity, 1)}%\n"
                 f"Wind Speed: {round(wind_speed, 1)} m/s\n"
                 f"Sunshine hours: {round(sunshine, 1)}\n"
                 f"Weather score: {score}/25\n")
        
        self.output_text.append(result)
        return temp, rain, sunshine, humidity, wind_speed, score
    
    def bfs_search_best_month(self):
        """Uninformed search (BFS) to find the best month for a country"""
        country = self.country_combo.currentText()
        start_month = self.current_month
        
        if country not in self.countries:
            self.output_text.append(f"No data available for {country}")
            return
            
        lat, lon = self.countries[country]['lat'], self.countries[country]['lon']
        
        visited = set()
        queue = deque([start_month])
        best_month = None
        best_score = 0
        best_data = None
        
        while queue:
            month = queue.popleft()
            
            if month in visited:
                continue
                
            visited.add(month)
            
            temp, rain, sunshine, humidity, wind_speed, score = self.get_weather_prediction_for_month(country, month)
                
            if score > best_score:
                best_score = score
                best_month = month
                best_data = (temp, rain, sunshine, humidity, wind_speed)
                
            # Explore adjacent months
            prev_month = month - 1 if month > 1 else 12
            next_month = month + 1 if month < 12 else 1
            
            if prev_month not in visited:
                queue.append(prev_month)
            if next_month not in visited:
                queue.append(next_month)
                
        if best_month:
            month_name = datetime(2023, best_month, 1).strftime('%B')
            result = (f"\nBest month to visit {country} (BFS): {month_name}\n"
                     f"Temperature: {round(best_data[0], 1)}°C\n"
                     f"Rainfall: {round(best_data[1], 1)}mm\n"
                     f"Humidity: {round(best_data[3], 1)}%\n"
                     f"Wind Speed: {round(best_data[4], 1)} m/s\n"
                     f"Sunshine hours: {round(best_data[2], 1)}\n"
                     f"Weather score: {best_score}/25\n")
            self.output_text.append(result)
        else:
            self.output_text.append("No suitable month found.")
    
    def astar_search_best_month(self):
        """Informed search (A*) to find the best month for a country"""
        country = self.country_combo.currentText()
        start_month = self.current_month
        
        if country not in self.countries:
            self.output_text.append(f"No data available for {country}")
            return
            
        lat, lon = self.countries[country]['lat'], self.countries[country]['lon']
        
        def heuristic(month, target_score=25):
            if self.countries[country]['lat'] < 0:  # Southern hemisphere
                ideal_month = 12
            else:
                ideal_month = 6
                
            month_diff = min(abs(month - ideal_month), 12 - abs(month - ideal_month))
            return (month_diff / 6) * 5  # Max 5 points penalty
            
        open_set = []
        heapq.heappush(open_set, (0, start_month))
        
        came_from = {}
        g_score = {month: float('inf') for month in range(1, 13)}
        g_score[start_month] = 0
        
        f_score = {month: float('inf') for month in range(1, 13)}
        f_score[start_month] = heuristic(start_month)
        
        best_month = None
        best_score = 0
        best_data = None
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            temp, rain, sunshine, humidity, wind_speed, current_score = self.get_weather_prediction_for_month(country, current)
            
            if current_score > best_score:
                best_score = current_score
                best_month = current
                best_data = (temp, rain, sunshine, humidity, wind_speed)
                
            if current_score >= 24:  # Good enough score
                break
                
            neighbors = [
                current - 1 if current > 1 else 12,
                current + 1 if current < 12 else 1
            ]
            
            for neighbor in neighbors:
                temp, rain, sunshine, humidity, wind_speed, neighbor_score = self.get_weather_prediction_for_month(country, neighbor)
                    
                tentative_g_score = g_score[current] + (25 - neighbor_score)
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                    if neighbor not in [m for (_, m) in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        
        if best_month:
            month_name = datetime(2023, best_month, 1).strftime('%B')
            result = (f"\nBest month to visit {country} (A*): {month_name}\n"
                     f"Temperature: {round(best_data[0], 1)}°C\n"
                     f"Rainfall: {round(best_data[1], 1)}mm\n"
                     f"Humidity: {round(best_data[3], 1)}%\n"
                     f"Wind Speed: {round(best_data[4], 1)} m/s\n"
                     f"Sunshine hours: {round(best_data[2], 1)}\n"
                     f"Weather score: {best_score}/25\n")
            self.output_text.append(result)
        else:
            self.output_text.append("No suitable month found.")
    
    def get_weather_prediction_for_month(self, country, month):
        """Helper method to get weather prediction for a specific month"""
        lat, lon = self.countries[country]['lat'], self.countries[country]['lon']
        temp, rain, sunshine = self.get_historical_weather(lat, lon, month)
        
        # Get additional weather data for score calculation
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
        except:
            humidity = random.uniform(40, 80)
            wind_speed = random.uniform(0, 10)
        
        score = self.calculate_weather_score(temp, rain, humidity, wind_speed)
        return temp, rain, sunshine, humidity, wind_speed, score
    
    def visualize_weather_data(self):
        """Visualize weather data for selected country"""
        country = self.country_combo.currentText()
        
        if country not in self.countries:
            self.output_text.append(f"No data available for {country}")
            return
            
        months = list(range(1, 13))
        temps = []
        rains = []
        sunshine_hours = []
        
        for month in months:
            temp, rain, sunshine, _, _, _ = self.get_weather_prediction_for_month(country, month)
            temps.append(temp)
            rains.append(rain)
            sunshine_hours.append(sunshine)
        
        self.figure.clear()
        
        # Temperature plot
        ax1 = self.figure.add_subplot(3, 1, 1)
        ax1.plot(months, temps, 'r-')
        ax1.set_title(f'Weather Data for {country}')
        ax1.set_ylabel('Temperature (°C)')
        ax1.grid(True)
        
        # Rainfall plot
        ax2 = self.figure.add_subplot(3, 1, 2)
        ax2.plot(months, rains, 'b-')
        ax2.set_ylabel('Rainfall (mm)')
        ax2.grid(True)
        
        # Sunshine plot
        ax3 = self.figure.add_subplot(3, 1, 3)
        ax3.plot(months, sunshine_hours, 'y-')
        ax3.set_ylabel('Sunshine (hours)')
        ax3.set_xlabel('Month')
        ax3.grid(True)
        
        self.canvas.draw()
    
    def get_current_weather(self):
        """Get current weather for a city using OpenWeather API"""
        city = self.city_input.text()
        if not city:
            self.output_text.append("Please enter a city name")
            return
            
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data['cod'] == 200:
                self.display_current_weather(data)
            
        except requests.exceptions.HTTPError as http_error:
            self.output_text.append(f"HTTP Error: {http_error}")
        except requests.exceptions.RequestException as req_error:
            self.output_text.append(f"Request Error: {req_error}")
    
    def display_current_weather(self, data):
        """Display current weather data"""
        city = data['name']
        country = data['sys']['country']
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        humidity = data["main"]["humidity"]
        weather_id = data["weather"][0]["id"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        
        # Calculate score for current weather
        rainfall = 0  # Current API doesn't provide rainfall, we'd need a different endpoint
        score = self.calculate_weather_score(temp_c, rainfall, humidity, wind_speed)
        
        emoji = self.get_weather_emoji(weather_id)
        
        result = (f"\nCurrent weather in {city}, {country}:\n"
                 f"Temperature: {temp_c:.1f}°C\n"
                 f"Weather: {weather_desc} {emoji}\n"
                 f"Humidity: {humidity}%\n"
                 f"Wind Speed: {wind_speed} m/s\n"
                 f"Weather score: {score}/25\n")
        
        self.output_text.append(result)
    
    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 781:
            return "🌫"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherPredictionApp()
    weather_app.show()
    sys.exit(app.exec_())