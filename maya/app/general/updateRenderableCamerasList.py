if False:
    from typing import Dict, List, Tuple, Union, Optional


class CameraInfo:
    def __init__(self, shapeName, associatedScriptJobNbr): pass


def onCameraChangedAddRemoveCameras():
    """
    The onCameraChange event is triggered when a camera is added or removed
    from the scene. We must react by updating the list of cameras in the
    current scene and add or kill scriptJobs accordingly.
    """
    pass


def getAddedAndRemovedCameras():
    """
    Return 2 iterables, one of the names of the new camera shapes added and
    one of the CameraInfo objects corresponding to the cameras that were
    removed since the last time the list of cameras (camerasList) was
    updated.
    """
    pass


def addCameraShapeToCamerasListAndScriptJobsList(cameraShape): pass


def createCommonRenderCamerasAddBaseCameras(fullPath, updateFunc):
    """
    This is called when the createCommonRenderCameras function is called.
    It is mandatory to store the fullPath given as argument as a global
    variable to be used later when scriptJobs are triggered.
    """
    pass


path = None

camerasList = []
