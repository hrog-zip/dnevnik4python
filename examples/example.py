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
