from PySide2.QtCore import *

from PySide2.QtGui import QGuiApplication
from PySide2.QtGui import QStandardItemModel
from PySide2.QtGui import QColor
from PySide2.QtGui import QFontMetrics
from PySide2.QtGui import QStandardItem
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication

if False:
    from typing import Dict, List, Tuple, Union, Optional

import maya.app.renderSetup.views.proxy.renderSetup as rsProxy


class LightEditorProxy(rsProxy.DataModelListObserver, QStandardItemModel):
    """
    The class provides the Qt model counterpart for the LightEditor model
    """

    def __eq__(self, o): pass

    def __init__(self, parent='None'): pass

    def __ne__(self, o): pass

    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def attachChild(self, child, pos): pass

    def child(self, row, column='0'): pass

    def createListItemProxy(self, listItem): pass

    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def dropMimeData(self, mimeData, action, row, column, parentIndex): pass

    def findProxyItem(self, name): pass

    def flags(self, index): pass

    def mimeData(self, indices):
        """
        This method builds the mimeData if the selection is correct
        """
        pass

    def mimeTypes(self): pass

    def refreshModel(self): pass

    def resetModel(self): pass

    def supportedDropActions(self): pass

    def type(self): pass

    def typeIdx(self): pass

    @property
    def model(self):
        """
        Get the data model object for this proxy item.
        If the data model object does not exist, None is returned.
        """
        pass

    staticMetaObject = None


class LabelColor(object):
    """
    Base class for all the proxy classes to offer the label color option
    """

    def getLabelColor(self): pass

    def setLabelColor(self, label): pass

    __dict__ = None

    __weakref__ = None


import maya.app.renderSetup.views.pySide.standardItem as standardItem


class LightItemProxyBase(LabelColor, standardItem.StandardItem):
    def __init__(self, model): pass

    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def data(self, role): pass

    def delete(self): pass

    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def equalsDragType(self, dragType): pass

    def findProxyItem(self, name): pass

    def genericTypeIdx(self): pass

    def getActionButton(self, column): pass

    def getActionButtonCount(self): pass

    def getDefaultColor(self): pass

    def handleDragMoveEvent(self, event): pass

    def handleDropEvent(self, event, sceneView): pass

    def headingWidth(self, heading): pass

    def isActive(self): pass

    def isCopyable(self): pass

    def isDropAllowed(self, destinationModel): pass

    def isModelDirty(self):
        """
        # The next function (isModelDirty) is a workaround.
        # It should not be necessary but it is currently because we set tooltips in the treeview
        # and that triggers emitDataChanged which triggers the rebuild or repopulate of the property editor.
        # The proper fix will be to use columns in the treeview where each column has its own static tooltip
        # and the tooltips should no longer be dynamically set by the delegate (views/renderSetupDelegate.py)
        # depending on the lastHitAction
        """
        pass

    def modelChanged(*args, **kwargs): pass

    def onClick(self, view): pass

    def onDoubleClick(self, view): pass

    def setData(self, value, role): pass

    def supportsAction(self, action, numIndexes): pass

    @property
    def model(self):
        """
        Get the data model object for this proxy item.
        """
        pass


class LightItemProxy(LightItemProxyBase):
    """
    The class provides the Qt model counterpart for the LightItem
    """

    def __init__(self, model): pass

    def acceptsDrops(self, attribute): pass

    def columnData(self, role, column): pass

    def data(self, role): pass

    def delete(self): pass

    def type(self): pass

    def typeIdx(self): pass


class LightGroupProxy(rsProxy.DataModelListObserver, LightItemProxyBase):
    """
    The class provides the Qt model counterpart for the LightGroup
    """

    def __init__(self, model): pass

    def aboutToDelete(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def acceptsDrops(self, attribute): pass

    def attachChild(self, override, pos): pass

    def createListItemProxy(self, listItem): pass

    def data(self, role): pass

    def dispose(self):
        """
        Cleanup method to be called immediately before the object is deleted.
        """
        pass

    def getDefaultColor(self): pass

    def type(self): pass

    def typeIdx(self): pass


def getProxy(dataModel): pass


LIGHT_ITEM_TYPE_IDX = 14

kSetLocalRender = []

LIGHT_ITEM_BASE_TYPE_IDX = 13

LIGHT_ITEM_TYPE = 1014

kFilterCustom = []

LIGHT_EDITOR_TYPE_IDX = 12

DEFAULT_LIGHT_GROUP_COLOR = None

kFilterAll = []

kNoOverride = []

DEFAULT_LIGHT_ITEM_COLOR = None

kCreateShaderOverrideAction = []

kDragAndDropFailed = []

kFilterTransformsShapesShaders = []

kCreateRelativeOverrideAction = []

kAbsolute = []

kFiltersMenu = []

kRelativeType = []

kSetEnabledAction = []

kCollectionWarningStr = []

kFilterGeometry = []

kFilterTransformsAndShapes = []

LIGHT_TEXT_COLOR_ANIMATED = None

kRenderLayerWarningStr = []

LIGHT_GROUP_TYPE = 1015

DISABLED_LIGHT_TEXT_COLOR = None

kCameras = []

kFilterLights = []

LIGHT_EDITOR_MIME_TYPE = 'application/lightEditor'

kOverrideWarningStr = []

kFilterShaders = []

kCreateCollectionAction = []

LIGHT_TEXT_COLOR = None

kAOVs = []

kCreateRenderSettingsChildCollectionAction = []

colors = {}

kRenameAction = []

kRenderSettings = []

kCreateConnectionOverrideAction = []

kDragAndDrop = []

LIGHT_EDITOR_TYPE = 1012

kFilterCameras = []

LIGHT_ITEM_BASE_TYPE = 1013

kAbsoluteType = []

kFullyExpandCollapseAction = []

kShaderType = []

kNewFilter = []

kCreateMaterialOverrideAction = []

kFilterTransforms = []

kMaterialType = []

kSetIsolateSelectedAction = []

kRelative = []

LIGHT_TEXT_COLOR_LOCKED = None

kConnectionType = []

kSelectionTypeError = []

kExpandCollapseAction = []

kFilterSets = []

kCreateAbsoluteOverrideAction = []

kDeleteAction = []

kSetRenderableAction = []

LIGHT_GROUP_TYPE_IDX = 15

kSetVisibilityAction = []

kLights = []

LIGHT_TEXT_COLOR_OVERRIDEN_BY_US = None
