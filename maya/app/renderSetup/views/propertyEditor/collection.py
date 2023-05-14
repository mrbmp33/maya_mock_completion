from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGroupBox
from functools import partial

if False:
    from typing import Dict, List, Tuple, Union, Optional

from . import basicCollection


class Collection(basicCollection.BasicCollection):
    """
    This class represents the property editor view of a collection.
    """

    def __del__(self): pass

    def __init__(self, item, parent): pass

    def dataModelChanged(self, *posArgs, **kwArgs): pass

    def getModelSelector(self): pass

    def highlight(self, names): pass

    def isAbsoluteMode(self): pass

    def populateFields(self): pass

    def postSelector(self): pass

    def preSelector(self):
        """
        Create UI displayed above selector UI.
        """
        pass

    def setupSelector(self, layout): pass

    staticMetaObject = None


kViewCollectionObjects = []

kRelativeWarning = []

kSelectAll = []

kViewAllTooltip = []

kViewAll = []

kAddOverrideTooltipStr = []

vSpc = 3

kSelectAllTooltip = []

kDragAttributesFromAE = []

kNbObjects = []

kOK = []

kAddOverride = []

hSpc = 10
