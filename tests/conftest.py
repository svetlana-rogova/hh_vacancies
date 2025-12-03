import pytest

from src.job_comparison import Vacancies


@pytest.fixture
def vacancies_one():
    return Vacancies("Программист", "ссылка", 50000, 100000, "удаленная работа", "Москва", "RUR", 123)


@pytest.fixture
def vacancies_two():
    return Vacancies("Разработчик", "ссылка", -50, -10, "работа в офисе", "Тверь", "RUR", 9153)


@pytest.fixture
def vacancies_three():
    return Vacancies("Менеджер", "ссылка", 70000, 150000, "работа в офисе", "Тамбов", "RUR", 999)


@pytest.fixture
def vacancies_one_list():
    return Vacancies(
        name="Программист1",
        link="Текст1",
        salary_from=120000,
        salary_to=170000,
        description="работа в офисе",
        area="Иркутск",
        currency_vac="RUR",
        id=123,
    )


@pytest.fixture
def vacancies_two_list():
    return Vacancies(
        name="Программист2",
        link="Текст2",
        salary_from=100000,
        salary_to=150000,
        description="работа в офисе",
        area="Иркутск",
        currency_vac="RUR",
        id=123,
    )


@pytest.fixture
def vacancies_three_list():
    return Vacancies(
        name="Программист2",
        link="Текст2",
        salary_from=100000,
        salary_to=150000,
        description="работа в офисе",
        area="Иркутск",
        currency_vac="RUR",
        id=898,
    )


@pytest.fixture
def vacancies():
    return [
        {
            "alternate_url": "Текст",
            "area": {"name": "Иркутск"},
            "id": 898,
            "name": "Программист2",
            "salary": {"currency": "RUR", "from": 100000, "to": 150000},
            "snippet": {"responsibility": "работа в офисе"},
        },
        {
            "alternate_url": "Текст2",
            "area": {"name": "Иркутск"},
            "id": 898,
            "name": "Монтажник",
            "salary": {"currency": "USD", "from": 80000, "to": 100000},
            "snippet": {"responsibility": "работа на объекте"},
        },
    ]


@pytest.fixture
def vacancies2():
    return [
        {
            "link": "Текст",
            "area": {"name": "Иркутск"},
            "id": 898,
            "name": "Программист2",
            "salary": {"currency": "RUR", "from": 100000, "to": 150000},
            "snippet": {"responsibility": "работа в офисе"},
        }
    ]


@pytest.fixture
def vacancies3():
    return [
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


@pytest.fixture
def vacancies4():
    return [
        Vacancies(
            name="Вакансия B",
            area="Санкт-Петербург",
            link="https://hh.ru/vacancy/2",
            description="Описание B",
            id=256,
            salary_from=80000,
            salary_to=100000,
            currency_vac="RUR",
        ),
        Vacancies(
            name="Вакансия A",
            area="Москва",
            link="https://hh.ru/vacancy/1",
            description="Описание A",
            id=123,
            salary_from=50000,
            salary_to=70000,
            currency_vac="RUR",
        ),
    ]


@pytest.fixture
def vac_hh():
    return [
        {
            "id": "128104969",
            "premium": False,
            "name": "Backend разработчик",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "2759", "name": "Ташкент", "url": "https://api.hh.ru/areas/2759"},
            "salary": None,
            "salary_range": None,
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-11-26T20:58:36+0300",
            "created_at": "2025-11-26T20:58:36+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=128104969",
            "show_logo_in_search": None,
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/128104969?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/128104969",
            "relations": [],
            "employer": {
                "id": "10782917",
                "name": "ZERODEV",
                "url": "https://api.hh.ru/employers/10782917",
                "alternate_url": "https://hh.ru/employer/10782917",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1337317.png",
                    "90": "https://img.hhcdn.ru/employer-logo/6969258.png",
                    "240": "https://img.hhcdn.ru/employer-logo/6969259.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10782917",
                "country_id": 6,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Пониманием : OOP, REST API, CRUD.  "
                "Будет плюсом знание: - Aiogram или Telebot. Умение писать чистый, поддерживаемый и "
                "оптимизированный код. ",
                "responsibility": "Разработка и поддержка backend-части CRM, CMS и корпоративных систем. "
                                  "Интеграция внешних "
                "API и сервисов. Настройка очередей задач (Celery) и...",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": True,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На месте работодателя"}],
            "working_hours": [{"id": "HOURS_8", "name": "8 часов"}],
            "work_schedule_by_days": [{"id": "SIX_ON_ONE_OFF", "name": "6/1"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]
