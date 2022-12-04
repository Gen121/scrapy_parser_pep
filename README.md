# Проект парсинга Python документации с использованием фреймворка Scrapy

## Описание

Парсинг данных статусов PEP'ов документации Python. С выводом данных в csv формате.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Gen121/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить парсинг:

```
scrapy crawl pep
```
