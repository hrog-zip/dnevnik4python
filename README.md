# dnevnikru4python

Dnevnikru4python - это библиотека для Python позволяющая удобно работать с электронным дневником dnevnik.ru
Главное отличие от оффициального API это то, что не требуется заключать договор и регестрировать приложение  

- Простая с работа с Дневником
- Получение оценок, д/з, расписания уроков 

## Пример

```python
from dnevnikru4python import * 
import datetime

login = "login"
password = "password"

# войти в аккаунт
d = Diary(login, password)

# получить дневник на сегодня
print(d.get_diary(datetime.datetime.now()))
```
## Планы на будующее
- Сделать библиотеку более удобной в использовании

