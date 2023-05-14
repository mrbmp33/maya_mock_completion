if False:
    from typing import Dict, List, Tuple, Union, Optional


def loadUserPreset(preset):
    """
    # Loads the specified user preset.
    """
    pass


def getGlobalPresets(renderer):
    """
    # Returns the list of presets in the global presets directory.
    """
    pass


def getUserPresets(renderer):
    """
    # Returns the list of presets in the user presets directory.
    """
    pass


def loadGlobalPreset(preset):
    """
    # Loads the specified global preset.
    """
    pass


def _exportNodesOfGivenType(encodeFunction, captionName, filePath='None'): pass


def deleteUserPreset(preset, warn='True'):
    """
    # Deletes a user preset. Note: for testing purposes, noWarn can be set to True
    # to prevent a warning popup box on delete, this should only be used for 
    # testing!
    """
    pass


def exportAOVs(captionName, fp='None'): pass


def _selectPath(userTextField, option, title): pass


def addRenderSetupPreferences(): pass


def _syncOptionVarWithTextField(userTextField, option): pass


def setDefaultPreset(): pass


def savePreset(captionName, fp='None'):
    """
    # Saves a preset to a user specified location. Note: for testing purposes, a
    # filename can be passed in, this should only be used for testing!
    """
    pass


def _loadPreset(preset, basePath):
    """
    # Loads the specified preset from the specified directory
    """
    pass


def _getPresets(renderer, basePath):
    """
    # Returns the list of presets in the specified base path.
    """
    pass


kSelectUserPresetsLocation = []

kGlobalTemplatesLocation = []

kSelectGlobalPresetsLocation = []

kDeleteUserRenderSettingsMsg = []

kUserPresetsLocation = []

kCancel = []

kDelete = []

kRenderSettingsPresetsTitle = []

kExportRenderSettings = []

kRenderSetupTemplatesTitle = []

kSelectUserTemplatesLocation = []

kDeleteUserRenderSettings = []

kUserTemplatesLocation = []

kInvalidPresetFound = []

kSelectGlobalTemplatesLocation = []

kGlobalPresetsLocation = []
