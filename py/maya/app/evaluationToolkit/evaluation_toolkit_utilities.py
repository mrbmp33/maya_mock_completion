if False:
    from typing import Dict, List, Tuple, Union, Optional


class EvaluationToolkitSection(object):
    """
    Base class with common methods for sections in the toolkit.
    """

    def update_ui(self):
        """
        Nothing to do by default for updating UI
        """
        pass

    __dict__ = None

    __weakref__ = None


class EvaluationToolkitSubsection(object):
    """
    Base class with common methods for subsections underneath sections in the toolkit.
    """

    def update_ui(self):
        """
        Nothing to do by default for updating UI
        """
        pass

    __dict__ = None

    __weakref__ = None


def set_gpu_override_active(state):
    """
    This method activates or deactivates the OpenCL evaluator.
    
    TODO: This could be better implemented by moving the gpuOverride optionVar
          into one of the OptionVar class objects for automatic management.
    
    :param state: New activation state of the evaluator.
    """
    pass


def section_layout(start_closed):
    """
    :param start_closed: True means the frame should be closed when the UI is initially created
    :return: A dictionary consisting of the parameters used by the top level frames
    """
    pass


BUTTON_WIDTH = 100

FILE_TEXT_FIELD_WIDTH = 150

COLUMN_SPACING = 10

ROW_SPACING = 4
