"""
This module monitors file loads (including imports and reference load) and 
    displays warning messages if it discovers that new loaded files are not 
    compatible with the current renderSetup mode
    
    Implementation details:
    In order to determine if the loaded file is compatible with the current Maya state
    we first determine the type the loaded file based on its content. Then depending 
    on the current Maya RenderSetup mode error messages are displayed if incompatibilities
    are identified
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


class _FileLoadMonitor(object):
    """
    Class that counts the types of nodes that are to be watched and/or cleaned
    up as they are added in the scene.
    """

    def __init__(self): pass

    def reset(self): pass

    def start(self): pass

    def stop(self): pass

    __dict__ = None

    __weakref__ = None

    watchedNodeTypes = []


def finalize(): pass


def onReadStart(_): pass


def _getErrorSwitchToRenderLayerIfNeeded(): pass


def onReadEnd(_): pass


def initialize(): pass


def onImportOrReferenceEnd(data): pass


_nodeCounter = _FileLoadMonitor()

kErrorCombiningNewToLegacy = []

kWarningVisibleRenderLayer = []

callbacks = []

kErrorSwitchToRenderLayer = []

kErrorSwitchToRenderSetup = []

kErrorCombiningLegacyToNew = []
