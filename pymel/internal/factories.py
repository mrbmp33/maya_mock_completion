import exceptions

from pymel.internal.docstrings import PyDocstringBuilder as docBuilderCls
from collections import namedtuple as _namedtuple
from pymel.internal.pwarnings import maya_deprecated
from operator import itemgetter
from pymel.internal.pwarnings import deprecated
from pymel.util.conditions import Condition

if False:
    from typing import Dict, List, Tuple, Union, Optional


class Flag(Condition):
    def __init__(self, longName, shortName, truthValue='True'):
        """
        Conditional for evaluating if a given flag is present.
        
        Will also check that the given flag has the required
        truthValue (True, by default). If you don't care
        about the truthValue (ie, you want to have the condition
        evaluate to true as long as the flag is present),
        set truthValue to None.
        """
        pass

    def __str__(self): pass

    def eval(self, kwargs): pass


class ApiUndoItem(object):
    """
    A simple class that reprsents an undo item to be undone or redone.
    """

    def __init__(self, setter, redoArgs, undoArgs, redoKwargs='None', undoKwargs='None'): pass

    def __repr__(self): pass

    def doIt(self): pass

    def redoIt(self): pass

    def undoIt(self): pass


import pymel.util as util


class MetaMayaTypeRegistry(util.metaReadOnlyAttr):
    """
    A metaclass for tracking pymel types.
    """

    @staticmethod
    def __new__(cls, classname, bases, classdict): pass


class MissingInCacheError(exceptions.Exception):
    __weakref__ = None


class VirtualClassManager(object):
    def __init__(self): pass

    def getVirtualClass(self, baseClass, obj, name='None', fnDepend='None'):
        """
        Returns the virtual class to use for the given baseClass + obj, or
        the original baseClass if no virtual class matches.
        """
        pass

    def getVirtualClassInfo(self, vclass):
        """
        Given a virtual class, returns it's registered VirtualClassInfo
        """
        pass

    def register(self, vclass, nameRequired='False', isVirtual="'_isVirtual'", preCreate="'_preCreateVirtual'",
                 create="'_createVirtual'", postCreate="'_postCreateVirtual'"):
        """
        Register a new virtual class
        
        Allows a user to create their own subclasses of leaf PyMEL node classes,
        which are returned by `general.PyNode` and all other pymel commands.
        
        The process is fairly simple:
            1.  Subclass a PyNode class.  Be sure that it is a leaf class,
                meaning that it represents an actual Maya node type and not an
                abstract type higher up in the hierarchy.
            2.  Add an _isVirtual classmethod that accepts two arguments: an
                MObject/MDagPath instance for the current object, and its name.
                It should return True if the current object meets the
                requirements to become the virtual subclass, or else False.
            3.  Add optional _preCreate, _create, and _postCreate methods.  For
                more on these, see below
            4.  Register your subclass by calling
                factories.registerVirtualClass. If the _isVirtual callback
                requires the name of the object, set the keyword argument
                nameRequired to True. The object's name is not always
                immediately available and may take an extra calculation to
                retrieve, so if nameRequired is not set the name argument
                passed to your callback could be None.
        
        The creation of custom nodes may be customized with the use of
        isVirtual, preCreate, create, and postCreate functions; these are
        functions (or classmethods) which are called before / during / after
        creating the node.
        
        The isVirtual method is required - it is the callback used on instances
        of the base (ie, 'real') objects to determine whether they should be
        considered an instance of this virtual class. It's input is an MObject
        and an optional name (if nameRequired is set to True). It should return
        True to indicate that the given object is 'of this class', False
        otherwise. PyMEL code should not be used inside the callback, only API
        and maya.cmds. Keep in mind that once your new type is registered, its
        test will be run every time a node of its parent type is returned as a
        PyMEL node class, so be sure to keep your tests simple and fast.
        
        The preCreate function is called prior to node creation and gives you a
        chance to modify the kwargs dictionary; they are fed the kwargs fed to
        the creation command, and return either 1 or 2 dictionaries; the first
        dictionary is the one actually passed to the creation command; the
        second, if present, is passed to the postCreate command.
        
        The create method can be used to override the 'default' node creation
        command;  it is given the kwargs given on node creation (possibly
        altered by the preCreate), and must return the string name of the
        created node. (...or any another type of object (such as an MObject),
        as long as the postCreate and class.__init__ support it.)
        
        The postCreate function is called after creating the new node, and
        gives you a chance to modify it.  The method is passed the PyNode of
        the newly created node, as well as the second dictionary returned from
        the preCreate function as kwargs (if it was returned). You can use
        PyMEL code here, but you should avoid creating any new nodes.
        
        By default, any method named '_isVirtual', '_preCreateVirtual',
        '_createVirtual', or '_postCreateVirtual' on the class is used; if
        present, these must be classmethods or staticmethods.
        
        Other methods / functions may be used by passing a string or callable
        to the preCreate / postCreate kwargs.  If a string, then the method
        with that name on the class is used; it should be a classmethod or
        staticmethod present at the time it is registered.
        
        The value None may also be passed to any of these args (except isVirtual)
        to signal that no function is to be used for these purposes.
        
        If more than one subclass is registered for a node type, the registered
        callbacks will be run newest to oldest until one returns True. If no
        test returns True, then the standard node class is used. Also, for each
        base node type, if there is already a virtual class registered with the
        same name and module, then it is removed. (This helps alleviate
        registered callbacks from piling up if, for instance, a module is
        reloaded.)
        
        Overriding methods of PyMEL base classes should be performed with care,
        because certain methods are used internally and altering their results
        may cause PyMEL to error or behave unpredictably.  This is particularly
        true for special methods like __setattr__, __getattr__, __setstate__,
        __getstate__, etc.  Some methods are considered too dangerous to modify,
        and registration will fail if the user defines an override for them;
        this set includes __init__, __new__, and __str__.
        
        For a usage example, see examples/customClasses.py
        
        Parameters
        ----------
        nameRequired : `bool`
            True if the _isVirtual callback requires the string name to operate
            on. The object's name is not always immediately avaiable and may
            take an extra calculation to retrieve.
        isVirtual: `str` or callable
            the function to determine whether an MObject is an instance of this
            class; should take an MObject and name, returns True / or False
        preCreate: `str` or callable
            the function used to modify kwargs before being passed to the
            creation function
        create: `str` or callable
            function to use instead of the standard node creation method;
            takes whatever args are given to the cl
        postCreate: `str` or callable
            the function used to modify the PyNode after it is created.
        """
        pass

    def unregister(self, vcls): pass

    INVALID_ATTRS = set()

    __dict__ = None

    __weakref__ = None


