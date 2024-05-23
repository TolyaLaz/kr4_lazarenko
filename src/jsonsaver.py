import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class Connector(ABC):
    """
    Абстрактный базовый класс, определяющий интерфейс для работы с файлом
    """

    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Абстрактный метод для добавления вакансии.

        :param vacancy: Объект вакансии.
        """
        pass

    @abstractmethod
    def load_vacancies(self, criteria: dict = {}) -> list:
        """
        Абстрактный метод для загрузки вакансий по критериям.

        :param criteria: Критерии для фильтрации вакансий.
        :return: Список вакансий.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Абстрактный метод для удаления вакансии.

        :param vacancy: Объект вакансии.
        """
        pass

class JSONSaver(Connector):
    """
    Класс, определяющий интерфейс для работы с файлом
    """
    FILE_PATH = 'vacancies.json'

    def add_vacancy(self, vacancy):
        """
        Добавляет вакансию в файл.

        :param vacancy: Объект вакансии.
        """
        vacancies = self._load_vacancies()
        vacancies.append(vacancy.to_dict())
        self._save_vacancies(vacancies)

    def load_vacancies(self, criteria: dict = {}) -> list:
        """
        Загружает вакансии из файла по критериям.

        :param criteria: Критерии для фильтрации вакансий.
        :return: Список вакансий.
        """
        return [Vacancy.from_dict(item) for item in self._load_vacancies()]

    def _load_vacancies(self) -> list:
        """
        Загружает вакансии из файла.

        :return: Список вакансий.
        """
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8', errors='replace') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_vacancies(self, vacancies: list):
        """
        Сохраняет вакансии в файл.

        :param vacancies: Список вакансий.
        """
        with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        vacancies = self._load_vacancies()
        vacancies = [v for v in vacancies if v['url'] != vacancy.url]
        self._save_vacancies(vacancies)
