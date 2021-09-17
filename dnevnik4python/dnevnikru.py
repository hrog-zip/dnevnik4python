from bs4 import BeautifulSoup
from requests import Session
from fake_useragent import UserAgent
from os import getenv
from json import loads as json_loads
from json import dumps as json_dumps
from datetime import datetime, timezone
import pytz

from .exceptions import *

class DiaryBase:
    """docstring for Diary."""

    login_url =  "https://login.dnevnik.ru/login"
    userfeed_url = "https://dnevnik.ru/userfeed"

    def __init__(self):
        self.session = Session()
        # "Referer" is needed
        self.session.headers = {"User-Agent": UserAgent().random,
                                "Referer": self.login_url}
    
    # simple wrappers for 'get' and 'post' methods from requests library
    def _get(self, url):
        r = self.session.get(url)

        if r.status_code != 200:
            if not self.servers_are_ok():
                raise ServersAreDownException("Dnevnik.ru servers are down, please retry later")
            else:
                raise NotOkCodeReturn(f"Get request to {url} resulted in {r.status_code} status code")
        return r

    def _post(self, url, data = {}):
        r = self.session.post(url, data)

        if r.status_code != 200:
            if not self.servers_are_ok():
                raise ServersAreDownException("Dnevnik.ru servers are down, please retry later")
            else:
                raise NotOkCodeReturn(f"Post request to {url} resulted in {r.status_code} status code")
        return r

    def servers_are_ok(self):
        r = self.session.get("https://dnevnik.ru/")
        if r.status_code != 200:
            return False
        return True

    def auth(self, login, password):
         r = self._post(self.login_url, data={"login": login, "password": password})
         # check if we accessed userfeed page
         if r.url != self.userfeed_url:
            raise Exception()
    
    def parse_user_data(self):
        r = self._get(self.userfeed_url)

        if r.status_code != 200 or r.url != self.userfeed_url:
                raise DataParseError("Cant reach userfeed")

        soup = BeautifulSoup(r.text, 'lxml')

        for script in soup.findAll("script"):
            if 'window.__TALK__INITIAL__STATE__' not in script.next:
                continue
            # remove everything we dont need
            raw_initial_info = script.next
            raw_initial_info = raw_initial_info.split('window.__TALK__INITIAL__STATE__')[0]
            raw_initial_info = raw_initial_info.replace('window.__USER__START__PAGE__INITIAL__STATE__ = ', '')
            raw_initial_info = raw_initial_info.strip()[:-1]
            json = json_loads(raw_initial_info)
            info = json['userSchedule']['currentChild']
            return info['schoolId'], info['groupId'], info['personId']

        raise DataParseError("Cannot find user info in userfeed page")


class Diary(DiaryBase):
    """docstring for Diary."""

    def __init__(self, login, password):
        super().__init__()

        self.auth(login, password)
        # parse data about user
        self.school_id, self.group_id, self.person_id = self.parse_user_data()
    
    def get_diary(self, date: datetime, span: int = 1, utc_aware: bool = False):
        # convert date to timestamp
        if not utc_aware:
            timestamp_date = int(datetime(year = date.year, month = date.month, day = date.day).replace(tzinfo = pytz.utc).timestamp())
        else:
            timestamp_date = int(datetime(year = date.year, month = date.month, day = date.day).timestamp())

        r = self._get(f'https://dnevnik.ru/api/userfeed/persons/'
                      f'{self.person_id}/schools/'
                      f'{self.school_id}/groups/'
                      f'{self.group_id}/schedule?'
                      f'date={timestamp_date}&'
                      f'takeDays={span}')
        return r.text