class VirtualClassError(exceptions.Exception):
    __weakref__ = None


class ApiUndo(object):
    """
    this is based on a clever prototype that Dean Edmonds posted on python_inside_maya
    awhile back.  it works like this:
    
        - using the API, create a garbage node with an integer attribute,
          lock it and set it not to save with the scene.
        - add an API callback to the node, so that when the special attribute
          is changed, we get a callback
        - the API queue is a list of simple python classes with undoIt and
          redoIt methods.  each time we add a new one to the queue, we increment
          the garbage node's integer attribute using maya.cmds.
        - when maya's undo or redo is called, it triggers the undoing or
          redoing of the garbage node's attribute change (bc we changed it using
          MEL/maya.cmds), which in turn triggers our API callback.  the callback
          runs the undoIt or redoIt method of the class at the index taken from
          the numeric attribute.
    """

    def __init__(self): pass

    def append(self, cmdObj, undoName='None'): pass

    def execute(self, cmdObj, *args): pass

    def flushCallback(self, undoOrRedoAvailable, *args): pass

    def flushUndo(self, *args): pass

    def installUndoStateCallbacks(self): pass

    @staticmethod
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
        pass

    __dict__ = None

    __weakref__ = None


class ApiArgUtil(object):
    def __init__(self, apiClassName, methodName, methodIndex='0'):
        """
        If methodInfo is None, then the methodIndex will be used to lookup
        the methodInfo from apiClassInfo
        
        Parameters
        ----------
        apiClassName : str
        methodName : str
        methodIndex : int
        """
        pass

    def argInfo(self): pass

    def argList(self): pass

    def canBeWrapped(self): pass

    def castInput(self, argName, input):
        """
        Parameters
        ----------
        argName : str
        input : Any
        
        Returns
        -------
        Any
        """
        pass

    def castResult(self, pynodeInstance, result): pass

    def getDefaults(self):
        """
        get a list of defaults
        """
        pass

    def getGetterInfo(self):
        """
        Return an ApiArgUtil for the getter method
        (assumes the current instance is the setter)
        
        Returns
        -------
        Optional[ApiArgUtil]
        """
        pass

    def getInputTypes(self): pass

    def getMethodDocs(self): pass

    def getOutputTypes(self): pass

    def getPrototype(self, className='True', methodName='True', outputs='False', defaults='False'): pass

    def getPymelName(self): pass

    def getReturnType(self): pass

    def getTypeComment(self): pass

    def hasOutput(self): pass

    def inArgs(self): pass

    def isDeprecated(self): pass

    def isStatic(self): pass

    def iterArgs(self, inputs='True', outputs='True', infoKeys='[]'): pass

    def outArgs(self): pass

    @classmethod
    def castInputEnum(cls, apiClassName, enumName, input): pass

    @classmethod
    def castReferenceResult(cls, argtype, outArg): pass

    @staticmethod
    def fromInternalUnits(result, returnType, unit='None'): pass

    @staticmethod
    def initReference(argtype): pass

    @staticmethod
    def isValidEnum(enumTuple): pass

    @staticmethod
    def toInternalUnits(input, unit): pass

    __dict__ = None

    __weakref__ = None


