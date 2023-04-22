"""
Utility to verify that the background evaluation and caching system are
yielding the same results as the Maya parallel evaluation.

It is a simple wrapper around run_correctness_test().  See its documentation
for more details.

Sample usage to run the tests on a single file:

    from maya.debug.cacheCorrectnessTest import cacheCorrectnessTest
    from maya.plugin.evaluator.CacheEvaluatorManager import CACHE_STANDARD_MODE_EVAL
    cacheErrors = cacheCorrectnessTest(file_name='MyDir/MyFile.ma', results_path='MyDir/cacheCorrectness', modes=[{KEY_CACHE_MODE: CACHE_STANDARD_MODE_EVAL}])

Sample usage to run the tests on the current scene and ignore output:

    from maya.debug.cacheCorrectnessTest import cacheCorrectnessTest
    from maya.plugin.evaluator.CacheEvaluatorManager import CACHE_STANDARD_MODE_EVAL
    cacheErrors = cacheCorrectnessTest(modes=[{KEY_CACHE_MODE: CACHE_STANDARD_MODE_EVAL}])
"""

from maya.debug.correctnessUtils import run_correctness_test
from maya.plugin.evaluator.CacheEvaluatorManager import standard_modes
from maya.debug.correctnessUtils import multichain_nodes
from maya.debug.EvaluatorManager import EvaluatorManager
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.debug.DeformerEvaluatorManager import DeformerEvaluatorManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheCorrectnessContext(object):
    """
    This class configures the cache evaluator according to a set of options and
    shuts off the HIK and GPU deformer evaluators to help isolate correctness errors.
    """

    def __enter__(self):
        """
        Enter the section controlled by the context
        """
        pass

    def __exit__(self, exit_type, value, traceback):
        """
        Exit the section controlled by the context, raising an exception if any restore failed
        """
        pass

    def __init__(self, mode, cache_timeout):
        """
        Create the evaluator managers and remember the desired configuration values
        """
        pass

    def __str__(self):
        """
        :return: a string with information on the managed evaluator's states
        """
        pass

    def should_pull_values(self):
        """
        Ask if the values in this context are good as-is or if they have to be pulled to be valid
        :return: True always - cached values need to be pulled to ensure correctness
        """
        pass

    __dict__ = None

    __weakref__ = None


class CacheCorrectnessMode(object):
    """
    This class represents a mode to be tested in cache correctness tests.
    
    It knows about the cache mode (i.e. what caching point to be enabled).
    
    It always requires the same evaluation mode:
    - Parallel evaluation
    - Cache evaluator enabled
    """

    def __init__(self, cache_mode, cache_timeout): pass

    def context(self):
        """
        Returns the context object that will set up and tear down the required
        caching configuration to be tested.
        """
        pass

    def em_mode(self):
        """
        Returns the evaluation mode in which the cache correctness test must be run.
        """
        pass

    def title(self):
        """
        Returns the identifying string for this cache mode.
        """
        pass

    @staticmethod
    def relevant_nodes(potential_nodes):
        """
        :param potential_nodes: Set of nodes that could be evaluated/compared in the current mode
        :return: a subset of nodes relevant to the defined evaluation caching mode
        """
        pass

    __dict__ = None

    __weakref__ = None


def cacheCorrectnessTest(file_name='None', results_path='None', verbose='False', modes='None', max_frames='20',
                         data_types="['matrix', 'vertex', 'screen']", em_setup='2', cache_timeout='1800'):
    """
    Evaluate the file in multiple caching modes and compare the results.
    
    :param file_name:    Name of file to load for comparison. None means use the current scene.
    :param results_path: Where to store the results. None means don't store anything.
    :param verbose:      If True then dump the differing values when they are encountered.
    :param modes:        List of modes to run the tests in.  A mode is a list of options to activate
                         in the cache system.  See the CacheEvaluatorManager set_state() method for
                         the format it expects for these modes.
    :param max_frames:   Maximum number of frames in the playback, to avoid long tests.
    :param data_types:   List of data types to include in the analysis.
                            See run_correctness_test for the possible values.
    :param em_setup:     What to do before running an EM mode test, in bitfield combinations.
                            See run_correctness_test for the possible values.
    :param cache_timeout: The maximum amount of time to wait for cache to fill.
    
    :return: a list of value tuples indicating the run mode and the number of
             changes encountered in that mode. e.g. ['ems', 0]
    """
    pass


def getModeString(mode):
    """
    Returns the identifying string for this cache mode.
    Temporary function here while QATA is refactored.
    """
    pass


CORRECTNESS_INVALIDATE = 2

MAX_CACHE_TIMEOUT = 1800

KEY_CACHE_MODE = 'cache_mode'

CORRECTNESS_MAX_FRAMECOUNT = 20
