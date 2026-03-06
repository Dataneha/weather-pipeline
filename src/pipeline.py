import requests
import pandas as pd

# Weather API (Kansas City example)
url = "https://api.open-meteo.com/v1/forecast?latitude=39.0997&longitude=-94.5786&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]

# Convert to dataframe
df = pd.DataFrame([weather])

# Save to CSV
df.to_csv("data/weather_data.csv", index=False)

print("Weather data saved successfully!")