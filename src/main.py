from src.vacancy import Vacancy
from src.utils import filter_vacancies,get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver



def user_interaction():
    """
    Взаимодействует с пользователем для выполнения операций с вакансиями, полученными из HeadHunter.

    Запрашивает у пользователя поисковый запрос, сохраняет выбранные вакансии и отображает лучшие вакансии на основе определенных пользователем критериев.
    """
    hh_api = HeadHunterAPI()
    search_query = input("Введите ваш запрос (Например: Python): ")
    hh_vacancies = hh_api.load_vacancies(search_query)

    vacancies_list = [Vacancy.from_json(vacancy) for vacancy in hh_vacancies]

    json_saver = JSONSaver()
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Например: 50000 - 350000): ")

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)


    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
