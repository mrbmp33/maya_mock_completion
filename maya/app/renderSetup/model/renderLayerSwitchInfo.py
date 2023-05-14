"""
This module is used to notify of progress during layer switching, which
can be a lengthy operation.
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


class RenderLayerSwitchInfo(object):
    """
    Gets information on layer switch operations.
    Keeps track of the layer switch progress by estimating the number
    of apply overrides that could possibly need applying/unapplying.
    When a layer switch operation is in progress, we frequently update the
    ProgressObservable with the current information.
    """

    def __init__(self): pass

    def info(self):
        """
        Returns information about the current operation being
        computed during the layer switch.
        """
        pass

    def progress(self): pass

    def update(self):
        """
        Update the ProgressObservable (the subject) with
        the new information of where the progress is at.
        This includes the percentage of progress estimated to be done and
        the information related to the current operation being computed.
        """
        pass

    __dict__ = None

    __weakref__ = None


class _Context(object):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    __dict__ = None

    __weakref__ = None


class ApplyOverrideContext(_Context):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, ovr): pass


class UnapplyApplyOverrideContext(_Context):
    def __exit__(self, type, value, traceback): pass


class SwitchLayerContext(_Context):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, oldLayer, newLayer): pass


class ApplyApplyOverrideContext(_Context):
    def __exit__(self, type, value, traceback): pass


class UnapplyOverrideContext(_Context):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, ovr): pass


class UnapplyLayerImportRefContext(_Context):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, oldLayer, data='None'): pass


kUnapplyLayer = []

kApplyOverride = []

kApplyLayer = []

kUnapplyOverride = []

IMPORT = 0

kReadResolveConflicts = []

kImporting = []

kReferencing = []

REFERENCE = 1
