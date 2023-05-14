from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow
from maya.app.renderSetup.views.renderSetupStyle import RenderSetupStyle
from PySide2.QtWidgets import QLayoutItem
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QMenu
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QPen
from PySide2.QtWidgets import QTreeView
from PySide2.QtWidgets import QToolTip
from PySide2.QtCore import QEvent
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import QModelIndex
from maya.app.renderSetup.views.renderSetupButton import RenderSetupButton
from PySide2.QtWidgets import QAbstractItemView
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QFrame
from PySide2.QtGui import QIcon
from maya.app.renderSetup.lightEditor.views.delegate import LightEditorDelegate
from PySide2.QtCore import QPersistentModelIndex
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMenuBar
from PySide2.QtCore import QItemSelectionModel
from PySide2.QtWidgets import QBoxLayout

if False:
    from typing import Dict, List, Tuple, Union, Optional


class LightEditorCentralWidget(QWidget):
    """
    This class implements the controls inside the light editor window
    """

    def __init__(self, parent): pass

    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def getLightCreator(self, lightType): pass

    def minimumSizeHint(self): pass

    def newGroup(*args, **kwargs): pass

    def newLight(*args, **kwargs): pass

    def renderSetupAdded(self): pass

    def renderSetupPreDelete(self): pass

    def selectionChanged(self): pass

    def sizeHint(self): pass

    BUTTON_SIZE = 40.0

    MINIMUM_SIZE = None

    PREFERRED_SIZE = None

    staticMetaObject = None


class LightEditorView(QTreeView):
    """
    This class implements the light editor view.
    """

    def __init__(self, parent): pass

    def aboutToDelete(self): pass

    def eventFilter(self, object, event): pass

    def leaveEvent(self, *args, **kwargs): pass

    def mouseDoubleClickEvent(self, event): pass

    def mouseMoveEvent(self, event): pass

    def mousePressEvent(self, event): pass

    def mouseReleaseEvent(self, event): pass

    def paintEvent(self, e):
        """
        Overrides the paint event to make it so that place holder text is displayed when the list is empty.
        """
        pass

    def refreshView(self): pass

    def rowsInserted(self, parent, start, end): pass

    def setExpanded(self, index, state):
        """
        Override from the Qt class
        Expands the group and saves its state
        """
        pass

    def showContextMenu(self, point):
        """
        Rebuild from scratch the context menu
        """
        pass

    HALF_FONT_HEIGHT = 14.0

    NO_LIGHTS_IMAGE_SIZE = 124.0

    PLACEHOLDER_TEXT_PEN = None

    staticMetaObject = None


class LightEditorWindow(MayaQWidgetDockableMixin, QWidget):
    """
    This class implements the dockable light editor window.
    """

    def __init__(self): pass

    def aboutToDelete(self): pass

    def minimumSizeHint(self): pass

    def setSizeHint(self, size): pass

    def show(self, *args, **kwargs): pass

    def sizeHint(self): pass

    MINIMUM_SIZE = None

    PREFERRED_SIZE = None

    STARTING_SIZE = None

    staticMetaObject = None

    width = 600


class LookThroughWindow(MayaQWidgetDockableMixin, QWidget):
    """
    This class implements the look through window.
    """

    def __init__(self): pass

    def aboutToDelete(self): pass

    def lookThroughLight(self, light):
        """
        Opens a model panel with camera looking through the given light.
        """
        pass

    def minimumSizeHint(self): pass

    def setSizeHint(self, size): pass

    def sizeHint(self): pass

    MINIMUM_SIZE = None

    PREFERRED_SIZE = None

    STARTING_SIZE = None

    staticMetaObject = None


def lookThroughWindowChanged(): pass


def lookThroughSelectedLight(): pass


def createLightEditorWindow(restore='False'):
    """
    # Sets up the light editor main window
    """
    pass


def saveWindowState(editor, optionVar): pass


def lookThroughWindowClosed(): pass


def getCppPointer(*args, **kwargs): pass


def createLookThroughWindow(restore='False'): pass


def propertyEditorWindowClosed(): pass


def lightEditorWindowChanged(): pass


def lightEditorWindowClosed(): pass


def propertyEditorWindowChanged(): pass


def createPropertyEditorWindow(restore='False'): pass


kLayerText = []

kLookThroughLightsToolTip = []

kSnapToSelectedToolTip = []

kHelp = []

_lightEditorWindow = None

kLightEditorTitle = []

kMayaHelp = []

kLightEditorHelp = []

kDefaultLayerText = []

kPropertyEditorToolTip = []
