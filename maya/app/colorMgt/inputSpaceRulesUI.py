if False:
    from typing import Dict, List, Tuple, Union, Optional


class Rule(object):
    def __init__(self, name): pass

    def canDelete(self): pass

    __dict__ = None

    __weakref__ = None


class ChainRule(Rule):
    def __init__(self, name="''"): pass

    def appendRule(self, rule): pass

    def createHandlerRuleUI(self): pass

    def createUI(self): pass

    def indexToPosition(self, index): pass

    def isReadOnly(self): pass

    def onAddRule(self, *args): pass

    def onDeleteRule(self, *args): pass

    def onDown(self, *args): pass

    def onReapply(self, *args): pass

    def onSelect(self, *args): pass

    def onUp(self, *args): pass

    def positionToIndex(self, position): pass

    def selectRule(self, position): pass

    def updateHandlerRuleUI(self): pass

    def updateScrollList(self): pass


class OpaqueRule(Rule):
    def __init__(self, name): pass

    def createUI(self): pass


class ColorSpaceRule(Rule):
    def __init__(self, name): pass

    def createColorSpaceMenu(self): pass

    def fileRuleLayout(self, extWidget, patternWidget):
        """
        Shared layout for color space rules.
        """
        pass

    def getColorSpace(self): pass

    def onInputColorSpaceChange(self, *args): pass

    def onRemoveColorSpace(self, *args): pass

    def setColorSpace(self, colorSpace): pass

    def setMenuValidColorSpace(self, valid): pass

    def validateColorSpace(self, colorSpace): pass

    @property
    def colorSpace(self): pass


class FilePathRule(ColorSpaceRule):
    def __init__(self, name): pass

    def canDelete(self): pass

    def createUI(self): pass

    def getExtension(self): pass

    def getPattern(self): pass

    def onExtensionChange(self, *args): pass

    def onPatternChange(self, *args): pass

    def setExtension(self, extension): pass

    def setPattern(self, pattern): pass

    @property
    def extension(self): pass

    @property
    def pattern(self): pass


class DefaultRule(ColorSpaceRule):
    def __init__(self): pass

    def createUI(self): pass


def build(): pass


def nativeMode(): pass


def mayaImageFileExtensions():
    """
    Return the list of image file extensions read by Maya.
    """
    pass


def createUI(): pass


buttonWidth = 60

hSpc = 10

parentForm = ''

red = []

black = []
