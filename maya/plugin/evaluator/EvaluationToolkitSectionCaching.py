from maya.app.evaluationToolkit.evaluation_toolkit_utilities import set_gpu_override_active
from maya.plugin.evaluator.cache_preferences import CachePreferenceMode
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import EvaluationToolkitSection
from maya.plugin.evaluator.cache_preferences import CachePreferenceEnabled
from maya.common.ui import callback_tool
from maya.plugin.evaluator.cache_ui import cache_ui_full_layout_create
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.plugin.evaluator.cache_ui import cache_ui_full_layout_update
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import section_layout
from maya.plugin.evaluator.cache_preferences import cache_ui_enabled
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceHud
from maya.plugin.evaluator.cache_preferences import CachePreferenceFillType
from maya.plugin.evaluator.CacheUiBase import CacheUiBase
from maya.common.ui import LayoutManager
from maya.debug.DeformerEvaluatorManager import DeformerEvaluatorManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EvaluationToolkitSectionCaching(EvaluationToolkitSection, CacheUiBase):
    """
    Class providing support for UI and functionality of the evaluation toolkit cachign section.
    
    :member ui_key: Unique identifier for this UI object. Used for client notification in CachePreferences()
    :member deformer_mgr: Local DeformerEvaluatorManager for easy access to evaluator parameters
    :member cache_mgr: Local CacheEvaluatorManager for easy access to evaluator parameters
    
    :member layout_root: Root control for everything in this section
    :member layout_actions: Layout control for the section containing action buttons
    :member layout_memory: Layout control for the memory management section
    :member layout_safe_mode: Layout control for the safe mode section
    :member menu_debug_cache_mode_list: Menu widget for debugging cache mode list
    :member checkbox_hybrid_gpu_cache: Checkbox widget for Hybrid GPU cache selection
    :member checkbox_flush_sync: Checkbox widget for whether flushing is synchronous
    :member widget_memory_usage: Text widget showing memory used
    :member widget_memory_available: Text widget showing memory available
    :member mode_change_job: scriptJob ID for the customEvaluatorChanged callback
    """

    def __init__(self, title, start_closed):
        """
        Set up the framework for the caching tools
        :param title: Name of the main caching section
        :param start_closed: True means the section should be initially closed when the UI window is created
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
        Update the UI values to match the current external states
        """
        pass

    @staticmethod
    def callback_apply_debug_cache_mode(tool):
        """
        Callback invoked when one of the custom cache modes was selected. This does not
        affect the mode preferences, it just changes the current caching mode.
        """
        pass

    @staticmethod
    def callback_flush_cache(tool):
        """
        Invoked when the "flush cache" button is pressed
        """
        pass

    @staticmethod
    def callback_invalidate_cache(tool):
        """
        Invoked when the "invalidate cache" button is pressed
        """
        pass

    @staticmethod
    def callback_print_safe_mode_messages(tool):
        """
        Invoked when the "print safe mode messages" button is pressed
        """
        pass

    @staticmethod
    def callback_rebuild_cache(tool):
        """
        Invoked when the "trigger rebuild" button is pressed
        """
        pass

    @staticmethod
    def callback_ui_deleted(tool):
        """
        Callback invoked when the UI was deleted. Clear out all of the local data.
        """
        pass

    @staticmethod
    def callback_update_enabled(tool):
        """
        Callback to refresh the enabled state of the UI to match the cache evaluator state.
        """
        pass

    @staticmethod
    def callback_update_fill_type(tool):
        """
        Callback to refresh the enabled state of the "Rebuild Cache" button to match the cache evaluator fill type.
        """
        pass

    @staticmethod
    def callback_update_flush_cache_synchronously(tool):
        """
        Invoked when the checkbox for how to flush the cache is pressed
        """
        pass

    @staticmethod
    def callback_update_hybrid_gpu_cache(tool):
        """
        Invoked when the Hybrid GPU cache checkbox is pressed
        """
        pass

    @staticmethod
    def callback_update_memory(tool):
        """
        Invoked when the "update memory" button is pressed.  Recalculates and displays current memory usage.
        """
        pass


def _menu(menu_grp_widget):
    """
    Helper to convert a menu group widget name to its child menu name
    """
    pass


def local_dbg(msg):
    """
    Access to the local debugging function, which just prepends the class name to debugging information
    """
    pass


BUTTON_WIDTH = 100

CACHE_STANDARD_MODE_VP2_HW_NO_FALLBACK = []

CP_DBG = None

DEBUG_CACHE_MODES = []

CACHE_STANDARD_MODE_EVAL_SHAPES = []

SHOW_HYBRID_CACHE_GPU = False

CACHE_STANDARD_MODE_VP2_SW_NO_FALLBACK = []

COLUMN_SPACING = 10

ROW_SPACING = 4
