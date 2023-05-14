"""
This module provides the override base and concrete classes, as well as
utility functions to operate on overrides.
"""

from maya.app.renderSetup.model.renderSetupPrivate import PostApplyCmd
from collections import namedtuple

if False:
    from typing import Dict, List, Tuple, Union, Optional


class OverridePlugHandle(object):
    """
    Plug class that handles dynamic plug and missing dependencies.
    
    Has functions for finalization, encoding, decoding and handling missing dependencies.
    
    Finalization creates a dynamic attribute based on another plug. It has 3 available modes:
     - kModeClone clones the input plug
     - kModeMultiply will have the same arity as the input plug but has float scalar units
       (can be used to multiply input's plug type by a scalar)
     - kModeOffset clones the input plug but with more flexible min/max, softMin/softMax
       (can be used to offset input's plug type by some value in the same units)
       
    Encode/decode creates/read dictionary of attributes that defines the plug attributes.
    
    Handles missing dependency:
     If the plug is decoded and can't find the source plug it's supposed to connect to, then
     it has a missing dependency. It creates a dynamic string attribute containing the name of the
     missing dependency (this allows the "missing dependency" state to persist on file new) and it 
     starts listening to scene changes to find the missing dependency and connect to it if it's created.
    """

    def __init__(self, ovr, longName, shortName, mode='0'): pass

    def decode(self, dict): pass

    def encode(self, dict): pass

    def finalize(self, plg): pass

    def getMissingDependency(self): pass

    def getPlug(self):
        """
        Return the Plug object (plug.py). (this is not a MPlug)
        """
        pass

    def getSource(self): pass

    def hasMissingDependency(self): pass

    def isFinalized(self): pass

    def isValid(self): pass

    def name(self): pass

    def node(self): pass

    def setMissingDependency(self, source): pass

    def setSource(self, source): pass

    def update(self): pass

    @property
    def attr(self): pass

    @property
    def attrDependency(self): pass

    __dict__ = None

    __weakref__ = None

    kModeClone = 0

    kModeMultiply = 2

    kModeOffset = 1


_Property = namedtuple('Property', ('name', 'encode', 'decode'))

from . import childNode


class Override(childNode.TreeOrderedItem, childNode.ChildNode):
    """
    Override node base class.
    
    An override represents a non-destructive change to a scene property
    that can be reverted or disabled.  Render setup uses overrides to describe
    changes that apply in a single render layer, and are unapplied when
    switching to another render layer.  When working within a render layer, an
    override can be preserved but disabled, to remove its effect.
    
    The override node base class cannot be directly created in Maya.  It is
    derived from the ListItem base class, so that overrides can be inserted
    in a list.
    """

    def attrValuePlugName(self): pass

    def attributeName(self): pass

    def compute(self, plug, dataBlock): pass

    def enabledChanged(self): pass

    def getApplyOverrides(self):
        """
        Return the list of apply override nodes that correspond to this override.
        """
        pass

    def getRenderLayer(self): pass

    def hasApplyOverrides(self): pass

    def isAbstractClass(self): pass

    def isAcceptableChild(self, model):
        """
        Check if the model could be a child
        """
        pass

    def isApplied(self): pass

    def isEnabled(self): pass

    def isLocalRender(self, dataBlock='None'): pass

    def isSelfEnabled(self, dataBlock='None'): pass

    def isValid(self): pass

    def itemChangedRecursive(self): pass

    def setAttributeName(self, attributeName):
        """
        Set the name of the attribute to be overridden.
        """
        pass

    def setLocalRender(self, value): pass

    def setSelfEnabled(self, value): pass

    def typeId(self): pass

    def typeName(self): pass

    @classmethod
    def creator(cls):
        """
        # Awkwardly, abstract base classes seem to need a creator method.
        """
        pass

    @staticmethod
    def initializer(): pass

    attrLocal = None

    attrName = None

    enabled = None

    kTypeId = None

    kTypeName = 'override'

    layerNumIsolatedChildren = None

    parentEnabled = None

    selfEnabled = None


