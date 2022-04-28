"""for stuff related to android"""

from typing import Optional

import ujson
from bs4 import BeautifulSoup
from requests import get
from userge import Message, userge

magisk_release = (
    "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/{}.json"
)
