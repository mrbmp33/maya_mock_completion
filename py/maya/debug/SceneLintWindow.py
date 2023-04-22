from maya.common.ui import callback_tool
from maya.common.ui import setClipboardData
from maya.debug.DebugTrace import DebugTrace
from functools import partial
from maya.common.ui import LayoutManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class SceneLintWindow(DebugTrace):
    """
    Class that manages the sceneLint UI. The window is an interface to the information
    provided by the sceneLint command, including the ability to run Python code it
    generates to help in optimizing a scene.
    
    :member all_issues_checkbox: Name of the "All" checkbox widget in the issue list
    :member issue_checkboxes:    {ISSUE_NAME: WIDGET} dictionary of checkbox widget names
    :member issue_descriptions:  {ISSUE_NAME: DESCRIPTION} dictionary of issue description strings
    :member issue_frame_layouts: {ISSUE_NAME: WIDGET} dictionary of issue frame layout widget names
    :member issue_results:       {ISSUE_NAME: MITIGATIONS} found by the most recent run, as
                                 defined by the sceneLint command. If an issue is missing then assume
                                 the test has not been run at all. If any mitigations are None then that
                                 specific issue test ran with no problems.
    :member issue_mitigation_widgets: { ISSUE_NAME : MITIGATION_WIDGETS } dictionary of widgets used to build up mitigation UI for an issue
                                            MITIGATION_WIDGETS = { KEY_LAYOUT|KEY_SELECT|KEY_INFO : WIDGET, KEY_TYPE : VALUE_CHECKBOX|VALUE_TEXTSCROLL }
                                                                 dictionary of widget information for the currently selected mitigation.
                                                                 KEY_LAYOUT:     The mitigation information layout control
                                                                 KEY_SELECT:     The selection widget (either a checkbox or a textScrollList)
                                                                 KEY_INFO:       The symbolButton widget to which the mitigation description is attached
                                                                 KEY_TYPE:       Which type of selection control is used. None means nothing is selectable
                                                                 KEY_MITIGATION: The mitigation dictionary to which the widget is attached
    :member script_job_id: ID of the job that is monitoring file read and new
    :member main_layout: UI name of the main layout inside the window (for rebuilding)
    :member window_name: UI name of main window
    """

    def __init__(self): pass

    def build_mitigation_widgets(self, issue_name, mitigation):
        """
        Build the widget that allows the user to select any number of objects on the mitigation
        object list.
        :param issue_name: Name of the issue to which this mitigation applies
        :param mitigation: Dictionary of information data.
                KEY_NAME        (mandatory)  Short name of the mitigation
                KEY_DESCRIPTION (mandatory)  Description of what it does
                KEY_BENEFIT     (mandatory)  Benefit applying the fix should bring
                KEY_CODE        (optional)   Code to apply the fix automatically
                KEY_OBJECTS     (optional)   Objects to pass to the code
        """
        pass

    def deselect_all_mitigation_objects(self, issue_name):
        """
        Helper method to deselect all of the objects under a particular issue/mitigation combination
        :param issue_name: Name of the lint issue under which the mitigation appears
        """
        pass

    def fix_selected_results(self, issue_name):
        """
        Apply the selected fixes for the given issue
        :param issue_name: Name of the lint issue under which the mitigation appears
        """
        pass

    def get_mitigation_code(self, issue_name):
        """
        Utility to take the given issue with repair code and construct the
        full code including the loop over all selected items (if applicable).
        
        This loops over all potential mitigations to allow for combinations
        of different mitigations on different objects to be selected.
        
        It does not try to filter multiple mitigations applied to the same
        object as that may be intentional in some cases.
        
        :param issue_name: Name of the lint issue under which the mitigation appears
        :return: The string implementing the code that fixes the selected objects for this mitigation
        """
        pass

    def populate_issue_results(self):
        """
                Update the status of all of the sceneLint issues.
                Issue results have these different states:
                    - Idle (Not Run and Not Selected)
                    - Ready (Not Run and Selected)
                    - Okay (Run and no issues found)
                    - Error (Run and some issues found)
        
                if the results are None then no issues have been run:
                    Idle/Ready
                else if an issue is not in the results:
                    Idle/Ready
                else if the issue results are None:
                    Okay
                else if the issue results are {}:
                    Okay
                else:
                    Error
        
                If the results are None then all issues are in the "Not Run" state.
        "nurbs-tessellation": {
                    "description": "Ensure NURBS are tessellated efficiently.",
                    "mitigation": [
                        {
                            "name": "enable-aruba",
                            "description": "Load the 'Aruba' plug-in to handle the tessellation.",
                            "benefit": "Increases the speed at which NURBS curves and surfaces are tessellated for drawing.",
                            "code": "import maya.cmds as cmds
        cmds.loadPlugin('ArubaTessellator')
        "
                        }
                    ]
                },
        """
        pass

    def select_all_mitigation_objects(self, issue_name):
        """
        Helper method to select all of the objects under a particular issue/mitigation combination
        :param issue: Name of the lint issue under which the mitigation appears
        """
        pass

    def show_window(self):
        """
        If the window already exists then pop it up, otherwise create it
        and then pop it up. The window's contents are not sync'd with the
        outside world so it's possible to have references to files or
        directories that no longer exist in the window.
        
        Returns the name of the window.
        """
        pass

    @staticmethod
    def callback_clear_results(tool):
        """
        Callback invoked from the button to clear the current results.
        Does not change the selection status of any of the results.
        """
        pass


READY_TO_RUN = []

READY_COLOUR = []

BENEFIT = []

SELECT_ALL = []

KEY_LAYOUT = '__LAYOUT__'

KEY_OBJECTS = 'objects'

CODE = []

RESULTS_NONE = []

KEY_CODE = 'code'

KEY_INFO = '__INFO__'

KEY_MAIN = 'sceneLint'

VALUE_TEXTSCROLL = '__TEXTSCROLL__'

KEY_SELECT = '__SELECT__'

RESULTS_ERRORS = []

KEY_NAME = 'name'

ERROR_COLOUR = []

KEY_BENEFIT = 'benefit'

OKAY_COLOUR = []

VALUE_CHECKBOX = '__CHECKBOX__'

NO_CODE = []

STANDBY_COLOUR = []

RESULTS_OKAY = []

KEY_TYPE = '__TYPE__'

DESCRIPTION = []

WINDOW_NAME = 'SceneLintWindow'

KEY_DESCRIPTION = 'description'

KEY_MITIGATION = 'mitigation'

SELECT_NONE = []
