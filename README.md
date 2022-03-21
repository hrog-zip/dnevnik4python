# dnevnik4python

Dnevnik4python - это библиотека для Python позволяющая удобно работать с электронным дневником dnevnik.ru

Главное отличие от оффициального API это то, что не требуется заключать договор и регистрировать приложение  

- Простая с работа с Дневником
- Получение оценок, д/з, расписания уроков 

## Пример

```python
from dnevnik4python import Diary
from datetime import datetime

login = "login"
password = "password"

# войти в аккаунт
d = Diary(login, password)

# получить дневник на сегодня
print(d.get_diary(datetime.now()))
# получить дневник на 2 дня вперед
print(d.get_diary(datetime.now(), 2))
# получить дневник за прошлые 2 дня
print(d.get_diary(datetime.now(), -2))
# получить дневник по указанным датам
print(d.get_diary(datetime(year = 2020, month = 4, day = 1), datetime(year = 2020, month = 4, day = 4)))
```

## Установка
### *Linux/macOS*
```
pip3 install dnevnik4python
```
### *Windows*
```
pip install dnevnik4python
```

## Планы на будущее
- Сделать библиотеку более удобной в использовании

## По всем вопросам
https://t.me/arzt_arsch
