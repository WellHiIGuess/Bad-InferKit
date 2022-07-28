import json


with open('article', 'r') as file:
    article = file.read()


data = {}


for i in range(1, len(article.split()) - 1):
    if article.split()[i] in data:
        data[article.split()[i]]['list'].append(article.split()[i + 1])
    else:
        data[article.split()[i]] = {"val" : article.split()[i], "context" : article.split()[i - 1], "list" : [article.split()[i + 1]]}


with open('data.json', 'w') as file:
    file.write(json.dumps(data))
