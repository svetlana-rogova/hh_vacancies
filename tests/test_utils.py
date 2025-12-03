from src.utils import filter_vacancies_by_city
from src.utils import filter_vacancies_by_currency
from src.utils import filter_vacancies_by_words
from src.utils import formater
from src.utils import get_top_vacancies
from src.utils import get_vacancies_by_salary
from src.utils import sort_vacancies


def test_formater(vac_hh):
    answer = formater(vac_hh)
    assert answer[0].to_dict() == {
        "link": "https://hh.ru/vacancy/128104969",
        "area": {"name": "Ташкент"},
        "id": 128104969,
        "name": "Backend разработчик",
        "salary": {"currency": "не указана", "from": 0, "to": 0},
        "snippet": {
            "responsibility": "Разработка и поддержка backend-части CRM, CMS "
            "и корпоративных систем. Интеграция внешних API "
            "и сервисов. Настройка очередей задач (Celery) "
            "и..."
        },
    }


def test_filter_vacancies_by_currency(vacancies):
    answer = filter_vacancies_by_currency(vacancies, "RUR")
    assert answer == [
        {
            "alternate_url": "Текст",
            "area": {"name": "Иркутск"},
            "id": 898,
            "name": "Программист2",
            "salary": {"currency": "RUR", "from": 100000, "to": 150000},
            "snippet": {"responsibility": "работа в офисе"},
        }
    ]


def test_filter_vacancies_by_words(vacancies3):
    answer = filter_vacancies_by_words(vacancies3, ["фирмы", "нашей"])
    assert answer == [
        {
            "link": "Текст",
            "area": {"name": "Иркутск"},
            "id": 898,
            "name": "Программист2",
            "salary": {"currency": "RUR", "from": 100000, "to": 150000},
            "description": "Разработка приложения для нашей фирмы",
        },
        {
            "link": "Текст2",
            "area": {"name": "Томск"},
            "id": 898,
            "name": "Монтажник",
            "salary": {"currency": "USD", "from": 80000, "to": 100000},
            "description": "Работа на объекте нашей фирмы",
        },
    ]


def test_filter_vacancies_by_words2(vacancies3):
    answer = filter_vacancies_by_words(vacancies3, ["слово"])
    assert answer == []


def test_filter_vacancies_by_city(vacancies3):
    answer = filter_vacancies_by_city(vacancies3, "Томск")
    assert answer == [
        {
            "link": "Текст2",
            "area": {"name": "Томск"},
            "id": 898,
            "name": "Монтажник",
            "salary": {"currency": "USD", "from": 80000, "to": 100000},
            "description": "Работа на объекте нашей фирмы",
        }
    ]


def test_filter_vacancies_by_city2(vacancies3):
    answer = filter_vacancies_by_city(vacancies3, "Тула")
    assert answer == []


def test_get_vacancies_by_salary(vacancies3):
    answer = get_vacancies_by_salary(vacancies3, "100000 - 180000")
    assert answer == [
        {
            "link": "Текст",
            "area": {"name": "Иркутск"},
            "id": 898,
            "name": "Программист2",
            "salary": {"currency": "RUR", "from": 100000, "to": 150000},
            "description": "Разработка приложения для" " нашей фирмы",
        }
    ]


def test_sort_vacancies(vacancies4):
    answer = sort_vacancies(vacancies4)
    assert answer[0].to_dict() == {
        "link": "https://hh.ru/vacancy/2",
        "area": {"name": "Санкт-Петербург"},
        "id": 256,
        "name": "Вакансия B",
        "salary": {"currency": "RUR", "from": 80000, "to": 100000},
        "snippet": {"responsibility": "Описание B"},
    }
    assert answer[1].to_dict() == {
        "area": {"name": "Москва"},
        "id": 123,
        "link": "https://hh.ru/vacancy/1",
        "name": "Вакансия A",
        "salary": {"currency": "RUR", "from": 50000, "to": 70000},
        "snippet": {"responsibility": "Описание A"},
    }


def test_get_top_vacancies(vacancies4):
    answer = get_top_vacancies(vacancies4, 4)
    assert answer == (
        "Вакансия № 1 Вакансия B, город Санкт-Петербург, зарплата от 80000 до 100000, "
        "валюта RUR, задачи: Описание B, ссылка https://hh.ru/vacancy/2\n"
        "Вакансия № 2 Вакансия A, город Москва, зарплата от 50000 до 70000, валюта "
        "RUR, задачи: Описание A, ссылка https://hh.ru/vacancy/1"
    )
