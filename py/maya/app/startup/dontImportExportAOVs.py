if False:
    from typing import Dict, List, Tuple, Union, Optional


def _getRenderers():
    """
    Return the list of renderers in the rendererCallbacks dict.
    """
    pass


def _getaovNodeTypes():
    """
    Return the list of AOV node types for all registered renderers.
    """
    pass


def _renderSetupEnabled(): pass


def initialize():
    """
    Create callbacks related to File Import and File Export, to prevent
    AOVs from being imported/exported. Theoretically, the callbacks should
    only be created when Render Setup is used. When legacy render layers
    are used instead, we should not execute the body of this function.
    In practice, we remove them during the first fileImport or fileExport
    that occurs.
    """
    pass


def _beforeFileExport(self): pass


def finalize():
    """
    Remove callbacks associated to file import operations.
    """
    pass


def _setDoNotWrite(nodes, state): pass


def _fileExported(self): pass


def _fileImported(_): pass


def _beforeFileImport(_):
    """
    No node added notification is sent during file import.  Therefore, we
    take a snapshot of all AOV nodes before the import, then take one
    after import, and remove all AOV nodes that were created by the
    import.
    """
    pass


_first_call_to_callback = True

_aovNodes = []

_aovNodesPre = []

_aovNodeTypes = []

_callbackIDs = []

aovNodeTypesTest = []
