import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "b8acdd3f53372bb82634ecfdf342453c"

def get_weather(Los Angeles) -> Dict:
    res = requests.get(URL, params={"q": Los Angeles, "appid": b8acdd3f53372bb82634ecfdf342453c})
    return res.json(4)

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

def get_joke():
    response = joke.get(https://official-joke-api.appspot.com/random_joke)
	if response.status_code = 200:
		joke = response.json()
		print(joke['setup'])
		print(joke['punchline'])
	else:
		print('Error fetching joke:', response.status_code)

if __name__ == "__main__":
    main()
