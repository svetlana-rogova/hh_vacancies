class Vacancies:
    __slots__ = ['name', 'link', 'salary', 'description', 'city']

    """Класс для основных характеристик вакансии"""
    def __init__(self, name: str, link: str, salary: int, description: str, city: str):
        self.name = self.__valid_name(name)
        self.link = self.__valid_link(link)
        self.salary = self.__valid_salary(salary)
        self.description = self.__valid_description(description)
        self.city = self.__valid_city(city)

    @staticmethod
    def __valid_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError("Название должно передаваться строкой")
        return name

    @staticmethod
    def __valid_link(link: str) -> str:
        if not isinstance(link, str):
            raise TypeError("Ссылка должна быть строкой")
        return link

    def __valid_salary(self, salary: int) -> int:
        if not salary or salary <= 0:
            return 0
        else:
            return salary

    @staticmethod
    def __valid_description(description: str) -> str:
        if not isinstance(description, str):
            raise TypeError("Описание должно быть строкой")
        return description

    @staticmethod
    def __valid_city(city: str) -> str:
        if not isinstance(city, str):
            raise TypeError("Город должен быть передан строкой")
        return city

    def __le__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Уступает или равна наша вакансия другой в зарплате?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        return self.salary <= other.salary

    def __ge__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Лучше или равна наша вакансия по зарплате, другой?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        return self.salary >= other.salary

    def __lt__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Уступает ли наша вакансия другой в зарплате?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        return self.salary < other.salary

    def __gt__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Лучше ли наша вакансия по зарплате, чем другая?"""
        if not isinstance(other, Vacancies):
            raise TypeError
        return self.salary > other.salary


if __name__ == "__main__":
    vac = Vacancies("Программист", "ссылка", 50000, "работа в офисе", "Москва")
    vac1 = Vacancies("Программист2", "ссылка2", -5, "работа в офисе", "Питер")
    print(vac1.salary)
    print(vac > vac1)
    print(vac <= vac1)
