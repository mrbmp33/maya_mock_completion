if False:
    from typing import Dict, List, Tuple, Union, Optional

import maya.app.renderSetup.model.nodeList as nodeList
from . import item as itemModel


class LightGroup(nodeList.ListBase, itemModel.LightItemBase):
    """
    Light Editor item for groups
    """

    def __init__(self): pass

    def appendChild(*args, **kwargs): pass

    def attachChild(*args, **kwargs): pass

    def detachChild(*args, **kwargs): pass

    def dispose(self, deleteLight): pass

    def getChildren(self, cls='"<class \'maya.app.renderSetup.model.childNode.ChildNode\'>"'):
        """
        Get the list of all children. 
        Optionally only the children matching the given class.
        """
        pass

    def isAbstractClass(self): pass

    def isAcceptableChild(self, model):
        """
        Check if the model could be a child
        """
        pass

    def rename(self, newName): pass

    @classmethod
    def creator(cls): pass

    @staticmethod
    def initializer(): pass

    firstItem = None

    items = None

    kTypeId = None

    kTypeName = 'lightGroup'

    lastItem = None


kChildAttached = []

kChildDetached = []
