import json
import os
from abc import ABC
from abc import abstractmethod

from src.job_comparison import Vacancies
from src.utils import formater


class WorkingFile(ABC):
    """Абстрактный класс для добавления данных в файл, получения данных из файла по указанным критериям и удаления
    информации о вакансиях"""

    def __init__(self, vacancies_file: str):
        self.__vacancies_file = vacancies_file

    @property
    def file_vac(self) -> str:
        return self.__vacancies_file

    @abstractmethod
    def add_info(self, data: Vacancies) -> None:
        """Метод для добавления информации в файл"""
        pass

    @abstractmethod
    def get(self, criteria: str) -> list[Vacancies] | str:
        """Метод для получения информации по критериям из файла"""
        pass

    @abstractmethod
    def delete_info(self) -> None:
        """Метод для удаления информации из файла"""
        pass


class WorkingDataJSON(WorkingFile):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, vacancies_file: str = os.path.join(os.path.dirname(__file__), "..", "data", "vacancies_hh")):
        super().__init__(vacancies_file)

    def add_info(self, data: Vacancies) -> None:
        """Метод для добавления информации в файл"""
        try:
            with open(self.file_vac, "r", encoding="UTF8") as f:
                data_json = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_json = []
        data_dict = {item["id"]: item for item in data_json}
        data_dict_vac = data.to_dict()
        if data_dict_vac["id"] is None:
            return
        if data_dict_vac["id"] not in data_dict:
            data_json.append(data_dict_vac)
        with open(self.file_vac, "w", encoding="UTF8") as f:
            json.dump(data_json, f, ensure_ascii=False, indent=2)

    def get(self, criteria: str) -> list[Vacancies] | str:
        """Метод для получения информации по критериям из файла"""
        try:
            with open(self.file_vac, 'r', encoding="UTF8") as f:
                data_info = json.load(f)
                answer = []
                for dict_data in data_info:
                    flag = False
                    for value in dict_data.values():
                        if isinstance(value, dict):
                            for val in value.values():
                                if isinstance(val, str) and criteria.lower() in val.lower():
                                    flag = True
                                    break
                        elif isinstance(value, str) and criteria.lower() in value.lower():
                            flag = True
                        if flag:
                            formatted = formater([dict_data])[0]
                            answer.append(formatted)
                            break
                return answer if answer else "Данный критерий отсутствует в файле"
        except FileNotFoundError:
            return "Файл не найден"

    def delete_info(self) -> None:
        """Метод для удаления всей информации из файла"""
        with open(self.file_vac, 'r+') as f:
            f.truncate(0)

    def delete_vac(self, id: int) -> None:
        """Метод для удаления вакансии из файла по id"""
        try:
            with open(self.file_vac, "r", encoding="UTF8") as f:
                data_json = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_json = []
        data = [vac for vac in data_json if vac.get("id") != id]
        with open(self.file_vac, "w", encoding="UTF8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    answer = WorkingDataJSON()
    vacancy = Vacancies("Программист", "ссылка", 50000, 100000, "работа в офисе", "Москва", "RUR", 111)
    answer.add_info(vacancy)
    print(answer.get("Программист"))
