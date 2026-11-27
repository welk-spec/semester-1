
import httpx
import pandas as pd
import matplotlib.pyplot as plt
from math import floor, ceil


api_key="9C89JM9QDSL4T44LMEJYB4496"   # your API key

city="Leeds"     # city location
country="UK"     # country location

elements = "include=days&elements=tempmax,tempmin,temp"   # request history of temperature data for Leeds

# URL location of the API for time history forecasts
base = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

# construct the URL string for the API call
url = base + city + "," + country + "?key=" + api_key + "&" + elements

# http request
response = httpx.get(url)

# status code (should be checked)
if response.status_code == 200:
    print(response.status_code)
else:
    print(f"Request failed with status code: {response.status_code}")

# json data
data = response.json()

# raw data output
print(data)

# extract the temperature data as lists from the JSON dictionary
temp_data = data['days']

print(temp_data)

# use pandas to convert data to  dataframe

df = pd.DataFrame(temp_data)

# using matplotlib plot the 3 data sets: (tempmin,temp,tempmax) as line graphs


df["tempmax"] = (df["tempmax"] - 32) * 5 / 9
df["temp"] = (df["temp"] - 32) * 5 / 9
df["tempmin"] = (df["tempmin"] - 32) * 5 / 9

df.index = range(1, len(df) + 1)
ax = df.plot()
ax.set_xlabel("Days")
ax.set_ylabel("Temperature (°C)")

y_min = floor(df[["tempmin", "temp", "tempmax"]].min().min())
y_max = ceil(df[["tempmin", "temp", "tempmax"]].max().max())
ax.set_xticks(range(1, len(df) + 1))
ax.set_yticks(range(y_min, y_max + 1))

plt.show()

# annotate the graph with axis labels
# note that temperature is in Farenheit (F)
# convert to Celcius before plotting

# using the documentation explore other data, eg. rainfall  
