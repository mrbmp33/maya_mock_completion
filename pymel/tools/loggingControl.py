from pymel.core.uitypes import Menu as _Menu

if False:
    from typing import Dict, List, Tuple, Union, Optional


class LoggingMenu(_Menu):
    def __init__(self, name='None', parent='None'): pass

    def addHandler(self, logger): pass

    def buildLevelMenu(self, parent, item): pass

    def buildSubMenu(self, parent, logger): pass

    def changeLevel(self, item, level): pass

    def refresh(self, *args): pass

    def refreshLoggingMenu(self): pass

    def setFormatter(self, handler): pass

    @staticmethod
    def __new__(cls, name="'pymelLoggingControl'", parent='None'): pass


def refreshLoggerHierarchy(): pass


def initMenu(): pass


n = 50

logLevelNames = []

logger = None

levelsDict = {}
