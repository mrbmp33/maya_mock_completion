"""
See the class docs for a description of the data collected.
"""

from maya.analytics.decorators import makeAnalytic
from maya.analytics.BaseAnalytic import BaseAnalytic
from maya.debug.emModeManager import emModeManager
from maya.analytics.decorators import addMethodDocs
from maya.debug.PlaybackManager import PlaybackManager
from maya.analytics.decorators import addHelp
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class analyticCachePerformance(BaseAnalytic):
    """
    The normal output is the set of cache performance statistics.
    
        {
          "baseline"    : {
              "memory"      : [0,0]  // baseline [physical,virtual] memory usage after animation, but before caching
            , "playback"    : 0      // frames-per-second for non-caching EMP playback
            , "start_frame" : 0
            , "end_frame"   : 0      // start and end frames being used for the test
            }
        // for each of the cache testing modes
        , "caching" : [
            { "configuration_name" : "XXX"     // the name given to this configuration for identification purposes
            , "configuration"      : { ... }   // the configuration information for the cache evaluator
            , "caching_points"     : { ... }   // caching points used by the cache evaluator for this run
            , "frames_cached"      : [[S1,E1],
                                      [S2,E2]] // list of frame ranges cached
            , "cached_data"        : {         // counts and memory used for each node type enabled as a caching point
               "NODE_TYPE" : {
                 "count"  : 0,
                 "memory" : 0} }
            , "filling_playback"       : 0       // frames-per-second for playback while the cache is refilling synchronously
            , "fill_time"              : 0       // amount of time it took to fill the cache in the background, in seconds
                                                 //    (while nothing is going on in the foreground)
            , "cached_playback"        : 0       // frames-per-second for playback from cached data
            , "memory_before_playback" : [0,0]   // overall Maya [physical,virtual] memory usage after caching
            , "memory_after_playback"  : [0,0]   // overall Maya [physical,virtual] memory usage after caching playback
            , "evacuation_time"        : 0       // amount of time it takes to evacuate the cache, in seconds
            }
          ]
        }
    
    Several values in this output are lists. If the 'details' option is specified then the full
    list is included in the output. Otherwise the list is replaced by a count of the list members.
    These members include:
        OUT[KEY_CACHING][KEY_CACHING_POINTS]
        OUT[KEY_CACHING][KEY_CONFIGURATION][KEY_CACHE_MODE]
    """

    def __init__(self):
        """
        Initialize the persistent class members
        """
        pass

    def get_memory(self):
        """
        :return: A 2 member list with current physical and virtual memory in use by Maya
        """
        pass

    def run(self):
        """
        Run the analytic on the current scene.
        Performs a playback for a set of caching modes, recording the memory usage
        and timing for each of them along with the default configuration for reference.
        :result: JSON data as described in the class doc
        """
        pass

    @staticmethod
    def help():
        """
        Call this method to print the class documentation, including all methods.
        """
        pass

    ANALYTIC_DESCRIPTION_DETAILED = 'The normal output is the set of cache performance statistics.\n\n    {\n      "baseline"    : {\n          "memory"      : [0,0]  // baseline [physical,virtual] memory usage after animation, but before caching\n        , "playback"    : 0      // frames-per-second for non-caching EMP playback\n        , "start_frame" : 0\n        , "end_frame"   : 0      // start and end frames being used for the test\n        }\n    // for each of the cache testing modes\n    , "caching" : [\n        { "configuration_name" : "XXX"     // the name given to this configuration for identification purposes\n        , "configuration"      : { ... }   // the configuration information for the cache evaluator\n        , "caching_points"     : { ... }   // caching points used by the cache evaluator for this run\n        , "frames_cached"      : [[S1,E1],\n                                  [S2,E2]] // list of frame ranges cached\n        , "cached_data"        : {         // counts and memory used for each node type enabled as a caching point\n           "NODE_TYPE" : {\n             "count"  : 0,\n             "memory" : 0} }\n        , "filling_playback"       : 0       // frames-per-second for playback while the cache is refilling synchronously\n        , "fill_time"              : 0       // amount of time it took to fill the cache in the background, in seconds\n                                             //    (while nothing is going on in the foreground)\n        , "cached_playback"        : 0       // frames-per-second for playback from cached data\n        , "memory_before_playback" : [0,0]   // overall Maya [physical,virtual] memory usage after caching\n        , "memory_after_playback"  : [0,0]   // overall Maya [physical,virtual] memory usage after caching playback\n        , "evacuation_time"        : 0       // amount of time it takes to evacuate the cache, in seconds\n        }\n      ]\n    }\n\nSeveral values in this output are lists. If the \'details\' option is specified then the full\nlist is included in the output. Otherwise the list is replaced by a count of the list members.\nThese members include:\n    OUT[KEY_CACHING][KEY_CACHING_POINTS]\n    OUT[KEY_CACHING][KEY_CONFIGURATION][KEY_CACHE_MODE]'

    ANALYTIC_DESCRIPTION_SHORT = []

    ANALYTIC_LABEL = []

    ANALYTIC_NAME = 'CachePerformance'

    __fulldocs__ = 'The normal output is the set of cache performance statistics.\n\n    {\n      "baseline"    : {\n          "memory"      : [0,0]  // baseline [physical,virtual] memory usage after animation, but before caching\n        , "playback"    : 0      // frames-per-second for non-caching EMP playback\n        , "start_frame" : 0\n        , "end_frame"   : 0      // start and end frames being used for the test\n        }\n    // for each of the cache testing modes\n    , "caching" : [\n        { "configuration_name" : "XXX"     // the name given to this configuration for identification purposes\n        , "configuration"      : { ... }   // the configuration information for the cache evaluator\n        , "caching_points"     : { ... }   // caching points used by the cache evaluator for this run\n        , "frames_cached"      : [[S1,E1],\n                                  [S2,E2]] // list of frame ranges cached\n        , "cached_data"        : {         // counts and memory used for each node type enabled as a caching point\n           "NODE_TYPE" : {\n             "count"  : 0,\n             "memory" : 0} }\n        , "filling_playback"       : 0       // frames-per-second for playback while the cache is refilling synchronously\n        , "fill_time"              : 0       // amount of time it took to fill the cache in the background, in seconds\n                                             //    (while nothing is going on in the foreground)\n        , "cached_playback"        : 0       // frames-per-second for playback from cached data\n        , "memory_before_playback" : [0,0]   // overall Maya [physical,virtual] memory usage after caching\n        , "memory_after_playback"  : [0,0]   // overall Maya [physical,virtual] memory usage after caching playback\n        , "evacuation_time"        : 0       // amount of time it takes to evacuate the cache, in seconds\n        }\n      ]\n    }\n\nSeveral values in this output are lists. If the \'details\' option is specified then the full\nlist is included in the output. Otherwise the list is replaced by a count of the list members.\nThese members include:\n    OUT[KEY_CACHING][KEY_CACHING_POINTS]\n    OUT[KEY_CACHING][KEY_CONFIGURATION][KEY_CACHE_MODE]\nBase class for output for analytics.\n\nThe default location for the anlaytic output is in a subdirectory\ncalled \'MayaAnalytics\' in your temp directory. You can change that\nat any time by calling set_output_directory().\n\nClass static member:\n     ANALYTIC_NAME : Name of the analytic\n\nClass members:\n     directory     : Directory the output will go to\n     is_static     : True means this analytic doesn\'t require a file to run\n     logger        : Logging object for errors, warnings, and messages\n     plug_namer    : Object creating plug names, possibly anonymous\n     node_namer    : Object creating node names, possibly anonymous\n     csv_output    : Location to store legacy CSV output\n     plug_namer    : Set by option \'anonymous\' - if True then make plug names anonymous\n     node_namer    : Set by option \'anonymous\' - if True then make node names anonymous\n     __options     : Dictionary of per-analytic options\n\n\tMethods\n\t-------\n\tdebug : Utility to standardize debug messages coming from analytics.\n\n\terror : Utility to standardize errors coming from analytics.\n\n\testablish_baseline : This is run on an empty scene, to give the analytic a chance to\n\t                     establish any baseline data it might need (e.g. the nodes in an\n\t                     empty scene could all be ignored by the analytic)\n\t                     \n\t                     Base implementation does nothing. Derived classes should call\n\t                     their super() method though, in case something does get added.\n\n\tget_memory : :return: A 2 member list with current physical and virtual memory in use by Maya\n\n\thelp : Call this method to print the class documentation, including all methods.\n\n\tjson_file : Although an analytic is free to create any set of output files it\n\t            wishes there will always be one master JSON file containing the\n\n\tlog : Utility to standardize logging messages coming from analytics.\n\n\tmarker_file : Returns the name of the marker file used to indicate that the\n\t              computation of an analytic is in progress. If this file remains\n\t              in a directory after the analytic has run that means it was\n\t              interrupted and the data is not up to date.\n\t              \n\t              This file provides a safety measure against machines going down\n\t              or analytics crashing.\n\n\tname : Get the name of this type of analytic\n\n\toption : :param option: Name of option to check\n\t         :return: the current value of the named option\n\n\toutput_files : This is used to get the list of files the analytic will generate.\n\t               There will always be a JSON file generated which contains at minimum\n\t               the timing information. An analytic should override this method only\n\t               if they are adding more output files (e.g. a .jpg file).\n\t               \n\t               This should only be called after the final directory has been set.\n\n\trun : Run the analytic on the current scene.\n\t      Performs a playback for a set of caching modes, recording the memory usage\n\t      and timing for each of them along with the default configuration for reference.\n\t      :result: JSON data as described in the class doc\n\n\tset_options : Modify the settings controlling the run operation of the analytic.\n\t              Override this method if your analytic has some different options\n\t              available to it, but be sure to call this parent version after since\n\t              it sets common options.\n\t              \n\t              Note: Options are merged with existing options so make sure they are unique\n\t              :param options: Dictionary of OPTION:OPTION_VALUE to be set\n\n\tset_output_directory : Call this method to set a specific directory as the output location.\n\t                       The special names \'stdout\' and \'stderr\' are recognized as the\n\t                       output and error streams respectively rather than a directory.\n\n\twarning : Utility to standardize warnings coming from analytics.\n'

    is_static = False


