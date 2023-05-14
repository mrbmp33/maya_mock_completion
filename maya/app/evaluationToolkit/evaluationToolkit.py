"""
This module contains the UI code for the Evaluation Toolkit.

It also holds several utility methods that are used by the tool.

import maya.app.evaluationToolkit.evaluationToolkit as et
et.OpenEvaluationToolkitUI()
"""

from maya.app.evaluationToolkit.EvaluationToolkitSectionHUD import EvaluationToolkitSectionHUD
from maya.debug.emPerformanceTest import emPerformanceTest
from maya.debug.TODO import TODO
from maya.common.ui import scrollableMessageBox
from maya.debug.emPerformanceTest import emPerformanceOptions
from functools import partial
from maya.debug.em_debug_utilities import convert_exception_to_unicode
from maya.debug.emModeManager import emModeManager
from maya.debug.emCorrectnessTest import emCorrectnessTest
from maya.debug.frozenUtilities import list_frozen
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import section_layout
from maya.plugin.evaluator.EvaluationToolkitSectionCaching import EvaluationToolkitSectionCaching
from maya.common.ui import showMessageBox
from maya.common.ui import callback_tool
from maya.debug.EvaluatorManager import EvaluatorManager
from maya.app.evaluationToolkit.EvaluationToolkitSectionDebugging import EvaluationToolkitSectionDebugging
from maya.debug.GraphVizManager import GraphVizManager
from maya.app.evaluationToolkit.evaluation_toolkit_utilities import set_gpu_override_active
from maya.common.ui import LayoutManager
from maya.debug.frozenUtilities import unfreeze_nodes
from maya.plugin.evaluator.CacheUiToolkit import CacheUiToolkit
from functools import wraps

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EvaluationToolkit(object):
    """
    This is the main UI class for the Evaluation Toolkit.
    
    It handles creation of the UI and provides various callbacks to handle
    user interactions.
    """

    def __init__(self, windowName="'evaluationToolkitWindowId'"):
        """
        Simple constructor.
        
        It does not create the UI.  UI creation is deferred until create() is
        called
        """
        pass

    def create(self):
        """
        This method completely builds the UI.  It shows the resulting window
        when it is fully created.
        """
        pass

    def updateUI(self):
        """
        This method performs a full UI refresh.
        """
        pass

    __dict__ = None

    __weakref__ = None


class dotFormatting(object):
    """
    Helper class to provide DOT language output support.
    """

    def __init__(self):
        """
        Initialize the allowed cluster color list and current color index.
        """
        pass

    def subgraphHeader(self, label):
        """
        Create a DOT subgraph with the given format information
        """
        pass

    @staticmethod
    def colorFormat(color):
        """
        Returns a string with DOT formatting information for a colored shape
        """
        pass

    @staticmethod
    def connection(srcNode, dstNode, connectionFormat="''", indent='1'):
        """
        Mark a connection between two DOT nodes
        """
        pass

    @staticmethod
    def ellipseFormat():
        """
        Returns a string with DOT formatting information for a simple ellipse shape
        """
        pass

    @staticmethod
    def filledFormat(color='(0.0, 0.5, 1.0)'):
        """
        Returns a string with DOT formatting information for a simple filled greenish-blue shape
        """
        pass

    @staticmethod
    def footer():
        """
        Closes out the body section
        """
        pass

    @staticmethod
    def header():
        """
        Print out a header defining the basic sizing information
        """
        pass

    @staticmethod
    def node(node, nodeFormat="''", indent='1'):
        """
        Creates a DOT node with the given format information
        """
        pass

    @staticmethod
    def subgraphFooter():
        """
        Close out the subgraph section
        """
        pass

    __dict__ = None

    __weakref__ = None


