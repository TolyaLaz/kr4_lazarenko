import requests
from abc import ABC, abstractmethod


class Parser:
    """
    Абстрактный класс для работы с API HeadHunter
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        """
        Метод для загрузки ваканский с заданными параметрами
        """
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Подготавливает параметры запроса и выбирает вакансии на основе поискового запроса.
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': 1, 'only_with_salary': True}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """
        Метод для загрузки ваканский с заданными параметрами
        """
        self.params['text'] = keyword
        while self.params.get('page') != 5:
            response = requests.get(self.__url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                break
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
