import pytest

from src.job_comparison import Vacancies


def test_valid_info(vacancies_one):
    vac = vacancies_one
    assert vac.name == "Программист"
    assert vac.id == 123
    assert vac.salary_from == 50000


def test_valid_info_two(vacancies_two):
    vac = vacancies_two
    assert vac.name == "Разработчик"
    assert vac.area == "Тверь"
    assert vac.salary_from == 0
    assert vac.salary_to == 0


def test_valid_info_three():
    with pytest.raises(TypeError):
        Vacancies("Менеджер", "ссылка", 70000, 150000, "работа в офисе", "Тамбов", "RUR", "999")


def test_comparison(vacancies_one, vacancies_three):
    vac_1 = vacancies_one
    vac_2 = vacancies_three
    assert vac_1 <= vac_2
    assert vac_1 < vac_2
    assert vac_2 >= vac_1


def test_comparison_one(vacancies_one, vacancies_two):
    vac_1 = vacancies_one
    vac_2 = vacancies_two
    assert vac_1 >= vac_2
    assert vac_1 > vac_2
    assert vac_2 <= vac_1
