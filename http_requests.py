import requests

url = 'https://icanhazdadjoke.com/'
user_input = 'cat'

response = requests.get('https://icanhazdadjoke.com/search',
                        headers={
                            'Accept': 'application/json'
                        },
                        params={
                            "term": user_input,
                            "limit": 2
                        })
data = response.json()
print(data)
