from maya.plugin.evaluator.cache_optionvar_states import *

from maya.plugin.evaluator.CacheWarningMessages import CacheWarningMessages
from maya.common.ui import callback_tool
from maya.app.prefs.OptionVar import OptionVar
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager
from maya.debug.PlaybackManager import PlaybackManager
from maya.common.utils import Singleton
from functools import partial
from maya.app.prefs.OptionVarManager import OptionVarManager
from maya.debug.DebugTrace import DebugTrace

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CachePreferencePreventFrameSkipping(OptionVar):
    """
    Class containing the information for the "caching playback prevent frame skipping" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    def read_preference_from_state(self):
        """
        Read the new value of the optionVar from the scene state
        """
        pass

    def set_state_from_preference(self):
        """
        Apply the current value of the optionVar to the scene state
        """
        pass

    ov_id = 'cachedPlaybackPreventFrameSkipping'


class CachePreferenceFillType(OptionVar):
    """
    Class containing the information for the "caching playback fill type" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    def find_index(self, value):
        """
        Find the index in the DATA list of the given enum value
        """
        pass

    def read_preference_from_state(self):
        """
        Read the new value of the optionVar from the scene state
        """
        pass

    def set_state_from_preference(self):
        """
        Apply the current value of the optionVar to the scene state
        """
        pass

    DATA = []

    KEYS = []

    data = []

    ov_id = 'cachedPlaybackFillType'


class CachePreferenceFillDirection(OptionVar):
    """
    Class containing the information for the "caching playback fill direction" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    def find_index(self, value):
        """
        Find the index in the DATA list of the given enum value
        """
        pass

    def read_preference_from_state(self):
        """
        Read the new value of the optionVar from the scene state
        """
        pass

    def set_state_from_preference(self):
        """
        Apply the current value of the optionVar to the scene state
        """
        pass

    DATA = []

    KEYS = []

    data = []

    ov_id = 'cachedPlaybackFillDirection'


class CachePreferenceEnabled(OptionVar):
    """
    Class containing the information for the "caching playback enabled" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    def read_preference_from_state(self):
        """
        Read the new value of the optionVar from the scene state
        """
        pass

    def set_state_from_preference(self):
        """
        Apply the current value of the optionVar to the scene state
        """
        pass

    ov_id = 'cachedPlaybackEnable'


