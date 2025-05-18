"""
* MayaQWidgetBaseMixin      Mixin that should be applied to all custom QWidgets created for Maya
                            to automatically handle setting the objectName and parenting
                            
* MayaQWidgetDockableMixin  Mixin that adds dockable capabilities within Maya controlled with
                            the show() function
"""

from qtpy.QtWidgets import *
from qtpy.QtGui import *

from qtpy.QtCore import Qt
from qtpy.QtCore import Signal
from qtpy.QtCore import QPoint
from qtpy.QtCore import QSize


class MayaQWidgetBaseMixin(QWidget):
    """
    Handle common actions for Maya Qt widgets during initialization:
        * auto-naming a Widget so it can be looked up as a string through
          maya.OpenMayaUI.MQtUtil.findControl()
        * parenting the widget under the main maya window if no parent is explicitly
          specified so not to have the Window disappear when the instance variable
          goes out of scope
    
    Integration Notes:
        Inheritance ordering: This class must be placed *BEFORE* the Qt class for proper execution
        This is needed to workaround a bug where PyQt/PySide does not call super() in its own __init__ functions
    
    Example:
        class MyQWidget(MayaQWidgetBaseMixin, QPushButton):
            def __init__(self, parent=None):
                super(MyQWidget, self).__init__(parent=parent)
                self.setText('Push Me')
        myWidget = MyQWidget()
        myWidget.show()
        print myWidget.objectName()
    """

    def __init__(self, parent=None, *args, **kwargs):
        # If no parent is specified, parent to the main window (simulate Maya's behavior)
        if parent is None:
            # In Maya, this would be the main window pointer; here we just use None
            parent = None
        super().__init__(parent, *args, **kwargs)
        # Auto-set objectName if not set
        if hasattr(self, "objectName") and not self.objectName():
            self.setObjectName(self.__class__.__name__)

    def setVisible(self, makeVisible):
        """
        Show/hide the widget.  Overrides standard QWidget.setVisible()
        """
        if hasattr(super(), "setVisible"):
            super().setVisible(makeVisible)
        else:
            if makeVisible:
                self.show()
            else:
                self.hide()

    def show(self):
        """
        Show the widget. Overrides standard QWidget.show()
        """
        if hasattr(super(), "show"):
            super().show()

    __dict__ = None

    __weakref__ = None


class MayaQDockWidget(MayaQWidgetBaseMixin, QDockWidget):
    """
    QDockWidget tailored for use with Maya.
    Mimics the behavior performed by Maya's internal QMayaDockWidget class and the dockControl command
    
    :Signals:
        closeEventTriggered: emitted when a closeEvent occurs
    
    :Known Issues:
        * Manually dragging the DockWidget to dock in the Main MayaWindow will have it resize to the 'sizeHint' size
          of the child widget() instead of preserving its existing size.
    """

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._area = None
        self.closeEventTriggered = Signal()
        self.windowStateChanged = Signal()

    def closeEvent(self, evt):
        """
        Hide the QDockWidget and trigger the closeEventTriggered signal
        """
        self.hide()
        if hasattr(self, "closeEventTriggered") and self.closeEventTriggered is not None:
            self.closeEventTriggered.emit()
        evt.accept()

    def moveEvent(self, event):
        # Optionally emit windowStateChanged or handle move logic
        if hasattr(self, "windowStateChanged") and self.windowStateChanged is not None:
            self.windowStateChanged.emit()
        super().moveEvent(event)

    def resizeEvent(self, event):
        # Optionally emit windowStateChanged or handle resize logic
        if hasattr(self, "windowStateChanged") and self.windowStateChanged is not None:
            self.windowStateChanged.emit()
        super().resizeEvent(event)

    def setArea(self, area):
        """
        Set the docking area
        """
        self._area = area

    closeEventTriggered = None

    staticMetaObject = None

    windowStateChanged = None


