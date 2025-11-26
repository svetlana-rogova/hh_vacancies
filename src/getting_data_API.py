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
    def reading(self) -> Any:
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
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params: dict[str, str | int] = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies: list[Dict[str, Any]] = []
        super().__init__(file_worker)

    def __load_vacancies(self, keyword: str) -> None:
        """Метод для загрузки данных по API"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] = int(self.__params['page']) + 1
            else:
                print(f"Произошла ошибка. Статус-код: {response.status_code}")

    def __writing_in_file(self) -> None:
        """Реализация метода записи данных в файл"""
        self.writing(self.__vacancies)

    def __reading_file(self) -> Any:
        """Реализация метода чтения файла"""
        return self.reading()

    def load_vacancies(self, keyword: str) -> None:
        self.__load_vacancies(keyword)

    def writing_in_file(self) -> None:
        self.__writing_in_file()

    def reading_file(self) -> Any:
        return self.__reading_file()


if __name__ == "__main__":
    file_worker = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies_hh")
    hh = HH(file_worker)
    hh.load_vacancies("Python")

    hh.writing_in_file()
    print(hh.reading_file())
