import json
import os
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List

import requests


class Getting(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """Абстрактный метод для загрузки данных по API"""
        pass

    @abstractmethod
    def writing(self, data: List[Dict[str, Any]]) -> None:
        """Абстрактный метод для записи данных в файл"""
        pass

    @abstractmethod
    def reading(self) -> List[Dict[str, Any]]:
        """Абстрактный метод для чтения данных из файла"""
        pass


class Parser(Getting):
    """Класс для работы с данными"""

    def __init__(self, file_worker: Any):
        self.file_worker = file_worker

    def writing(self, data: List[Dict[str, Any]]) -> None:
        """Метод для записи данных в файл"""
        with open(self.file_worker, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def reading(self) -> Any:
        """Метод для чтения данных из файла"""
        with open(self.file_worker, "r", encoding="UTF-8") as file:
            return json.load(file)


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self, file_worker: Any):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params: dict[str, str | int] = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies: list[Dict[str, Any]] = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str) -> None:
        """Метод для загрузки данных по API"""
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] = int(self.params['page']) + 1

    def writing_in_file(self) -> None:
        """Реализация метода записи данных в файл"""
        self.writing(self.vacancies)

    def reading_file(self) -> Any:
        """Реализация метода чтения файла"""
        return self.reading()


file_worker = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies_hh")
hh = HH(file_worker)
hh.load_vacancies("Python")

hh.writing_in_file()
print(hh.reading_file())
