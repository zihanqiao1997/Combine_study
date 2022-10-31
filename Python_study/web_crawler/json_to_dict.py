import requests
 
URL = "https://api.github.com/users/jbrownlee"
resp = requests.get(URL)
if resp.status_code == 200:
    data = resp.json()
    print("type of data is ", type(data)) # <class 'dict'>
    print(data)