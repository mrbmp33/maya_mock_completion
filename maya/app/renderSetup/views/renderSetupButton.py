from PySide2.QtGui import QColor
from PySide2.QtCore import QSize
from PySide2.QtGui import QImage
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QEvent
from PySide2.QtWidgets import QStyleOptionButton
from PySide2.QtWidgets import QStyle
from PySide2.QtWidgets import QToolTip
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QAbstractButton
from PySide2.QtGui import QIcon

if False:
    from typing import Dict, List, Tuple, Union, Optional


class RenderSetupButton(QAbstractButton):
    """
    This class represents a render setup button which is an icon button that produces a brighter version of the icon when hovered over.
    """

    def __init__(self, parent, icon, size='40.0', isEnabled='True'): pass

    def createOption(self): pass

    def createPixmap(self, option): pass

    def drawControl(self, element, option, painter, widget='None'):
        """
        Draws the icon button
        """
        pass

    def enterEvent(self, event): pass

    def event(self, event): pass

    def generateDisabledIconPixmap(self, pixmap): pass

    def generateHighlightedIconPixmap(self, pixmap): pass

    def generateIconPixmap(self, pixmap, type):
        """
        # Code taken from QadskDarkStyle.cpp - QadskDarkStyle::generatedIconPixmap
        """
        pass

    def generatePixmapActiveIcon(self, iconMode, pixmap, option): pass

    def getGeneratedIconPixmap(self, iconMode, pixmap, option):
        """
        Draws the icon button brighter when hovered over.
        """
        pass

    def isEnabled(self): pass

    def leaveEvent(self, event): pass

    def paintEvent(self, e):
        """
        Draws the render setup button
        """
        pass

    def setEnabled(self, enabled): pass

    def sizeHint(self): pass

    ADJUSTMENT = 50

    DEFAULT_BUTTON_SIZE = 40.0

    DISABLED = 0

    HIGHLIGHTED = 1

    HIGH_LIMIT = 205

    LOW_LIMIT = 30

    MAX_VALUE = 255

    staticMetaObject = None


def qRgba(*args, **kwargs): pass


def qAlpha(*args, **kwargs): pass
