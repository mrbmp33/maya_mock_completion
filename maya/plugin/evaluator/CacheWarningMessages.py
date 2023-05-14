from maya.plugin.evaluator.CacheScriptJobHelper import CacheScriptJobHelper
from maya.common.ui import callback_tool
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceMemoryThreshold
from maya.debug.DebugTrace import DebugTrace
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceShowWarningMessages
from maya.common.utils import Singleton
from maya.plugin.evaluator.cache_optionvar_states import CachePreferenceResourceGuard
from maya.plugin.evaluator.CacheEvaluatorManager import CacheEvaluatorManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CacheWarningMessages(object):
    """
    Class to manage the display and handling of cache warning messages.
    :member silenced: Set of warnings that have been silenced, either temporarily or permanently
    :member cache_mgr: Local references to a CacheEvaluatorManager for getting state information
    :member last_memory_state: Last encountered state of memory usage
    :member last_safe_trigger: Last encountered safe mode trigger
    :member last_safe_messages: Last encountered safe mode messages
    :member last_resource_state: Last encountered resource state
    :member last_disable_message: Last reason the EM was disabled
    :member last_evaluation_mode: Last evaluation mode
    :member last_had_animation: True if animation existed last time the evaluator change was triggered
    """

    def __init__(self):
        """
        Initialize the toolkit widgets to be empty initially
        """
        pass

    def messaging_wanted(self):
        """
        :return: True if the EM and cache evaluator are in states where the warning messages are desirable
        """
        pass

    @staticmethod
    def callback_em_disabled_changed(tool):
        """
        Callback received when the evaluation manager has been disabled internally, e.g. due to
        a configuration that the EM cannot handle such as motion blur being enabled in VP2
        """
        pass

    @staticmethod
    def callback_evaluation_mode_changed(tool):
        """
        Callback received when the some sort of configuration changed happened to the EM modes.
        This callback is only concerned with transitions to and from DG evaluation mode so all
        other configuration changes are ignored.
        """
        pass

    @staticmethod
    def callback_memory_state_changed(tool):
        """
        Invoked when the state of the resource usage or the limit values have changed.
        Memory messages are silenced after their first use and only re-enabled in a new
        session, or if the resource guard or memory threshold values changed.
        """
        pass

    @staticmethod
    def callback_reset_message_warnings(tool):
        """
        Invoked when an event happens that should (re)enable warnings for low memory conditions
        """
        pass

    @staticmethod
    def callback_safe_mode_event(tool):
        """
        Invoked when the safe mode state has been set, or the safe mode messages have been set.
        Safe mode messages are only displayed when transitioning from normal mode to safe mode,
        or when in safe mode with messages that are different from the last time they were reported.
        """
        pass

    MSG_MEMORY_LOW = 0

    MSG_MEMORY_OUT = 1

    __dict__ = None

    __weakref__ = None


def dbg(msg):
    """
    Print the debugging string with the class name prepended
    """
    pass


def in_em_mode():
    """
    :return: True if the current evaluation is one of the EM modes (i.e. not DG)
    """
    pass


EVENT_SAFE_MODE = 'cachingSafeModeChanged'

EVENT_EM_DISABLED = 'cachingEvaluationModeChanged'

DBG = None

EVENT_CACHE_DESTROYED = 'cacheDestroyed'

EVENT_LIMIT_CHANGE = 'resourceLimitStateChange'
