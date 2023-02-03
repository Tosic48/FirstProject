import requests

api_result = requests.get('https://www.timeapi.io')
print(f'status of request: {api_result.status_code}')
if api_result.status_code == 200:
    while True:
        city = input('write city of Europe where you live: ')
        if city:
            params = {
                'timeZone': 'Europe/' + city
            }
            api_result = requests.get('https://www.timeapi.io/api/Time/current/zone', params)
            api_response = api_result.json()
            try:
                print(f'current time in {city}: {api_response["time"]} and date: {api_response["date"]}')
            except:
                print('city is not found')
else:
    print('Error!')
