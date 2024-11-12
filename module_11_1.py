import requests
import pandas

print('------\nЗадание по теме "Обзор сторонних библиотек"\n------')

# Запрос данных с сайта и вывод их в консоль с помощью библиотеки requests

print('Библитека requests')

response1 = requests.get('https://api.github.com')
print(response1.ok)
print((response1.status_code))
print(response1.text)

post_params = {'param1': 'value1', 'param2': 'value2'}
response2 = requests.post('https://httpbin.org/post', post_params, timeout=2)
print(response2.json()['form'])

print('---')


# Считывание данных и анализ данных из файла с использованием библиотеки pandas

dataframe = pandas.read_csv('data.txt', sep=' ', header=None)
print(f'Количество строк в файле: {dataframe.shape[0]}')
print(f'Количество столбцов в файле: {dataframe.shape[1]}\n')
all_data = dataframe.describe(percentiles=None, include=None, exclude=None)
print(all_data)
print(dataframe.tail(1))

print('------')