VirtualClassInfo = _namedtuple('VirtualClassInfo',
                               ('vclass', 'parent', 'nameRequired', 'isVirtual', 'preCreate', 'create', 'postCreate'))


class ClassConstant(object):
    """
    Class constant descriptor
    """

    def __delete__(self, instance): pass

    def __get__(self, instance, owner): pass

    def __init__(self, value): pass

    def __repr__(self): pass

    def __set__(self, instance, value): pass

    def __str__(self): pass

    __dict__ = None

    __weakref__ = None


class Callback(object):
    """
    Enables deferred function evaluation with 'baked' arguments.
    Useful where lambdas won't work...
    
    It also ensures that the entire callback will be be represented by one
    undo entry.
    
    Example::
    
        import pymel as pm
        def addRigger(rigger, **kwargs):
            print "adding rigger", rigger
    
        for rigger in riggers:
            pm.menuItem(
                label = "Add " + str(rigger),
                c = Callback(addRigger,rigger,p=1))   # will run: addRigger(rigger,p=1)
    """

    def __call__(self, *args): pass

    def __init__(self, func, *args, **kwargs): pass

    @classmethod
    def formatRecentError(cls, index='0'): pass

    @classmethod
    def logCallbackError(cls, callback, exception='None', trace='None', creationTrace='None'): pass

    @classmethod
    def printRecentError(cls, index='0'): pass

    CallbackErrorLog = None

    MAX_RECENT_ERRORS = 10

    __dict__ = None

    __weakref__ = None

    recentErrors = []


class ApiTypeRegister(object):
    """
    "
    Use this class to register the classes and functions used to wrap api methods.
    
    there are 4 dictionaries of functions maintained by this class:
        - inCast : for casting input arguments to a type that the api method expects
        - outCast: for casting the result of the api method to a type that pymel expects (outCast expect two args (self, obj) )
        - refInit: for initializing types passed by reference or via pointer
        - refCast: for casting the pointers to pymel types after they have been passed to the method
    
    To register a new type call `ApiTypeRegister.register`.
    """

    @classmethod
    def getPymelType(cls, apiType, allowGuess='True'):
        """
        Map from api name to pymelName.
        
        we start by looking up types which are registered and then fall back
        to naming convention for types that haven't been registered yet.
        Perhaps pre-register the names?
        
        Returns
        -------
        Optional[str]
        """
        pass

    @classmethod
    def isRegistered(cls, apiTypeName): pass

    @classmethod
    def register(cls, apiTypeName, pymelType, inCast='None', outCast='None', apiArrayItemType='None'):
        """
        pymelType is the type to be used internally by pymel.
        apiType will be hidden from the user and converted to the pymel type,
        possibly via inCast.
        
        Parameters
        ----------
        apiTypeName : str
            the name of an apiType
        pymelType : Type
        inCast : Optional[Callable[[Any], Any]]
        outCast : Optional[Callable[[Any], Any]]
        apiArrayItemType : Optional[Type]
            if set, it should be the api type that represents each item in the array
        """
        pass

    __dict__ = None

    __weakref__ = None

    arrayItemTypes = {}

    doc = {}

    inCast = {}

    outCast = {}

    refCast = {}

    refInit = {}

    types = {}


