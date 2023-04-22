from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLabel
from maya.app.renderSetup.common.utils import ReportableException
from maya.app.renderSetup.views.propertyEditor.layout import Layout

if False:
    from typing import Dict, List, Tuple, Union, Optional


class Override(MayaQWidgetBaseMixin, QGroupBox):
    """
    This class represents the property editor view of an override.
    """

    def __init__(self, item, parent): pass

    def paintEvent(self, event): pass

    def update(self): pass

    staticMetaObject = None


def getCppPointer(*args, **kwargs): pass


kIncompatibleAttribute = []

kInvalidAttribute = []

kDragAttributeFromAE = []

kLayer = []

kAppliedToUnique = []
