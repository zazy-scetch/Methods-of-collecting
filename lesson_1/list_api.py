"""2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
   требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл."""

import requests
import sys
import json


URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=e4d256314b984424bb9122029222302&q=London&fx=no&cc=no&mca=yes&format=xml'


def _main():
    """Entry point."""
    req = requests.get(URL + '/getMe')

    with open('lesson_1/response.json', 'w') as f_obj:
        json.dump(req.text, f_obj)


if __name__ == '__main__':
    sys.exit(_main())