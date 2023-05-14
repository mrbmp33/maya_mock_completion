from maya.common.ui import callback_tool
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import EvaluationToolkitSection
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import section_layout
from maya.common.ui import LayoutManager
from maya.plugin.evaluator.CacheUiHud import CacheUiHud

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EvaluationToolkitSectionHUD(EvaluationToolkitSection):
    """
    Class providing support for UI and functionality of the evaluation toolkit HUD section.
    """

    def __init__(self, title, start_closed):
        """
        Set up the framework for the HUD controls
        :param title: Name of the main HUD section
        :param get_graphviz_manager: Callback to retrieve a GraphVizManager for use in DOT/PDF file generation
        """
        pass

    def update_ui(self):
        """
        Update the HUD values to match the current optionVar values
        """
        pass

    @staticmethod
    def callback_evaluation_hud_changed(tool):
        """
        Invoked when the evaluation HUD value was changed via the checkbox
        """
        pass

    @staticmethod
    def callback_frame_rate_hud_changed(tool):
        """
        Invoked when the frame rate HUD value was changed via the checkbox
        """
        pass

    @staticmethod
    def callback_update_plugin_state(tool, new_state):
        """
        Callback to match the visibility of the cache HUD with the plug-in loaded state
        :param tool: EvaluationToolkitSectionHUD object to be updated
        :param new_state: True if the plug-in was just loaded, False if just unloaded
        """
        pass

    @staticmethod
    def ui_deleted(tool):
        """
        Callback when the UI is deleted - cleans up the class variables.
        """
        pass


CP_DBG = None
