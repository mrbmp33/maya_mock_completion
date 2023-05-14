from maya.common.ui import callback_tool
from maya.plugin.evaluator.CacheUiTimesliderPreferences import CacheUiTimesliderPreferences
from maya.common.utils import Singleton
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_preferences import cache_preferences_initialize
from maya.plugin.evaluator.CacheUiBase import CacheUiBase
from maya.plugin.evaluator.CacheUiFullLayout import CacheUiFullLayout

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheUiPreferencesTab(CacheUiBase):
    """
    Class to manage the UI for the cached playback tab in the preferences window.
    The main reason this has to be its own class is that the tabLayout command does not
    support making children invisible (and if you make the child invisible directly then
    it just makes the frame invisible, leaving the tab itself visible).
    
    Only one of these can exist at a time, however the names of the widgets around it
    may change if, for example, the preferences window closes and re-opens. For that reason
    all initialization is done in the create_ui method.
    
    :member widgets: Set of widgets used to manage the various UI components
    :member prefs_window: Name of the preferences window
    :member prefs_template: Name of the template the preferences window uses
    :member text_scroll_widget: Name of the textScrollList control in which the cache preferences item lives
    :member text_scroll_index: Index of the cache preferences item within the textScrollList
    """

    def __init__(self):
        """
        Initialize the toolkit widgets to be empty initially
        """
        pass

    def create_frame(self):
        """
        Create the frame in which the cache preferences tab will live.
        """
        pass

    def create_list_entry(self, prefs_window, text_scroll_widget, text_scroll_index, new_state='None'):
        """
        Create the textScrollList entry from which the cached playback is enabled
        :param text_scroll_widget: Name of the textScrollList control in which the cache preferences item lives
        :param text_scroll_index: Index of the cache preferences item within the textScrollList
        :param new_state: New plugin load state. If None then read from the evalutor
        """
        pass

    def create_ui(self, prefs_template):
        """
        Creates the Cached Playback frame that is part of the preferences window tabs.
        :param prefs_template: Name of the template the preferences window uses
        :return: Title to show when the cache preferences tab is visible
        """
        pass

    def plugin_state_change(self, new_state):
        """
        Called when the plug-in state changed to loaded or unloaded. Updates the UI appearance to
        reflect the new state.
        As tabLayouts do not have the ability to make their children invisible the
        entire child has to be deleted and added back on unload and load.
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    def update_ui(self):
        """
        Updates the Cached Playback frame that is part of the preferences window tabs.
        """
        pass

    @staticmethod
    def callback_ui_deleted(tool):
        """
        Invoked when the entire preference window is deleted - cleans up the class variables and client monitoring.
        :param tool: CacheUiPreferencesTab object attached to the UI that was deleted
        """
        pass

    ID_ROOT = 'prefCachingColumn'


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to debugging information
    """
    pass


CP_DBG = None