class ApiRedoUndoItem(ApiUndoItem):
    """
    Similar to the base ApiUndoItem, but allows specifying a separate
    function for the redoer and the undoer
    """

    def __init__(self, redoer, redoArgs, undoer, undoArgs, redoKwargs='None', undoKwargs='None'): pass

    def __repr__(self): pass

    def undoIt(self): pass


class MelCommandMissingError(MissingInCacheError):
    def __init__(self, cmdName): pass

    def str(self): pass


class ApiMethodMissingError(MissingInCacheError):
    def __init__(self, apiClassName, methodName): pass

    def str(self): pass


class CallbackWithArgs(Callback):
    def __call__(self, *args, **kwargs): pass


class MetaMayaTypeWrapper(MetaMayaTypeRegistry):
    """
    A metaclass to wrap Maya api types, with support for class constants
    """

    @staticmethod
    def __new__(cls, classname, bases, classdict):
        """
        Create a new class of metaClassConstants type
        """
        pass

    @staticmethod
    def setattr_fixed_forDataDescriptorBug(self, name, value):
        """
        Fixes __setattr__ to work properly with properties
        
        Maya has a bug on windows where some api objects have a __setattr__
        that bypasses properties (and other data descriptors).
        """
        pass

    ClassConstant = None


class MAnimCurveChangeUndoItem(ApiRedoUndoItem):
    """
    Specialization of ApiRedoUndoItem for MAnimCurveChange objects.
    
    Basically just removes some boilerplate for construction of an
    ApiRedoUndoItem from an MAnimCurveChange object
    """

    def __init__(self, curveChangeObj): pass

    def __repr__(self): pass


class _MetaMayaCommandWrapper(MetaMayaTypeWrapper):
    """
    A metaclass for creating classes based on a maya command.
    
    Not intended to be used directly; instead, use the descendants: MetaMayaNodeWrapper, MetaMayaUIWrapper
    """

    @classmethod
    def docstring(cls, melCmdName): pass

    @classmethod
    def getMelCmd(cls, classdict):
        """
        Retrieves the name of the mel command the generated class wraps, and whether it is an info command.
        
        Intended to be overridden in derived metaclasses.
        """
        pass

    @staticmethod
    def __new__(cls, classname, bases, classdict): pass


class MetaMayaUIWrapper(_MetaMayaCommandWrapper):
    """
    A metaclass for creating classes based on on a maya UI type/command.
    """

    @classmethod
    def getMelCmd(cls, classdict): pass

    @staticmethod
    def __new__(cls, classname, bases, classdict): pass


class MetaMayaNodeWrapper(_MetaMayaCommandWrapper):
    """
    A metaclass for creating classes based on node type.  Methods will be added to the new classes
    based on info parsed from the docs on their command counterparts.
    """

    @classmethod
    def getMelCmd(cls, classdict):
        """
        Retrieves the name of the mel command for the node that the generated class wraps,
        and whether it is an info command.
        
        Derives the command name from the mel node name - so '__melnode__' must already be set
        in classdict.
        """
        pass

    @staticmethod
    def __new__(cls, classname, bases, classdict): pass


def mergeApiClassOverrides(): pass


def queryflag(cmdName, flag):
    """
    query flag decorator
    """
    pass


def getDoArgs(args, argList):
    """
    Parameters
    ----------
    args : List[Any]
        argument values
    argList : List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]]
    
    Returns
    -------
    do_args : List[Any]
    final_do_args : List[Any]
        Arguments prepped to be passed to the API method.
        Same as above but with SafeApiPtr converted
    out_type_list : List[Tuple[str, int]]
        list of (argument type, index)
    """
    pass


def _guessCmdName(func): pass


def toApiTypeEnum(obj, default='None'):
    """
    Parameters
    ----------
    obj : Union[str, util.ProxyUnicode]
    default : Optional[int]
    
    Returns
    -------
    int
    """
    pass


def makeEditFlagMethod(inFunc, flag, newMethodName='None', docstring="''", cmdName='None'): pass


def saveApiMelBridgeCache(): pass


def toPyTypeList(moduleName, objectName):
    """
    Returns a function which casts the members of it's iterable
    argument to the given class.
    
    Parameters
    ----------
    moduleName : str
    objectName : str
    
    Returns
    -------
    Callable[[Any], List[Any]]
    """
    pass


def _setApiCacheGlobals(): pass


def editflag(cmdName, flag):
    """
    edit flag decorator
    """
    pass


def loadCmdDocCache(): pass