class CachePreferences(object):
    """
    Class that initializes and aggregates all of the caching playback preferences,
    as well as supplying an interface for updating the preference values (the
    CacheEvaluatorManager instance)
    
    As certain data, notably the caching preferences change event, relies on the
    plug-in being loaded this class also monitors for it being loaded and unloaded
    in order to modify its scriptJob callbacks.
    
    :member option_vars:     Dictionary of optionVars that implement caching preferences
                             KEY=optionVar name, VALUE=OptionVar object controlling it
    :member pref_change_job: scriptJob ID for the cachingPreferencesChanged event
    :member monitor_load:    True if monitoring for plug-in load events
    :member monitor_unload:  True if monitoring for plug-in unload events
    :member plugin_clients:  Dictionary of clients listening for plug-in load/unload
                             KEY=ID of client, VALUE=Function to call when plug-in is loaded/unloaded
                             This is preferred over having every little bit of UI have its
                             own plug-in load/unload callbacks because it manages which events
                             to monitor and provides verification of the plug-in changing all in
                             one place.
    :member cache_mgr:       Instance of a CacheEvaluationManager() that can be used to easily
                             handle state changes of the cache evaluator
    :member cache_warnings:  Instance of a CacheWarningMessages() used to manage scene configuration warnings
    """

    def __init__(self):
        """
        Create all of the OptionVar objects used to manage the preferences.
        """
        pass

    def add_plugin_client(self, client, client_callback):
        """
        Add a new client function to be called when the plug-in state changes
        :param client: Name of client owning the callback
        :param client_callback: Function to be called when the plug-in state changes.
        """
        pass

    def add_preference(self, option_var):
        """
        Add a new OptionVar to be managed by the preferences class
        """
        pass

    def monitor_load_plugin(self, enable_monitor):
        """
        Enable or disable monitoring of the loadPlugin command
        :param enable_monitor: Should loadPlugin calls be monitored?
        """
        pass

    def monitor_state_changes(self, enable_listening):
        """
        Set the state of monitoring for preference changes. Preference changes can
        only be monitored when the plug-in is loaded so confirm it's possible when
        enabling.
        
        :param enable_listening: True if preference changes should be monitored.
        """
        pass

    def monitor_unload_plugin(self, enable_monitor):
        """
        Enable or disable monitoring of the unloadPlugin command
        :param enable_monitor: Should unloadPlugin calls be monitored?
        """
        pass

    def remove_plugin_client(self, client):
        """
        Remove all clients of the plug-in state change
        """
        pass

    def update_plugin_clients(self, new_state):
        """
        Update all of the clients listening to changes in the plug-in load/unload state
        """
        pass

    @staticmethod
    def callback_flush_frames_out_of_range(tool):
        """
        Invoked when the frame range flush preference changes - decides if the cache should flush frames out of the new range
        """
        pass

    @staticmethod
    def callback_plugin_loaded(plugin_name):
        """
        Callback invoked whenever a plug-in is loaded. Used to manage the
        scriptJob that monitors the cachingPreferencesChanged event since
        it is controlled by the plug-in.
        :param plugin_name: Name of the plug-in that was loaded. Only 'cache' is of interest.
        """
        pass

    @staticmethod
    def callback_plugin_unloaded(plugin_name):
        """
        Callback invoked whenever a plug-in is unloaded. Used to manage the
        scriptJob that monitors the cachingPreferencesChanged event since
        it is controlled by the plug-in.
        :param plugin_name: Name of the plug-in that was unloaded. Only 'cache' is of interest.
        """
        pass

    @staticmethod
    def callback_state_changed(tool):
        """
        Callback invoked when any of the state information on the cache evaluator affecting
        the preferences has changed. Only a generic event is triggered so all of the optionVars
        need to be updated even though only one is changing.
        """
        pass

    KEY_ENUM_DATA = 3

    KEY_ENUM_ID = 0

    KEY_ENUM_INFO = 2

    KEY_ENUM_NAME = 1

    __dict__ = None

    __weakref__ = None


class CachePreferenceMode(OptionVar):
    """
    Class containing the information for the "caching playback mode" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    def find_index(self, value):
        """
        Find the index in the DATA list of the given enum value
        """
        pass

    def read_preference_from_state(self):
        """
        Read the new value of the optionVar from the scene state
        """
        pass

    def set_state_from_preference(self):
        """
        Apply the current value of the optionVar to the scene state.
        The preference is an enum name while the actual caching mode is a set of rules.
        Do the conversion, reverting to the original values if the preference didn't
        point to a legal type.
        """
        pass

    DATA = []

    KEYS = []

    data = []

    ov_id = 'cachedPlaybackMode'


def cache_ui_enabled():
    """
    :return: False if any current condition requires disabling of the caching UI (caching disabled
    or EM evaluation not enabled)
    """
    pass


def _aggregate_enum_info(enum_data):
    """
    Take the enum_info and aggregate the list of enum values and their descriptions into
    an overall description string.
    :param enum_data: List of lists for allowed enum values and their associated text.
    :return: Aggregated string consisting of one line per enum value and its description.
    """
    pass


def cache_preferences_initialize():
    """
    Initialize all of the optionVar monitoring used by the cache preferences.
    This doesn't set up or read any optionVar values, it only creates the
    OptionVar classes required to manage the preferences.
    
    This function must be called on startup so that the management is in place
    before any commands or UI try to access them.
    """
    pass


CACHE_PLUGIN_NAME = 'cacheEvaluator'

CACHE_STANDARD_MODE_VP2_SW = []

CACHE_STANDARD_MODE_EVAL = []

CACHE_STANDARD_MODE_VP2_HW = []

OPTION_VAR_TYPE_BOOL = 0

CP_DBG = None
