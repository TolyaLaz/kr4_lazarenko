def get_vacancies_by_salary(vacancies_data: list, salary_range: str) -> list:
    """
    Фильтрует вакансии в пределах заданного диапазона зарплат.

    :param vacancies_data: Список объектов вакансий для фильтрации.
    :param salary_range: Строка, указывающая минимальное и максимальное значения заработной платы.

    :return: Отфильтрованный список объектов вакансий в пределах диапазона заработной платы.
    """
    min_salary, max_salary = map(int, salary_range.split('-'))
    ranged_vacancies = []
    for vacancy in vacancies_data:
        if vacancy.salary_from is not None and vacancy.salary_to is not None:
            if vacancy.salary_from >= min_salary and vacancy.salary_to <= max_salary:
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies_data: list) -> list:
    """
    Сортирует список вакансий по начальной зарплате в порядке убывания.

    :param vacancies_data: Список объектов вакансий для сортировки.

    :return: Отсортированный список объектов вакансий.
    """
    return sorted(vacancies_data, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies_data: list, top_n) -> list:
    """
    Возвращает N лучших вакансий из отсортированного списка.

    :param vacancies_data: Отсортированный список объектов вакансий.
    :param top_n: Количество вакансий для возврата.

    :return: Топ N вакансий.
    """
    return vacancies_data[:top_n]


def filter_vacancies(vacancies, filter_words) -> list:
    """
    Фильтрует вакансии по ключевым словам в описании.

    :param vacancies: Список объектов вакансий для фильтрации.
    :param filter_words: Список ключевых слов для фильтрации.
    :return: Список отфильтрованных вакансий.
    """
    return [vac for vac in vacancies if vac.description and any(word in vac.description for word in filter_words)]
