class Vacancies:
    """Класс для основных характеристик вакансии"""
    def __init__(self, name: str, link: str, salary: int | float, description: str, city: str):
        if not isinstance(name, str):
            raise TypeError("Название должно передаваться строкой")
        self.name = name

        if not isinstance(link, str):
            raise TypeError("Ссылка должна быть строкой")
        self.link = link

        if not salary or salary <= 0:
            self.salary: int | float = 0
        else:
            self.salary = salary

        if not isinstance(description, str):
            raise TypeError("Описание должно быть строкой")
        self.description = description

        if not isinstance(city, str):
            raise TypeError("Город должен быть передан строкой")
        self.city = city

    def __le__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Уступает или равна наша вакансия другой в зарплате?"""
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary <= other.salary

    def __ge__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Лучше или равна наша вакансия по зарплате, другой?"""
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary >= other.salary

    def __lt__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Уступает ли наша вакансия другой в зарплате?"""
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other: "Vacancies") -> bool:
        """Магический метод сравнения. Лучше ли наша вакансия по зарплате, чем другая?"""
        if not isinstance(other, Vacancies):
            return NotImplemented
        return self.salary > other.salary


if __name__ == "__main__":
    vac = Vacancies("Программист", "ссылка", 50000, "работа в офисе", "Москва")
    vac1 = Vacancies("Программист2", "ссылка2", 10000, "работа в офисе", "Питер")
    print(vac > vac1)
    print(vac <= vac1)
