# @Time    : 2018/3/14 18:24
# @Author  : Alienzjn
# @Email   : zjning95@126.com
# @File    : atm.py

import os

import sys

BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.append(BASE_DIR)

from conf import settings
from core import main

main.login()


