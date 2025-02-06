
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import maya.api.OpenMaya as om

class ActiveSelection:

    def __init__(self):
        self._selection: list['om.MObject']= []

    def add(self, node):
        self._selection.append(node)
    
    def extend(self, nodes: list['om.MObject']):
        self._selection.extend(nodes)

    def remove(self, node):
        self._selection.remove(node)

    def clear(self):
        self._selection = []

    def get(self):
        return self._selection

    def __iter__(self):
        return iter(self._selection)

    def __len__(self):
        return len(self._selection)
    
    def __getitem__(self, index):
        return self._selection[index]
    
    def __setitem__(self, index, value):
        self._selection[index] = value

    def __delitem__(self, index):
        del self._selection[index]
    
    def __contains__(self, item):
        return item in self._selection
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self._selection})"

    def replace_all(self, nodes: list['om.MObject']):
        self._selection = nodes

    def replace(self, index: int, node: 'om.MObject'):
        self._selection[index] = node

    def index(self, node):
        return self._selection.index(node)
    
    @property
    def as_list(self) -> list['om.MObject']:
        return self._selection
    
    @property
    def length(self) -> int:
        return len(self._selection)