class MayaQWidgetDockableMixin(MayaQWidgetBaseMixin):
    """
    Handle Maya dockable actions controlled with the show() function.
    
    Integration Notes:
        Inheritance ordering: This class must be placed *BEFORE* the Qt class for proper execution
        This is needed to workaround a bug where PyQt/PySide does not call super() in its own __init__ functions
    
    Example:
        class MyQWidget(MayaQWidgetDockableMixin, QPushButton):
            def __init__(self, parent=None):
                super(MyQWidget, self).__init__(parent=parent)
                self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred )
                self.setText('Push Me')
        myWidget = MyQWidget()
        myWidget.show(dockable=True)
        myWidget.show(dockable=False)
        print myWidget.showRepr()
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._dockable = False
        self._floating = True
        self._dock_area = None
        self._allowed_area = 'all'
        self._dock_params = {}
        self._size_hint = None

    def close(self):
        """
        Closes the widget. Overrides standard QWidget.close()
        """
        if hasattr(super(), "close"):
            super().close()

    def dockArea(self):
        """
        Return area if the widget is currently docked to the Maya MainWindow
        Will return None if not dockable
        
        :Return: str
        """
        if self._dockable:
            return self._dock_area
        return None

    def dockCloseEventTriggered(self):
        """
        Triggered when QDockWidget.closeEventTriggered() signal is triggered.
        Stub function.  Override to perform actions when this happens.
        """
        # Stub for override
        pass

    def floatingChanged(self, isFloating):
        """
        Triggered when QDockWidget.topLevelChanged() signal is triggered.
        Stub function.  Override to perform actions when this happens.
        """
        # Stub for override
        pass

    def hide(self, *args, **kwargs):
        """
        Hides the widget.  Will hide the parent widget if it is a QDockWidget.
        Overrides standard QWidget.hide()
        """
        if hasattr(super(), "hide"):
            super().hide(*args, **kwargs)

    def isDockable(self):
        """
        Return if the widget is currently dockable (under a QDockWidget)
        
        :Return: bool
        """
        return getattr(self, "_dockable", False)

    def isFloating(self):
        """
        Return if the widget is currently floating (under a QDockWidget)
        Will return True if is a standalone window OR is a floating dockable window.
        
        :Return: bool
        """
        if self.isDockable():
            return getattr(self, "_floating", True)
        return True

    def isVisible(self):
        """
        Return if the widget is currently visible. Overrides standard QWidget.isVisible()
        
        :Return: bool
        """
        if hasattr(super(), "isVisible"):
            return super().isVisible()
        return False

    def raise_(self):
        """
        Raises the widget to the top.  Will raise the parent widget if it is a QDockWidget.
        Overrides standard QWidget.raise_()
        """
        if hasattr(super(), "raise_"):
            super().raise_()

    def setDockableParameters(self, dockable=None, floating=None, area=None, allowedArea=None, width=None,
                              widthSizingProperty=None, minWidth=None, height=None, heightSizingProperty=None,
                              x=None, y=None, retain=True, plugins=None, controls=None, uiScript=None,
                              closeCallback=None, *args, **kwargs):
        """
        Set the dockable parameters.
        
        :Parameters:
            dockable (bool)
                Specify if the window is dockable (default=False)
            floating (bool)
                Should the window be floating or docked (default=True)
            area (string)
                Default area to dock into (default='left')
                Options: 'top', 'left', 'right', 'bottom'
            allowedArea (string)
                Allowed dock areas (default='all')
                Options: 'top', 'left', 'right', 'bottom', 'all'
            width (int)
                Width of the window
            height (int)
                Height of the window
            x (int)
                left edge of the window
            y (int)
                top edge of the window
                
        :See: show(), hide(), and setVisible()
        """
        if dockable is not None:
            self._dockable = bool(dockable)
        if floating is not None:
            self._floating = bool(floating)
        if area is not None:
            self._dock_area = area
        if allowedArea is not None:
            self._allowed_area = allowedArea
        # Store all params for showRepr
        self._dock_params = {
            "dockable": self._dockable,
            "floating": self._floating,
            "area": self._dock_area,
            "allowedArea": self._allowed_area,
            "width": width,
            "height": height,
            "x": x,
            "y": y,
            "retain": retain,
            "plugins": plugins,
            "controls": controls,
            "uiScript": uiScript,
            "closeCallback": closeCallback,
        }
        # Set geometry if provided
        if width is not None or height is not None or x is not None or y is not None:
            cur_geom = self.geometry()
            w = width if width is not None else cur_geom.width()
            h = height if height is not None else cur_geom.height()
            xpos = x if x is not None else cur_geom.x()
            ypos = y if y is not None else cur_geom.y()
            self.setGeometry(xpos, ypos, w, h)

    def setSizeHint(self, size):
        """
        Virtual method used to pass the user settable width and height down to the widget whose 
        size policy controls the actual size most of the time.
        """
        self._size_hint = size

    def setVisible(self, makeVisible, *args, **kwargs):
        """
        Show/hide the QWidget window.  Overrides standard QWidget.setVisible() to pass along additional arguments
        
        :See: show() and hide()
        """
        if hasattr(super(), "setVisible"):
            super().setVisible(makeVisible)

    def setWindowTitle(self, val):
        """
        Sets the QWidget's title and also it's parent QDockWidget's title if dockable.
        
        :Return: None
        """
        if hasattr(super(), "setWindowTitle"):
            super().setWindowTitle(val)
        # If dockable, also set parent QDockWidget's title if present
        if self.isDockable() and hasattr(self.parent(), "setWindowTitle"):
            self.parent().setWindowTitle(val)

    def show(self, *args, **kwargs):
        """
        Show the QWidget window.  Overrides standard QWidget.show()
        
        :See: setDockableParameters() for a list of parameters
        """
        # Accept dockable params via kwargs
        dockable = kwargs.get("dockable", None)
        floating = kwargs.get("floating", None)
        area = kwargs.get("area", None)
        allowedArea = kwargs.get("allowedArea", None)
        width = kwargs.get("width", None)
        height = kwargs.get("height", None)
        x = kwargs.get("x", None)
        y = kwargs.get("y", None)
        self.setDockableParameters(
            dockable=dockable, floating=floating, area=area, allowedArea=allowedArea,
            width=width, height=height, x=x, y=y
        )
        if hasattr(super(), "show"):
            super().show()

    def showRepr(self):
        """
        Present a string of the parameters used to reproduce the current state of the
        widget used in the show() command.
        
        :Return: str
        """
        params = getattr(self, "_dock_params", {})
        param_strs = []
        for k, v in params.items():
            if v is not None:
                param_strs.append(f"{k}={repr(v)}")
        return f"{self.__class__.__name__}.show({', '.join(param_strs)})"

    closeEventTriggered = None

    windowStateChanged = None


def workspaceControlDeleted(controlName): pass


def wrapInstance(*args, **kwargs): pass


def workspaceControlClosed(controlName): pass


def getCppPointer(*args, **kwargs): pass


def workspaceControlReparented(controlName, isFloating): pass


mixinWorkspaceControls = {}

_qtImported = 'PySide2'
