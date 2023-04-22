"""
Utility to contain the EM state information. This is only the information
regarding the configuration of the EM, such as evaluators enabled and
their parameters.

State information is returned in JSON format for easy storage, parsing,
and comparison.

    {
        "emState" :
        {
            "mode" : EM_MODE,
            "enabled" : true,
            ...
            "evaluators" :
            {
                EVALUATOR_NAME :
                {
                    node_types : [],
                    enabled    : true,
                    ...
                },
                ...
            },
        }
"""

from maya.debug.EvaluatorManager import EvaluatorManager
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.debug.DeformerEvaluatorManager import DeformerEvaluatorManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EMState(object):
    """
    State object containing all configuration values for the EM. This doesn't attempt
    to read any scene-specific information, only the global configuration information
    such as evaluators enabled, evaluation mode, etc.
    
    :member results_files: Where the intermediate results are stored. None means don't store them.
    :member state:         Data state information from the scene.
    """

    def __init__(self):
        """
        Create a new state object and read all of the current state information.
        """
        pass

    def __str__(self):
        """
        Dump the state as a string. This converts the state information into a JSON
        indented format to make it easier to read.
        """
        pass

    __dict__ = None

    __weakref__ = None
