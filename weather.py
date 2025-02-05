# Hardcodede weather data dictionary
weather_data = {
  "London" : {
    "Current Temperature" : "6°C",
    "Weather Condition" : "Mostly Sunny", 
    "Wind Speed": "5mph",
    "Humidity": "74%", 
    "Chance of Rain": "<5%"
  },
  "Birmingham" : {
   "Current Temperature" : "5°C",
    "Weather Condition" : "Mostly Cloudy", 
    "Wind Speed": "9mph",
    "Humidity": "81%", 
    "Chance of Rain": "50%"
  },
    "Edinburgh" : {
    "Current Temperature" : "4°C",
    "Weather Condition" : "Sunny", 
    "Wind Speed": "10mph",
    "Humidity": "67%", 
    "Chance of Rain": "<5%"
  },
    "Cardiff" : {
    "Current Temperature" : "8°C",
    "Weather Condition" : "Mostly Sunny", 
    "Wind Speed": "10mph",
    "Humidity": "63%", 
    "Chance of Rain": "<5%"
  },
   "Dublin" : {
    "Current Temperature" : "6°C",
    "Weather Condition" : "Mostly Sunny", 
    "Wind Speed": "19mph",
    "Humidity": "67%", 
    "Chance of Rain": "20%"
  },
    "Truro" : {
   "Current Temperature" : "9°C",
    "Weather Condition" : "Mostly Cloudy", 
    "Wind Speed": "10mph",
    "Humidity": "59%", 
    "Chance of Rain": "<5%"
  },
    "Inverness" : {
   "Current Temperature" : "3°C",
    "Weather Condition" : "Sunny", 
    "Wind Speed": "7mph",
    "Humidity": "81%", 
    "Chance of Rain": "10%"
  },
   "Manchester" : {
   "Current Temperature" : "7°C",
    "Weather Condition" : "Mostly Sunny", 
    "Wind Speed": "8mph",
    "Humidity": "66%", 
    "Chance of Rain": "10%"
   }
}

# personalised welcome message
def greeting(name):
    name = input("What is your name?")
    print(f"Hello, {name}! Welcome to How's the WeatherApp there! Let's see what the weather's like in your nearest city.")
greeting("name")

# Function to retrieve weather data for a city
city = input("Enter the name of your city to see if you need a coat: ")

# We need the name of the city the user is in to provide weather details
def get_weather(city):
    if city in weather_data:
        print(f"Current weather in {city}:")
        for key, value in weather_data[city].items():
            print(f"{key}: {value}")    
    if "Chance of Rain" in weather_data[city]:
        if weather_data[city]["Chance of Rain"] == ">5%":
            print("Oh wow, no need for a coat today!")
        elif weather_data[city]["Chance of Rain"] == "10%":
            print("Might be best to take a coat, just in case!")
        elif weather_data[city]["Chance of Rain"] == "20%":
            print("Looks like there'll be drizzle, take a coat.")
        else:
            print("Take a good coat, it's the UK, of course it's going to rain.")
    else:
        print("Sorry, we don't have weather data for that city. Please try another city.")

get_weather(city)
