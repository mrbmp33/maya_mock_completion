from maya.app.prefs.OptionVar import OptionVar

if False:
    from typing import Dict, List, Tuple, Union, Optional


class OptionVarManager(object):
    """
    Class that manages the states for all registered optionVars.
    :member option_vars: Dictionary of optionVars being managed.
        KEY : Name of optionVar
        VALUE : List of management information
            KEY_TYPE             : Option var data type
            KEY_DEFAULT          : Option var default value
            KEY_HELD             : Remembered option var value
            KEY_SYNC_TO_VAR_FN   : Callback to take the app implementation of the
                                   optionVar data and put its value into the optionVar
            KEY_SYNC_FROM_VAR_FN : Callback to set the app implementation of the optionVar
                                   data to be the current value of the optionVar
    """

    @classmethod
    def as_str(cls):
        """
        Return a string representation of all of the active OptionVars
        """
        pass

    @classmethod
    def clear_all(cls):
        """
        Debugging method to remove all option vars from the manager
        """
        pass

    @classmethod
    def manage(cls, option_var):
        """
        Add the option_var to the set of managed variables
        :param option_var: OptionVar object to be added to the managed list
        :raise AssertionError: If an option variable with the given name is already managed
        """
        pass

    @classmethod
    def manages(cls, var_name):
        """
        :param var_name: Name of optionVar to check
        :return: True if the manager is actively managing the optionVar var_name
        """
        pass

    @classmethod
    def option_var(cls, option_var_name):
        """
        Lookup the option_var_name in the managed list, returning the OptionVar
        implementing it, if it exists.
        :param option_var_name: Name of the managed optionVar to retrieve
        :raise KeyError: If the optionVar is not in the managed list
        :return: OptionVar corresponding to the managed option_var_name
        """
        pass

    @classmethod
    def read_preferences_from_state(cls):
        """
        Update all of the optionVar values to match the Maya state.
        (Called after preference modifications were undone or canceled.)
        """
        pass

    @classmethod
    def remember_states(cls):
        """
        Remember the current states of all managed optionVars
        """
        pass

    @classmethod
    def restore_states(cls):
        """
        Restore the remembered states of all managed optionVars
        """
        pass

    @classmethod
    def revert_to_defaults(cls):
        """
        Restore the states of all managed optionVars to their factory defaults
        """
        pass

    @classmethod
    def set_state_from_preferences(cls):
        """
        Take all of the optionVar values and update the Maya state to reflect
        those values. (Called after preferences were read or updated.)
        """
        pass

    __dict__ = None

    __weakref__ = None

    option_vars = {}
