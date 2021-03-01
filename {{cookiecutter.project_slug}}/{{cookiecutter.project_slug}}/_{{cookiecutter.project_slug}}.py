# coding: utf-8

import logging


log = logging.getLogger(__name__)


class MyPublicClass():
    def run(self) -> int:
        print("Hello World")
        return 0
