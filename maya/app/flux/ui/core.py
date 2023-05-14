from copy import deepcopy
from PySide2.QtCore import Slot

if False:
    from typing import Dict, List, Tuple, Union, Optional

import PySide2.QtWidgets as QtWidgets


class ListButtonItem(QtWidgets.QListWidgetItem):
    def __init__(self, text, parent, index='None'): pass

    def addButton(self, icons, name, alignLeft='True', alignRight='False', highlightable='True'): pass

    def getButton(self, name): pass


class DraggableTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent='None'): pass

    def dragEnterEvent(self, event): pass

    def dragMoveEvent(self, event): pass

    def paintEvent(self, e): pass

    staticMetaObject = None


import PySide2.QtGui as QtGui


class QPainter(QtGui.QPainter):
    """
    # Qt Painter with antialiasing
    """

    def __init__(self, *args): pass


class ImageButton(QtWidgets.QWidget):
    def __init__(self, imageName, text="''", textPos="'bottom'", highlighted='False', parent='None'): pass

    def createBackground(self): pass

    def createButton(self): pass

    def createImage(self, imageName): pass

    def createRoundRectPixmap(self, color): pass

    def createTextLabel(self, text): pass

    def enterEvent(self, e): pass

    def fadeBackground(self): pass

    def isHighlighted(self): pass

    def leaveEvent(self, e): pass

    def leftMousePress(self): pass

    def mousePressEvent(self, e): pass

    def mouseReleaseEvent(self, e): pass

    def redrawPixmap(self): pass

    def setBackgroundColor(self, color): pass

    def setConstantBackground(self, hasConst): pass

    def setHighlighted(self, highlighted): pass

    def setImage(self, image): pass

    def setImageFromPixmap(self, pixmap): pass

    def setText(self, text): pass

    clicked = None

    rightClicked = None

    staticMetaObject = None


class DraggableListWidget(QtWidgets.QListWidget):
    def __init__(self, parent='None'): pass

    def dragEnterEvent(self, event): pass

    def dragMoveEvent(self, event): pass

    def paintEvent(self, e): pass

    def resizeEvent(self, e): pass

    staticMetaObject = None


class SingleNodeInputWidget(QtWidgets.QWidget):
    def __init__(self, acceptableNode="''", createCallback='None', acceptableFunc='None'): pass

    def acceptNode(self, name): pass

    def createTrianglePixmap(self): pass

    def currentNode(self): pass

    def dragEnterEvent(self, e): pass

    def dragLeaveEvent(self, e): pass

    def dragMoveEvent(self, e): pass

    def dropEvent(self, e): pass

    def getNodeType(self, node): pass

    def paintEvent(self, e): pass

    def selectorFinished(self, result): pass

    def setIcon(self, name): pass

    def setNode(self, node='None'): pass

    def showSelector(self): pass

    accepted = None

    staticMetaObject = None


class HWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs): pass

    staticMetaObject = None


class VWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs): pass

    staticMetaObject = None


class FrameBar(QtWidgets.QWidget):
    def __init__(self, parent='None'): pass

    def paintEvent(self, e): pass

    staticMetaObject = None


import PySide2.QtCore as QtCore


class TextFieldWrapper(QtCore.QObject):
    def __init__(self, lineEdit): pass

    def setText(self, text): pass

    def text(self): pass

    staticMetaObject = None

    textEdited = None


class ListButtonWidget(QtWidgets.QListWidget):
    """
    Data delegate must implement these methods:
        def dropEvent(self, event):
            pass
        def setupTreeMenu(self, treeMenu, position):
            pass
        def selectionChanged(self):
            pass
        def buttonPressed(self, index, buttonName):
            pass
        def doubleClick(self, index, buttonName):
            pass
        def itemTextChangedAtIndex(self, index, oldValue, newValue):
            return newName
    
    Default buttons:
        'dragIndicator', 'textField', 'toggleButton'
    """

    def __init__(self, parent='None'): pass

    def createNewLayer(self): pass

    def dragEnterEvent(self, event): pass

    def dragMoveEvent(self, event): pass

    def dropEvent(self, event): pass

    def getButtonPressed(self, item, x): pass

    def handleNormalSelection(self, index): pass

    def handleRightClickSelection(self, index): pass

    def itemTextChangedAtIndex(self, index, oldValue, newValue): pass

    def mouseDoubleClickEvent(self, event): pass

    def mouseMoveEvent(self, event): pass

    def mousePressEvent(self, event): pass

    def mouseReleaseEvent(self, event): pass

    def openTreeMenu(self, position): pass

    def paintEvent(self, e): pass

    def selectionChanged(self, item1, item2): pass

    def setLabelColor(self, color): pass

    staticMetaObject = None


