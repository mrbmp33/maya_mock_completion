import exceptions

if False:
    from typing import Dict, List, Tuple, Union, Optional


class DagPath(object):
    """
    Helper class wrapper over MDagPath with specialized queries.
    """

    def __init__(self, dagPath):
        """
        Constructor. "dagPath" is a OpenMaya.MDagPath.
        """
        pass

    def findDisplacementShaders(self):
        """
        Generator over the displacement shaders assigned to this DAG path.
        There can be more than one if shape has per-face shading.
        """
        pass

    def findGeometryGenerator(self):
        """
        Returns the mesh or nurbs generator of this DAG path if any, None otherwise.
        """
        pass

    def findMaterialPlugs(self):
        """
        Find and yield all the shape plugs connected to materials (shading engines)
        """
        pass

    def findSets(self): pass

    def findSetsConnections(self, fnType='467'):
        """
        Generator over all the connections from this path to a node of type
        fnType. There can be more than one if the shape has per-face shading.
        
        Connections are returned as tuples (srcPlug, destPlug)
        "srcPlug" belongs to the shape node. "destPlug" belongs to the assigned node of type fnType.
        srcPlug ---> destPlug
        """
        pass

    def findShadingEngineConnections(self):
        """
        Find and yield all connections from the shape to a shading engine.
        """
        pass

    def findShadingEngines(self):
        """
        Generator over all the shading engines assigned to this DAG path.
        There can be more than one if shape has per-face shading.
        """
        pass

    def findSurfaceShaders(self):
        """
        Generator over the surface shaders assigned to this DAG path.
        There can be more than one if shape has per-face shading.
        """
        pass

    def findVolumeShaders(self):
        """
        Generator over the volume shaders assigned to this DAG path.
        There can be more than one if shape has per-face shading.
        """
        pass

    def fullPathName(self):
        """
        Returns the full path string of this DAG path.
        """
        pass

    def node(self):
        """
        Returns the DAG node at the end of the path (as MObject).
        """
        pass

    @staticmethod
    def create(pathStr):
        """
        Create a DagPath object for the given string path or None if it doesn't exist.
        """
        pass

    __dict__ = None

    __weakref__ = None


class _PlugNotFound(exceptions.Exception):
    __weakref__ = None


def _filterConnectionsToSpecificNodeType(plugs, fnType):
    """
    Return a generator of all connections to nodes of type fnType
    """
    pass
