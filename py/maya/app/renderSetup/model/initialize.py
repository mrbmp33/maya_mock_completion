from maya.app.renderSetup.model.overrideUtils import getAllOverrideClasses
from maya.app.renderSetup.model.selector import SimpleSelector
from maya.app.renderSetup.model.selector import Selector
from maya.app.renderSetup.model.collection import getAllCollectionClasses
from maya.app.renderSetup.model.applyOverride import getAllApplyOverrideClasses
from maya.app.renderSetup.model.renderSetup import RenderSetup as nodeType
from maya.app.renderSetup.model.renderLayer import RenderLayer
from maya.app.renderSetup.model.selector import LightsCollectionSelector
from maya.app.renderSetup.model.selector import BasicSelector

if False:
    from typing import Dict, List, Tuple, Union, Optional


def setVisibilityNodes(val, nodeTypeNamesList):
    """
    Set the visibility of the nodes in nodeTypeNamesList to val (either
    True or False). This affects the visibility of those nodes in editors.
    """
    pass


def initialize(mplugin): pass


def uninitialize(mplugin): pass


nodeDragAndDropBehaviors = []

renderSetupNodeNamesToShowInOutliner = []

nodeTypes = []

syntaxCommands = []

commands = []
