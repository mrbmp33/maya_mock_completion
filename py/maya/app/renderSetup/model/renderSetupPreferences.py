from distutils.dir_util import copy_tree

if False:
    from typing import Dict, List, Tuple, Union, Optional


class IncludeAllLightsSettingContextManager:
    """
    Make sure to update visible layer membership when the value of
    the setting include all lights changes during a set/unset of the
    optionVar or the envVar.
    """

    def __enter__(self): pass

    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def __init__(self): pass

    @staticmethod
    def updateVisibleLayerMembership(): pass


class DisplayRSNodesSettingContextManager:
    """
    Make sure to change the visibility of render setup nodes in editors
    if needed during a set/unset of the corresponding optionVar or envVar.
    """

    def __enter__(self): pass

    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def __init__(self): pass


class BaseSetting(object):
    """
    Accessor and mutator class methods to be used by derived classes
    for various Render Setup Options/Settings.
    All of those Render Setup Options have to implement their own boolean
    variables kEnvVar, kOptionVar and kDefault to be derived properly from this
    base class.
    Manipulate the environment and option variables that toggle
    the setting on or off. If an environment variable is set, we
    ignore the option variable.
    Else, take care of toggling the setting on or off when asked.
    This class should be considered abstract and should not be used as is
    (only the derived classes are usable), hence why its variables are None.
    """

    def __init__(self):
        """
        # No need for an instance of this class, it is only encapsulating methods to
        # access and set various settings. (this is to make pylint happy)
        """
        pass

    @classmethod
    def getEnvVar(cls):
        """
        " Return the value of the environment variable
        or None if it is unset. The user can use an environment variable
        to override user preferences and enable/disable the setting.
        """
        pass

    @classmethod
    def getOptionVar(cls): pass

    @classmethod
    def hasEnvVar(cls): pass

    @classmethod
    def hasOptionVar(cls): pass

    @classmethod
    def isEnabled(cls):
        """
        Return whether or not the setting is enabled according
        to the corresponding environment variable or user preference
        """
        pass

    @classmethod
    def setEnvVar(cls, val): pass

    @classmethod
    def setOptionVar(cls, val): pass

    @classmethod
    def toggleOptionVar(cls): pass

    @classmethod
    def unsetEnvVar(cls): pass

    @classmethod
    def unsetOptionVar(cls): pass

    __dict__ = None

    __weakref__ = None

    kDefault = None

    kEnvVar = None

    kOptionVar = None


class DisplayRSNodesSetting(BaseSetting):
    """
    Accessor and mutator static/class methods for
    Display Render Setup Nodes setting.
    By default, we hide render setup nodes from the editors.
    """

    @classmethod
    def setEnvVar(*args, **kwargs): pass

    @classmethod
    def setOptionVar(*args, **kwargs): pass

    @classmethod
    def unsetEnvVar(*args, **kwargs): pass

    @classmethod
    def unsetOptionVar(*args, **kwargs): pass

    kDefault = False

    kEnvVar = 'MAYA_RENDER_SETUP_DISPLAY_RS_NODES'

    kOptionVar = 'renderSetup_displayRSNodes'


class IncludeAllLightsSetting(BaseSetting):
    """
    Accessor and mutator static/class methods for
    Include All Lights setting.
    """

    @classmethod
    def setEnvVar(*args, **kwargs): pass

    @classmethod
    def setOptionVar(*args, **kwargs): pass

    @classmethod
    def unsetEnvVar(*args, **kwargs): pass

    @classmethod
    def unsetOptionVar(*args, **kwargs): pass

    kDefault = True

    kEnvVar = 'MAYA_RENDER_SETUP_INCLUDE_ALL_LIGHTS'

    kOptionVar = 'renderSetup_includeAllLights'


class AlwaysListVisibleLayerSetting(BaseSetting):
    """
    Accessor and mutator static/class methods for
    Always list visible layer setting.
    """

    @classmethod
    def addOptionChangeObserver(cls, obsMethod): pass

    @classmethod
    def getEnvVar(cls): pass

    @classmethod
    def hasEnvVar(cls): pass

    @classmethod
    def hasOptionChangeObserver(cls, obsMethod): pass

    @classmethod
    def removeOptionChangeObserver(cls, obsMethod): pass

    @classmethod
    def setEnvVar(cls, val): pass

    @classmethod
    def setOptionVar(cls, val): pass

    kDefault = True

    kOptionVar = 'renderSetup_alwaysListVisibleLayer'

    optionChangeObservable = None


class ExportRenderSettingsAOVs(BaseSetting):
    """
    Accessor and mutator static/class methods for
    Export Render Settings AOVs.
    """

    @classmethod
    def isEnabled(cls):
        """
        Return whether or not the setting is enabled according
        to the corresponding environment variable or user preference
        """
        pass

    @classmethod
    def setToggled(cls, value):
        """
        When the user checks/unchecks the box this value will update.
        This value will override environment variables temporarily.
        """
        pass

    kDefault = True

    kEnvVar = 'MAYA_RENDER_SETUP_DISABLE_RENDER_SETTINGS_AOVS_EXPORT'

    kOptionVar = 'renderSetup_exportRenderSettingsAOVs'

    kToggled = False


class UntitledCollectionsSetting(BaseSetting):
    """
    Accessor and mutator static/class methods for
    Untitled Collections setting.
    """

    kDefault = True

    kEnvVar = 'MAYA_RENDER_SETUP_USE_UNTITLED_COLLECTIONS'

    kOptionVar = 'renderSetup_useUntitledCollections'


def getUserPresetsDirectory(): pass


def getGlobalTemplateDirectory(): pass


def _getUserDirectory(userDirectoryOptionVar, defaultUserDirectoryName): pass


def _getGlobalDirectory(globalDirectoryOptionVar): pass


def getEditMode(): pass


def getGlobalTemplateDirectoryWithoutCheck():
    """
    For asynchronous purpose, we want to check if the path
    really exists AFTER getting the path string
    """
    pass


def getGlobalPresetsDirectory(): pass


def initialize(): pass


def displayRSNodesSettingDecorator(f):
    """
    Use the DisplayRSNodesSetting's context manager.
    """
    pass


def setEditMode(value): pass


def includeAllLightsSettingDecorator(f):
    """
    Use the IncludeAllLightsSetting's context manager.
    """
    pass


def getUserTemplateDirectory(): pass


def getFileExtension(): pass


kOptionVarUserTemplateDirectory = 'renderSetup_userTemplateDirectory'

kOptionVarUserPresetsDirectory = 'renderSetup_userPresetsDirectory'

kOptionVarGlobalTemplateDirectory = 'renderSetup_globalTemplateDirectory'

kOptionVarEditMode = 'renderSetup_editMode'

kOptionVarGlobalPresetsDirectory = 'renderSetup_globalPresetsDirectory'

kGlobalPresetsPathInvalid = []

kGlobalTemplatePathInvalid = []
