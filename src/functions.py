import json


with open('operations.json','r',encoding='utf-8')as file:
    bank_file = json.load(file)

print(bank_file)