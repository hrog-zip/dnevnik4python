from dnevnik4python import * 
import datetime

login = "login"
password = "password"

# войти в аккаунт
d = Diary(login, password)

# получить дневник на сегодня
print(d.get_diary(datetime.datetime.now()))
