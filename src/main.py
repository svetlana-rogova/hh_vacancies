import os
from typing import Any

from src.getting_data_API import HH
from src.job_comparison import Vacancies
from src.utils import filter_vacancies_by_city
from src.utils import filter_vacancies_by_currency
from src.utils import filter_vacancies_by_words
from src.utils import formater
from src.utils import get_top_vacancies
from src.utils import get_vacancies_by_salary
from src.utils import sort_vacancies
from src.working_file import WorkingDataJSON

# Получение вакансий с hh.ru в формате JSON
file_worker = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies_hh")
hh_demo = HH(file_worker)
hh_demo.load_vacancies("Python")

# Пример работы контструктора класса с одной вакансией
vacancy = Vacancies("Программист", "ссылка", 50000, 100000, "работа в офисе", "Москва", "RUR", 111)
answer = WorkingDataJSON()
answer.add_info(vacancy)
answer.delete_vac(111)


def user_interaction() -> Any:
    """Функция, которая запрашивает данные у пользователя для дальнейшей работы с файлом вакансий"""
    search_query = input("Введите поисковый запрос: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий (можно оставить поле пустым): ").split()
    salary_range = input("Введите диапазон зарплат в формате 10 - 20 ")
    currency = input("Введите валюту для поиска: RUR/USD/EUR/CNY или другие: ")
    city = input("Введите город для поиска вакансий, если хотите поиск по всем, то введите No ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    hh = HH(file_worker)
    file_work = hh.load_vacancies(search_query)
    file_work_currency = filter_vacancies_by_currency(file_work, currency)
    file_work_word = filter_vacancies_by_words(file_work_currency, filter_words)
    file_work_city = filter_vacancies_by_city(file_work_word, city)
    file_work_salary = get_vacancies_by_salary(file_work_city, salary_range)
    file_work_format = formater(file_work_salary)
    file_work_sort = sort_vacancies(file_work_format)
    file_work_get = get_top_vacancies(file_work_sort, top_n)
    return file_work_get


if __name__ == "__main__":
    print(user_interaction())
