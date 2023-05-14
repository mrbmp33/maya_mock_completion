"""
This module centralizes type IDs for all render setup nodes.  The
range of reserved node type IDs for render setup is 0x58000370 to
0x580003FF, inclusive.  See file Maya/src/Plugins/NodeIdList.txt.
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


def isRenderSetupType(typeID):
    """
    Args:
        typeID: the MTypeId to test
    
    Returns: True if it is in the range of reserved RenderSetup class types otherwise False
    
    Note: Don't include the light editor nodes as RenderSetup node types. 
          We must be able to add overrides on the light editor nodes.
    """
    pass


selector = None

renderSettingsChildCollection = None

valueOverride = None

renderSetup = None

applyRel3FloatsOverride = None

childNode = None

applyAbsFloatOverride = None

lightItemBase = None

applyAbsOverride = None

materialOverride = None

basicSelector = None

connectionOverride = None

listItem = None

renderLayer = None

applyRelFloatOverride = None

applyAbsBoolOverride = None

aovCollection = None

applyAbsIntOverride = None

lightsCollection = None

applyAbs3FloatsOverride = None

simpleSelector = None

lightItem = None

collection = None

absUniqueOverride = None

applyRelIntOverride = None

lightsCollectionSelector = None

absOverride = None

applyAbsStringOverride = None

applyAbsEnumOverride = None

applyRel2FloatsOverride = None

lightGroup = None

upperBound = 1476395941L

applyOverride = None

connectionUniqueOverride = None

relOverride = None

lowerBound = 1476395888L

applyRelOverride = None

override = None

lightEditor = None

applyAbs2FloatsOverride = None

renderSettingsCollection = None

arnoldAOVChildSelector = None

relUniqueOverride = None

applyConnectionOverride = None

lightsChildCollection = None

shaderOverride = None

aovChildCollection = None
