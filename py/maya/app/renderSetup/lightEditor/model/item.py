if False:
    from typing import Dict, List, Tuple, Union, Optional

import maya.app.renderSetup.model.childNode as childNode


class LightItemBase(childNode.TreeOrderedItem, childNode.ChildNode):
    """
    Base class for light editor items
    """

    def __init__(self): pass

    def activate(self): pass

    def compute(self, plug, dataBlock): pass

    def deactivate(self): pass

    def detachFromParent(self): pass

    def dispose(self, deleteLight): pass

    def enabledChanged(self): pass

    def getChildren(self, cls='"<class \'maya.app.renderSetup.model.childNode.ChildNode\'>"'): pass

    def getLayerNumIsolatedChildren(self): pass

    def getNumIsolatedAncestors(self): pass

    def getNumIsolatedChildren(self, includeSelf='False'): pass

    def hasIsolatedAncestors(self, dataBlock='None'): pass

    def hasIsolatedChildren(self, dataBlock='None'): pass

    def isAbstractClass(self): pass

    def isAcceptableChild(self, model):
        """
        Check if the model could be a child
        """
        pass

    def isEnabled(self): pass

    def isIsolateSelected(self, dataBlock='None'): pass

    def isSelfEnabled(self, dataBlock='None'): pass

    def postConstructor(self): pass

    def setIsolateSelected(self, value): pass

    def setSelfEnabled(self, value): pass

    def typeId(self): pass

    def typeName(self): pass

    def updateIsolateState(self, numIsolatedAncestors='0'):
        """
        Update the isolate state in the item hierarchy.
        
        Pushing the number of isolated ancestors down the tree,
        and pulling the number of isolated children back up.
        """
        pass

    @classmethod
    def creator(cls):
        """
        # Awkwardly, abstract base classes seem to need a creator method.
        """
        pass

    @staticmethod
    def initializer(): pass

    ATTRIBUTE_COLOR = 2

    ATTRIBUTE_EXPOSURE = 1

    ATTRIBUTE_INTENSITY = 0

    enabled = None

    isolateSelected = None

    kTypeId = None

    kTypeName = 'lightItemBase'

    layerNumIsolatedChildren = None

    numIsolatedAncestors = None

    numIsolatedChildren = None

    parentEnabled = None

    selfEnabled = None


def createItem(*args, **kwargs): pass


def deleteItem(*args, **kwargs): pass


def getLightItemName(lightShapeObj): pass


kSet = []
