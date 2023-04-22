from maya.plugin.evaluator.cache_preferences import *

from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceHud
from maya.common.ui import callback_tool
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceResourceGuard
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceDiscardFramesOutOfRange
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceShowWarningMessages
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceMemoryThreshold
from maya.common.ui import LayoutManager
from maya.plugin.evaluator.CacheUiBase import CacheUiBase

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheUiFullLayout(CacheUiBase):
    """
    Class managing the cache preferences UI.
    
    :member preferences: CachePreferences object that handles updating the actual preference values
    :member ui_key: Unique identifier for this UI object. Used for smart deletion from CONTROLS dictionary
    :member widgets: Dictionary of widgets used by the UI (KEY=widget_id, VALUE=ui control name)
    :member mode_change_job: scriptJob ID for the customEvaluatorChanged callback
    """

    def __init__(self, ui_key):
        """
        Initialize the cache preferences UI with a specific parent control.
        There is no reason to create this class without having a UI to be controlled
        so the setup of the actual UI elements is done right here in the initializer.
        :param ui_key: Unique identifier for this set of controls.
        """
        pass

    def plugin_state_change(self, new_state):
        """
        Called when the plug-in state changed to loaded or unloaded. Updates the UI appearance to
        reflect the new state.
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    def update_ui(self):
        """
        Update the state of all of the managed widgets based on the current state of the
        optionVars that drive them. There isn't much benefit to modifying one at a time
        """
        pass

    def update_warning_states(self):
        """
        Update the visibility of the warning icons given the current preference values
        """
        pass

    @staticmethod
    def callback_change_cache_enabled(tool):
        """
        Callback invoked when the enabled state changes. Read the new value for the optionVar,
        set the new state, and update the UI
        """
        pass

    @staticmethod
    def callback_change_cache_fill_direction(tool):
        """
        Callback invoked when the cache fill direction changes.
        Read the new value for the optionVar and set the new state.
        """
        pass

    @staticmethod
    def callback_change_cache_fill_type(tool):
        """
        Callback invoked when the cache fill type changes.
        Read the new value for the optionVar and set the new state.
        """
        pass

    @staticmethod
    def callback_change_cache_mode(tool):
        """
        Callback invoked when the cache mode type changes.
        Read the new value for the optionVar and set the new state.
        """
        pass

    @staticmethod
    def callback_change_prevent_frame_skipping(tool):
        """
        Callback invoked when the prevent-frame-skipping state changes.
        Read the new value for the optionVar and set the new state.
        """
        pass

    @staticmethod
    def callback_change_show_warning_messages(tool):
        """
        Callback invoked when the show-warning-messages state changes.
        Read the new value for the optionVar and set the new state.
        """
        pass

    @staticmethod
    def callback_mode_changed(tool):
        """
        Callback invoked when the evaluation manager state changes.
        """
        pass

    @staticmethod
    def callback_option_var_changed(tool):
        """
        Callback invoked when any of the optionVars affecting the cached playback preferences has changed.
        There are only a few of them and the entire UI has to be redrawn anyway so there is no
        need to provide separate handling for each of the optionVars.
        """
        pass

    @staticmethod
    def callback_ui_deleted(tool):
        """
        :param tool: CacheUiFullLayout object attached to the UI that was deleted
        """
        pass

    @staticmethod
    def callback_update_memory_management(tool):
        """
        Invoked when one of the "stop caching" or "discard frames" checkboxes are pressed or the memory threshold is changed
        """
        pass

    CONTROLS = {}

    ID_ROOT = 'cachedPlaybackMasterControl'

    ID_WARNING_NO_LIMIT = 'cachedPlaybackRAMLimitWarningIcon'

    ID_WARNING_PERCENT = 'cachedPlaybackRAMPercentWarningIcon'


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to the shared debug class output
    """
    pass


def _menu(menu_grp_widget):
    """
    Helper to convert a menu group widget name to its child menu name
    """
    pass


PREFS_MONITORED = []
