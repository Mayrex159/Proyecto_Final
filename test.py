import requests


response = requests.get('https://attackontitanapi.herokuapp.com/api/characters').json()
print(response)


#print(response['results'])