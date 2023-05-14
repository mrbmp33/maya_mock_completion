"""
This file contains the classes that access the implementation of all of the UI components
that drive the cached playback feature. The management of the actual features they control
is in cache_preferences.py.

The exposed methods provide a consistent interface to the Mel code that is used
to incorporate those components into the larger UI.
"""

from maya.plugin.evaluator.CacheUiColour import CacheUiColour
from maya.plugin.evaluator.CacheUiHud import CacheUiHud
from maya.plugin.evaluator.CacheUiToggle import CacheUiToggle
from maya.plugin.evaluator.CacheUiMenu import CacheUiMenu
from maya.plugin.evaluator.CacheUiPreferencesTab import CacheUiPreferencesTab
from maya.plugin.evaluator.CacheUiFullLayout import CacheUiFullLayout

if False:
    from typing import Dict, List, Tuple, Union, Optional


def cache_ui_preferences_tab_update():
    """
    Update the aggregation UI that comprises of the cached playback preferences tab.
    """
    pass


def cache_ui_hud_create(section, label_width, starting_block):
    """
    Create the HUD menu entry from initHUD.mel
    :param section: Section in which the HUD will appear
    :param label_width: How wide the HUD label should be
    :param starting_block: Block for the first HUD element
    :return: Next block index to use in order to appear after the last caching HUD element
    """
    pass


def cache_ui_hud_menu_item_create(previous_item):
    """
    Create the HUD menu entry from buildDisplay.mel
    :param previous_item: Name of the menuItem appearing above this one in the menu
    """
    pass


def cache_ui_colour_preferences_create():
    """
    Create the colour preferences widgets
    :return: Name of the frameLayout widget created
    """
    pass


def cache_ui_preferences_tab_create(prefs_template):
    """
    Create the aggregation UI that comprises of the cached playback preferences tab.
    :param prefs_template: Name of the template the preferences window uses
    """
    pass


def cache_ui_colour_preferences_populate():
    """
    Create the child widgets inside the cached playback colour preferences frame
    """
    pass


def cache_ui_full_layout_create(ui_key):
    """
    Create UI underneath a control and set up smart deletion of the management object
    :param ui_key: Unique identifier for this set of controls
    """
    pass


def cache_ui_full_layout_update(ui_key):
    """
    Update UI underneath a control and set up smart deletion of the management object
    :param ui_key: ID of UI control under which this set of preferences appears (comes from cache_ui_full_layout_create)
    """
    pass


def cache_ui_colour_preferences_update():
    """
    Update the colour preferences widgets with the current colour values
    """
    pass


def cache_ui_toggle_create():
    """
    Create the button with popup menu for cache preferences that is shown from playbackRange.mel
    :return: UI Widget ID of the button
    """
    pass


def cache_ui_preferences_tab_frame_create():
    """
    Create the frame for the cache preferences tab
    """
    pass


def cache_ui_preferences_list_item_create(prefs_window, text_scroll_widget, text_scroll_index):
    """
    Create the aggregation UI that comprises of the cached playback preferences tab.
    :param prefs_window: Name of the window in which the preferences will reside
    :param text_scroll_widget: Name of the textScrollList control in which the cache preferences item lives
    :param text_scroll_index: Index of the cache preferences item within the textScrollList
    :return: True if the list entry was created, else False
    """
    pass


def cache_ui_menu_create(ui_key):
    """
    Create the menu for cache preferences that is shown from TimeSliderMenu.mel
    :param ui_key: Unique identifier for this menu
    """
    pass


CP_DBG = None
