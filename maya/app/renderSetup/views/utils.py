from PySide2.QtWidgets import QSizePolicy
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QMouseEvent
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QHBoxLayout
from maya.app.renderSetup.model.progressObservable import ProgressObservable
from functools import partial
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFrame

if False:
    from typing import Dict, List, Tuple, Union, Optional


class ProgressBar(object):
    def __init__(self): pass

    def createProgressBar(self): pass

    def endProgressBar(self): pass

    def reactToItemChangedNotification(self, *posArgs, **kwArgs):
        """
        The subject of observation sends messages in the form of classes to
        indicate that progress has started or ended. Otherwise, it sends
        information about the progress estimated to be done
        (as a value from 0 to 1) and a message to be displayed.
        """
        pass

    def registerAsProgressObserver(self): pass

    def stepProgressBar(self, progress, info): pass

    def unregisterAsProgressObserver(self): pass

    __dict__ = None

    __weakref__ = None


class NodeListView:
    def __init__(self, title): pass

    def buildViewObjects(self, names): pass

    def onOKButton(self, data, msg): pass

    def onSelectAllButton(self, data, treeView, names): pass

    def selectTreeCallBack(self, *args): pass

    def show(self, names): pass


class LabelFieldButtonGrp(QWidget):
    """
    Same as cmds.textFieldButtonGrp, but with better controls on each different widgets.
    (ex: more control on callbacks, tooltips and such).
    """

    def __init__(self, label='None', text='None', placeholder='None', tooltip='None', button='None'): pass

    @property
    def button(self): pass

    @property
    def field(self): pass

    @property
    def label(self): pass

    @property
    def layout(self): pass

    staticMetaObject = None


class Separator(QWidget):
    """
    Same as cmds.separator(), except it allows to add a text in the middle of the separator.
    Ex: -------------- My Section --------------
    """

    def __init__(self, text='None'): pass

    staticMetaObject = None


def updateMouseEvent(event): pass


def wrapInstance(*args, **kwargs): pass


def getExpandedState(node):
    """
    Retrieves the expanded state attribute of the node
    """
    pass


def createPixmap(imageName, width='0', height='0'): pass


def createIconWithOnOffStates(pixmapOffState, pixmapOnState):
    """
    Create an icon with on/off states. Each state has a different pixmap.
    """
    pass


def createIcon(iconName): pass


def browse(fileNameAttr): pass


def dpiScale(value): pass


def setExpandedState(node, value):
    """
    Sets an attribute on the node storing the expanded state of
    this node in the view. Creates it if it doesn't exist
    """
    pass


kSelectAll = []

kImageNotFoundError = []

kIconNotFoundError = []

kNbObjects = []

kExpandedStateString = 'expandedState'

kOK = []

_DPI_SCALE = 2.0
