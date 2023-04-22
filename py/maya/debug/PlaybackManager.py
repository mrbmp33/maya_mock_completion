"""
Holds the helper class PlaybackManager used to change and restore
the playbackOptions within a scope and manages simple playing.

Load with:
        from maya.debug.PlaybackManager import PlaybackManager

See the class docs for how to use this to control playback.
"""

from traceback import extract_tb
from traceback import format_list
from maya.debug.DebugTrace import DebugTrace

if False:
    from typing import Dict, List, Tuple, Union, Optional


class PlaybackManager(DebugTrace):
    """
    Helper class that maintains the playback mode information.
    
    It maintains state information for all playback options so that they can be
    modified within a scope and have the original settings restored on completion.
    
    Calling any of the setXXX() methods
    
    The object is set up to use the Python "with" syntax as follows:
    
        with PlaybackManager() as mgr:
            mgr.minTime = new_start_frame
    
    That will ensure the original states are all restored. There's no other
    reliable way to do it in Python. If you need different scoping that can't
    be put into a nice code block like this you can manually call the methods
    to complete the sequence:
    
        mgr = PlaybackManager()
            ...
        mgr.minTime = new_start_frame )
            ...
        mgr.restore()
    
    You may also be interested in this utility method that will playback the
    entire range from the start in 'wait' mode. You want this because if you
    don't play in 'wait' mode then your manager can go out of scope while
    playback is running, messing up your state on exit.
    
        with PlaybackManager() as mgr:
            mgr.play_all()
    
    See also mgr.play_range() and mgr.play_limited_range() for other options.
    """

    def __enter__(self):
        """
        Beginning of scope object for "with" statement. __init__ does all intialization
        """
        pass

    def __exit__(self, exit_type, exit_value, traceback):
        """
        Ensure the state is restored if this object goes out of scope
        """
        pass

    def __getattribute__(self, option_name):
        """
        :param option_name: Name of one of the parameters to the playbackOptions command
        :return: the playback option's current value
        """
        pass

    def __init__(self):
        """
        Defining both __enter__ and __init__ so that either one can be used
        """
        pass

    def __setattr__(self, option_name, new_value):
        """
        Set the new value of the playback option
        :param option_name: Name of one of the parameters to the playbackOptions command
        :param new_value: New end time value
        """
        pass

    def __str__(self):
        """
        Nicer formatting for the playback options
        """
        pass

    def get_current_state(self):
        """
        :return: PlaybackManagerState object containing the current state of the playback options.
        Meant to be mainly used for testing.
        """
        pass

    def limited_range(self, max_frames, from_start='False'):
        """
        :param max_frames: Maximum number of frames to play
        :param from_start: When set to True get the range from the start of the
                   animation, else get it from the current frame.
        
        :return: 2-tuple (START,END) indicating the frame numbers actually used
                 in the defined limited range
        """
        pass

    def play_all(self):
        """
        Playback the entire animation sequence, once
        
        :return: 3-tuple (TIME,START,END) indicating the elapsed play time and the
                frame numbers that were played
        """
        pass

    def play_for(self, seconds):
        """
        Playback the entire animation sequence until "seconds" time has elapsed.
        If the total time it takes to play the animation range is less than seconds,
        loop until seconds time has elapsed.
        
        :return: 2-tuple (ELAPSED_TIME,PLAYED_FRAMES) indicating the total elapsed time and
                the number of played back frames.
        """
        pass

    def play_limited_range(self, max_frames, from_start='False'):
        """
        Playback the given animation range, returning the elapsed time when it is done.
        The time range is only set temporarily for this playback sequence.
        If you wish to permanently change the time range use setOptions().
        
        max_frames: Maximum number of frames to play
        from_start: When set to True this will first move the playback to the first
                   frame of the animation. Otherwise it will go to what the current
                   time was when the manager was created. This allows you to get
                   consistent limited length playbacks from an arbitrary starting
                   frame.
        
        Note: If the current time is at or near the maxTime and you do not
              specify 'from_start=True' there may be little or no animation so
              make sure your scene is set up appropriate if you use that option.
        
        :return: 3-tuple (TIME,START,END) indicating the elapsed play time and the
                frame numbers that were played
        """
        pass

    def play_range(self, min_time, max_time):
        """
        Playback the given animation range once, returning the elapsed time when it is done.
        The time range is only set temporarily for this playback sequence.
        
        :return: 3-tuple (TIME,START,END) indicating the elapsed play time and the
                frame numbers that were played
        """
        pass

    def restore(self):
        """
        Restore the playback options to their original values (i.e. the ones
        present when this object was constructed).
        
        It's necessary to call this when using the "with PlaybackManager()"
        syntax. It's only needed when you explicitly instantiate the mode manager.
        Then you have to call this if you want your original state restored,
        or wait for the unknown point in the future where this object is
        destroyed.
        """
        pass

    def set_limited_range(self, max_frames, from_start='False'):
        """
        Set up the manager to play the given animation range by setting the
        minTime and maxTime to respect the arguments. After calling this you
        can use playAll() rather than playRange() or playLimitedRange().
        
        The time range is set for the duration of this manager so only use
        it if you will be using the same range repeatedly. It returns a
        tuple of (original_min_time, original_max_time) in case you want
        to restore it later.
        
        :param max_frames: Maximum number of frames to play
        :param from_start: When True this will first move the playback to the first
                   frame of the animation. Otherwise it will go to what the current
                   time was when the manager was created. This allows you to get
                   consistent limited length playbacks from an arbitrary starting
                   frame.
        
        Note: If the current time is at or near the maxTime and you do not
              specify 'from_start=True' there may be little or no animation so
              make sure your scene is set up appropriate if you use that option.
        
        :return: 2-tuple (START,END) indicating the frame numbers actually used
                 in the defined limited range
        """
        pass

    @property
    def current_time(self):
        """
        Get the current time in the playback timeline
        """
        pass

    @property
    def current_time_unit(self):
        """
        Get the current time unit in the playback timeline
        """
        pass

    PLAYBACK_OPTIONS = []

    PlaybackManagerState = None