KEY_CONFIGURATION = 'configuration'

KEY_CACHE_MODE = 'cache_mode'

KEY_MEMORY_BEFORE = 'memory_before_playback'

KEY_CACHED_DATA = 'cached_data'

CACHE_UNAVAILABLE = -1.0

KEY_EVACUATION = 'evacuation_time'

KEY_END_FRAME = 'end_frame'

KEY_BASELINE = 'baseline'

KEY_MEMORY = 'memory'

KEY_NODE_COUNT = 'count'

KEY_CACHING_POINTS = 'caching_points'

KEY_CONFIGURATION_NAME = 'configuration_name'

CACHE_STANDARD_MODE_VP2_SW = []

CACHE_STANDARD_MODE_EVAL_SHAPES = []

KEY_MEMORY_AFTER = 'memory_after_playback'

CACHE_STANDARD_MODE_EVAL = []

CACHE_STANDARD_MODE_VP2_HW = []

KEY_FILLING_PLAYBACK = 'filling_playback'

KEY_LOADED = 'plugin_loaded'

KEY_ENABLED = 'enabled'

KEY_CACHED_PLAYBACK = 'cached_playback'

KEY_CACHING = 'caching'

KEY_PLAYBACK = 'playback'

KEY_START_FRAME = 'start_frame'

KEY_FRAMES_CACHED = 'frames_cached'

EVALUATOR_NAME = 'cache'

MAX_FRAMES = 20

OPTION_DETAILS = 'details'

KEY_FILL_TIME = 'fill_time'
