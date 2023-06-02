from pathlib import Path
from typing import Dict, Any, List, Optional
import re
import csv

def count_words(text: str) -> Dict[str, int]:
    
    result=dict()
    
    text=re.split(r'\W+', text)
    
    for word in text:
        if word.isalpha():
            if word.lower() in result:
                result[word.lower()] += 1
            else:
                result[word.lower()] = 1
            

    return result


def exp_list(numbers: List[int], exp: int) -> List[int]:

    return [elem**exp for elem in numbers]


def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:

    result = 0

    for oper in operations:
        
        if oper["category"] in special_category:
            result += oper["amount"]*0.05
        else:
            result +=oper["amount"]*0.01

    return result


def get_path_to_file() -> Optional[Path]:
    """
    Находит корректный путь до тестового файла.

    Если запускать тесты из pycharm - начальная папка - tests
    Если запускать файлы через make tests - начальная папка - корень проекта

    :return: путь до тестового файла tasks.csv
    """
    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'


def csv_reader(header: str) -> int:
    
    with open(get_path_to_file()) as file:
        text=csv.DictReader(file)
        return len(set([row[header] for row in text]))

    return result
