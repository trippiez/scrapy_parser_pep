# Парсер документов PEP

## Описание проекта

Этот парсер разработан на базе фреймворка Scrapy для извлечения информации из документов PEP (Python Enhancement Proposals) с официального сайта Python.
Он позволяет получить данные о номере, названии и статусе каждого PEP-документа, а также сгенерировать сводку по статусам PEP в виде файла с информацией о количестве документов в каждом статусе, включая общее количество.

## Функциональность

- **Получение информации о PEP**: Извлекает номер, название и статус каждого PEP-документа.
- **Сводка по статусам PEP**: Генерирует файл со статистикой количества документов в каждом статусе, включая общее количество.

## Использованные технологии

- Python
- Scrapy

## Инструкция по запуску

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:trippiez/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустите парсер для получения списка всех PEP:

```
scrapy crawl pep
```

## Автор

Backend by: @trippiez

## Контакты

Электронная почта: ldqfv@mail.ru