def _createPyNode(module, mayaType, pyNodeTypeName, parentPyNodeTypeName, extraAttrs='None'):
    """
    Parameters
    ----------
    module
    mayaType : str
    pyNodeTypeName : str
    parentPyNodeTypeName : str
    extraAttrs
    
    Returns
    -------
    Optional[type]
    """
    pass


def _addFlagCmdDocs(func, cmdName, flag, docstring="''"): pass


def maybeConvert(val, castFunc): pass


def handleCallbacks(args, kwargs, callbackFlags): pass


def toPyType(moduleName, objectName):
    """
    Returns a function which casts it's single argument to
    an object with the given name in the given module (name).
    
    The module / object are given as strings, so that the module
    may be imported when the function is called, to avoid
    making factories dependent on, say, pymel.core.general or
    pymel.core.uitypes
    
    Parameters
    ----------
    moduleName : str
    objectName : str
    
    Returns
    -------
    Callable[[Any], Any]
    """
    pass


def splitToPyNodeList(res):
    """
    converts a whitespace-separated string of names to a list of PyNode objects
    
    Parameters
    ----------
    res : str
    
    Returns
    -------
    List[pymel.core.general.PyNode]
    """
    pass


def clearPyNodeTypes(): pass


def saveApiCache(): pass


def removeMayaType(mayaType):
    """
    Remove a type from the MayaTypes lists.
    
    - mayaTypesToApiTypes
    - mayaTypesToApiEnums
    """
    pass


def loadApiCache(): pass


def toPyUI(res):
    """
    returns a PyUI object
    
    Parameters
    ----------
    res : Optional[str]
    
    Returns
    -------
    Optional[pymel.core.uitypes.PyUI]
    """
    pass


def getDoArgsGetterUndo(args, argList, getter, setter, getterInArgs):
    """
    Parameters
    ----------
    args : List[Any]
        argument values
    argList : List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]]
    getter : Callable
        get function
    setter : Callable
        set function
    getterInArgs : List[str]
        list of argument names that are used to get the initial state when
        a method is undoable.
    
    Returns
    -------
    do_args : List[Any]
    final_do_args : List[Any]
        Same as above but with SafeApiPtr converted
    outTypeList : List[Tuple[str, int]]
        list of (argument type, index), used by processApiResult to retrieve
        output values from do_args
    undoItem : ApiUndoItem
    """
    pass


def fixCallbacks(inFunc, commandFlags, funcName='None'):
    """
    Prior to maya 2011, when a user provides a custom callback functions for a
    UI elements, such as a checkBox, when the callback is triggered it is passed
    a string instead of a real python values.
    
    For example, a checkBox changeCommand returns the string 'true' instead of
    the python boolean True. This function wraps UI commands to correct the
    problem and also adds an extra flag to all commands with callbacks called
    'passSelf'.  When set to True, an instance of the calling UI class will be
    passed as the first argument.
    
    if inFunc has been renamed, pass a funcName to lookup command info in apicache.cmdlist
    """
    pass


def getProxyResult(self, apiClass, method, final_do='()'): pass


def makeCreateFlagMethod(inFunc, flag, newMethodName='None', docstring="''", cmdName='None', returnFunc='None'):
    """
    Add documentation to a method that corresponds to a single command flag
    """
    pass


def addMelDocs(cmdName, flag='None'):
    """
    decorator for adding docs
    """
    pass


def getUndoArgs(args, argList, getter, getterInArgs):
    """
    Parameters
    ----------
    args : List[Any]
        argument values
    argList : List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]]
    getter : Callable
        get function
    getterInArgs : List[str]
    
    Returns
    -------
    List[Any]
    """
    pass


def raiseError(typ, *args): pass


def addCustomPyNode(module, mayaType, extraAttrs='None'):
    """
    create a PyNode, also adding each member in the given maya node's inheritance if it does not exist.
    
    This function is used for creating PyNodes via plugins, where the nodes parent's might be abstract
    types not yet created by pymel.  also, this function ensures that the newly created node types are
    added to pymel.all, if that module has been imported.
    
    Returns
    -------
    Optional[str]
    """
    pass


def asQuery(self, func, kwargs, flag): pass


def apiClassNameToPymelClassName(apiName, allowGuess='True'):
    """
    Given the name of an api class, such as MFnTransform, MSpace, MAngle,
    returns the name of the corresponding pymel class.
    
    Parameters
    ----------
    apiName : str
    allowGuess : bool
        If enabled, and we cannot find a registered type that matches, will
        try to do string parsing to guess the pymel name.
    
    Returns
    -------
    Optional[str]
        Returns None if it was unable to determine the name.
    """
    pass


