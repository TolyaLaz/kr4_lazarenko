import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class Connector(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def load_vacancies(self, criteria: dict = {}) -> list:
        pass


class JSONSaver(Connector):
    FILE_PATH = 'vacancies.json'

    def add_vacancy(self, vacancy):
        vacancies = self._load_vacancies()
        vacancies.append(vacancy.to_dict())
        self._save_vacancies(vacancies)

    def load_vacancies(self, criteria: dict = {}) -> list:
        return [Vacancy.from_dict(item) for item in self._load_vacancies()]

    def _load_vacancies(self) -> list:
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8', errors='replace') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_vacancies(self, vacancies: list):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
