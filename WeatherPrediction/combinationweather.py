import sys
import heapq
from collections import deque, defaultdict
import random
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
        self.countries = ['USA', 'Japan', 'Australia', 'France', 'Brazil', 'Malaysia']
        self.initUI()
        self.load_country_data()

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
        self.country_combo.addItems(self.countries)
        
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
    
    def load_country_data(self):
        """Load historical weather data for countries"""
        self.historical_data = {
            'USA': {
                1: (5, 80, 4), 2: (7, 70, 5), 3: (12, 65, 6), 4: (16, 60, 7),
                5: (20, 55, 8), 6: (25, 50, 9), 7: (28, 45, 10), 8: (27, 50, 9),
                9: (23, 55, 7), 10: (17, 60, 6), 11: (11, 70, 4), 12: (6, 75, 3)
            },
            'Japan': {
                1: (6, 50, 5), 2: (7, 60, 5), 3: (10, 90, 6), 4: (16, 120, 6),
                5: (20, 130, 6), 6: (24, 180, 5), 7: (28, 150, 6), 8: (29, 140, 7),
                9: (25, 180, 5), 10: (19, 130, 6), 11: (14, 80, 6), 12: (9, 50, 5)
            },
            'Australia': {
                1: (28, 80, 8), 2: (27, 90, 8), 3: (25, 70, 8), 4: (22, 50, 7),
                5: (18, 40, 7), 6: (15, 30, 6), 7: (14, 30, 7), 8: (16, 30, 8),
                9: (19, 35, 8), 10: (22, 50, 8), 11: (25, 60, 9), 12: (27, 70, 9)
            },
            'France': {
                1: (6, 60, 3), 2: (7, 50, 4), 3: (11, 55, 5), 4: (14, 50, 6),
                5: (18, 60, 7), 6: (22, 50, 8), 7: (24, 40, 9), 8: (24, 50, 8),
                9: (20, 60, 7), 10: (15, 70, 5), 11: (10, 70, 4), 12: (7, 60, 3)
            },
            'Brazil': {
                1: (28, 200, 6), 2: (28, 180, 6), 3: (28, 170, 6), 4: (27, 120, 7),
                5: (26, 90, 7), 6: (25, 60, 8), 7: (25, 50, 8), 8: (26, 50, 8),
                9: (26, 80, 7), 10: (27, 120, 6), 11: (27, 150, 6), 12: (28, 190, 6)
            },
            'Malaysia': {
                1: (28, 200, 6), 2: (28, 180, 6), 3: (29, 220, 6), 4: (29, 250, 6),
                5: (29, 200, 6), 6: (29, 180, 6), 7: (28, 180, 6), 8: (28, 190, 6),
                9: (28, 200, 6), 10: (28, 250, 5), 11: (28, 300, 5), 12: (28, 250, 5)
            }
        }
    
    def calculate_weather_score(self, temp, rain, sunshine):
        """Calculate a weather score between 20-25 based on weather parameters"""
        temp_score = min(max((temp - 10) / 25 * 10, 0), 10)
        rain_score = min(max((100 - rain) / 100 * 10, 0), 10)
        sunshine_score = min(max(sunshine / 10 * 10, 0), 10)
        
        total = temp_score * 0.5 + rain_score * 0.3 + sunshine_score * 0.2
        return round(20 + (total / 10) * 5, 1)
    
    def get_weather_prediction(self):
        """Get weather prediction for selected country and month"""
        country = self.country_combo.currentText()
        month = self.month_combo.currentIndex() + 1
        
        if country not in self.historical_data:
            self.output_text.append(f"No data available for {country}")
            return
            
        if month not in self.historical_data[country]:
            self.output_text.append(f"No data available for month {month}")
            return
            
        temp, rain, sunshine = self.historical_data[country][month]
        # Add some randomness to simulate prediction
        temp += random.uniform(-2, 2)
        rain += random.uniform(-10, 10)
        sunshine += random.uniform(-1, 1)
        
        score = self.calculate_weather_score(temp, rain, sunshine)
        
        result = (f"\nWeather prediction for {country} in {datetime(2023, month, 1).strftime('%B')}:\n"
                 f"Temperature: {round(temp, 1)}°C\n"
                 f"Rainfall: {round(rain, 1)}mm\n"
                 f"Sunshine hours: {round(sunshine, 1)}\n"
                 f"Weather score: {score}/25\n")
        
        self.output_text.append(result)
    
    def bfs_search_best_month(self):
        """Uninformed search (BFS) to find the best month for a country"""
        country = self.country_combo.currentText()
        start_month = self.current_month
        
        if country not in self.historical_data:
            self.output_text.append(f"No data available for {country}")
            return
            
        visited = set()
        queue = deque([start_month])
        best_month = None
        best_score = 0
        
        while queue:
            month = queue.popleft()
            
            if month in visited:
                continue
                
            visited.add(month)
            
            temp, rain, sunshine = self.historical_data[country][month]
            score = self.calculate_weather_score(temp, rain, sunshine)
                
            if score > best_score:
                best_score = score
                best_month = month
                
            # Explore adjacent months
            prev_month = month - 1 if month > 1 else 12
            next_month = month + 1 if month < 12 else 1
            
            if prev_month not in visited:
                queue.append(prev_month)
            if next_month not in visited:
                queue.append(next_month)
                
        if best_month:
            month_name = datetime(2023, best_month, 1).strftime('%B')
            self.output_text.append(f"\nBest month to visit {country} (BFS): {month_name} (Score: {best_score}/25)")
        else:
            self.output_text.append("No suitable month found.")
    
    def astar_search_best_month(self):
        """Informed search (A*) to find the best month for a country"""
        country = self.country_combo.currentText()
        start_month = self.current_month
        
        if country not in self.historical_data:
            self.output_text.append(f"No data available for {country}")
            return
            
        def heuristic(month, target_score=25):
            if country == 'Australia' or country == 'Brazil':
                ideal_month = 12
            else:
                ideal_month = 6
                
            month_diff = min(abs(month - ideal_month), 12 - abs(month - ideal_month))
            return (month_diff / 6) * 5
            
        open_set = []
        heapq.heappush(open_set, (0, start_month))
        
        came_from = {}
        g_score = {month: float('inf') for month in range(1, 13)}
        g_score[start_month] = 0
        
        f_score = {month: float('inf') for month in range(1, 13)}
        f_score[start_month] = heuristic(start_month)
        
        best_month = None
        best_score = 0
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            temp, rain, sunshine = self.historical_data[country][current]
            current_score = self.calculate_weather_score(temp, rain, sunshine)
            
            if current_score > best_score:
                best_score = current_score
                best_month = current
                
            if current_score >= 24:
                break
                
            neighbors = [
                current - 1 if current > 1 else 12,
                current + 1 if current < 12 else 1
            ]
            
            for neighbor in neighbors:
                temp, rain, sunshine = self.historical_data[country][neighbor]
                neighbor_score = self.calculate_weather_score(temp, rain, sunshine)
                    
                tentative_g_score = g_score[current] + (25 - neighbor_score)
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                    if neighbor not in [m for (_, m) in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        
        if best_month:
            month_name = datetime(2023, best_month, 1).strftime('%B')
            self.output_text.append(f"\nBest month to visit {country} (A*): {month_name} (Score: {best_score}/25)")
        else:
            self.output_text.append("No suitable month found.")
    
    def visualize_weather_data(self):
        """Visualize weather data for selected country"""
        country = self.country_combo.currentText()
        
        if country not in self.historical_data:
            self.output_text.append(f"No data available for {country}")
            return
            
        months = list(range(1, 13))
        temps = [self.historical_data[country][m][0] for m in months]
        rains = [self.historical_data[country][m][1] for m in months]
        sunshine = [self.historical_data[country][m][2] for m in months]
        
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
        ax3.plot(months, sunshine, 'y-')
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
        
        emoji = self.get_weather_emoji(weather_id)
        
        result = (f"\nCurrent weather in {city}, {country}:\n"
                 f"Temperature: {temp_c:.1f}°C\n"
                 f"Weather: {weather_desc} {emoji}\n"
                 f"Humidity: {humidity}%\n"
                 f"Wind Speed: {wind_speed} m/s\n")
        
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