def addCmdDocs(func, cmdName='None'):
    """
    Parameters
    ----------
    func : C
    cmdName : Optional[str]
    
    Returns
    -------
    C
    """
    pass


def toPyNodeList(res):
    """
    returns a list of PyNode objects
    
    Parameters
    ----------
    res : Optional[List[str]]
    
    Returns
    -------
    List[pymel.core.general.PyNode]
    """
    pass


def _getApiOverrideData(classname, pymelName): pass


def addApiDocs(apiClass, methodName, overloadIndex='None', undoable='True'):
    """
    decorator for adding API docs
    """
    pass


def getDoArgsAnimCurveUndo(args, argList):
    """
    Parameters
    ----------
    args : List[Any]
        argument values
    argList : List[Tuple[str, Union[str, Tuple[str, str]], str, Optional[str]]]
    
    Returns
    -------
    do_args : List[Any]
    final_do_args : List[Any]
        Arguments prepped to be passed to the API method.
        Same as above but with SafeApiPtr converted
    out_type_list : List[Tuple[str, int]]
        list of (argument type, index)
    undoItem : ApiUndoItem
    """
    pass


def getComponentTypes(): pass


def toApiTypeStr(obj, default='None'):
    """
    Parameters
    ----------
    obj : Union[int, str, util.ProxyUnicode]
    default : Optional[str]
    
    Returns
    -------
    Optional[str]
    """
    pass


def convertTimeValues(rawVal): pass


def makeQueryFlagMethod(inFunc, flag, newMethodName='None', docstring="''", cmdName='None', returnFunc='None'): pass


def removePyNode(module, mayaType): pass


def functionFactory(funcNameOrObject, returnFunc='None', module='None', rename='None', uiWidget='False'):
    """
    create a new function, apply the given returnFunc to the results (if any)
    Use pre-parsed command documentation to add to __doc__ strings for the
    command.
    """
    pass


def addApiDocsCallback(apiClass, methodName, overloadIndex='None', undoable='True', origDocstring="''"): pass


def addFlagCmdDocsCallback(cmdName, flag, docstring):
    """
    Add documentation to a method that corresponds to a single command flag
    """
    pass


def getUncachedCmds(): pass


def unwrapToPyNode(res):
    """
    unwraps a 1-item list, and returns a PyNode object
    
    Parameters
    ----------
    res : List[str]
    
    Returns
    -------
    Optional[pymel.core.general.PyNode]
    """
    pass


def getPymelTypeName(mayaTypeName, create='True'): pass


def addPyNodeType(pyNodeType, parentPyNode): pass


def isValidPyNodeName(arg): pass


def toApiFunctionSet(obj):
    """
    Parameters
    ----------
    obj : Union[str, int]
    
    Returns
    -------
    Optional[Type]
    """
    pass


def _getApiOverrideNameAndData(classname, pymelName): pass


def makeUICallback(origCallback, args, doPassSelf):
    """
    this function is used to make the callback, so that we can ensure the origCallback gets
    "pinned" down
    """
    pass


def loadCmdCache(): pass


def removePyNodeType(pyNodeTypeName): pass


def _getSourceFunction(funcNameOrObject, module='None'): pass


def _addApiDocs(wrappedApiFunc, apiClass, methodName, overloadIndex='None', undoable='True'): pass


def getCmdFunc(cmdName):
    """
    Parameters
    ----------
    cmdName : str
    
    Returns
    -------
    Callable
    """
    pass


