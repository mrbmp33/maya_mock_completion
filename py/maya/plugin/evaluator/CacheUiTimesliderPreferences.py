from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceTimesliderBarSpacing
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceShowSubframes
from maya.common.utils import Singleton
from maya.common.ui import callback_tool
from functools import partial
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceShowInvalidatedFrames
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceShowWarningFrames
from maya.common.ui import LayoutManager
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceTimesliderBarPosition
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_preferences import cache_preferences_initialize
from maya.plugin.evaluator.CacheUiBase import CacheUiBase
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceTimesliderBarHeight
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceShowCacheStatus
from maya.plugin.evaluator.cache_preferences import CachePreferenceEnabled

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheUiTimesliderPreferences(CacheUiBase):
    """
    Class to manage the UI for the cache HUD preferences.
    
    :member widgets: Set of widgets used to manage the various UI for the cache HUD state
    """

    def __init__(self):
        """
        Initialize the toolkit widgets to be empty initially
        """
        pass

    def create_ui(self):
        """
        Creates the Cached Playback frame used in the Timeslider preferences window tab.
        """
        pass

    def plugin_state_change(self, new_state):
        """
        Called when the plug-in state changed to loaded or unloaded. Updates the UI appearance to
        reflect the new state.
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    def update_ui(self, plugin_state='None'):
        """
        Update the preferences UI based on the current values of the optionVars
        :param plugin_state: If specified then it is the new plug-in loaded state, otherwise it is read from the evaluator manager
        """
        pass

    @staticmethod
    def callback_ui_deleted(tool, element):
        """
        Invoked when the UI is deleted - cleans up the class variables and client monitoring
        :param tool: CacheUiTimesliderPreferences object attached to the UI that was deleted
        """
        pass

    @staticmethod
    def callback_update_height(value, tool):
        """
        Callback invoked when the cache timeslider bar height changes through the UI
        """
        pass

    @staticmethod
    def callback_update_location(value, location, tool):
        """
        Callback invoked when the cache timeslider bar location changes through the UI
        """
        pass

    @staticmethod
    def callback_update_show_invalidated_frames(value, tool):
        """
        Callback invoked when the cache timeslider invalidated frame display state changes through the UI
        """
        pass

    @staticmethod
    def callback_update_show_subframes(value, tool):
        """
        Callback invoked when the cache timeslider subframe frame display state changes through the UI
        """
        pass

    @staticmethod
    def callback_update_show_warning_frames(value, tool):
        """
        Callback invoked when the cache timeslider warning frame display state changes through the UI
        """
        pass

    @staticmethod
    def callback_update_spacing(value, tool):
        """
        Callback invoked when the cache timeslider bar spacing changes through the UI
        """
        pass

    @staticmethod
    def callback_update_status(value, tool):
        """
        Callback invoked when the status changes through the UI.
        """
        pass

    @staticmethod
    def callback_update_ui(tool):
        """
        Callback to match the visibility of the UI with the plug-in loaded state
        :param tool: CacheUiTimesliderPreferences object to be updated
        """
        pass

    ID_HEIGHT = 3

    ID_POSITION = 2

    ID_ROOT = 0

    ID_SHOW_INVALID = 5

    ID_SHOW_SUBFRAMES = 6

    ID_SHOW_WARNING = 7

    ID_SPACING = 4

    ID_STATUS = 1

    OPTION_VARS_MONITORED = []


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to debugging information
    """
    pass


CP_DBG = None
