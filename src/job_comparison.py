class Vacancies:
    __slots__ = ['name', 'link', 'salary_from', 'salary_to', 'description', 'area', 'currency_vac', 'id_vac']

    """Класс для основных характеристик вакансии"""
    def __init__(self, name: str, link: str, salary_from: int, salary_to: int, description: str, area: str,
                 currency_vac: str, id_vac: int):
        self.name = self.__valid_name(name)
        self.link = self.__valid_link(link)
        self.salary_from = self.__valid_salary_from(salary_from)
        self.salary_to = self.__valid_salary_to(salary_to)
        self.description = self.__valid_description(description)
        self.area = self.__valid_area(area)
        self.currency_vac = self.__valid_currency_vac(currency_vac)
        self.id_vac = self.__valid_id_vac(id_vac)

    @staticmethod
    def __valid_name(name: str) -> str:
        """Метод для проверки соответствия названия вакансии"""
        if not name.strip():
            raise ValueError("Название вакансии не может быть пустым")
        if not isinstance(name, str):
            raise TypeError("Название должно передаваться строкой")
        return name

    @staticmethod
    def __valid_link(link: str) -> str:
        """Метод для проверки соответствия типа ссылки"""
        if not isinstance(link, str):
            raise TypeError("Ссылка должна быть строкой")
        return link

    @staticmethod
    def __valid_salary_from(salary_from: int) -> int:
        """Метод для проверки соответствия типа зарплаты"""
        if not salary_from or salary_from <= 0:
            return 0
        else:
            return salary_from

    @staticmethod
    def __valid_salary_to(salary_to: int) -> int:
        """Метод для проверки соответствия типа зарплаты"""
        if not salary_to or salary_to <= 0:
            return 0
        else:
            return salary_to

    @staticmethod
    def __valid_description(description: str) -> str:
        """Метод для проверки соответствия типа описания вакансии"""
        if not isinstance(description, str):
            raise TypeError("Описание должно быть строкой")
        return description

    @staticmethod
    def __valid_area(area: str) -> str:
        """Метод для проверки соответствия типа города"""
        if not isinstance(area, str):
            raise TypeError("Город должен быть передан строкой")
        return area

    @staticmethod
    def __valid_currency_vac(currency_vac: str) -> str:
        """Метод для проверки соответствия типа валюты"""
        if not isinstance(currency_vac, str):
            raise TypeError("Валюта должна быть передана строкой")
        return currency_vac

    @staticmethod
    def __valid_id_vac(id: int) -> int:
        """Метод для проверки соответствия типа идентификатора"""
        if not isinstance(id, int):
            raise TypeError("Идентификатор должен быть передан числами")
        return id

    def __le__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Уступает или равна наша вакансия другой в зарплате?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        self_salary = self.salary_from or 0
        other_salary = other.salary_from or 0
        return self_salary <= other_salary

    def __ge__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Лучше или равна наша вакансия по зарплате, другой?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        self_salary = self.salary_from or 0
        other_salary = other.salary_from or 0
        return self_salary >= other_salary

    def __lt__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Уступает ли наша вакансия другой в зарплате?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        self_salary = self.salary_from or 0
        other_salary = other.salary_from or 0
        return self_salary < other_salary

    def __gt__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Лучше ли наша вакансия по зарплате, чем другая?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        self_salary = self.salary_from or 0
        other_salary = other.salary_from or 0
        return self_salary > other_salary

    def to_dict(self) -> dict:
        """Метод для превращения вакансии в словарь"""
        return {
            "id": self.id_vac,
            "name": self.name,
            "alternate_url": self.link,
            "salary": {
                "from": self.salary_from,
                "to": self.salary_to,
                "currency": self.currency_vac
            },
            "area": {"name": self.area},
            "snippet": {"responsibility": self.description}
        }


if __name__ == "__main__":
    vac = Vacancies("Программист", "ссылка", 50000, 10000, "работа в офисе", "Москва", "RUR", 123)
    vac1 = Vacancies("Программист2", "ссылка2", -5,  10, "работа в офисе", "Питер", "RUR", 567)
    print(vac1.salary_to)
    print(vac > vac1)
    print(vac <= vac1)
