import requests
import pprint   # для вывода информации в более красивом виде

params = {
    'timeZone': 'Europe/Minsk'
}

api_result = requests.get('https://www.timeapi.io/api/Time/current/zone', params)

api_response = api_result.json()

pprint.pprint(api_response)
