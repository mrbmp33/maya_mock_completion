from maya.common.ui import LayoutManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class EventDescriptionWindow(object):
    """
    This is the main UI class for the profiler event description window.
    
    It handles creation of the UI and provides various callbacks to handle
    user interactions.
    """

    def __init__(self, window_name="'profilerEventDescriptionWindowId'"):
        """
        This does not create the UI.  UI creation is deferred until create() is called
        :param window_name: UI name for the window
        """
        pass

    def create(self):
        """
        This method completely builds the UI, then shows the finished window
        """
        pass

    def populate(self):
        """
        This method populates the current window with the framework necessary to
        store the event and category description information.
        """
        pass

    def selection_changed(self):
        """
        Callback for when the list of selected events in the profiler view changed
        """
        pass

    def window_closed(self):
        """
        Callback for when the profiler event description window closes
        """
        pass

    @staticmethod
    def populate_categories(category_info):
        """
        Populate the section of the window containing the category information
        :param category_info: List of (category_name, category_description) pairs
        """
        pass

    @staticmethod
    def populate_event_types(selected_event_types):
        """
        Populate the section of the window containing the event type information
        :param selected_event_types: List of dictionaries with event type description information
            KEY_TYPE        = Name of event type (Not present for anonymous events)
            KEY_DESCRIPTION = Description of event type (Not present for anonymous events)
            KEY_COLOUR      = List of 3 floats representing R, G, B of the event type
            KEY_CATEGORY    = Name of the category to which the event type belongs
            KEY_COUNT       = Number of events of this type found
        """
        pass

    __dict__ = None

    __weakref__ = None


def create_window():
    """
    This method is the entry point of the Profiler Event Description window.
    
    It creates the window and brings it up.
    """
    pass


KEY_COLOUR = 'color'

COL_SPACING = 10

RC_LAYOUT_5_COLUMN = {}

KEY_CATEGORY = 'category'

PROFILER_EVENT_DESCRIPTION_WINDOW_CONTROLLER = None

KEY_COUNT = 'count'

FRAME_MARGIN_HEIGHT = 4

RC_LAYOUT_2_COLUMN = {}

KEY_TYPE = 'type'

KEY_MAIN = 'eventSummary'

KEY_DESCRIPTION = 'description'

FRAME_LAYOUT = {}

FRAME_MARGIN_WIDTH = 25

TABLE_HEADER = {}
