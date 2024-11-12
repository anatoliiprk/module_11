import requests
import pandas

print('------\nЗадание по теме "Обзор сторонних библиотек"\n------')

# Запрос данных с сайта и вывод их в консоль с помощью библиотеки requests

print('Библитека requests')

response1 = requests.get('https://api.github.com') # создание запроса
print(response1.ok) # проверка успешен ли запрос
print((response1.status_code)) # статус запроса
print(response1.text) # одержимое ответа

post_params = {'param1': 'value1', 'param2': 'value2'}
response2 = requests.post('https://httpbin.org/post', post_params, timeout=2) # post-запрос
print(response2.json()['form']) # вывод словаря с данными запроса

print('---')


# Считывание данных и анализ данных из файла с использованием библиотеки pandas

dataframe = pandas.read_csv('data.txt', sep=' ', header=None) # чтение данных из файла
print(f'Количество строк в файле: {dataframe.shape[0]}') # Вывод количества строк в файле
print(f'Количество столбцов в файле: {dataframe.shape[1]}\n') # Вывод количества столбцов в файле
all_data = dataframe.describe(percentiles=None, include=None, exclude=None) # Описательная статистика данных файла
print(all_data)
print(dataframe.tail(1)) # Вывод заданного количества последних строк

print('------')
