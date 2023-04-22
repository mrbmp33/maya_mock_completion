from PySide2.QtWidgets import QAction
from contextlib import contextmanager

if False:
    from typing import Dict, List, Tuple, Union, Optional


class Action(QAction):
    def excepthook(self, type, value, traceback): pass

    def trigger(self):
        """
        The only method Render Setup is currently using from the QAction interface
        """
        pass

    exceptionRaised = None

    staticMetaObject = None


def excepthookGuard(*args, **kwds): pass
