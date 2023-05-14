from maya.debug.emModeManager import emModeManager
from functools import wraps

if False:
    from typing import Dict, List, Tuple, Union, Optional


def expand_to_shapes(input_list):
    """
    Expand an input_list to include all shapes below them in the DAG
    :param input_list: List of nodes for which shapes are to be added
    :return: Input list plus any shapes below transforms that appear in the input_list
    """
    pass


def expand_to_upstream_hierarchy(input_list):
    """
    Traverse upstream through the evaluation graph to find nodes related
    to those in the starting_nodes list.
    :param starting_nodes: Initial nodes from which to go upstream
    :return: Unique list of all nodes upstream from and including the starting_nodes
    """
    pass


def dbg_scheduling_graph(summary_only, include_clusters, use_selection, selection_depth):
    """
    Generate a string representing the scheduling graph structure
    :param summary_only: If True then just summarize the information rather than using JSON format
    :param include_clusters: If True then include the members of each cluster rather than just a membership size
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :return: Scheduling graph structure in string form
    :raise RuntimeError: if the graph was not available
    """
    pass


def open_file(file_name):
    """
    Open up an output file with the application assigned to it by the OS.
    
    :param file_name: File to be opened up (usually a PDF or DOT file but can be any recognized format)
    """
    pass


def get_upstream_set(starting_nodes):
    """
    Find all nodes one step upstream from the starting_nodes
    :param starting_nodes: Initial nodes from which to go upstream
    :return: Unique list of the starting_nodes plus any nodes one step upstream from them
    """
    pass


def select_inverse_visible_dag_objects(original_nodes):
    """
    Create an inverse selection list from the specified original nodes
    """
    pass


def dbg_nodes(summary_only, include_plugs, use_selection, selection_depth):
    """
    Generate a string representing the evaluation graph nodes.
    :param summary_only: If True then just summarize the information rather than using JSON format
    :param include_plugs: If True then include the lists of dirty plugs the evaluation node knows about
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :return: Evaluation node structure in string form, None if the graph was not available
    """
    pass


def dbg_scheduling_types(summary_only, use_selection, selection_depth):
    """
    Generate a string representing the scheduling types of nodes
    :param summary_only: If True then just summarize the information rather than using JSON format
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :return: String containing the scheduling type information
    :raise RuntimeError: if the graph was not available
    """
    pass


def dbpeek_selection_expansion(expansion_type, use_selection, selection_depth, peek_args):
    """
    Take the current configuration and figure out the parameters required by the dbpeek
    command to handle the selection.
    The two selection settings are the All/Selected boolean, and the integer depth. When
    "All" is selected every node is used, otherwise the selection is expanded "depth" steps and
    the expanded selection list is returned (without actually changing the selection).
    
    :param expansion_type: Type of graph for selection expansion, if needed (DG, SG, or DG)
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :param peek_args: Initial arguments in use by the dbpeek command, modified to include
                         any extra arguments required to respect the current selection settings
    
    :return: List of the expanded selection, empty list if using all nodes
    """
    pass


def require_evaluation_graph(func):
    """
    This decorator makes sure that the given function will have a valid
    evaluation graph.
    """
    pass


def dbg_graph(summary_only, include_plugs, use_selection, selection_depth):
    """
    Generate a string representing the evaluation graph nodes and connections.
    :param summary_only: If True then just summarize the information rather than using JSON format
    :param include_plugs: If True then include the lists of dirty plugs the evaluation node knows about
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :return: Evaluation graph structure in string form
    :raise RuntimeError: if the graph was not available
    """
    pass


def get_minimal_scene_objects_from(input_list):
    """
    :param input_list: List of nodes that are required in the minimal scene
    :return: List of nodes required in order to correctly evaluate the nodes in input_list
    """
    pass


def get_default_directory():
    """
    Get a reasonable default directory for temporary output.
    """
    pass


def collapse_lists(list_of_items):
    """
    Convert a list of mixed strings and other iterables to a list of unique items
    :param list_of_items: List consisting of strings, tuples, or other lists to be collapsed
    :return: List consisting of unique strings that were somewhere in the input list structure
    """
    pass


def dbg_scheduling_graph_to_dot(include_clusters, use_selection, selection_depth, out_dot):
    """
    Generate a string representing the evaluation graph nodes and connections in a DOT visualization format.
    :param include_clusters: If True then include the members of each cluster rather than just a membership size
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :param out_dot: File where the .dot format data should go
    :return: Full path to the .dot file location
    :raise RuntimeError: if the graph was not available
    """
    pass


def dbg_graph_to_dot(include_plugs, use_selection, selection_depth, out_dot):
    """
    Generate a string representing the evaluation graph nodes and connections in a DOT visualization format.
    :param include_plugs: If True then include the lists of dirty plugs the evaluation node knows about
    :param use_selection: True if the selection list should be used, otherwise use all nodes
    :param selection_depth: Number of steps from selected nodes to include, if selection is being used
    :param out_dot: File where the .dot format data should go
    :return: Full path to the .dot file location
    :raise RuntimeError: if the graph was not available
    """
    pass


def convert_exception_to_unicode(exception):
    """
    :return: a string representing the exception, in Unicode format.
    
    It handles cases such as when WindowsError exceptions contain Unicode
    characters encoded in a regular string in the OS encoding.  It does
    so in a slightly more generic and robust way by also trying the
    system's locale encoding.
    """
    pass


GRAPH_NOT_AVAILABLE = []

DOWNSTREAM_LINK = '[]-->'

PLUG_TYPES = {}

UPSTREAM_LINK = '-->[]'