class NodeSelector(QtWidgets.QDialog):
    def __init__(self, parent='None', acceptableNode="''", createCallback='None', acceptableFunc='None'): pass

    def focusOutEvent(self, event): pass

    def getIcon(self, name): pass

    def getNodeType(self, node): pass

    def rowClicked(self, row): pass

    clicked = None

    staticMetaObject = None


class DropWindow(QtWidgets.QDialog):
    def __init__(self, label="''", title="''", accepts='None', ui='None', minWidth='450', **kw): pass

    def closeEvent(self, e): pass

    def eventFilter(self, widget, event): pass

    def flashRedIndicator(self): pass

    def updateCustomUI(self): pass

    @staticmethod
    def getDrop(label="''", callback='None', title="''", accepts='None', ui='None', minWidth='450'): pass

    dropped = None

    instance = None

    staticMetaObject = None


class FrameWidget(QtWidgets.QWidget):
    def __init__(self, text, expanded='False', parent='None'): pass

    def addWidget(self, widget): pass

    def createCollapsedIcon(self): pass

    def createExpandedIcon(self): pass

    def mousePressEvent(self, e): pass

    def switchMode(self): pass

    def updateArrow(self): pass

    def updateVisibility(self): pass

    staticMetaObject = None

    switched = None


class ListButtonDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent='None'): pass

    def applyCellMargins(self, index): pass

    def createEditor(self, parent, option, index):
        """
        Creates the double-click editor for renaming render setup entries. The override entry is left aligned.
        """
        pass

    def paint(self, painter, option, index):
        """
        Main entry point of drawing the cell
        """
        pass

    def setEditorData(self, editor, index): pass

    def setModelData(self, editor, model, index):
        """
        Sets the model data which will trigger the node renaming script to run in Maya
        """
        pass

    def sizeHint(self, option, index): pass

    def updateEditorGeometry(self, editor, option, index):
        """
        Defines the rectangle of the QLineEdit used to edit the name of the node.
        """
        pass

    staticMetaObject = None


class NodeListWidget(QtWidgets.QListWidget):
    def __init__(self, parent='None'): pass

    def mouseMoveEvent(self, e): pass

    def mousePressEvent(self, e): pass

    clicked = None

    staticMetaObject = None


class ListButtonBtn:
    def __init__(self, icons, name, highlightable='True'): pass


class DropWindowListWidget(DraggableListWidget):
    def __init__(self, *args, **wargs): pass

    def event(self, e): pass

    def onBackgroundPropertyChange(self): pass

    staticMetaObject = None


def applyMargins(margins, rect):
    """
    margins: list[4]
    rect: qt.QRect
    """
    pass


def wrapInstance(*args, **kwargs): pass


def getIconFromName(name): pass


def unwrapInstance(*args, **kwargs): pass


def setWidgetWindowColor(widget, color): pass


def getWidgetOfClassFromLayout(layout, widgetClassName): pass


def setHLayout(widget, spacing='0', *margins): pass


def getIconSuffix(): pass


def widgetWithLayout(typ="'V'", spacing='0', *margins): pass


def setVLayout(widget, spacing='0', *margins): pass


def createPixmap(imageName): pass


def setWidgetBackgroundColor(widget, color): pass


def dpiScale(value): pass


def pix(value='1'): pass


def getPixmap(name): pass


def highlightPixmap(pixmap): pass


def registerQtObject(obj): pass


def configureRightClickMenu(widget, callback): pass


def centerOnScreen(dialog): pass


def setWidgetBaseColor(widget, color): pass


def dpi(value='1'): pass


def scalePixmap(pixmap, width, height): pass


def loadFluxIcons(): pass


def configureDragDrop(widget): pass


maya_scale = 2.0

fluxIcons = {}

qt_dpi = 1

pixmap_cache = {}