class UniqueOverride(object):
    """
    Mixin class for override that applies to a unique node. This override 
    unconditionnaly applies to the node it was finalized on (if it exists).
    It doesn't care about the collection's content.
    """

    def finalize(*args, **kwargs): pass

    def setTargetNodeName(*args, **kwargs): pass

    def targetNodeName(self, dataBlock='None'): pass

    @classmethod
    def addTargetAttribute(cls): pass

    __dict__ = None

    __weakref__ = None

    kTargetNodeName = None


class _MPxCommand(object):
    """
    Base class for custom commands.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def doIt(*args, **kwargs):
        """
        Called by Maya to execute the command.
        """
        pass

    def hasSyntax(*args, **kwargs):
        """
        Called by Maya to determine if the command provides an MSyntax object describing its syntax.
        """
        pass

    def isUndoable(*args, **kwargs):
        """
        Called by Maya to determine if the command supports undo.
        """
        pass

    def redoIt(*args, **kwargs):
        """
        Called by Maya to redo a previously undone command.
        """
        pass

    def syntax(*args, **kwargs):
        """
        Returns the command's MSyntax object, if it has one.
        """
        pass

    def undoIt(*args, **kwargs):
        """
        Called by Maya to undo a previously executed command.
        """
        pass

    @staticmethod
    def appendToResult(*args, **kwargs):
        """
        Append a value to the result to be returned by the command.
        """
        pass

    @staticmethod
    def clearResult(*args, **kwargs):
        """
        Clears the command's result.
        """
        pass

    @staticmethod
    def currentResult(*args, **kwargs):
        """
        Returns the command's current result.
        """
        pass

    @staticmethod
    def currentResultType(*args, **kwargs):
        """
        Returns the type of the current result.
        """
        pass

    @staticmethod
    def displayError(*args, **kwargs):
        """
        Display an error message.
        """
        pass

    @staticmethod
    def displayInfo(*args, **kwargs):
        """
        Display an informational message.
        """
        pass

    @staticmethod
    def displayWarning(*args, **kwargs):
        """
        Display a warning message.
        """
        pass

    @staticmethod
    def isCurrentResultArray(*args, **kwargs):
        """
        Returns true if the command's current result is an array of values.
        """
        pass

    @staticmethod
    def setResult(*args, **kwargs):
        """
        Set the value of the result to be returned by the command.
        """
        pass

    __new__ = None

    commandString = None

    historyOn = None

    kDouble = 1

    kLong = 0

    kNoArg = 3

    kString = 2


class LeafClass(object):
    """
    To be used by leaf classes only
    """

    def isAbstractClass(self): pass

    __dict__ = None

    __weakref__ = None


class ValueOverride(Override):
    """
    Override node base class for all value overrides.
    """

    def __init__(self): pass

    def acceptsAttr(*args, **kwargs): pass

    def apply(*args, **kwargs): pass

    def applyInsertOne(self, node, attr, nextOvr='None'): pass

    def getOverridden(self):
        """
        Return the list of nodes being overridden.
        
        The items in the return list are triplets of (MObject, attrName, ovrNext).
        MObject is the object being overridden, attrName is the name of the attribute 
        being overridden and ovrNext is the override node in the position of the next 
        override in the apply override list.
        
        Returns an empty list if no attribute is being overridden.
        """
        pass

    def overridesConnections(self): pass

    def postApply(*args, **kwargs): pass

    def reapply(*args, **kwargs): pass

    def unapply(*args, **kwargs): pass

    def update(*args, **kwargs): pass

    @staticmethod
    def initializer(): pass

    kTypeId = None

    kTypeName = 'valueOverride'


class Property(_Property):
    """
    Namedtuple to hold what is needed to encode a property (name, encode function, decode function).
    'name' will be the name of the given attribute (MObject).
    """

    @staticmethod
    def __new__(cls, attr, encode, decode): pass

    __dict__ = None


class UnapplyCmd(_MPxCommand):
    """
    Command to unapply and reapply an override.
    
    This command is a private implementation detail of this module and should
    not be called otherwise.
    """

    def __init__(self, override): pass

    def doIt(self, args): pass

    def isUndoable(self): pass

    def redoIt(*args, **kwargs): pass

    def undoIt(*args, **kwargs): pass

    @staticmethod
    def creator(): pass

    @staticmethod
    def execute(override):
        """
        Unapply the override, and add an entry to the undo queue.
        """
        pass

    __dict__ = None

    __weakref__ = None

    kCmdName = 'unapplyOverride'

    override = None


class AbsOverride(LeafClass, ValueOverride):
    """
    Absolute override node.
    
    This concrete override node type implements an absolute override
    (replace value) for an attribute.
    """

    def __init__(self): pass

    def compute(self, plg, dataBlock): pass

    def finalize(*args, **kwargs): pass

    def getAttrValue(self):
        """
        Returns the value of the override.
        
        This value is always in internal units.  See OpenMaya documentation for
        MAngle, MDistance, and MTime.  plug.toUiUnits and plug.toInternalUnits
        can be used to convert between units.
        """
        pass

    def hasMissingDependencies(self): pass

    def isFinalized(self): pass

    def isValid(self): pass

    def postConstructor(self): pass

    def setAttrValue(self, value):
        """
        Sets the value of the override.
        
        This value must be in internal units.  See OpenMaya documentation for
        MAngle, MDistance, and MTime.  plug.toUiUnits and plug.toInternalUnits
        can be used to convert between units.
        """
        pass

    def status(self):
        """
        Returns a problem string if there is a problem with override or None otherwise.
        """
        pass

    @staticmethod
    def initializer(): pass

    kAttrValueLong = 'attrValue'

    kAttrValueShort = 'atv'

    kTypeId = None

    kTypeName = 'absOverride'


class RelOverride(LeafClass, ValueOverride):
    """
    Relative override node to transform a attribute using:
    
    newValue = originalValue * multiply + offset
    
    This concrete override node type implements a relative override
    for a float scalar attribute.
    """

    def __init__(self): pass

    def compute(self, plug, dataBlock): pass

    def finalize(*args, **kwargs): pass

    def getMultiply(self): pass

    def getOffset(self): pass

    def isFinalized(self): pass

    def isValid(self): pass

    def multiplyPlugName(self): pass

    def offsetPlugName(self): pass

    def postConstructor(self): pass

    def setMultiply(self, value): pass

    def setOffset(self, value): pass

    def status(self):
        """
        Returns a problem string if there is a problem with override or None otherwise.
        """
        pass

    @staticmethod
    def initializer(): pass

    kMultiplyLong = 'multiply'

    kMultiplyShort = 'mul'

    kOffsetLong = 'offset'

    kOffsetShort = 'ofs'

    kTypeId = None

    kTypeName = 'relOverride'


class RelUniqueOverride(UniqueOverride, RelOverride):
    @staticmethod
    def initializer(): pass

    kTargetNodeName = None

    kTypeId = None

    kTypeName = 'relUniqueOverride'


class AbsUniqueOverride(UniqueOverride, AbsOverride):
    @staticmethod
    def initializer(): pass

    kTargetNodeName = None

    kTypeId = None

    kTypeName = 'absUniqueOverride'


def create(*args, **kwargs): pass


def fillVector(value, dimension):
    """
    Return a list of specified dimension initialized with value.
    
    If dimension is 0, return the argument value as a scalar.
    """
    pass


def attributeToPlug(f):
    """
    Decorator that adds a node name to an attribute name, if not present. (attribute => plug)
    Using template node name of parent collection's selector.
    """
    pass


def delete(*args, **kwargs): pass


def valid(f):
    """
    Decorator that calls the decorated method if and only if self.isValid() evaluates to True.
    """
    pass


def finalizationChanged(f):
    """
    Decorator for functions that may change the finalization of an override (decode, finalize).
    This will ensure that if the layer in which this override lives is visible, then the override
    should be unapplied and reapplied with the new finalization.
    """
    pass


kMissingDependencies = []

kUnfinalized = []

kUnconnectableAttr = []

kUnapplyCmdPrivate = []
