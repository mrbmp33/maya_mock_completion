from PySide2.QtWidgets import QLineEdit

if False:
    from typing import Dict, List, Tuple, Union, Optional


class CollectionFilterLineEdit(QLineEdit):
    def __init__(self, text='None', parent='None'): pass

    def dragEnterEvent(self, event):
        """
        Accepts drag events if the dragged event text contains only commands
        """
        pass

    def dragMoveEvent(self, event):
        """
        Accepts drag move events. Validation is already done in the enter event
        """
        pass

    def dropEvent(self, event):
        """
        Adds the dropped object types to the list
        """
        pass

    staticMetaObject = None


def _textContainsObject(text):
    """
    Does the first line of text contain an object that exists?
    """
    pass
