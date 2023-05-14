from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin as dockableMixin
from PySide2.QtCore import Slot

if False:
    from typing import Dict, List, Tuple, Union, Optional


class csv_writer:
    __init__ = None

    def writerow(self, row): pass

    def writerows(self, rows): pass


class csv_reader:
    __init__ = None

    def __iter__(self): pass

    def next(self): pass


class UTF8Wrapper:
    def __init__(self, f, encoding): pass

    def __iter__(self): pass

    def next(self): pass


class MCallbackIdWrapper(object):
    """
    Wrapper class to handle cleaning up of MCallbackIds from registered MMessage
    """

    def __del__(self): pass

    def __init__(self, callbackId): pass

    def __repr__(self): pass

    __dict__ = None

    __weakref__ = None


def getReadFileName(message, fileFilter="''"): pass


def importJSONFile(): pass


def getStringResource(indentifier, key): pass


def getFluxString(key): pass


def unwrapInstance(*args, **kwargs): pass


def endProgressBar(): pass


def getColourFromLabel(label): pass


def stepProgressBar(amount='1'): pass


def getQtWidgetAtPos(x, y): pass


def getWriteFileName(message, fileFilter="''"): pass


def getFuncFullName(func): pass


def wrapInstance(*args, **kwargs): pass


def colorLabel(identifier): pass


def createColorIcon(colorName='None', qcolor='None', x='100', y='100'): pass


def printCallStack(): pass


def getWidgetNameAtPos(x, y): pass


def applyRotations(rotations, origin): pass


def getDagPathFromName(nodeName): pass


def mayaWindow(): pass


def str_res(name): pass


def getMObjectFromName(nodeName): pass


def getMayaWidget(name): pass


def registerStringResources(identifier, resources): pass


def getPluginStringResource(key): pass


def mayaViewport(): pass


def startProgressBar(message="'Loading...'", length='100'): pass


def allColorLabels(): pass


def loadStringResources(module): pass


def getAttributePlug(name, attr): pass


def exportJSONFile(jsonData): pass


def getLocale(): pass


_color_labels = []

fluxResourcesFolder = r'C:\Apps\3D\Autodesk\Maya2019\Python\lib\site-packages\maya\app\flux\resources'

moduleIdentifier = 'maya.app.flux.utils'
