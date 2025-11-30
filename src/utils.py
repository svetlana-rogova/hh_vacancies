from typing import Any

from src.job_comparison import Vacancies


def formater(vacancies_data: list[dict[str, Any]]) -> list[Vacancies]:
    """Функция, которая приводит вывод вакансий в понятный человеку формат"""
    answer = []
    for dict_vacancies in vacancies_data:
        description = dict_vacancies.get("snippet", {}).get("responsibility") or "не указаны"
        salary_raw = dict_vacancies.get("salary")
        salary_from: int = 0
        salary_to: int = 0
        currency_vac: str = "не указана"
        if isinstance(salary_raw, dict):
            raw_from = salary_raw.get("from")
            raw_to = salary_raw.get("to")
            try:
                salary_from = int(raw_from) if raw_from is not None else 0
            except (ValueError, TypeError):
                salary_from = 0
            try:
                salary_to = int(raw_to) if raw_to is not None else salary_from
            except (ValueError, TypeError):
                salary_to = salary_from
            currency_vac = salary_raw.get("currency") or "не указана"
        id_vac_raw = dict_vacancies.get("id")
        id_vac: int = 0
        if id_vac_raw is not None:
            try:
                id_vac = int(id_vac_raw)
            except (ValueError, TypeError):
                id_vac = 0
        answer.append(Vacancies(name=str(dict_vacancies.get("name")),
                                area=str(dict_vacancies.get("area", {}).get("name", "не указан")),
                                link=str(dict_vacancies.get('alternate_url', "не указана")),
                                description=str(description),
                                id_vac=id_vac,
                                salary_from=int(salary_from),
                                salary_to=int(salary_to),
                                currency_vac=str(currency_vac)))
    return answer


def filter_vacancies_by_currency(filtered_vacancies: list[dict[str, Any]], currency: str) -> list[dict[str, Any]]:
    """Функция для фильтрации вакансий по валюте зарплаты"""
    filter_vac_currency = []
    for vacancy in filtered_vacancies:
        currency_vac = vacancy.get("salary")
        if not currency_vac:
            continue
        if vacancy["salary"]["currency"] == currency:
            filter_vac_currency.append(vacancy)
    return filter_vac_currency


def filter_vacancies_by_words(filtered_vacancies: list[dict[str, Any]],
                              filter_words: list[str]) -> list[dict[str, Any]]:
    """Функция для фильтрации вакансий по словам"""
    if not filter_words:
        return filtered_vacancies
    filter_vac_words = []
    for dict_vac in filtered_vacancies:
        text = (dict_vac.get("description", "") + " " + dict_vac.get("name", "")).lower()
        for word in filter_words:
            if word.lower() in text:
                filter_vac_words.append(dict_vac)
    return filter_vac_words


def filter_vacancies_by_city(filtered_vacancies: list[dict[str, Any]], city: str) -> list[dict[str, Any]]:
    """Функция для фильтрации вакансий по городу"""
    filter_vac_city = []
    if city == "No":
        return filtered_vacancies
    else:
        for vacancy in filtered_vacancies:
            if vacancy["area"]["name"] == city:
                filter_vac_city.append(vacancy)
        return filter_vac_city


def get_vacancies_by_salary(filtered_vacancies: list[dict[str, Any]], salary_range: str) -> list[dict[str, Any]]:
    """Функция для выборки вакансий по зарплате"""
    filter_vac_salary = []
    min_sal, max_sal = salary_range.split(" - ")
    for vacancy in filtered_vacancies:
        salary = vacancy.get("salary")
        if not salary:
            continue
        sal_from = salary.get("from") or 0
        sal_to = salary.get("to") or sal_from
        if sal_from >= int(min_sal) and sal_to <= int(max_sal):
            filter_vac_salary.append(vacancy)
    return filter_vac_salary


def sort_vacancies(filter_vac_salary: list[Vacancies]) -> list["Vacancies"]:
    """Функция для сортировки вакансий по уменьшению зарплаты"""
    sorted_vac_salary = sorted(
        filter_vac_salary, key=lambda x: x.salary_from or 0, reverse=True
    )
    return sorted_vac_salary


def get_top_vacancies(sorted_vacancies: list["Vacancies"], top_n: int) -> str:
    """Функция для вывода топ N вакансий по зарплате"""
    answer = []
    for i, dict_vacancies in enumerate(sorted_vacancies[0:top_n], start=1):
        name = dict_vacancies.name
        area = dict_vacancies.area
        salary_from = dict_vacancies.salary_from
        salary_to = dict_vacancies.salary_to
        link = dict_vacancies.link
        description = dict_vacancies.description
        currency_vac = dict_vacancies.currency_vac
        answer.append(f"Вакансия № {i} {name}, город {area}, зарплата от {salary_from} до {salary_to}, "
                      f"валюта {currency_vac}, задачи: {description}, ссылка {link}")
    return "\n".join(answer)
