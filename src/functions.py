import json


with open('operations.json','r',encoding='utf-8')as file:
    bank_file = file.read()

print(bank_file)