from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QStyle

if False:
    from typing import Dict, List, Tuple, Union, Optional

from . import renderSetupButton


class RenderSetupCheckableButton(renderSetupButton.RenderSetupButton):
    """
    This class represents a checkable render setup button. This supports
    2 different pixmaps, one for each state (checked/unchecked)
    """

    def __init__(self, parent, icon, size='40.0', isEnabled='True', isCheckable='False', isChecked='False'): pass

    def createOption(self): pass

    def createPixmap(self, option): pass

    def generatePixmapActiveIcon(self, iconMode, pixmap, option): pass

    def isCheckable(self): pass

    def isChecked(self): pass

    def setCheckable(self, isCheckable): pass

    def setChecked(self, checked): pass

    staticMetaObject = None
