import requests


response = requests.post('http://127.0.0.1:5000/ads/', json={'title': 'Стол 2', 'description': 'Удобный стол', 'owner': 'Иванов'})
print(response.status_code)
print(response.json())

response = requests.get('http://127.0.0.1:5000/ads/10/')
print(response.status_code)
print(response.json())

response = requests.delete('http://127.0.0.1:5000/ads/10/')
print(response.status_code)
print(response.json())
