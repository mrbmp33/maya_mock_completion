if False:
    from typing import Dict, List, Tuple, Union, Optional


class LocalOverrideGuard(object):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, newEnabled): pass

    __dict__ = None

    __weakref__ = None


class ExportListener(object):
    """
    This instance listen for export callbacks (before/after).
    Ensures that all calls to ov.isEnabled() for every applied local override
    will return false during export time.
    """

    def __init__(self): pass

    def isExporting(self): pass

    @staticmethod
    def deleteInstance(): pass

    @staticmethod
    def instance(): pass

    __dict__ = None

    __weakref__ = None


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


class RenderSetupLocalOverrideCmd(_MPxCommand):
    def doIt(self, args): pass

    def isUndoable(self): pass

    @staticmethod
    def createSyntax(): pass

    @staticmethod
    def creator(): pass

    __dict__ = None

    __weakref__ = None

    kCmdName = 'renderSetupLocalOverride'

    kStateFlag = '-st'

    kStateFlagLong = '-state'


def _setLocalOverrideEnabled(newEnabled): pass


def _toggle(ovrs): pass


def enabled(): pass


def localOverrideEnabled(newEnabled): pass


_localOverrideEnabled = True
