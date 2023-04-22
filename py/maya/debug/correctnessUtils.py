"""
It is meant to be used by tests validating the correctness of evaluation, for
instance validating the correctness of evaluation under evaluation manager or
background evaluation.

Its main utility function is run_correctness_test().

If results_path is set then the graph output and differences are dumped to
files using that path as the base name.  For example:

    results_path            = MyDirectory/emCorrecteness_animCone
    reference results dump  = MyDirectory/emCorrecteness_animCone.ref.txt
    reference results image = MyDirectory/emCorrecteness_animCone.ref.png
    ${mode} results dump    = MyDirectory/emCorrecteness_animCone.${mode}.txt
    ${mode} results image   = MyDirectory/emCorrecteness_animCone.${mode}.png

If results_path is not set then no output is stored, everything is live.

The return value is a list of value pairs indicating number of differences
between the reference evaluation and the tested mode. e.g. if you requested 'ems'
mode then you would get back {'ems' : (0, 0, 0)} from a successful comparison.

If file_name is not set then the current scene is analyzed.
"""

from maya.debug.TODO import TODO
from maya.debug.PlaybackManager import PlaybackManager
from maya.debug.DGState import DGState
from maya.debug.emModeManager import emModeManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EmptyContext(object):
    """
    Empty context class that performs no action on entry or exit.
    """

    def __enter__(self):
        """
        Simple entry of empty context
        """
        pass

    def __str__(self):
        """
        Empty context has no parameters
        """
        pass

    @staticmethod
    def __exit__(exit_type, value, traceback):
        """
        Simple exit of empty context
        """
        pass

    @staticmethod
    def should_pull_values():
        """
        :return: True, empty contexts always pull
        """
        pass

    __dict__ = None

    __weakref__ = None


def multichain_nodes():
    """
    The IK multi-chain solver is known to create inconsistent results so remove
    any joints that are being controlled by it from the list being compared.
    Even though we have an evaluator that disables the EM when these are found even
    the DG results are not consistent so these always must be ignored.
    :return: Set of nodes that are affected by the multi-chain solver
    """
    pass


def __is_maya_file(path):
    """
    Check to see if the given path is a Maya file. Only looks for native Maya
    files ".ma" and ".mb", not other importable formats such as ".obj" or ".dxf"
    """
    pass


def __find_em_plugs(relevant_nodes, results_filename):
    """
    Find all of the root level plugs that the EM will be marking
    dirty. The passed-in dictionary will be populated by a list of
    dictionaries.
    
    :param relevant_nodes:  Array of [NODES_TO_INCLUDE]
    
    :return: Dictionary of NODE -> [DIRTY_PLUG_IN_NODE]
    """
    pass


def model_panel_visible():
    """
    Return true if any model panel is currently visible. This includes
    checking for GUI model and looking at the currently visible panels
    to see if any of them are model panels.
    """
    pass


def run_correctness_test(reference_mode, modes, file_name, results_path, verbose, max_frames, data_types, em_setup):
    """
    Evaluate the file in multiple modes and compare the results.
    
    Modes are objects that must contain at least the following methods:
        title   : returns a string describing the mode
        em_mode : returns a string to be passed to emModeManager.setMode()
                  before running the test.
        context : returns a context object that can set extra state on enter
                  and reset it on exit (or None if not needed).
        relevant_nodes : takes a set of potential nodes to use and filters them,
                         returning the subset of those nodes to which the mode is applicable
    
    :param reference_mode: Mode against which the test runs will be compared
    :param modes:          List of modes to run the tests in.
    :param file_name:      Name of file to load for comparison. None means use the current scene
    :param results_path:   Where to store the results. None means don't store anything
    :param verbose:        If True then dump the differing values when they are encountered
    :param max_frames:     Maximum number of frames in the playback, to avoid long tests.
    :param data_types:     List of data types to include in the analysis. These are the possibilities:
                               matrix: Any attribute that returns a matrix
                               vector: Any attribute with type 3Double
                               vertex: Attributes on the mesh shape that hold vertex positions
                               number: Any attribute that returns a number
                               screen: Screenshot after the animation runs
    :param em_setup:       What to do before running an EM mode test, in bitfield combinations
                               CORRECTNESS_NO_SETUP        Do nothing, just run playback
                               CORRECTNESS_DOUBLE_PLAYBACK Run playback twice to ensure graph is valid
                               CORRECTNESS_INVALIDATE      Invalidate the graph to force rebuild
                               CORRECTNESS_LOAD            Load the file between every mode's run
                                                           (Default is to just load once at the beginning.)
    
    :return: a list of value tuples indicating the run mode and the number of
             changes encountered in that mode. e.g. ['ems', 0]
    
    If verbose is true then instead of counts return a list of actual changes.
    e.g. ['ems', ["plug1,oldValue,newValue"]]
    
    Changed values are a CSV 3-tuple with "plug name", "value in reference mode", "value in the named test mode"
    in most cases.
    
    In the special case of an image difference the plug name will be one
    of the special ones below and the values will be those generated by the
    comparison method used:
        DGState.SCREENSHOT_PLUG_MD5 : md5 values when the image compare could not be done
        DGState.SCREENSHOT_PLUG_MAG : md5 and image difference values from ImageMagick
        DGState.SCREENSHOT_PLUG_IMF : md5 and image difference values from imf_diff
    """
    pass


CORRECTNESS_INVALIDATE = 2

CORRECTNESS_DOUBLE_PLAYBACK = 1

CORRECTNESS_LOAD = 4

CORRECTNESS_NO_SETUP = 0

CACHE_EVALUATOR = 'cache'

CORRECTNESS_MAX_FRAMECOUNT = 20
