if False:
    from typing import Dict, List, Tuple, Union, Optional


def resolveTemplateFile(fileName):
    """
    # Locate a template file by name.
    # Location:
    #    - First use the provided path (as an absolute path) if it exists
    #    - Second look in the user template directory
    #    - Third look in the global template directory
    """
    pass


def loadPreset(fileName):
    """
    # Load a render settings preset file from disk. Resolve the path if needed.
    # This method can be called when batch rendering from the command line using the "-rsp" flag.
    """
    pass


def resolvePresetFile(fileName):
    """
    # Locate a preset file by name.
    # Location:
    #    - First use the provided path (as an absolute path) if it exists
    #    - Second look in the user preset directory
    #    - Third look in the global preset directory
    """
    pass


def loadAOVs(fileName):
    """
    # Load an AOV preset file from disk.   Resolve the path if needed.
    # This method can be called when batch rendering from the command line using the "-rsa" flag.
    """
    pass


def loadTemplate(fileName):
    """
    # Load a template file from disk.  Resolve the path if needed.
    # This method can be called when batch rendering from the command line using the "-rst" flag.
    """
    pass


kTemplateFileNotFound = []

kPresetFileNotFound = []

kInvalidTemplateFound = []

kInvalidPresetFound = []
