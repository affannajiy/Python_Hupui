'''
Weather Forecasting App
Choose from 5 Countries (Malaysia, Germany, Japan, Germany, USA)
Use Past Data to Predict Weather
Informed and Uninformed Search
Score of indicates 20 to 25 good weather (Month)
'''

import heapq
from collections import deque, defaultdict
import random
from datetime import datetime
import matplotlib.pyplot as plt

class WeatherPrediction:
  def __init__(self):
    
    self.historical_data = {
      'Malaysia': {
        1: (31, 80, 11), #January: Temperature C, Rain mm, Sunshine hours
        2: (29, 75, 12),
        3: (32, 70, 13),
        4: (33, 65, 14),
        5: (34, 60, 15),
        6: (36, 55, 16),
        7: (33, 50, 17),
        8: (30, 45, 18),
        9: (31, 40, 19),
        10: (30, 35, 20),
        11: (28, 30, 21),
        12: (27, 25, 22)
      },
      
    }

    self.current_month = datetime.now().month
  
  def calculate_weather_score(self, temperature, rain, sunshine):
    return temperature + rain + sunshine