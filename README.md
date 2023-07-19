# BMI_App
Non professional app. First try to understand, how to bring up several projects at once

![Логотип проекта](путь_к_логотипу.png)

[![Статус сборки](https://img.shields.io/travis/пользователь/репозиторий.svg)](https://travis-ci.org/пользователь/репозиторий)
[![Лицензия](https://img.shields.io/github/license/пользователь/репозиторий.svg)](https://github.com/пользователь/репозиторий/blob/master/LICENSE.md)

## Описание

Обучение создания оконных приложений на питоне. Попытка интеграции с телеграм-ботом

## Особенности

* Функция 1
* Функция 2
* Функция 3

## Установка

### Требования

* Требование 1
* Требование 2
* Требование 3

### Инструкции по установке

1. Шаг 1
2. Шаг 2
3. Шаг 3

## Использование

Приложение служит одной цели - подсчёт массы тела на основании полученных данных

```python
def calculate():
    height = float(entry_for_height.get())
    weigth = float(entry_for_weigth.get())

    # bmi = weigth / (height ** 2)

    bmi = round(weigth / (height ** 2), 2)
    

    if bmi < 15.99:
        status = 'выраженный дефицит массы тела'
    elif bmi > 16 and bmi < 18.49:
        status = 'недостаточная масса тела'
Вклад