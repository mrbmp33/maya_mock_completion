from functools import partial
from maya.plugin.evaluator.CacheScriptJobHelper import CacheScriptJobHelper
from maya.common.ui import callback_tool
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceHud
from maya.plugin.evaluator.cache_preferences import cache_preferences_initialize
from maya.plugin.evaluator.CacheUiBase import CacheUiBase
from maya.common.utils import Singleton
from maya.plugin.evaluator.cache_preferences import CachePreferences

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheUiHud(CacheUiBase):
    """
    Class to manage the UI for the cache HUD preferences.
    
    :member widgets: Set of widgets used to manage the various UI for the cache HUD state
    """

    def __init__(self):
        """
        Initialize the toolkit widgets to be empty initially
        """
        pass

    def create_heads_up_display(self, section, label_width, starting_block):
        """
        Creates the HUD elements used by the cache evaluator.
        :param section: Section in which the HUD will appear
        :param label_width: How wide the HUD label should be
        :param starting_block: Block for the first HUD element
        :return: Next block index to use in order to appear after the last caching HUD element
        """
        pass

    def create_hud_menu_item(self, previous_item):
        """
        Creates the menu item used in the Display menu for the cache HUD state.
        :param previous_item: Name of the menuItem appearing above this one in the menu
        """
        pass

    def create_toolkit_button(self):
        """
        Creates the checkbox used for the cache HUD state in the evaluation toolkit.
        """
        pass

    def insert_menu_item(self):
        """
        Put the Display menu HUD cache menuItem into its proper place. This method was
        designed to work both when the menu is initially being populated and when the
        item is being added back to the existing menu.
        """
        pass

    def plugin_state_change(self, new_state):
        """
        Called when the plug-in state changed to loaded or unloaded. Updates the UI appearance to
        reflect the new state.
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    def start_monitoring(self):
        """
        Enable the monitoring of changes to the plug-in state and the preference value.
        This uses a monitor count to allow one or both UI elements to be active at the
        same time and share the callback method that updates whichever of them is active.
        """
        pass

    @staticmethod
    def callback_memory_changed(tool):
        """
        Invoked when the memory usage may have changed and the HUD needs to update.
        """
        pass

    @staticmethod
    def callback_ui_deleted(tool, element):
        """
        Callback when the UI is deleted - cleans up the class variables.
        :param element: Index of UI element that was just deleted
        """
        pass

    @staticmethod
    def callback_update_preference(tool):
        """
        Invoked when the state of the cache HUD checkbox changes. Updates the
        optionVar associated with the cache HUD.
        """
        pass

    @staticmethod
    def callback_update_ui(tool):
        """
        Invoked when the preference value has been altered through some outside agent.
        Updates the various bits of UI to match it. No need to check the plug-in state
        as when it is unloaded the UI is not available for changes.
        """
        pass

    @staticmethod
    def callback_update_visibility(tool):
        """
        Invoked when some external agent could affect the visibility of the widgets.
        e.g. the opening of a frame layout, which automatically makes all children visible
        """
        pass

    HUD_DATA = {}

    HUD_NAMES = []

    ID_MENU = 'menu'

    ID_MENU_ITEM_PARENT = 'menuItemParent'

    ID_PREVIOUS_MENU_ITEM = 'previousMenuItem'

    ID_TOOLKIT = 'toolkit'


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to debugging information
    """
    pass


RUNTIME_TOGGLE_CMD = 'ToggleCacheVisibility'

EVENT_CACHE_DESTROYED = 'cacheDestroyed'

CP_DBG = None
