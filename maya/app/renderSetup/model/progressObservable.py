if False:
    from typing import Dict, List, Tuple, Union, Optional

from . import observable


class ProgressObservable(observable.SingletonObservable):
    """
    When an operation has a high chance of taking time to complete, this
    class should be used to track information on its progress.
    The goal is to register observers that care about the progress of
    long operations so that they react to the incremental steps being done.
    The consumer has to take ownership of the singleton and give it back
    once the operation is complete.
    """

    def __init__(self): pass

    def endProgress(self):
        """
        This should always be called once the long operation is complete.
        This ceases ownership of the singleton for others to use it.
        """
        pass

    def inProgress(self):
        """
        As soon as the first caller calls startProgress, callerCount gets
        incremented, meaning that an operation is in progress.
        """
        pass

    def notifyItemObserver(self, progress, info):
        """
        Whenever the owner wants to notify observers of progress being done
        on the way to completing the long operation, this should be called
        with the percentage of progress already done and the info on the
        'suboperation' being computed.
        """
        pass

    def startProgress(self):
        """
        Allows a consumer to take ownership of this singleton.
        Should always be called before notifyItemObserver and endProgress.
        """
        pass

    def topLevelCaller(self):
        """
        The first caller to call startProgress is the top level one, and
        the only one that gets taken care of. An assumption has to be made
        that the number of startProgress and endProgress calls is
        symmetrical. The ProgressCtxMgr helps to make that assumption true.
        """
        pass

    EndProgressNotification = None

    StartProgressNotification = None


class ProgressCtxMgr(object):
    """
    This context manager can be used to encapsulate code containing
    a long operation. It allows the consumer to take ownership of the
    progress bar temporarily (on __exit__ ownership is given back to be
    used by other consumers).
    """

    def __enter__(self): pass

    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def __init__(self): pass

    __dict__ = None

    __weakref__ = None


def progress(f):
    """
    This is a clean way to encapsulate the whole function f as a long op
    """
    pass
