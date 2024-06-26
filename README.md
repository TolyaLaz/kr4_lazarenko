Описание проекта
Этот проект представляет собой инструмент для работы с вакансиями, опубликованными на сайте HeadHunter. Он позволяет пользователям искать вакансии по заданным критериям, сохранять результаты поиска, фильтровать и сортировать вакансии, а также выводить топ вакансий согласно заданным параметрам.

Структура проекта
Проект состоит из следующих основных компонентов:

main.py: Основной скрипт, который управляет взаимодействием с пользователем и вызывает другие модули для выполнения операций. src/: Каталог, содержащий основные модули проекта: headhunterapi.py: Модуль для взаимодействия с API HeadHunter и получения данных о вакансиях. jsonsaver.py: Модуль для управления данными о вакансиях, включая сохранение, загрузку и удаление вакансий из файла. vacancy.py: Модель данных для представления вакансии. utils.py: Утилитарные функции для фильтрации, сортировки и выборки вакансий.

Запуск проекта Для запуска проекта необходимо выполнить следующие шаги:

Установите все необходимые зависимости, используя команду: poetry update Запустите основной скрипт: python main.py Использование После запуска main.py программа предложит вам ввести поисковый запрос. После этого будут выполнены следующие действия:

Поиск вакансий на HeadHunter с использованием введенного запроса. Сохранение найденных вакансий в файл. Фильтрация и сортировка вакансий по диапазону зарплат.
