from maya.plugin.evaluator.cache_preferences import CachePreferences
from maya.plugin.evaluator.cache_preferences import cache_ui_enabled
from maya.common.ui import callback_tool
from functools import partial
from maya.plugin.evaluator.CacheUiToggle import cache_preferences_menu_item
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_preferences import cache_preferences_initialize
from maya.plugin.evaluator.CacheUiBase import CacheUiBase
from maya.plugin.evaluator.cache_preferences import CachePreferenceMode
from maya.plugin.evaluator.cache_preferences import CachePreferenceEnabled

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheUiMenu(CacheUiBase):
    """
    Class managing the cache preferences submenu within other menus.
    :member widgets: Dictionary of widgets used by the UI (KEY=widget_id, VALUE=ui control name)
    :member parent_menu: Menu control for the TimeSlider menu as a whole
    :member mode_change_job: scriptJob ID for the customEvaluatorChanged callback
    :member ui_key: Unique identifier for this particular menu
    """

    def __init__(self, ui_key):
        """
        Initialize the menu controls
        """
        pass

    def __str__(self):
        """
        Return a useful formatting for all of the information in the menu.
        Not localized as this is only for debugging purposes.
        """
        pass

    def plugin_state_change(self, new_state):
        """
        Called when the plug-in state changed to loaded or unloaded. Updates the UI appearance to
        reflect the new state.
        menuItem controls do not have a visibility attribute so the actual submenu must
        be destroyed or recreated as necessary.
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    @staticmethod
    def callback_set_mode(value, mode):
        """
        Callback when one of the caching mode radio buttons is clicked.
        :param mode: New caching mode to be set (as enum string)
        """
        pass

    @staticmethod
    def callback_toggle_enabled(tool):
        """
        Callback when the enabled checkbox is clicked.
        :param tool: Checkbox menu item widget
        """
        pass

    @staticmethod
    def callback_update_menu(tool):
        """
        Callback to refresh the values of the menu items to match the preferences.
        :param tool: CacheUiMenu object to be updated
        """
        pass

    @staticmethod
    def menu_deleted(tool):
        """
        Callback when the UI is deleted - cleans up the class variables.
        :param tool: CacheUiMenu object attached to the UI that was deleted
        """
        pass

    CONTROLS = {}

    ID_OPEN_PREFS = 'openCachedPlaybackPreferences'

    ID_ROOT = 'cachedPlaybackMasterControl'


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to debugging information
    """
    pass


CP_DBG = None