def registerVirtualClass(self, vclass, nameRequired='False', isVirtual="'_isVirtual'", preCreate="'_preCreateVirtual'",
                         create="'_createVirtual'", postCreate="'_postCreateVirtual'"):
    """
    Register a new virtual class
    
    Allows a user to create their own subclasses of leaf PyMEL node classes,
    which are returned by `general.PyNode` and all other pymel commands.
    
    The process is fairly simple:
        1.  Subclass a PyNode class.  Be sure that it is a leaf class,
            meaning that it represents an actual Maya node type and not an
            abstract type higher up in the hierarchy.
        2.  Add an _isVirtual classmethod that accepts two arguments: an
            MObject/MDagPath instance for the current object, and its name.
            It should return True if the current object meets the
            requirements to become the virtual subclass, or else False.
        3.  Add optional _preCreate, _create, and _postCreate methods.  For
            more on these, see below
        4.  Register your subclass by calling
            factories.registerVirtualClass. If the _isVirtual callback
            requires the name of the object, set the keyword argument
            nameRequired to True. The object's name is not always
            immediately available and may take an extra calculation to
            retrieve, so if nameRequired is not set the name argument
            passed to your callback could be None.
    
    The creation of custom nodes may be customized with the use of
    isVirtual, preCreate, create, and postCreate functions; these are
    functions (or classmethods) which are called before / during / after
    creating the node.
    
    The isVirtual method is required - it is the callback used on instances
    of the base (ie, 'real') objects to determine whether they should be
    considered an instance of this virtual class. It's input is an MObject
    and an optional name (if nameRequired is set to True). It should return
    True to indicate that the given object is 'of this class', False
    otherwise. PyMEL code should not be used inside the callback, only API
    and maya.cmds. Keep in mind that once your new type is registered, its
    test will be run every time a node of its parent type is returned as a
    PyMEL node class, so be sure to keep your tests simple and fast.
    
    The preCreate function is called prior to node creation and gives you a
    chance to modify the kwargs dictionary; they are fed the kwargs fed to
    the creation command, and return either 1 or 2 dictionaries; the first
    dictionary is the one actually passed to the creation command; the
    second, if present, is passed to the postCreate command.
    
    The create method can be used to override the 'default' node creation
    command;  it is given the kwargs given on node creation (possibly
    altered by the preCreate), and must return the string name of the
    created node. (...or any another type of object (such as an MObject),
    as long as the postCreate and class.__init__ support it.)
    
    The postCreate function is called after creating the new node, and
    gives you a chance to modify it.  The method is passed the PyNode of
    the newly created node, as well as the second dictionary returned from
    the preCreate function as kwargs (if it was returned). You can use
    PyMEL code here, but you should avoid creating any new nodes.
    
    By default, any method named '_isVirtual', '_preCreateVirtual',
    '_createVirtual', or '_postCreateVirtual' on the class is used; if
    present, these must be classmethods or staticmethods.
    
    Other methods / functions may be used by passing a string or callable
    to the preCreate / postCreate kwargs.  If a string, then the method
    with that name on the class is used; it should be a classmethod or
    staticmethod present at the time it is registered.
    
    The value None may also be passed to any of these args (except isVirtual)
    to signal that no function is to be used for these purposes.
    
    If more than one subclass is registered for a node type, the registered
    callbacks will be run newest to oldest until one returns True. If no
    test returns True, then the standard node class is used. Also, for each
    base node type, if there is already a virtual class registered with the
    same name and module, then it is removed. (This helps alleviate
    registered callbacks from piling up if, for instance, a module is
    reloaded.)
    
    Overriding methods of PyMEL base classes should be performed with care,
    because certain methods are used internally and altering their results
    may cause PyMEL to error or behave unpredictably.  This is particularly
    true for special methods like __setattr__, __getattr__, __setstate__,
    __getstate__, etc.  Some methods are considered too dangerous to modify,
    and registration will fail if the user defines an override for them;
    this set includes __init__, __new__, and __str__.
    
    For a usage example, see examples/customClasses.py
    
    Parameters
    ----------
    nameRequired : `bool`
        True if the _isVirtual callback requires the string name to operate
        on. The object's name is not always immediately avaiable and may
        take an extra calculation to retrieve.
    isVirtual: `str` or callable
        the function to determine whether an MObject is an instance of this
        class; should take an MObject and name, returns True / or False
    preCreate: `str` or callable
        the function used to modify kwargs before being passed to the
        creation function
    create: `str` or callable
        function to use instead of the standard node creation method;
        takes whatever args are given to the cl
    postCreate: `str` or callable
        the function used to modify the PyNode after it is created.
    """
    pass


def mayaTypeToApiType(mayaType):
    """
    Get the Maya API type from the name of a Maya type
    
    Parameters
    ----------
    mayaType : str
    
    Returns
    -------
    str
    """
    pass


def asEdit(self, func, kwargs, flag, val): pass


def addMayaType(mayaType, apiType='None'):
    """
    Add a type to the MayaTypes lists. Fill as many dictionary caches as we have info for.
    
    - mayaTypesToApiTypes
    - mayaTypesToApiEnums
    """
    pass


