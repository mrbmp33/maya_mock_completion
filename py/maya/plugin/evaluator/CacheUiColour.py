from functools import partial
from maya.common.ui import callback_tool
from maya.common.utils import Singleton
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_preferences import cache_preferences_initialize
from maya.plugin.evaluator.CacheUiBase import CacheUiBase
from maya.plugin.evaluator.cache_preferences import CachePreferenceEnabled

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheUiColour(CacheUiBase):
    """
    Class to manage the UI for the cache playback colour preferences.
    
    :member widgets: Set of widgets used to manage the various UI for the cache HUD state
    :member parent:  Parent control of the colour frame
    """

    def __init__(self):
        """
        Initialize the toolkit widgets to be empty initially
        """
        pass

    def create_colour_slider(self, colour_name, colour_label):
        """
        Create an RGB slider corresponding to the colour_name
        :param colour_name: Name of the colour whose slider is to be created
        """
        pass

    def create_frame(self):
        """
        Creates the frame used for the cache colour preferences.
        """
        pass

    def create_opacity_slider(self, colour_name, colour_label):
        """
        Create an opacity slider corresponding to the colour_name
        :param colour_name: Name of the colour whose slider is to be created
        """
        pass

    def plugin_state_change(self, new_state):
        """
        Called when the plug-in state changed to loaded or unloaded. Updates the UI appearance to
        reflect the new state.
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    @staticmethod
    def callback_populate_frame(tool):
        """
        Populates the frame used for the cache colour preferences underneath the parent_control.
        """
        pass

    @staticmethod
    def callback_ui_deleted(tool, element):
        """
        Callback when the UI is deleted - cleans up the class variables.
        :param tool: CachePreferencesHud object attached to the UI that was deleted
        """
        pass

    @staticmethod
    def callback_update_colour(tool, colour_name):
        """
        Invoked when the 'colour_name' colour slider is changed to update the colour value
        """
        pass

    @staticmethod
    def callback_update_frame(tool):
        """
        Updates the contents of the frame used for the cache colour preferences.
        """
        pass

    @staticmethod
    def callback_update_opacity(tool, colour_name):
        """
        Invoked when the 'colour_name' opacity slider is changed to update the opacity value
        """
        pass

    @staticmethod
    def callback_update_ui(tool, plugin_loaded='None'):
        """
        Invoked when the preference value has been altered through some outside agent.
        Updates the various bits of UI to match it. No need to check the plug-in state
        as when it is unloaded the UI is not available for changes.
        :param plugin_loaded: If plug-in load state is known this will be a boolean, else None and it has to be read
        """
        pass

    @staticmethod
    def update_opacity_slider(colour_name):
        """
        Find the opacity slider corresponding to the colour and update its value
        :param colour_name: Name of the colour to be updated
        """
        pass

    @staticmethod
    def update_rgb_slider(colour_name):
        """
        Find the RGB slider corresponding to the colour and update its value.
        :param colour_name: Name of the colour to be updated
        """
        pass

    FRAME_NAME = 'CacheUiColourPrefsFrame'

    ID_FRAME = 'frame'


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to debugging information
    """
    pass


def colour_widget(colour_name):
    """
    :return: Name of the RGB slider widget corresponding to the colour 'colour_name'
    """
    pass


def opacity_widget(colour_name):
    """
    :return: Name of the opacity slider widget corresponding to the colour 'colour_name'
    """
    pass


COLOUR_NAMES = []

OPACITY_NAMES = []

name = 'cachedPlaybackWarningFrames'

CP_DBG = None

COLOUR_INFO = {}

text = []
