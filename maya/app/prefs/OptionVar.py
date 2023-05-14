from functools import partial
from maya.debug.DebugTrace import DebugTrace

if False:
    from typing import Dict, List, Tuple, Union, Optional


class OptionVar(object):
    """
    Class that manages an optionVar synced preference variable. It understands all of the various
    types of optionVars as well as some metatypes (e.g. boolean implemented as int, enum
    implemented as string).
        :member name: Name of the optionVar (i.e. what you pass to the optionVar command)
        :member value_default: The default value of the optionVar (i.e. the value it gets when prefs are reset)
        :member value_type: One of the OPTION_VAR_TYPE_xxx constants indicating what type of variable this is
        :member value_remembered: Value that was remembered when requested
        :member title: Short title describing the preference
        :member info: Longer description of the preference
        :member option_var_job: scriptJob ID for the job that updates the preference when the optionVar changes
        :member clients: Dictionary of client methods to call when the OptionVar changes,
                         either directly or via the Maya state - usually for UI. KEY=client, VALUE=callback
    """

    def __init__(self, name, value_type, value_default):
        """
        Initialize a new optionVar sync object
        :param name: Name of the optionVar (i.e. what you pass to the optionVar command)
        :param value_type: One of the OPTION_VAR_TYPE_xxx constants indicating what type of variable this is
                           If this is a list instead then it is considered to be the list of valid
                           strings for an enum type.
        :param value_default: The default value of the optionVar (i.e. the value it gets when prefs are reset)
        """
        pass

    def __str__(self):
        """
        :return: String representation of the optionVar
        """
        pass

    def add_client(self, client, client_callback):
        """
        Add a new client function to be called when this OptionVar value changes
        :param client: Name of client owning the callback
        :param client_callback: Function to be called when the OptionVar changes
                                Takes this OptionVar as the parameter.
        """
        pass

    def do_read_preference_from_state(self):
        """
        Wrapper around read_preference_from_state that ensures monitoring is off and values are legal
        """
        pass

    def do_set_state_from_preference(self):
        """
        Wrapper around set_state_from_preference that ensures monitoring is off and values are legal
        """
        pass

    def get_value(self):
        """
        Get the current value of this managed variable. If the value has not yet
        been defined as an optionVar then return the default (not 0 as the optionVar
        command normally would).
        :raise ValueError: If the var_name is not known to the manager
        """
        pass

    def read_preference_from_state(self):
        """
        Override this to read the new value of the optionVar from the scene state. Do not call directly.
        """
        pass

    def remember_current(self):
        """
        Remember the current states of all managed optionVars
        """
        pass

    def remove_client(self, client):
        """
        Remove all clients
        """
        pass

    def restore_remembered(self):
        """
        Restore the remembered states of all managed optionVars
        """
        pass

    def revert_to_default(self):
        """
        Restore the states of all managed optionVars to their factory defaults
        """
        pass

    def set_state_from_preference(self):
        """
        Override this to apply the current value of the optionVar to the scene state. Do not call directly.
        """
        pass

    def set_value(self, var_value):
        """
        Set the value of the managed variable. The value passed in must match
        the type the variable has been defined as.
        :param var_value: New value of the optionVar
        """
        pass

    def set_value_directly(self, client, var_value):
        """
        Same as set_value, except that monitoring is disabled and the state is updated
        directly after the new optionVar is set, including any clients (not including
        the client that set the value).
        :param var_value: New value of the optionVar
        :param client: Who set the value directly
        :raise ValueError: If the value was not a legal value for this optionVar
        """
        pass

    def update_all_clients_but_me(self, who_am_i):
        """
        Notify the list of clients that the value has changed, not including the one passed in
        :param who_am_i: The client that initiated the changed (which is why it won't be notified)
        """
        pass

    def update_clients(self):
        """
        Notify the list of clients that the value has changed
        """
        pass

    @staticmethod
    def callback_preference_changed(option_var):
        """
        Callback invoked when the optionVar has been modified via the optionVar command
        :param option_var: OptionVar object generating the callback
        """
        pass

    @property
    def monitor_preference(self):
        """
        Return the resource guard state value
        """
        pass

    StateError = None

    __dict__ = None

    __weakref__ = None


def var_type_info(var_type):
    """
    Utility method to return a debug string representing a variable type
    """
    pass


def option_var_get_value(var_name, var_type):
    """
    Type-safe method of retrieving the current value of the optionVar. Converts from
    the raw value to the var_type the optionVar is expected to be.
    :param var_name: Name of the optionVar to retrieve
    :param var_type: Type of optionVar this is
    :param var_value: New value to be set
    :raise ValueError: If the var_value type is not compatible with retrieved value.
                       - A boolean is not 0 or 1
                       - An enum is not part of the allowed enum string list
                       - Floats are truncated to integers
    """
    pass


def option_var_set_value(var_name, var_type, var_value):
    """
    Set the value of an optionVar, with input type validation
    :param var_name: Name of the optionVar to retrieve
    :param var_type: Type of optionVar this is
    :param var_value: New value to be set
    :raise ValueError: If the var_value type is not compatible with var_type
                       This is slightly more restrictive than normal usage:
                           - non-string types to strings.
                           - integers are converted to floats but not booleans
                           - booleans are converted to ints (0, 1) but not floats
                           - enum string matches the known string types
    """
    pass


ERR_OV_NOT_INT = []

OPTION_VAR_TYPE_STRING = 3

ERR_OV_NOT_STRING = []

DBG = None

ERR_OV_NOT_ENUM = []

OPTION_VAR_TYPE_FLOAT = 1

OPTION_VAR_TYPES = []

CREATE_DEBUG_PROXY = False

ERR_OV_NOT_BOOL = []

ERR_OV_NOT_LEGAL_ENUM = []

OPTION_VAR_TYPE_BOOL = 0

ERR_OV_TYPE_UNKNOWN = []

ERR_OV_NOT_FLOAT = []

OPTION_VAR_TYPE_INT = 2

ENUM_LISTS = {}
