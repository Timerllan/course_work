import json
from datetime import datetime


FILE_BANK = 'operations.json'

def func_load_file(file_name):
    with open('operations.json','r',encoding='utf-8')as file:
        bank_file = json.load(file)
    return bank_file


def executed_operations(operation_list):
    return [operation for operation in operation_list if operation and operation["state"]== "EXECUTED"]


def sorted_operations(operation_list):
    return sorted(operation_list,key=lambda x:datetime.strptime(x['date'],'%Y-%m-%dT%H:%M:%S.%f'),reverse=True)



def return_date_time(str_type):
    return datetime.strptime(str_type, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')

