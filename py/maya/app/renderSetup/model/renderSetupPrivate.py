if False:
    from typing import Dict, List, Tuple, Union, Optional


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


class PostApplyCmd(_MPxCommand):
    """
    Command to apply collection or override when the layer is already visible.
    This should apply the overrides in the right order, i.e. apply override nodes
    must be inserted at the right position in the apply chain.
    
    This command is a private implementation detail of this module and should
    not be called otherwise.
    """

    def __init__(self, applicable): pass

    def doIt(self, args): pass

    def isUndoable(self): pass

    def redoIt(*args, **kwargs): pass

    def undoIt(*args, **kwargs): pass

    @classmethod
    def creator(cls): pass

    @classmethod
    def execute(cls, applicable):
        """
        Applies an applicable (collection/override) after the layer was already set visible.
        """
        pass

    __dict__ = None

    __weakref__ = None

    applicable = None

    kCmdName = 'renderSetupPostApply'


class SwitchVisibleRenderLayerCmd(_MPxCommand):
    """
    Command to switch the visible layer.
    
    This command is a private implementation detail of this module and should
    not be called otherwise.
    """

    def __init__(self, newLayer): pass

    def doIt(self, args): pass

    def isUndoable(self): pass

    def redoIt(self): pass

    def undoIt(self): pass

    @staticmethod
    def creator(): pass

    @staticmethod
    def execute(newLayer):
        """
        Switch to given RenderLayer
        """
        pass

    __dict__ = None

    __weakref__ = None

    kCmdName = 'renderSetupSwitchVisibleRenderLayer'

    newLayer = None


def moveModel(modelToMove, destinationModel, destinationPosition):
    """
    Helper method to move a model from a location to antoher location
    """
    pass


def _renderSetupInstance(): pass


kSwitchVisibleRenderLayer = []

kCmdPrivate = []

logger = None