def _addPyNode(module, mayaType, parentMayaType, extraAttrs='None'):
    """
    create a PyNode type for a maya node.
    
    Returns
    -------
    name : str
    class : type
    """
    pass


def toPyNode(res):
    """
    returns a PyNode object
    
    Parameters
    ----------
    res : Optional[str]
    
    Returns
    -------
    Optional[pymel.core.general.PyNode]
    """
    pass


def createflag(cmdName, flag):
    """
    create flag decorator
    """
    pass


def toPyUIList(res):
    """
    returns a list of PyUI objects
    
    Parameters
    ----------
    res : str
    
    Returns
    -------
    List[pymel.core.uitypes.PyUI]
    """
    pass


def wrapApiMethod(apiClass, methodName, newName='None', proxy='True', overloadIndex='None'):
    """
    create a wrapped, user-friendly API method that works the way a python method should: no MScriptUtil and
    no special API classes required.  Inputs go in the front door, and outputs come out the back door.
    
    
    Regarding Undo
    --------------
    
    The API provides many methods which are pairs -- one sets a value
    while the other one gets the value.  the naming convention of these
    methods follows a fairly consistent pattern.  so what I did was
    determine all the get and set pairs, which I can use to automatically
    register api undo items:  prior to setting something, we first *get*
    it's existing value, which we can later use to reset when undo is
    triggered.
    
    This API undo is only for PyMEL methods which are derived from API
    methods.  it's not meant to be used with plugins.  and since it just
    piggybacks maya's MEL undo system, it won't get cross-mojonated.
    
    Take `MFnTransform.setTranslation`, for example. PyMEL provides a wrapped copy of this as
    `Transform.setTranslation`.   when pymel.Transform.setTranslation is
    called, here's what happens in relation to undo:
    
        #. process input args, if any
        #. call MFnTransform.getTranslation() to get the current translation.
        #. append to the api undo queue, with necessary info to undo/redo
           later (the current method, the current args, and the current
           translation)
        #. call MFnTransform.setTranslation() with the passed args
        #. process result and return it
    
    
    Parameters
    ----------
    apiClass : Type
        the api class
    methodName : str
        the name of the api method
    newName : str
        optionally provided if a name other than that of api method is desired
    proxy : bool
        If True, then __apimfn__ function used to retrieve the proxy class. If False,
        then we assume that the class being wrapped inherits from the underlying api class.
    overloadIndex : Optional[int]
        which of the overloaded C++ signatures to use as the basis of our wrapped function.
    """
    pass


def listForNoneQuery(res, kwargs, flags):
    """
    convert a None to an empty list on the given query flags
    """
    pass


def _getTimeRangeFlags(cmdName):
    """
    used parsed data and naming convention to determine which flags are
    callbacks
    """
    pass


def processApiResult(result, outTypeList, do_args):
    """
    Parameters
    ----------
    result : Any
        Result returned from the API method
    outTypeList : List[Tuple[str, int]]
        output argument types and their indices.  should be same len as outArgs
    do_args : List[Any]
    
    Returns
    -------
    Any
    """
    pass


def isValidPyNode(arg): pass


def addCmdDocsCallback(cmdName, docstring="''"): pass


def isMayaType(mayaType):
    """
    Whether the given type is a currently-defined maya node name
    
    Parameters
    ----------
    str
    
    Returns
    -------
    bool
    """
    pass


apiClassNamesToPyNodeNames = {}

apiTypesToApiClasses = {}

moduleCmds = {}

apiEnumsToApiTypes = {}

Always = None

pymelTypeNameToMayaTypeName = {}

apiEnumsToPyComponents = {}

_apiMelBridgeCacheInst = None

apiTypesToApiEnums = {}

apiToMelData = {}

simpleCommandWraps = {}

apiClassNamesToPymelTypes = {}

_logger = None

nodeHierarchy = []

apiUndo = ApiUndo()

nodeCommandList = []

EXCLUDE_METHODS = []

pyNodeTypesHierarchy = {}

docCacheLoaded = True

nodeTypeToInfoCommand = {}

_DEBUG_API_WRAPS = False

pyNodeNamesToPyNodes = {}

mayaTypesToApiTypes = {}

uiClassList = []

_apiCacheInst = None

_cmdCacheInst = None

mayaTypesToApiEnums = {}

cmdlist = {}

apiClassInfo = {}

virtualClasses = VirtualClassManager()

mayaTypeNameToPymelTypeName = {}

docstringMode = 'pydoc'

apiClassOverrides = {}
