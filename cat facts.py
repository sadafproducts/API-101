import requests
import json

response = requests.get('https://cat-fact.herokuapp.com/facts')

print(response)
print('\n')
print(response.json())
print('\n')
print(response.json()['all'])
print('\n\n')


for question in response.json()['all']:
    print(question['text'])
    print()
        

