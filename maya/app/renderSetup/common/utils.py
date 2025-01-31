if False:
    from typing import Dict, List, Tuple, Union, Optional


class ReportableException(Exception):
    def __init__(self, text): pass

    def __str__(self): pass

    @property
    def text(self): pass

    __weakref__ = None


class SettingContextManager:
    """
    For use with the Render Setup Options menu tests.
    Store a cached version of the option var and environment variable for
    the corresponding Setting. This is used in the exit method to restore
    the corresponding values to both those variables, since we might have
    modified them during the called functions for testing purposes.
    """

    def __enter__(self): pass

    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def __init__(self, classOfSetting):
        """
        #This is callable on any render setup option menu settings.
        """
        pass


class SingletonMetaClass(type):
    """
    Setting this class as a class' metaclass allows it to become
    a Singleton, meaning that at most one instance of that class may
    exist at any given time. Acts as a class-factory.
    """

    def __call__(cls, *args, **kwargs): pass

    classInstances = {}


def removeDuplicates(seq):
    """
    Removes all duplicated elements from a list.
    Note that order is not preserved.
    """
    pass


def nodeToShortName(node):
    """
    Returns the minimum name string necessary to uniquely identify the node.
    """
    pass


def getSubClasses(classType): pass


def isNodeInstance(node, nodeType): pass


def _selectPlug(name): pass


def nodeToLongName(node):
    """
    Returns the full name of the node, 
    i.e. the absolute path for dag nodes and name for dependency (non-dag) nodes.
    """
    pass


def settingDecorator(classOfSetting):
    """
    Use the setting's context manager.
    This ensures that the correct values are restored to the environment
    and option variables after calling function f.
    """
    pass


def findPlug(node, attr):
    """
    Return the MPlug corresponding to attr on argument node or None if not found.
    The node argument can be an MObject or a node string name.
    The attr argument can be an MObject or a attr string name.
    Raises RuntimeError if plug is ambiguous.
    """
    pass


def findRecursivelyInEncodedProperties(d, searched): pass


def nameToDagPath(name):
    """
    Returns the MDagPath matching given name or None if not found.
    Raises RuntimeError if name is ambiguous.
    """
    pass


def echoSelect(*args, **kwargs):
    """
    Calls 'select' command with given args, then prints the obtained selection.
    """
    pass


def nameToPlug(name):
    """
    Returns the MPlug matching given name or None if not found.
    Raises RuntimeError if name is ambiguous.
    """
    pass


def nameToNode(name):
    """
    Returns the MObject matching given name or None if not found.
    Raises RuntimeError if name is ambiguous.
    """
    pass


kAmbiguousName = []

kNameToNodeTypeMismatch = []
