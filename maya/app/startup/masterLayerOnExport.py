if False:
    from typing import Dict, List, Tuple, Union, Optional


def _renderSetupEnabled(): pass


def finalize():
    """
    Remove the created callbacks
    """
    pass


def initialize():
    """
    Create 2 callbacks, one before and one after export, to change to the master
    layer and then back again.
    """
    pass


def _noSwitchToMaster(): pass


def _beforeFileExport(_):
    """
    Change to the master layer before file export.
    """
    pass


def _fileExported(_):
    """
    Change back to the previously saved render layer after export.
    """
    pass


_first_call_to_callback = True

_exported_file_extension = None

_callbackIDs = []

_supported_renderer_extensions = set()
