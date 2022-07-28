import json
import random


with open('data.json', 'r') as file:
    data = json.loads(file.read())


start = data['My']
last = start

print(start['val'], end=' ')

for i in range(50):
    n = data[random.choice(last['list'])]

    if n['context'] != last['val']:
        n = data[random.choice(last['list'])]
        print(n['val'], end=' ')
    else:    
        print(n['val'], end=' ')

    last = n