def updateUI_05_Dynamics(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def callback_12_PrintSchedulingForTypesOfNodes(tool): pass


def updateUI_04_CustomEvaluators(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def callback_11_UpdateDownstreamFreezeMode(tool):
    """
    Update the downstream freeze option to match the new value
    """
    pass


def getCycleCluster(name):
    """
    Find the cycle cluster a node is involved in, if any.
    
        name: Name of node to check
    """
    pass


def runEMPerformanceTest():
    """
    Run the emPerformanceTest on the current scene. The resulting
    output will be shown in the script editor window.
    
    The raw performance data consists of two rows, the first containing the
    names of the data collected and the second consisting of the values
    for each data collection item.
    
    This raw list is filtered so that only the most useful data is shown.
    This includes the frames per second for playback in each of DG, EMS,
    and EMP modes. For the unfiltered results see the emPerformanceTest
    script.
    """
    pass


def callback_04_ShowHelpEvaluator(tool, evaluator): pass


def isGPUOverrideActive():
    """
    This method returns True if the OpenCL evaluator is active, False
    otherwise.
    """
    pass


def callback_11_UpdateUpstreamFreezeMode(tool):
    """
    Update the upstream freeze option to match the new value
    """
    pass


def callback_scriptJob_customEvaluatorChanged(tool):
    """
    Update the UI since the list or state of custom evaluators may have changed
    """
    pass


def callback_CFG_PrintGraphvizVersion(tool): pass


def clear_09_Validation(tool):
    """
    Clear out all of the current results; should only happen when a new file is loaded
    """
    pass


def callback_11_UpdateFreezeInvisibleDisplayLayers(tool):
    """
    Update the freeze invisible display layer option to match the new value
    """
    pass


def callback_08_SelectNode(tool, textfield): pass


def callback_11_UpdateFreezeExplicitPropagation(tool):
    """
    Update the freeze explicit propagation option to match the new value
    """
    pass


def callback_05_UpdateDynamicsOptions(tool, option): pass


def callback_01_UpdateEvaluationMode(tool): pass


def callback_04_setEvaluatorActive(tool, evaluator, state): pass


def printReportExpressions():
    """
    This method prints a report about expression nodes in the scene.
    """
    pass


def require_evaluation_graph(func):
    """
    This decorator makes sure that the given function will have a valid
    evaluation graph.
    """
    pass


def getShortestPath(nodes, startNode, endNode):
    """
    Return the chain of nodes forming the shortest path between two nodes.
    
        nodes     : the list of allowed nodes in which the search can be performed.
        startNode : the node from which to start looking for the shortest path.
        endNode   : the node to which the shortest path must go.
    """
    pass


def isControllerPrepopulateActive():
    """
    This method returns True if the controllers are set to prepopulate the
    graph, False otherwise.
    """
    pass


def setControllerPrepopulateActive(state):
    """
    This method activates or deactivates the controller prepopulation of the
    graph.
    """
    pass


def callback_07_SelectDownStreamNodes(*args, **kwargs): pass


def callback_11_PrintFrozenNodes(tool): pass


def callback_scriptJob_uiDeleted(tool):
    """
    Remove all of the scriptJobs being used by this window
    """
    pass


def callback_09_RunCorrectnessTest(tool): pass


def callback_08_GenerateDependenciesGraph(*args, **kwargs): pass


def callback_scriptJob_freezeOptionsChanged(tool):
    """
    Update the UI since the state of freeze options may have changed
    """
    pass


def callback_01_UpdateControllerPrepopulate(tool): pass


def callback_08_RefreshCycleClusters(*args, **kwargs): pass


def getReports():
    """
    Return a list of reports.
    """
    pass


def getCustomEvaluatorClusters(evaluator):
    """
    Get the clusters for a given custom evaluator, if any.
    """
    pass


def callback_12_RefreshNodeTypes(tool): pass


def setEvaluationManagerMode(mode):
    """
    This method sets the current evaluation mode.
    """
    pass


def printDeformerClusters():
    """
    Print out any clusters of nodes captured by the deformer evaluator.
    """
    pass


def getEvaluationGraph(attributes, allObjects='False'):
    """
    Get the evaluation graph, if any.
    
        attributes: Attributes to retrieve from the evaluation graph.
                    Can be 'nodes', 'plugs', 'connections' or a list of those.
                    See the documentation for graph operator in dbpeek command.
        allObjects: True to force to get all objects instead of selection.
    """
    pass


def callback_10_RunReports(tool): pass


def callback_04_PrintEvaluatorInfo(tool, evaluator): pass


def callback_01_UpdateIdleAction(tool): pass


def callback_12_SetSchedulingForTypesOfNodes(tool): pass


def get_graphviz_manager(tool):
    """
    Helper function to get a GraphVizManager with the current settings
    """
    pass


def getSchedulingTypeOverride(nodeType):
    """
    Return a string describing the scheduling type override for this node type.
    """
    pass


def setSchedulingTypeOverride(nodeType, schedulingInfo):
    """
    Set the scheduling type override of the given node type.
    
    The scheduling info is an array of flags for scheduling type to set to true.
    """
    pass


def callback_11_UpdateFreezeInvisibleNodes(tool):
    """
    Update the freeze invisible option to match the new value
    """
    pass


def open_file(file_name):
    """
    Open up an output file with the application assigned to it by the OS.
    
    :param file_name: File to be opened up (usually a PDF or DOT file but can be any recognized format)
    """
    pass


def setIdleAction(idleAction):
    """
    This method sets the current idle action.
    """
    pass


def OpenEvaluationToolkitUI():
    """
    This method is the entry point of the Evaluation Toolkit.
    
    It creates the Evaluation Toolkit window and brings it up.
    """
    pass


def setEvaluatorActive(evaluator, state):
    """
    This method activates or deactivates the given evaluator.
    """
    pass


def callback_scriptJob_dbTraceChanged(tool):
    """
    Update the UI since the list or state of available trace objects may have changed
    """
    pass


def callback_11_UnfreezeAllFrozenNodes(tool): pass


def callback_05_UpdateDynamicsMode(tool): pass


def updateUI_08_Cycles(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def callback_12_PrintSchedulingForTypes(tool): pass


def updateUI_07_Selection(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def updateUI_01_Mode(self): pass


def getEvaluationManagerNodes():
    """
    Get the nodes under evaluation manager control.
    """
    pass


def getCycleClusters(nodes):
    """
    Get the clusters for cycles, if any.
    
        nodes: Nodes to test for cycles
    """
    pass


def runEMCorrectnessTest():
    """
    Run the emCorrectnessTest on the current scene. The resulting
    output will be shown in the script editor window.
    """
    pass


def callback_08_GenerateCycleGraph(*args, **kwargs): pass


def updateUI_09_Validation(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def callback_12_PrintSchedulingUsedForNodes(*args, **kwargs): pass


def callback_11_SelectFrozenNodes(tool): pass


def callback_06_PrintDeformerClusters(*args, **kwargs): pass


def callback_08_GenerateFullGraph(*args, **kwargs): pass


def callback_04_GetEvaluatorInfo(tool, evaluator):
    """
    Return the evaluator's info value
    :param tool: The evaluation toolkit manager
    :param evalatuor: The name of the evaluator whose information is to be returned
    """
    pass


def callback_07_SelectNodesUnderEvaluationManagerControl(*args, **kwargs): pass


def callback_04_GetClaimedNodes(tool, evaluator):
    """
    Return the nodes currently claimed by the given evaluator in a human-readable format
    :param tool: The evaluation toolkit manager
    :param evaluator: The name of the evaluator whose claimed nodes are requested
    Nodes are grouped by cluster in which the evaluator has claimed them
    """
    pass


def callback_04_ShowEvaluatorNodes(tool, evaluator):
    """
    Callback when the button to show the nodes claimed by a given evaluator was pressed.
    Opens up a window with the set of claimed nodes.
    :param tool: The evaluation toolkit manager
    :param evaluator: The name of the evaluator whose claimed nodes are requested
    """
    pass


def callback_01_UpdateGPUOverride(tool): pass


def setManipulationActive(state):
    """
    This method activates or deactivates manipulation using the evaluation
    manager.
    """
    pass


def callback_08_SelectCycleBasedOnSelection(*args, **kwargs): pass


def printReportPerformance():
    """
    This function prints a report about performance problems that were detected
    in the scene. It prints the results given by calling
    cmds.sceneLint()
    """
    pass


def dumpClusterToDot(fileName, nodesInCycle, nodesToMark, shortestPathInfo):
    """
    Take all of the nodes in a cycle cluster and dump them out in
    a DOT graph format to the named file.
    
        nodesInCycle     : List of the nodes involved in the cycle
        fileName         : Name of output file
        shortestPathInfo : A tuple with a source and destination node between
                           which to highlight the shortest path, or None not
                           to highlight.
                           The first element of the tuple is a (source,
                           destination) node pair; the second element is a
                           boolean to indicate if only the shortest path should
                           be in the graph.
    """
    pass


def callback_07_SelectUpStreamNodes(*args, **kwargs): pass


def callback_12_SetSchedulingForTypes(tool): pass


def callback_11_UpdateFreezeRuntimePropagation(tool):
    """
    Update the freeze runtime propagation option to match the new value
    """
    pass


def getEvaluationManagerMode():
    """
    This method returns the current evaluation manager mode.
    """
    pass


def updateUI_10_Reports(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def selectNodesUnderEvaluationManagerControl():
    """
    Scan the entire evaluation graph and select all DG nodes appearing in it.
    """
    pass


def callback_08_SelectNodes(tool, textScrollList): pass


def callback_06_PrintChains(*args, **kwargs): pass


def callback_06_PrintMeshes(*args, **kwargs): pass


def callback_01_UpdateManipulation(tool): pass


def callback_06_PrintSelected(*args, **kwargs): pass


def callback_scriptJob_deleteAll(tool):
    """
    Update the UI since all objects have been deleted
    """
    pass


def updateUI_00_Viewport(self): pass


def isManipulationActive():
    """
    This method returns True if the evaluation manager is used for
    manipulation, False otherwise.
    """
    pass


def getAllCustomEvaluatorsClusters():
    """
    Get the clusters for all custom evaluators, if any.
    """
    pass


def dumpDependenciesBetweenToDot(fileName, upstreamNodes, downstreamNodes):
    """
    Take all the dependencies between a set of upstream nodes and downstream
    nodes and dump them out in a DOT graph format to the named file.
    
        fileName        : Name of output file
        upstreamNodes   : Set of upstream nodes in the evaluation graph
        downstreamNodes : Set of downstream nodes in the evaluation graph
    """
    pass


def selectNextNodes(upstream='True'):
    """
    Select all nodes upstream or downstream from the current selection that are
    currently under evaluation manager control.
    """
    pass


def getIdleAction():
    """
    This method returns the current idle action
    """
    pass


def updateUI_06_GPUOverride(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def isEvaluatorActive(evaluatorName):
    """
    This method returns True if the given evaluator is active, False otherwise.
    """
    pass


def getShortestPaths(nodes, startNode, endNode='None'):
    """
    Return a dictionary which associates each node with its previous node in the shortest path from startNode.
    
    If endNode is specified, the algorithm will stop when the shortest path to endNode is found.
    Then the dictionary is only guaranteed to hold nodes on this path.
    
        nodes     : the list of allowed nodes in which the search can be performed.
        startNode : the node from which to start looking for the shortest path.
        endNode   : the node for which to stop the search, or None to search for all nodes.
    """
    pass


def callback_09_RunPerformanceTest(tool): pass


def updateUI_11_FreezeOptions(self):
    """
    Update the UI configuration for the freeze options based on current state
    """
    pass


def updateUI_12_Scheduling(self):
    """
    # ----------------------------------------------------------------------
    """
    pass


def callback_08_ListNodesInCycleCluster(tool): pass


def dumpEvaluationGraphToDot(fileName):
    """
    Take all of the nodes in the evaluation graph and dump them out in
    a DOT graph format to the named file.
    
        fileName : Name of output file
    """
    pass


BUTTON_WIDTH = 100

kSelectLabel = []

kSectionCaching = 'Caching'

kIdleActions = []

kGroupLabelWidth = 140

kCorrectnessModeNames = {}

kFreezeDownstreamModes = []

COLUMN_SPACING = 10

kDynamicsOptions = []

kTextNumberWidth = 30

kNodeNotInCluster = []

kPathTextFieldWidth = 300

kPerformanceModeNames = []

kNodeOptions = []

kProcessTypes = []

kPrintLabel = []

ROW_SPACING = 4

kSectionDebugging = 'Debugging'

kUIRateFmt = []

kRunLabel = []

kGenerateLabel = []

kTestNotRun = []

kActionOptions = []

kOpenLabel = []

kFreezeUpstreamModes = []

kSchedulingTypes = []

kRemoveLabel = []

kEvaluationManagerModes = []

kSectionHUD = 'HUD'

kDynamicsModes = []

FILE_TEXT_FIELD_WIDTH = 150

kSetLabel = []

kShowLabel = []
