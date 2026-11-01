# Работа с ORM

## Каталог телефонов


## Подготовка

Нужны Python, PostgreSQL и работающий сервер PostgreSQL.


Создайте базу данных `netology_import_phones`. 

```sql
CREATE DATABASE netology_import_phones;
```


Установите зависимости:

```powershell
py -m pip install -r requirements.txt
```

## Подключение к PostgreSQL

Перед запуском укажите параметры подключения в терминале PowerShell:

```powershell
$env:POSTGRES_DB = "netology_import_phones"
$env:POSTGRES_USER = "postgres"
$env:POSTGRES_PASSWORD = "ваш_пароль"
$env:POSTGRES_HOST = "127.0.0.1"
$env:POSTGRES_PORT = "5432"
```

Вместо `ваш_пароль` укажите пароль пользователя PostgreSQL. 
Настройки подключения находятся в `main/settings.py`. Файл `.env.example` содержит образец параметров.

## Запуск

Примените миграции:

```powershell
py manage.py migrate
```

Импортируйте телефоны из CSV:

```powershell
py manage.py import_phones
```



Проверьте тесты:

```powershell
py manage.py test
```

Запустите сайт:

```powershell
py manage.py runserver
```

## Проверка в браузере

Откройте страницу каталога:

http://127.0.0.1:8000/catalog/

Проверка сортировки:

- По названию: http://127.0.0.1:8000/catalog/?sort=name
- Сначала дешёвые: http://127.0.0.1:8000/catalog/?sort=min_price
- Сначала дорогие: http://127.0.0.1:8000/catalog/?sort=max_price

Страница отдельного телефона:

http://127.0.0.1:8000/catalog/iphone-x/

В исходном файле три телефона: Samsung Galaxy Edge 2, Iphone X и Nokia 8.

## Файлы проекта

- `phones/models.py` — модель телефона.
- `phones/views.py` — вывод каталога, сортировка и страница телефона.
- `phones/management/commands/import_phones.py` — загрузка CSV в базу.
- `phones/tests.py` — тесты.
- `phones/migrations/` — миграции.
- `templates/` — страницы сайта.
- `phones.csv` — исходные данные.
