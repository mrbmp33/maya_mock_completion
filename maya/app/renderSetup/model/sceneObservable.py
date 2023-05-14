"""
It listens to Maya scene change events and it forwards them to the
registered callbacks when global observation is enabled (sceneObserversEnabled).
"""

from maya.app.renderSetup.model.observableProxy import ObservableDGProxy
from maya.app.renderSetup.model.observableProxy import ObservableProxy
from maya.app.renderSetup.model.observableProxy import ObservableDagProxy

if False:
    from typing import Dict, List, Tuple, Union, Optional


class SceneObservable(object):
    def __del__(self): pass

    def __init__(self): pass

    def activate(self):
        """
        Create callbacks to listen to scene changes.
        """
        pass

    def activated(self): pass

    def beforeNew(self):
        """
        Infrastructure method called on file new.
        
        This method should not be called by SceneObservable clients.
        """
        pass

    def deactivate(self):
        """
        Removes callbacks to listen to scene changes
        """
        pass

    def isInSceneChangeCallback(self): pass

    def register(self, eventType, observer):
        """
        Add a callback for the given event(s).
        """
        pass

    def unregister(self, eventType, observer):
        """
        Removes a callback for the given event(s).
        """
        pass

    BEFORE_FILE_EXPORT = 'BeforeFileExport'

    BEFORE_FILE_IMPORT = 'BeforeFileImport'

    BEFORE_FILE_OPEN = 'BeforeFileOpen'

    BEFORE_REFERENCE_CREATE = 'BeforeReferenceCreate'

    BEFORE_REFERENCE_LOAD = 'BeforeReferenceLoad'

    BEFORE_REFERENCE_REMOVE = 'BeforeReferenceRemove'

    BEFORE_REFERENCE_UNLOAD = 'BeforeReferenceUnload'

    CONNECTION_CHANGED = 'ConnectionChanged'

    FILE_EXPORTED = 'FileExported'

    FILE_IMPORTED = 'FileImported'

    FILE_OPENED = 'FileOpened'

    NODE_ADDED = 'NodeAdded'

    NODE_REMOVED = 'NodeRemoved'

    NODE_RENAMED = 'NodeRenamed'

    NODE_REPARENTED = 'NodeReparented'

    REFERENCE_CREATED = 'ReferenceCreated'

    REFERENCE_LOADED = 'ReferenceLoaded'

    REFERENCE_REMOVED = 'ReferenceRemoved'

    REFERENCE_UNLOADED = 'ReferenceUnloaded'

    __dict__ = None

    __weakref__ = None


def enableSceneObservers(value): pass


def sceneObserversEnabled(): pass


def isInSceneChangeCallback(): pass


def instance(): pass


_renderSetup_sceneObserversEnabled = True

_sceneObservable = SceneObservable()

logger = None
