# Use https://api.stackexchange.com

import requests
import json

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

print(response)
print('\n\n')
print(response.json())
print('\n\n')
print(response.json()['items'])
print('\n\n')


for question in response.json()['items']:
    if question['answer_count'] > 1:
        print(question['answer_count'])
        print(question['title'])
        print(question['link'])
    else:
        print('Skipped')
    print()
        