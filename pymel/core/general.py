import exceptions

"""
For the rest of the class hierarchy, including `DependNode <pymel.core.nodetypes.DependNode>`, `Transform <pymel.core.nodetypes.Transform>`,
and `Attribute <pymel.core.nodetypes.Attribute>`, see :mod:`pymel.core.nodetypes`.
"""

from pymel.internal.pmcmds import removeMultiInstance
from pymel.internal.pmcmds import objExists
from pymel.internal.pmcmds import selectMode
from pymel.internal.pmcmds import pause
from pymel.internal.pmcmds import aliasAttr
from pymel.internal.pmcmds import makePaintable
from pymel.internal.pmcmds import displayColor
from pymel.internal.pmcmds import affectedNet
from pymel.internal.pmcmds import pickWalk
from pymel.internal.pmcmds import isolateSelect
from pymel.internal.pmcmds import scaleComponents
from pymel.internal.pmcmds import evalDeferred
from pymel.internal.pmcmds import listNodesWithIncorrectNames
from pymel.internal.pmcmds import containerProxy
from pymel.internal.pmcmds import artAttrTool
from pymel.internal.pmcmds import reorder
from pymel.internal.pmcmds import baseView
from pymel.internal.pmcmds import contextInfo
from pymel.internal.pmcmds import transformCompare
from pymel.internal.pmcmds import timeCode
from pymel.internal.pmcmds import editDisplayLayerMembers
from pymel.internal.pmcmds import format
from pymel.internal.pmcmds import selectPriority
from pymel.internal.pmcmds import containerView
from pymel.internal.pmcmds import exactWorldBoundingBox
from pymel.internal.pmcmds import itemFilterAttr
from pymel.internal.pmcmds import containerBind
from pymel.internal.pmcmds import relationship
from pymel.internal.pmcmds import performanceOptions
from pymel.internal.pmcmds import paramLocator
from pymel.internal.pmcmds import upAxis
from pymel.internal.pmcmds import symmetricModelling
from pymel.util.enum import Enum
from pymel.internal.pmcmds import objectType
from pymel.internal.pmcmds import attributeQuery
from pymel.internal.pmcmds import affects
from pymel.internal.pmcmds import currentUnit
from pymel.internal.pmcmds import expandedSelection
from pymel.internal.pmcmds import selectedNodes
from pymel.internal.pmcmds import containerPublish
from pymel.internal.pmcmds import toolDropped
from pymel.internal.pmcmds import deleteAttr
from pymel.internal.pmcmds import displayLevelOfDetail
from pymel.internal.pmcmds import listNodeTypes
from pymel.internal.pmcmds import suitePrefs
from pymel.internal.pmcmds import displayRGBColor
from pymel.internal.pmcmds import containerTemplate
from pymel.internal.pmcmds import sceneLint
from pymel.internal.pmcmds import sculptMeshCacheChangeCloneSource
from pymel.internal.pmcmds import toolHasOptions
from pymel.internal.pmcmds import stringArrayIntersector
from pymel.internal.pmcmds import objectCenter
from pymel.internal.pmcmds import showHidden
from pymel.internal.pmcmds import toggleAxis
from pymel.internal.pmcmds import snapMode
from pymel.internal.pmcmds import displayStats
from pymel.internal.pmcmds import selectType
from pymel.internal.pmcmds import makeLive
from pymel.internal.pmcmds import deleteExtension
from pymel.internal.pmcmds import xform
from pymel.internal.pmcmds import lockNode
from pymel.internal.pmcmds import colorManagementConvert
from pymel.internal.pmcmds import colorIndex
from pymel.internal.pmcmds import addExtension
from pymel.internal.pmcmds import color
from pymel.internal.pmcmds import makeIdentity
from pymel.internal.pmcmds import toggle
from pymel.internal.pmcmds import attributeInfo
from pymel.internal.pmcmds import license
from pymel.internal.pmcmds import pixelMove
from pymel.internal.pmcmds import setToolTo
from pymel.internal.pmcmds import isTrue
from pymel.internal.pmcmds import selectPref
from pymel.internal.pmcmds import hide
from pymel.internal.pmcmds import renameAttr
from pymel.internal.pmcmds import displayCull
from pymel.internal.pmcmds import attributeName
from pymel.internal.pmcmds import createAttrPatterns
from pymel.internal.pmcmds import itemFilter
from pymel.internal.pmcmds import toggleDisplacement
from pymel.internal.pmcmds import colorManagementPrefs
from pymel.internal.pmcmds import displayAffected
from pymel.internal.pmcmds import editDisplayLayerGlobals
from pymel.internal.pmcmds import threadCount
from pymel.internal.pmcmds import cycleCheck
from pymel.internal.pmcmds import encodeString
from pymel.internal.pmcmds import xformConstraint
from pymel.internal.pmcmds import reorderContainer
from pymel.internal.pmcmds import saveToolSettings
from pymel.internal.pmcmds import displayPref
from pymel.internal.pmcmds import colorManagementFileRules
from pymel.internal.pmcmds import displaySurface
from pymel.internal.pmcmds import about
from pymel.internal.pmcmds import itemFilterRender
from pymel.internal.pmcmds import baseTemplate
from pymel.internal.pmcmds import isConnected
from pymel.internal.pmcmds import copyAttr
from pymel.internal.pmcmds import listAttrPatterns
from pymel.internal.pmcmds import bakePartialHistory
from pymel.internal.pmcmds import inheritTransform
from pymel.internal.pmcmds import commandEcho
from pymel.internal.pmcmds import deleteAttrPattern
from pymel.internal.pmcmds import resetTool
from pymel.internal.pmcmds import ungroup
from pymel.internal.pmcmds import itemFilterType
from pymel.internal.pmcmds import matchTransform
from pymel.internal.pmcmds import displaySmoothness
from pymel.internal.pmcmds import connectionInfo
from pymel.internal.pmcmds import webView
from pymel.internal.pmcmds import refresh
from pymel.internal.pmcmds import nodeCast
from pymel.internal.pmcmds import softSelect
from pymel.internal.pmcmds import isDirty
from pymel.internal.pmcmds import align
from pymel.internal.pmcmds import polySplitCtx2
from pymel.internal.pmcmds import colorManagementCatalog
from pymel.internal.pmcmds import transformLimits
from pymel.internal.pmcmds import instanceable
from pymel.internal.pmcmds import shapeCompare
from pymel.internal.pmcmds import curveRGBColor
from pymel.internal.plogging import getLogger as _getLogger
from pymel.internal.pmcmds import hilite
from pymel.internal.pmcmds import applyAttrPattern

if False:
    from typing import Dict, List, Tuple, Union, Optional


