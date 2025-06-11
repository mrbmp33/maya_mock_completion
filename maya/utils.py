"""
General utility functions that are not specific to Maya Commands or the 
OpenMaya API.

Note:
By default, handlers are installed for the root logger.  This can be overriden
with env var MAYA_DEFAULT_LOGGER_NAME.
Env vars MAYA_GUI_LOGGER_FORMAT and MAYA_SHELL_LOGGER_FORMAT can be used to 
override the default formatting of logging messages sent to the GUI and 
shell respectively.
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


class StringTable(object):
    """
    The StringTable object allows access to the application's string catalog which is used, which is used to support application lookup for localized string resources.  The strings in this table may be over written by localized versions, which will then be picked up by scripts that access these values.
    
    This class behaves in the same way as a Dictionary object in Python with respect to getting and setting values.
    Note that StringTable objects just provide access to the single application-wide string table.  So, creating a new StringTable object does not create a new string table inside the application, it is just another interface to the existing global table.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    __new__ = None


class Output(object):
    """
    MayaOutput objects
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def flush(*args, **kwargs):
        """
        Flush no-op
        """
        pass

    def write(*args, **kwargs):
        """
        Write the given string
        """
        pass

    def writelines(*args, **kwargs):
        """
        Write the given sequence
        """
        pass

    __new__ = None

    softspace = None


import logging


class MayaGuiLogHandler(logging.Handler):
    """
    A python logging handler that displays error and warning
    records with the appropriate color labels within the Maya GUI
    """

    def __init__(self): pass

    def emit(self, record): pass


def formatGuiException(exceptionType, exceptionObject, traceBack, detail='2'):
    """
    Format a trace stack into a string.
    
        exceptionType   : Type of exception
        exceptionObject : Detailed exception information
        traceBack       : Exception traceback stack information
        detail          : 0 = no trace info, 1 = line/file only, 2 = full trace
                          
    To perform an action when an exception occurs without modifying Maya's 
    default printing of exceptions, do the following::
    
        import maya.utils
        def myExceptCB(etype, value, tb, detail=2):
            # do something here...
            return maya.utils._formatGuiException(etype, value, tb, detail)
        maya.utils.formatGuiException = myExceptCB
    """
    pass


def _dumpCurrentFrames():
    """
    # crash handling
    """
    pass


def loadStringResourcesForFile(scriptPath, fullModulePath, resourceFileName):
    """
    Load a string resource.
    
    The 'scriptPath' argument must be a string containing the full path of to 
    a language resource file. The 'resourceFileName' is the _res.py that must be loaded.
    
    If the _res.py fails to be found or executed successfully, the method returns False.
    Otherwise it returns True.
    """
    pass


def _prefixTraceStack(tbStack, prefix="'# '"):
    """
    prefix with '#', being sure to get internal newlines. do not prefix first line
    as that will be added automatically.
    """
    pass


def formatGuiResult(obj): pass


def helpNonVerbose(thing, title="'Python Library Documentation: %s'", forceload='0'):
    """
    Utility method to return python help in the form of a string
    
    thing - str or unicode name to get help on
    title - format string for help result
    forceload - argument to pydoc.resolve, force object's module to be reloaded from file
    
    returns formated help string
    """
    pass


def loadStringResourcesForModule(moduleName):
    """
    Load the string resources associated with the given module
    
    Note that the argument must be a string containing the full name of the 
    module (eg "maya.app.utils").  The module of that name must have been 
    previously imported.
    
    The base resource file is assumed to be in the same location as the file
    defining the module and will have the same name as the module except with
    _res.py appended to it.  So, for the module foo, the resource file should
    be foo_res.py.  
    
    If Maya is running in localized mode, then the standard location for 
    localized scripts will also be searched (the location given by the 
    command cmds.about( localizedResourceLocation=True ))
    
    Failure to find the base resources for the given module will trigger an 
    exception. Failure to find localized resources is not an error.
    """
    pass


def _fixConsoleLineNumbers(tbStack): pass


def _guiExceptHook(exceptionType, exceptionObject, traceBack, detail='2'):
    """
    Whenever Maya receives an error from the command engine it comes into here
    to format the message for display. 
    Formatting is performed by formatGuiException.
        exceptionType   : Type of exception
        exceptionObject : Detailed exception information
        traceBack       : Exception traceback stack information
        detail          : 0 = no trace info, 1 = line/file only, 2 = full trace
    """
    pass


def _origShellLogHandler():
    """
    Adds an additional handler to the root logger to print to sys.stdout
    Returns the handler.
    """
    pass


def executeDeferred(*args, **kwargs):
    """
    Delays the execution of the given script or function until Maya is idle.

    This function runs code using the idle event loop.  This means that the
    main thread must become idle before this python code will be executed.

    There are two different ways to call this function.  The first is to
    supply a single string argument which contains the Python code to execute.
    In that case the code is interpreted.

    The second way to call this routine is to pass it a "callable" object.
    When that is the case, then the remaining regular arguments and keyword
    arguments will be passed to the callable object
    """
    try:
        import maya.utils as maya_utils
    except ImportError:
        # If maya.utils is not available, just execute immediately (mock behavior)
        if not any(args) and not kwargs:
            raise TypeError("executeDeferred() requires at least one argument")
        if callable(args[0]):
            func = args[0]
            args = args[1:]
            return func(*args, **kwargs)
        elif isinstance(args[0], str):
            code = args[0]
            compiled_code = compile(code, '<string>', 'exec')
            exec(compiled_code, globals(), locals())
            return
        else:
            raise TypeError("First argument must be a callable or a string of code")
    else:
        # Use Maya's real executeDeferred if available
        if hasattr(maya_utils, "executeDeferred") and maya_utils.executeDeferred is not executeDeferred:
            return maya_utils.executeDeferred(*args, **kwargs)
        # Fallback: execute immediately
        if not any(args) and not kwargs:
            raise TypeError("executeDeferred() requires at least one argument")
        if callable(args[0]):
            func = args[0]
            args = args[1:]
            return func(*args, **kwargs)
        elif isinstance(args[0], str):
            code = args[0]
            compiled_code = compile(code, '<string>', 'exec')
            exec(compiled_code, globals(), locals())
            return
        else:
            raise TypeError("First argument must be a callable or a string of code")


def processIdleEvents(*args, **kwargs):
    """
    Run commands from the idle queue.
    
    In general there should be no need to call this method.  It is included here
    as it allows for testing of code that uses the idle events for processing.
    Use this method with caution as will change the behaviour of Maya by 
    possibly forcing refreshes or causing other code run before it normally would.
    This may make Maya unrepsonsive.
    
    This function will return True if all items on the idle queue have been 
    processed.  It will return False if only some of the items have been processed.
    There are several cases in which not all items on the idle queue will execute,
    such as when there is an item with exclusive priority.
    
    This function does not take any arguments.
    """
    pass


def _mayadisplayhook(*args, **kwargs):
    """
    Display hook function used to capture interpreter results
    """
    pass


def guiLogHandler():
    """
    Adds an additional handler to the root logger to print to
    the script editor.  Sets the shell/outputWindow handler to
    only print 'Critical' records, so that the logger's primary
    output is the script editor.
    Returns the handler.
    """
    pass


def _formatGuiResult(obj):
    """
    Gets a string representation of a result object.
    
    To perform an action when a result is about to returned to the script editor
    without modifying Maya's default printing of results, do the following:
    
        import maya.utils
        def myResultCallback(obj):
            # do something here...
            return maya.utils._formatGuiResult(obj)
        maya.utils.formatGuiResult = myResultCallback
    """
    pass


def _decodeStack(tbStack): pass


def shellLogHandler(*args, **kwargs): pass


def _guiResultHook(obj):
    """
    In GUI mode, called by the command engine to stringify a result for display.
    """
    pass


def getPossibleCompletions(input):
    """
    Utility method to handle command completion
    Returns in a list all of the possible completions that apply
    to the input string
    """
    pass


def executeInMainThreadWithResult(*args, **kwargs):
    """
    Runs Python code in the main thread and waits for the return code.
    
    There are two different ways to call this function.  The first is to
    supply a single string argument which contains the Python code to execute.
    In that case the code is interpreted.
    
    The second way to call this routine is to pass it a "callable" object.
    When that is the case, then the remaining regular arguments and keyword
    arguments will be passed to the callable object
    
    Note that if this routine is called from the main thread, then it will
    simply execute the given Python on the spot and return the result
    """
    if not any(args) and not kwargs:
        raise TypeError("executeInMainThreadWithResult() requires at least one argument")

    if callable(args[0]):
        # If the first argument is callable, we assume it's a function to call
        # with the remaining args and kwargs.
        func = args[0]
        args = args[1:]
        return func(*args, **kwargs)
    
    elif isinstance(args[0], str):
        # If the first argument is a string, we assume it's a Python code snippet
        # to execute.
        code = args[0]
        try:
            # Compile the code to ensure it's valid Python
            compiled_code = compile(code, '<string>', 'exec')
            # Execute the compiled code in the main thread
            exec(compiled_code, globals(), locals())
            return locals()  # Return the local variables after execution
        except Exception as e:
            raise RuntimeError(f"Error executing code: {e}")

def runOverriddenModule(modName, callingFileFunc, globals):
    """
    Run a module that has been 'overriden' on the python path by another module.
    
    Ie, if you have two modules in your python path named 'myModule', this can
    be used to execute the code in the myModule that is LOWER in priority on the
    sys.path (the one that would normally not be found).
    
    Intended to be used like:
    
    >> import maya.utils
    >> maya.utils.runOverriddenModule(__name__, lambda: None, globals())
    
    Note that if modName is a sub-module, ie "myPackage.myModule", then calling
    this function will cause "myPackage" to be imported, in order to determine
    myPackage.__path__ (though in most circumstances, it will already have
    been).
    
    Parameters
    ----------
    modName : str
        The name of the overriden module that you wish to execute
    callingFileFunc : function
        A function that is defined in the file that calls this function; this is
        provided solely as a means to identify the FILE that calls this
        function, through the use of inspect.getsourcefile(callingFileFunc).
        This is necessary because it is possible for this call to get "chained";
        ie, if you have path1/myMod.py, path2/myMod.py, and path3/myMod.py,
        which will be found on the sys.path in that order when you import myMod,
        and BOTH path1/myMod.py AND path2/myMod.py use runOverriddenModule, then
        the desired functionality would be: path1/myMod.py causes
        path2/myMod.py, which causes path3/myMod.py to run.  However, if
        runOverriddenModule only had __name__ (or __file__) to work off of,
        path2/myMod.py would still "think" it was executing in the context of
        path1/myMod.py... resulting in an infinite loop when path2/myMod.py
        calls runOverriddenModule. This parameter allows runOverriddenModule to
        find the "next module down" on the system path. If the file that
        originated this function is NOT found on the system path, an ImportError
        is raised.
    globals : dict
        the globals that the overridden module should be executed with
    
    Returns
    -------
    str
        The filepath that was executed
    """
    pass


_shellLogHandler = None

appLoggerName = ''

_runOverriddenModule_already_executed = set()

_guiLogHandler = MayaGuiLogHandler()
