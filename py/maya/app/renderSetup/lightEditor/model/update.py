if False:
    from typing import Dict, List, Tuple, Union, Optional


def isDirty(): pass


def setDirty(dirty): pass


def doUpdate(): pass


def requestRefreshUI(): pass


def doRefreshUI(): pass


def addChangeCallbacks(node):
    """
    Add callbacks needed for keeping enabled up to date in the light editor item tree when 
    selfEnabled or isolateSelected changes on an item. We have extra requirements for this 
    in the light editor since these attributes can have overrides applied, that is why these
    callbacks are needed.
    
    In order to support the case where an override is applied and changes the value of 
    selfEnabled or isolateSelected we must use the addNodeDirtyPlugCallback. However
    we are not allowed to perform the update immediately from this callback since it's
    called during dirty propagation and evaluation is not finished yet. So instead we
    need to defer the update until the next time someone wants to query an enabled plug.
    The addAttributeChangedCallback is used to check when that plug is evaluated and if 
    the state is set to dirty then we perform the update.
    """
    pass


_isDirty = False

_refreshUIRequested = _isDirty
