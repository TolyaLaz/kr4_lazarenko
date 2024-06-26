class Vacancy:
    __slots__ = ['__name', 'url', 'description', 'salary_from', 'salary_to', 'currency']

    def __init__(self, name, url, description, salary_from, salary_to, currency):
        """
        Инициализирует объект вакансии.

        :param name: Название вакансии.
        :param url: Ссылка на вакансию.
        :param description: Описание вакансии.
        :param salary_from: Нижняя граница зарплаты.
        :param salary_to: Верхняя граница зарплаты.
        :param currency: Валюта зарплаты.
        """
        self.__name = name
        self.url = url
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта вакансии.

        :return: Строковое представление вакансии.
        """
        return f"\nВакансия: {self.__name}\n" \
               f"Зарплата: {self.salary_from} - {self.salary_to} {self.currency}\n" \
               f"Требования: {self.description}\n" \
               f"Ссылка: {self.url}"

    def __lt__(self, other) -> bool:
        """
        Сравнивает вакансии по нижней границе зарплаты.

        :param other: Другая вакансия.
        :return: Результат сравнения.
        """
        if not isinstance(other, Vacancy):
            raise ValueError("Не является классом Vacancy")
        return self.salary_from < other.salary_from

    @staticmethod
    def from_json(json_item):
        """
        Создает объект вакансии из элемента JSON.

        :param json_item: файл JSON, представляющий вакансию.

        :return: Объект вакансии инициализируется данными из элемента JSON.
        """
        salary_info = json_item.get('salary')
        salary_from = salary_info['from'] if salary_info and 'from' in salary_info else 0
        salary_to = salary_info['to'] if salary_info and 'to' in salary_info else 0
        currency = salary_info['currency'] if salary_info and 'currency' in salary_info else None

        return Vacancy(
            name=json_item['name'],
            url=json_item['alternate_url'],
            description=json_item['snippet']['requirement'],
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency
        )

    def to_dict(self):
        """
        Преобразует объект вакансии в словарь dict.

        :return: Dictionary representation of the Vacancy object.
        """
        return {
            'name': self.__name,
            'url': self.url,
            'description': self.description,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency
        }

    @classmethod
    def from_dict(cls, dict_item):
        """
        Создает объект вакансии из словаря.

        :param dict_item: Dictionary representing a job vacancy.

        :return: Vacancy object initialized with data from the dictionary.
        """
        return cls(**dict_item)
