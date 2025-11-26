import json
import os
from abc import ABC
from abc import abstractmethod
from typing import Any


class WorkingFile(ABC):
    """Абстрактный класс для добавления данных в файл, получения данных из файла по указанным критериям и удаления
    информации о вакансиях"""

    def __init__(self, vacancies_file: Any):
        self.vacancies_file = vacancies_file

    @abstractmethod
    def add_info(self, data: list[dict[str, Any]]) -> None:
        """Метод для добавления информации в файл"""
        pass

    @abstractmethod
    def get(self, criteria: str) -> list[dict[str, Any]] | str:
        """Метод для получения информации по критериям из файла"""
        pass

    @abstractmethod
    def delete_info(self) -> None:
        """Метод для удаления информации из файла"""
        pass


class WorkingDataJSON(WorkingFile):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, vacancies_file: Any):
        super().__init__(vacancies_file)

    def add_info(self, data: list[dict[str, Any]]) -> None:
        """Метод для добавления информации в файл"""
        try:
            with open(self.vacancies_file, "r", encoding="UTF8") as f:
                data_json = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_json = []
        data_json.append(data)
        with open(self.vacancies_file, "w", encoding="UTF8") as f:
            json.dump(data_json, f, ensure_ascii=False, indent=2)

    def get(self, criteria: str) -> list[dict[str, Any]] | str:
        """Метод для получения информации по критериям из файла"""
        try:
            with open(self.vacancies_file, 'r', encoding="UTF8") as f:
                data_info = json.load(f)
                answer = []
                for dict_data in data_info:
                    for value in dict_data.values():
                        if isinstance(value, str) and criteria.lower() in value.lower():
                            answer.append(dict_data)
                return answer if answer else "Данный критерий отсутствует в файле"
        except FileNotFoundError:
            return "Файл не найден"

    def delete_info(self) -> None:
        """Метод для удаления информации из файла"""
        with open(self.vacancies_file, 'r+') as f:
            f.truncate(0)


if __name__ == "__main__":
    file_worker = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies_hh")
    answer = WorkingDataJSON(file_worker)
    res = answer.get("разработчик")
    for i in res:
        print(i)
