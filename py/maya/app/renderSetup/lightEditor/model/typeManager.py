if False:
    from typing import Dict, List, Tuple, Union, Optional


def pluginLights(): pass


def getAllAttributes(): pass


def isValidLightShapeObject(mayaObj): pass


def isValidLightTransformObject(mayaObj): pass


def _getAttributesFromViewTemplate(nodeType, viewName): pass


def isLight(mayaObj): pass


def lights(): pass


def excludeFromUI(nodeType): pass


def findLightShapeObject(transformObj): pass


def _getDataTypeFromTemplateType(typeName): pass


def isLightEditorItem(mayaObj): pass


def getIcon(lightType): pass


def getAttributesForLightType(lightType): pass


def mayaLights(): pass


def getCreateCmd(lightType): pass


def _isPluginLight(nodeType): pass


def rebuild(): pass


def findAllLightTransforms(): pass


def findLightTransformObject(shapeObj): pass


mayaLightTypes = []

pluginLightTypes = []

uiExcludedLightTypes = []

lightTypes = []

attributesForLightType = {}

allLightAttributes = {}

lightConstructionData = {}

dataTypeConversionTable = {}
