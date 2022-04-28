"""for stuff related to android"""

from typing import Optional

import ujson
from bs4 import BeautifulSoup
from requests import get


magisk_release = (
    "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/{}.json"
)


class Dynamic:
    TIMEOUT = 60


def shared_method() -> None:
    pass