class ProxySlice(object):
    """
    slice(stop)
    slice(start, stop[, step])
    
    Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).
    """

    def __cmp__(self, *args, **kwargs):
        """
        x.__cmp__(y) <==> cmp(x,y)
        """
        pass

    def __delattr__(self, *args, **kwargs):
        """
        x.__delattr__('name') <==> del x.name
        """
        pass

    def __format__(self, *args, **kwargs):
        """
        default object formatter
        """
        pass

    def __hash__(self, *args, **kwargs):
        """
        x.__hash__() <==> hash(x)
        """
        pass

    def __init__(self, *args, **kwargs): pass

    def __repr__(self, *args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __str__(self, *args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def indices(self, *args, **kwargs):
        """
        S.indices(len) -> (start, stop, stride)
        
        Assuming a sequence of length len, calculate the start and stop
        indices, and the stride length of the extended slice described by
        S. Out of bounds indices are clipped in a manner consistent with the
        handling of normal slices.
        """
        pass

    start = None

    step = None

    stop = None

    __dict__ = None

    __weakref__ = None


import pymel.util as _util


class PyNode(_util.ProxyUnicode):
    """
    Abstract class that is base for all pymel nodes classes.
    
    The names of nodes and attributes can be passed to this class, and the appropriate subclass will be determined.
    
        >>> PyNode('persp')
        nt.Transform(u'persp')
        >>> PyNode('persp.tx')
        Attribute(u'persp.translateX')
    
    If the passed node or attribute does not exist an error will be raised.
    """

    def __apimfn__(self):
        """
        Get a ``maya.OpenMaya*.MFn*`` instance
        """
        pass

    def __eq__(self, other):
        """
        Returns
        -------
        bool
        """
        pass

    def __ge__(self, other): pass

    def __getitem__(*args, **kwargs):
        """
        The function '{objName}' is deprecated and will become unavailable in future pymel versions. Convert to string first using str() or PyNode.name()
        
        deprecated
        """
        pass

    def __gt__(self, other): pass

    def __init__(self, *args, **kwargs): pass

    def __le__(self, other): pass

    def __lt__(self, other): pass

    def __melobject__(self):
        """
        Special method for returning a mel-friendly representation.
        """
        pass

    def __ne__(self, other):
        """
        Returns
        -------
        bool
        """
        pass

    def __nonzero__(self):
        """
        Returns
        -------
        bool
        """
        pass

    def __radd__(self, other): pass

    def __reduce__(self):
        """
        allows PyNodes to be pickled
        """
        pass

    def __repr__(self):
        """
        Returns
        -------
        unicode
        """
        pass

    def addPrefix(self, prefix):
        """
        Returns the object's name with a prefix added to the beginning of the name
        
        :rtype: `other.NameParser`
        """
        pass

    def connections(*args, **kwargs):
        """
        This command returns a list of all attributes/objects of a specified type that
        are connected to the given object(s). If no objects are specified then the
        command lists the connections on selected nodes.
        
        Modifications:
          - returns an empty list when the result is None
          - returns an empty list (with a warning) when the arg is an empty list, tuple,
                set, or frozenset, making it's behavior consistent with when None is
                passed, or no args and nothing is selected (would formerly raise a
                TypeError)
          - When 'connections' flag is True, (and 'plugs' is True) the attribute pairs are returned in a 2D-array::
        
                [['checker1.outColor', 'lambert1.color'], ['checker1.color1', 'fractal1.outColor']]
        
                Note that if 'plugs' is False (the default), for backward compatibility, the returned pairs are somewhat less intuitive attrs + nodes::
        
                [['checker1.outColor', 'lambert1'], ['checker1.color1', 'fractal1']]
        
          - added sourceFirst keyword arg. when sourceFirst is true and connections is also true,
                the paired list of plugs is returned in (source,destination) order instead of (thisnode,othernode) order.
                this puts the pairs in the order that disconnectAttr and connectAttr expect.
          - added ability to pass a list of types
        
        Returns
        -------
        List[Union[PyNode, Attribute, Tuple[PyNode, PyNode], Tuple[Attribute, Attribute]]]
        
        Flags:
        - connections : c                (bool)          [create]
            If true, return both attributes involved in the connection. The one on the
            specified object is given first.  Default false.
        
        - destination : d                (bool)          [create]
            Give the attributes/objects that are on the destinationside of connection to the
            given object.  Default true.
        
        - exactType : et                 (bool)          [create]
            When set to true, -t/type only considers node of this exact type. Otherwise,
            derived types are also taken into account.
        
        - plugs : p                      (bool)          [create]
            If true, return the connected attribute names; if false, return the connected
            object names only.  Default false;
        
        - shapes : sh                    (bool)          [create]
            Actually return the shape name instead of the transform when the shape is
            selected.  Default false.
        
        - skipConversionNodes : scn      (bool)          [create]
            If true, skip over unit conversion nodes and return the node connected to the
            conversion node on the other side.  Default false.
        
        - source : s                     (bool)          [create]
            Give the attributes/objects that are on the sourceside of connection to the
            given object.  Default true.
        
        - type : t                       (unicode)       [create]
            If specified, only take objects of a specified type.
            Flag can have multiple arguments, passed either as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.listConnections`
        """
        pass

    def deselect(self): pass

    def exists(self, **kwargs):
        """
        objExists
        """
        pass

    def future(*args, **kwargs):
        """
        Modifications:
          - returns an empty list when the result is None
          - added a much needed 'type' filter
          - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
        
        Returns
        -------
        List[nodetypes.DependNode]
        """
        pass

    def history(*args, **kwargs):
        """
        This command traverses backwards or forwards in the graph from the specified
        node and returns all of the nodes whose construction history it passes through.
        The construction history consists of connections to specific attributes of a
        node defined as the creators and results of the node's main data, eg. the curve
        for a Nurbs Curve node. For information on history connections through specific
        plugs use the listConnectionscommand first to find where the history begins then
        use this command on the resulting node.
        
        Modifications:
          - returns an empty list when the result is None
          - raises a RuntimeError when the arg is an empty list, tuple, set, or
                frozenset, making it's behavior consistent with when None is passed, or
                no args and nothing is selected (would formerly raise a TypeError)
          - added a much needed 'type' filter
          - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
        
        Returns
        -------
        List[nodetypes.DependNode]
        
        Flags:
        - allConnections : ac            (bool)          [create]
            If specified, the traversal that searches for the history or future will not
            restrict its traversal across nodes to only dependent plugs. Thus it will reach
            all upstream nodes (or all downstream nodes for f/future).
        
        - allFuture : af                 (bool)          [create]
            If listing the future, list all of it. Otherwise if a shape has an attribute
            that represents its output geometry data, and that plug is connected, only list
            the future history downstream from that connection.
        
        - allGraphs : ag                 (bool)          [create]
            This flag is obsolete and has no effect.
        
        - breadthFirst : bf              (bool)          [create]
            The breadth first traversal will return the closest nodes in the traversal
            first. The depth first traversal will follow a complete path away from the node,
            then return to any other paths from the node. Default is depth first.
        
        - future : f                     (bool)          [create]
            List the future instead of the history.
        
        - futureLocalAttr : fl           (bool)          [query]
            This flag allows querying of the local-space future-related attribute(s) on
            shape nodes.
        
        - futureWorldAttr : fw           (bool)          [query]
            This flag allows querying of the world-space future-related attribute(s) on
            shape nodes.
        
        - groupLevels : gl               (bool)          [create]
            The node names are grouped depending on the level.  1 is the lead, the rest are
            grouped with it.
        
        - historyAttr : ha               (bool)          [query]
            This flag allows querying of the attribute where history connects on shape
            nodes.
        
        - interestLevel : il             (int)           [create]
            If this flag is set, only nodes whose historicallyInteresting attribute value is
            not less than the value will be listed. The historicallyInteresting attribute is
            0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
            the users.
        
        - leaf : lf                      (bool)          [create]
            If transform is selected, show history for its leaf shape. Default is true.
        
        - levels : lv                    (int)           [create]
            Levels deep to traverse. Setting the number of levels to 0 means do all levels.
            All levels is the default.
        
        - pruneDagObjects : pdo          (bool)          [create]
            If this flag is set, prune at dag objects.                  Flag can have
            multiple arguments, passed either as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.listHistory`
        """
        pass

    def listConnections(*args, **kwargs):
        """
        This command returns a list of all attributes/objects of a specified type that
        are connected to the given object(s). If no objects are specified then the
        command lists the connections on selected nodes.
        
        Modifications:
          - returns an empty list when the result is None
          - returns an empty list (with a warning) when the arg is an empty list, tuple,
                set, or frozenset, making it's behavior consistent with when None is
                passed, or no args and nothing is selected (would formerly raise a
                TypeError)
          - When 'connections' flag is True, (and 'plugs' is True) the attribute pairs are returned in a 2D-array::
        
                [['checker1.outColor', 'lambert1.color'], ['checker1.color1', 'fractal1.outColor']]
        
                Note that if 'plugs' is False (the default), for backward compatibility, the returned pairs are somewhat less intuitive attrs + nodes::
        
                [['checker1.outColor', 'lambert1'], ['checker1.color1', 'fractal1']]
        
          - added sourceFirst keyword arg. when sourceFirst is true and connections is also true,
                the paired list of plugs is returned in (source,destination) order instead of (thisnode,othernode) order.
                this puts the pairs in the order that disconnectAttr and connectAttr expect.
          - added ability to pass a list of types
        
        Returns
        -------
        List[Union[PyNode, Attribute, Tuple[PyNode, PyNode], Tuple[Attribute, Attribute]]]
        
        Flags:
        - connections : c                (bool)          [create]
            If true, return both attributes involved in the connection. The one on the
            specified object is given first.  Default false.
        
        - destination : d                (bool)          [create]
            Give the attributes/objects that are on the destinationside of connection to the
            given object.  Default true.
        
        - exactType : et                 (bool)          [create]
            When set to true, -t/type only considers node of this exact type. Otherwise,
            derived types are also taken into account.
        
        - plugs : p                      (bool)          [create]
            If true, return the connected attribute names; if false, return the connected
            object names only.  Default false;
        
        - shapes : sh                    (bool)          [create]
            Actually return the shape name instead of the transform when the shape is
            selected.  Default false.
        
        - skipConversionNodes : scn      (bool)          [create]
            If true, skip over unit conversion nodes and return the node connected to the
            conversion node on the other side.  Default false.
        
        - source : s                     (bool)          [create]
            Give the attributes/objects that are on the sourceside of connection to the
            given object.  Default true.
        
        - type : t                       (unicode)       [create]
            If specified, only take objects of a specified type.
            Flag can have multiple arguments, passed either as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.listConnections`
        """
        pass

    def listFuture(*args, **kwargs):
        """
        Modifications:
          - returns an empty list when the result is None
          - added a much needed 'type' filter
          - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
        
        Returns
        -------
        List[nodetypes.DependNode]
        """
        pass

    def listHistory(*args, **kwargs):
        """
        This command traverses backwards or forwards in the graph from the specified
        node and returns all of the nodes whose construction history it passes through.
        The construction history consists of connections to specific attributes of a
        node defined as the creators and results of the node's main data, eg. the curve
        for a Nurbs Curve node. For information on history connections through specific
        plugs use the listConnectionscommand first to find where the history begins then
        use this command on the resulting node.
        
        Modifications:
          - returns an empty list when the result is None
          - raises a RuntimeError when the arg is an empty list, tuple, set, or
                frozenset, making it's behavior consistent with when None is passed, or
                no args and nothing is selected (would formerly raise a TypeError)
          - added a much needed 'type' filter
          - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
        
        Returns
        -------
        List[nodetypes.DependNode]
        
        Flags:
        - allConnections : ac            (bool)          [create]
            If specified, the traversal that searches for the history or future will not
            restrict its traversal across nodes to only dependent plugs. Thus it will reach
            all upstream nodes (or all downstream nodes for f/future).
        
        - allFuture : af                 (bool)          [create]
            If listing the future, list all of it. Otherwise if a shape has an attribute
            that represents its output geometry data, and that plug is connected, only list
            the future history downstream from that connection.
        
        - allGraphs : ag                 (bool)          [create]
            This flag is obsolete and has no effect.
        
        - breadthFirst : bf              (bool)          [create]
            The breadth first traversal will return the closest nodes in the traversal
            first. The depth first traversal will follow a complete path away from the node,
            then return to any other paths from the node. Default is depth first.
        
        - future : f                     (bool)          [create]
            List the future instead of the history.
        
        - futureLocalAttr : fl           (bool)          [query]
            This flag allows querying of the local-space future-related attribute(s) on
            shape nodes.
        
        - futureWorldAttr : fw           (bool)          [query]
            This flag allows querying of the world-space future-related attribute(s) on
            shape nodes.
        
        - groupLevels : gl               (bool)          [create]
            The node names are grouped depending on the level.  1 is the lead, the rest are
            grouped with it.
        
        - historyAttr : ha               (bool)          [query]
            This flag allows querying of the attribute where history connects on shape
            nodes.
        
        - interestLevel : il             (int)           [create]
            If this flag is set, only nodes whose historicallyInteresting attribute value is
            not less than the value will be listed. The historicallyInteresting attribute is
            0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
            the users.
        
        - leaf : lf                      (bool)          [create]
            If transform is selected, show history for its leaf shape. Default is true.
        
        - levels : lv                    (int)           [create]
            Levels deep to traverse. Setting the number of levels to 0 means do all levels.
            All levels is the default.
        
        - pruneDagObjects : pdo          (bool)          [create]
            If this flag is set, prune at dag objects.                  Flag can have
            multiple arguments, passed either as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.listHistory`
        """
        pass

    def listSets(self, *args, **kwargs):
        """
        Returns list of sets this object belongs
        
        listSets -o $this
        
        Returns
        -------
        List[PyNode]
        """
        pass

    def namespaceList(self):
        """
        Useful for cascading references.  Returns all of the namespaces of the calling object as a list
        
        Returns
        -------
        List[unicode]
        """
        pass

    def nodeType(*args, **kwargs): pass

    def objExists(self, **kwargs):
        """
        objExists
        """
        pass

    def select(self, **kwargs): pass

    def stripNamespace(self, *args, **kwargs):
        """
        Returns the object's name with its namespace removed.  The calling instance is unaffected.
        The optional levels keyword specifies how many levels of cascading namespaces to strip, starting with the topmost (leftmost).
        The default is 0 which will remove all namespaces.
        
        :rtype: `other.NameParser`
        """
        pass

    def swapNamespace(self, prefix):
        """
        Returns the object's name with its current namespace replaced with the provided one.
        The calling instance is unaffected.
        
        :rtype: `other.NameParser`
        """
        pass

    @staticmethod
    def __new__(cls, *args, **kwargs):
        """
        Catch all creation for PyNode classes, creates correct class depending on type passed.
        
        
        For nodes:
            MObject
            MObjectHandle
            MDagPath
            string/unicode
        
        For attributes:
            MPlug
            MDagPath, MPlug
            string/unicode
        """
        pass

    __apiobjects__ = {}


class NodeTracker(object):
    """
    A class for tracking Maya Objects as they are created and deleted.
    Can (and probably should) be used as a context manager
    """

    def __enter__(self): pass

    def __exit__(self, exctype, excval, exctb): pass

    def __init__(self): pass

    def endTrack(self):
        """
        Stop tracking and remove the callback
        """
        pass

    def getNodes(self, returnType="'PyNode'"):
        """
        Return a list of maya objects as strings.
        
        Parameters
        ----------
        returnType : str
            {'PyNode', 'str', 'MObject'}
        """
        pass

    def isTracking(self):
        """
        Return True/False
        """
        pass

    def reset(self): pass

    def startTrack(self): pass

    __dict__ = None

    __weakref__ = None


class Scene(object):
    """
    The Scene class provides an attribute-based method for retrieving `PyNode` instances of
    nodes in the current scene.
    
        >>> SCENE = Scene()
        >>> SCENE.persp
        nt.Transform(u'persp')
        >>> SCENE.persp.t
        Attribute(u'persp.translate')
    
    An instance of this class is provided for you with the name `SCENE`.
    """

    def __getattr__(self, obj): pass

    @staticmethod
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
        pass

    __dict__ = None

    __weakref__ = None


class ComponentIndex(tuple):
    """
    Class used to specify a multi-dimensional component index.
    
    If the length of a ComponentIndex object < the number of dimensions,
    then the remaining dimensions are taken to be 'complete' (ie, have not yet
    had indices specified).
    """

    def __add__(self, other): pass

    def __repr__(self): pass

    @staticmethod
    def __new__(cls, *args, **kwargs):
        """
        Parameters
        ----------
        label : str
            Component label for this index.
            Useful for components whose 'mel name' may vary - ie, an isoparm
            may be specified as u, v, or uv.
        """
        pass

    __dict__ = None


class AmbiguityWarning(exceptions.Warning):
    __weakref__ = None


class MayaObjectError(exceptions.TypeError):
    """
    # -------------------------
    # PyNode Exceptions
    # -------------------------
    """

    def __init__(self, node='None'): pass

    def __str__(self): pass

    __weakref__ = None


class MayaAttributeError(MayaObjectError, exceptions.AttributeError):
    pass


class Component(PyNode):
    """
    Abstract base class for pymel components.
    """

    def __apicomponent__(self): pass

    def __apihandle__(self): pass

    def __apimdagpath__(self):
        """
        Return the MDagPath for the node of this component, if it is valid
        """
        pass

    def __apimfn__(self): pass

    def __apimobject__(self):
        """
        get the MObject for this component if it is valid
        """
        pass

    def __apiobject__(self): pass

    def __eq__(self, other): pass

    def __init__(self, *args, **kwargs): pass

    def __melobject__(self): pass

    def __nonzero__(self):
        """
        Returns
        -------
        bool
        """
        pass

    def __str__(self): pass

    def __unicode__(self): pass

    def isComplete(self, *args, **kwargs): pass

    def name(self): pass

    def namespace(self, *args, **kwargs): pass

    def node(self): pass

    def plugAttr(self): pass

    def plugNode(self): pass

    @staticmethod
    def numComponentsFromStrings(*componentStrings):
        """
        Does basic string processing to count the number of components
        given a number of strings, which are assumed to be the valid mel names
        of components.
        """
        pass

    __readonly__ = {}


class Attribute(PyNode):
    """
    Attribute class
    
    see pymel docs for details on usage
    """

    def __apimattr__(self):
        """
        Return the MFnAttribute for this attribute, if it is valid
        """
        pass

    def __apimdagpath__(self):
        """
        Return the MDagPath for the node of this attribute, if it is valid
        """
        pass

    def __apimobject__(self):
        """
        Return the MObject for this attribute, if it is valid
        """
        pass

    def __apimplug__(self):
        """
        Return the MPlug for this attribute, if it is valid
        """
        pass

    def __apiobject__(self):
        """
        Return the default API object (MPlug) for this attribute, if it is valid
        """
        pass

    def __call__(self, *args, **kwargs): pass

    def __delitem__(self, index='None', break_='False'):
        """
        Parameters
        ----------
        index : Optional[Union[int, Iterable[int]]]
        break_ : bool
        """
        pass

    def __eq__(self, other):
        """
        Returns
        -------
        bool
        """
        pass

    def __floordiv__(self, other):
        """
        operator for 'disconnectAttr'
        
            >>> from pymel.core import *
            >>> SCENE.persp.tx >> SCENE.top.tx  # connect
            >>> SCENE.persp.tx // SCENE.top.tx  # disconnect
        """
        pass

    def __getattr__(self, attr): pass

    def __getitem__(self, index):
        """
        This method will find and return a plug with the given logical index. The logical index is the sparse array index used in MEL scripts. If a plug does not exist at the given Index, Maya will create a plug at that index. This is not the case with elementByPhysicalIndex(). If needed, elementByLogicalIndex can be used to expand an array plug on a node. It is important to note that Maya assumes that all such plugs serve a purpose and it will not free non-networked plugs that result from such an array expansion.
        
        Parameters:
        index : 'int'
            The index of the plug to be found
        
        
        Returns:
        'PyNode'
        
        Derived from api method `maya.OpenMaya.MPlug.elementByLogicalIndex`
        
        Aliases: __getitem__, elementByLogicalIndex
        """
        pass

    def __hash__(self):
        """
        Returns
        -------
        int
        """
        pass

    def __iter__(self):
        """
        iterator for multi-attributes
        
            >>> from pymel.core import *
            >>> f=newFile(f=1) #start clean
            >>>
            >>> at = PyNode( 'defaultLightSet.dagSetMembers' )
            >>> nt.SpotLight()
            nt.SpotLight(u'spotLightShape1')
            >>> nt.SpotLight()
            nt.SpotLight(u'spotLightShape2')
            >>> nt.SpotLight()
            nt.SpotLight(u'spotLightShape3')
            >>> for x in at: print x
            ...
            defaultLightSet.dagSetMembers[0]
            defaultLightSet.dagSetMembers[1]
            defaultLightSet.dagSetMembers[2]
        """
        pass

    def __ne__(self, other):
        """
        Returns
        -------
        bool
        """
        pass

    def __rshift__(self, other):
        """
        operator for 'connectAttr'
        
            >>> from pymel.core import *
            >>> SCENE.persp.tx >> SCENE.top.tx  # connect
            >>> SCENE.persp.tx // SCENE.top.tx  # disconnect
        """
        pass

    def __str__(self):
        """
        Returns
        -------
        str
        """
        pass

    def __unicode__(self):
        """
        Returns
        -------
        unicode
        """
        pass

    def affected(self):
        """
        Returns
        -------
        List[Attribute]
        """
        pass

    def affects(self):
        """
        Returns
        -------
        List[Attribute]
        """
        pass

    def array(self):
        """
        Returns the array (multi) attribute of the current element:
        
            >>> n = Attribute(u'initialShadingGroup.groupNodes[0]')
            >>> n.isElement()
            True
            >>> n.array()
            Attribute(u'initialShadingGroup.groupNodes')
        
        This method will raise an error for attributes which are not elements of
        an array:
        
            >>> m = Attribute(u'initialShadingGroup.groupNodes')
            >>> m.isElement()
            False
            >>> m.array()
            Traceback (most recent call last):
            ...
            TypeError: initialShadingGroup.groupNodes is not an array (multi) attribute
        
        Returns
        -------
        Attribute
        """
        pass

    def attr(self, attr):
        """
        Returns
        -------
        Attribute
        """
        pass

    def attrName(self, longName='False', includeNode='False'):
        """
        Just the name of the attribute for this plug
        
        This will have no indices, no parent attributes, etc...
        This is suitable for use with cmds.attributeQuery
        
            >>> at = SCENE.persp.instObjGroups.objectGroups
            >>> at.name()
            u'persp.instObjGroups[-1].objectGroups'
            >>> at.attrName()
            u'og'
            >>> at.attrName(longName=True)
            u'objectGroups'
        """
        pass

    def children(self):
        """
        attributeQuery -listChildren
        
        Returns
        -------
        List[Attribute]
        """
        pass

    def connect(source, destination, **kwargs):
        """
        Connect the attributes of two dependency nodes and return the names of the two
        connected attributes. The connected attributes must be be of compatible types.
        First argument is the source attribute, second one is the destination. Refer to
        dependency node documentation.
        
        Maya Bug Fix:
          - even with the 'force' flag enabled, the command would raise an error if the connection already existed.
        
        Flags:
        - force : f                      (bool)          [create]
            Forces the connection.  If the destination is already connected, the old
            connection is broken and the new one made.
        
        - lock : l                       (bool)          [create]
            If the argument is true, the destination attribute is locked after making the
            connection. If the argument is false, the connection is unlocked before making
            the connection.
        
        - nextAvailable : na             (bool)          [create]
            If the destination multi-attribute has set the indexMatters to be false with
            this flag specified, a connection is made to the next available index. No index
            need be specified.
        
        - referenceDest : rd             (unicode)       [create]
            This flag is used for file io only. The flag indicates that the connection
            replaces a connection made in a referenced file, and the flag argument indicates
            the original destination from the referenced file. This flag is used so that if
            the reference file is modified, maya can still attempt to make the appropriate
            connections in the main scene to the referenced object.                  Flag
            can have multiple arguments, passed either as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.connectAttr`
        """
        pass

    def delete(self):
        """
        deleteAttr
        """
        pass

    def destinations(self):
        """
        If this plug is a source, return the destination plugs connected to it.
        
        Returns:
        Tuple['bool', List['PyNode']]
        
        Derived from api method `maya.OpenMaya.MPlug.destinations`
        """
        pass

    def destinationsWithConversions(self):
        """
        If this plug is a source, return the destination plugs connected to it.
        
        Returns:
        Tuple['bool', List['PyNode']]
        
        Derived from api method `maya.OpenMaya.MPlug.destinationsWithConversions`
        """
        pass

    def disconnect(source, destination='None', inputs='None', outputs='None', **kwargs):
        """
        Disconnects two connected attributes. First argument is the source attribute,
        second is the destination.
        
        Modifications:
          - If no destination is passed, then all inputs will be disconnected if inputs
              is True, and all outputs will be disconnected if outputs is True; if
              neither are given (or both are None), both all inputs and all outputs
              will be disconnected
        
        Flags:
        - nextAvailable : na             (bool)          [create]
            If the destination multi-attribute has set the indexMatters to be false, the
            command will disconnect the first matching connection.  No index needs to be
            specified.                  Flag can have multiple arguments, passed either as a
            tuple or a list.
        
        
        Derived from mel command `maya.cmds.disconnectAttr`
        """
        pass

    def elementByLogicalIndex(self, index):
        """
        This method will find and return a plug with the given logical index. The logical index is the sparse array index used in MEL scripts. If a plug does not exist at the given Index, Maya will create a plug at that index. This is not the case with elementByPhysicalIndex(). If needed, elementByLogicalIndex can be used to expand an array plug on a node. It is important to note that Maya assumes that all such plugs serve a purpose and it will not free non-networked plugs that result from such an array expansion.
        
        Parameters:
        index : 'int'
            The index of the plug to be found
        
        
        Returns:
        'PyNode'
        
        Derived from api method `maya.OpenMaya.MPlug.elementByLogicalIndex`
        
        Aliases: __getitem__, elementByLogicalIndex
        """
        pass

    def elementByPhysicalIndex(self, index):
        """
        This method will find and return a plug with the given physical index. The index can range from 0 to numElements() - 1. This function is particularly useful for iteration through the element plugs of an array plug. It is equivalent to operator [] (int) This method is only valid for array plugs.
        
        Parameters:
        index : 'int'
            The physical array index of the plug to be found
        
        
        Returns:
        'PyNode'
        
        Derived from api method `maya.OpenMaya.MPlug.elementByPhysicalIndex`
        """
        pass

    def elements(self):
        """
        ``listAttr -multi``
        
        Return a list of strings representing all the attributes in the array.
        
        If you don't need actual strings, it is recommended that you simply iterate through the elements in the array.
        See `Attribute.__iter__`.
        
        Modifications:
          - returns an empty list when the result is None
        
        Returns
        -------
        List[unicode]
        """
        pass

    def evaluate(self, **kwargs): pass

    def evaluateNumElements(self):
        """
        Return the total number of elements in the datablock of this array plug. The return count will include both connected and non-connected elements, and will perform an evaluate in order to make sure that the datablock is as up-to-date as possible since some nodes do not place array elements into the datablock until the attribute is evaluated.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.evaluateNumElements`
        """
        pass

    def exists(self):
        """
        Whether the attribute actually exists.
        
        In spirit, similar to 'attributeQuery -exists'...
        ...however, also handles multi (array) attribute elements, such as
        plusMinusAverage.input1D[2]
        
        Returns
        -------
        bool
        """
        pass

    def firstParent(*args, **kwargs):
        """
        The function '{objName}' is deprecated and will become unavailable in future pymel versions. use Attribute.getParent instead
        
        deprecated: use getParent instead
        """
        pass

    def get(attr, default='None', **kwargs):
        """
        This command returns the value of the named object's attribute. UI units are
        used where applicable. Currently, the types of attributes that can be displayed
        are: numeric attributesstring attributesmatrix attributesnumeric compound
        attributes (whose children are all numeric)vector array attributesdouble array
        attributesint32 array attributespoint array attributesdata component list
        attributesOther data types cannot be retrieved. No result is returned if the
        attribute contains no data.
        
        Maya Bug Fix:
          - maya pointlessly returned vector results as a tuple wrapped in a list ( ex.  '[(1,2,3)]' ). This command unpacks the vector for you.
        
        Modifications:
          - casts double3 datatypes to `Vector`
          - casts matrix datatypes to `Matrix`
          - casts vectorArrays from a flat array of floats to an array of Vectors
          - when getting a multi-attr, maya would raise an error, but pymel will return a list of values for the multi-attr
          - added a default argument. if the attribute does not exist and this argument is not None, this default value will be returned
          - added support for getting message attributes
        
        Flags:
        - asString : asString            (bool)          [create]
            This flag is only valid for enum attributes. It allows you to get the attribute
            values as strings instead of integer values. Note that the returned string value
            is dependent on the UI language Maya is running in (about -uiLanguage).
        
        - caching : ca                   (bool)          [create]
            Returns whether the attribute is set to be cached internally
        
        - channelBox : cb                (bool)          [create]
            Returns whether the attribute is set to show in the channelBox. Keyable
            attributes also show in the channel box.
        
        - expandEnvironmentVariables : x (bool)          [create]
            Expand any environment variable and (tilde characters on UNIX) found in string
            attributes which are returned.
        
        - keyable : k                    (bool)          [create]
            Returns the keyable state of the attribute.
        
        - lock : l                       (bool)          [create]
            Returns the lock state of the attribute.
        
        - multiIndices : mi              (bool)          [create]
            If the attribute is a multi, this will return a list containing all of the valid
            indices for the attribute.
        
        - settable : se                  (bool)          [create]
            Returns 1 if this attribute is currently settable by setAttr, 0 otherwise. An
            attribute is settable if it's not locked and either not connected, or has only
            keyframed animation.
        
        - silent : sl                    (bool)          [create]
            When evaluating an attribute that is not a numeric or string value, suppress the
            error message saying that the data cannot be displayed. The attribute will be
            evaluated even though its data cannot be displayed. This flag does not suppress
            all error messages, only those that are benign.
        
        - size : s                       (bool)          [create]
            Returns the size of a multi-attribute array.  Returns 1 if non-multi.
        
        - time : t                       (time)          [create]
            Evaluate the attribute at the given time instead of the current time.
        
        - type : typ                     (bool)          [create]
            Returns the type of data currently in the attribute. Attributes of simple types
            such as strings and numerics always contain data, but attributes of complex
            types (arrays, meshes, etc) may contain no data if none has ever been assigned
            to them. When this happens the command will return with no result: not an empty
            string, but no result at all. Attempting to directly compare this non-result to
            another value or use it in an expression will result in an error, but you can
            assign it to a variable in which case the variable will be set to the default
            value for its type (e.g. an empty string for a string variable, zero for an
            integer variable, an empty array for an array variable). So to be safe when
            using this flag, always assign its result to a string variable, never try to use
            it directly.                   Flag can have multiple arguments, passed either
            as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.getAttr`
        """
        pass

    def getAlias(self, **kwargs):
        """
        Returns the alias for this attribute, or None.
        
        The alias of the attribute is set through
        Attribute.setAlias, or the aliasAttr command.
        """
        pass

    def getAllParents(self, arrays='False'):
        """
        Return a list of all parents above this.
        
        Starts from the parent immediately above, going up.
        
        Returns
        -------
        List[Attribute]
        """
        pass

    def getArrayIndices(self):
        """
        Get all set or connected array indices. Raises an error if this is not an array Attribute
        
        Returns
        -------
        List[int]
        """
        pass

    def getChildren(self):
        """
        attributeQuery -listChildren
        
        Returns
        -------
        List[Attribute]
        """
        pass

    def getDefault(self): pass

    def getEnums(attr):
        """
        Get the enumerators for an enum attribute.
        
        Parameters
        ----------
        attr : Union[unicode, Attribute]
        
        Returns
        -------
        _util.enum.EnumDict
        
        Examples
        --------
        >>> addAttr( "persp", ln='numbers', at='enum', enumName="zero:one:two:thousand=1000:three")
        >>> numbers = Attribute('persp.numbers').getEnums()
        >>> sorted(numbers.items())
        [(u'one', 1), (u'thousand', 1000), (u'three', 1001), (u'two', 2), (u'zero', 0)]
        >>> numbers[1]
        u'one'
        >>> numbers['thousand']
        1000
        """
        pass

    def getMax(self):
        """
        attributeQuery -max
            Returns None if max does not exist.
        
        Returns
        -------
        float
        """
        pass

    def getMin(self):
        """
        attributeQuery -min
            Returns None if min does not exist.
        
        Returns
        -------
        float
        """
        pass

    def getNumElements(self):
        """
        Return the total number of elements in the datablock of this array plug. The return count will include all existing non-connected elements plus connected elements if they have been evaluated. It will not include connected elements that have not yet been placed into the datablock. The method MPlug::evaluateNumElements can be used in the sitution where you want an accurate count that includes all connected elements.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.numElements`
        """
        pass

    def getParent(self, generations='1', arrays='False'):
        """
        Modifications:
            - added optional generations keyword arg, which gives the number of
              levels up that you wish to go for the parent
        
              Negative values will traverse from the top.
        
              A value of 0 will return the same node.
              The default value is 1.
        
              If generations is None, it will be interpreted as 'return all
              parents', and a list will be returned.
        
              Since the original command returned None if there is no parent,
              to sync with this behavior, None will be returned if generations
              is out of bounds (no IndexError will be thrown).
        
            - added optional arrays keyword arg, which if True, will also
              traverse from an array element to an array plug
        
        Returns
        -------
        Attribute
        """
        pass

    def getRange(self):
        """
        attributeQuery -range
            returns a two-element list containing min and max. if the attribute does not have
            a softMin or softMax the corresponding element will be set to None.
        
        Returns
        -------
        List[float]
        """
        pass

    def getSetAttrCmds(self, valueSelector="'all'", useLongNames='False'):
        """
        Returns an array of strings containing setAttr commands for this plug and all of its descendent plugs.
        
        Parameters:
        valueSelector : 'Attribute.MValueSelector'
            kAll- return setAttr commands for the plug and its children, regardless of their values. kNonDefault- only return setAttr commands for the plug or its children if they are not at their default values. kChanged- for nodes from referenced files, setAttr commands are only returned if the plug or one of its children has changed since its file was loaded. For all other nodes, the behaviour is the same a kNonDefault. Note that if the plug is compound and one of its children has changed, then setAttrs will be generated for all of its children, even those which have not changed. (default: kAll)
        
            values: 'all', 'nonDefault', 'changed', 'lastAttrSelector'
        useLongNames : 'bool'
            Normally, the returned commands will use the short names for flags and attributes. If this parameter is true then their long names will be used instead. (default: false)
        
        
        Returns:
        List['list']
        
        Derived from api method `maya.OpenMaya.MPlug.getSetAttrCmds`
        """
        pass

    def getSiblings(self):
        """
        attributeQuery -listSiblings
        
        Returns
        -------
        Optional[List[Attribute]]
        """
        pass

    def getSoftMax(self):
        """
        attributeQuery -softMax
            Returns None if softMax does not exist.
        
        Returns
        -------
        float
        """
        pass

    def getSoftMin(self):
        """
        attributeQuery -softMin
            Returns None if softMin does not exist.
        
        Returns
        -------
        float
        """
        pass

    def getSoftRange(self):
        """
        attributeQuery -softRange
            returns a two-element list containing softMin and softMax. if the attribute does not have
            a softMin or softMax the corresponding element in the list will be set to None.
        
        Returns
        -------
        List[float]
        """
        pass

    def index(self):
        """
        Returns the logical index of the element this plug refers to. The logical index is a sparse index, equivalent to the array index used in MEL.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.logicalIndex`
        
        Aliases: index, item, logicalIndex
        """
        pass

    def indexMatters(self): pass

    def info(self):
        """
        This method returns a string containing the name of the node this plug belongs to and the attributes that the plug refers to. The string is of the form dependNode:atr1.atr2[].attr3 ...
        
        Returns:
        'unicode'
        
        Derived from api method `maya.OpenMaya.MPlug.info`
        """
        pass

    def inputs(self, **kwargs):
        """
        ``listConnections -source 1 -destination 0``
        
        see `Attribute.connections` for the full ist of flags.
        
        Returns
        -------
        List[PyNode]
        """
        pass

    def insertInput(self, node, nodeOutAttr, nodeInAttr):
        """
        connect the passed node.outAttr to this attribute and reconnect
        any pre-existing connection into node.inAttr.  if there is no
        pre-existing connection, this method works just like connectAttr.
        
        for example, for two nodes with the connection::
        
            a.out-->b.in
        
        running this command::
        
            b.in.insertInput( 'c', 'out', 'in' )
        
        causes the new connection order (assuming 'c' is a node with 'in' and 'out' attributes)::
        
            a.out-->c.in
            c.out-->b.in
        """
        pass

    def isArray(self):
        """
        This method determines if the plug is an array plug. Array plugs refer to array attributes and contain element plugs.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isArray`
        
        Aliases: isArray, isMulti
        """
        pass

    def isCaching(self):
        """
        Returns true if this plug or its attribute has its caching flag set.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isCachingFlagSet`
        """
        pass

    def isChild(self):
        """
        This method determines if the plug is a child plug. A child plug's parent is always a compound plug.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isChild`
        """
        pass

    def isCompound(self):
        """
        This method determines if the plug is a compound plug. Compound plugs refer to compound attributes and have child plugs.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isCompound`
        """
        pass

    def isConnectable(self):
        """
        attributeQuery -connectable
        
        Returns
        -------
        bool
        """
        pass

    def isConnected(self):
        """
        Determines if this plug is connected to one or more plugs.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isConnected`
        """
        pass

    def isConnectedTo(self, other, ignoreUnitConversion='False', checkLocalArray='False', checkOtherArray='False'):
        """
        Determine if the attribute is connected to the passed attribute.
        
        If checkLocalArray is True and the current attribute is a multi/array, the current attribute's elements will also be tested.
        
        If checkOtherArray is True and the passed attribute is a multi/array, the passed attribute's elements will also be tested.
        
        If checkLocalArray and checkOtherArray are used together then all element combinations will be tested.
        
        Returns
        -------
        bool
        """
        pass

    def isDefaultValue(self, forceEval='True'):
        """
        This method determines if the plug value is equivalent to the plug's default value.
        
        Parameters:
        forceEval : 'bool'
            Evaluate the plug prior to test.
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isDefaultValue`
        """
        pass

    def isDestination(self):
        """
        Determines if this plug is connected as a destination.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isDestination`
        """
        pass

    def isDirty(self, **kwargs):
        """
        Returns
        -------
        bool
        """
        pass

    def isDynamic(self):
        """
        Determines whether the attribute is of dynamic type or not.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isDynamic`
        """
        pass

    def isElement(self):
        """
        This method determines if the plug is an element plug. Element plugs refer to array attributes and are members of array plugs.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isElement`
        """
        pass

    def isFreeToChange(self, checkParents='True', checkChildren='True'):
        """
        Returns true if the plug's value is allowed to be set directly. A plug isFreeToChange if it is not locked, and it is not a destination or if it is a destination, then it must be a special case (such as connected to an anim curve).
        
        Parameters:
        checkParents : 'bool'
            Check parent plugs.
        checkChildren : 'bool'
            Check child plugs.
        
        
        Returns:
        'Attribute.FreeToChangeState'
        
        Derived from api method `maya.OpenMaya.MPlug.isFreeToChange`
        """
        pass

    def isFromReferencedFile(self):
        """
        This method determines whether this plug came from a referenced file. A plug is considered to have come from a referenced file if it is connected and that connection was made within a referenced file.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isFromReferencedFile`
        """
        pass

    def isHidden(self):
        """
        attributeQuery -hidden
        
        Returns
        -------
        bool
        """
        pass

    def isIgnoredWhenRendering(self):
        """
        Determines whether a connection to the attribute should be ignored during rendering.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isIgnoredWhenRendering`
        """
        pass

    def isInChannelBox(self):
        """
        Returns true if this plug or its attribute has its channel box flag set. Attributes will appear in the channel box if their channel box flag is set or if they are keyable.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isChannelBoxFlagSet`
        """
        pass

    def isKeyable(self):
        """
        Determines if this plug is keyable. The default keyability of a plug is determined by its attribute, and can be retrieved using MFnAttribute::isKeyable. Keyable plugs will be keyed by AutoKey and the Set Keyframe UI. Non-keyable plugs prevent the user from setting keys via the obvious UI provided for keying. Being non-keyable is not a hard block against adding keys to an attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isKeyable`
        """
        pass

    def isLocked(self):
        """
        Determines the locked state of this plug's value. A plug's locked state determines whether or not the plug's value can be changed.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isLocked`
        """
        pass

    def isMulti(self):
        """
        This method determines if the plug is an array plug. Array plugs refer to array attributes and contain element plugs.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isArray`
        
        Aliases: isArray, isMulti
        """
        pass

    def isMuted(self):
        """
        mute -q
        
        Returns
        -------
        bool
        """
        pass

    def isNetworked(self):
        """
        This method determines if the plug is networked or non-networked.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isNetworked`
        """
        pass

    def isNull(self):
        """
        This method determines whether this plug is valid. A plug is valid if it refers to an attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isNull`
        """
        pass

    def isProcedural(self):
        """
        This method determines if the plug is a procedural plug. A procedural plug is one which is created by Maya's internal procedures or by the nodes themselves and which should not be saved to or restored from files.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isProcedural`
        """
        pass

    def isSettable(self):
        """
        getAttr -settable
        
        Returns
        -------
        bool
        """
        pass

    def isSource(self):
        """
        Determines if this plug is connected as a source.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MPlug.isSource`
        """
        pass

    def isUsedAsColor(self):
        """
        attributeQuery -usedAsColor
        
        Returns
        -------
        bool
        """
        pass

    def item(self):
        """
        Returns the logical index of the element this plug refers to. The logical index is a sparse index, equivalent to the array index used in MEL.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.logicalIndex`
        
        Aliases: index, item, logicalIndex
        """
        pass

    def iterDescendants(self, levels='None', leavesOnly='False'):
        """
        Yields all attributes "below" this attribute, recursively,
        traversing down both through multi/array elements, and through
        compound attribute children.
        
        Parameters
        ----------
        levels : Optional[int]
            the number of levels deep to descend; each descent from an array
            to an array element, and from a compound to it's child, counts as
            one level (so, if you have a compound-multi attr parentAttr, to get
            to parentAttr[0].child would require levels to be at least 2); None
            means no limit
        leavesOnly : bool
            if True, then results will only be returned if they do not have any
            children to recurse into (either because it's not an arry or
            compound, or because we've hit the levels limit)
        
        Returns
        -------
        Iterator[Attribute]
        """
        pass

    def lastPlugAttr(self, longName='False'):
        """
            >>> from pymel.core import *
            >>> at = SCENE.persp.t.tx
            >>> at.lastPlugAttr(longName=False)
            u'tx'
            >>> at.lastPlugAttr(longName=True)
            u'translateX'
        
        Returns
        -------
        unicode
        """
        pass

    def lock(self, checkReference='False'):
        """
        setAttr -locked 1
        """
        pass

    def logicalIndex(self):
        """
        Returns the logical index of the element this plug refers to. The logical index is a sparse index, equivalent to the array index used in MEL.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.logicalIndex`
        
        Aliases: index, item, logicalIndex
        """
        pass

    def longName(self, fullPath='False'):
        """
            >>> from pymel.core import *
            >>> at = SCENE.persp.t.tx
            >>> at.longName(fullPath=False)
            u'translateX'
            >>> at.longName(fullPath=True)
            u'translate.translateX'
        
        Returns
        -------
        unicode
        """
        pass

    def mute(self, **kwargs):
        """
        mute
         Mutes the attribute.
        """
        pass

    def name(self, includeNode='True', longName='True', fullAttrPath='False', fullDagPath='False',
             placeHolderIndices='True'):
        """
        Returns the name of the attribute (plug)
        
            >>> tx = SCENE.persp.t.tx
            >>> tx.name()
            u'persp.translateX'
            >>> tx.name(includeNode=False)
            u'translateX'
            >>> tx.name(longName=False)
            u'persp.tx'
            >>> tx.name(fullAttrPath=True, includeNode=False)
            u'translate.translateX'
        
            >>> vis = SCENE.perspShape.visibility
            >>> vis.name()
            u'perspShape.visibility'
            >>> vis.name(fullDagPath=True)
            u'|persp|perspShape.visibility'
        
            >>> og = SCENE.persp.instObjGroups.objectGroups
            >>> og.name()
            u'persp.instObjGroups[-1].objectGroups'
            >>> og.name(placeHolderIndices=False)
            u'persp.instObjGroups.objectGroups'
        
        Returns
        -------
        unicode
        """
        pass

    def namespace(self, *args, **kwargs): pass

    def node(self):
        """
        plugNode
        
        Returns
        -------
        nodetypes.DependNode
        """
        pass

    def nodeName(self):
        """
        The node part of this plug as a string
        
        Returns
        -------
        unicode
        """
        pass

    def numChildren(self):
        """
        Return the total number of children of this compound plug.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.numChildren`
        """
        pass

    def numConnectedChildren(self):
        """
        Return the number of children of this plug that are connected in the dependency graph.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.numConnectedChildren`
        """
        pass

    def numConnectedElements(self):
        """
        Return the total number of connected element plugs belonging to this array plug.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MPlug.numConnectedElements`
        """
        pass

    def numElements(self):
        """
        The number of elements in an array attribute. Raises an error if this is not an array Attribute
        
        Be aware that ``getAttr(..., size=1)`` does not always produce the expected value. It is recommend
        that you use `Attribute.numElements` instead.  This is a maya bug, *not* a pymel bug.
        
            >>> from pymel.core import *
            >>> f=newFile(f=1) #start clean
            >>>
            >>> dls = SCENE.defaultLightSet
            >>> dls.dagSetMembers.numElements()
            0
            >>> nt.SpotLight() # create a light, which adds to the lightSet
            nt.SpotLight(u'spotLightShape1')
            >>> dls.dagSetMembers.numElements()
            1
            >>> nt.SpotLight() # create another light, which adds to the lightSet
            nt.SpotLight(u'spotLightShape2')
            >>> dls.dagSetMembers.numElements()
            2
        
        Returns
        -------
        int
        """
        pass

    def outputs(self, **kwargs):
        """
        ``listConnections -source 0 -destination 1``
        
        see `Attribute.connections` for the full ist of flags.
        
        Returns
        -------
        List[PyNode]
        """
        pass

    def parent(self, generations='1', arrays='False'):
        """
        Modifications:
            - added optional generations keyword arg, which gives the number of
              levels up that you wish to go for the parent
        
              Negative values will traverse from the top.
        
              A value of 0 will return the same node.
              The default value is 1.
        
              If generations is None, it will be interpreted as 'return all
              parents', and a list will be returned.
        
              Since the original command returned None if there is no parent,
              to sync with this behavior, None will be returned if generations
              is out of bounds (no IndexError will be thrown).
        
            - added optional arrays keyword arg, which if True, will also
              traverse from an array element to an array plug
        
        Returns
        -------
        Attribute
        """
        pass

    def plugAttr(self, longName='False', fullPath='False'):
        """
            >>> from pymel.core import *
            >>> at = SCENE.persp.t.tx
            >>> at.plugAttr(longName=False, fullPath=False)
            u'tx'
            >>> at.plugAttr(longName=False, fullPath=True)
            u't.tx'
            >>> at.plugAttr(longName=True, fullPath=True)
            u'translate.translateX'
        
        Returns
        -------
        unicode
        """
        pass

    def plugNode(self):
        """
        plugNode
        
        Returns
        -------
        nodetypes.DependNode
        """
        pass

    def remove(self, **kwargs):
        """
        removeMultiInstance
        """
        pass

    def removeMultiInstance(self, index='None', break_='False'):
        """
        Parameters
        ----------
        index : Optional[Union[int, Iterable[int]]]
        break_ : bool
        """
        pass

    def set(attr, *args, **kwargs):
        """
        Sets the value of a dependency node attribute.  No value for the the attribute
        is needed when the -l/-k/-s flags are used. The -type flag is only required when
        setting a non-numeric attribute. The following chart outlines the syntax of
        setAttr for non-numeric data types: TYPEbelow means any number of values of type
        TYPE, separated by a space[TYPE]means that the value of type TYPEis
        optionalA|Bmeans that either of Aor Bmay appearIn order to run its examples,
        first execute these commands to create the sample attribute types:sphere -n
        node; addAttr -ln short2Attr -at short2; addAttr -ln short2a -p short2Attr -at
        short; addAttr -ln short2b -p short2Attr -at short; addAttr -ln short3Attr -at
        short3; addAttr -ln short3a -p short3Attr -at short; addAttr -ln short3b -p
        short3Attr -at short; addAttr -ln short3c -p short3Attr -at short; addAttr -ln
        long2Attr -at long2; addAttr -ln long2a -p long2Attr -at long; addAttr -ln
        long2b -p long2Attr -at long; addAttr -ln long3Attr -at long3; addAttr -ln
        long3a -p long3Attr -at long; addAttr -ln long3b -p long3Attr -at long; addAttr
        -ln long3c -p long3Attr -at long; addAttr -ln float2Attr -at float2; addAttr -ln
        float2a -p float2Attr -at float; addAttr -ln float2b -p float2Attr -at float;
        addAttr -ln float3Attr -at float3; addAttr -ln float3a -p float3Attr -at float;
        addAttr -ln float3b -p float3Attr -at float; addAttr -ln float3c -p float3Attr
        -at float; addAttr -ln double2Attr -at double2; addAttr -ln double2a -p
        double2Attr -at double; addAttr -ln double2b -p double2Attr -at double; addAttr
        -ln double3Attr -at double3; addAttr -ln double3a -p double3Attr -at double;
        addAttr -ln double3b -p double3Attr -at double; addAttr -ln double3c -p
        double3Attr -at double; addAttr -ln int32ArrayAttr -dt Int32Array; addAttr -ln
        doubleArrayAttr -dt doubleArray; addAttr -ln pointArrayAttr -dt pointArray;
        addAttr -ln vectorArrayAttr -dt vectorArray; addAttr -ln stringArrayAttr -dt
        stringArray; addAttr -ln stringAttr -dt string; addAttr -ln matrixAttr -dt
        matrix; addAttr -ln sphereAttr -dt sphere; addAttr -ln coneAttr -dt cone;
        addAttr -ln meshAttr -dt mesh; addAttr -ln latticeAttr -dt lattice; addAttr -ln
        spectrumRGBAttr -dt spectrumRGB; addAttr -ln reflectanceRGBAttr -dt
        reflectanceRGB; addAttr -ln componentListAttr -dt componentList; addAttr -ln
        attrAliasAttr -dt attributeAlias; addAttr -ln curveAttr -dt nurbsCurve; addAttr
        -ln surfaceAttr -dt nurbsSurface; addAttr -ln trimFaceAttr -dt nurbsTrimface;
        addAttr -ln polyFaceAttr -dt polyFaces; -type short2Array of two short
        integersValue Syntaxshort shortValue Meaningvalue1 value2Mel ExamplesetAttr
        node.short2Attr -type short2 1 2;Python
        Examplecmds.setAttr('node.short2Attr',1,2,type='short2')-type short3Array of
        three short integersValue Syntaxshort short shortValue Meaningvalue1 value2
        value3Mel ExamplesetAttr node.short3Attr -type short3 1 2 3;Python
        Examplecmds.setAttr('node.short3Attr',1,2,3,type='short3')-type long2Array of
        two long integersValue Syntaxlong longValue Meaningvalue1 value2Mel
        ExamplesetAttr node.long2Attr -type long2 1000000 2000000;Python
        Examplecmds.setAttr('node.long2Attr',1000000,2000000,type='long2')-type
        long3Array of three long integersValue Syntaxlong long longValue Meaningvalue1
        value2 value3Mel ExamplesetAttr node.long3Attr -type long3 1000000 2000000
        3000000;Python
        Examplecmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')-type
        Int32ArrayVariable length array of long integersValue SyntaxValue MeaningMel
        ExamplesetAttr node.int32ArrayAttr -type Int32Array 2 12 75;Python
        Examplecmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')-type
        float2Array of two floatsValue Syntaxfloat floatValue Meaningvalue1 value2Mel
        ExamplesetAttr node.float2Attr -type float2 1.1 2.2;Python
        Examplecmds.setAttr('node.float2Attr',1.1,2.2,type='float2')-type float3Array of
        three floatsValue Syntaxfloat float floatValue Meaningvalue1 value2 value3Mel
        ExamplesetAttr node.float3Attr -type float3 1.1 2.2 3.3;Python
        Examplecmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')-type
        double2Array of two doublesValue Syntaxdouble doubleValue Meaningvalue1
        value2Mel ExamplesetAttr node.double2Attr -type double2 1.1 2.2;Python
        Examplecmds.setAttr('node.double2Attr',1.1,2.2,type='double2')-type double3Array
        of three doublesValue Syntaxdouble double doubleValue Meaningvalue1 value2
        value3Mel ExamplesetAttr node.double3Attr -type double3 1.1 2.2 3.3;Python
        Examplecmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')-type
        doubleArrayVariable length array of doublesValue SyntaxValue MeaningMel
        ExamplesetAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;Python
        Examplecmds.setAttr( node.doubleArrayAttr, (2, 3.14159, 2.782,),
        type=doubleArray)-type matrix4x4 matrix of doublesValue Syntaxdouble double
        double doubledouble double double doubledouble double double doubledouble double
        double doubleValue Meaningrow1col1 row1col2 row1col3 row1col4row2col1 row2col2
        row2col3 row2col4row3col1 row3col2 row3col3 row3col4row4col1 row4col2 row4col3
        row4col4Alternate Syntaxstring double double doubledouble double
        doubleintegerdouble double doubledouble double doubledouble double doubledouble
        double doubledouble double doubledouble double doubledouble double double
        doubledouble double double doubledouble double doublebooleanAlternate
        MeaningxformscaleX scaleY scaleZrotateX rotateY rotateZrotationOrder (0=XYZ,
        1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)translateX translateY translateZshearXY
        shearXZ shearYZscalePivotX scalePivotY scalePivotZscaleTranslationX
        scaleTranslationY scaleTranslationZrotatePivotX rotatePivotY
        rotatePivotZrotateTranslationX rotateTranslationY
        rotateTranslationZrotateOrientW rotateOrientX rotateOrientY
        rotateOrientZjointOrientW jointOrientX jointOrientY
        jointOrientZinverseParentScaleX inverseParentScaleY
        inverseParentScaleZcompensateForParentScale Mel ExamplesetAttr node.matrixAttr
        -type matrix1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;setAttr node.matrixAttr -type
        matrixxform1 1 1 0 0 0 0 2 3 4 0 0 00 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1
        0 false;Python Examplecmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,
        3,4,1),type='matrix')cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2
        ,3,4),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,
        type=matrix)-type pointArrayVariable length array of pointsValue SyntaxValue
        MeaningMel ExamplesetAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2
        1;Python Examplecmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='p
        ointArray')-type vectorArrayVariable length array of vectorsValue SyntaxValue
        MeaningMel ExamplesetAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2
        2;Python Examplecmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vect
        orArray')-type stringCharacter stringValue SyntaxstringValue
        MeaningcharacterStringValueMel ExamplesetAttr node.stringAttr -type
        stringblarg;Python Examplecmds.setAttr('node.stringAttr',blarg,type=string)-type
        stringArrayVariable length array of stringsValue SyntaxValue MeaningMel
        ExamplesetAttr node.stringArrayAttr -type stringArray 3 abc;Python
        Examplecmds.setAttr('node.stringArrayAttr',3,a,b,c,type='stringArray')-type
        sphereSphere dataValue SyntaxdoubleValue MeaningsphereRadiusExamplesetAttr
        node.sphereAttr -type sphere 5.0;-type coneCone dataValue Syntaxdouble
        doubleValue MeaningconeAngle coneCapMel ExamplesetAttr node.coneAttr -type cone
        45.0 5.0;Python Examplecmds.setAttr('node.coneAttr',45.0,5.0,type='cone')-type
        reflectanceRGBReflectance dataValue Syntaxdouble double doubleValue
        MeaningredReflect greenReflect blueReflectMel ExamplesetAttr
        node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;Python Examplecmds.setA
        ttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')-type
        spectrumRGBSpectrum dataValue Syntaxdouble double doubleValue MeaningredSpectrum
        greenSpectrum blueSpectrumMel ExamplesetAttr node.spectrumRGBAttr -type
        spectrumRGB 0.5 0.5 0.1;Python
        Examplecmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')-type
        componentListVariable length array of componentsValue SyntaxValue MeaningMel
        ExamplesetAttr node.componentListAttr -type componentList 3 cv[1] cv[12]
        cv[3];Python Examplecmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv
        [3]',type='componentList')-type attributeAliasString alias dataValue
        Syntaxstring stringValue MeaningnewAlias currentNameMel ExamplesetAttr
        node.attrAliasAttr -type attributeAliasGoUp, translateY, GoLeft,
        translateX;Python Examplecmds.setAttr('node.attrAliasAttr',(GoUp,
        translateY,GoLeft, translateX),type='attributeAlias')-type nurbsCurveNURBS curve
        dataValue SyntaxValue MeaningMel Example// degree is the degree of the
        curve(range 1-7)// spans is the number of spans // form is open (0), closed (1),
        periodic (2)// dimension is 2 or 3, depending on the dimension of the curve//
        isRational is true if the curve CVs contain a rational component // knotCount is
        the size of the knot list//  knotValue is a single entry in the knot list//
        cvCount is the number of CVs in the curve//  xCVValue,yCVValue,[zCVValue]
        [wCVValue] is a single CV.//  zCVValue is only present when dimension is 3.//
        wCVValue is only present when isRational is true.//setAttr node.curveAttr -type
        nurbsCurve 3 1 0 no 36 0 0 0 1 1 14 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;-type
        nurbsSurfaceNURBS surface dataValue Syntaxint int int int bool Value
        MeaninguDegree vDegree uForm vForm isRationalTRIM|NOTRIMExample// uDegree is
        degree of the surface in U direction (range 1-7)// vDegree is degree of the
        surface in V direction (range 1-7)// uForm is open (0), closed (1), periodic (2)
        in U direction// vForm is open (0), closed (1), periodic (2) in V direction//
        isRational is true if the surface CVs contain a rational component// uKnotCount
        is the size of the U knot list//  uKnotValue is a single entry in the U knot
        list// vKnotCount is the size of the V knot list//  vKnotValue is a single entry
        in the V knot list// If TRIMis specified then additional trim information is
        expected// If NOTRIMis specified then the surface is not trimmed// cvCount is
        the number of CVs in the surface//  xCVValue,yCVValue,zCVValue [wCVValue]is a
        single CV.//  zCVValue is only present when dimension is 3.//  wCVValue is only
        present when isRational is true//setAttr node.surfaceAttr -type nurbsSurface 3 3
        0 0 no 6 0 0 0 1 1 16 0 0 0 1 1 116 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0-1 3 0 -1 1 0
        -1 -1 0 -1 -3 01 3 0 1 1 0 1 -1 0 1 -3 03 3 0 3 1 0 3 -1 0 3 -3 0;-type
        nurbsTrimfaceNURBS trim face dataValue SyntaxValue MeaningExample// flipNormal
        if true turns the surface inside out// boundaryCount: number of boundaries//
        boundaryType: // tedgeCountOnBoundary    : number of edges in a boundary//
        splineCountOnEdge    : number of splines in an edge in// edgeTolerance        :
        tolerance used to build the 3d edge// isEdgeReversed        : if true, the edge
        is backwards// geometricContinuity    : if true, the edge is tangent
        continuous// splineCountOnPedge    : number of splines in a 2d edge// isMonotone
        : if true, curvature is monotone// pedgeTolerance        : tolerance for the 2d
        edge//-type polyFacesPolygon face dataValue SyntaxfhmfmhmumcValue
        MeaningfhmfmhmumcExample// This data type (polyFace) is meant to be used in file
        I/O// after setAttrs have been written out for vertex position// arrays, edge
        connectivity arrays (with corresponding start// and end vertex descriptions),
        texture coordinate arrays and// color arrays.  The reason is that this data type
        references// all of its data through ids created by the former types.////
        fspecifies the ids of the edges making up a face -//     negative value if the
        edge is reversed in the face// hspecifies the ids of the edges making up a hole
        -//     negative value if the edge is reversed in the face// mfspecifies the ids
        of texture coordinates (uvs) for a face.//     This data type is obsolete as of
        version 3.0. It is replaced by mu.// mhspecifies the ids of texture coordinates
        (uvs) for a hole//     This data type is obsolete as of version 3.0. It is
        replaced by mu.// muThe  first argument refers to the uv set. This is a zero-
        based//     integer number. The second argument refers to the number of vertices
        (n)//     on the face which have valid uv values. The last n values are the uv//
        ids of the texture coordinates (uvs) for the face. These indices//     are what
        used to be represented by the mfand mhspecification.//     There may be more
        than one muspecification, one for each unique uv set.// mcspecifies the color
        index values for a face. The first argument//     is color index. The second
        argument is the number of color ids to follow.//     Rest of the arguments are
        color ids for the face.//setAttr node.polyFaceAttr -type polyFaces f3 1 2 3 mc0
        4 0 1 2 3;-type meshPolygonal meshValue SyntaxValue
        Meaningvvn[vtesmooth|hard]Example// vspecifies the vertices of the polygonal
        mesh// vnspecifies the normal of each vertex// vtis optional and specifies a U,V
        texture coordinate for each vertex// especifies the edge connectivity
        information between vertices//setAttr node.meshAttr -type mesh v3 0 0 0 0 1 0 0
        0 1vn3 1 0 0 1 0 0 1 0 0vt3 0 0 0 1 1 0e3 0 1 hard1 2 hard2 0 hard;-type
        latticeLattice dataValue SyntaxValue MeaningsDivisionCount tDivisionCount
        uDivisionCountExample// sDivisionCount is the horizontal lattice division
        count// tDivisionCount is the vertical lattice division count// uDivisionCount
        is the depth lattice division count// pointCount is the total number of lattice
        points// pointX,pointY,pointZ is one lattice point.  The list is//   specified
        varying first in S, then in T, last in U so the//   first two entries are
        (S=0,T=0,U=0) (s=1,T=0,U=0)//setAttr node.latticeAttr -type lattice 2 5 2 20-2
        -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -22 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2-2 -2
        2 2 -2 2 -2 -1 2 2 -1 2 -2 0 22 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;In query mode,
        return type is based on queried flag.
        
        Maya Bug Fix:
          - setAttr did not work with type matrix.
        
        Modifications:
          - No need to set type, this will automatically be determined
          - Adds support for passing a list or tuple as the second argument for datatypes such as double3.
          - When setting stringArray datatype, you no longer need to prefix the list with the number of elements - just pass a list or tuple as with other arrays
          - Added 'force' kwarg, which causes the attribute to be added if it does not exist.
                - if no type flag is passed, the attribute type is based on type of value being set (if you want a float, be sure to format it as a float, e.g.  3.0 not 3)
                - currently does not support compound attributes
                - currently supported python-to-maya mappings:
        
                    ============ ===========
                    python type  maya type
                    ============ ===========
                    float        double
                    ------------ -----------
                    int          long
                    ------------ -----------
                    str          string
                    ------------ -----------
                    bool         bool
                    ------------ -----------
                    Vector       double3
                    ------------ -----------
                    Matrix       matrix
                    ------------ -----------
                    [str]        stringArray
                    ============ ===========
        
        
            >>> addAttr( 'persp', longName= 'testDoubleArray', dataType='doubleArray')
            >>> setAttr( 'persp.testDoubleArray', [0,1,2])
            >>> setAttr( 'defaultRenderGlobals.preMel', 'sfff')
        
          - Added ability to set enum attributes using the string values; this may be
            done either by setting the 'asString' kwarg to True, or simply supplying
            a string value for an enum attribute.
        
        Flags:
        - alteredValue : av              (bool)          [create]
            The value is only the current value, which may change in the next evalution (if
            the attribute has an incoming connection). This flag is only used during file
            I/O, so that attributes with incoming connections do not have their data
            overwritten during the first evaluation after a file is opened.
        
        - caching : ca                   (bool)          [create]
            Sets the attribute's internal caching on or off. Not all attributes can be
            defined as caching. Only those attributes that are not defined by default to be
            cached can be made caching.  As well, multi attribute elements cannot be made
            caching. Caching also affects child attributes for compound attributes.
        
        - capacityHint : ch              (int)           [create]
            Used to provide a memory allocation hint to attributes where the -size flag
            cannot provide enough information. This flag is optional and is primarily
            intended to be used during file I/O. Only certain attributes make use of this
            flag, and the interpretation of the flag value varies per attribute. This flag
            is currently used by (node.attribute): mesh.face - hints the total number of
            elements in the face edge lists
        
        - channelBox : cb                (bool)          [create]
            Sets the attribute's display in the channelBox on or off. Keyable attributes are
            always display in the channelBox regardless of the channelBox settting.
        
        - clamp : c                      (bool)          [create]
            For numeric attributes, if the value is outside the range of the attribute,
            clamp it to the min or max instead of failing
        
        - keyable : k                    (bool)          [create]
            Sets the attribute's keyable state on or off.
        
        - lock : l                       (bool)          [create]
            Sets the attribute's lock state on or off.
        
        - size : s                       (int)           [create]
            Defines the size of a multi-attribute array. This is only a hint, used to help
            allocate memory as efficiently as possible.
        
        - type : typ                     (unicode)       [create]
            Identifies the type of data.  If the -type flag is not present, a numeric type
            is assumed.                  Flag can have multiple arguments, passed either as
            a tuple or a list.
        
        
        Derived from mel command `maya.cmds.setAttr`
        """
        pass

    def setAlias(self, alias):
        """
        Sets the alias for this attribute (similar to aliasAttr).
        """
        pass

    def setCaching(self, isCaching):
        """
        Sets whether this plug is cached internally. Note: turning caching on for a plug will force the plug to become networked. Network plugs take longer to look up in the DG; therefore you should only make a plug cached only if you are certain that the network plug look-up will take less than the saved evaluation cost.
        
        Parameters:
        isCaching : 'bool'
            True if this plug should be cached
        
        Derived from api method `maya.OpenMaya.MPlug.setCaching`
        """
        pass

    def setDirty(self, **kwargs): pass

    def setEnums(attr, enums):
        """
        Set the enumerators for an enum attribute.
        """
        pass

    def setKey(self, **kwargs):
        """
        This command creates keyframes for the specified objects, or the active objects
        if none are specified on the command line. The default time for the new
        keyframes is the current time. Override this behavior with the -tflag on the
        command line. The default value for the keyframe is the current value of the
        attribute for which a keyframe is set.  Override this behavior with the -vflag
        on the command line. When setting keyframes on animation curves that do not have
        timeas an input attribute (ie, they are unitless animation curves), use
        -f/-floatto specify the unitless value at which to set a keyframe. The -time and
        -float flags may be combined in one command. This command sets up Dependency
        Graph relationships for proper evaluation of a given attribute at a given time.
        
        Flags:
        - animLayer : al                 (unicode)       [create]
            Specifies that the new key should be placed in the specified animation layer.
            Note that if the objects being keyframed are not already part of the layer, this
            flag will be ignored.
        
        - animated : an                  (bool)          [create]
            Add the keyframe only to the attribute(s) that have already a keyframe on.
            Default: false
        
        - attribute : at                 (unicode)       [create]
            Attribute name to set keyframes on.
        
        - breakdown : bd                 (bool)          [create,query,edit]
            Sets the breakdown state for the key.  Default is false
        
        - clip : c                       (unicode)       [create]
            Specifies that the new key should be placed in the specified clip. Note that if
            the objects being keyframed are not already part of the clip, this flag will be
            ignored.
        
        - controlPoints : cp             (bool)          [create]
            Explicitly specify whether or not to include the control points of a shape (see
            -sflag) in the list of attributes. Default: false.
        
        - dirtyDG : dd                   (bool)          [create]
            Allow dirty messages to be sent out when a keyframe is set.
        
        - float : f                      (float)         [create]
            Float time at which to set a keyframe on float-based animation curves.
        
        - hierarchy : hi                 (unicode)       [create]
            Controls the objects this command acts on, relative to the specified (or active)
            target objects. Valid values are above,below,both,and none.Default is hierarchy
            -query
        
        - identity : id                  (bool)          [create]
            Sets an identity key on an animation layer.  An identity key is one that
            nullifies the effect of the anim layer.  This flag has effect only when the
            attribute being keyed is being driven by animation layers.
        
        - inTangentType : itt            (unicode)       [create]
            The in tangent type for keyframes set by this command. Valid values are: auto,
            clamped, fast, flat, linear, plateau, slow, spline, and stepnextDefault is
            keyTangent -q -g -inTangentType
        
        - insert : i                     (bool)          [create]
            Insert keys at the given time(s) and preserve the shape of the animation
            curve(s). Note: the tangent type on inserted keys will be fixed so that the
            curve shape can be preserved.
        
        - insertBlend : ib               (bool)          [create]
            If true, a pairBlend node will be inserted for channels that have nodes other
            than animCurves driving them, so that such channels can have blended animation.
            If false, these channels will not have keys inserted. If the flag is not
            specified, the blend will be inserted based on the global preference for
            blending animation.
        
        - minimizeRotation : mr          (bool)          [create]
            For rotations, ensures that the key that is set is a minimum distance away from
            the previous key.  Default is false
        
        - noResolve : nr                 (bool)          [create]
            When used with the -value flag, causes the specified value to be set directly
            onto the animation curve, without attempting to resolve the value across
            animation layers.
        
        - outTangentType : ott           (unicode)       [create]
            The out tangent type for keyframes set by this command. Valid values are: auto,
            clamped, fast, flat, linear, plateau, slow, spline, step, and stepnext. Default
            is keyTangent -q -g -outTangentType
        
        - respectKeyable : rk            (bool)          [create]
            When used with the -attribute flag, prevents the keying of the non keyable
            attributes.
        
        - shape : s                      (bool)          [create]
            Consider attributes of shapes below transforms as well, except controlPoints.
            Default: true
        
        - time : t                       (time)          [create]
            Time at which to set a keyframe on time-based animation curves.
        
        - useCurrentLockedWeights : lw   (bool)          [create]
            If we are setting a key over an existing key, use that key tangent's locked
            weight value for the new locked weight value.  Default is false
        
        - value : v                      (float)         [create]
            Value at which to set the keyframe. Using the value flag will not cause the
            keyed attribute to change to the specified value until the scene re-evaluates.
            Therefore, if you want the attribute to update to the new value immediately, use
            the setAttr command in addition to setting the key.                  Flag can
            have multiple arguments, passed either as a tuple or a list.
        
        
        Derived from mel command `maya.cmds.setKeyframe`
        """
        pass

    def setKeyable(self, keyable):
        """
        This overrides the default keyability of a plug set with MFnAttribute::setKeyable. Keyable plugs will be keyed by AutoKey and the Set Keyframe UI. Non-keyable plugs prevent the user from setting keys via the obvious UI provided for keying. Being non-keyable is not a hard block against adding keys to an attribute.
        
        Parameters:
        keyable : 'bool'
            True if this plug should be keyable
        
        Derived from api method `maya.OpenMaya.MPlug.setKeyable`
        """
        pass

    def setLocked(self, locked, checkReference='False'):
        """
        Sets the locked state for this plug's value. A plug's locked state
        determines whether or not the plug's value can be changed.
        
        Parameters
        ----------
        locked : `bool`
            True if this plug's value is to be locked
        checkReference : `bool`
            Set True to raise errors on referenced attributes.
        
            By default pymel and the maya api do not check if the node is referenced before
            setting the locked state. This is unsafe because changes to the locked state on
            referenced nodes are not saved with the scene.
        """
        pass

    def setMax(self, newMax): pass

    def setMin(self, newMin): pass

    def setNumElements(self, elements):
        """
        The method is used to pre-allocate the number of elements that an array plug will contain. The plug passed to this method must be an array plug and there must be no elements already allocated.
        
        Parameters:
        elements : 'int'
            new array size
        
        Derived from api method `maya.OpenMaya.MPlug.setNumElements`
        """
        pass

    def setRange(self, *args):
        """
        provide a min and max value as a two-element tuple or list, or as two arguments to the
        method. To remove a limit, provide a None value.  for example:
        
            >>> from pymel.core import *
            >>> s = polyCube()[0]
            >>> s.addAttr( 'new' )
            >>> s.new.setRange( -2, None ) #sets just the min to -2 and removes the max limit
            >>> s.new.setMax( 3 ) # sets just the max value and leaves the min at its previous default
            >>> s.new.getRange()
            [-2.0, 3.0]
        """
        pass

    def setSoftMax(self, newMax): pass

    def setSoftMin(self, newMin): pass

    def setSoftRange(self, *args): pass

    def shortName(self, fullPath='False'):
        """
            >>> from pymel.core import *
            >>> at = SCENE.persp.t.tx
            >>> at.shortName(fullPath=False)
            u'tx'
            >>> at.shortName(fullPath=True)
            u't.tx'
        
        Returns
        -------
        unicode
        """
        pass

    def showInChannelBox(self, inChannelBox):
        """
        Sets whether this plug is displayed in the channel box. This overrides the default display of a plug set with MFnAttribute::setChannelBox. Keyable attributes are always shown in the channel box so this flag is ignored on keyable plugs.
        
        Parameters:
        inChannelBox : 'bool'
            True if this plug should be displayed in the channel box
        
        Derived from api method `maya.OpenMaya.MPlug.setChannelBox`
        """
        pass

    def siblings(self):
        """
        attributeQuery -listSiblings
        
        Returns
        -------
        Optional[List[Attribute]]
        """
        pass

    def source(self):
        """
        If this plug is a destination, return the source plug connected to it. If this plug is not a destination, a null plug is returned.
        
        Returns:
        'PyNode'
        
        Derived from api method `maya.OpenMaya.MPlug.source`
        """
        pass

    def sourceWithConversion(self):
        """
        If this plug is a destination, return the source plug connected to it.
        
        Returns:
        'PyNode'
        
        Derived from api method `maya.OpenMaya.MPlug.sourceWithConversion`
        """
        pass

    def type(self):
        """
        getAttr -type
        
        Returns
        -------
        unicode
        """
        pass

    def unlock(self, checkReference='False'):
        """
        setAttr -locked 0
        """
        pass

    def unmute(self, **kwargs):
        """
        mute -disable -force
         Unmutes the attribute
        """
        pass

    FreeToChangeState = {}

    MValueSelector = {}

    __apicls__ = None

    __readonly__ = {}

    attrItemReg = None


class HashableSlice(ProxySlice):
    """
    # Really, don't need to have another class inheriting from
    # the proxy class, but do this so I can define a method using
    # normal class syntax...
    """

    def __cmp__(self, other): pass

    def __hash__(self): pass

    def __init__(self, *args, **kwargs): pass

    @property
    def start(self): pass

    @property
    def step(self): pass

    @property
    def stop(self): pass


class MayaNodeError(MayaObjectError):
    pass


class AttributeSpec(PyNode):
    """
    Represents a specification for the type of an attribute.
    
    This is different from an Attribute, which is a particular instance of
    an attribute, and is associated with a single node.  For instance, consider
    the "translateX" on "transform" nodes.  Every instance of a transform node
    will have it's own unique Attribute (ie, Attribute('top.translateX') and
    Attribute('top.translateX') are separate objects), but they all share the
    same AttributeSpec, since the properites of all the translateX's are all
    the same - ie, they are all floating point numerical attributes, are all
    storable, etc.
    
    For those familar with the API, an Attribute wraps an MPlug, while an
    AttributeSpec wraps MFnAttribute.
    """

    def __apimdagpath__(self):
        """
        Return the MDagPath for the node of this attribute, if it is valid
        """
        pass

    def __apimobject__(self):
        """
        Return the MObject for this attribute, if it is valid
        """
        pass

    def __apimplug__(self):
        """
        Return the MPlug for this attribute, if it is valid
        """
        pass

    def __apiobject__(self):
        """
        Return the default API object for this attribute, if it is valid
        """
        pass

    def accepts(self, type):
        """
        Returns true if this attribute can accept a connection of the given type.
        
        Parameters:
        type : 'Data.Type'
            data type
        
            values: 'numeric', 'plugin', 'pluginGeometry', 'string', 'matrix', 'stringArray', 'doubleArray', 'floatArray', 'intArray', 'pointArray', 'vectorArray', 'matrixArray', 'componentList', 'mesh', 'lattice', 'nurbsCurve', 'nurbsSurface', 'sphere', 'dynArrayAttrs', 'dynSweptGeometry', 'subdSurface', 'NObject', 'NId', 'any'
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnData.accepts`
        """
        pass

    def addToCategory(self, category):
        """
        Add the attribute to the named category.
        
        Parameters:
        category : 'unicode'
            New category to which the attribute is to be added
        
        Derived from api method `maya.OpenMaya.MFnAttribute.addToCategory`
        """
        pass

    def getAddAttrCmd(self, useLongName='False'):
        """
        Returns a string containing the addAttr command which would be required to recreate the attribute on a node. The command includes the terminating semicolon and is formatted as if for use with a selected node, meaning that it contains no node name.
        
        Parameters:
        useLongName : 'bool'
            if true, use the attribute's long name rather than its short name
        
        
        Returns:
        'unicode'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.getAddAttrCmd`
        """
        pass

    def getAffectsAppearance(self):
        """
        Returns true if this attribute affects the appearance of the object when rendering in the viewport.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.affectsAppearance`
        """
        pass

    def getCategories(self):
        """
        Get all of the categories to which this attribute belongs.
        
        Returns:
        List['list']
        
        Derived from api method `maya.OpenMaya.MFnAttribute.getCategories`
        """
        pass

    def getDisconnectBehavior(self):
        """
        Returns the behavior of this attribute when it is disconnected. The possible settings are as follows:
        
        Returns:
        'AttributeSpec.DisconnectBehavior'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.disconnectBehavior`
        """
        pass

    def getIndexMatters(self):
        """
        Determines whether the user must specify an index when connecting to this attribute, or whether the next available index can be used. This method only applies to array attributes which are non readable, i.e. destination attributes.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.indexMatters`
        """
        pass

    def getInternal(self):
        """
        Returns true if a node has internal member data representing this attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.internal`
        """
        pass

    def getUsesArrayDataBuilder(self):
        """
        Returns true if this attribute uses an array data builder. If so, then the MArrayDataBuilder class may be used with this attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.usesArrayDataBuilder`
        """
        pass

    def hasCategory(self, category):
        """
        Check to see if the attribute belongs to the named category.
        
        Parameters:
        category : 'unicode'
            Category to check for attribute membership
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.hasCategory`
        """
        pass

    def isAffectsWorldSpace(self):
        """
        Returns true if this attribute affects worldspace.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isAffectsWorldSpace`
        """
        pass

    def isArray(self):
        """
        Returns true if this attribute supports an array of data.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isArray`
        """
        pass

    def isCached(self):
        """
        Returns true if this attribute is cached locally in the node's data block. The default for this is true. Caching a node locally causes a copy of the attribute value for the node to be cached with the node. This removes the need to traverse through the graph to get the value each time it is requested.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isCached`
        """
        pass

    def isChannelBoxFlagSet(self):
        """
        Returns true if this attribute has its channel box flag set. Attributes will appear in the channel box if their channel box flag is set or if they are keyable.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isChannelBoxFlagSet`
        """
        pass

    def isConnectable(self):
        """
        Returns true if this attribute accepts dependency graph connections. If it does, then the readable and writable methods will indicate what types of connections are accepted.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isConnectable`
        """
        pass

    def isDynamic(self):
        """
        Returns true if this attribute is a dynamic attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isDynamic`
        """
        pass

    def isExtension(self):
        """
        Returns true if this attribute is an extension attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isExtension`
        """
        pass

    def isHidden(self):
        """
        Returns true if this attribute is to hidden from the UI. The attribute will not show up in attribute editors.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isHidden`
        """
        pass

    def isIndeterminant(self):
        """
        Returns true if this attribute is indeterminant. If an attribute may or may not be used during an evaluation then it is indeterminant. This attribute classification is mainly used on rendering nodes to indicate that some attributes are not always used.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isIndeterminant`
        """
        pass

    def isKeyable(self):
        """
        Returns true if this attribute is keyable. Keyable attributes will be keyed by AutoKey and the Set Keyframe UI. Non-keyable attributes prevent the user from setting keys via the obvious UI provided for keying. Being non-keyable is not a hard block against adding keys to an attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isKeyable`
        """
        pass

    def isProxyAttribute(self):
        """
        Returns true if this attribute is a proxy attribute.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isProxyAttribute`
        """
        pass

    def isReadable(self):
        """
        Returns true if this attribute is readable. If an attribute is readable, then it can be used as the source in a dependency graph connection.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isReadable`
        """
        pass

    def isRenderSource(self):
        """
        Returns true if this attribute is a render source. This attribute is used on rendering nodes to override the rendering sampler info.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isRenderSource`
        """
        pass

    def isStorable(self):
        """
        Returns true if this attribute is to be stored when the node is saved to a file.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isStorable`
        """
        pass

    def isUsedAsColor(self):
        """
        Returns true if this attribute is to be presented as a color in the UI.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isUsedAsColor`
        """
        pass

    def isUsedAsFilename(self):
        """
        Returns true if this attribute is to be used as a filename. In the UI this attr will be presented as a file name.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isUsedAsFilename`
        """
        pass

    def isWorldSpace(self):
        """
        Returns true if this attribute is worldspace.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isWorldSpace`
        """
        pass

    def isWritable(self):
        """
        Returns true if this attribute is writable. If an attribute is writable, then it can be used as the destination in a dependency graph connection.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.isWritable`
        """
        pass

    def name(self): pass

    def parent(self):
        """
        Modifications:
          - returns None instead of erroring if no parent
                
        Get the parent of this attribute, if it has one.
        
        Returns:
        'PyNode'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.parent`
        """
        pass

    def removeFromCategory(self, category):
        """
        Remove the attribute from the named category.
        
        Parameters:
        category : 'unicode'
            Category from which the attribute is to be removed
        
        Derived from api method `maya.OpenMaya.MFnAttribute.removeFromCategory`
        """
        pass

    def setAffectsAppearance(self, state):
        """
        Sets whether this attribute affects the appearance of the object when rendering in the viewport.
        
        Parameters:
        state : 'bool'
            whether the attribute affects the appearance of the object when rendering in the viewport.
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setAffectsAppearance`
        """
        pass

    def setAffectsWorldSpace(self, state):
        """
        Sets whether this attribute should affect worldspace. NOTES: This property is ignored on non-dag nodes.
        
        Parameters:
        state : 'bool'
            whether the attribute should affect worldspace
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setAffectsWorldSpace`
        """
        pass

    def setArray(self, state):
        """
        Sets whether this attribute should have an array of data. This should be set to true if the attribute needs to accept multiple incoming connections.
        
        Parameters:
        state : 'bool'
            whether the attribute is to have an array of data
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setArray`
        """
        pass

    def setCached(self, state):
        """
        Sets whether the data for this attribute is cached locally in the node's data block. The default for this is true. Caching a node locally causes a copy of the attribute value for the node to be cached with the node. This removes the need to traverse through the graph to get the value each time it is requested. This should only get called in the initialize call of your node creator.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be cached locally
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setCached`
        """
        pass

    def setChannelBox(self, state):
        """
        Sets whether this attribute should appear in the channel box when the node is selected. This should only get called in the initialize call of your node creator. Keyable attributes are always shown in the channel box so this flag is ignored on keyable attributes. It is for intended for use on non-keyable attributes which you want to appear in the channel box.
        
        Parameters:
        state : 'bool'
            whether the attribute is to appear in the channel box
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setChannelBox`
        """
        pass

    def setConnectable(self, state):
        """
        Sets whether this attribute should allow dependency graph connections. This should only get called in the initialize call of your node creator.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be connectable
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setConnectable`
        """
        pass

    def setDisconnectBehavior(self, behavior):
        """
        Sets the disconnection behavior for this attribute. This determines what happens when a connection to this attribute is deleted. This should only get called in the initialize call of your node creator.
        
        Parameters:
        behavior : 'AttributeSpec.DisconnectBehavior'
            the new disconnect behavior
        
            values: 'delete', 'reset', 'nothing'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setDisconnectBehavior`
        """
        pass

    def setHidden(self, state):
        """
        Sets whether this attribute should be hidden from the UI. This is useful if the attribute is being used for blind data, or if it is being used as scratch space for a geometry calculation (should also be marked non-connectable in that case).
        
        Parameters:
        state : 'bool'
            whether the attribute is to be hidden
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setHidden`
        """
        pass

    def setIndeterminant(self, state):
        """
        Sets whether this attribute is indeterminant. If an attribute may or may not be used during an evaluation then it is indeterminant. This attribute classification is mainly used on rendering nodes to indicate that some attributes are not always used.
        
        Parameters:
        state : 'bool'
            whether the attribute indeterminant
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setIndeterminant`
        """
        pass

    def setIndexMatters(self, state):
        """
        If the attribute is an array, then this method specifies whether to force the user to specify an index when connecting to this attribute, or to use the next available index.
        
        Parameters:
        state : 'bool'
            whether the attribute's index must be specified when connecting to this attribute using the connectAttr command
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setIndexMatters`
        """
        pass

    def setInternal(self, state):
        """
        The function controls an attribute's data storage. When set to true, the virtual methods MPxNode::setInternalValue() and MPxNode::getInternalValue() are invoked whenever the attribute value is set or queried, respectively. By default, attributes are not internal.
        
        Parameters:
        state : 'bool'
            whether the attribute uses internal data
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setInternal`
        """
        pass

    def setKeyable(self, state):
        """
        Sets whether this attribute should accept keyframe data. This should only get called in the initialize call of your node creator. Keyable attributes will be keyed by AutoKey and the Set Keyframe UI. Non-keyable attributes prevent the user from setting keys via the obvious UI provided for keying. Being non-keyable is not a hard block against adding keys to an attribute.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be keyable
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setKeyable`
        """
        pass

    def setNiceNameOverride(self, localizedName):
        """
        Sets the localized string which should be used for this attribute in the UI.
        
        Parameters:
        localizedName : 'unicode'
            The name to use for the current locale.
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setNiceNameOverride`
        """
        pass

    def setProxyAttribute(self, state):
        """
        Sets whether this attribute is a proxy attribute.
        
        Parameters:
        state : 'bool'
            whether the attribute is a proxy attribute.
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setProxyAttribute`
        """
        pass

    def setReadable(self, state):
        """
        Sets whether this attribute should be readable. If an attribute is readable, then it can be used as the source in a dependency graph connection.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be readable
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setReadable`
        """
        pass

    def setRenderSource(self, state):
        """
        Sets whether this attribute should be used as a render source attribute. When writing shader plug-ins, it is sometimes useful to be able to modify the sampler info, so upstream shading network can be re- evaluated with different sampler info values.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be a render source
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setRenderSource`
        """
        pass

    def setStorable(self, state):
        """
        Sets whether this attribute should be storable. If an attribute is storable, then it will be writen out when the node is stored to a file. This should only get called in the initialize call of your node creator.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be storable
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setStorable`
        """
        pass

    def setUsedAsColor(self, state):
        """
        Sets whether this attribute should be presented as a color in the UI.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be presented as a color
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setUsedAsColor`
        """
        pass

    def setUsedAsFilename(self, state):
        """
        Sets whether this attribute should be presented as a filename in the UI.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be presented as a filename
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setUsedAsFilename`
        """
        pass

    def setUsesArrayDataBuilder(self, state):
        """
        Sets whether this attribute uses an array data builder. If true, then the MArrayDataBuilder class may be used with this attribute to generate its data. If false, MArrayDataHandle::builder will fail.
        
        Parameters:
        state : 'bool'
            whether the attribute uses an array data builder
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setUsesArrayDataBuilder`
        """
        pass

    def setWorldSpace(self, state):
        """
        Sets whether this attribute should be treated as worldspace. Being worldspace indicates the attribute is dependent on the worldSpace transformation of this node, and will be marked dirty by any attribute changes in the hierarchy that affects the worldSpace transformation. The attribute needs to be an array since during instancing there are multiple worldSpace paths to the node & Maya requires one array element per path for worldSpace attributes.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be presented as worldspace
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setWorldSpace`
        """
        pass

    def setWritable(self, state):
        """
        Sets whether this attribute should be writable. If an attribute is writable, then it can be used as the destination in a dependency graph connection. If an attribute is not writable then setAttr commands will fail to change the attribute.
        
        Parameters:
        state : 'bool'
            whether the attribute is to be writable
        
        Derived from api method `maya.OpenMaya.MFnAttribute.setWritable`
        """
        pass

    def shortName(self):
        """
        Returns the short name of the attribute. If the attribute has no short name then its long name is returned.
        
        Returns:
        'unicode'
        
        Derived from api method `maya.OpenMaya.MFnAttribute.shortName`
        """
        pass

    @staticmethod
    def __new__(cls, *args, **kwargs): pass

    DisconnectBehavior = {}

    __apicls__ = None

    __readonly__ = {}


AttributeDefaults = AttributeSpec


class Pivot(Component):
    __readonly__ = {}


class MayaComponentError(MayaAttributeError):
    pass


class DeletedMayaNodeError(MayaNodeError):
    def __init__(self, node='None'): pass

    def __str__(self): pass

    @classmethod
    def handle(cls, pynode): pass


class MItComponent(Component):
    """
    Abstract base class for pymel components that can be accessed via iterators.
    
    (ie, `MeshEdge`, `MeshVertex`, and `MeshFace` can be wrapped around
    MItMeshEdge, etc)
    
    If deriving from this class, you should set __apicls__ to an appropriate
    MIt* type - ie, for MeshEdge, you would set __apicls__ = _api.MItMeshEdge
    """

    def __apimfn__(self): pass

    def __apimit__(self, alwaysUnindexed='False'): pass

    def __init__(self, *args, **kwargs): pass

    __readonly__ = {}


class DimensionedComponent(Component):
    """
    Components for which having a __getitem__ of some sort makes sense
    
    ie, myComponent[X] would be reasonable.
    """

    def __getitem__(self, item):
        """
        # subclasses should not override this - override _getitem_overrideable
        # instead
        """
        pass

    def __init__(self, *args, **kwargs): pass

    def currentDimension(self):
        """
        Returns the dimension index that an index operation - ie, self[...] /
        self.__getitem__(...) - will operate on.
        
        If the component is completely specified (ie, all dimensions are
        already indexed), then None is returned.
        """
        pass

    VALID_SINGLE_INDEX_TYPES = []

    __readonly__ = {}

    dimensions = 0


class MayaInstanceError(MayaNodeError):
    def __str__(self): pass


class MayaAttributeEnumError(MayaAttributeError):
    def __init__(self, node='None', enum='None'): pass

    def __str__(self): pass


class ContinuousComponent(DimensionedComponent):
    """
    Components whose dimensions are continuous.
    
    Ie, there are an infinite number of possible components, referenced by
    floating point parameters.
    
    Example: nurbsCurve.u[7.48], nurbsSurface.uv[3.85][2.1]
    
    Derived classes should implement:
    _dimRange
    """

    def __iter__(self): pass

    VALID_SINGLE_INDEX_TYPES = ()

    __readonly__ = {}


class MayaParticleAttributeError(MayaComponentError):
    pass


class DiscreteComponent(DimensionedComponent):
    """
    Components whose dimensions are discretely indexed.
    
    Ie, there are a finite number of possible components, referenced by integer
    indices.
    
    Example: polyCube.vtx[38], f.cv[3][2]
    
    Derived classes should implement:
    _dimLength
    """

    def __init__(self, *args, **kwargs): pass

    def __iter__(self): pass

    def __len__(self): pass

    def count(self): pass

    def currentItem(self): pass

    def currentItemIndex(self):
        """
        Returns the component indices for the current item in this component
        group
        
        If the component type has more then one dimension, the return result
        will be a ComponentIndex object which is a sub-class of tuple; otherwise,
        it will be a single int.
        
        These values correspond to the indices that you would use when selecting
        components in mel - ie, vtx[5], cv[3][2]
        """
        pass

    def getIndex(self):
        """
        Returns the current 'flat list' index for this group of components -
        ie, if this component holds the vertices:
            [5, 7, 12, 13, 14, 25]
        then if the 'flat list' index is 2, then we are pointing to vertex 12.
        """
        pass

    def indices(self):
        """
        A list of all the indices contained by this component.
        """
        pass

    def indicesIter(self):
        """
        An iterator over all the indices contained by this component,
        as ComponentIndex objects (which are a subclass of tuple).
        """
        pass

    def next(self): pass

    def reset(self): pass

    def setIndex(self, index): pass

    def totalSize(self):
        """
        The maximum possible number of components
        
        ie, for a polygon cube, the totalSize for verts would be 8, for edges
        would be 12, and for faces would be 6
        """
        pass

    VALID_SINGLE_INDEX_TYPES = ()

    __readonly__ = {}


class Component1D64(DiscreteComponent):
    def __len__(self): pass

    def totalSize(self): pass

    __readonly__ = {}

    dimensions = 2


class Component2D(DiscreteComponent):
    __readonly__ = {}

    dimensions = 2


class Component1D(DiscreteComponent):
    def __add__(self, other):
        """
        # TODO: also add __add__ / __iadd__ for 2D / 3D components
        """
        pass

    def __iadd__(self, other): pass

    def currentItem(self): pass

    def currentItemIndex(self):
        """
        Returns the component indices for the current item in this component
        group
        
        If the component type has more then one dimension, the return result
        will be a ComponentIndex object which is a sub-class of tuple; otherwise,
        it will be a single int.
        
        These values correspond to the indices that you would use when selecting
        components in mel - ie, vtx[5], cv[3][2]
        """
        pass

    def index(self): pass

    def indicesIter(self):
        """
        An iterator over all the indices contained by this component,
        as integers.
        """
        pass

    def name(self): pass

    __readonly__ = {}

    dimensions = 1


class Component1DFloat(ContinuousComponent):
    def index(self): pass

    __readonly__ = {}

    dimensions = 1


class Component3D(DiscreteComponent):
    __readonly__ = {}

    dimensions = 3


class Component2DFloat(ContinuousComponent):
    __readonly__ = {}

    dimensions = 2


class ParticleComponent(Component1D):
    def __getattr__(self, attr): pass

    def attr(self, attr): pass

    __readonly__ = {}


class NurbsSurfaceEP(Component2D):
    __readonly__ = {}


class NurbsSurfaceFace(Component2D):
    __readonly__ = {}


class NurbsSurfaceCV(Component2D):
    __readonly__ = {}


class SubdFace(Component1D64):
    __readonly__ = {}


class SubdVertex(Component1D64):
    __readonly__ = {}


class MItComponent1D(MItComponent, Component1D):
    __readonly__ = {}


class MeshUV(Component1D):
    __readonly__ = {}


class NurbsSurfaceIsoparm(Component2DFloat):
    def __init__(self, *args, **kwargs): pass

    __readonly__ = {}


class NurbsCurveParameter(Component1DFloat):
    __readonly__ = {}


class LatticePoint(Component3D):
    __readonly__ = {}


class NurbsSurfaceKnot(Component2D):
    __readonly__ = {}


class SubdUV(Component1D):
    def totalSize(self): pass

    __readonly__ = {}


class SubdEdge(Component1D64):
    __readonly__ = {}


class NurbsCurveKnot(Component1D):
    __readonly__ = {}


class MeshVertexFace(Component2D):
    def __melobject__(self):
        """
        # getting all the mel strings for MeshVertexFace is SLLOOOWW - so check if
        # it's complete, and if so, just return the .vtxFace[*] form
        """
        pass

    def totalSize(self): pass

    __readonly__ = {}


class NurbsCurveEP(Component1D):
    __readonly__ = {}


class NurbsCurveCV(MItComponent1D):
    def getPosition(self, space="'preTransform'"):
        """
        Return the position of the current CV.
        
        Parameters:
        space : 'Space.Space'
            the co-oordinate system for the returned point
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'Point'
        
        Derived from api method `maya.OpenMaya.MSpace.position`
        """
        pass

    def hasHistoryOnCreate(self):
        """
        This method determines if the shape was created with history.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItCurveCV.hasHistoryOnCreate`
        """
        pass

    def isDone(self):
        """
        Returns true if the iteration is finished, i.e. there are no more CVs to iterate on.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItCurveCV.isDone`
        """
        pass

    def setPosition(self, pt, space="'preTransform'"):
        """
        Set the position of the current CV to the specified point.
        
        Parameters:
        pt : 'Point'
            new position of CV
        space : 'Space.Space'
            the co-ordinate system for this transformation.
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.setPosition`
        """
        pass

    def translateBy(self, vec, space="'preTransform'"):
        """
        Translates the current CV by the amount specified in vec.
        
        Parameters:
        vec : 'Vector'
            translation to be applied to the CV
        space : 'Space.Space'
            the co-oordinate system for this transformation.
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.translateBy`
        """
        pass

    def updateCurve(self):
        """
        This method is used to signal the curve that it has been changed and needs to redraw itself.
        Derived from api method `maya.OpenMaya.MItCurveCV.updateCurve`
        """
        pass

    __apicls__ = None

    __readonly__ = {}


class MeshEdge(MItComponent1D):
    def connectedEdges(self):
        """
        Returns
        -------
        List[MeshEdge]
        """
        pass

    def connectedFaces(self):
        """
        Returns
        -------
        List[MeshFace]
        """
        pass

    def connectedVertices(self):
        """
        Returns
        -------
        Tuple[MeshVertex, MeshVertex]
        """
        pass

    def getLength(self, space="'preTransform'"):
        """
        This method returns the length of the current edge.
        
        Parameters:
        space : 'Space.Space'
            Coordinate space in which to perform the operation.
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'float'
        
        Derived from api method `maya.OpenMaya.MSpace.getLength`
        """
        pass

    def getPoint(self, index, space="'preTransform'"):
        """
        Return the position of the specified vertex of the current edge.
        
        Parameters:
        index : 'int'
            The vertex of the edge we wish to examine (0 or 1)
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'Point'
        
        Derived from api method `maya.OpenMaya.MSpace.point`
        """
        pass

    def isConnectedTo(self, component):
        """
        Parameters
        ----------
        component : Union[MeshFace, MeshEdge, MeshVertex]
        
        Returns
        -------
        bool
        """
        pass

    def isConnectedToEdge(self, index):
        """
        This method determines whether the given edge is connected to the current edge
        
        Parameters:
        index : 'int'
            Index of edge to check.
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.connectedToEdge`
        """
        pass

    def isConnectedToFace(self, index):
        """
        This method determines whether the given face contains the current edge
        
        Parameters:
        index : 'int'
            Index of face to check.
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.connectedToFace`
        """
        pass

    def isOnBoundary(self):
        """
        This method checks to see if the current edge is a border edge.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.onBoundary`
        """
        pass

    def isSmooth(self):
        """
        This method determines if the current edge in the iteration is smooth (soft).
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.isSmooth`
        """
        pass

    def numConnectedEdges(self):
        """
        This method returns the number of edges connected to the current edge.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.numConnectedEdges`
        """
        pass

    def numConnectedFaces(self):
        """
        This method returns the number of faces (1 or 2 ) connected to the current edge.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.numConnectedFaces`
        """
        pass

    def setPoint(self, point, index, space="'preTransform'"):
        """
        Set the specified vertex of the current edge to the given value.
        
        Parameters:
        point : 'Point'
            The new value for the edge
        index : 'int'
            The vertex index of the current edge we wish to set (0 or 1)
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.setPoint`
        """
        pass

    def setSmoothing(self, smooth='True'):
        """
        This method sets the current edge to be hard or smooth (soft). The cleanupSmoothing method is no longer required to be called after setSmoothing in Maya3.0 and later versions.
        
        Parameters:
        smooth : 'bool'
            if true the edge will be smooth (soft), otherwise the edge will be hard.
        
        Derived from api method `maya.OpenMaya.MItMeshEdge.setSmoothing`
        """
        pass

    def updateSurface(self):
        """
        Signal that this polygonal surface has changed and needs to redraw itself.
        Derived from api method `maya.OpenMaya.MItMeshEdge.updateSurface`
        """
        pass

    __apicls__ = None

    __readonly__ = {}


class NurbsSurfaceRange(NurbsSurfaceIsoparm):
    __readonly__ = {}


class MeshVertex(MItComponent1D):
    def connectedEdges(self):
        """
        Returns
        -------
        List[MeshEdge]
        """
        pass

    def connectedFaces(self):
        """
        Returns
        -------
        List[MeshFace]
        """
        pass

    def connectedVertices(self):
        """
        Returns
        -------
        List[MeshVertex]
        """
        pass

    def geomChanged(self):
        """
        Reset the geom pointer in the MItMeshVertex. If you're using MFnMesh to update Normals or Color per vertex while iterating, you must call geomChanged on the iteratior immediately after the MFnMesh call to make sure that your geometry is up to date. A crash may result if this method is not called. A similar approach must be taken for updating upstream vertex tweaks with an MPlug. After the update, call this method.
        Derived from api method `maya.OpenMaya.MItMeshVertex.geomChanged`
        """
        pass

    def getColor(self, *args, **kwargs): pass

    def getColorIndices(self, colorSetName='None'):
        """
        This method returns the colorIndices into the color array see MFnMesh::getColors() of the current vertex.
        
        Parameters:
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        List['int']
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.getColorIndices`
        """
        pass

    def getColors(self, colorSetName='None'):
        """
        This method gets the colors of the current vertex for each face it belongs to. If no colors are assigned to the vertex at all, the return values will be (-1 -1 -1 1). If some but not all of the vertex/face colors have been explicitly set, the ones that have not been set will be (0, 0, 0, 1).
        
        Parameters:
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        List['Color']
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.getColors`
        """
        pass

    def getNormal(self, space="'preTransform'"):
        """
        Return the normal or averaged normal if unshared of the current vertex.
        
        Parameters:
        space : 'Space.Space'
            The transformation space.
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'Vector'
        
        Derived from api method `maya.OpenMaya.MSpace.getNormal`
        """
        pass

    def getNormalIndices(self):
        """
        This method returns the normal indices of the face/vertex associated with the current vertex.
        
        Returns:
        List['int']
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.getNormalIndices`
        """
        pass

    def getNormals(self, space="'preTransform'"):
        """
        Return the normals of the current vertex for all faces
        
        Parameters:
        space : 'Space.Space'
            The transformation space.
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        List['Vector']
        
        Derived from api method `maya.OpenMaya.MSpace.getNormals`
        """
        pass

    def getPosition(self, space="'preTransform'"):
        """
        Return the position of the current vertex in the specified space. Object space ignores all transformations for the polygon, world space includes all such transformations.
        
        Parameters:
        space : 'Space.Space'
            The transformation space
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'Point'
        
        Derived from api method `maya.OpenMaya.MSpace.position`
        """
        pass

    def getUV(self, uvSet='None'):
        """
        Get the shared UV value at this vertex
        
        Parameters:
        uvSet : 'unicode'
            Name of the uv set to work with.
        
        
        Returns:
        ('float', 'float')
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.getUV`
        """
        pass

    def getUVIndices(self, uvSet='None'):
        """
        This method returns the uv indices into the normal array see MFnMesh::getUVs() of the current vertex.
        
        Parameters:
        uvSet : 'unicode'
            Name of the uv set.
        
        
        Returns:
        List['int']
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.getUVIndices`
        """
        pass

    def getUVs(self, uvSet='None'):
        """
        Get the UV values for all mapped faces at the current vertex. If at least one face was mapped the method will succeed.
        
        Parameters:
        uvSet : 'unicode'
            Name of the uv set to work with
        
        
        Returns:
        Tuple[List['float'], List['float'], List['int']]
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.getUVs`
        """
        pass

    def hasColor(self):
        """
        This method determines whether the current Vertex has a color set for one or more faces.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.hasColor`
        """
        pass

    def isConnectedTo(self, component):
        """
        pass a component of type `MeshVertex`, `MeshEdge`, `MeshFace`, with a single element
        
        Returns
        -------
        bool
        """
        pass

    def isConnectedToEdge(self, index):
        """
        This method determines whether the given edge contains the current vertex
        
        Parameters:
        index : 'int'
            Index of edge to check.
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.connectedToEdge`
        """
        pass

    def isConnectedToFace(self, index):
        """
        This method determines whether the given face contains the current vertex
        
        Parameters:
        index : 'int'
            Index of face to check.
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.connectedToFace`
        """
        pass

    def isOnBoundary(self):
        """
        This method determines whether the current vertex is on a Boundary
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.onBoundary`
        """
        pass

    def numConnectedEdges(self):
        """
        This Method checks for the number of connected Edges on this vertex
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.numConnectedEdges`
        """
        pass

    def numConnectedFaces(self):
        """
        This Method checks for the number of Connected Faces
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.numConnectedFaces`
        """
        pass

    def numUVs(self, uvSet='None'):
        """
        This method returns the number of unique UVs mapped on this vertex
        
        Parameters:
        uvSet : 'unicode'
            Name of the uv set to work with
        
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.numUVs`
        """
        pass

    def setColor(self, color): pass

    def setPosition(self, point, space="'preTransform'"):
        """
        Set the position of the current vertex in the given space.
        
        Parameters:
        point : 'Point'
            The new position for the current vertex
        space : 'Space.Space'
            Transformation space
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.setPosition`
        """
        pass

    def setUV(self, uvPoint, uvSet='None'):
        """
        Set the shared UV value at this vertex
        
        Parameters:
        uvPoint : ('float', 'float')
            The UV value to set.
        uvSet : 'unicode'
            Name of the UV set to work with
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.setUV`
        """
        pass

    def setUVs(self, uArray, vArray, faceIds, uvSet='None'):
        """
        Set the UV value for the specified faces at the current vertex. If the face is not already mapped, the value will not be set. If at least ne face was previously mapped, the method should succeed. If no faces were mapped, the method will fail.
        
        Parameters:
        uArray : List['float']
            All the U values - in local face order
        vArray : List['float']
            The corresponding V values
        faceIds : List['int']
            The corresponding face Ids
        uvSet : 'unicode'
            Name of the uv set to work with
        
        Derived from api method `maya.OpenMaya.MItMeshVertex.setUVs`
        """
        pass

    def translateBy(self, vector, space="'preTransform'"):
        """
        Translate the current vertex by the amount specified by the given vector.
        
        Parameters:
        vector : 'Vector'
            The amount of translation
        space : 'Space.Space'
            The transformation space
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.translateBy`
        """
        pass

    def updateSurface(self):
        """
        Signal that this polygonal surface has changed and needs to redraw itself.
        Derived from api method `maya.OpenMaya.MItMeshVertex.updateSurface`
        """
        pass

    __apicls__ = None

    __readonly__ = {}


class MeshFace(MItComponent1D):
    def connectedEdges(self):
        """
        Returns
        -------
        List[MeshEdge]
        """
        pass

    def connectedFaces(self):
        """
        Returns
        -------
        List[MeshFace]
        """
        pass

    def connectedVertices(self):
        """
        Returns
        -------
        List[MeshVertex]
        """
        pass

    def geomChanged(self):
        """
        Reset the geom pointer in the MItMeshPolygon. This is now being handled automatically inside the iterator, and users should no longer need to call this method directly to sync up the iterator to changes made by MFnMesh
        Derived from api method `maya.OpenMaya.MItMeshPolygon.geomChanged`
        """
        pass

    def getArea(self, space="'preTransform'"):
        """
        This method gets the area of the face
        
        Parameters:
        space : 'Space.Space'
            World Space or Object Space
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'float'
        
        Derived from api method `maya.OpenMaya.MSpace.getArea`
        """
        pass

    def getAxisAtUV(self, uvPoint, space="'preTransform'", uvSet='None', tolerance='0.0'):
        """
        Return the axis of the point at the given UV value in the current polygon.
        
        Parameters:
        uvPoint : ('float', 'float')
            The UV value to try to locate
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        uvSet : 'unicode'
            UV set to work with
        tolerance : 'float'
            tolerance value to compare float data type
        
        
        Returns:
        Tuple['Vector', 'Vector', 'Vector']
        
        Derived from api method `maya.OpenMaya.MSpace.getAxisAtUV`
        """
        pass

    def getColor(self, colorSetName='None'):
        """
        This method gets the average color of the all the vertices in this face
        
        Parameters:
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        'Color'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getColor`
        """
        pass

    def getColorIndex(self, vertexIndex, colorSetName='None'):
        """
        This method returns the colorIndex for a vertex of the current face.
        
        Parameters:
        vertexIndex : 'int'
            Face-relative index of vertex.
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getColorIndex`
        """
        pass

    def getColorIndices(self, colorSetName='None'):
        """
        This method returns the colorIndices for each vertex on the face.
        
        Parameters:
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        List['int']
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getColorIndices`
        """
        pass

    def getColors(self, colorSetName='None'):
        """
        This method gets the color of the each vertex in the current face.
        
        Parameters:
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        List['Color']
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getColors`
        """
        pass

    def getEdges(self):
        """
        This method gets the indices of the edges contained in the current face.
        
        Returns:
        List['int']
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getEdges`
        """
        pass

    def getNormal(self, space="'preTransform'"):
        """
        Return the face normal of the current polygon.
        
        Parameters:
        space : 'Space.Space'
            The transformation space
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'Vector'
        
        Derived from api method `maya.OpenMaya.MSpace.getNormal`
        """
        pass

    def getNormals(self, space="'preTransform'"):
        """
        Returns the normals for all vertices in the current face
        
        Parameters:
        space : 'Space.Space'
            The transformation space
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        List['Vector']
        
        Derived from api method `maya.OpenMaya.MSpace.getNormals`
        """
        pass

    def getPoint(self, index, space="'preTransform'"):
        """
        Return the position of the vertex at index in the current polygon.
        
        Parameters:
        index : 'int'
            The face-relative index of the vertex in the current polygon
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        'Point'
        
        Derived from api method `maya.OpenMaya.MSpace.point`
        """
        pass

    def getPointAtUV(self, uvPoint, space="'preTransform'", uvSet='None', tolerance='0.0'):
        """
        Return the position of the point at the given UV value in the current polygon.
        
        Parameters:
        uvPoint : ('float', 'float')
            The UV value to try to locate
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        uvSet : 'unicode'
            UV set to work with
        tolerance : 'float'
            tolerance value to compare float data type
        
        
        Returns:
        'Point'
        
        Derived from api method `maya.OpenMaya.MSpace.getPointAtUV`
        """
        pass

    def getPoints(self, space="'preTransform'"):
        """
        Retrieves the positions of the vertices on the current face/polygon that the iterator is pointing to. Vertex positions will be inserted into the given array and will be indexed using face-relative vertex IDs (ie. ordered from 0 to (vertexCount of the face) - 1), which should not be confused with the vertexIDs of each vertex in relation to the entire mesh object.
        
        Parameters:
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        
        Returns:
        List['Point']
        
        Derived from api method `maya.OpenMaya.MSpace.getPoints`
        """
        pass

    def getUV(self, vertex, uvSet='None'):
        """
        Return the texture coordinate for the given vertex.
        
        Parameters:
        vertex : 'int'
            The face-relative vertex index to get UV for
        uvSet : 'unicode'
            UV set to work with
        
        
        Returns:
        ('float', 'float')
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getUV`
        """
        pass

    def getUVArea(self, uvSet='None'):
        """
        This method gets the UV area of the face
        
        Parameters:
        uvSet : 'unicode'
            UV set to work with
        
        
        Returns:
        'float'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getUVArea`
        """
        pass

    def getUVAtPoint(self, pt, space="'preTransform'", uvSet='None'):
        """
        Find the point closest to the given point in the current polygon, and return the UV value at that point.
        
        Parameters:
        pt : 'Point'
            The point to try to get UV for
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        uvSet : 'unicode'
            UV set to work with
        
        
        Returns:
        ('float', 'float')
        
        Derived from api method `maya.OpenMaya.MSpace.getUVAtPoint`
        """
        pass

    def getUVIndex(self, vertex, uvSet='None'):
        """
        Returns the index of the texture coordinate for the given vertex. This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh::getUVs.
        
        Parameters:
        vertex : 'int'
            The face-relative vertex index of the current polygon
        uvSet : 'unicode'
            UV set to work with
        
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getUVIndex`
        """
        pass

    def getUVSetNames(self):
        """
        This method is used to find the UV set names mapped to the current face.
        
        Returns:
        List['list']
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getUVSetNames`
        """
        pass

    def getUVs(self, uvSet='None'):
        """
        Return the all the texture coordinates for the vertices of this face (in local vertex order).
        
        Parameters:
        uvSet : 'unicode'
            UV set to work with
        
        
        Returns:
        Tuple[List['float'], List['float']]
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getUVs`
        """
        pass

    def getVertices(self):
        """
        This method gets the indices of the vertices of the current face
        
        Returns:
        List['int']
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.getVertices`
        """
        pass

    def hasColor(self):
        """
        This method determines whether the current face has color-per-vertex set for any vertex.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.hasColor`
        """
        pass

    def hasUVs(self):
        """
        Tests whether this face has UV's mapped or not (either all the vertices for a face should have UV's, or none of them do, so the UV count for a face is either 0, or equal to the number of vertices).
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.hasUVs`
        """
        pass

    def hasValidTriangulation(self):
        """
        This method checks if the face has a valid triangulation. If it doesn't, then the face was bad geometry: it may gave degenerate points or cross over itself.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.hasValidTriangulation`
        """
        pass

    def isConnectedTo(self, component):
        """
        Parameters
        ----------
        component : Union[MeshFace, MeshEdge, MeshVertex]
        
        Returns
        -------
        bool
        """
        pass

    def isConnectedToEdge(self, index):
        """
        This method determines whether the given edge is connected to a vertex in the current face
        
        Parameters:
        index : 'int'
            Index of the edge to be tested for
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isConnectedToEdge`
        """
        pass

    def isConnectedToFace(self, index):
        """
        This method determines whether the given face is adjacent to the current face
        
        Parameters:
        index : 'int'
            Index of the face to be tested for
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isConnectedToFace`
        """
        pass

    def isConnectedToVertex(self, index):
        """
        This method determines whether the given vertex shares an edge with a vertex in the current face.
        
        Parameters:
        index : 'int'
            Index of the vertex to be tested for
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isConnectedToVertex`
        """
        pass

    def isConvex(self):
        """
        This method checks if the face is convex.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isConvex`
        """
        pass

    def isHoled(self):
        """
        This method checks if the face has any holes.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isHoled`
        """
        pass

    def isLamina(self):
        """
        This method checks if the face is a lamina (the face is folded over onto itself).
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isLamina`
        """
        pass

    def isOnBoundary(self):
        """
        This method determines whether the current face is on a boundary
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.onBoundary`
        """
        pass

    def isPlanar(self):
        """
        This method checks if the face is planar
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isPlanar`
        """
        pass

    def isStarlike(self):
        """
        This method checks if the face is starlike. That is, a line from the centre to any vertex lies entirely within the face.
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isStarlike`
        """
        pass

    def isUVReversed(self, uvSet='None'):
        """
        This method checks if the winding order of UV's for this face are reversed (clockwise), or not (counter clockwise)
        
        Parameters:
        uvSet : 'unicode'
            UV set to work with
        
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.isUVReversed`
        """
        pass

    def isZeroArea(self):
        """
        This method checks if its a zero area face
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.zeroArea`
        """
        pass

    def isZeroUVArea(self):
        """
        This method checks if the UV area of the face is zero
        
        Returns:
        'bool'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.zeroUVArea`
        """
        pass

    def normalIndex(self, localVertexIndex):
        """
        Returns the normal index for the specified vertex. This index refers to an element in the normal array returned by MFnMesh::getNormals. These normals are per-polygon per-vertex normals. See the MFnMesh description for more information on normals.
        
        Parameters:
        localVertexIndex : 'int'
            The face-relative index of the vertex to examine for the current polygon
        
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.normalIndex`
        """
        pass

    def numColors(self, colorSetName='None'):
        """
        This method checks for the number of colors on vertices in this face.
        
        Parameters:
        colorSetName : 'unicode'
            Name of the color set.
        
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.numColors`
        """
        pass

    def numConnectedEdges(self):
        """
        This method checks for the number of connected edges on the vertices of this face
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.numConnectedEdges`
        """
        pass

    def numConnectedFaces(self):
        """
        This method checks for the number of connected faces
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.numConnectedFaces`
        """
        pass

    def numTriangles(self):
        """
        This Method checks for the number of triangles in this face in the current triangulation
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.numTriangles`
        """
        pass

    def numVertices(self):
        """
        Return the number of vertices for the current polygon.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.polygonVertexCount`
        """
        pass

    def polygonVertexCount(self):
        """
        Return the number of vertices for the current polygon.
        
        Returns:
        'int'
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.polygonVertexCount`
        """
        pass

    def setPoint(self, point, index, space="'preTransform'"):
        """
        Set the vertex at the given index in the current polygon.
        
        Parameters:
        point : 'Point'
            The new position for the vertex
        index : 'int'
            The face-relative index of the vertex in the current polygon
        space : 'Space.Space'
            The coordinate system for this operation
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.setPoint`
        """
        pass

    def setPoints(self, pointArray, space="'preTransform'"):
        """
        Sets new locations for vertices of the current polygon that the iterator is pointing to.
        
        Parameters:
        pointArray : List['Point']
            The new positions for the vertices.
        space : 'Space.Space'
            The coordinate system for this operation.
        
            values: 'transform', 'preTransform', 'object', 'world'
        
        Derived from api method `maya.OpenMaya.MSpace.setPoints`
        """
        pass

    def setUV(self, vertexId, uvPoint, uvSet='None'):
        """
        Modify the UV value for the given vertex in the current face. If the face is not already mapped, this method will fail.
        
        Parameters:
        vertexId : 'int'
            face-relative index of the vertex to set UV for.
        uvPoint : ('float', 'float')
            The UV values to set it to
        uvSet : 'unicode'
            UV set to work with
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.setUV`
        """
        pass

    def setUVs(self, uArray, vArray, uvSet='None'):
        """
        Modify the UV value for all vertices in the current face. If the face has not already been mapped, this method will fail.
        
        Parameters:
        uArray : List['float']
            All the U values - in local face order
        vArray : List['float']
            The corresponding V values
        uvSet : 'unicode'
            UV set to work with
        
        Derived from api method `maya.OpenMaya.MItMeshPolygon.setUVs`
        """
        pass

    def updateSurface(self):
        """
        Signal that this polygonal surface has changed and needs to redraw itself.
        Derived from api method `maya.OpenMaya.MItMeshPolygon.updateSurface`
        """
        pass

    __apicls__ = None

    __readonly__ = {}


def connectAttr(source, destination, **kwargs):
    """
    Connect the attributes of two dependency nodes and return the names of the two
    connected attributes. The connected attributes must be be of compatible types.
    First argument is the source attribute, second one is the destination. Refer to
    dependency node documentation.
    
    Maya Bug Fix:
      - even with the 'force' flag enabled, the command would raise an error if the connection already existed.
    
    Flags:
    - force : f                      (bool)          [create]
        Forces the connection.  If the destination is already connected, the old
        connection is broken and the new one made.
    
    - lock : l                       (bool)          [create]
        If the argument is true, the destination attribute is locked after making the
        connection. If the argument is false, the connection is unlocked before making
        the connection.
    
    - nextAvailable : na             (bool)          [create]
        If the destination multi-attribute has set the indexMatters to be false with
        this flag specified, a connection is made to the next available index. No index
        need be specified.
    
    - referenceDest : rd             (unicode)       [create]
        This flag is used for file io only. The flag indicates that the connection
        replaces a connection made in a referenced file, and the flag argument indicates
        the original destination from the referenced file. This flag is used so that if
        the reference file is modified, maya can still attempt to make the appropriate
        connections in the main scene to the referenced object.                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.connectAttr`
    """
    pass


def scale(obj, *args, **kwargs):
    """
    The scale command is used to change the sizes of geometric objects. The default
    behaviour, when no objects or flags are passed, is to do a relative scale on
    each currently selected object object using each object's existing scale pivot
    point.
    
    Modifications:
      - allows any iterable object to be passed as first argument::
    
            scale("pSphere1", [0,1,2])
    
    NOTE: this command also reorders the argument order to be more intuitive, with the object first
    
    Flags:
    - absolute : a                   (bool)          [create]
        Perform an absolute operation.
    
    - centerPivot : cp               (bool)          [create]
        Let the pivot be the center of the bounding box of all objects
    
    - componentSpace : cs            (bool)          [create]
        Move in local component space
    
    - constrainAlongNormal : xn      (bool)          [create]
        When true, transform constraints are applied along the vertex normal first and
        only use the closest point when no intersection is found along the normal.
    
    - deletePriorHistory : dph       (bool)          [create]
        If true then delete the history prior to the current operation.
    
    - distanceOnly : dso             (bool)          [create]
        Scale only the distance between the objects.
    
    - localSpace : ls                (bool)          [create]
        Use local space for scaling
    
    - objectCenterPivot : ocp        (bool)          [create]
        Let the pivot be the center of the bounding box of each object
    
    - objectSpace : os               (bool)          [create]
        Use object space for scaling
    
    - orientAxes : oa                (float, float, float) [create]
        Use the angles for the orient axes.
    
    - pivot : p                      (float, float, float) [create]
        Define the pivot point for the transformation
    
    - preserveChildPosition : pcp    (bool)          [create]
        When true, transforming an object will apply an opposite transform to its child
        transform to keep them at the same world-space position. Default is false.
    
    - preserveGeometryPosition : pgp (bool)          [create]
        When true, transforming an object will apply an opposite transform to its
        geometry points to keep them at the same world-space position. Default is false.
    
    - preserveUV : puv               (bool)          [create]
        When true, UV values on scaled components are projected along the axis of
        scaling in 3d space. For small edits, this will freeze the world space texture
        mapping on the object. When false, the UV values will not change for a selected
        vertices. Default is false.
    
    - reflection : rfl               (bool)          [create]
        To move the corresponding symmetric components also.
    
    - reflectionAboutBBox : rab      (bool)          [create]
        Sets the position of the reflection axis  at the geometry bounding box
    
    - reflectionAboutOrigin : rao    (bool)          [create]
        Sets the position of the reflection axis  at the origin
    
    - reflectionAboutX : rax         (bool)          [create]
        Specifies the X=0 as reflection plane
    
    - reflectionAboutY : ray         (bool)          [create]
        Specifies the Y=0 as reflection plane
    
    - reflectionAboutZ : raz         (bool)          [create]
        Specifies the Z=0 as reflection plane
    
    - reflectionTolerance : rft      (float)         [create]
        Specifies the tolerance to findout the corresponding reflected components
    
    - relative : r                   (bool)          [create]
        Perform a operation relative to the object's current position
    
    - scaleX : x                     (bool)          [create]
        Scale in X direction
    
    - scaleXY : xy                   (bool)          [create]
        Scale in X and Y direction
    
    - scaleXYZ : xyz                 (bool)          [create]
        Scale in all directions (default)
    
    - scaleXZ : xz                   (bool)          [create]
        Scale in X and Z direction
    
    - scaleY : y                     (bool)          [create]
        Scale in Y direction
    
    - scaleYZ : yz                   (bool)          [create]
        Scale in Y and Z direction
    
    - scaleZ : z                     (bool)          [create]
        Scale in Z direction
    
    - symNegative : smn              (bool)          [create]
        When set the component transformation is flipped so it is relative to the
        negative side of the symmetry plane. The default (no flag) is to transform
        components relative to the positive side of the symmetry plane.
    
    - worldSpace : ws                (bool)          [create]
        Use world space for scaling
    
    - xformConstraint : xc           (unicode)       [create]
        Apply a transform constraint to moving components. none - no constraintsurface -
        constrain components to the surfaceedge - constrain components to surface
        edgeslive - constraint components to the live surfaceFlag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.scale`
    """
    pass


def getClassification(*args, **kwargs):
    """
    Returns the classification string for a given node type. Classification strings
    look like file pathnames (shader/reflectiveor texture/2D, for example).
    Multiple classifications can be combined into a single compound classification
    string by joining the individual classifications with ':'. For example, the
    classification string shader/reflective:texture/2Dmeans that the node is both a
    reflective shader and a 2D texture. The classification string is used to
    determine how rendering nodes are categorized in various UI, such as the Create
    Render Node and HyperShade windows: CategoryClassification String2D
    Texturestexture/2d3D Texturestexture/3dEnv Texturestexture/environmentSurface
    Materialsshader/surfaceVolumetric Materialsshader/volumeDisplacement
    Materialsshader/displacementLightslightGeneral Utilitiesutility/generalColor
    Utilitiesutility/colorParticle Utilitiesutility/particleImage
    PlanesimageplaneGlowpostprocess/opticalFXThe classification string is also used
    to determine how Viewport 2.0 will interpret the node. CategoryClassification
    StringGeometrydrawdb/geometryTransformdrawdb/geometry/transformSub-Scene
    Objectdrawdb/subsceneShaderdrawdb/shaderSurface Shaderdrawdb/shader/surface
    
    Modifications:
      - previously returned a list with a single colon-separated string of classifications. now returns a list of classifications
    
    
    Modifications:
      - supports satisfies flag.
        Returns true if the given node type's classification satisfies the classification string which is passed with the flag.
    
        Returns
        -------
        Union[bool, List[unicode]]
        
    
    Flags:
    - satisfies : sat                (unicode)       [create]
        Returns true if the given node type's classification satisfies the
        classification string which is passed with the flag. A non-compound
        classification string A is said to satisfy a non-compound classification string
        B if A is a subclassification of B (for example, shaders/reflectivesatisfies
        shaders). A compound classification string A satisfies a compound classification
        string B iff: every component of A satisfies at least one component of B and
        every component of B is satisfied by at least one component of AHence,
        shader/reflective/phong:texturesatisfies shader:texture, but
        shader/reflective/phongdoes not satisfy shader:texture.                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.getClassification`
    """
    pass


def instance(*args, **kwargs):
    """
    Instancing is a way of making the same object appear twice in the scene. This is
    accomplished by creation of a new transform node that points to an exisiting
    object. Changes to the transform are independent but changes to the
    instancedobject affect all instances since the node is shared. If no objects are
    given, then the selected list is instanced. When an object is instanced a  new
    transform node is created that points to the selected object. The smart
    transform feature allows instance to transform newly instanced objects based on
    previous transformations between instances. Example: Instance an object and move
    it to a new location.  Instance it again with the smart transform flag.  It
    should have moved once again the distance you had previously moved it. Note:
    changing the selected list between smart instances will cause the transform
    information to be deleted. It returns a list of the new objects created by the
    instance operation. See also:duplicate
    
    Flags:
    - leaf : lf                      (bool)          [create]
        Instances leaf-level objects. Acts like duplicate except leaf-level objects are
        instanced.
    
    - name : n                       (unicode)       [create]
        Name to give new instance
    
    - smartTransform : st            (bool)          [create]
        Transforms instances item based on movements between transforms
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.instance`
    """
    pass


def _MPlugIn(x): pass


def assembly(*args, **kwargs):
    """
    Command to register assemblies for the scene assembly framework, to create them,
    and to edit and query them. Assembly nodes are DAG nodes, and are therefore
    shown in the various DAG editors (Outliner, Hypergraph, Node Editor). At
    assembly creation time, the node name defaults to the node type name. The
    assembly command can create any node that is derived from the assembly node base
    class.  It also acts as a registry of these types, so that various scripting
    callbacks can be defined and registered with the assembly command.  These
    callbacks are invoked by Maya during operations on assembly nodes, and can be
    used to customize behavior. In query mode, return type is based on queried flag.
    
    Flags:
    - active : a                     (unicode)       [query,edit]
        Set the active representation by name, or query the name of the active
        representation. Edit mode can be applied to more than one assembly. Query mode
        will return a single string when only a single assembly is specified, and will
        return an array of strings when multiple assemblies are specified. Using an
        empty string as name means to inactivate the currently active representation.
    
    - activeLabel : al               (unicode)       [query,edit]
        Set the active representation by label, or query the label of the active
        representation. Edit mode can be applied to more than one assembly. Query mode
        will return a single string when only a single assembly is specified, and will
        return an array of strings when multiple assemblies are specified.
    
    - canCreate : cc                 (unicode)       [query]
        Query the representation types the specific assembly can create.
    
    - createOptionBoxProc : cob      (script)        [query,edit]
        Set or query the option box menu procedure for a specific assembly type. The
        assembly type will be the default type, unless the -type flag is used to specify
        an explicit assembly type.
    
    - createRepresentation : cr      (unicode)       [edit]
        Create and add a specific type of representation for an assembly. If the
        representation type needs additional parameters, they must be specified using
        the inputflag. For example, the Maya scene assembly reference implementation
        Cache and Scene representations need an input file.
    
    - defaultType : dt               (unicode)       [query,edit]
        Set or query the default type of assembly.  When the assembly command is used to
        perform an operation on an assembly type rather than on an assembly object, it
        will be performed on the default type, unless the -type flag is used to specify
        an explicit assembly type.
    
    - deleteRepresentation : dr      (unicode)       [edit]
        Delete a specific representation from an assembly.
    
    - deregister : d                 (unicode)       [edit]
        Deregister a registered assembly type. If the deregistered type is the default
        type, the default type will be set to the empty string.
    
    - input : input                  (unicode)       [edit]
        Specify the additional parameters of representation creation procedure when
        creating a representation. This flag must be used with createRepresentation
        flag.
    
    - isAType : isa                  (unicode)       [query]
        Query whether the given object is of an assembly type.
    
    - isTrackingMemberEdits : ite    (unicode)       [query]
        Query whether the given object is tracking member edits.
    
    - label : lbl                    (unicode)       [query,edit]
        Set or query the label for an assembly type. Assembly type is specified with
        flag type. If no type specified, the default type is used.
    
    - listRepTypes : lrt             (bool)          [query]
        Query the supported representation types for a given assembly type.  The
        assembly type will be the default type, unless the -type flag is used to specify
        an explicit assembly type.
    
    - listRepTypesProc : lrp         (script)        [query,edit]
        Set or query the procedure that provides the representation type list which an
        assembly type supports.  This procedure takes no argument, and returns a string
        array of representation types that represents the full set of representation
        types this assembly type can create.  The assembly type for which this procedure
        applies will be the default type, unless the type flag is used to specify an
        explicit assembly type.
    
    - listRepresentations : lr       (bool)          [query]
        Query the created representations list for a specific assembly.  The -repType
        flag can be used to filter the list and return representations for a single
        representation type.  If the -repType flag is not used, all created
        representations will be returned.
    
    - listTypes : lt                 (bool)          [query]
        Query the supported assembly types.
    
    - name : n                       (unicode)       [create]
        Specify the name of the assembly when creating it.
    
    - newRepLabel : nrl              (unicode)       [edit]
        Specify the representation label to set on representation label edit.
    
    - postCreateUIProc : aoc         (script)        [query,edit]
        Set or query the UI post-creation procedure for a given assembly type. This
        procedure will be invoked by Maya immediately after an assembly of the specified
        type is created from the UI, but not through scripting.  It can be used to
        invoke a dialog, to obtain and set initial parameters on a newly-created
        assembly.  The assembly type will be the default type, unless the -type flag is
        used to specify an explicit assembly type.
    
    - proc : prc                     (script)        [edit]
        Specify the procedure when setting the representation UI post- or pre-creation
        procedure, for a given assembly type.  The assembly type will be the default
        type, unless the -type flag is used to specify an explicit assembly type.
    
    - renameRepresentation : rnr     (unicode)       [edit]
        Renames the representation that is the argument to this flag.  The repName flag
        must be used to provide the new name.
    
    - repLabel : rl                  (unicode)       [query,edit]
        Query or edit the label of the representation that is the argument to this flag,
        for a given assembly.  In both query and edit modes, the -repLabel flag
        specifies the name of the representation.  In edit mode, the -newRepLabel flag
        must be used to specify the new representation label.
    
    - repName : rnm                  (unicode)       [edit]
        Specify the representation name to set on representation creation or rename.
        This flag is optional with the createRepresentation flag: if omitted, the
        assembly will name the representation.  It is mandatory with the
        renameRepresentation flag.
    
    - repNamespace : rns             (unicode)       [query]
        Query the representation namespace of this assembly node. The value returned is
        used by Maya for creating the namespace where nodes created by the activation of
        a representation will be added. If a name clash occurs when the namespace is
        added to its parent namespace, Maya will update repNamespace with the new name.
        Two namespaces are involved when dealing with an assembly node: the namespace of
        the assembly node itself (which this flag does not affect or query), and the
        namespace of its representations. The representation namespace is a child of its
        assembly node's namespace. The assembly node's namespace is set by its
        containing assembly, if it is nested, or by the top-level file. Either the
        assembly node's namespace, or the representation namespace, or both, can be the
        empty string. It should be noted that if the assembly node is nested, the
        assembly node's namespace will be (by virtue of its nesting) the representation
        namespace of its containing assembly.
    
    - repPostCreateUIProc : poc      (unicode)       [query,edit]
        Set or query the UI post-creation procedure for a specific representation type,
        and for a specific assembly type.  This procedure takes two arguments, the first
        the DAG path to the assembly, and the second the name of the representation.  It
        returns no value.  It will be invoked by Maya immediately after a representation
        of the specified type is created from the UI, but not through scripting.  It can
        be used to invoke a dialog, to obtain and set initial parameters on a newly-
        created representation.  The representation type is the argument of this flag.
        The -proc flag must be used to specify the procedure name.  The assembly type
        will be the default type, unless the -type flag is used to specify an explicit
        assembly type.
    
    - repPreCreateUIProc : pec       (unicode)       [query,edit]
        Set or query the UI pre-creation procedure for a specific representation type,
        and for a specific assembly type.  This procedure takes no argument, and returns
        a string that is passed as an argument to the -input flag when Maya invokes the
        assembly command with the -createRepresentation flag. The representation pre-
        creation procedure is invoked by Maya immediately before creating a
        representation of the specified type from the UI, but not through scripting.  It
        can be used to invoke a dialog, to obtain the creation argument for a new
        representation.  The representation type is the argument of this flag.  The
        -proc flag must be used to specify the procedure name.  The assembly type will
        be the default type, unless the -type flag is used to specify an explicit
        assembly type.
    
    - repType : rt                   (unicode)       [query]
        Specify a representation type to use as a filter for the -listRepresentations
        query.  The representation type is the argument to this flag.
    
    - repTypeLabel : rtl             (unicode)       [query]
        Query the label of the specific representation type.
    
    - repTypeLabelProc : rtp         (script)        [query,edit]
        Set or query the procedure that provides the representation type label, for a
        given assembly type.  The procedure takes the representation type as its sole
        argument, and returns a localized representation type label. The assembly type
        for which this procedure applies will be the default type, unless the -type flag
        is used to specify an explicit assembly type.
    
    - type : typ                     (unicode)       [create,query,edit]
        Set or query properties for the specified registered assembly type. Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.assembly`
    """
    pass


def _instancer(*args, **kwargs):
    """
    Maya Bug Fix:
      - name of newly created instancer was not returned
    """
    pass


def _getPymelType(arg, name):
    """
    Get the correct Pymel Type for an object that can be a MObject, PyNode or
    name of an existing Maya object, if no correct type is found returns
    DependNode by default.
    
    If the name of an existing object is passed, the name and MObject will be
    returned. If a valid MObject is passed, the name will be returned as None
    If a PyNode instance is passed, its name and MObject will be returned
    """
    pass


def _spaceLocator(*args, **kwargs):
    """
    Modifications:
        - returns a single Transform instead of a list with a single locator
    """
    pass


def move(*args, **kwargs):
    """
    The move command is used to change the positions of geometric objects. The
    default behaviour, when no objects or flags are passed, is to do a absolute move
    on each currently selected object in the world space. The value of the
    coordinates are interpreted as being defined in the current linear unit unless
    the unit is explicitly mentioned. When using -objectSpace there are two ways to
    use this command. If numbers are typed without units then the internal values of
    the object are set to these values. If, on the other hand a unit is specified
    then the internal value is set to the equivalent internal value that represents
    that world-space distance. The -localSpace flag moves the object in its parent
    space. In this space the x,y,z values correspond directly to the tx, ty, tz
    channels on the object. The -rotatePivotRelative/-scalePivotRelative flags can
    be used with the -absolute flag to translate an object so that its pivot point
    ends up at the given absolute position. These flags will be ignored if
    components are specified. The -worldSpaceDistance flag is a modifier flag that
    may be used in conjunction with the -objectSpace/-localSpace flags. When this
    flag is specified the command treats the x,y,z values as world space units so
    the object will move the specified world space distance but it will move along
    the axis specified by the -objectSpace/-localSpace flag. The default behaviour,
    without this flag, is to treat the x,y,z values as units in object space or
    local space. In other words, the worldspace distance moved will depend on the
    transformations applied to the object unless this flag is specified.
    
    Modifications:
      - allows any iterable object to be passed as first argument::
    
            move("pSphere1", [0,1,2])
    
    NOTE: this command also reorders the argument order to be more intuitive, with the object first
    
    Flags:
    - absolute : a                   (bool)          [create]
        Perform an absolute operation.
    
    - componentOffset : co           (bool)          [create]
        Move components individually in local space
    
    - componentSpace : cs            (bool)          [create]
        Move in local component space
    
    - constrainAlongNormal : xn      (bool)          [create]
        When true, transform constraints are applied along the vertex normal first and
        only use the closest point when no intersection is found along the normal.
    
    - deletePriorHistory : dph       (bool)          [create]
        If true then delete the history prior to the current operation.
    
    - localSpace : ls                (bool)          [create]
        Move in local space
    
    - moveX : x                      (bool)          [create]
        Move in X direction
    
    - moveXY : xy                    (bool)          [create]
        Move in XY direction
    
    - moveXYZ : xyz                  (bool)          [create]
        Move in all directions (default)
    
    - moveXZ : xz                    (bool)          [create]
        Move in XZ direction
    
    - moveY : y                      (bool)          [create]
        Move in Y direction
    
    - moveYZ : yz                    (bool)          [create]
        Move in YZ direction
    
    - moveZ : z                      (bool)          [create]
        Move in Z direction
    
    - objectSpace : os               (bool)          [create]
        Move in object space
    
    - orientJoint : oj               (unicode)       [create]
        Default is xyz.
    
    - parameter : p                  (bool)          [create]
        Move in parametric space
    
    - preserveChildPosition : pcp    (bool)          [create]
        When true, transforming an object will apply an opposite transform to its child
        transform to keep them at the same world-space position. Default is false.
    
    - preserveGeometryPosition : pgp (bool)          [create]
        When true, transforming an object will apply an opposite transform to its
        geometry points to keep them at the same world-space position. Default is false.
    
    - preserveUV : puv               (bool)          [create]
        When true, UV values on translated components are projected along the
        translation in 3d space. For small edits, this will freeze the world space
        texture mapping on the object. When false, the UV values will not change for a
        selected vertices. Default is false.
    
    - reflection : rfl               (bool)          [create]
        To move the corresponding symmetric components also.
    
    - reflectionAboutBBox : rab      (bool)          [create]
        Sets the position of the reflection axis  at the geometry bounding box
    
    - reflectionAboutOrigin : rao    (bool)          [create]
        Sets the position of the reflection axis  at the origin
    
    - reflectionAboutX : rax         (bool)          [create]
        Specifies the X=0 as reflection plane
    
    - reflectionAboutY : ray         (bool)          [create]
        Specifies the Y=0 as reflection plane
    
    - reflectionAboutZ : raz         (bool)          [create]
        Specifies the Z=0 as reflection plane
    
    - reflectionTolerance : rft      (float)         [create]
        Specifies the tolerance to findout the corresponding reflected components
    
    - relative : r                   (bool)          [create]
        Perform a operation relative to the object's current position
    
    - rotatePivotRelative : rpr      (bool)          [create]
        Move relative to the object's rotate pivot point.
    
    - scalePivotRelative : spr       (bool)          [create]
        Move relative to the object's scale pivot point.
    
    - secondaryAxisOrient : sao      (unicode)       [create]
        Default is xyz.
    
    - symNegative : smn              (bool)          [create]
        When set the component transformation is flipped so it is relative to the
        negative side of the symmetry plane. The default (no flag) is to transform
        components relative to the positive side of the symmetry plane.
    
    - worldSpace : ws                (bool)          [create]
        Move in world space
    
    - worldSpaceDistance : wd        (bool)          [create]
        Move is specified in world space units
    
    - xformConstraint : xc           (unicode)       [create]
        Apply a transform constraint to moving components. none - no constraintsurface -
        constrain components to the surfaceedge - constrain components to surface
        edgeslive - constraint components to the live surfaceFlag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.move`
    """
    pass


def listHistory(*args, **kwargs):
    """
    This command traverses backwards or forwards in the graph from the specified
    node and returns all of the nodes whose construction history it passes through.
    The construction history consists of connections to specific attributes of a
    node defined as the creators and results of the node's main data, eg. the curve
    for a Nurbs Curve node. For information on history connections through specific
    plugs use the listConnectionscommand first to find where the history begins then
    use this command on the resulting node.
    
    Modifications:
      - returns an empty list when the result is None
      - raises a RuntimeError when the arg is an empty list, tuple, set, or
            frozenset, making it's behavior consistent with when None is passed, or
            no args and nothing is selected (would formerly raise a TypeError)
      - added a much needed 'type' filter
      - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
    
    Returns
    -------
    List[nodetypes.DependNode]
    
    Flags:
    - allConnections : ac            (bool)          [create]
        If specified, the traversal that searches for the history or future will not
        restrict its traversal across nodes to only dependent plugs. Thus it will reach
        all upstream nodes (or all downstream nodes for f/future).
    
    - allFuture : af                 (bool)          [create]
        If listing the future, list all of it. Otherwise if a shape has an attribute
        that represents its output geometry data, and that plug is connected, only list
        the future history downstream from that connection.
    
    - allGraphs : ag                 (bool)          [create]
        This flag is obsolete and has no effect.
    
    - breadthFirst : bf              (bool)          [create]
        The breadth first traversal will return the closest nodes in the traversal
        first. The depth first traversal will follow a complete path away from the node,
        then return to any other paths from the node. Default is depth first.
    
    - future : f                     (bool)          [create]
        List the future instead of the history.
    
    - futureLocalAttr : fl           (bool)          [query]
        This flag allows querying of the local-space future-related attribute(s) on
        shape nodes.
    
    - futureWorldAttr : fw           (bool)          [query]
        This flag allows querying of the world-space future-related attribute(s) on
        shape nodes.
    
    - groupLevels : gl               (bool)          [create]
        The node names are grouped depending on the level.  1 is the lead, the rest are
        grouped with it.
    
    - historyAttr : ha               (bool)          [query]
        This flag allows querying of the attribute where history connects on shape
        nodes.
    
    - interestLevel : il             (int)           [create]
        If this flag is set, only nodes whose historicallyInteresting attribute value is
        not less than the value will be listed. The historicallyInteresting attribute is
        0 on nodes which are not of interest to non-programmers.  1 for the TDs, 2 for
        the users.
    
    - leaf : lf                      (bool)          [create]
        If transform is selected, show history for its leaf shape. Default is true.
    
    - levels : lv                    (int)           [create]
        Levels deep to traverse. Setting the number of levels to 0 means do all levels.
        All levels is the default.
    
    - pruneDagObjects : pdo          (bool)          [create]
        If this flag is set, prune at dag objects.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.listHistory`
    """
    pass


def group(*args, **kwargs):
    """
    This command groups the specified objects under a new group and returns the name
    of the new group. If the -em flag is specified, then an empty group (with no
    objects) is created. If the -w flag is specified then the new group is placed
    under the world, otherwise if -p is specified it is placed under the specified
    node. If neither -w or -p is specified the new group is placed under the lowest
    common group they have in common. (or the world if no such group exists) If an
    object is grouped with another object that has the same name then one of the
    objects will be renamed by this command.
    
    Modifications
      - if no objects are passed or selected, the empty flag is automatically set
    Maya Bug Fix:
      - corrected to return a unique name
    
    Flags:
    - absolute : a                   (bool)          [create]
        preserve existing world object transformations (overall object transformation is
        preserved by modifying the objects local transformation) [default]
    
    - empty : em                     (bool)          [create]
        create an empty group (with no objects in it)
    
    - name : n                       (unicode)       [create]
        Assign given name to new group node.
    
    - parent : p                     (unicode)       [create]
        put the new group under the given parent
    
    - relative : r                   (bool)          [create]
        preserve existing local object transformations (relative to the new group node)
    
    - useAsGroup : uag               (unicode)       [create]
        Use the specified node as the group node. The specified node must be derived
        from the transform node and must not have any existing parents or children.
    
    - world : w                      (bool)          [create]
        put the new group under the world                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.group`
    """
    pass


def validComponentIndexType(argObj, allowDicts='True', componentIndexTypes='None'):
    """
    True if argObj is of a suitable type for specifying a component's index.
    False otherwise.
    
    Dicts allow for components whose 'mel name' may vary - ie, a single
    isoparm component may have, u, v, or uv elements; or, a single pivot
    component may have scalePivot and rotatePivot elements.  The key of the
    dict would indicate the 'mel component name', and the value the actual
    indices.
    
    Thus:
       {'u':3, 'v':(4,5), 'uv':ComponentIndex((1,4)) }
    would represent single component that contained:
       .u[3]
       .v[4]
       .v[5]
       .uv[1][4]
    
    Derived classes should implement:
    _dimLength
    """
    pass


def createDisplayLayer(*args, **kwargs):
    """
    Create a new display layer.  The display layer number will be assigned based on
    the first unassigned number not less than the base index number found in the
    display layer global parameters.  Normally all objects and their descendants
    will be added to the new display layer but if the '-nr' flag is specified then
    only the objects themselves will be added.
    
    Flags:
    - empty : e                      (bool)          [create]
        If set then create an empty display layer.  ie. Do not add the selected items to
        the new display layer.
    
    - makeCurrent : mc               (bool)          [create]
        If set then make the new display layer the current one.
    
    - name : n                       (unicode)       [create]
        Name of the new display layer being created.
    
    - noRecurse : nr                 (bool)          [create]
        If set then only add selected objects to the display layer.  Otherwise all
        descendants of the selected objects will also be added.
    
    - number : num                   (int)           [create]
        Number for the new display layer being created.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.createDisplayLayer`
    """
    pass


def selectionConnection(*args, **kwargs):
    """
    This command creates a named selectionConnection object. This object is simply a
    shared selection list. It may be used by editors to share their highlight data.
    For example, an outliner may attach its selected list to one of these objects,
    and a graph editor may use the same object as a list source. Then, the graph
    editor would only display objects that are selected in the outliner. Selection
    connections are UI objects which contain a list of model objects. Selection
    connections are useful for specifying which objects are to be displayed within a
    particular editor. Editor's have three plug socketswhere a selection connection
    may be attached. They are: mainListConnectionan inputsocket which contains a
    list of objects that are to be displayed within the editorselectionConnectionan
    outputsocket which contains a list of objects that are selectedwithin the
    editorhighlightConnectionan inputsocket which contains a list of objects that
    are to be highlightedwithin the editorThere are several different types of
    selection connections that may be created. They include: activeLista selection
    connection which contains a list of everything in the model which is active
    (which includes geometry objects and keys)modelLista selection connection which
    contains a list of all the geometry (i.e. excluding keys) objects that are
    currently activekeyframeLista selection connection which contains a list of all
    the keys that are currently activeworldLista selection connection which contains
    a list of all the objects in the worldobjectLista selection connection which
    contains one model object (which may be a set)listLista selection connection
    which contains a list of selection connectionseditorLista selection connection
    which contains a list of objects that are attached to the mainListConnection of
    the specified editorsetLista selection connection which contains a list of all
    the sets in the worldcharacterLista selection connection which contains a list
    of all the characters in the worldhighlightLista selection connection which
    contains a list of objects to be highlighted in some fashionBelow is an example
    selectionConnection network between two editors. Editor 1 is setup to display
    objects on the activeList. Editor 2 is setup to display objects which are
    selected within Editor 1, and objects that are selected in Editor 2 are
    highlighted within Editor 1: -- Editor 1--       -- Editor 2-- inputList--| main
    |      |  |-| main |      | |      | sele |--|  |      | sele |--| |-| high |
    |     | high |      |  | |   -------------       -------------   |
    |------------- fromEditor2 -------------| The following commands will establish
    this network: selectionConnection -activeList inputList; selectionConnection
    fromEditor1; selectionConnection fromEditor2; editor -edit -mainListConnection
    inputList Editor1; editor -edit -selectionConnection fromEditor1 Editor1; editor
    -edit -mainListConnection fromEditor1 Editor2; editor -edit -selectionConnection
    fromEditor2 Editor2; editor -edit -highlightConnection fromEditor2 Editor1;
    Note: to delete a selection connectionuse the deleteUI commandNote: commands
    which expect objects may be given a selection connection instead, and the
    command will operate upon the objects wrapped by the selection connectionNote:
    the graph editor and the dope sheet are the only editors which can use the
    editor connection to the highlightConnection of another editorWARNING: some flag
    combinations may not behave as you expect.  The command is really intended for
    internal use for managing the outliner used by the various editors.
    
    Flags:
    - activeCacheList : atc          (bool)          [create]
        Specifies that this connection should reflect the cache that objects on the
        active list belong to.
    
    - activeCharacterList : acl      (bool)          [create]
        Specifies that this connection should reflect the characters that objects on the
        active list belong to.
    
    - activeList : act               (bool)          [create]
        Specifies that this connection should reflect the active list (geometry objects
        and keys).
    
    - addScript : addScript          (script)        [create,query,edit]
        Specify a script to be called when something is added to the selection.
    
    - addTo : add                    (unicode)       [create,edit]
        The name of a selection connection that should be added to this list of
        connections.
    
    - characterList : cl             (bool)          [create]
        Specifies that this connection should reflect all the characters in the world.
    
    - clear : clr                    (bool)          [create,edit]
        Remove everything from the selection connection.
    
    - connectionList : lst           (bool)          [create,query]
        Specifies that this connection should contain a list of selection connections.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - deselect : d                   (PyNode)        [create,edit]
        Remove something from the selection.
    
    - editor : ed                    (unicode)       [create,query,edit]
        Specifies that this connection should reflect the -mainListConnection of the
        specified editor.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - filter : f                     (unicode)       [create,query,edit]
        Optionally specifies an itemFilter for this connection. An empty string ()
        clears the current filter. If a filter is specified, all the information going
        into the selectionConnection must first pass through the filter before being
        accepted.  NOTE: filters can only be attached to regular selectionConnections.
        They cannot be attached to any connection created using the -act, -mdl, -key,
        -wl, -sl, -cl, -lst, -obj, or -ren flags. We strongly recommend that you do not
        attach filters to a selectionConnection --- it is better to attach your filter
        to the editor that is using the selectionConnection instead.
    
    - findObject : fo                (PyNode)        [query]
        Find a selection connection in this list that wraps the specified object.
    
    - g : g                          (bool)          [create,query,edit]
        A global selection connection cannot be deleted by any script commands.
    
    - highlightList : hl             (bool)          [create]
        Specifies that this connection is being used as a highlight list.
    
    - identify : id                  (bool)          [query]
        Find out what type of selection connection this is.  May be: activeList |
        modelList | keyframeList | worldList | objectList listList | editorList |
        connection | unknown
    
    - keyframeList : key             (bool)          [create]
        Specifies that this connection should reflect the animation portion of the
        active list.
    
    - lock : lck                     (bool)          [create,query,edit]
        For activeList connections, locking the connection means that it will not listen
        to activeList changes.
    
    - modelList : mdl                (bool)          [create]
        Specifies that this connection should reflect the modeling (i.e. excluding keys)
        portion of the active list.
    
    - object : obj                   (PyNode)        [create,query,edit]
        Specifies that this connection should wrap around the specified object (which
        may be a set).  Query will return all the members of the selection connection
        (if the connection wraps a set, the set members will be returned)
    
    - parent : p                     (unicode)       [create,query,edit]
        The name of a UI object this should be attached to.  When the parent is
        destroyed, the selectionConnection will auto-delete. If no parent is specified,
        the connection is created in the current controlLayout.
    
    - remove : rm                    (unicode)       [create,edit]
        The name of a selection connection that should be removed from this list of
        connections.
    
    - removeScript : rs              (script)        [create,query,edit]
        Specify a script to be called when something is removed from the selection.
    
    - select : s                     (PyNode)        [create,edit]
        Add something to the selection. This does not replace the existing selection.
    
    - setList : sl                   (bool)          [create]
        Specifies that this connection should reflect all the sets in the world.
    
    - switch : sw                    (bool)          [create,query]
        Acts as a modifier to -connectionList which sets the list of objects to be the
        first non-empty selection connection.  selection connections are tested in the
        order in which they are added.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - worldList : wl                 (bool)          [create]
        Specifies that this connection should reflect all objects in the world.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.selectionConnection`
    """
    pass


def listFuture(*args, **kwargs):
    """
    Modifications:
      - returns an empty list when the result is None
      - added a much needed 'type' filter
      - added an 'exactType' filter (if both 'exactType' and 'type' are present, 'type' is ignored)
    
    Returns
    -------
    List[nodetypes.DependNode]
    """
    pass


def commandPort(*args, **kwargs):
    """
    Opens or closes the Maya command port. The command port comprises a socket to
    which a client program may connect. An example command port client mcpis
    included in the Motion Capture developers kit. It supports multi-byte commands
    and uses utf-8 as its transform format. It will receive utf8 command string and
    decode it to Maya native coding. The result will also be encoded to utf-8 before
    sending back. Care should be taken regarding INET domain sockets as no user
    identification, or authorization is required to connect to a given socket, and
    all commands (including system(...)) are allowed and executed with the user id
    and permissions of the Maya user. The prefix flag can be used to reduce this
    security risk, as only the prefix command is executed. The query flag can be
    used to determine if a given command port exists. See examples below.
    
    Flags:
    - bufferSize : bs                (int)           [create]
        Commands and results are each subject to size limits. This option allows the
        user to specify the size of the buffer used to communicate with Maya. If
        unspecified the default buffer size is 4096 characters. Commands longer than
        bufferSize characters will cause the client connection to close. Results longer
        that bufferSize characters are replaced with an error message.
    
    - close : cl                     (bool)          [create]
        Closes the commandPort, deletes the pipes
    
    - echoOutput : eo                (bool)          [create]
        Sends a copy of all command output to the command port. Typically only the
        result is transmitted. This option provides a copy of all output.
    
    - listPorts : lp                 (bool)          [create]
        Returns the available ports
    
    - name : n                       (unicode)       [create]
        Specifies the name of the command port which this command creates. CommandPort
        names of the form namecreate a UNIX domain socket on the localhost corresponding
        to name. If namedoes not begin with /, then /tmp/nameis used. If namebegins with
        /, namedenotes the full path to the socket.  Names of the form :port
        numbercreate an INET domain on the local host at the given port.
    
    - noreturn : nr                  (bool)          [create]
        Do not write the results from executed commands back to the command port socket.
        Instead, the results from executed commands are written to the script editor
        window. As no information passes back to the command port client regarding the
        execution of the submitted commands, care must be taken not to overflow the
        command buffer, which would cause the connection to close.
    
    - pickleOutput : po              (bool)          [create]
        Python output will be pickled.
    
    - prefix : pre                   (unicode)       [create]
        The string argument is the name of a Maya command taking one string argument.
        This command is called each time data is sent to the command port. The data
        written to the command port is passed as the argument to the prefix command. The
        data from the command port is encoded as with enocodeString and enclosed in
        quotes.  If newline characters are embedded in the command port data, the input
        is split into individual lines. These lines are treated as if they were separate
        writes to the command port. Only the result to the last prefix command is
        returned.
    
    - returnNumCommands : rnc        (bool)          [create]
        Ignore the result of the command, but return the number of commands that have
        been read and executed in this call. This is a simple way to track buffer
        overflow. This flag is ignored when the noreturnflag is specified.
    
    - securityWarning : sw           (bool)          [create]
        Enables security warning on command port input.
    
    - sourceType : stp               (unicode)       [create]
        The string argument is used to indicate which source type would be passed to the
        commandPort, like mel, python. The default source type is mel.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.commandPort`
    """
    pass


def delete(*args, **kwargs):
    """
    This command is used to delete selected objects, or all objects, or objects
    specified along with the command. Flags are available to filter the type of
    objects that the command acts on. At times, more than just specified items will
    be deleted.  For example, deleting two CVs in the same rowon a NURBS surface
    will delete the whole row.
    
    Modifications:
      - the command will not fail on an empty list
        
    
    Flags:
    - all : all                      (bool)          [create]
        Remove all objects of specified kind, in the scene. This flag is to be used in
        conjunction with the following flags.
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - channels : c                   (bool)          [create]
        Remove animation channels in the scene. Either all channels can be removed, or
        the scope can be narrowed down by specifying some of the above mentioned
        options.
    
    - constraints : cn               (bool)          [create]
        Remove selected constraints and constraints attached to the selected nodes, or
        remove all constraints in the scene.
    
    - constructionHistory : ch       (bool)          [create]
        Remove the construction history on the objects specified or selected.
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - expressions : e                (bool)          [create]
        Remove expressions in the scene. Either all expressions can be removed, or the
        scope can be narrowed down by specifying some of the above mentioned options.
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
    - inputConnectionsAndNodes : icn (bool)          [create]
        Break input connection to specified attribute and delete all unconnected nodes
        that are left behind. The graph will be traversed until a node that cannot be
        deleted is encountered.
    
    - motionPaths : mp               (bool)          [create]
        Remove motion paths in the scene. Either all motion paths can be removed, or the
        scope can be narrowed down by specifying some of the above mentioned options.
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - staticChannels : sc            (bool)          [create]
        Remove static animation channels in the scene. Either all static channels can be
        removed, or the scope can be narrowed down by specifying some of the above
        mentioned options.
    
    - timeAnimationCurves : tac      (bool)          [create]
        Modifies the -c/channels and -sc/staticChannels flags. When true, only channels
        connected to time-input animation curves (for instance, those created by
        'setKeyframe' will be deleted.  When false, no time-input animation curves will
        be deleted. Default: true.
    
    - unitlessAnimationCurves : uac  (bool)          [create]
        Modifies the -c/channels and -sc/staticChannels flags. When true, only channels
        connected to unitless-input animation curves (for instance, those created by
        'setDrivenKeyframe' will be deleted.  When false, no unitless-input animation
        curves will be deleted.  Default: true.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.delete`
    """
    pass


def _MDagPathIn(x): pass


def select(*args, **kwargs):
    """
    This command is used to put objects onto or off of the active list. If none of
    the five flags [-add, -af, -r, -d, -tgl] are specified, the default is to
    replace the objects on the active list with the given list of objects. When
    selecting a set as in select set1, the behaviour is for all the members of the
    set to become selected instead of the set itself. If you want to select a set,
    the -ne/noExpandflag must be used. With the advent of namespaces, selection by
    name may be confusing.  To clarify, without a qualified namespace, name lookup
    is limited to objects in the root namespace :. There are really two parts of a
    name: the namespace and the name itself which is unique within the namespace. If
    you want to select objects in a specific namespace, you need to include the
    namespace separator :. For example, 'select -r foo\*' is trying to look for an
    object with the fooprefix in the root namespace. It is not trying to look for
    all objects in the namespace with the fooprefix. If you want to select all
    objects in a namespace (foo), use 'select foo:\*'. Note: When the application
    starts up, there are several dependency nodes created by the system which must
    exist. These objects are not deletable but are selectable.  All objects (dag and
    dependency nodes) in the scene can be obtained using the lscommand without any
    arguments. When using the -all, adn/allDependencyNodesor
    -ado/allDagObjectsflags, only the deletable objects are selected.  The non
    deletable object can still be selected by explicitly specifying their name as in
    select time1;.
    
    Modifications:
      - passing an empty list no longer causes an error.
          instead, the selection is cleared if the selection mod is replace (the default);
          otherwise, it does nothing
    
    Flags:
    - add : add                      (bool)          [create]
        Indicates that the specified items should be added to the active list without
        removing existing items from the active list.
    
    - addFirst : af                  (bool)          [create]
        Indicates that the specified items should be added to the front of the active
        list without removing existing items from the active list.
    
    - all : all                      (bool)          [create]
        Indicates that all deletable root level dag objects and all deletable non-dag
        dependency nodes should be selected.
    
    - allDagObjects : ado            (bool)          [create]
        Indicates that all deletable root level dag objects should be selected.
    
    - allDependencyNodes : adn       (bool)          [create]
        Indicates that all deletable dependency nodes including all deletable dag
        objects should be selected.
    
    - clear : cl                     (bool)          [create]
        Clears the active list.  This is more efficient than select -d;.  Also select
        -d;will not remove sets from the active list unless the -neflag is also
        specified.
    
    - containerCentric : cc          (bool)          [create]
        Specifies that the same selection rules as apply to selection in the main
        viewport will also be applied to the select command. In particular, if the
        specified objects are members of a black-boxed container and are not published
        as nodes, Maya will not select them. Instead, their first parent valid for
        selection will be selected.
    
    - deselect : d                   (bool)          [create]
        Indicates that the specified items should be removed from the active list if
        they are on the active list.
    
    - hierarchy : hi                 (bool)          [create]
        Indicates that all children, grandchildren, ... of the specified dag objects
        should also be selected.
    
    - noExpand : ne                  (bool)          [create]
        Indicates that any set which is among the specified items should not be expanded
        to its list of members. This allows sets to be selected as opposed to the
        members of sets which is the default behaviour.
    
    - replace : r                    (bool)          [create]
        Indicates that the specified items should replace the existing items on the
        active list.
    
    - symmetry : sym                 (bool)          [create]
        Specifies that components should be selected symmetrically using the current
        symmetricModelling command settings. If symmetric modeling is not enabled then
        this flag has no effect.
    
    - symmetrySide : sys             (int)           [create]
        Indicates that components involved in the current symmetry object should be
        selected, according to the supplied parameter. Valid values for the parameter
        are: -1 : Select components in the unsymmetrical region. 0 : Select components
        on the symmetry seam. 1 : Select components on side 1. 2 : Select components on
        side 2. If symmetric modeling is not enabled then this flag has no effect. Note:
        currently only works for topological symmetry.
    
    - toggle : tgl                   (bool)          [create]
        Indicates that those items on the given list which are on the active list should
        be removed from the active list and those items on the given list which are not
        on the active list should be added to the active list.
    
    - visible : vis                  (bool)          [create]
        Indicates that of the specified items only those that are visible should be
        affected.                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.select`
    """
    pass


def listConnections(*args, **kwargs):
    """
    This command returns a list of all attributes/objects of a specified type that
    are connected to the given object(s). If no objects are specified then the
    command lists the connections on selected nodes.
    
    Modifications:
      - returns an empty list when the result is None
      - returns an empty list (with a warning) when the arg is an empty list, tuple,
            set, or frozenset, making it's behavior consistent with when None is
            passed, or no args and nothing is selected (would formerly raise a
            TypeError)
      - When 'connections' flag is True, (and 'plugs' is True) the attribute pairs are returned in a 2D-array::
    
            [['checker1.outColor', 'lambert1.color'], ['checker1.color1', 'fractal1.outColor']]
    
            Note that if 'plugs' is False (the default), for backward compatibility, the returned pairs are somewhat less intuitive attrs + nodes::
    
            [['checker1.outColor', 'lambert1'], ['checker1.color1', 'fractal1']]
    
      - added sourceFirst keyword arg. when sourceFirst is true and connections is also true,
            the paired list of plugs is returned in (source,destination) order instead of (thisnode,othernode) order.
            this puts the pairs in the order that disconnectAttr and connectAttr expect.
      - added ability to pass a list of types
    
    Returns
    -------
    List[Union[PyNode, Attribute, Tuple[PyNode, PyNode], Tuple[Attribute, Attribute]]]
    
    Flags:
    - connections : c                (bool)          [create]
        If true, return both attributes involved in the connection. The one on the
        specified object is given first.  Default false.
    
    - destination : d                (bool)          [create]
        Give the attributes/objects that are on the destinationside of connection to the
        given object.  Default true.
    
    - exactType : et                 (bool)          [create]
        When set to true, -t/type only considers node of this exact type. Otherwise,
        derived types are also taken into account.
    
    - plugs : p                      (bool)          [create]
        If true, return the connected attribute names; if false, return the connected
        object names only.  Default false;
    
    - shapes : sh                    (bool)          [create]
        Actually return the shape name instead of the transform when the shape is
        selected.  Default false.
    
    - skipConversionNodes : scn      (bool)          [create]
        If true, skip over unit conversion nodes and return the node connected to the
        conversion node on the other side.  Default false.
    
    - source : s                     (bool)          [create]
        Give the attributes/objects that are on the sourceside of connection to the
        given object.  Default true.
    
    - type : t                       (unicode)       [create]
        If specified, only take objects of a specified type.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.listConnections`
    """
    pass


def _pathFromMObj(mObj, fullPath='False'):
    """
    Return a unique path to an mObject
    """
    pass


def sets(*args, **kwargs):
    """
    This command is used to create a set, query some state of a set, or perform
    operations to update the membership of a set. A set is a logical grouping of an
    arbitrary collection of objects, attributes, or components of objects. Sets are
    dependency nodes. Connections from objects to a set define membership in the
    set. Sets are used throughout Maya in a multitude of ways. They are used to
    define an association of material properties to objects, to define an
    association of lights to objects, to define a bookmark or named collection of
    objects, to define a character, and to define the components to be deformed by
    some deformation operation. Sets can be connected to any number of partitions. A
    partition is a node which enforces mutual exclusivity amoung the sets in the
    partition. That is, if an object is in a set which is in a partition, that
    object cannot be a member of any other set that is in the partition. Without any
    flags, the setscommand will create a set with a default name of set#(where # is
    an integer). If no items are specified on the command line, the currently
    selected items are added to the set. The -em/empty flag can be used to create an
    empty set and not have the selected items added to the set. Sets can be created
    to have certain restrictions on membership. There can be renderablesets which
    only allow renderable objects (such as nurbs geometry or polymesh faces) to be
    members of the set. There can also be vertex (or control point), edit point,
    edge, or face sets which only allow those types of components to be members of a
    set. Note that for these sets, if an object with a valid type of component is to
    be added to a set, the components of the object are added to the set instead.
    Sets can have an associated color which is only of use when creating vertex
    sets. The color can be one of the eight user defined colors defined in the color
    preferences. This color can be used, for example to distinguish which vertices
    are being deformed by a particular deformation. Objects, components, or
    attributes can be added to a set using one of three flags. The -add/addElement
    flag will add the objects to a set as long as this won't break any mutual
    exclusivity constraints. If there are any items which can't be added, the
    command will fail. The -in/include flag will only add those items which can be
    added and warn of those which can't. The -fe/forceElement flag will add all the
    items to the set but will also remove any of those items that are in any other
    set which is in the same partition as the set. There are several operations on
    sets that can be performed with the setscommand. Membership can be queried.
    Tests for whether an item is in a set or whether two sets share the same item
    can be performed. Also, the union, intersection and difference of sets can be
    performed which returns a list of members of the sets which are a result of the
    operation.
    
    Modifications
      - resolved confusing syntax: operating set is always the first and only arg:
    
            >>> from pymel.core import *
            >>> f=newFile(f=1) #start clean
            >>>
            >>> shdr, sg = createSurfaceShader( 'blinn' )
            >>> shdr
            nt.Blinn(u'blinn1')
            >>> sg
            nt.ShadingEngine(u'blinn1SG')
            >>> s,h = polySphere()
            >>> s
            nt.Transform(u'pSphere1')
            >>> sets( sg, forceElement=s ) # add the sphere
            nt.ShadingEngine(u'blinn1SG')
            >>> sets( sg, q=1)  # check members
            [nt.Mesh(u'pSphereShape1')]
            >>> sets( sg, remove=s )
            nt.ShadingEngine(u'blinn1SG')
            >>> sets( sg, q=1)
            []
    
      - returns wrapped classes
    
        
    
    Flags:
    - addElement : add               (PyNode)        [edit]
        Adds the list of items to the given set.  If some of the items cannot be added
        to the set because they are in another set which is in the same partition as the
        set to edit, the command will fail.
    
    - afterFilters : af              (bool)          [edit]
        Default state is false. This flag is valid in edit mode only. This flag is for
        use on sets that are acted on by deformers such as sculpt, lattice, blendShape.
        The default edit mode is to edit the membership of the group acted on by the
        deformer. If you want to edit the group but not change the membership of the
        deformer, set the flag to true.
    
    - clear : cl                     (PyNode)        [edit]
        An operation which removes all items from the given set making the set empty.
    
    - color : co                     (int)           [create,query,edit]
        Defines the hilite color of the set. Must be a value in range [-1, 7] (one of
        the user defined colors).  -1 marks the color has being undefined and therefore
        not having any affect. Only the vertices of a vertex set will be displayed in
        this color.
    
    - copy : cp                      (PyNode)        [create]
        Copies the members of the given set to a new set. This flag is for use in
        creation mode only.
    
    - edges : eg                     (bool)          [create,query]
        Indicates the new set can contain edges only. This flag is for use in creation
        or query mode only. The default value is false.
    
    - editPoints : ep                (bool)          [create,query]
        Indicates the new set can contain editPoints only. This flag is for use in
        creation or query mode only. The default value is false.
    
    - empty : em                     (bool)          [create]
        Indicates that the set to be created should be empty. That is, it ignores any
        arguments identifying objects to be added to the set. This flag is only valid
        for operations that create a new set.
    
    - facets : fc                    (bool)          [create,query]
        Indicates the new set can contain facets only. This flag is for use in creation
        or query mode only. The default value is false.
    
    - flatten : fl                   (PyNode)        [edit]
        An operation that flattens the structure of the given set. That is, any sets
        contained by the given set will be replaced by its members so that the set no
        longer contains other sets but contains the other sets' members.
    
    - forceElement : fe              (PyNode)        [edit]
        For use in edit mode only. Forces addition of the items to the set. If the items
        are in another set which is in the same partition as the given set, the items
        will be removed from the other set in order to keep the sets in the partition
        mutually exclusive with respect to membership.
    
    - include : include              (PyNode)        [edit]
        Adds the list of items to the given set.  If some of the items cannot be added
        to the set, a warning will be issued. This is a less strict version of the
        -add/addElement operation.
    
    - intersection : int             (PyNode)        [create]
        An operation that returns a list of items which are members of all the sets in
        the list.
    
    - isIntersecting : ii            (PyNode)        [create]
        An operation which tests whether the sets in the list have common members.
    
    - isMember : im                  (PyNode)        [create]
        An operation which tests whether all the given items are members of the given
        set.
    
    - layer : l                      (bool)          [create]
        OBSOLETE. DO NOT USE.
    
    - name : n                       (unicode)       [create]
        Assigns string as the name for a new set. This flag is only valid for operations
        that create a new set.
    
    - noSurfaceShader : nss          (bool)          [create]
        If set is renderable, do not connect it to the default surface shader.  Flag has
        no meaning or effect for non renderable sets. This flag is for use in creation
        mode only. The default value is false.
    
    - noWarnings : nw                (bool)          [create]
        Indicates that warning messages should not be reported such as when trying to
        add an invalid item to a set. (used by UI)
    
    - nodesOnly : no                 (bool)          [query]
        This flag is usable with the -q/query flag but is ignored if used with another
        queryable flags. This flag modifies the results of the set membership query such
        that when there are attributes (e.g. sphere1.tx) or components of nodes included
        in the set, only the nodes will be listed. Each node will only be listed once,
        even if more than one attribute or component of the node exists in the set.
    
    - remove : rm                    (PyNode)        [edit]
        Removes the list of items from the given set.
    
    - renderable : r                 (bool)          [create,query]
        This flag indicates that a special type of set should be created. This type of
        set (shadingEngine as opposed to objectSet) has certain restrictions on its
        membership in that it can only contain renderable elements such as lights and
        geometry. These sets are referred to as shading groups and are automatically
        connected to the renderPartitionnode when created (to ensure mutual exclusivity
        of the set's members with the other sets in the partition). This flag is for use
        in creation or query mode only. The default value is false which means a normal
        set is created.
    
    - size : s                       (bool)          [query]
        Use the size flag to query the length of the set.
    
    - split : sp                     (PyNode)        [create]
        Produces a new set with the list of items and removes each item in the list of
        items from the given set.
    
    - subtract : sub                 (PyNode)        [create]
        An operation between two sets which returns the members of the first set that
        are not in the second set.
    
    - text : t                       (unicode)       [create,query,edit]
        Defines an annotation string to be stored with the set.
    
    - union : un                     (PyNode)        [create]
        An operation that returns a list of all the members of all sets listed.
    
    - vertices : v                   (bool)          [create,query]
        Indicates the new set can contain vertices only. This flag is for use in
        creation or query mode only. The default value is false.                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.sets`
    """
    pass


def _about(*args, **kwargs): pass


def selectKey(*args, **kwargs):
    """
    This command operates on a keyset.  A keyset is defined as a group of keys
    within a specified time range on one or more animation curves. The animation
    curves comprising a keyset depend on the value of the -animationflag:
    keysOrObjects: Any active keys, when no target objects or -attribute flags
    appear on the command line, orAll animation curves connected to all keyframable
    attributes of objects specified as the command line's targetList, when there are
    no active keys.keys: Only act on active keys or tangents. If there are no active
    keys or tangents, don't do anything. objects: Only act on specified objects.  If
    there are no objects specified, don't do anything. Note that the -animationflag
    can be used to override the curves uniquely identified by the multi-use
    -attributeflag, which takes an argument of the form attributeName, such as
    translateX. Keys on animation curves are identified by either their time values
    or their indices.  Times and indices can be given individually or as part of a
    list or range (see Examples). This command places keyframes and/or keyframe
    tangents on the active list.
    
    Flags:
    - addTo : add                    (bool)          [create]
        Add to the current selection of keyframes/tangents
    
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - clear : cl                     (bool)          [create]
        Remove all keyframes and tangents from the active list.
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
    - inTangent : it                 (bool)          [create]
        Select in-tangents of keyframes in the specified time range
    
    - includeUpperBound : iub        (bool)          [create]
        When the -t/time or -f/float flags represent a range of keys, this flag
        determines whether the keys at the upper bound of the range are included in the
        keyset. Default value: true.  This flag is only valid when the argument to the
        -t/time flag is a time range with a lower and upper bound.  (When used with the
        pasteKeycommand, this flag refers only to the time range of the target curve
        that is replaced, when using options such as replace,fitReplace,or
        scaleReplace.This flag has no effect on the curve pasted from the clipboard.)
    
    - index : index                  (int)           [create]
        index of a key on an animCurve
    
    - keyframe : k                   (bool)          [create]
        select only keyframes (cannot be combined with -in/-out)
    
    - outTangent : ot                (bool)          [create]
        Select out-tangents of keyframes in the specified time range
    
    - remove : rm                    (bool)          [create]
        Remove from the current selection of keyframes/tangents
    
    - replace : r                    (bool)          [create]
        Replace the current selection of keyframes/tangents
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - toggle : tgl                   (bool)          [create]
        Toggle the picked state of the specified keyset
    
    - unsnappedKeys : uk             (float)         [create]
        Select only keys that have times that are not a multiple of the specified
        numeric value.                  Flag can have multiple arguments, passed either
        as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.selectKey`
    """
    pass


def ls(*args, **kwargs):
    """
    The lscommand returns the names (and optionally the type names) of objects in
    the scene. The most common use of lsis to filter or match objects based on their
    name (using wildcards) or based on their type. By default lswill match any
    object in the scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag. If type names are
    requested, using the showType flag, they will be interleaved with object names
    so the result will be pairs of object, typevalues. Internal nodes (for example
    itemFilter nodes) are typically filtered so that only scene objects are
    returned. However, using a wildcard will cause all the nodes matching the wild
    card to show up, including internal nodes.  For example, ls \*will list all
    nodes whether internal or not. Use the syntax ::to denote a recursive namespace
    search when listing nodes. For example, ls ::pSphere1would match objects named
    pSphere1in any namespace, at any depth. ls ns::\*would match any node in
    namespace nsor children namespaces. When Maya is in relativeNames mode, the
    lscommand will return names relativeto the current namespace and ls \*will list
    from the the current namespace. For more details, please refer to the
    -relativeNamesflag of the namespacecommand. The command may also be passed node
    UUIDs instead of names/paths, and can return UUIDs instead of names via the
    -uuid flag.
    
    Modifications:
      - Returns PyNode objects, not "names" - all flags which do nothing but modify
        the string name of returned objects are ignored (ie, 'long'); note that
        the 'allPaths' flag DOES have an effect, as PyNode objects are aware of
        their dag paths (ie, two different instances of the same object will result
        in two unique PyNodes)
      - Added new keyword: 'editable' - this will return the inverse set of the readOnly flag. i.e. non-read-only nodes
      - Added new keyword: 'regex' - pass a valid regular expression string, compiled regex pattern, or list thereof.
    
            >>> group('top')
            nt.Transform(u'group1')
            >>> duplicate('group1')
            [nt.Transform(u'group2')]
            >>> group('group2')
            nt.Transform(u'group3')
            >>> ls(regex='group\d+\|top') # don't forget to escape pipes `|`
            [nt.Transform(u'group1|top'), nt.Transform(u'group2|top')]
            >>> ls(regex='group\d+\|top.*')
            [nt.Transform(u'group1|top'), nt.Camera(u'group1|top|topShape'), nt.Transform(u'group2|top'), nt.Camera(u'group2|top|topShape')]
            >>> ls(regex='group\d+\|top.*', cameras=1)
            [nt.Camera(u'group2|top|topShape'), nt.Camera(u'group1|top|topShape')]
            >>> ls(regex='\|group\d+\|top.*', cameras=1) # add a leading pipe to search for full path
            [nt.Camera(u'group1|top|topShape')]
    
        The regular expression will be used to search the full DAG path, starting from the right, in a similar fashion to how globs currently work.
        Technically speaking, your regular expression string is used like this::
    
            re.search( '(\||^)' + yourRegexStr + '$', fullNodePath )
    
    Returns
    -------
    List[PyNode]
    
    Flags:
    - absoluteName : an              (bool)          [create]
        This flag can be used in conjunction with the showNamespace flag to specify that
        the namespace(s) returned by the command be in absolute namespace format. The
        absolute name of the namespace is a full namespace path, starting from the root
        namespace :and including all parent namespaces.  For example :ns:ballis an
        absolute namespace name while ns:ballis not. The absolute namespace name is
        invariant and is not affected by the current namespace or relative namespace
        modes.
    
    - allPaths : ap                  (bool)          [create]
        List all paths to nodes in DAG. This flag only works if -dagis also specified or
        if an object name is supplied.
    
    - assemblies : assemblies        (bool)          [create]
        List top level transform Dag objects
    
    - cameras : ca                   (bool)          [create]
        List camera shapes.
    
    - containerType : ct             (unicode)       [create]
        List containers with the specified user-defined type. This flag cannot be used
        in conjunction with the type or exactType flag.
    
    - containers : con               (bool)          [create]
        List containers. Includes both standard containers as well as other types of
        containers such as dagContainers.
    
    - dagObjects : dag               (bool)          [create]
        List Dag objects of any type. If object name arguments are passed to the command
        then this flag will list all Dag objects below the specified object(s).
    
    - defaultNodes : dn              (bool)          [create]
        Returns default nodes. A default node is one that Maya creates automatically and
        does not get saved out with the scene, although some of its attribute values
        may.
    
    - dependencyNodes : dep          (bool)          [create]
        List dependency nodes. (including Dag objects)
    
    - exactType : et                 (unicode)       [create]
        List all objects of the specified type, but notobjects that are descendents of
        that type. This flag can appear multiple times on the command line. Note: the
        type passed to this flag is the same type name returned from the showType flag.
        This flag cannot be used in conjunction with the type or excludeType flag.
    
    - excludeType : ext              (unicode)       [create]
        List all objects that are not of the specified type. This flag can appear
        multiple times on the command line. Note: the type passed to this flag is the
        same type name returned from the showType flag. This flag cannot be used in
        conjunction with the type or exactType flag.
    
    - flatten : fl                   (bool)          [create]
        Flattens the returned list of objects so that each component is identified
        individually.
    
    - geometry : g                   (bool)          [create]
        List geometric Dag objects.
    
    - ghost : gh                     (bool)          [create]
        List ghosting objects.
    
    - head : hd                      (int)           [create]
        This flag  specifies the maximum number of elements to be returned from the
        beginning of the list of items. Note: each type flag will return at most this
        many items so if multiple type flags are specified then the number of items
        returned can be greater than this amount.
    
    - hilite : hl                    (bool)          [create]
        List objects that are currently hilited for component selection.
    
    - intermediateObjects : io       (bool)          [create]
        List only intermediate dag nodes.
    
    - invisible : iv                 (bool)          [create]
        List only invisible dag nodes.
    
    - leaf : lf                      (bool)          [create]
        List all leaf nodes in Dag. This flag is a modifier and must be used in
        conjunction with the -dag flag.
    
    - lights : lt                    (bool)          [create]
        List light shapes.
    
    - live : lv                      (bool)          [create]
        List objects that are currently live.
    
    - lockedNodes : ln               (bool)          [create]
        Returns locked nodes, which cannot be deleted or renamed. However, their status
        may change.
    
    - long : l                       (bool)          [create]
        Return full path names for Dag objects. By default the shortest unique name is
        returned.
    
    - materials : mat                (bool)          [create]
        List materials or shading groups.
    
    - modified : mod                 (bool)          [create]
        When this flag is set, only nodes modified since the last save will be returned.
    
    - noIntermediate : ni            (bool)          [create]
        List only non intermediate dag nodes.
    
    - nodeTypes : nt                 (bool)          [create]
        Lists all registered node types.
    
    - objectsOnly : o                (bool)          [create]
        When this flag is set only object names will be returned and
        components/attributes will be ignored.
    
    - orderedSelection : os          (bool)          [create]
        List objects and components that are currently selected in their order of
        selection.  This flag depends on the value of the -tso/trackSelectionOrder flag
        of the selectPref command.  If that flag is not enabled than this flag will
        return the same thing as the -sl/selection flag would.
    
    - partitions : pr                (bool)          [create]
        List partitions.
    
    - persistentNodes : pn           (bool)          [create]
        Returns persistent nodes, which are nodes that stay in the Maya session after a
        file new. These are a special class of default nodes that do not get reset on
        file new. Ex: itemFilter and selectionListOperator nodes.
    
    - planes : pl                    (bool)          [create]
        List construction plane shapes.
    
    - preSelectHilite : psh          (bool)          [create]
        List components that are currently hilited for pre-selection.
    
    - readOnly : ro                  (bool)          [create]
        Returns referenced nodes. Referenced nodes are read only. NOTE: Obsolete. Please
        use -referencedNodes.
    
    - recursive : r                  (bool)          [create]
        When set to true, this command will look for name matches in all namespaces.
        When set to false, this command will only look for matches in namespaces that
        are requested (e.g. by specifying a name containing the ':'... ns1:pSphere1).
    
    - referencedNodes : rn           (bool)          [create]
        Returns referenced nodes. Referenced nodes are read only.
    
    - references : rf                (bool)          [create]
        List references associated with files. Excludes special reference nodes such as
        the sharedReferenceNode and unknown reference nodes.
    
    - renderGlobals : rg             (bool)          [create]
        List render globals.
    
    - renderQualities : rq           (bool)          [create]
        List named render qualities.
    
    - renderResolutions : rr         (bool)          [create]
        List render resolutions.
    
    - renderSetups : rs              (bool)          [create]
        Alias for -renderGlobals.
    
    - selection : sl                 (bool)          [create]
        List objects that are currently selected.
    
    - sets : set                     (bool)          [create]
        List sets.
    
    - shapes : s                     (bool)          [create]
        List shape objects.
    
    - shortNames : sn                (bool)          [create]
        Return short attribute names. By default long attribute names are returned.
    
    - showNamespace : sns            (bool)          [create]
        Show the namespace of each object after the object name. This flag cannot be
        used in conjunction with the showType flag.
    
    - showType : st                  (bool)          [create]
        List the type of each object after its name.
    
    - tail : tl                      (int)           [create]
        This flag specifies the maximum number of elements to be returned from the end
        of the list of items. Note: each    type flag will return at most this many
        items so if multiple type flags are specified then the number of items returned
        can be greater than this amount
    
    - templated : tm                 (bool)          [create]
        List only templated dag nodes.
    
    - textures : tex                 (bool)          [create]
        List textures.
    
    - transforms : tr                (bool)          [create]
        List transform objects.
    
    - type : typ                     (unicode)       [create]
        List all objects of the specified type. This flag can appear multiple times on
        the command line. Note: the type passed to this flag is the same type name
        returned from the showType flag. Note: some selection items in Maya do not have
        a specific object/data type associated with them and will return untypedwhen
        listed with this flag. This flag cannot be used in conjunction with the
        exactType or excludeType flag.
    
    - undeletable : ud               (bool)          [create]
        Returns nodes that cannot be deleted (which includes locked nodes). These nodes
        also cannot be renamed.
    
    - untemplated : ut               (bool)          [create]
        List only un-templated dag nodes.
    
    - uuid : uid                     (bool)          [create]
        Return node UUIDs instead of names. Note that there are no UUID paths- combining
        this flag with e.g. the -long flag will not result in a path formed of node
        UUIDs.
    
    - visible : v                    (bool)          [create]
        List only visible dag nodes.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.ls`
    """
    pass


def getAttr(attr, default='None', **kwargs):
    """
    This command returns the value of the named object's attribute. UI units are
    used where applicable. Currently, the types of attributes that can be displayed
    are: numeric attributesstring attributesmatrix attributesnumeric compound
    attributes (whose children are all numeric)vector array attributesdouble array
    attributesint32 array attributespoint array attributesdata component list
    attributesOther data types cannot be retrieved. No result is returned if the
    attribute contains no data.
    
    Maya Bug Fix:
      - maya pointlessly returned vector results as a tuple wrapped in a list ( ex.  '[(1,2,3)]' ). This command unpacks the vector for you.
    
    Modifications:
      - casts double3 datatypes to `Vector`
      - casts matrix datatypes to `Matrix`
      - casts vectorArrays from a flat array of floats to an array of Vectors
      - when getting a multi-attr, maya would raise an error, but pymel will return a list of values for the multi-attr
      - added a default argument. if the attribute does not exist and this argument is not None, this default value will be returned
      - added support for getting message attributes
    
    Flags:
    - asString : asString            (bool)          [create]
        This flag is only valid for enum attributes. It allows you to get the attribute
        values as strings instead of integer values. Note that the returned string value
        is dependent on the UI language Maya is running in (about -uiLanguage).
    
    - caching : ca                   (bool)          [create]
        Returns whether the attribute is set to be cached internally
    
    - channelBox : cb                (bool)          [create]
        Returns whether the attribute is set to show in the channelBox. Keyable
        attributes also show in the channel box.
    
    - expandEnvironmentVariables : x (bool)          [create]
        Expand any environment variable and (tilde characters on UNIX) found in string
        attributes which are returned.
    
    - keyable : k                    (bool)          [create]
        Returns the keyable state of the attribute.
    
    - lock : l                       (bool)          [create]
        Returns the lock state of the attribute.
    
    - multiIndices : mi              (bool)          [create]
        If the attribute is a multi, this will return a list containing all of the valid
        indices for the attribute.
    
    - settable : se                  (bool)          [create]
        Returns 1 if this attribute is currently settable by setAttr, 0 otherwise. An
        attribute is settable if it's not locked and either not connected, or has only
        keyframed animation.
    
    - silent : sl                    (bool)          [create]
        When evaluating an attribute that is not a numeric or string value, suppress the
        error message saying that the data cannot be displayed. The attribute will be
        evaluated even though its data cannot be displayed. This flag does not suppress
        all error messages, only those that are benign.
    
    - size : s                       (bool)          [create]
        Returns the size of a multi-attribute array.  Returns 1 if non-multi.
    
    - time : t                       (time)          [create]
        Evaluate the attribute at the given time instead of the current time.
    
    - type : typ                     (bool)          [create]
        Returns the type of data currently in the attribute. Attributes of simple types
        such as strings and numerics always contain data, but attributes of complex
        types (arrays, meshes, etc) may contain no data if none has ever been assigned
        to them. When this happens the command will return with no result: not an empty
        string, but no result at all. Attempting to directly compare this non-result to
        another value or use it in an expression will result in an error, but you can
        assign it to a variable in which case the variable will be set to the default
        value for its type (e.g. an empty string for a string variable, zero for an
        integer variable, an empty array for an array variable). So to be safe when
        using this flag, always assign its result to a string variable, never try to use
        it directly.                   Flag can have multiple arguments, passed either
        as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.getAttr`
    """
    pass


def strDeprecateDecorator(func):
    """
    #@decorator
    """
    pass


def duplicate(*args, **kwargs):
    """
    This command duplicates the given objects. If no objects are given, then the
    selected list is duplicated. The smart transform feature allows duplicate to
    transform newly duplicated objects based on previous transformations between
    duplications. Example: Duplicate an object and move it to a new location.
    Duplicate it again with the smart duplicate flag. It should have moved once
    again the distance you had previously moved it. Note: changing the selected list
    between smart duplications will cause the transform information to be deleted
    The upstream Nodes option forces duplication of all upstream nodes leading upto
    the selected objects.. Upstream nodes are defined as all nodes feeding into
    selected nodes. During traversal of Dependency graph, if another dagObject is
    encountered, then that node and all it's parent transforms are also duplicated.
    The inputConnections option forces the duplication of input connections to the
    nodes that are to be duplicated. This is very useful especially in cases where
    two nodes that are connected to each other are specified as nodes to be
    duplicated. In that situation, the connection between the nodes is also
    duplicated. See also:instance
    
    Modifications:
      - new option: addShape
            If addShape evaluates to True, then all arguments fed in must be shapes, and each will be duplicated and added under
            the existing parent transform, instead of duplicating the parent transform.
            The following arguments are incompatible with addShape, and will raise a ValueError if enabled along with addShape:
                renameChildren (rc), instanceLeaf (ilf), parentOnly (po), smartTransform (st)
      - returns wrapped classes
      - returnRootsOnly is forced on for dag objects. This is because the duplicate command does not use full paths when returning
        the names of duplicated objects and will fail if the name is not unique.
    
    Returns
    -------
    List[nodetypes.DependNode]
    
    Flags:
    - inputConnections : ic          (bool)          [create]
        Input connections to the node to be duplicated, are also duplicated. This would
        result in a fan-out scenario as the nodes at the input side are not duplicated
        (unlike the -un option).
    
    - instanceLeaf : ilf             (bool)          [create]
        instead of duplicating leaf DAG nodes, instance them.
    
    - name : n                       (unicode)       [create]
        name to give duplicated object(s)
    
    - parentOnly : po                (bool)          [create]
        Duplicate only the specified DAG node and not any of its children.
    
    - renameChildren : rc            (bool)          [create]
        rename the child nodes of the hierarchy, to make them unique.
    
    - returnRootsOnly : rr           (bool)          [create]
        return only the root nodes of the new hierarchy. When used with upstreamNodes
        flag, the upstream nodes will be omitted in the result.  This flag controls only
        what is returned in the output string[], and it does NOT change the behaviour of
        the duplicate command.
    
    - smartTransform : st            (bool)          [create]
        remembers last transformation and applies it to duplicated object(s)
    
    - transformsOnly : to            (bool)          [create]
        Duplicate only transform nodes and not any shapes.
    
    - upstreamNodes : un             (bool)          [create]
        the upstream nodes leading upto the selected nodes (along with their
        connections) are also duplicated.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.duplicate`
    """
    pass


def paramDimension(*args, **kwargs):
    """
    This command is used to create a param dimension to display the parameter value
    of a curve/surface at a specified point on the curve/surface.
    
    
    Derived from mel command `maya.cmds.paramDimension`
    """
    pass


def setAttr(attr, *args, **kwargs):
    """
    Sets the value of a dependency node attribute.  No value for the the attribute
    is needed when the -l/-k/-s flags are used. The -type flag is only required when
    setting a non-numeric attribute. The following chart outlines the syntax of
    setAttr for non-numeric data types: TYPEbelow means any number of values of type
    TYPE, separated by a space[TYPE]means that the value of type TYPEis
    optionalA|Bmeans that either of Aor Bmay appearIn order to run its examples,
    first execute these commands to create the sample attribute types:sphere -n
    node; addAttr -ln short2Attr -at short2; addAttr -ln short2a -p short2Attr -at
    short; addAttr -ln short2b -p short2Attr -at short; addAttr -ln short3Attr -at
    short3; addAttr -ln short3a -p short3Attr -at short; addAttr -ln short3b -p
    short3Attr -at short; addAttr -ln short3c -p short3Attr -at short; addAttr -ln
    long2Attr -at long2; addAttr -ln long2a -p long2Attr -at long; addAttr -ln
    long2b -p long2Attr -at long; addAttr -ln long3Attr -at long3; addAttr -ln
    long3a -p long3Attr -at long; addAttr -ln long3b -p long3Attr -at long; addAttr
    -ln long3c -p long3Attr -at long; addAttr -ln float2Attr -at float2; addAttr -ln
    float2a -p float2Attr -at float; addAttr -ln float2b -p float2Attr -at float;
    addAttr -ln float3Attr -at float3; addAttr -ln float3a -p float3Attr -at float;
    addAttr -ln float3b -p float3Attr -at float; addAttr -ln float3c -p float3Attr
    -at float; addAttr -ln double2Attr -at double2; addAttr -ln double2a -p
    double2Attr -at double; addAttr -ln double2b -p double2Attr -at double; addAttr
    -ln double3Attr -at double3; addAttr -ln double3a -p double3Attr -at double;
    addAttr -ln double3b -p double3Attr -at double; addAttr -ln double3c -p
    double3Attr -at double; addAttr -ln int32ArrayAttr -dt Int32Array; addAttr -ln
    doubleArrayAttr -dt doubleArray; addAttr -ln pointArrayAttr -dt pointArray;
    addAttr -ln vectorArrayAttr -dt vectorArray; addAttr -ln stringArrayAttr -dt
    stringArray; addAttr -ln stringAttr -dt string; addAttr -ln matrixAttr -dt
    matrix; addAttr -ln sphereAttr -dt sphere; addAttr -ln coneAttr -dt cone;
    addAttr -ln meshAttr -dt mesh; addAttr -ln latticeAttr -dt lattice; addAttr -ln
    spectrumRGBAttr -dt spectrumRGB; addAttr -ln reflectanceRGBAttr -dt
    reflectanceRGB; addAttr -ln componentListAttr -dt componentList; addAttr -ln
    attrAliasAttr -dt attributeAlias; addAttr -ln curveAttr -dt nurbsCurve; addAttr
    -ln surfaceAttr -dt nurbsSurface; addAttr -ln trimFaceAttr -dt nurbsTrimface;
    addAttr -ln polyFaceAttr -dt polyFaces; -type short2Array of two short
    integersValue Syntaxshort shortValue Meaningvalue1 value2Mel ExamplesetAttr
    node.short2Attr -type short2 1 2;Python
    Examplecmds.setAttr('node.short2Attr',1,2,type='short2')-type short3Array of
    three short integersValue Syntaxshort short shortValue Meaningvalue1 value2
    value3Mel ExamplesetAttr node.short3Attr -type short3 1 2 3;Python
    Examplecmds.setAttr('node.short3Attr',1,2,3,type='short3')-type long2Array of
    two long integersValue Syntaxlong longValue Meaningvalue1 value2Mel
    ExamplesetAttr node.long2Attr -type long2 1000000 2000000;Python
    Examplecmds.setAttr('node.long2Attr',1000000,2000000,type='long2')-type
    long3Array of three long integersValue Syntaxlong long longValue Meaningvalue1
    value2 value3Mel ExamplesetAttr node.long3Attr -type long3 1000000 2000000
    3000000;Python
    Examplecmds.setAttr('node.long3Attr',1000000,2000000,3000000,type='long3')-type
    Int32ArrayVariable length array of long integersValue SyntaxValue MeaningMel
    ExamplesetAttr node.int32ArrayAttr -type Int32Array 2 12 75;Python
    Examplecmds.setAttr('node.int32ArrayAttr',[2,12,75],type='Int32Array')-type
    float2Array of two floatsValue Syntaxfloat floatValue Meaningvalue1 value2Mel
    ExamplesetAttr node.float2Attr -type float2 1.1 2.2;Python
    Examplecmds.setAttr('node.float2Attr',1.1,2.2,type='float2')-type float3Array of
    three floatsValue Syntaxfloat float floatValue Meaningvalue1 value2 value3Mel
    ExamplesetAttr node.float3Attr -type float3 1.1 2.2 3.3;Python
    Examplecmds.setAttr('node.float3Attr',1.1,2.2,3.3,type='float3')-type
    double2Array of two doublesValue Syntaxdouble doubleValue Meaningvalue1
    value2Mel ExamplesetAttr node.double2Attr -type double2 1.1 2.2;Python
    Examplecmds.setAttr('node.double2Attr',1.1,2.2,type='double2')-type double3Array
    of three doublesValue Syntaxdouble double doubleValue Meaningvalue1 value2
    value3Mel ExamplesetAttr node.double3Attr -type double3 1.1 2.2 3.3;Python
    Examplecmds.setAttr('node.double3Attr',1.1,2.2,3.3,type='double3')-type
    doubleArrayVariable length array of doublesValue SyntaxValue MeaningMel
    ExamplesetAttr node.doubleArrayAttr -type doubleArray 2 3.14159 2.782;Python
    Examplecmds.setAttr( node.doubleArrayAttr, (2, 3.14159, 2.782,),
    type=doubleArray)-type matrix4x4 matrix of doublesValue Syntaxdouble double
    double doubledouble double double doubledouble double double doubledouble double
    double doubleValue Meaningrow1col1 row1col2 row1col3 row1col4row2col1 row2col2
    row2col3 row2col4row3col1 row3col2 row3col3 row3col4row4col1 row4col2 row4col3
    row4col4Alternate Syntaxstring double double doubledouble double
    doubleintegerdouble double doubledouble double doubledouble double doubledouble
    double doubledouble double doubledouble double doubledouble double double
    doubledouble double double doubledouble double doublebooleanAlternate
    MeaningxformscaleX scaleY scaleZrotateX rotateY rotateZrotationOrder (0=XYZ,
    1=YZX, 2=ZXY, 3=XZY, 4=YXZ, 5=ZYX)translateX translateY translateZshearXY
    shearXZ shearYZscalePivotX scalePivotY scalePivotZscaleTranslationX
    scaleTranslationY scaleTranslationZrotatePivotX rotatePivotY
    rotatePivotZrotateTranslationX rotateTranslationY
    rotateTranslationZrotateOrientW rotateOrientX rotateOrientY
    rotateOrientZjointOrientW jointOrientX jointOrientY
    jointOrientZinverseParentScaleX inverseParentScaleY
    inverseParentScaleZcompensateForParentScale Mel ExamplesetAttr node.matrixAttr
    -type matrix1 0 0 0 0 1 0 0 0 0 1 0 2 3 4 1;setAttr node.matrixAttr -type
    matrixxform1 1 1 0 0 0 0 2 3 4 0 0 00 0 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1 0 1 1 1
    0 false;Python Examplecmds.setAttr('node.matrixAttr',(1,0,0,0,0,1,0,0,0,0,1,0,2,
    3,4,1),type='matrix')cmds.setAttr('node.matrixAttr','xform',(1,1,1),(0,0,0),0,(2
    ,3,4),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,1,1),(0,0,1,0),(1,0,1,0),(1,2,3),False,
    type=matrix)-type pointArrayVariable length array of pointsValue SyntaxValue
    MeaningMel ExamplesetAttr node.pointArrayAttr -type pointArray 2 1 1 1 1 2 2 2
    1;Python Examplecmds.setAttr('node.pointArrayAttr',2,(1,1,1,1),(2,2,2,1),type='p
    ointArray')-type vectorArrayVariable length array of vectorsValue SyntaxValue
    MeaningMel ExamplesetAttr node.vectorArrayAttr -type vectorArray 2 1 1 1 2 2
    2;Python Examplecmds.setAttr('node.vectorArrayAttr',2,(1,1,1),(2,2,2),type='vect
    orArray')-type stringCharacter stringValue SyntaxstringValue
    MeaningcharacterStringValueMel ExamplesetAttr node.stringAttr -type
    stringblarg;Python Examplecmds.setAttr('node.stringAttr',blarg,type=string)-type
    stringArrayVariable length array of stringsValue SyntaxValue MeaningMel
    ExamplesetAttr node.stringArrayAttr -type stringArray 3 abc;Python
    Examplecmds.setAttr('node.stringArrayAttr',3,a,b,c,type='stringArray')-type
    sphereSphere dataValue SyntaxdoubleValue MeaningsphereRadiusExamplesetAttr
    node.sphereAttr -type sphere 5.0;-type coneCone dataValue Syntaxdouble
    doubleValue MeaningconeAngle coneCapMel ExamplesetAttr node.coneAttr -type cone
    45.0 5.0;Python Examplecmds.setAttr('node.coneAttr',45.0,5.0,type='cone')-type
    reflectanceRGBReflectance dataValue Syntaxdouble double doubleValue
    MeaningredReflect greenReflect blueReflectMel ExamplesetAttr
    node.reflectanceRGBAttr -type reflectanceRGB 0.5 0.5 0.1;Python Examplecmds.setA
    ttr('node.reflectanceRGBAttr',0.5,0.5,0.1,type='reflectanceRGB')-type
    spectrumRGBSpectrum dataValue Syntaxdouble double doubleValue MeaningredSpectrum
    greenSpectrum blueSpectrumMel ExamplesetAttr node.spectrumRGBAttr -type
    spectrumRGB 0.5 0.5 0.1;Python
    Examplecmds.setAttr('node.spectrumRGBAttr',0.5,0.5,0.1,type='spectrumRGB')-type
    componentListVariable length array of componentsValue SyntaxValue MeaningMel
    ExamplesetAttr node.componentListAttr -type componentList 3 cv[1] cv[12]
    cv[3];Python Examplecmds.setAttr('node.componentListAttr',3,'cv[1]','cv[12]','cv
    [3]',type='componentList')-type attributeAliasString alias dataValue
    Syntaxstring stringValue MeaningnewAlias currentNameMel ExamplesetAttr
    node.attrAliasAttr -type attributeAliasGoUp, translateY, GoLeft,
    translateX;Python Examplecmds.setAttr('node.attrAliasAttr',(GoUp,
    translateY,GoLeft, translateX),type='attributeAlias')-type nurbsCurveNURBS curve
    dataValue SyntaxValue MeaningMel Example// degree is the degree of the
    curve(range 1-7)// spans is the number of spans // form is open (0), closed (1),
    periodic (2)// dimension is 2 or 3, depending on the dimension of the curve//
    isRational is true if the curve CVs contain a rational component // knotCount is
    the size of the knot list//  knotValue is a single entry in the knot list//
    cvCount is the number of CVs in the curve//  xCVValue,yCVValue,[zCVValue]
    [wCVValue] is a single CV.//  zCVValue is only present when dimension is 3.//
    wCVValue is only present when isRational is true.//setAttr node.curveAttr -type
    nurbsCurve 3 1 0 no 36 0 0 0 1 1 14 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0;-type
    nurbsSurfaceNURBS surface dataValue Syntaxint int int int bool Value
    MeaninguDegree vDegree uForm vForm isRationalTRIM|NOTRIMExample// uDegree is
    degree of the surface in U direction (range 1-7)// vDegree is degree of the
    surface in V direction (range 1-7)// uForm is open (0), closed (1), periodic (2)
    in U direction// vForm is open (0), closed (1), periodic (2) in V direction//
    isRational is true if the surface CVs contain a rational component// uKnotCount
    is the size of the U knot list//  uKnotValue is a single entry in the U knot
    list// vKnotCount is the size of the V knot list//  vKnotValue is a single entry
    in the V knot list// If TRIMis specified then additional trim information is
    expected// If NOTRIMis specified then the surface is not trimmed// cvCount is
    the number of CVs in the surface//  xCVValue,yCVValue,zCVValue [wCVValue]is a
    single CV.//  zCVValue is only present when dimension is 3.//  wCVValue is only
    present when isRational is true//setAttr node.surfaceAttr -type nurbsSurface 3 3
    0 0 no 6 0 0 0 1 1 16 0 0 0 1 1 116 -2 3 0 -2 1 0 -2 -1 0 -2 -3 0-1 3 0 -1 1 0
    -1 -1 0 -1 -3 01 3 0 1 1 0 1 -1 0 1 -3 03 3 0 3 1 0 3 -1 0 3 -3 0;-type
    nurbsTrimfaceNURBS trim face dataValue SyntaxValue MeaningExample// flipNormal
    if true turns the surface inside out// boundaryCount: number of boundaries//
    boundaryType: // tedgeCountOnBoundary    : number of edges in a boundary//
    splineCountOnEdge    : number of splines in an edge in// edgeTolerance        :
    tolerance used to build the 3d edge// isEdgeReversed        : if true, the edge
    is backwards// geometricContinuity    : if true, the edge is tangent
    continuous// splineCountOnPedge    : number of splines in a 2d edge// isMonotone
    : if true, curvature is monotone// pedgeTolerance        : tolerance for the 2d
    edge//-type polyFacesPolygon face dataValue SyntaxfhmfmhmumcValue
    MeaningfhmfmhmumcExample// This data type (polyFace) is meant to be used in file
    I/O// after setAttrs have been written out for vertex position// arrays, edge
    connectivity arrays (with corresponding start// and end vertex descriptions),
    texture coordinate arrays and// color arrays.  The reason is that this data type
    references// all of its data through ids created by the former types.////
    fspecifies the ids of the edges making up a face -//     negative value if the
    edge is reversed in the face// hspecifies the ids of the edges making up a hole
    -//     negative value if the edge is reversed in the face// mfspecifies the ids
    of texture coordinates (uvs) for a face.//     This data type is obsolete as of
    version 3.0. It is replaced by mu.// mhspecifies the ids of texture coordinates
    (uvs) for a hole//     This data type is obsolete as of version 3.0. It is
    replaced by mu.// muThe  first argument refers to the uv set. This is a zero-
    based//     integer number. The second argument refers to the number of vertices
    (n)//     on the face which have valid uv values. The last n values are the uv//
    ids of the texture coordinates (uvs) for the face. These indices//     are what
    used to be represented by the mfand mhspecification.//     There may be more
    than one muspecification, one for each unique uv set.// mcspecifies the color
    index values for a face. The first argument//     is color index. The second
    argument is the number of color ids to follow.//     Rest of the arguments are
    color ids for the face.//setAttr node.polyFaceAttr -type polyFaces f3 1 2 3 mc0
    4 0 1 2 3;-type meshPolygonal meshValue SyntaxValue
    Meaningvvn[vtesmooth|hard]Example// vspecifies the vertices of the polygonal
    mesh// vnspecifies the normal of each vertex// vtis optional and specifies a U,V
    texture coordinate for each vertex// especifies the edge connectivity
    information between vertices//setAttr node.meshAttr -type mesh v3 0 0 0 0 1 0 0
    0 1vn3 1 0 0 1 0 0 1 0 0vt3 0 0 0 1 1 0e3 0 1 hard1 2 hard2 0 hard;-type
    latticeLattice dataValue SyntaxValue MeaningsDivisionCount tDivisionCount
    uDivisionCountExample// sDivisionCount is the horizontal lattice division
    count// tDivisionCount is the vertical lattice division count// uDivisionCount
    is the depth lattice division count// pointCount is the total number of lattice
    points// pointX,pointY,pointZ is one lattice point.  The list is//   specified
    varying first in S, then in T, last in U so the//   first two entries are
    (S=0,T=0,U=0) (s=1,T=0,U=0)//setAttr node.latticeAttr -type lattice 2 5 2 20-2
    -2 -2 2 -2 -2 -2 -1 -2 2 -1 -2 -2 0 -22 0 -2 -2 1 -2 2 1 -2 -2 2 -2 2 2 -2-2 -2
    2 2 -2 2 -2 -1 2 2 -1 2 -2 0 22 0 2 -2 1 2 2 1 2 -2 2 2 2 2 2;In query mode,
    return type is based on queried flag.
    
    Maya Bug Fix:
      - setAttr did not work with type matrix.
    
    Modifications:
      - No need to set type, this will automatically be determined
      - Adds support for passing a list or tuple as the second argument for datatypes such as double3.
      - When setting stringArray datatype, you no longer need to prefix the list with the number of elements - just pass a list or tuple as with other arrays
      - Added 'force' kwarg, which causes the attribute to be added if it does not exist.
            - if no type flag is passed, the attribute type is based on type of value being set (if you want a float, be sure to format it as a float, e.g.  3.0 not 3)
            - currently does not support compound attributes
            - currently supported python-to-maya mappings:
    
                ============ ===========
                python type  maya type
                ============ ===========
                float        double
                ------------ -----------
                int          long
                ------------ -----------
                str          string
                ------------ -----------
                bool         bool
                ------------ -----------
                Vector       double3
                ------------ -----------
                Matrix       matrix
                ------------ -----------
                [str]        stringArray
                ============ ===========
    
    
        >>> addAttr( 'persp', longName= 'testDoubleArray', dataType='doubleArray')
        >>> setAttr( 'persp.testDoubleArray', [0,1,2])
        >>> setAttr( 'defaultRenderGlobals.preMel', 'sfff')
    
      - Added ability to set enum attributes using the string values; this may be
        done either by setting the 'asString' kwarg to True, or simply supplying
        a string value for an enum attribute.
    
    Flags:
    - alteredValue : av              (bool)          [create]
        The value is only the current value, which may change in the next evalution (if
        the attribute has an incoming connection). This flag is only used during file
        I/O, so that attributes with incoming connections do not have their data
        overwritten during the first evaluation after a file is opened.
    
    - caching : ca                   (bool)          [create]
        Sets the attribute's internal caching on or off. Not all attributes can be
        defined as caching. Only those attributes that are not defined by default to be
        cached can be made caching.  As well, multi attribute elements cannot be made
        caching. Caching also affects child attributes for compound attributes.
    
    - capacityHint : ch              (int)           [create]
        Used to provide a memory allocation hint to attributes where the -size flag
        cannot provide enough information. This flag is optional and is primarily
        intended to be used during file I/O. Only certain attributes make use of this
        flag, and the interpretation of the flag value varies per attribute. This flag
        is currently used by (node.attribute): mesh.face - hints the total number of
        elements in the face edge lists
    
    - channelBox : cb                (bool)          [create]
        Sets the attribute's display in the channelBox on or off. Keyable attributes are
        always display in the channelBox regardless of the channelBox settting.
    
    - clamp : c                      (bool)          [create]
        For numeric attributes, if the value is outside the range of the attribute,
        clamp it to the min or max instead of failing
    
    - keyable : k                    (bool)          [create]
        Sets the attribute's keyable state on or off.
    
    - lock : l                       (bool)          [create]
        Sets the attribute's lock state on or off.
    
    - size : s                       (int)           [create]
        Defines the size of a multi-attribute array. This is only a hint, used to help
        allocate memory as efficiently as possible.
    
    - type : typ                     (unicode)       [create]
        Identifies the type of data.  If the -type flag is not present, a numeric type
        is assumed.                  Flag can have multiple arguments, passed either as
        a tuple or a list.
    
    
    Derived from mel command `maya.cmds.setAttr`
    """
    pass


def uniqueObjExists(name):
    """
    Returns True if name uniquely describes an object in the scene.
    """
    pass


def distanceDimension(*args, **kwargs):
    """
    This command is used to create a distance dimension to display the distance
    between two specified points.
    
    Flags:
    - endPoint : ep                  (float, float, float) [create]
        Specifies the point to measure distance to, from the startPoint.
    
    - startPoint : sp                (float, float, float) [create]
        Specifies the point to start measuring distance from.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.distanceDimension`
    """
    pass


def getEnums(attr):
    """
    Get the enumerators for an enum attribute.
    
    Parameters
    ----------
    attr : Union[unicode, Attribute]
    
    Returns
    -------
    _util.enum.EnumDict
    
    Examples
    --------
    >>> addAttr( "persp", ln='numbers', at='enum', enumName="zero:one:two:thousand=1000:three")
    >>> numbers = Attribute('persp.numbers').getEnums()
    >>> sorted(numbers.items())
    [(u'one', 1), (u'thousand', 1000), (u'three', 1001), (u'two', 2), (u'zero', 0)]
    >>> numbers[1]
    u'one'
    >>> numbers['thousand']
    1000
    """
    pass


def listTransforms(*args, **kwargs):
    """
    Modifications:
      - returns wrapped classes
    
    Returns
    -------
    List[nodetypes.Transform]
    """
    pass


def disconnectAttr(source, destination='None', inputs='None', outputs='None', **kwargs):
    """
    Disconnects two connected attributes. First argument is the source attribute,
    second is the destination.
    
    Modifications:
      - If no destination is passed, then all inputs will be disconnected if inputs
          is True, and all outputs will be disconnected if outputs is True; if
          neither are given (or both are None), both all inputs and all outputs
          will be disconnected
    
    Flags:
    - nextAvailable : na             (bool)          [create]
        If the destination multi-attribute has set the indexMatters to be false, the
        command will disconnect the first matching connection.  No index needs to be
        specified.                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.disconnectAttr`
    """
    pass


def _formatSlice(sliceObj): pass


def setEnums(attr, enums):
    """
    Set the enumerators for an enum attribute.
    """
    pass


def _deprecatePyNode(): pass


def rename(obj, newname, **kwargs):
    """
    Renames the given object to have the new name. If only one argument is supplied
    the command will rename the (first) selected object. If the new name conflicts
    with an existing name, the object will be given a unique name based on the
    supplied name. It is not legal to rename an object to the empty string. When a
    transform is renamed then any shape nodes beneath the transform that have the
    same prefix as the old transform name are renamed. For example, rename
    nurbsSphere1 ballwould rename nurbsSphere1|nurbsSphereShape1to ball|ballShape.
    If the new name ends in a single '#' then the rename command will replace the
    trailing '#' with a number that ensures the new name is unique.
    
    Modifications:
        - if the full path to an object is passed as the new name, the shortname of the object will automatically be used
        
    
    Flags:
    - ignoreShape : ignoreShape      (bool)          [create]
        Indicates that renaming of shape nodes below transform nodes should be
        prevented.
    
    - uuid : uid                     (bool)          [create]
        Indicates that the new name is actually a UUID, and that the command should
        change the node's UUID. (In which case its name remains unchanged.)
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.rename`
    """
    pass


def condition(*args, **kwargs):
    """
    This command creates a new named condition object whose true/false value is
    calculated by running a mel script. This new condition can then be used for
    dimming, or controlling other scripts, or whatever. In query mode, return type
    is based on queried flag.
    
    Flags:
    - delete : delete                (bool)          [create]
        Deletes the condition.
    
    - dependency : d                 (unicode)       [create]
        Each -dependency flag specifies another condition that the new condition will be
        dependent on.  When any of these conditions change, the new-state-script will
        run, and the state of this condition will be set accordingly.  It is possible to
        define infinite loops, but they will be caught and handled correctly at run-
        time.
    
    - initialize : i                 (bool)          [create]
        Initializes the condition, by forcing it to run its script as soon as it is
        created.  If this flag is not specified, the script will not run until one of
        the dependencies is triggered.
    
    - script : s                     (unicode)       [create]
        The script that determines the new state of the condition.
    
    - state : st                     (bool)          [create,query,edit]
        Sets the state of the condition. This can be used to create a manually triggered
        condition: you could create a condition without any dependencies and without a
        new-state-script. This condition would only change state in response to the
        -st/state flag.                  Flag can have multiple arguments, passed either
        as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.condition`
    """
    pass


def _MPlugOut(self, x): pass


def listAttr(*args, **kwargs):
    """
    This command lists the attributes of a node.  If no flags are specified all
    attributes are listed.
    
    Flags:
    - array : a                      (bool)          [create]
        only list array (not multi) attributes
    
    - caching : ca                   (bool)          [create]
        only show attributes that are cached internally
    
    - category : ct                  (unicode)       [create]
        only show attributes belonging to the given category. Category string can be a
        regular expression.
    
    - changedSinceFileOpen : cfo     (bool)          [create]
        Only list the attributes that have been changed since the file they came from
        was opened. Typically useful only for objects/attributes coming from referenced
        files.
    
    - channelBox : cb                (bool)          [create]
        only show non-keyable attributes that appear in the channelbox
    
    - connectable : c                (bool)          [create]
        only show connectable attributes
    
    - extension : ex                 (bool)          [create]
        list user-defined attributes for all nodes of this type (extension attributes)
    
    - fromPlugin : fp                (bool)          [create]
        only show attributes that were created by a plugin
    
    - hasData : hd                   (bool)          [create]
        list only attributes that have data (all attributes except for message
        attributes)
    
    - hasNullData : hnd              (bool)          [create]
        list only attributes that have null data. This will list all attributes that
        have data (see hasData flag) but the data value is uninitialized. A common
        example where an attribute may have null data is when a string attribute is
        created but not yet assigned an initial value. Similarly array attribute data is
        often null until it is initialized.
    
    - inUse : iu                     (bool)          [create]
        only show attributes that are currently marked as in use. This flag indicates
        that an attribute affects the scene data in some way. For example it has a non-
        default value or it is connected to another attribute.  This is the general
        concept though the precise implementation is subject to change.
    
    - keyable : k                    (bool)          [create]
        only show attributes that can be keyframed
    
    - leaf : lf                      (bool)          [create]
        Only list the leaf-level name of the attribute. controlPoints[44].xValue would
        be listed as xValue.
    
    - locked : l                     (bool)          [create]
        list only attributes which are locked
    
    - multi : m                      (bool)          [create]
        list each currently existing element of a multi-attribute
    
    - output : o                     (bool)          [create]
        List only the attributes which are numeric or which are compounds of numeric
        attributes.
    
    - ramp : ra                      (bool)          [create]
        list only attributes which are ramps
    
    - read : r                       (bool)          [create]
        list only attributes which are readable
    
    - readOnly : ro                  (bool)          [create]
        List only the attributes which are readable and not writable.
    
    - scalar : s                     (bool)          [create]
        only list scalar numerical attributes
    
    - scalarAndArray : sa            (bool)          [create]
        only list scalar and array attributes
    
    - settable : se                  (bool)          [create]
        list attribute which are settable
    
    - shortNames : sn                (bool)          [create]
        list short attribute names (default is to list long names)
    
    - string : st                    (unicode)       [create]
        List only the attributes that match the other criteria AND match the string(s)
        passed from this flag. String can be a regular expression.
    
    - unlocked : u                   (bool)          [create]
        list only attributes which are unlocked
    
    - usedAsFilename : uf            (bool)          [create]
        list only attributes which are designated to be treated as filenames
    
    - userDefined : ud               (bool)          [create]
        list user-defined (dynamic) attributes
    
    - visible : v                    (bool)          [create]
        only show visible or non-hidden attributes
    
    - write : w                      (bool)          [create]
        list only attributes which are writable                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.listAttr`
    """
    pass


def toolPropertyWindow(*args, **kwargs):
    """
    End users should only call this command as 1. a query (in the custom tool
    property sheet code) or 2. with no arguments to create the default tool property
    sheet.  The more complex uses of it are internal. In query mode, return type is
    based on queried flag.
    
    Flags:
    - field : fld                    (unicode)       [query,edit]
        Sets/returns the name of the text field used to store the tool name in the
        property sheet.
    
    - helpButton : hb                (unicode)       [query,edit]
        Sets/returns the name of the button used to show help on the tool in the
        property sheet.
    
    - icon : icn                     (unicode)       [query,edit]
        Sets/returns the name of the static picture object (used to display the tool
        icon in the property sheet).
    
    - inMainWindow : imw             (bool)          [create]
        Specify true if you want the tool settings to appear in the main window rather
        than a separate window.
    
    - location : loc                 (unicode)       [query,edit]
        Sets/returns the location of the current tool property sheet, or an empty string
        if there is none.
    
    - noviceMode : nm                (bool)          [query,edit]
        Sets/returns the 'novice mode' flag.(unused at the moment)
    
    - refresh : rf                   (bool)          []
    
    - resetButton : rb               (unicode)       [query,edit]
        Sets/returns the name of the button used to restore the tool settings in the
        property sheet.
    
    - restore : rs                   (bool)          [create]
        Reopens the tool settings window. This flag can be used with the flag
        inMainWindowfor the fall back location if the tool settings can't be restored.
    
    - selectCommand : sel            (unicode)       [query,edit]
        Sets/returns the property sheet's select command.
    
    - showCommand : shw              (unicode)       [query,edit]
        Sets/returns the property sheet's display command.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.toolPropertyWindow`
    """
    pass


def _objectError(objectName): pass


def commandLogging(*args, **kwargs):
    """
    This command controls logging of Maya commands, in memory and on disk. Note that
    if commands are logged in memory, they will be available to the crash reporter
    and appear in crash logs.                In query mode, return type is based on
    queried flag.
    
    Flags:
    - historySize : hs               (int)           [create,query]
        Sets the number of entries in the in-memory command history.
    
    - logCommands : lc               (bool)          [create,query]
        Enables or disables the on-disk logging of commands.
    
    - logFile : lf                   (unicode)       [create,query]
        Sets the filename to use for the on-disk log. If logging is active, the current
        file will be closed before the new one is opened.
    
    - recordCommands : rc            (bool)          [create,query]
        Enables or disables the in-memory logging of commands.
    
    - resetLogFile : rl              (bool)          [create,query]
        Reset the log filename to the default ('mayaCommandLog.txt' in the application
        folder, alongside 'Maya.env' and the default projects folder).
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.commandLogging`
    """
    pass


def assignCommand(*args, **kwargs):
    """
    This command allows the user to assign hotkeys and manipulate the internal array
    of named command objects. Each object in the array has an 1-based index which is
    used for referencing. Under expected usage you should not need to use this
    command directly as the Hotkey Editor may be used to assign hotkeys. This
    command is obsolete for setting new hotkeys, instead please use the
    hotkeycommand. In query mode, return type is based on queried flag.
    
    Flags:
    - addDivider : ad                (unicode)       [edit]
        Appends an annotated divideritem to the end of the list of commands.
    
    - altModifier : alt              (bool)          [edit]
        This flag specifies if an alt modifier is used for the key.
    
    - annotation : ann               (unicode)       [query,edit]
        The string is the english name describing the command.
    
    - command : c                    (script)        [query,edit]
        This is the command that is executed when this object is mapped to a key or
        menuItem.
    
    - commandModifier : cmd          (bool)          [edit]
        This flag specifies if a command modifier is used for the key. This is only
        available on systems which support a separate command key.
    
    - ctrlModifier : ctl             (bool)          [edit]
        This flag specifies if a ctrl modifier is used for the key.
    
    - data1 : da1                    (unicode)       [query,edit]
        Optional, user-defined data strings may be attached to the nameCommand objects.
    
    - data2 : da2                    (unicode)       [query,edit]
        Optional, user-defined data strings may be attached to the nameCommand objects.
    
    - data3 : da3                    (unicode)       [query,edit]
        Optional, user-defined data strings may be attached to the nameCommand objects.
    
    - delete : d                     (int)           [edit]
        This tells the Manager to delete the object at position index.
    
    - dividerString : ds             (unicode)       [query]
        If the passed index corresponds to a divideritem, then the divider's annotation
        is returned.  Otherwise, a null string is returned.
    
    - enableCommandRepeat : ecr      (bool)          [edit]
        This flag specifies whether command repeat is enabled.
    
    - factorySettings : fs           (bool)          [edit]
        This flag sets the manager back to factory settings.
    
    - index : i                      (int)           [edit]
        The index of the object to operate on. The index value ranges from 1 to the
        number of name command objects.
    
    - keyArray : ka                  (bool)          [query]
        This flag returns all of the hotkeys on the command.
    
    - keyString : k                  (unicode)       [query,edit]
        This specifies a key to assign a command to in edit mode. In query mode this
        flag returns the key string, modifiers and indicates if the command is mapped to
        keyUp or keyDown.
    
    - keyUp : kup                    (bool)          [edit]
        This flag specifies if the command is executed on keyUp or keyDown.
    
    - name : n                       (bool)          [query]
        The name of the command object.
    
    - numDividersPreceding : ndp     (int)           [query]
        If the index of a namedCommand object Cis passed in, then this flag returns the
        number of divideritems preceding Cwhen the namedCommands are sorted by category.
    
    - numElements : num              (bool)          [query]
        This command returns the number of namedCommands in the system. This flag
        doesn't require the index to be specified.
    
    - optionModifier : opt           (bool)          [edit]
        This flag specifies if an option modifier is used for the key.
    
    - sortByKey : sbk                (bool)          [query,edit]
        This key tells the manager to sort by key or by order of creation.
    
    - sourceUserCommands : suc       (bool)          [edit]
        This command sources the user named command file.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.assignCommand`
    """
    pass


def parent(*args, **kwargs):
    """
    This command parents (moves) objects under a new group, removes objects from an
    existing group, or adds/removes parents. If the -w flag is specified all the
    selected or specified objects are parented to the world (unparented first). If
    the -rm flag is specified then all the selected or specified instances are
    removed. If there are more than two objects specified all the objects are
    parented to the last object specified. If the -add flag is specified, the
    objects are not reparented but also become children of the last object
    specified. If there is only a single object specified then the selected objects
    are parented to that object. If an object is parented under a different group
    and there is an object in that group with the same name then this command will
    rename the parented object.
    
    Modifications:
        - if parent is `None`, world=True is automatically set
        - if the given parent is the current parent, don't error (similar to mel)
    
    Returns
    -------
    List[nodetypes.DagNode]
    
    Flags:
    - absolute : a                   (bool)          [create]
        preserve existing world object transformations (overall object transformation is
        preserved by modifying the objects local transformation) If the object to parent
        is a joint, it will alter the translation and joint orientation of the joint to
        preserve the world object transformation if this suffices. Otherwise, a
        transform will be inserted between the joint and the parent for this purpose. In
        this case, the transformation inside the joint is not altered. [default]
    
    - addObject : add                (bool)          [create]
        preserve existing local object transformations but don't reparent, just add the
        object(s) under the parent. Use -world to add the world as a parent of the given
        objects.
    
    - noConnections : nc             (bool)          [create]
        The parent command will normally generate new instanced set connections when
        adding instances. (ie. make a connection to the shading engine for new
        instances) This flag suppresses this behaviour and is primarily used by the file
        format.
    
    - noInvScale : nis               (bool)          [create]
        The parent command will normally connect inverseScale to its parent scale on
        joints. This is used to compensate scale on joint. The connection of
        inverseScale will occur if both child and parent are joints and no connection is
        present on child's inverseScale. In case of a reparenting, the old inverseScale
        will only get broken if the old parent is a joint. Otherwise connection will
        remain intact. This flag suppresses this behaviour.
    
    - relative : r                   (bool)          [create]
        preserve existing local object transformations (relative to the parent node)
    
    - removeObject : rm              (bool)          [create]
        Remove the immediate parent of every object specified. To remove only a single
        instance of a shape from a parent, the path to the shape should be specified.
        Note: if there is a single parent then the object is effectively deleted from
        the scene. Use -world to remove the world as a parent of the given object.
    
    - shape : s                      (bool)          [create]
        The parent command usually only operates on transforms.  Using this flags allows
        a shape that is specified to be directly parented under the given transform.
        This is used to instance a shape node. (ie. parent -add -shapeis equivalent to
        the instancecommand). This flag is primarily used by the file format.
    
    - world : w                      (bool)          [create]
        unparent given object(s) (parent to world)                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.parent`
    """
    pass


def addAttr(*args, **kwargs):
    """
    This command is used to add a dynamic attribute to a node or nodes. Either the
    longName or the shortName or both must be specified. If neither a dataType nor
    an attributeType is specified, a double attribute will be added.  The dataType
    flag can be specified more than once indicating that any of the supplied types
    will be accepted (logical-or).  To add a non-double attribute the following
    criteria can be used to determine whether the dataType or the attributeType flag
    is appropriate.  Some types, such as double3can use either. In these cases the
    -dtflag should be used when you only wish to access the data as an atomic entity
    (eg. you never want to access the three individual values that make up a
    double3).  In general it is best to use the -atin these cases for maximum
    flexibility. In most cases the -dtversion will not display in the attribute
    editor as it is an atomic type and you are not allowed to change individual
    parts of it.  All attributes flagged as (compound)below or the compound
    attribute itself are not actually added to the node until all of the children
    are defined (using the -pflag to set their parent to the compound being
    created).  See the EXAMPLES section for more details.  Type of attribute
    Flag and argument to use      boolean
    -at bool                      32 bit integer                                 -at
    long                      16 bit integer                                 -at
    short                     8 bit integer                                  -at
    byte                      char
    -at char                      enum
    -at enum (specify the enum names using the enumName flag) float
    -at float(use quotes
    since float is a mel keyword)   double
    -at double            angle value                                    -at
    doubleAngle       linear value                                   -at
    doubleLinear      string                                                 -dt
    string(use quotes
    since string is a mel keyword)  array of strings
    -dt stringArray       compound                                               -at
    compound          message (no data)                              -at message
    time                                                   -at time
    4x4 double matrix                              -dt matrix(use quotes
    since matrix is a mel keyword)  4x4 float matrix
    -at fltMatrix         reflectance                                    -dt
    reflectanceRGBreflectance (compound)                 -at reflectance
    spectrum                                               -dt spectrumRGB
    spectrum (compound)                    -at spectrum          2 floats
    -dt float2            2 floats (compound)                    -at float2
    3 floats                                               -dt float3            3
    floats (compound)                    -at float3            2 doubles
    -dt double2           2 doubles (compound)                   -at double2
    3 doubles                                              -dt double3           3
    doubles (compound)                   -at double3           2 32-bit integers
    -dt long2                     2 32-bit integers (compound)   -at long2
    3 32-bit integers                              -dt long3                     3
    32-bit integers (compound)   -at long3                     2 16-bit integers
    -dt short2            2 16-bit integers (compound)   -at short2            3
    16-bit integers                              -dt short3            3 16-bit
    integers (compound)   -at short3            array of doubles
    -dt doubleArray       array of floats                                -dt
    floatArray        array of 32-bit ints                   -dt Int32Array
    array of vectors                               -dt vectorArray       nurbs curve
    -dt nurbsCurve        nurbs surface                                  -dt
    nurbsSurface      polygonal mesh                                 -dt mesh
    lattice                                                -dt lattice
    array of double 4D points              -dt pointArray        In query mode,
    return type is based on queried flag.
    
    Modifications:
      - allow python types to be passed to set -at type
                str         string
                float       double
                int         long
                bool        bool
                Vector      double3
      - when querying dataType, the dataType is no longer returned as a list
      - when editing hasMinValue, hasMaxValue, hasSoftMinValue, or hasSoftMaxValue the passed boolean value was ignored
        and the command instead behaved as a toggle.  The behavior is now more intuitive::
    
            >>> addAttr('persp', ln='test', at='double', k=1)
            >>> addAttr('persp.test', query=1, hasMaxValue=True)
            False
            >>> addAttr('persp.test', edit=1, hasMaxValue=False)
            >>> addAttr('persp.test', query=1, hasMaxValue=True)
            False
            >>> addAttr('persp.test', edit=1, hasMaxValue=True)
            >>> addAttr('persp.test', query=1, hasMaxValue=True)
            True
    
      - allow passing a list or dict instead of a string for enumName
      - allow user to pass in type and determine whether it is a dataType or
        attributeType. Types that may be both, such as float2, float3, double2,
        double3, long2, long3, short2, and short3 are all treated as
        attributeTypes. In addition, as a convenience, since these attributeTypes
        are actually treated as compound attributes, the child attributes are
        automatically created, with X/Y/Z appended, unless usedAsColor is set, in
        which case R/G/B is added. Alternatively, the suffices can explicitly
        specified with childSuffixes:
    
            >>> addAttr('persp', ln='autoDouble', type='double', k=1)
            >>> addAttr('persp.autoDouble', query=1, attributeType=1)
            u'double'
            >>> addAttr('persp.autoDouble', query=1, dataType=1)
            u'TdataNumeric'
            >>> addAttr('persp', ln='autoMesh', type='mesh', k=1)
            >>> addAttr('persp.autoMesh', query=1, attributeType=1)
            u'typed'
            >>> addAttr('persp.autoMesh', query=1, dataType=1)
            u'mesh'
            >>> addAttr('persp', ln='autoDouble3Vec', type='double3', k=1)
            >>> [x.attrName() for x in PyNode('persp').listAttr() if 'autoDouble3' in x.name()]
            [u'autoDouble3Vec', u'autoDouble3VecX', u'autoDouble3VecY', u'autoDouble3VecZ']
            >>> addAttr('persp', ln='autoFloat3Col', type='float3', usedAsColor=1)
            >>> [x.attrName() for x in PyNode('persp').listAttr() if 'autoFloat3' in x.name()]
            [u'autoFloat3Col', u'autoFloat3ColR', u'autoFloat3ColG', u'autoFloat3ColB']
            >>> addAttr('persp', ln='autoLong2', type='long2', childSuffixes=['_first', '_second'])
            >>> [x.attrName() for x in PyNode('persp').listAttr() if 'autoLong2' in x.name()]
            [u'autoLong2', u'autoLong2_first', u'autoLong2_second']
    
    Flags:
    - attributeType : at             (unicode)       [create,query]
        Specifies the attribute type, see above table for more details. Note that the
        attribute types float, matrixand stringare also MEL keywords and must be
        enclosed in quotes.
    
    - binaryTag : bt                 (unicode)       [create,query]
        This flag is obsolete and does not do anything any more
    
    - cachedInternally : ci          (bool)          [create,query]
        Whether or not attribute data is cached internally in the node. This flag
        defaults to true for writable attributes and false for non-writable attributes.
        A warning will be issued if users attempt to force a writable attribute to be
        uncached as this will make it impossible to set keyframes.
    
    - category : ct                  (unicode)       [create,query,edit]
        An attribute category is a string associated with the attribute to identify it.
        (e.g. the name of a plugin that created the attribute, version information,
        etc.) Any attribute can be associated with an arbitrary number of categories
        however categories can not be removed once associated.
    
    - dataType : dt                  (unicode)       [create,query]
        Specifies the data type.  See setAttrfor more information on data type names.
    
    - defaultValue : dv              (float)         [create,query,edit]
        Specifies the default value for the attribute (can only be used for numeric
        attributes).
    
    - disconnectBehaviour : dcb      (int)           [create,query]
        defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete
    
    - enumName : en                  (unicode)       [create,query,edit]
        Flag used to specify the ui names corresponding to the enum values. The
        specified string should contain a colon-separated list of the names, with
        optional values. If values are not specified, they will treated as sequential
        integers starting with 0. For example: -enumName A:B:Cwould produce options:
        A,B,C with values of 0,1,2; -enumName zero:one:two:thousand=1000would produce
        four options with values 0,1,2,1000; and -enumName
        solo=1:triplet=3:quintet=5would produce three options with values 1,3,5.  (Note
        that there is a current limitation of the Channel Box that will sometimes
        incorrectly display an enumerated attribute's pull-down menu.  Extra menu items
        can appear that represent the numbers inbetween non-sequential option values.
        To avoid this limitation, specify sequential values for the options of any
        enumerated attributes that will appear in the Channel Box.  For example:
        solo=1:triplet=2:quintet=3.)
    
    - exists : ex                    (bool)          [create,query]
        Returns true if the attribute queried is a user-added, dynamic attribute; false
        if not.
    
    - fromPlugin : fp                (bool)          [create,query]
        Was the attribute originally created by a plugin? Normally set automatically
        when the API call is made - only added here to support storing it in a file
        independently from the creating plugin.
    
    - hasMaxValue : hxv              (bool)          [create,query,edit]
        Flag indicating whether an attribute has a maximum value. (can only be used for
        numeric attributes).
    
    - hasMinValue : hnv              (bool)          [create,query,edit]
        Flag indicating whether an attribute has a minimum value. (can only be used for
        numeric attributes).
    
    - hasSoftMaxValue : hsx          (bool)          [create,query]
        Flag indicating whether a numeric attribute has a soft maximum.
    
    - hasSoftMinValue : hsn          (bool)          [create,query]
        Flag indicating whether a numeric attribute has a soft minimum.
    
    - hidden : h                     (bool)          [create,query]
        Will this attribute be hidden from the UI?
    
    - indexMatters : im              (bool)          [create,query]
        Sets whether an index must be used when connecting to this multi-attribute.
        Setting indexMatters to false forces the attribute to non-readable.
    
    - internalSet : internalSet      (bool)          [create,query]
        Whether or not the internal cached value is set when this attribute value is
        changed.  This is an internal flag used for updating UI elements.
    
    - keyable : k                    (bool)          [create,query]
        Is the attribute keyable by default?
    
    - longName : ln                  (unicode)       [create,query]
        Sets the long name of the attribute.
    
    - maxValue : max                 (float)         [create,query,edit]
        Specifies the maximum value for the attribute (can only be used for numeric
        attributes).
    
    - minValue : min                 (float)         [create,query,edit]
        Specifies the minimum value for the attribute (can only be used for numeric
        attributes).
    
    - multi : m                      (bool)          [create,query]
        Makes the new attribute a multi-attribute.
    
    - niceName : nn                  (unicode)       [create,query,edit]
        Sets the nice name of the attribute for display in the UI.  Setting the
        attribute's nice name to a non-empty string overrides the default behaviour of
        looking up the nice name from Maya's string catalog.   (Use the MEL commands
        attributeNiceNameand attributeQuery -niceNameto lookup an attribute's nice name
        in the catalog.)
    
    - numberOfChildren : nc          (int)           [create,query]
        How many children will the new attribute have?
    
    - parent : p                     (unicode)       [create,query]
        Attribute that is to be the new attribute's parent.
    
    - proxy : pxy                    (unicode)       [create,query]
        Proxy another node's attribute. Proxied plug will be connected as source. The
        UsedAsProxy flag is automatically set in this case.
    
    - readable : r                   (bool)          [create,query]
        Can outgoing connections be made from this attribute?
    
    - shortName : sn                 (unicode)       [create,query]
        Sets the short name of the attribute.
    
    - softMaxValue : smx             (float)         [create,query,edit]
        Soft maximum, valid for numeric attributes only.  Specifies the upper default
        limit used in sliders for this attribute.
    
    - softMinValue : smn             (float)         [create,query,edit]
        Soft minimum, valid for numeric attributes only.  Specifies the upper default
        limit used in sliders for this attribute.
    
    - storable : s                   (bool)          [create,query]
        Can the attribute be stored out to a file?
    
    - usedAsColor : uac              (bool)          [create,query]
        Is the attribute to be used as a color definition? Must have 3 DOUBLE or 3 FLOAT
        children to use this flag.  The attribute type -atshould be double3or float3as
        appropriate.  It can also be used to less effect with data types -dtas double3or
        float3as well but some parts of the code do not support this alternative.  The
        special attribute types/data spectrumand reflectancealso support the color flag
        and on them it is set by default.
    
    - usedAsFilename : uaf           (bool)          [create,query]
        Is the attribute to be treated as a filename definition? This flag is only
        supported on attributes with data type -dtof string.
    
    - usedAsProxy : uap              (bool)          [create,query]
        Set if the specified attribute should be treated as a proxy to another
        attributes.
    
    - writable : w                   (bool)          [create,query]
        Can incoming connections be made to this attribute?
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.addAttr`
    """
    pass


def selected(**kwargs):
    """
    ls -sl
    """
    pass


def createNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.
    
    Flags:
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace doesn't
        exist, we will create the namespace.
    
    - parent : p                     (unicode)       [create]
        Specifies the parent in the DAG under which the new node belongs.
    
    - shared : s                     (bool)          [create]
        This node is shared across multiple files, so only create it if it does not
        already exist.
    
    - skipSelect : ss                (bool)          [create]
        This node is not to be selected after creation, the original selection will be
        preserved.                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.createNode`
    """
    pass


def instancer(*args, **kwargs):
    """
    This command is used to create a instancer node and set the proper attributes in
    the node.
    
    Flags:
    - addObject : a                  (bool)          [create,edit]
        This flag indicates that objects specified by the -object flag will be added to
        the instancer node as instanced objects.
    
    - cycle : c                      (unicode)       [create,query,edit]
        This flag sets or queries the cycle attribute for the instancer node. The
        options are noneor sequential.  The default is none.
    
    - cycleStep : cs                 (float)         [create,query,edit]
        This flag sets or queries the cycle step attribute for the instancer node.  This
        attribute indicates the size of the step in frames or seconds (see
        cycleStepUnit).
    
    - cycleStepUnits : csu           (unicode)       [create,query,edit]
        This flag sets or queries the cycle step unit attribute for the instancer node.
        The options are framesor seconds.  The default is frames.
    
    - index : i                      (int)           [query]
        This flag is used to query the name of the ith instanced object.
    
    - levelOfDetail : lod            (unicode)       [create,query,edit]
        This flag sets or queries the level of detail of the instanced objects.  The
        options are geometry, boundingBox, boundingBoxes.  The default is geometry.
    
    - name : n                       (unicode)       [create,query]
        This flag sets or queries the name of the instancer node.
    
    - object : obj                   (unicode)       [create,query,edit]
        This flag indicates which objects will be add/removed from the list of instanced
        objects.  The flag is used in conjuction with the -add and -remove flags.  If
        neither of these flags is specified on the command line then -add is assumed.
    
    - objectPosition : op            (unicode)       [query]
        This flag queries the given objects position.  This object can be any instanced
        object or sub-object.
    
    - objectRotation : objectRotation (unicode)       [query]
        This flag queries the given objects rotation.  This object can be any instanced
        object or sub-object.
    
    - objectScale : os               (unicode)       [query]
        This flag queries the given objects scale.  This object can be any instanced
        object or sub-object.
    
    - pointDataSource : pds          (bool)          [query]
        This flag is used to query the source node supply the data for the input points.
    
    - removeObject : rm              (bool)          [edit]
        This flag indicates that objects specified by the -object flag will be removed
        from the instancer node as instanced objects.
    
    - rotationOrder : ro             (unicode)       [create,query,edit]
        This flag specifies the rotation order associated with the rotation flag.  The
        options are XYZ, XZY, YXZ, YZX, ZXY, or ZYX.  By default the attribute is XYZ.
    
    - rotationUnits : ru             (unicode)       [create,query,edit]
        This flag specifies the rotation units associated with the rotation flag.  The
        options are degrees or radians.  By default the attribute is degrees.
    
    - valueName : vn                 (unicode)       [query]
        This flag is used to query the value(s) of the array associated with the given
        name.  If the -index flag is used in conjuction with this flag then the ith
        value will be returned.  Otherwise, the entire array will be returned.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.instancer`
    """
    pass


def _getParent(getter, obj, generations):
    """
    If generations is None, then a list of all the parents is returned.
    """
    pass


def nodeType(node, **kwargs):
    """
    This command returns a string which identifies the given node's type. When no
    flags are used, the unique type name is returned.  This can be useful for seeing
    if two nodes are of the same type. When the apiflag is used, the MFn::Type of
    the node is returned. This can be useful for seeing if a plug-in node belongs to
    a given class. The apiflag cannot be used in conjunction with any other flags.
    When the derivedflag is used, the command returns a string array containing the
    names of all the currently known node types which derive from the node type of
    the given object. When the inheritedflag is used, the command returns a string
    array containing the names of all the base node types inherited by the the given
    node. If the isTypeNameflag is present then the argument provided to the command
    is taken to be the name of a node type rather than the name of a specific node.
    This makes it possible to query the hierarchy of node types without needing to
    have instances of each node type.
    
    Note: this will return the dg node type for an object, like maya.cmds.nodeType,
    NOT the pymel PyNode class.  For objects like components or attributes,
    nodeType will return the dg type of the node to which the PyNode is attached.
    
    Returns
    -------
    unicode
    
    Flags:
    - apiType : api                  (bool)          [create]
        Return the MFn::Type value (as a string) corresponding to the given node.  This
        is particularly useful when the given node is defined by a plug-in, since in
        this case, the MFn::Type value corresponds to the underlying proxy class. This
        flag cannot be used in combination with any of the other flags.
    
    - derived : d                    (bool)          [create]
        Return a string array containing the names of all the currently known node types
        which derive from the type of the specified node.
    
    - inherited : i                  (bool)          [create]
        Return a string array containing the names of all the base node types inherited
        by the specified node.
    
    - isTypeName : itn               (bool)          [create]
        If this flag is present, then the argument provided to the command is the name
        of a node type rather than the name of a specific node.                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.nodeType`
    """
    pass


def partition(*args, **kwargs):
    """
    This command is used to create, query or add/remove sets to a partition. If a
    partition name needs to be specified, it is the first argument, other arguments
    represent the set names. Without any flags, the command will create a partition
    with a default name.  Any sets which are arguments to the command will be added
    to the partition. A set can be added to a partition only if none of its members
    are in any of the other sets in the partition. If the -re/render flag is
    specified when the partition is created, only 'renderable' sets can be added to
    the partition. Sets can be added and removed from a partition by using the
    -addSet or -removeSet flags. Note:If a set is already selected, and the
    partition command is executed, the set will be added to the created partition.
    
    Flags:
    - addSet : add                   (PyNode)        [create]
        Adds the list of sets to the named partition.
    
    - name : n                       (unicode)       [create]
        Assigns the given name to new partition. Valid only for create mode.
    
    - removeSet : rm                 (PyNode)        [create]
        Removes the list of sets from the named partition.
    
    - render : re                    (bool)          [create,query]
        New partition can contain render sets. For use in creation mode only. Default is
        false.  Can also be used with query flag - returns boolean.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.partition`
    """
    pass


def listRelatives(*args, **kwargs):
    """
    This command lists parents and children of DAG objects. The flags -c/children,
    -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents are mutually
    exclusive. Only one can be used in a command. When listing parents of objects
    directly under the world, the command will return an empty parent list. Listing
    parents of objects directly under a shape (underworld objects) will return their
    containing shape node in the list of parents. Listing parents of components of
    objects will return the object. When listing children, shape nodes will return
    their underworld objects in the list of children. Listing children of components
    of objects returns nothing. The -ni/noIntermediate flag works with the -s/shapes
    flag. It causes any intermediate shapes among the descendents to be ignored.
    
    Maya Bug Fix:
      - allDescendents and shapes flags did not work in combination
      - noIntermediate doesn't appear to work
    
    Modifications:
      - returns an empty list when the result is None
      - returns an empty list when the arg is an empty list, tuple, set, or
            frozenset, making it's behavior consistent with when None is passed, or
            no args and nothing is selected (would formerly raise a TypeError)
      - returns wrapped classes
      - fullPath is forced on to ensure that all returned node paths are unique
    
    Returns
    -------
    List[nodetypes.DependNode]
    
    Flags:
    - allDescendents : ad            (bool)          [create]
        Returns all the children, grand-children etc. of this dag node.  If a descendent
        is instanced, it will appear only once on the list returned. Note that it lists
        grand-children before children.
    
    - allParents : ap                (bool)          [create]
        Returns all the parents of this dag node. Normally, this command only returns
        the parent corresponding to the first instance of the object
    
    - children : c                   (bool)          [create]
        List all the children of this dag node (default).
    
    - fullPath : f                   (bool)          [create]
        Return full pathnames instead of object names.
    
    - noIntermediate : ni            (bool)          [create]
        No intermediate objects
    
    - parent : p                     (bool)          [create]
        Returns the parent of this dag node
    
    - path : pa                      (bool)          [create]
        Return a proper object name that can be passed to other commands.
    
    - shapes : s                     (bool)          [create]
        List all the children of this dag node that are shapes (ie, not transforms)
    
    - type : typ                     (unicode)       [create]
        List all relatives of the specified type.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.listRelatives`
    """
    pass


def container(*args, **kwargs):
    """
    This command can be used to create and query container nodes. It is also used to
    perform operations on containers such as: add and remove nodes from the
    containerpublish attributes from nodes inside the containerreplace the
    connections and values from one container onto another oneremove a container
    without removing its member nodes
    
    Flags:
    - addNode : an                   (unicode)       [create,edit]
        Specifies the list of nodes to add to container.
    
    - asset : a                      (unicode)       [query]
        When queried, if all the nodes in nodeList belong to the same container, returns
        container's name. Otherwise returns empty string. This flag is functionally
        equivalent to the findContainer flag.
    
    - assetMember : am               (unicode)       [query]
        Can be used during query in conjunction with the bindAttr flag to query for the
        only published attributes related to the specified node within the container.
    
    - bindAttr : ba                  (unicode, unicode) [query,edit]
        Bind a contained attribute to an unbound published name on the interface of the
        container; returns a list of bound published names. The first string specifies
        the node and attribute name to be bound in node.attrformat. The second string
        specifies the name of the unbound published name. In query mode, returns a
        string array of the published names and their corresponding attributes. The flag
        can also be used in query mode in conjunction with the -publishName,
        -publishAsParent, and -publishAsChild flags.
    
    - connectionList : cl            (bool)          [query]
        Returns a list of the exterior connections to the container node.
    
    - current : c                    (bool)          [create,query,edit]
        In create mode, specify that the newly created asset should be current. In edit
        mode, set the selected asset as current. In query, return the current asset.
    
    - fileName : fn                  (unicode)       [query]
        Used to query for the assets associated with a given file name.
    
    - findContainer : fc             (unicode)       [query]
        When queried, if all the nodes in nodeList belong to the same container, returns
        container's name. Otherwise returns empty string.
    
    - force : f                      (bool)          [create,edit]
        This flag can be used in conjunction with -addNode and -removeNode flags only.
        If specified with -addNode, nodes will be disconnected from their current
        containers before they are added to new one. If specified with -removeNode,
        nodes will be removed from all containers, instead of remaining in the parent
        container if being removed from a nested container.
    
    - includeHierarchyAbove : iha    (bool)          [create,edit]
        Used to specify that the parent hierarchy of the supplied node list should also
        be included in the container (or deleted from the container). Hierarchy
        inclusion will stop at nodes which are members of other containers.
    
    - includeHierarchyBelow : ihb    (bool)          [create,edit]
        Used to specify that the hierarchy below the supplied node list should also be
        included in the container (or delete from the container). Hierarchy inclusion
        will stop at nodes which are members of other containers.
    
    - includeNetwork : inc           (bool)          [create,edit]
        Used to specify that the node network connected to supplied node list should
        also be included in the container. Network traversal will stop at default nodes
        and nodes which are members of other containers.
    
    - includeNetworkDetails : ind    (unicode)       [create,edit]
        Used to specify specific parts of the network that should be included. Valid
        arguments to this flag are: channels, sdk, constraints, historyand expressions,
        inputs, outputs. The difference between this flag and the includeNetwork flag,
        is that it will include all connected nodes regardless of their type. Note that
        dag containers include their children, so they will always include constraint
        nodes that are parented beneath the selected objects, even when constraints are
        not specified as an input.
    
    - includeShaders : isd           (bool)          [create,edit]
        Used to specify that for any shapes included, their shaders will also be
        included in the container.
    
    - includeShapes : ish            (bool)          [create,edit]
        Used to specify that for any transforms selected, their direct child shapes will
        be included in the container (or deleted from the container). This flag is not
        necessary when includeHierarchyBelow is used since the child shapes and all
        other descendents will automatically be included.
    
    - includeTransform : it          (bool)          [create,edit]
        Used to specify that for any shapes selected, their parent transform will be
        included in the container (or deleted from the container). This flag is not
        necessary when includeHierarchyAbove is used since the parent transform and all
        of its parents will automatically be included.
    
    - isContainer : isc              (bool)          [query]
        Return true if the selected or specified node is a container node. If multiple
        containers are queried, only the state of the first will be returned.
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created container.
    
    - nodeList : nl                  (bool)          [query]
        When queried, returns a list of nodes in container. The list will be sorted in
        the order they were added to the container. This will also display any
        reordering done with the reorderContainer command.
    
    - nodeNamePrefix : nnp           (bool)          [create,edit]
        Specifies that the name of published attributes should be of the form node_attr.
        Must be used with the -publishConnections/-pc flag.
    
    - parentContainer : par          (bool)          [query]
        Flag to query the parent container of a specified container.
    
    - preview : p                    (bool)          [create]
        This flag is valid in create mode only. It indicates that you do not want the
        container to be created, instead you want to preview its contents. When this
        flag is used, Maya will select the nodes that would be put in the container if
        you did create the container. For example you can see what would go into the
        container with -includeNetwork, then modify your selection as desired, and do a
        create container with the selected objects only.
    
    - publishAndBind : pb            (unicode, unicode) [edit]
        Publish the given name and bind the attribute to the given name. First string
        specifies the node and attribute name in node.attrformat. Second string
        specifies the name it should be published with.
    
    - publishAsChild : pac           (unicode, unicode) [query,edit]
        Publish contained node to the interface of the container to indicate it can be a
        child of external nodes. The second string is the name of the published node. In
        query mode, returns a string of the published names and the corresponding nodes.
        If -publishName flag is used in query mode, only returns the published names; if
        -bindAttr flag is used in query mode, only returns the name of the published
        nodes.
    
    - publishAsParent : pap          (unicode, unicode) [query,edit]
        Publish contained node to the interface of the container to indicate it can be a
        parent to external nodes. The second string is the name of the published node.
        In query mode, returns a string of array of the published names and the
        corresponding nodes. If -publishName flag is used in query mode, only returns
        the published names; if -bindAttr flag is used in query mode, only returns the
        name of the published nodes.
    
    - publishAsRoot : pro            (unicode, bool) [query,edit]
        Publish or unpublish a node as a root. The significance of root transform node
        is twofold. When container-centric selection is enabled, the root transform will
        be selected if a container node in the hierarchy below it is selected in the
        main scene view. Also, when exporting a container proxy, any published root
        transformation attributes such as translate, rotate or scale will be hooked up
        to attributes on a stand-in node. In query mode, returns the node that has been
        published as root.
    
    - publishAttr : pa               (unicode)       [query]
        In query mode, can only be used with the -publishName(-pn) flag, and takes an
        attribute as an argument; returns the published name of the attribute, if any.
    
    - publishConnections : pc        (bool)          [create,edit]
        Publish all connections from nodes inside the container to nodes outside the
        container.
    
    - publishName : pn               (unicode)       [query,edit]
        Publish a name to the interface of the container, and returns the actual name
        published to the interface.  In query mode, returns the published names for the
        container. If the -bindAttr flag is specified, returns only the names that are
        bound; if the -unbindAttr flag is specified, returns only the names that are not
        bound; if the -publishAsParent/-publishAsChild flags are specified, returns only
        names of published parents/children. if the -publishAttr is specified with an
        attribute argument in the node.attrformat, returns the published name for that
        attribute, if any.
    
    - removeContainer : rc           (bool)          [edit]
        Disconnects all the nodes from container and deletes container node.
    
    - removeNode : rn                (unicode)       [edit]
        Specifies the list of nodes to remove from container. If node is a member of a
        nested container, it will be added to the parent container. To remove from all
        containers completely, use the -force flag.
    
    - type : typ                     (unicode)       [create,query]
        By default, a container node will be created. Alternatively, the type flag can
        be used to indicate that a different type of container should be created. At the
        present time, the only other valid type of container node is dagContainer.
    
    - unbindAndUnpublish : ubp       (unicode)       [edit]
        Unbind the given attribute (in node.attrformat) and unpublish its associated
        name. Unbinding a compound may trigger unbinds of its compound parents/children.
        So the advantage of using this one flag is that it will automatically unpublish
        the names associated with these automatic unbinds.
    
    - unbindAttr : ua                (unicode, unicode) [query,edit]
        Unbind a published attribute from its published name on the interface of the
        container, leaving an unbound published name on the interface of the container;
        returns a list of unbound published names. The first string specifies the node
        and attribute name to be unbound in node.attrformat, and the second string
        specifies the name of the bound published name. In query mode, can only be used
        with the -publishName, -publishAsParent and -publishAsChild flags.
    
    - unbindChild : unc              (unicode)       [edit]
        Unbind the node published as child, but do not remove its published name from
        the interface of the container.
    
    - unbindParent : unp             (unicode)       [edit]
        Unbind the node published as parent, but do not remove its published name from
        the interface of the container.
    
    - unpublishChild : upc           (unicode)       [edit]
        Unpublish node published as child from the interface of the container
    
    - unpublishName : un             (unicode)       [edit]
        Unpublish an unbound name from the interface of the container.
    
    - unpublishParent : upp          (unicode)       [edit]
        Unpublish node published as parent from the interface of the container
    
    - unsortedOrder : uso            (bool)          [query]
        This flag has no effect on the operation of the container command (OBSOLETE).
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.container`
    """
    pass


def listSets(*args, **kwargs):
    """
    The listSets command is used to get a list of all the sets an object belongs to.
    To get sets of a specific type for an object use the type flag as well. To get a
    list of all sets in the scene then don't use an object in the command line but
    use one of the flags instead.
    
    Modifications:
      - returns wrapped classes
      - if called without arguments and keys works as with allSets=True
    
    Returns
    -------
    List[PyNode]
    
    Flags:
    - allSets : allSets              (bool)          [create]
        Returns all sets in the scene.
    
    - extendToShape : ets            (bool)          [create]
        When requesting a transform's sets also walk down to the shape immediately below
        it for its sets.
    
    - object : o                     (PyNode)        [create]
        Returns all sets which this object is a member of.
    
    - type : t                       (int)           [create]
        Returns all sets in the scene of the given type: 1 - all rendering sets2 - all
        deformer setsFlag can have multiple arguments, passed either as a tuple or a
        list.
    
    
    Derived from mel command `maya.cmds.listSets`
    """
    pass


def rotate(obj, *args, **kwargs):
    """
    The rotate command is used to change the rotation of geometric objects. The
    rotation values are specified as Euler angles (rx, ry, rz). The values are
    interpreted based on the current working unit for Angular measurements. Most
    often this is degrees. The default behaviour, when no objects or flags are
    passed, is to do a absolute rotate on each currently selected object in the
    world space.
    
    Modifications:
      - allows any iterable object to be passed as first argument::
    
            rotate("pSphere1", [0,1,2])
    
    NOTE: this command also reorders the argument order to be more intuitive, with the object first
    
    Flags:
    - absolute : a                   (bool)          [create]
        Perform an absolute operation.
    
    - centerPivot : cp               (bool)          [create]
        Let the pivot be the center of the bounding box of all objects
    
    - componentSpace : cs            (bool)          [create]
        Rotate in local component space
    
    - constrainAlongNormal : xn      (bool)          [create]
        When true, transform constraints are applied along the vertex normal first and
        only use the closest point when no intersection is found along the normal.
    
    - deletePriorHistory : dph       (bool)          [create]
        If true then delete the history prior to the current operation.
    
    - euler : eu                     (bool)          [create]
        Modifer for -relative flag that specifies rotation values should be added to
        current XYZ rotation values.
    
    - forceOrderXYZ : fo             (bool)          [create]
        When true, euler rotation value will be understood in XYZ rotation order not per
        transform node basis.
    
    - objectCenterPivot : ocp        (bool)          [create]
        Let the pivot be the center of the bounding box of each object
    
    - objectSpace : os               (bool)          [create]
        Perform rotation about object-space axis.
    
    - orientAxes : oa                (float, float, float) [create]
        Euler axis for orientation.
    
    - pivot : p                      (float, float, float) [create]
        Define the pivot point for the transformation
    
    - preserveChildPosition : pcp    (bool)          [create]
        When true, transforming an object will apply an opposite transform to its child
        transform to keep them at the same world-space position. Default is false.
    
    - preserveGeometryPosition : pgp (bool)          [create]
        When true, transforming an object will apply an opposite transform to its
        geometry points to keep them at the same world-space position. Default is false.
    
    - preserveUV : puv               (bool)          [create]
        When true, UV values on rotated components are projected across the rotation in
        3d space. For small edits, this will freeze the world space texture mapping on
        the object. When false, the UV values will not change for a selected vertices.
        Default is false.
    
    - reflection : rfl               (bool)          [create]
        To move the corresponding symmetric components also.
    
    - reflectionAboutBBox : rab      (bool)          [create]
        Sets the position of the reflection axis  at the geometry bounding box
    
    - reflectionAboutOrigin : rao    (bool)          [create]
        Sets the position of the reflection axis  at the origin
    
    - reflectionAboutX : rax         (bool)          [create]
        Specifies the X=0 as reflection plane
    
    - reflectionAboutY : ray         (bool)          [create]
        Specifies the Y=0 as reflection plane
    
    - reflectionAboutZ : raz         (bool)          [create]
        Specifies the Z=0 as reflection plane
    
    - reflectionTolerance : rft      (float)         [create]
        Specifies the tolerance to findout the corresponding reflected components
    
    - relative : r                   (bool)          [create]
        Perform a operation relative to the object's current position
    
    - rotateX : x                    (bool)          [create]
        Rotate in X direction
    
    - rotateXY : xy                  (bool)          [create]
        Rotate in X and Y direction
    
    - rotateXYZ : xyz                (bool)          [create]
        Rotate in all directions (default)
    
    - rotateXZ : xz                  (bool)          [create]
        Rotate in X and Z direction
    
    - rotateY : y                    (bool)          [create]
        Rotate in Y direction
    
    - rotateYZ : yz                  (bool)          [create]
        Rotate in Y and Z direction
    
    - rotateZ : z                    (bool)          [create]
        Rotate in Z direction
    
    - symNegative : smn              (bool)          [create]
        When set the component transformation is flipped so it is relative to the
        negative side of the symmetry plane. The default (no flag) is to transform
        components relative to the positive side of the symmetry plane.
    
    - translate : t                  (bool)          [create]
        When true, the command will modify the node's translate attribute instead of its
        rotateTranslate attribute, when rotating around a pivot other than the object's
        own rotate pivot.
    
    - worldSpace : ws                (bool)          [create]
        Perform rotation about global world-space axis.
    
    - xformConstraint : xc           (unicode)       [create]
        Apply a transform constraint to moving components. none - no constraintsurface -
        constrain components to the surfaceedge - constrain components to surface
        edgeslive - constraint components to the live surfaceFlag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.rotate`
    """
    pass


def _nodeAddedCallback(list_): pass


def _MObjectIn(x): pass


def _toEnumStr(enums): pass


def hasAttr(pyObj, attr, checkShape='True'):
    """
    Convenience function for determining if an object has an attribute.
    
    Parameters
    ----------
    pyObj : PyNode
    attr : Union[unicode, Attribute, AttributeSpec]
    checkShape : bool
        If enabled, the shape node of a transform will also be
        checked for the attribute.
    
    Returns
    -------
    bool
    """
    pass


def spaceLocator(*args, **kwargs):
    """
    The command creates a locator at the specified position in space. By default it
    is created at (0,0,0).
    
    Flags:
    - absolute : a                   (bool)          [create,edit]
        If set, the locator's position is in world space.
    
    - name : n                       (unicode)       [create,edit]
        Name for the locator.
    
    - position : p                   (float, float, float) [create,query,edit]
        Location in  3-dimensional space where locator is to be created.
    
    - relative : r                   (bool)          [create,edit]
        If set, the locator's position is relative to its local space. The locator is
        created in relative mode by default.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.spaceLocator`
    """
    pass


def _getPymelTypeFromObject(obj, name): pass


_logger = None

SCENE = Scene()

CHECK_ATTR_BEFORE_LOCK = False

deprecated_str_methods = []
