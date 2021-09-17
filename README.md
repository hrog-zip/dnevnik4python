# dnevnikru4python

Dnevnik4python - это библиотека для Python позволяющая удобно работать с электронным дневником dnevnik.ru
Главное отличие от оффициального API это то, что не требуется заключать договор и регестрировать приложение  

- Простая с работа с Дневником
- Получение оценок, д/з, расписания уроков 

## Пример

```python
from dnevnik4python import * 
import datetime

login = "login"
password = "password"

# войти в аккаунт
d = Diary(login, password)

# получить дневник на сегодня
print(d.get_diary(datetime.datetime.now()))
```

## Установка
### *Linux/macOS*
```
pip3 install dnevnikru4py
```
### *Windows*
```
pip install dnevnikru4py
```

## Планы на будущее
- Сделать библиотеку более удобной в использовании

