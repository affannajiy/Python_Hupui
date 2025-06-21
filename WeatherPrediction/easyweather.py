import requests

def get_weather(api_key, city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        
        if data.get('cod') != 200:
            return None
        
        return {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'description': data['weather'][0]['description'],
            'temp': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    except requests.exceptions.RequestException:
        return None

def main():
    api_key = 'a64a2f0c3f1535863073a63c1b494d18'  # Consider using environment variables
    
    print("🌦️ Weather App 🌦️")
    print("------------------")
    
    while True:
        user_input = input("\nEnter city (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ('quit', 'exit', 'q'):
            print("Goodbye!")
            break
            
        if not user_input:
            print("Please enter a city name.")
            continue
            
        weather_data = get_weather(api_key, user_input)
        
        if not weather_data:
            print(f"Could not find weather data for '{user_input}'. Please check the city name and try again.")
            continue
            
        print(f"\nWeather in {weather_data['city']}:")
        print(f"- Condition: {weather_data['weather']} ({weather_data['description']})")
        print(f"- Temperature: {weather_data['temp']}°C (Feels like {weather_data['feels_like']}°C)")
        print(f"- Humidity: {weather_data['humidity']}%")
        print(f"- Wind Speed: {weather_data['wind_speed']} kph")

if __name__ == "__main__":
    main()