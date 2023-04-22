"""
# DEV_FLAG
# import maya.app.flux.ui.core
# import maya.app.flux.utils
"""

from maya.app.flux.utils import *

from maya.app.flux.ui.core import getIconFromName
from maya.app.flux.ui.core import setWidgetWindowColor
from maya.app.flux.ui.core import getPixmap
from maya.app.flux.ui.core import ListButtonBtn
from maya.app.flux.ui.core import ListButtonDelegate
from maya.app.flux.ui.core import NodeSelector
from maya.app.flux.ui.core import ImageButton
from maya.app.flux.ui.core import setWidgetBaseColor
from maya.app.flux.ui.core import ListButtonItem
from copy import deepcopy
from maya.app.flux.utils import str_res as res
from maya.app.flux.undo import undoChunk
from maya.app.flux.ui.core import highlightPixmap
from maya.app.flux.ui.core import FrameBar
from maya.app.flux.ui.core import DraggableListWidget
from maya.app.flux.ui.core import setVLayout
from maya.app.flux.ui.core import scalePixmap
from maya.app.flux.ui.core import QPainter
from maya.app.flux.ui.core import registerQtObject
from maya.app.flux.ui.core import dpi
from maya.app.flux.ui.core import SingleNodeInputWidget
from maya.app.flux.ui.core import HWidget
from maya.app.flux.ui.core import TextFieldWrapper
from maya.app.flux.ui.core import getIconSuffix
from maya.app.flux.ui.core import createPixmap
from maya.app.flux.ui.core import setWidgetBackgroundColor
from maya.app.flux.ui.core import pix
from maya.app.flux.ui.core import NodeListWidget
from maya.app.flux.ui.core import ListButtonWidget
from maya.app.flux.ui.core import VWidget
from maya.app.flux.ui.core import configureDragDrop
from maya.app.flux.ui.core import applyMargins
from maya.app.flux.ui.core import DraggableTreeWidget
from maya.app.flux.ui.core import loadFluxIcons
from maya.app.flux.ui.core import setHLayout
from maya.app.flux.ui.core import DropWindow
from maya.app.flux.ui.core import widgetWithLayout
from maya.app.flux.ui.core import dpiScale
from maya.app.flux.ui.core import configureRightClickMenu
from maya.app.flux.ui.core import DropWindowListWidget
from maya.app.flux.ui.core import getWidgetOfClassFromLayout
from maya.app.flux.ui.core import centerOnScreen
from maya.app.flux.ui.core import FrameWidget

if False:
    from typing import Dict, List, Tuple, Union, Optional

qt_dpi = 1

pixmap_cache = {}

maya_scale = 2.0

fluxIcons = {}
