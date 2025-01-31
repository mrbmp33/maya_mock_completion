"""
Redefine format warning to avoid getting garbage at end of line when raised directly from Maya console
and define a UserWarning class that does only print it's message (no line or module info)
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


class PymelBaseWarning(Warning):
    """
    # Subclass just to allow users to configure filtering of pymel-specific
    # deprecations
    """

    __weakref__ = None


class PymelBaseDeprecationWarning(PymelBaseWarning):
    pass


class ExecutionWarning(UserWarning, PymelBaseWarning):
    """
    Simple Warning class that doesn't print any information besides warning message
    """

    __weakref__ = None


class PymelFutureWarning(FutureWarning, PymelBaseDeprecationWarning):
    """
    # Subclass from FutureWarning so it's displayed by default
    """

    __weakref__ = None


class MayaDeprecationWarning(DeprecationWarning, PymelBaseDeprecationWarning):
    """
    # Subclass from DeprecationWarning so it's not displayed by default
    """

    __weakref__ = None


def warn(*args, **kwargs):
    """
    Default Maya warn which uses ExecutionWarning as the default warning class.
    """
    pass


def formatwarning(message, category, filename, lineno, line='None'):
    """
    Redefined format warning for maya.
    """
    pass


def deprecated(funcOrMessage='None', className='None',
               baseMessage='"The function \'{objName}\' is deprecated and will become unavailable in future pymel versions"',
               warningType='"<class \'pymel.internal.pwarnings.PymelFutureWarning\'>"'):
    """
    Decorates a function so that it prints a deprecation warning when called.
    
    The decorator can either receive parameters or the function directly.
    
    Parameters
    ----------
    funcOrMessage : Union[str, Callable[..., Any], None]
        If passed a message, the message will be appended to the standard
        deprecation warning and should serve to further clarify why the function
        is being deprecated and/or suggest an alternative function. In this
        case, the return result of this function is another decorator (with the
        ammended message), which then needs to be fed the function to be
        decorated. Otherwise, funcOrMessage should be the func to be decorated,
        and the return result is decorated version of funcOrMessage
    className : Union[str, False, None]
        If given as a str, then the decorated function is asssumed to be method,
        and the name is printed as "module.className.funcName".  If False, it
        is assumed to NOT be a method, and the name is printed as
        "module.funcName".  If None, then the decorator will try to
        automatically determine whether the passed function is a method, and if
        so, what it's className is.
    baseMessage : Optional[str]
        Message which will be combined with the optional message (in
        funcOrMessage) to form the final message. Maybe set to None to ensure
        only the message (in funcOrMessage) is printed.
    warningType : Type[Warning]
        Warning class to raise. Note that DeprecationWarning is ignored by
        default.
    """
    pass


def maya_deprecated(funcOrMessage='None', className='None',
                    baseMessage='"The function \'{objName}\' has been deprecated by maya and may become unavailable in future maya versions"',
                    warningType='"<class \'pymel.internal.pwarnings.MayaDeprecationWarning\'>"'): pass
