import requests
 
# Lat-Lon of New York
URL = "https://weather.com/weather/today/l/40.75,-73.98"
resp = requests.get(URL)
print(resp.status_code) # 200 means the request is successfully fulfilled.
# print(resp.text)