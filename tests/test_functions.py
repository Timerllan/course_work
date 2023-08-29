from src.functions import details_to_str,sorted_operations,executed_operations,return_date_time,func_load_file
import pytest
@pytest.fixture()
def sample_data():
    return [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2017-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2018-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2023-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  },
  {
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2017-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  },
  {
    "id": 142264268,
    "state": "CANCELED",
    "date": "2014-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  }]



def test_details_to_str():
    assert details_to_str('Счет 38427597486442637521') == 'Счет **7521'
    assert details_to_str('Visa Classic 8906171742833215') == 'Visa Classic 8906 17** **** 3215'
    assert details_to_str(None) == 'нет данных'


def test_sorted_operations(sample_data):
    operation_list = sorted_operations(sample_data)
    assert operation_list[0]["id"] == 939719570
    assert operation_list[-1]['id'] == 142264268


def test_executed_operations(sample_data):
    operation_list = executed_operations(sample_data)
    assert len(operation_list) == 4


def test_return_date_time():
    assert return_date_time('2014-04-06T23:20:05.206878') == '06.04.2014'


def test_func_load_file():
    operation_list = func_load_file('tests/sample_file.json')
    assert len(operation_list) == 5
    assert operation_list[0]['id'] == 441945886


