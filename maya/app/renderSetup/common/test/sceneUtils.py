if False:
    from typing import Dict, List, Tuple, Union, Optional


class ColorConstants(object):
    def __init__(self): pass

    BLACK = ()

    BLUE = ()

    GREEN = ()

    PURPLE = ()

    RED = ()

    WHITE = ()

    YELLOW = ()

    __dict__ = None

    __weakref__ = None


def setColor(attr, color): pass


def getShader(shapeName): pass


def assignMaterial(shapeName, shadingGroupName): pass


def testShapeColor(shapeName, color): pass


def createShadingGroup(color):
    """
    Create a shading group connected to a surface shader of the given color.
    Return the names of both the shading group and its associated shader.
    """
    pass


def findShadingEngine(connections): pass


def findComplementShadingGroup(shapeName): pass


def findShadingGroup(shapeName): pass


def createShader(shaderType):
    """
    Create a shader of the given type
    """
    pass


def findSurfaceShader(sgName): pass


def tmpSubDirName(dir, subDir):
    """
    Create a unique sub directory
    """
    pass


def createBasicRenderSetup():
    """
    Create a basic render setup
    """
    pass


def getShape(transform):
    """
    Return the shape of the argument transform.
    """
    pass
