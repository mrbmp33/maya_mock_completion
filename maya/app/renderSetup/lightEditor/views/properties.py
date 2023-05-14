from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from maya.app.renderSetup.views.propertyEditor.layout import Layout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGroupBox

if False:
    from typing import Dict, List, Tuple, Union, Optional


class LightProperties(MayaQWidgetBaseMixin, QGroupBox):
    """
    This class represents the property editor view of a light editor light item.
    """

    def __init__(self, item, parent): pass

    staticMetaObject = None


class GroupProperties(MayaQWidgetBaseMixin, QGroupBox):
    """
    This class represents the property editor view of a light editor group item.
    """

    def __init__(self, item, parent): pass

    staticMetaObject = None


def _createControl(plg, attrLabel, connectable='True', enabled='True'):
    """
    Create a UI control for the given attribute, 
    matching its type and considering if it's connectable.
    """
    pass


def getCppPointer(*args, **kwargs): pass


kEnable = []

kIsolate = []
