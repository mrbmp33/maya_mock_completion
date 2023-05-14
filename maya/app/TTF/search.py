if False:
    from typing import Dict, List, Tuple, Union, Optional


class TTFSearch:
    def __init__(self): pass

    def addItem(self, item): pass

    def find(self, searchString): pass


class ClosestMatch:
    def __init__(self, values, maxErr='2'): pass

    def search(self, text): pass

    def searchChildren(self, node, errors): pass

    def searchRecursive(self, node, x, prevErrors): pass


class ClosestMatchNode:
    def __init__(self): pass

    def add(self, text): pass
