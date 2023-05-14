from maya.common.utils import Singleton
from maya.app.prefs.OptionVar import OptionVar

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CachePreferenceHud(OptionVar):
    """
    Class containing the information for the "caching playback HUD visibility" preference.
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cacheVisibility'


class CachePreferenceShowWarningMessages(OptionVar):
    """
    Class containing the information for the "caching playback shows warning messages" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackShowWarningMessages'


class CachePreferenceDiscardFramesOutOfRange(OptionVar):
    """
    Class containing the information for the "caching playback discards cache data outside of playback range" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackDiscardFramesOutOfRange'


class CachePreferenceMemoryThreshold(OptionVar):
    """
    Class containing the information for the "caching playback resource guard memory threshold" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    @staticmethod
    def ranges():
        """
        :return 4-tuple with the min/max/soft_min/soft_max values for the threshold
        """
        pass

    ov_id = 'cachedPlaybackMemoryThreshold'


class CachePreferenceShowWarningFrames(OptionVar):
    """
    Class containing the information for the "caching playback shows warning frames in the timeslider" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackShowWarningFrames'


class CachePreferenceTimesliderBarSpacing(OptionVar):
    """
    Class containing the information for the "timeslider bar custom draw spacing" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'timeSliderCustomDrawSpacing'


class CachePreferenceTimesliderBarPosition(OptionVar):
    """
    Class containing the information for the "caching playback timeslider bar position" preference
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

    DATA = []

    KEYS = []

    data = []

    ov_id = 'cachedPlaybackPosition'


class CachePreferenceShowInvalidatedFrames(OptionVar):
    """
    Class containing the information for the "caching playback shows invalid frames in the timeslider" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackShowInvalidatedFrames'


class CachePreferenceResourceGuard(OptionVar):
    """
    Class containing the information for the "caching playback resource guard mode" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackResourceGuard'


class CachePreferenceTimesliderBarHeight(OptionVar):
    """
    Class containing the information for the "caching playback timeslider bar height" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackHeight'


class CachePreferenceShowSubframes(OptionVar):
    """
    Class containing the information for the "caching playback shows subframes in the timeslider" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackShowCachedSubframes'


class CachePreferenceShowCacheStatus(OptionVar):
    """
    Class containing the information for the "caching playback show cache status" preference
    """

    def __init__(self):
        """
        Initialize the preference interface
        """
        pass

    ov_id = 'cachedPlaybackShowCacheStatus'


OPTION_VAR_TYPE_FLOAT = 1

OPTION_VAR_TYPE_INT = 2

OPTION_VAR_TYPE_BOOL = 0
