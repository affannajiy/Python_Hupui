'''
Bro Code Weather App
Link: https://youtu.be/Q4377DH5Jso?si=OSo58860_c8BUvvH
'''

import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton)  
from PyQt5.QtCore import Qt #Qt for alignment

class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter city name: ", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button = QPushButton("Get Weather", self)
    self.temperature_label = QLabel("70°C", self)
    self.emoji_label = QLabel("🌞", self)
    self.description_label = QLabel("Sunny", self)
    self.initUI()

  def initUI(self):
    self.setWindowTitle("Weather App")

    vbox = QVBoxLayout(self)
    
    vbox.addWidget(self.city_label)
    vbox.addWidget(self.city_input)
    vbox.addWidget(self.get_weather_button)
    vbox.addWidget(self.temperature_label)
    vbox.addWidget(self.emoji_label)
    vbox.addWidget(self.description_label)

    self.setLayout(vbox)

    self.city_label.setAlignment(Qt.AlignCenter)
    self.city_input.setAlignment(Qt.AlignCenter)
    self.temperature_label.setAlignment(Qt.AlignCenter)
    self.emoji_label.setAlignment(Qt.AlignCenter)
    self.description_label.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
  app = QApplication(sys.argv) #sys.argv is a list of command line arguments
  weather_app = WeatherApp()
  weather_app.show()
  sys.exit(app.exec_())  #app.exec_() starts the event loop