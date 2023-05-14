from maya.app.flux.ae.Template import *

from maya.app.flux.ae.Custom import Custom
from maya.app.flux.ui.core import pix
from PySide2.QtCore import Slot

if False:
    from typing import Dict, List, Tuple, Union, Optional


class MyCustom(Custom):
    def addShellDynamics(self): pass

    def alignChanged(self, *args): pass

    def alignClicked(self, index): pass

    def animationTabChanged(self, visible): pass

    def backBevelEnabledChanged(self): pass

    def bevelStyleChanged(self): pass

    def buildUI(self, nodeName): pass

    def connectToMash(self, name): pass

    def contextChanged(self): pass

    def createAndConnectToMash(self): pass

    def createCurveClicked(self): pass

    def createCustomWidgets(self): pass

    def createFalloffCurve(self, attr): pass

    def createLocalPivotBtn(self, axis): pass

    def deformableTypeChanged(self): pass

    def disableAllBevels(self): pass

    def editFalloffCurve(self, attr): pass

    def enableBevelClicked(self): pass

    def enableBevelStyle(self): pass

    def enableDisableBevels(self): pass

    def extrudeEnableChanged(self): pass

    def fixAnimLegacyConnections(self): pass

    def fontChanged(self, index='None'): pass

    def fontStyleChanged(self, index='None'): pass

    def generatorChanged(self): pass

    def getAcceptableNodesForMASH(self): pass

    def getAnimationNode(self): pass

    def getExtrudeNode(self):
        """
        # Utilities
        """
        pass

    def getMashConnection(self): pass

    def getRemeshNode(self): pass

    def getShader(self, index): pass

    def initFontDictionary(self): pass

    def isAnimConnLegacy(self): pass

    def isBevelEnabled(self): pass

    def loadStyleList(self): pass

    def manipReplacementClicked(self): pass

    def materialJoinClicked(self): pass

    def materialSplitClicked(self): pass

    def nodeChanged(self): pass

    def pivotLocationClicked(self, axis): pass

    def pivotLocationMenuClicked(self, cmd): pass

    def setupNavigationControls(self, navigations): pass

    def setupWritingSystems(self): pass

    def shellAnimOptionChanged(self, index): pass

    def shellAnimationClicked(self): pass

    def showLocalPivotMenu(self, axis, rpChecked, spChecked): pass

    def strRes(self, name): pass

    def stringResourceFunction(self, name): pass

    def switchBackBevel(self): pass

    def switchFrontBevel(self): pass

    def textChanged(self): pass

    def updateAnimateEnabled(self): pass

    def updateBevelVisibility(self): pass

    def updateDecimalPlaces(self): pass

    def updateFont(self): pass

    def updateFontStyle(self): pass

    def updateFontWritingSystem(self): pass

    def updateMASHShortcuts(self): pass

    def updateMaterialSplitBtn(self): pass

    def updateShellAnimOption(self): pass

    def updateTextValues(self): pass

    def updateWritingSystem(self): pass

    def writingSystemChanged(self, index='None'): pass

    staticMetaObject = None


class AEtypeTemplate(Template):
    def buildUI(self, nodeName): pass


def EscapedToUni(str): pass


def wrapInstance(*args, **kwargs): pass


def getShaderFromObject(mesh):
    """
    #get the shader attribute attached to an object
    #this and the next function are VERY similar, but they go about their task in different ways - which only work in different situations.
    """
    pass


def unwrapInstance(*args, **kwargs): pass


def getShaderFromArray(GrpMessageConections):
    """
    #given a list of nodes, find the shading engine, and it's material
    """
    pass


def UniToEscaped(str): pass


def ByteToHex(byteStr):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    pass


def getVectorShadingGroups(mesh, extrudeNode):
    """
    #given the group nodes, get the associated materials
    """
    pass


def getShadingGroupsFromObject(mesh):
    """
    #get the shaders attached to an object
    """
    pass


def str_res(name): pass


def joinTypeMaterials(meshShape, typeNode, shaderType): pass


def HexToUni(hexStr): pass


def splitTypeMaterials(extrudeNode, meshShape, typeNode, shaderType):
    """
    #assign materials to the type tool
    """
    pass


def HexToByte(hexStr):
    """
    Convert a string hex byte values into a byte string. The Hex Byte values may
    or may not be space separated.
    """
    pass


def getCurrentCtxName(): pass
