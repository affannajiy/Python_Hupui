import heapq
from collections import deque, defaultdict
import random
from datetime import datetime
import matplotlib.pyplot as plt

class WeatherPredictionApp:
    def __init__(self):
        # Historical weather data structure: {country: {month: (avg_temp, avg_rain, avg_sunshine)}}
        self.historical_data = {
            'USA': {
                1: (5, 80, 4),  # January: 5°C, 80mm rain, 4 sunshine hours
                2: (7, 70, 5),
                3: (12, 65, 6),
                4: (16, 60, 7),
                5: (20, 55, 8),
                6: (25, 50, 9),
                7: (28, 45, 10),
                8: (27, 50, 9),
                9: (23, 55, 7),
                10: (17, 60, 6),
                11: (11, 70, 4),
                12: (6, 75, 3)
            },
            'Japan': {
                1: (6, 50, 5),
                2: (7, 60, 5),
                3: (10, 90, 6),
                4: (16, 120, 6),
                5: (20, 130, 6),
                6: (24, 180, 5),
                7: (28, 150, 6),
                8: (29, 140, 7),
                9: (25, 180, 5),
                10: (19, 130, 6),
                11: (14, 80, 6),
                12: (9, 50, 5)
            },
            'Australia': {
                1: (28, 80, 8),  # Southern hemisphere - seasons reversed
                2: (27, 90, 8),
                3: (25, 70, 8),
                4: (22, 50, 7),
                5: (18, 40, 7),
                6: (15, 30, 6),
                7: (14, 30, 7),
                8: (16, 30, 8),
                9: (19, 35, 8),
                10: (22, 50, 8),
                11: (25, 60, 9),
                12: (27, 70, 9)
            },
            'France': {
                1: (6, 60, 3),
                2: (7, 50, 4),
                3: (11, 55, 5),
                4: (14, 50, 6),
                5: (18, 60, 7),
                6: (22, 50, 8),
                7: (24, 40, 9),
                8: (24, 50, 8),
                9: (20, 60, 7),
                10: (15, 70, 5),
                11: (10, 70, 4),
                12: (7, 60, 3)
            },
            'Brazil': {
                1: (28, 200, 6),  # Tropical climate
                2: (28, 180, 6),
                3: (28, 170, 6),
                4: (27, 120, 7),
                5: (26, 90, 7),
                6: (25, 60, 8),
                7: (25, 50, 8),
                8: (26, 50, 8),
                9: (26, 80, 7),
                10: (27, 120, 6),
                11: (27, 150, 6),
                12: (28, 190, 6)
            }
        }
        
        # Current month
        self.current_month = datetime.now().month
        
    def calculate_weather_score(self, temp, rain, sunshine):
        """Calculate a weather score between 20-25 based on weather parameters"""
        # Normalize parameters (weights can be adjusted)
        temp_score = min(max((temp - 10) / 25 * 10, 0), 10)  # Ideal around 20-25°C
        rain_score = min(max((100 - rain) / 100 * 10, 0), 10)  # Less rain is better
        sunshine_score = min(max(sunshine / 10 * 10, 0), 10)  # More sunshine is better
        
        # Combine scores and scale to 20-25 range
        total = temp_score * 0.5 + rain_score * 0.3 + sunshine_score * 0.2
        return round(20 + (total / 10) * 5, 1)
    
    def get_weather_prediction(self, country, month):
        """Get weather prediction for a country in a specific month"""
        if country not in self.historical_data:
            return None
        
        if month not in self.historical_data[country]:
            return None
            
        temp, rain, sunshine = self.historical_data[country][month]
        # Add some randomness to simulate prediction
        temp += random.uniform(-2, 2)
        rain += random.uniform(-10, 10)
        sunshine += random.uniform(-1, 1)
        
        score = self.calculate_weather_score(temp, rain, sunshine)
        
        return {
            'temperature': round(temp, 1),
            'rainfall': round(rain, 1),
            'sunshine': round(sunshine, 1),
            'score': score
        }
    
    def bfs_search_best_month(self, country, start_month=None):
        """Uninformed search (BFS) to find the best month for a country"""
        if start_month is None:
            start_month = self.current_month
            
        visited = set()
        queue = deque([start_month])
        best_month = None
        best_score = 0
        
        while queue:
            month = queue.popleft()
            
            if month in visited:
                continue
                
            visited.add(month)
            
            prediction = self.get_weather_prediction(country, month)
            if not prediction:
                continue
                
            if prediction['score'] > best_score:
                best_score = prediction['score']
                best_month = month
                
            # Explore adjacent months
            prev_month = month - 1 if month > 1 else 12
            next_month = month + 1 if month < 12 else 1
            
            if prev_month not in visited:
                queue.append(prev_month)
            if next_month not in visited:
                queue.append(next_month)
                
        return best_month, best_score
    
    def astar_search_best_month(self, country, start_month=None):
        """Informed search (A*) to find the best month for a country"""
        if start_month is None:
            start_month = self.current_month
            
        def heuristic(month, target_score=25):
            # Simple heuristic: how close is this month to the ideal summer month (June/December)
            if country == 'Australia' or country == 'Brazil':  # Southern hemisphere
                ideal_month = 12
            else:  # Northern hemisphere
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
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            prediction = self.get_weather_prediction(country, current)
            if not prediction:
                continue
                
            current_score = prediction['score']
            
            if current_score > best_score:
                best_score = current_score
                best_month = current
                
            if current_score >= 24:  # Good enough score
                break
                
            # Explore adjacent months
            neighbors = [
                current - 1 if current > 1 else 12,
                current + 1 if current < 12 else 1
            ]
            
            for neighbor in neighbors:
                prediction = self.get_weather_prediction(country, neighbor)
                if not prediction:
                    continue
                    
                tentative_g_score = g_score[current] + (25 - prediction['score'])
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                    if neighbor not in [m for (_, m) in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        
        return best_month, best_score
    
    def visualize_weather_data(self, country):
        """Visualize weather data for a country"""
        if country not in self.historical_data:
            print(f"No data available for {country}")
            return
            
        months = list(range(1, 13))
        temps = [self.historical_data[country][m][0] for m in months]
        rains = [self.historical_data[country][m][1] for m in months]
        sunshine = [self.historical_data[country][m][2] for m in months]
        
        plt.figure(figsize=(12, 8))
        
        # Temperature plot
        plt.subplot(3, 1, 1)
        plt.plot(months, temps, 'r-')
        plt.title(f'Weather Data for {country}')
        plt.ylabel('Temperature (°C)')
        plt.grid(True)
        
        # Rainfall plot
        plt.subplot(3, 1, 2)
        plt.plot(months, rains, 'b-')
        plt.ylabel('Rainfall (mm)')
        plt.grid(True)
        
        # Sunshine plot
        plt.subplot(3, 1, 3)
        plt.plot(months, sunshine, 'y-')
        plt.ylabel('Sunshine (hours)')
        plt.xlabel('Month')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def run(self):
        """Run the weather prediction app"""
        print("Welcome to the Weather Prediction App!")
        print("Available countries:", ", ".join(self.historical_data.keys()))
        
        while True:
            print("\nMenu:")
            print("1. Get weather prediction for a country and month")
            print("2. Find best month to visit a country (BFS)")
            print("3. Find best month to visit a country (A*)")
            print("4. Visualize weather data for a country")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                country = input("Enter country: ").title()
                month = int(input("Enter month (1-12): "))
                
                prediction = self.get_weather_prediction(country, month)
                if prediction:
                    print(f"\nWeather prediction for {country} in month {month}:")
                    print(f"Temperature: {prediction['temperature']}°C")
                    print(f"Rainfall: {prediction['rainfall']}mm")
                    print(f"Sunshine hours: {prediction['sunshine']}")
                    print(f"Weather score: {prediction['score']}/25")
                else:
                    print("Invalid country or month.")
                    
            elif choice == '2':
                country = input("Enter country: ").title()
                start_month = input("Enter starting month (1-12, leave blank for current month): ")
                start_month = int(start_month) if start_month else None
                
                month, score = self.bfs_search_best_month(country, start_month)
                if month:
                    month_name = datetime(2023, month, 1).strftime('%B')
                    print(f"\nBest month to visit {country} (BFS): {month_name} (Score: {score}/25)")
                else:
                    print("Invalid country.")
                    
            elif choice == '3':
                country = input("Enter country: ").title()
                start_month = input("Enter starting month (1-12, leave blank for current month): ")
                start_month = int(start_month) if start_month else None
                
                month, score = self.astar_search_best_month(country, start_month)
                if month:
                    month_name = datetime(2023, month, 1).strftime('%B')
                    print(f"\nBest month to visit {country} (A*): {month_name} (Score: {score}/25)")
                else:
                    print("Invalid country.")
                    
            elif choice == '4':
                country = input("Enter country: ").title()
                self.visualize_weather_data(country)
                
            elif choice == '5':
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = WeatherPredictionApp()
    app.run()