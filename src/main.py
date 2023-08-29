from src.functions import func_load_file,details_to_str,sorted_operations,return_date_time,executed_operations,FILE_BANK


operations_list = func_load_file(FILE_BANK)

operations_list = executed_operations(operations_list)
operations_list = sorted_operations(operations_list)[:5]

for operations in operations_list:
    print(return_date_time(operations['date']),operations['description'])
    print(details_to_str(operations.get('from',None)),'->',details_to_str(operations['to']))
    print(operations['operationAmount']['amount'],operations['operationAmount']['currency']['name'],'\n')







