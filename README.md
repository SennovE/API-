# API для анализа текста
Веб сервис, который может быть использован для определения тональности или языка текста.

Сервис может быть использован для автоматического разделения отзывов.

## Возможности:
- Определение тональности текста: Анализ текста на предмет его эмоциональной окраски (от 1 (крайне позитивный) до -1 (крайне негативный)).
- Определение языка текста: Определение языка, на котором написан текст.

### Требования для запуска:
- `Python 3.11`
- `Poetry`

### Установка и запуск
- Создание виртуального окружения и установка зависимостей:

  `poetry install`

- Активация виртуального окружения:

  `poetry shell`

- Запуск сервиса

  `make run`

После запуска запросы можно отправлять через POST запросы.

С документацией можно ознакомиться после запуска по адресу [http://127.0.0.1:8000/docs ](http://127.0.0.1:8000/docs ).
