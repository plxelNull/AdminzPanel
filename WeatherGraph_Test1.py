import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

api_endpoint = "https://api.weatherapi.com/v1/history.json"
api_key = "PUT_API_KEY_HERE"

end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

params = {
    "key": api_key,
    "q": "Los Angeles",
    "dt": f"{start_date}/{end_date}",
}

response = requests.get(api_endpoint, params=params)
data = response.json()

dates = []
temperatures = []

for item in data['forecast']['forecastday']:
    date = datetime.strptime(item['date'], '%Y-%m-%d').strftime('%m-%d')
    temp = item['day']['avgtemp_c']
    dates.append(date)
    temperatures.append(temp)

plt.plot(dates, temperatures, marker='o')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature in Los Angeles - Last 30 Days')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
