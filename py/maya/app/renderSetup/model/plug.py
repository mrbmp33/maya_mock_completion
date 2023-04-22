if False:
    from typing import Dict, List, Tuple, Union, Optional


class Plug(object):
    """
    Helper class to allow seamless value assignment from one plug to another, 
    while correctly handling and abstracting away plug type.
    
    "self.type" returns the type of the plug.
        This is necessary to determine how to read and write the plug.
    "self.value" returns the value of the plug.
    "self.value = otherValue" will set the value of the plug to otherValue.
        This mutator assumes otherValue to be the same type as self.type
    
    "self.overrideType" returns the type of the override that should be created to override this plug.
    """

    def __init__(self, plugOrNode, attrName='None'):
        """
        Constructors:
        Plug(MPlug)
        Plug(string (full plug name))
        Plug(MObject, MObject)
        Plug(MObject, string (attribute name))
        Plug(string (node name), string (attribute name))
        """
        pass

    def __str__(self): pass

    def accepts(self, other):
        """
        Returns true if plug would accept a connection with other plug
        i.e. plug and other plug are type compatible for connection.
        """
        pass

    def acceptsOverrideType(self, typeId): pass

    def applyOverrideType(self, overType): pass

    def attribute(self):
        """
        Returns the attribute (MFnAttribute) of the plug
        """
        pass

    def availableOverrides(self): pass

    def children(self): pass

    def cloneAttribute(self, nodeObj, longName, shortName, undoable='1'):
        """
        Creates a new attribute on a node by cloning this plug's attribute.
        Undoable by default
        """
        pass

    def copyValue(self, other):
        """
        Sets the value of plug 'self' to the value contained in plug 'other' 
        The 'other' plug can be either a Plug or a MPlug.
        """
        pass

    def createAttributeFrom(self, nodeObj, longName, shortName, limits='None'):
        """
        Creates a new attribute on a node by cloning this plug's attribute. 
        
        Note: None for a limit value means that there is no limit. For example,
              if min is None, it means that there is no minimum limit.
        """
        pass

    def getAttributeLimits(self):
        """
        Get the limits of the plug
        """
        pass

    def isOvrSupported(self): pass

    def localizedTypeString(self): pass

    def node(self): pass

    def overrideType(self, overType): pass

    def parent(self): pass

    def setAttributeLimits(self, limits): pass

    @staticmethod
    def createAttribute(nodeObj, longName, shortName, dict, undoable='1'):
        """
        Create a new attribute on a node using the given names and properties dictionary. 
        Returns an MObject to the new attribute. By default, it uses the command 
        addDynamicAttribute (if it's not undoable, use MFnDependencyNode.addAttribute()) 
        to add the returned object as a new dynamic attribute on a node.
        """
        pass

    @staticmethod
    def getNames(plugName): pass

    @property
    def attributeName(self): pass

    @property
    def hasLimits(self):
        """
        Returns true if the type supports min/max limits.
        """
        pass

    @property
    def isConnectable(self):
        """
        Returns true if plug's input can be connected.
        """
        pass

    @property
    def isKeyable(self):
        """
        Returns true if the plug has the keyable property.
        
        Note that a plug that does not have this property can still have
        key frames set on it.  As per Maya documentation, a keyable
        attribute means that 'if any of the animation commands (setKeyframe,
        cutKey, copyKey,..) are issued without explicitly specifying any
        attributes with the -at/attribute flag, then the command will
        operate on all keyable attributes of the specified objects'.
        
        The autoKeyframe functionality also uses the keyable property to
        determine if key frames should be set.
        """
        pass

    @property
    def isLocked(self):
        """
        Returns true is plug or plug's children (compound) are locked.
        """
        pass

    @property
    def isNumeric(self): pass

    @property
    def isUnit(self): pass

    @property
    def isValid(self): pass

    @property
    def isVector(self):
        """
        Returns true if the type is a vector type.
        """
        pass

    @property
    def name(self): pass

    @property
    def nodeName(self): pass

    @property
    def plug(self): pass

    @property
    def type(self): pass

    @property
    def uiUnitValue(self): pass

    @property
    def value(self): pass

    __dict__ = None

    __weakref__ = None

    kAngle = 12

    kArray = 14

    kBool = 5

    kByte = 4

    kColor = 6

    kDistance = 13

    kDouble = 2

    kEnum = 7

    kFilename = 15

    kFloat = 1

    kInt = 3

    kInvalid = 0

    kLast = 16

    kMessage = 10

    kObject = 9

    kString = 8

    kTime = 11


class UnlockedGuard:
    """
    Safe way to unlock a plug in a block. 
    Lock state will be recovered back on exit of the block (for ancestors and children plugs).
    Example:
        with UnlockedGuard(aLockedPlug):
            someActionsOnThePlug()
    """

    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, plg): pass


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


class AddDynamicAttribute(_MPxCommand):
    """
    Undoable command to add an attribute to a node
    
    This command is a private implementation detail of this module and should
    not be called otherwise.
    """

    def __init__(self, node, attribute, mdgModifier): pass

    def doIt(self, args): pass

    def isUndoable(self): pass

    def redoIt(self): pass

    def undoIt(self): pass

    @staticmethod
    def creator(): pass

    @staticmethod
    def execute(node, attribute): pass

    __dict__ = None

    __weakref__ = None

    attribute = None

    kCmdName = 'addDynamicAttribute'

    mdgModifier = None

    node = None


def findPlug(node, attr='None'):
    """
    Return a Plug instance if the MPlug was found, None otherwise.
    """
    pass


def relatives(plg):
    """
    Returns relatives (ancestors, plug itself and descendant) of the given plug in deterministic order.
    Parents are guaranteed to come before children in generator.
    """
    pass


def toUiUnits(type, value): pass


def _createFilenameAttr(longName, shortName): pass


def value(mPlug):
    """
    Convenience function to retrieve the value of an MPlug.
    """
    pass


def isSettable(plug):
    """
    Predicate that returns whether the MPlug argument can be set.
    """
    pass


def toInternalUnits(type, value): pass


kAddAttributePrivate = []

kArityMismatch = []

kNotUndoable = 0

kPlugWithoutLimits = []

kPlugHasNotSettableChild = []

kUnknownType = []

kUndoable = 1

kCompoundTypeStr = []

kPlugHasConnectedParent = []

kVectorTypeStr = []

kUnsupportedAttribute = []

kNotOverridablePlug = []
