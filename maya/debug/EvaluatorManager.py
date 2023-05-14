"""
Derived classes will handle evaluator-specific information, this
one just handles the information that is common to all evaluators.

The object is set up to use the Python "with" syntax as follows:

    class MyEvaluatorManager(EvaluatorManager):
        ...

    from maya.debug.MyEvaluatorManager import MyEvaluatorManager
    with MyEvaluatorManager() as mgr:
        mgr.setMode( someMode )

That will ensure the original states are all restored.

If you need different control you can manually complete the sequence:

    mgr = MyEvaluatorManager()
    mgr.save_state()
    mgr.setMode( someMode )
    mgr.restore_state()
"""

from traceback import extract_tb
from maya.app.prefs.OptionVar import OptionVar
from maya.debug.DebugTrace import DebugTrace
from traceback import format_list

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EvaluatorManager(DebugTrace):
    """
    Class for managing the shared evaluator state in a 'with' format. Remembers
    and restores the mode and parameters, including the load state of any plug-in
    associated with the manager.
    """

    def __enter__(self):
        """
        Defining both __enter__ and __init__ so that either one can be used
        """
        pass

    def __exit__(self, event_type, value, traceback):
        """
        Ensure the state is restored if this object goes out of scope
        """
        pass

    def __init__(self, name, plugin):
        """
        Defining both __enter__ and __init__ so that either one can be used
        
        Members:
            state          : Values of the various states when save_state was called
            evaluator_name : Name of the evaluator this object manages
            plugin_name    : Name of the plug-in in which the evaluator is found (None if native)
            in_debug_mode  : True if debugging messages are to be printed
        """
        pass

    def __str__(self):
        """
        Display mechanism to show evaluator information in JSON format
        """
        pass

    def as_json(self):
        """
        Display mechanism to retrieve evaluator information in a format conducive to JSON formatting
        """
        pass

    def check_evaluator(self):
        """
        Check to see if the evaluator is known by the system
        :raise OptionVar.StateError: The evaluator is not known
        """
        pass

    def claimed_nodes(self, flatten):
        """
        :param flatten: Boolean determining how to return the claimed nodes
        :return: If flatten is True then returns a single list of all nodes
                 claimed by this evaluator.
                 If flatten is False then return a list of clusters created
                 by this evaluator, where each cluster is in turn a list of
                 nodes contained within that cluster.
        """
        pass

    def restore_state(self):
        """
        Restore the evaluator to its original mode prior to creation of this
        object. Using the "with" syntax this will be called automatically.
        
        You only need to call explicitly when you instantiate the mode manager
        as an object.
        """
        pass

    def save_state(self):
        """
        Remember the current state of all evaluator parameters so that they
        can be restored on exit.
        
        self.state must be initialized to an object of type EvaluatorState
            (or derived class) before calling here
        """
        pass

    def set_state(self, new_state):
        """
        Define the evaluator state parameters.
        :param new_state: State information in the format provided by as_json
                          Only key values specified will change. Others retain
                          their current values (*not* default values).
        """
        pass

    @property
    def consolidation(self):
        """
        Return the cluster consolidation method to use (none or subgraph)
        """
        pass

    @property
    def enabled(self):
        """
        Return the evaluator's enabled state
        """
        pass

    @property
    def node_types(self):
        """
        Return the evaluator's enabled node type list
        """
        pass

    @property
    def plugin_loaded(self):
        """
        Return whether the evaluator's plug-in was loaded
        """
        pass

    @property
    def priority(self):
        """
        Return the evaluator's evaluation priority
        """
        pass

    EvaluatorState = None


def as_list(thing):
    """
    Simple utility to ensure the thing is a list, return None as an empty list
    """
    pass


KEY_CONSOLIDATION = 'consolidation'

KEY_PRIORITY = 'priority'

KEY_PLUGIN = 'plugin'

KEY_NODE_TYPES = 'node_types'

KEY_LOADED = 'plugin_loaded'

KEY_ENABLED = 'enabled'

KEY_NAME = 'name'
