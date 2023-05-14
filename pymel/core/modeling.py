from pymel.internal.pmcmds import polyUVCoverage
from pymel.internal.pmcmds import nurbsSelect
from pymel.internal.pmcmds import subdToBlind
from pymel.internal.pmcmds import subdCollapse
from pymel.internal.pmcmds import nurbsBoolean
from pymel.internal.pmcmds import pointCurveConstraint
from pymel.internal.pmcmds import constructionHistory
from pymel.internal.pmcmds import setXformManip
from pymel.internal.pmcmds import filterExpand
from pymel.internal.pmcmds import polyMirrorFace
from pymel.internal.pmcmds import polyPlanarProjection
from pymel.internal.pmcmds import bezierInfo
from pymel.internal.pmcmds import polyClipboard
from pymel.internal.pmcmds import addMetadata
from pymel.internal.pmcmds import polyBlendColor
from pymel.internal.pmcmds import polyCanBridgeEdge
from pymel.internal.pmcmds import polyForceUV
from pymel.internal.pmcmds import subdivDisplaySmoothness
from pymel.internal.pmcmds import polyEditUV
from pymel.internal.pmcmds import polyAverageNormal
from pymel.internal.pmcmds import polyUVSet
from pymel.internal.pmcmds import nurbsToPoly
from pymel.internal.pmcmds import arubaNurbsToPoly
from pymel.internal.pmcmds import squareSurface
from pymel.internal.pmcmds import polyMergeVertex
from pymel.internal.pmcmds import textCurves
from pymel.internal.pmcmds import polyColorSet
from pymel.internal.pmcmds import subdTransferUVsToCache
from pymel.internal.pmcmds import polySphericalProjection
from pymel.internal.pmcmds import manipPivot
from pymel.internal.pmcmds import polyQueryBlindData
from pymel.internal.pmcmds import stitchSurfacePoints
from pymel.internal.pmcmds import subdEditUV
from pymel.internal.pmcmds import transferShadingSets
from pymel.internal.pmcmds import polyEvaluate
from pymel.internal.pmcmds import subdivCrease
from pymel.internal.pmcmds import makeSingleSurface
from pymel.internal.pmcmds import manipOptions
from pymel.internal.pmcmds import singleProfileBirailSurface
from pymel.internal.pmcmds import polySetToFaceNormal
from pymel.internal.pmcmds import polyColorBlindData
from pymel.internal.pmcmds import nurbsToPolygonsPref
from pymel.internal.pmcmds import polySelectConstraint
from pymel.internal.pmcmds import polyCylindricalProjection
from pymel.internal.pmcmds import polyCreateFacet
from pymel.internal.pmcmds import nurbsCopyUVSet
from pymel.internal.pmcmds import polyCompare
from pymel.internal.pmcmds import polyCollapseTweaks
from pymel.internal.pmcmds import polyUVStackSimilarShells
from pymel.internal.pmcmds import dataStructure
from pymel.internal.pmcmds import polyCircularizeEdge
from pymel.internal.pmcmds import polyCircularizeFace
from pymel.internal.pmcmds import refineSubdivSelectionList
from pymel.internal.pmcmds import subdMatchTopology
from pymel.internal.pmcmds import coarsenSubdivSelectionList
from pymel.internal.pmcmds import polySubdivideFacet
from pymel.internal.pmcmds import nurbsToSubdivPref
from pymel.internal.pmcmds import polyExtrudeFacet
from pymel.internal.pmcmds import subdDuplicateAndConnect
from pymel.internal.pmcmds import polyDuplicateAndConnect
from pymel.internal.pmcmds import pointOnSurface
from pymel.internal.pmcmds import bezierAnchorPreset
from pymel.internal.pmcmds import polyMultiLayoutUV
from pymel.internal.pmcmds import duplicateCurve
from pymel.internal.pmcmds import changeSubdivComponentDisplayLevel
from pymel.internal.pmcmds import polySelect
from pymel.internal.pmcmds import stitchSurface
from pymel.internal.pmcmds import intersect
from pymel.internal.pmcmds import blindDataType
from pymel.internal.pmcmds import polySubdivideEdge
from pymel.internal.pmcmds import polyInfo
from pymel.internal.pmcmds import polyCacheMonitor
from pymel.internal.pmcmds import smoothTangentSurface
from pymel.internal.pmcmds import applyMetadata
from pymel.internal.pmcmds import polyAutoProjection
from pymel.internal.pmcmds import unfold
from pymel.internal.pmcmds import querySubdiv
from pymel.internal.pmcmds import polyUVOverlap
from pymel.internal.pmcmds import polySplitVertex
from pymel.internal.pmcmds import doubleProfileBirailSurface
from pymel.internal.pmcmds import subdPlanarProjection
from pymel.internal.pmcmds import subdAutoProjection
from pymel.internal.pmcmds import changeSubdivRegion
from pymel.internal.pmcmds import polyMoveFacet
from pymel.internal.pmcmds import polyCheck
from pymel.internal.pmcmds import createSubdivRegion
from pymel.internal.pmcmds import polySlideEdge
from pymel.internal.pmcmds import curveOnSurface
from pymel.internal.pmcmds import polyProjection
from pymel.internal.pmcmds import polyEditUVShell
from pymel.internal.pmcmds import geomToBBox
from pymel.internal.pmcmds import duplicateSurface
from pymel.internal.pmcmds import subdToPoly
from pymel.internal.pmcmds import showMetadata
from pymel.internal.pmcmds import polyListComponentConversion
from pymel.internal.pmcmds import getMetadata
from pymel.internal.pmcmds import subdListComponentConversion
from pymel.internal.pmcmds import planarSrf
from pymel.internal.pmcmds import subdMirror
from pymel.internal.pmcmds import polyMergeFacet
from pymel.internal.pmcmds import polyCollapseFacet
from pymel.internal.pmcmds import polyOptions
from pymel.internal.pmcmds import offsetCurveOnSurface
from pymel.internal.pmcmds import multiProfileBirailSurface
from pymel.internal.pmcmds import polyGeoSampler
from pymel.internal.pmcmds import uvSnapshot
from pymel.internal.pmcmds import polyContourProjection
from pymel.internal.pmcmds import illustratorCurves
from pymel.internal.pmcmds import freeFormFillet
from pymel.internal.pmcmds import untangleUV
from pymel.internal.pmcmds import hasMetadata
from pymel.internal.pmcmds import nurbsEditUV
from pymel.internal.pmcmds import blend2
from pymel.internal.pmcmds import moveVertexAlongDirection
from pymel.internal.pmcmds import circularFillet
from pymel.internal.pmcmds import propMove
from pymel.internal.pmcmds import hardenPointCurve
from pymel.internal.pmcmds import tolerance
from pymel.internal.pmcmds import bezierAnchorState
from pymel.internal.pmcmds import canCreateManip
from pymel.internal.pmcmds import polyHole
from pymel.internal.pmcmds import nurbsUVSet
from pymel.internal.pmcmds import pointOnCurve
from pymel.internal.pmcmds import polyOutput

if False:
    from typing import Dict, List, Tuple, Union, Optional


def polyAppendVertex(*args, **kwargs):
    """
    Appends a new face to the selected polygonal object. The direction of the normal
    is given by the vertex order: the face normal points towards the user when the
    vertices rotate counter clockwise. Note that holes must be described in the
    opposite direction. Only works with one object selected.
    
    Flags:
    - append : a                     (float, float, float) [create]
        Append a vertex or a point to the selected object, or mark the start of a hole.
        This flag may also be used in place of the hole, vertexand pointflags. If no
        argument is passed to the appendflag, then it marks the beginning of a hole (use
        an empty tuple in Python '()').  If one argument is passed, then the argument is
        considered to be an index into the vertices of the selected object, as with the
        vertexflag.  If three arguments are passed, then it is interpreted as the
        coordinates of a new point which will be inserted, as with the pointflag.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - hole : h                       (bool)          [create]
        Add a hole. The following points and edges will define a hole.  Note that this
        flag should be avoided in Python.  You may use the appendflag instead and pass
        an empty tuple '()' to specify the start of a hole.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - point : p                      (float, float, float) [create]
        Adds a new point to the new face. Coordinates of free points are given in the
        local object reference.  Note that this flag should be avoided in Python.  You
        may use the appendflag instead and pass three arguments.
    
    - texture : tx                   (int)           [create,query,edit]
        Specifies how new faces are mapped. 0 - None; 1 - Normalize; 2 - Unitize C:
        Default is 0 (no mapping). Q: When queried, this flag returns an int
    
    - vertex : v                     (int)           [create]
        Adds the given vertex of the selected object to the new face.  Note that this
        flag should be avoided in Python.  You may use the appendflag instead and pass
        one argument.                  Flag can have multiple arguments, passed either
        as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyAppendVertex`
    """
    pass


def arcLengthDimension(*args, **kwargs):
    """
    This command is used to create an arcLength dimension to display the arcLength
    of a curve/surface at a specified point on the curve/surface.
    
    
    Derived from mel command `maya.cmds.arcLengthDimension`
    """
    pass


def pointPosition(*args, **kwargs):
    """
    This command returns the world or local space position for any type of point
    object. Valid selection items are: - curve and surface CVs - poly vertices -
    lattice points - particles - curve and surface edit points - curve and surface
    parameter points - poly uvs - rotate/scale/joint pivots - selection handles -
    locators, param locators and arc length locators It works on the selected object
    or you can specify the object in the command. By default, if no flag is
    specified then the world position is returned.
    
    Flags:
    - local : l                      (bool)          [create]
        Return the point in local space coordinates.
    
    - world : w                      (bool)          [create]
        Return the point in world space coordinates.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pointPosition`
    """
    pass


def polyQuad(*args, **kwargs):
    """
    Merges selected triangles of a polygonal object into four-sided faces.
    
    Flags:
    - angle : a                      (float)         [create,query,edit]
        Angle threshold above which two triangles are not merged. C: Default is 30
        degrees. The range is [0.0, 180.0]. Q: When queried, this flag returns a float.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - keepGroupBorder : kgb          (bool)          [create,query,edit]
        Keep facet group border : If on, the borders of selected faces are maintained,
        otherwise the borders of selected facets may be modified. C: Default is on. Q:
        When queried, this flag returns an int.
    
    - keepHardEdges : khe            (bool)          [create,query,edit]
        Keep hard edges : If on, the hard edges of selected faces are maintained,
        otherwise they may be deleted between two triangles. C: Default is on. Q: When
        queried, this flag returns an int.
    
    - keepTextureBorders : ktb       (bool)          [create,query,edit]
        Keep texture border : If on, the borders of texture maps are maintained,
        otherwise the boreders of texture maps may be modified. C: Default is on. Q:
        When queried, this flag returns an int.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyQuad`
    """
    pass


def polyTriangulate(*args, **kwargs):
    """
    Triangulation breaks polygons down into triangles, ensuring that all faces are
    planar and non-holed. Triangulation of models can be beneficial in many areas.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyTriangulate`
    """
    pass


def sphere(*args, **kwargs):
    """
    The sphere command creates a new sphere. The number of spans in the in each
    direction of the sphere is determined by the useTolerance attribute. If -ut is
    true then the -tolerance attribute will be used. If -ut is false then the
    -sections attribute will be used.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        The primitive's axis
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface: 1 - linear, 3 - cubic Default:3
    
    - endSweep : esw                 (float)         [create,query,edit]
        The angle at which to end the surface of revolution. Default is 2Pi radians, or
        360 degrees. Default:6.2831853
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - heightRatio : hr               (float)         [create,query,edit]
        Ratio of heightto widthDefault:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The primitive's pivot point
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    - radius : r                     (float)         [create,query,edit]
        The radius of the object Default:1.0
    
    - sections : s                   (int)           [create,query,edit]
        The number of sections determines the resolution of the surface in the sweep
        direction. Used only if useTolerance is false. Default:8
    
    - spans : nsp                    (int)           [create,query,edit]
        The number of spans determines the resolution of the surface in the opposite
        direction. Default:1
    
    - startSweep : ssw               (float)         [create,query,edit]
        The angle at which to start the surface of revolution Default:0
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to build the surface. Used only if useTolerance is true
        Default:0.01
    
    - useTolerance : ut              (bool)          [create,query,edit]
        Use the specified tolerance to determine resolution. Otherwise number of
        sections will be used. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.sphere`
    """
    pass


def polyDelFacet(*args, **kwargs):
    """
    Deletes faces. If the result is split into disconnected pieces, the pieces (so-
    called shells) are still considered to be one object. Notice : The last face
    cannot be deleted.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyDelFacet`
    """
    pass


def polyColorDel(*args, **kwargs):
    """
    Deletes color from selected components.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - colorSetName : cls             (unicode)       [create,query,edit]
        The name of the color set to work on
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyColorDel`
    """
    pass


def polyMapSewMove(*args, **kwargs):
    """
    This command can be used to Move and Sew together separate UV pieces along
    geometric edges. UV pieces that correspond to the same geometric edge, are
    merged together by moving the smaller piece to the larger one.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - limitPieceSize : lps           (bool)          [create,query,edit]
        When on, this flag specifies that the face number limit described above should
        be used.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - numberFaces : nf               (int)           [create,query,edit]
        Maximum number of faces in a UV piece. When trying to combine two UV pieces into
        a single one, the merge operation is rejected if the smaller piece has more
        faces than the number specified by this flag.This flag is only used when
        limitPieceSizeis set to on.
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMapSewMove`
    """
    pass


def polyOptUvs(*args, **kwargs):
    """
    Optimizes selected UVs.
    
    Flags:
    - applyToShell : applyToShell    (bool)          [create]
        Specifies where the whole object or just shells that are selected or pinned
        should be affected.
    
    - areaWeight : aw                (float)         [create]
        Surface driven importance. 0 treat all faces equal. 1 gives more importance to
        large ones.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - globalBlend : gb               (float)         [create]
        This allows the user to blend between a local optimization method (globalBlend =
        0.0) and a global optimization method (globalBlend = 1.0). The local
        optimization method looks at the ratio between the triangles on the object and
        the triangles in UV space.  It has a side affect that it can sometimes introduce
        tapering problems.  The global optimization is much slower, but takes into
        consideration the entire object when optimizing uv placement.
    
    - globalMethodBlend : gmb        (float)         [create]
        The global optimization method uses two functions to compute a minimization.
        The first function controls edge stretch by using edges lengths between xyz and
        uv.  The second function penalizes the first function by preventing
        configurations where triangles would overlap.  For every surface there is a mix
        between these two functions that will give the appropriate response. Values
        closer to 1.0 give more weight to the edge length function. Values closer to 0.0
        give more weight to surface area.  The default value of '0.5' is a even mix
        between these two values.
    
    - iterations : i                 (int)           [create]
        Maximum number of iterations for each connected UV piece.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - optimizeAxis : oa              (int)           [create]
        Degree of freedom for optimization: 0=Optimize freely, 1=Move vertically only,
        2=Move horzontally only
    
    - pinSelected : ps               (bool)          [create]
        Specifies that the selected components should be pinned instead of the
        unselected components.
    
    - pinUvBorder : pub              (bool)          [create]
        Specifies that the UV border should be pinned when doing the solve. By default
        only unselected components are pinned.
    
    - scale : s                      (float)         [create]
        Ratio between 2d and 3d space.
    
    - stoppingThreshold : ss         (float)         [create]
        Minimum distorsion improvement between two steps in %.
    
    - useScale : us                  (bool)          [create]
        Adjust the scale or not.
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyOptUvs`
    """
    pass


def insertKnotSurface(*args, **kwargs):
    """
    The insertKnotSurface command inserts knots (aka isoparms) into a surface given
    a list of parameter values.  The number of knots to add at each parameter value
    and whether the knots are added or complemented can be specified. The name of
    the surface is returned and if history is on, the name of the resulting
    dependency node is also returned. You must specify one, none or all number of
    knots with the -nkflag. eg. if you specify none, then the default (one) knot
    will be added at each specified parameter value.  If you specify one -nkvalue
    then that number of knots will be added at each parameter value. Otherwise, you
    must specify the same number of -nkflags as -pflags, defining the number of
    knots to be added at each specified parameter value. You can insert up to
    degreeknots at a parameter value that isn't already an isoparm.  eg. for a
    degree 3 surface, you can insert up to 3 knots. Use this operation if you need
    more CVs in a local area of the surface. Use this operation if you want to
    create a corner in the surface. Note: A single insertKnotSurface command cannot
    insert in both directions at once; you must use two separate commands to do
    this.
    
    Flags:
    - addKnots : add                 (bool)          [create,query,edit]
        Whether to add knots or complement.  Complement means knots will be added to
        reach the specified number of knots. Default:true
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - direction : d                  (int)           [create,query,edit]
        Direction in which to insert knot: 0 - V direction, 1 - U direction Default:1
    
    - frozen : fzn                   (bool)          []
    
    - insertBetween : ib             (bool)          [create,query,edit]
        If set to true, and there is more than one parameter value specified, the knots
        will get inserted at equally spaced intervals between the given parameter
        values, rather than at the parameter values themselves. Default:false
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - numberOfKnots : nk             (int)           [create,query,edit]
        How many knots to insert Default:1
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        Parameter value(s) where knots are added Default:0.0                  Common
        flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.insertKnotSurface`
    """
    pass


def grid(*args, **kwargs):
    """
    This command changes the size and spacing of lines on the ground plane displayed
    in the perspective and orthographic views. This command lets you reset the
    ground plane, change its size and grid line spacing, grid subdivisions and
    display options. In query mode, return type is based on queried flag.
    
    Flags:
    - default : df                   (bool)          [query]
        Used to specify/query default values.
    
    - displayAxes : da               (bool)          [query]
        Specify true to display the grid axes.
    
    - displayAxesBold : dab          (bool)          [query]
        Specify true to accent the grid axes by drawing them with a thicker line.
    
    - displayDivisionLines : ddl     (bool)          [query]
        Specify true to display the subdivision lines between grid lines.
    
    - displayGridLines : dgl         (bool)          [query]
        Specify true to display the grid lines.
    
    - displayOrthographicLabels : dol (bool)          [query]
        Specify true to display the grid line numeric labels in the orthographic views.
    
    - displayPerspectiveLabels : dpl (bool)          [query]
        Specify true to display the grid line numeric labels in the perspective view.
    
    - divisions : d                  (int)           [query]
        Sets the number of subdivisions between major grid lines. The default is 5. If
        the spacing is 5 units, setting divisions to 5 will cause division lines to
        appear 1 unit apart.
    
    - orthographicLabelPosition : olp (unicode)       [query]
        The position of the grid's numeric labels in orthographic views. Valid values
        are    axisand edge.
    
    - perspectiveLabelPosition : plp (unicode)       [query]
        The position of the grid's numeric labels in perspective views. Valid values are
        axisand edge.
    
    - reset : r                      (bool)          []
        Resets the ground plane to its default values
    
    - size : s                       (float)         [query]
        Sets the size of the grid in linear units.  The default is 12 units.
    
    - spacing : sp                   (float)         [query]
        Sets the spacing between major grid lines in linear units. The default is 5
        units.
    
    - style : st                     (int)           [query]
        This flag is obsolete and should not be used.
    
    - toggle : tgl                   (bool)          [query]
        Turns the ground plane display off in all windows, including orthographic
        windows.  Default is true.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.grid`
    """
    pass


def polyMoveEdge(*args, **kwargs):
    """
    Modifies edges of a polygonal object. Translate, move, rotate or scale edges.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - gain : ga                      (float)         [create,query,edit]
        Gain factor per component. Can be painted using Artisan. Default:1.0
    
    - localCenter : lc               (int)           [create,query,edit]
        Local center on the edge : 0=Middle point, 1=Start point, 2=End point. Default:0
    
    - localDirection : ld            (float, float, float) [create,query,edit]
        Direction to determine X axis for local space. Default:1.0, 0.0, 0.0
    
    - localDirectionX : ldx          (float)         [create,query,edit]
        X coord of the X axis.
    
    - localDirectionY : ldy          (float)         [create,query,edit]
        Y coord of the X axis.
    
    - localDirectionZ : ldz          (float)         [create,query,edit]
        Z coord of the X axis.
    
    - localRotate : lr               (float, float, float) [create,query,edit]
        The local rotations. Default:0.0, 0.0, 0.0
    
    - localRotateX : lrx             (float)         [create,query,edit]
        Local rotate X coord. The range is [0, 360].
    
    - localRotateY : lry             (float)         [create,query,edit]
        Local rotate Y coord. The range is [0, 360].
    
    - localRotateZ : lrz             (float)         [create,query,edit]
        Local rotate Z coord : Rotation along the normal. The range is [0, 360].
    
    - localScale : ls                (float, float, float) [create,query,edit]
        Local Scale. Default:1.0, 1.0, 1.0
    
    - localScaleX : lsx              (float)         [create,query,edit]
        Scale X coord.
    
    - localScaleY : lsy              (float)         [create,query,edit]
        Scale Y coord.
    
    - localScaleZ : lsz              (float)         [create,query,edit]
        Scale Z coord.
    
    - localTranslate : lt            (float, float, float) [create,query,edit]
        Local translate. Default:0.0, 0.0, 0.0
    
    - localTranslateX : ltx          (float)         [create,query,edit]
        Local translation X coord.
    
    - localTranslateY : lty          (float)         [create,query,edit]
        Local translation Y coord.
    
    - localTranslateZ : ltz          (float)         [create,query,edit]
        Local translation Z coord : Move along the normal.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - pivot : pvt                    (float, float, float) [create,query,edit]
        The pivot for scaling and rotation. Default:0.0, 0.0, 0.0
    
    - pivotX : pvx                   (float)         [create,query,edit]
        Pivot X coord.
    
    - pivotY : pvy                   (float)         [create,query,edit]
        Pivot Y coord.
    
    - pivotZ : pvz                   (float)         [create,query,edit]
        Pivot Z coord.
    
    - random : ran                   (float)         [create,query,edit]
        Random value for all parameters. Default:0.0
    
    - rotate : ro                    (float, float, float) [create,query,edit]
        Rotation angles around X, Y, Z. Default:0.0, 0.0, 0.0
    
    - rotateX : rx                   (float)         [create,query,edit]
        Rotation angle around X.
    
    - rotateY : ry                   (float)         [create,query,edit]
        Rotation angle around Y.
    
    - rotateZ : rz                   (float)         [create,query,edit]
        Rotation angle around Z.
    
    - scale : s                      (float, float, float) [create,query,edit]
        Scaling vector. Default:1.0, 1.0, 1.0
    
    - scaleX : sx                    (float)         [create,query,edit]
        Scale X coord.
    
    - scaleY : sy                    (float)         [create,query,edit]
        Scale Y coord.
    
    - scaleZ : sz                    (float)         [create,query,edit]
        Scale Z coord.
    
    - translate : t                  (float, float, float) [create,query,edit]
        Translation vector. Default:0.0, 0.0, 0.0
    
    - translateX : tx                (float)         [create,query,edit]
        Translation X coord.
    
    - translateY : ty                (float)         [create,query,edit]
        Translation Y coord.
    
    - translateZ : tz                (float)         [create,query,edit]
        Translation Z coord.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMoveEdge`
    """
    pass


def bevelPlus(*args, **kwargs):
    """
    The bevelPlus command creates a new bevel surface for the specified curves using
    a given style curve. The first curve should be the outsidecurve, and the
    (optional) rest of them should be inside of the first one. For predictable
    results, the curves should be planar and all in the same plane.
    
    Flags:
    - bevelInside : bin              (bool)          [create,query,edit]
        If true, ensure surface always remains within the original profile curve
        Default:false
    
    - caching : cch                  (bool)          []
    
    - capSides : cap                 (int)           [create,query]
        How to cap the bevel. 1 - no caps2 - cap at start only3 - cap at end only4 - cap
        at start and endDefault:4
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - depth : d                      (float)         []
    
    - extrudeDepth : ed              (float)         []
    
    - frozen : fzn                   (bool)          []
    
    - innerStyle : innerStyle        (int)           [create,query,edit]
        Similar to outerStyle, this style is applied to all but the first (outer) curve
        specified.
    
    - joinSurfaces : js              (bool)          [create,query,edit]
        Attach bevelled surfaces into one surface for each input curve. Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           []
    
    - normalsOutwards : no           (bool)          [create,query,edit]
        If enabled, the normals point outwards on the resulting NURBS or poly surface.
    
    - numberOfSides : ns             (int)           [create,query,edit]
        How to apply the bevel. 1 - no bevels2 - bevel at start only3 - bevel at end
        only4 - bevel at start and endDefault:4
    
    - outerStyle : os                (int)           [create,query,edit]
        Choose a style to use for the bevel of the first (outer) curve.  There are 15
        predefined styles (values 0 to 14 can be used to select them). For those
        experienced with MEL, you can, after the fact, specify a custom curve and use it
        for the style curve. See the documentation for styleCurve node to see what
        requirements a style curve must satisfy.
    
    - polyOutChordHeight : cht       (float)         []
    
    - polyOutChordHeightRatio : chr  (float)         []
    
    - polyOutCount : poc             (int)           []
    
    - polyOutCurveSamples : pcs      (int)           []
    
    - polyOutCurveType : pct         (int)           []
    
    - polyOutExtrusionSamples : pes  (int)           []
    
    - polyOutExtrusionType : pet     (int)           []
    
    - polyOutMethod : pom            (int)           []
    
    - polyOutUseChordHeight : uch    (bool)          []
    
    - polyOutUseChordHeightRatio : ucr (bool)          []
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - tolerance : tol                (float)         []
    
    - width : w                      (float)         []
    
    
    Derived from mel command `maya.cmds.bevelPlus`
    """
    pass


def rebuildCurve(*args, **kwargs):
    """
    This command rebuilds a curve by modifying its parameterization. In some cases
    the shape may also change. The rebuildType (-rt) determines how the curve is to
    be rebuilt. The optional second curve can be used to specify a reference
    parameterization.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting curve 1 - linear, 2 - quadratic, 3 - cubic, 5 -
        quintic, 7 - heptic Default:3
    
    - endKnots : end                 (int)           [create,query,edit]
        End conditions for the curve 0 - uniform end knots, 1 - multiple end knots,
        Default:0
    
    - fitRebuild : fr                (bool)          [create,query,edit]
        If true use the least squares fit rebuild. Otherwise use the convert method.
        Default:true
    
    - frozen : fzn                   (bool)          []
    
    - keepControlPoints : kcp        (bool)          [create,query,edit]
        If true, the CVs will remain the same. This forces uniform parameterization
        unless rebuildType is matchKnots. Default:false
    
    - keepEndPoints : kep            (bool)          [create,query,edit]
        If true, keep the endpoints the same. Default:true
    
    - keepRange : kr                 (int)           [create,query,edit]
        Determine the parameterization for the resulting curve. 0 - reparameterize the
        resulting curve from 0 to 1, 1 - keep the original curve parameterization, 2 -
        reparameterize the result from 0 to number of spans Default:1
    
    - keepTangents : kt              (bool)          [create,query,edit]
        If true, keep the end tangents the same. Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.
    
    - rebuildType : rt               (int)           [create,query,edit]
        How to rebuild the input curve. 0 - uniform, 1 - reduce spans, 2 - match knots,
        3 - remove multiple knots, 4 - curvature 5 - rebuild ends 6 - clean Default:0
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - smartSurfaceCurveRebuild : scr (bool)          [create,query,edit]
        If true, curve on surface is rebuild in 3D and 2D info is kept Default:false
    
    - smooth : sm                    (float)         []
    
    - spans : s                      (int)           [create,query,edit]
        The number of spans in resulting curve Used only if rebuildType is uniform.
        Default:4
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to rebuild. Default:0.01                  Common flags
    
    
    Derived from mel command `maya.cmds.rebuildCurve`
    """
    pass


def surface(*args, **kwargs):
    """
    The cmd creates a NURBS spline surface (rational or non rational). The surface
    is created by specifying control vertices (CV's) and knot sequences in the U and
    V direction.  You cannot query the properties of the surface using this command.
    See examples below.
    
    Flags:
    - degreeU : du                   (int)           [create]
        Degree in surface U direction.  Default is degree 3.
    
    - degreeV : dv                   (int)           [create]
        Degree in surface V direction.  Default is degree 3.
    
    - formU : fu                     (unicode)       [create]
        The string for open is open, for closed is closedor for periodic is periodicin
        U.
    
    - formV : fv                     (unicode)       [create]
        The string for open is open, for closed is closedor for periodic is periodicin
        V.
    
    - knotU : ku                     (float)         [create]
        Knot value(s) in U direction.  One flag per knot value. There must be
        (numberOfPointsInU + degreeInU - 1) knots and the knot vector must be non-
        decreasing.
    
    - knotV : kv                     (float)         [create]
        Knot value(s) in V direction.  One flag per knot value. There must be
        (numberOfPointsInV + degreeInV - 1) knots and the knot vector must be non-
        decreasing.
    
    - name : n                       (unicode)       [create]
        Name to use for new transforms.
    
    - objectSpace : ob               (bool)          [create]
        Should the operation happen in objectSpace?
    
    - point : p                      (float, float, float) [create]
        To specify non rational CV with (x, y, z) values.  linearmeans that this flag
        can take values with units.  Note that you must specify (degree+1) surface
        points in any direction to create a visible surface span.  eg.  if the surface
        is degree 3 in the U direction, you must specify 4 CVs in the U direction.
        Points are specified in rows of U and columns of V.  If you want to incorporate
        units, add the unit name to the value, eg. -p 3.3in 5.5ft 6.6yd
    
    - pointWeight : pw               (float, float, float, float) [create]
        To specify rational CV with (x, y, z, w) values.  linearmeans that this flag can
        take values with units.  Note that you must specify (degree+1) surface points in
        any direction to create a visible surface span.  eg.  if the surface is degree 3
        in the U direction, you must specify 4 CVs in the U direction. Points are
        specified in rows of U and columns of V.
    
    - worldSpace : ws                (bool)          [create]
        Should the operation happen in worldSpace?                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.surface`
    """
    pass


def polyBridgeEdge(*args, **kwargs):
    """
    Bridges two sets of edges.
    
    Flags:
    - bridgeOffset : bo              (int)           [create,query,edit]
        Add offset to which vertices are connected. Default:0
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - curveType : ctp                (int)           [create,query,edit]
        Format: 0 - Linear, 1 - Blend, 2 - Curve Default:TdnpolyBridgeEdge::Linear
    
    - direction : d                  (int)           []
    
    - divisions : dv                 (int)           [create,query,edit]
        The number of subdivisions in the bridging faces (resulting in (divisions+1) row
        of faces). Default:1
    
    - frozen : fzn                   (bool)          []
    
    - inputCurve : inc               (PyNode)        [create]
        This flag specifies the name of the curve to be used as input for the operation.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - reverse : rev                  (bool)          []
    
    - smoothingAngle : sma           (float)         [create,query,edit]
        Angle below which new edges will be smoothed Default:kPi/6.0
    
    - sourceDirection : sd           (int)           []
    
    - startVert1 : sv1               (int)           [create,query,edit]
        The start vertex from the first set of edges Default:-1
    
    - startVert2 : sv2               (int)           [create,query,edit]
        The start vertex from the second set of edges Default:-1
    
    - taper : tp                     (float)         [create,query,edit]
        Taper or Scale along the extrusion path Default:1.0
    
    - taperCurve_FloatValue : cfv    (float)         [create,query,edit]
        Value for taperCurve; Curve control for taper along extrusion Using this curve,
        the taper along extrusion can be changed from a simple linear scaling to custom
        scaling along the extrusion path.
    
    - taperCurve_Interp : ci         (int)           [create,query,edit]
        Interpolation type for taperCurve; Curve control for taper along extrusion Using
        this curve, the taper along extrusion can be changed from a simple linear
        scaling to custom scaling along the extrusion path.
    
    - taperCurve_Position : cp       (float)         [create,query,edit]
        Position for taperCurve; Curve control for taper along extrusion Using this
        curve, the taper along extrusion can be changed from a simple linear scaling to
        custom scaling along the extrusion path.
    
    - targetDirection : td           (int)           []
    
    - twist : twt                    (float)         [create,query,edit]
        Twist or Rotation along the extrusion path Default:0.0
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyBridgeEdge`
    """
    pass


def polyCircularize(*args, **kwargs):
    """
    Mirror all the faces of the selected object.
    
    Flags:
    - alignment : al                 (int)           [create,query,edit]
        How the circle should be  oriented relative to the surface Default:0
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createCurve : cc               (bool)          [create]
        If true then the operation can create a curve.
    
    - divisions : d                  (int)           []
    
    - evenlyDistribute : ed          (bool)          [create,query,edit]
        Should the point be evenly distributed around the circle Default:true
    
    - frozen : fzn                   (bool)          []
    
    - inputCurve : inc               (PyNode)        [create]
        This flag specifies the name of the curve to be used as input for the operation.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - normalOffset : no              (float)         []
    
    - normalOrientation : nor        (int)           [create,query,edit]
        What calculation to use to get circle plane normal Default:0
    
    - radialOffset : ro              (float)         [create,query,edit]
        The amount the circle points should be translated along radius Default:0.0
    
    - relaxInterior : ri             (float)         []
    
    - smoothingAngle : sa            (float)         [create,query,edit]
        The angle that decides which resulting faces are hard or soft Default:30.0
    
    - supportingEdges : se           (int)           []
    
    - twist : t                      (float)         []
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCircularize`
    """
    pass


def polyEditEdgeFlow(*args, **kwargs):
    """
    Edit edges of a polygonal object to respect surface curvature.
    
    Flags:
    - adjustEdgeFlow : aef           (float)         [create]
        The weight value of the edge vertices to be positioned. 0: Concave 0:  Middle
        point 1:  Surface continuity 1: Convex Default is 1.0
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - edgeFlow : ef                  (bool)          [create]
        True to enable edge flow. Otherwise, the edge flow is disabled. Default is true.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyEditEdgeFlow`
    """
    pass


def polyCrease(*args, **kwargs):
    """
    Command to set the crease values on the edges or vertices of a poly.  The crease
    values are used by the smoothing algorithm.
    
    Flags:
    - createHistory : ch             (bool)          [create,query,edit]
        For objects that have no construction history, this flag can be used to force
        the creation of construction history for creasing.  By default, history is not
        created if the object has no history.  Regardless of this flag, history is
        always created if the object already has history.
    
    - operation : op                 (int)           [create,query,edit]
        Operation to perform.  Valid values are: 0: Crease the specified components. 1:
        Remove the crease values for the specified components. 2: Remove all crease
        values from the mesh. Default is 0.
    
    - relativeValue : rv             (float)         [create,query,edit]
        Specifies a new relative value for all selected vertex and edge components. This
        flag can not be used at the same time as either the value or vertexValue flags.
    
    - value : v                      (float)         [create,query,edit]
        Specifies the crease value for the selected edge components. When specified
        multiple times, the values are assigned respectively to the specified edges.
    
    - vertexValue : vv               (float)         [create,query,edit]
        Specifies the crease value for the selected vertex components. When specified
        multiple times, the values are assigned respectively to the specified vertices.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCrease`
    """
    pass


def nurbsToSubdiv(*args, **kwargs):
    """
    This command converts a NURBS surface and produces a subd surface. The name of
    the new subdivision surface is returned. If construction history is ON, then the
    name of the new dependency node is returned as well.
    
    Flags:
    - addUnderTransform : aut        (bool)          [create,query,edit]
        Specify whether the new surface should be added under the old transform or not.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - collapsePoles : cp             (bool)          [create,query,edit]
        Collapse poles into a single point Default:false
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - matchPeriodic : mp             (bool)          [create,query,edit]
        Match periodic surface texture mapping in the result. Default:false
    
    - maxPolyCount : mpc             (int)           [create,query,edit]
        The maximum number of base mesh faces in the resulting subdivision surface.
        Default:1000
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - reverseNormal : rn             (bool)          [create,query,edit]
        Reverse the NURBS surface normal in the conversion. Default:true
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.nurbsToSubdiv`
    """
    pass


def attachSurface(*args, **kwargs):
    """
    This attach command is used to attach surfaces. Once the surfaces are attached,
    there will be multiple knots at the joined point(s). These can be kept or
    removed if the user wishes. The end of the first surface is attached to the
    start of the second surface in the specified direction. Note: if the command is
    done with Keep Original off there will be an extra surface in the model (the
    second surface). The command does not delete it. The first surface is replaced
    by the attached surface.
    
    Flags:
    - blendBias : bb                 (float)         [create,query,edit]
        Skew the result toward the first or the second curve depending on the blend
        factory being smaller or larger than 0.5. Default:0.5
    
    - blendKnotInsertion : bki       (bool)          [create,query,edit]
        If set to true, insert a knot in one of the original curves (relative position
        given by the parameter attribute below) in order to produce a slightly different
        effect. Default:false
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - directionU : du                (bool)          [create,query,edit]
        If true attach in U direction of surface and V direction otherwise. Default:true
    
    - frozen : fzn                   (bool)          []
    
    - keepMultipleKnots : kmk        (bool)          [create,query,edit]
        If true, keep multiple knots at the join parameter. Otherwise remove them.
        Default:true
    
    - method : m                     (int)           [create,query,edit]
        Attach method (connect-0, blend-1) Default:0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        The parameter value for the positioning of the newly inserted knot. Default:0.1
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - reverse1 : rv1                 (bool)          [create,query,edit]
        If true, reverse the direction (specified by directionU) of the first input
        surface before doing attach. Otherwise, do nothing to the first input surface
        before attaching. NOTE: setting this attribute to random values will cause
        unpredictable results and is not supported. Default:false
    
    - reverse2 : rv2                 (bool)          [create,query,edit]
        If true, reverse the direction (specified by directionU) of the second input
        surface before doing attach. Otherwise, do nothing to the second input surface
        before attaching. NOTE: setting this attribute to random values will cause
        unpredictable results and is not supported. Default:false
    
    - swap1 : sw1                    (bool)          [create,query,edit]
        If true, swap the UV directions of the first input surface before doing attach.
        Otherwise, do nothing to the first input surface before attaching. NOTE: setting
        this attribute to random values will cause unpredictable results and is not
        supported. Default:false
    
    - swap2 : sw2                    (bool)          [create,query,edit]
        If true, swap the UV directions of the second input surface before doing attach.
        Otherwise, do nothing to the second input surface before attaching. NOTE:
        setting this attribute to random values will cause unpredictable results and is
        not supported. Default:false
    
    - twist : tw                     (bool)          [create,query,edit]
        If true, reverse the second surface in the opposite direction (specified by
        directionU) before doing attach. This will avoid twists in the attached
        surfaces. Otherwise, do nothing to the second input surface before attaching.
        NOTE: setting this attribute to random values will cause unpredictable results
        and is not supported. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.attachSurface`
    """
    pass


def _surface(*args, **kwargs):
    """
    Maya Bug Fix:
      - name parameter only applied to transform. now applies to shape as well
    """
    pass


def polyFlipUV(*args, **kwargs):
    """
    Flip (mirror) the UVs (in texture space) of input polyFaces, about either the U
    or V axis..
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createNewMap : cm              (bool)          [create]
        Set to true if a new map should be created
    
    - cutUV : cut                    (bool)          [create,query,edit]
        Cut UV edges when flipping some components on a UV shell C: Default is on. Q:
        When queried, returns an int.
    
    - flipType : ft                  (int)           [create,query,edit]
        Flip along U or V direction. 0Horizontal1VerticalC: Default is 0. Q: When
        queried, returns an int.
    
    - frozen : fzn                   (bool)          []
    
    - insertBeforeDeformers : ibd    (bool)          [create]
        Set to true if the new node created should inserted before any deformer nodes.
    
    - local : l                      (bool)          [create,query,edit]
        Flips in the local space of the input faces. C: Default is on. Q: When queried,
        returns an int.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - pivotU : pu                    (float)         [create,query,edit]
        Specifies the pivot value, in the U direction.
    
    - pivotV : pv                    (float)         [create,query,edit]
        Specifies the pivot value, in the V direction.
    
    - usePivot : up                  (bool)          [create,query,edit]
        Flip using pivot or not. C: Default is off. Q: When queried, returns an int.
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyFlipUV`
    """
    pass


def polyMoveVertex(*args, **kwargs):
    """
    Modifies vertices of a polygonal object. Translate, rotate or scale vertices in
    local or world space.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - gain : ga                      (float)         [create,query,edit]
        Gain factor per component. Can be painted using Artisan. Default:1.0
    
    - localDirection : ld            (float, float, float) [create,query,edit]
        Direction to determine X axis for local space. Default:1.0, 0.0, 0.0
    
    - localDirectionX : ldx          (float)         [create,query,edit]
        X coord of the X axis.
    
    - localDirectionY : ldy          (float)         [create,query,edit]
        Y coord of the X axis.
    
    - localDirectionZ : ldz          (float)         [create,query,edit]
        Z coord of the X axis.
    
    - localTranslate : lt            (float, float, float) [create,query,edit]
        Local translate. Default:0.0, 0.0, 0.0
    
    - localTranslateX : ltx          (float)         [create,query,edit]
        Local translation X coord.
    
    - localTranslateY : lty          (float)         [create,query,edit]
        Local translation Y coord.
    
    - localTranslateZ : ltz          (float)         [create,query,edit]
        Local translation Z coord : Move along the normal.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - pivot : pvt                    (float, float, float) [create,query,edit]
        The pivot for scaling and rotation. Default:0.0, 0.0, 0.0
    
    - pivotX : pvx                   (float)         [create,query,edit]
        Pivot X coord.
    
    - pivotY : pvy                   (float)         [create,query,edit]
        Pivot Y coord.
    
    - pivotZ : pvz                   (float)         [create,query,edit]
        Pivot Z coord.
    
    - random : ran                   (float)         [create,query,edit]
        Random value for all parameters. Default:0.0
    
    - rotate : ro                    (float, float, float) [create,query,edit]
        Rotation angles around X, Y, Z. Default:0.0, 0.0, 0.0
    
    - rotateX : rx                   (float)         [create,query,edit]
        Rotation angle around X.
    
    - rotateY : ry                   (float)         [create,query,edit]
        Rotation angle around Y.
    
    - rotateZ : rz                   (float)         [create,query,edit]
        Rotation angle around Z.
    
    - scale : s                      (float, float, float) [create,query,edit]
        Scaling vector. Default:1.0, 1.0, 1.0
    
    - scaleX : sx                    (float)         [create,query,edit]
        Scale X coord.
    
    - scaleY : sy                    (float)         [create,query,edit]
        Scale Y coord.
    
    - scaleZ : sz                    (float)         [create,query,edit]
        Scale Z coord.
    
    - translate : t                  (float, float, float) [create,query,edit]
        Translation vector. Default:0.0, 0.0, 0.0
    
    - translateX : tx                (float)         [create,query,edit]
        Translation X coord.
    
    - translateY : ty                (float)         [create,query,edit]
        Translation Y coord.
    
    - translateZ : tz                (float)         [create,query,edit]
        Translation Z coord.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMoveVertex`
    """
    pass


def polyMapDel(*args, **kwargs):
    """
    Deletes texture coordinates (UVs) from selected faces.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMapDel`
    """
    pass


def extendSurface(*args, **kwargs):
    """
    This command extends a surface or creates a new surface as an extension.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - distance : d                   (float)         [create,query,edit]
        The distance to extend (for by distance only) Default:1
    
    - extendDirection : ed           (int)           [create,query,edit]
        Which parametric direction of the surface to extend ( 0 - U, 1 - V, 2 - both )
        Default:0
    
    - extendMethod : em              (int)           [create,query,edit]
        The extend method (0 - distance) Default:0
    
    - extendSide : es                (int)           [create,query,edit]
        Which end of the surface to extend ( 0 - end, 1 - start, 2 - both ) Default:1
    
    - extensionType : et             (int)           [create,query,edit]
        The type of extension (0 - tangent, 2 - extrapolate) Default:0
    
    - frozen : fzn                   (bool)          []
    
    - join : jn                      (bool)          [create,query,edit]
        Join extension to original Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.extendSurface`
    """
    pass


def polyTransfer(*args, **kwargs):
    """
    Transfer information from one polygonal object to another one. Both objects must
    have identical topology, that is same vertex, edge, and face numbering. The
    flags specify which of the vertices, UV sets or vertex colors will be copied.
    
    Flags:
    - alternateObject : ao           (unicode)       [create,query,edit]
        Name of the alternate object.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - uvSets : uv                    (bool)          [create,query,edit]
        When true, the UV sets are copied from the alternate object. C: Default is on.
    
    - vertexColor : vc               (bool)          [create,query,edit]
        When true, the colors per vertex are copied from the alternate object. C:
        Default is off.
    
    - vertices : v                   (bool)          [create,query,edit]
        When true, the vertices positions are copied from the alternate object. C:
        Default is off.                  Flag can have multiple arguments, passed either
        as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyTransfer`
    """
    pass


def polyPlane(*args, **kwargs):
    """
    Create a new polygonal plane.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the plane.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize and Preserve Aspect
        RatioDefault:1
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - height : h                     (float)         [create,query,edit]
        Height of the plane. Default:1.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height of the sphere.
    
    - subdivisionsWidth : sw         (int)           [create,query,edit]
        Subdivisions along the width of the plane. Default:10
    
    - subdivisionsX : sx             (int)           [create,query,edit]
        This specifies the number of subdivisions in the X direction for the plane.
        Default is 5.
    
    - subdivisionsY : sy             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Y direction for the plane.
        Default is 5.
    
    - texture : tx                   (int)           [create,query,edit]
        What texture mechanism to be applied. 0=No textures; 1=stretch to fit;
        2=preserve aspect ratio Default:1
    
    - width : w                      (float)         [create,query,edit]
        Width of the plane. Default:1.0                  Common poly creation operation
        flags
    
    
    Derived from mel command `maya.cmds.polyPlane`
    """
    pass


def smoothCurve(*args, **kwargs):
    """
    The smooth command smooths the curve at the given control points.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - smoothness : s                 (float)         [create,query,edit]
        smoothness factor Default:10.0                  Common flags
    
    
    Derived from mel command `maya.cmds.smoothCurve`
    """
    pass


def projectCurve(*args, **kwargs):
    """
    The projectCurve command creates curves on surface where all selected curves
    project onto the selected surfaces. Projection can be done using the surface
    normals or the user can specify the vector to project along. Note: the user does
    not have to specify the curves and surfaces in any particular order in the
    command line.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - direction : d                  (float, float, float) [create,query,edit]
        Direction of projection. Available only if useNormal is false.
    
    - directionX : dx                (float)         [create,query,edit]
        X direction of projection. Default:0.0
    
    - directionY : dy                (float)         [create,query,edit]
        Y direction of projection. Default:0.0
    
    - directionZ : dz                (float)         [create,query,edit]
        Z direction of projection. Default:1.0
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - tolerance : tol                (float)         [create,query,edit]
        Tolerance to fit to. Default:0.01
    
    - useNormal : un                 (bool)          [create,query,edit]
        True if the surface normal is to be used and false if the direction vector
        should be used instead. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.projectCurve`
    """
    pass


def closeSurface(*args, **kwargs):
    """
    The closeSurface command closes a surface in the U, V, or both directions,
    making it periodic. The close direction is controlled by the direction flag. If
    a surface is not specified in the command, then the first selected surface will
    be used. The pathname to the newly closed surface and the name of the resulting
    dependency node are returned. This command also handles selected surface
    isoparms. For example, if an isoparm is specified, surface1.u[0.33], then the
    surface will be closed in V, regardless of the direction flag.
    
    Flags:
    - blendBias : bb                 (float)         [create,query,edit]
        Skew the result toward the first or the second surface depending on the blend
        value being smaller or larger than 0.5. Default:0.5
    
    - blendKnotInsertion : bki       (bool)          [create,query,edit]
        If set to true, insert a knot in one of the original surfaces (relative position
        given by the parameter attribute below) in order to produce a slightly different
        effect. Default:false
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - direction : d                  (int)           [create,query,edit]
        The direction in which to close: 0 - U, 1 - V, 2 - Both U and V Default:0
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        The parameter value for the positioning of the newly inserted knot. Default:0.1
    
    - preserveShape : ps             (int)           [create,query,edit]
        0 - without preserving the shape 1 - preserve shape 2 - blend Default:1
        Common flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.closeSurface`
    """
    pass


def polyPyramid(*args, **kwargs):
    """
    The pyramid command creates a new polygonal pyramid.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the pyramid. Q: When
        queried, this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize3: Normalize and
        Preserve Aspect RatioDefault:2
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - numberOfSides : ns             (int)           [create,query,edit]
        Number of sides of Pyramid. Default:4
    
    - numderOfSides : nsi            (int)           [create,query,edit]
        Number of sides of Pyramid. Default:4
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - sideLength : w                 (float)         [create,query,edit]
        Side length of the Pyramid. Default:1.0
    
    - subdivisionsCaps : sc          (int)           [create,query,edit]
        Subdivisions on bottom cap Default:0
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height. Default:1
    
    - texture : tx                   (bool)          [create,query,edit]
        Apply texture or not. Default:true                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyPyramid`
    """
    pass


def polyDelVertex(*args, **kwargs):
    """
    Deletes vertices. Joins two edges which have a common vertex. The vertices must
    be connected to exactly two edges (so-called winged).
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyDelVertex`
    """
    pass


def polyPipe(*args, **kwargs):
    """
    The polyPipe command creates a new polygonal pipe.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the pipe. Q: When queried,
        this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (bool)          [create,query,edit]
        Create UVs or not. Default:true
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - height : h                     (float)         [create,query,edit]
        Height of the pipe. Default:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - radius : r                     (float)         [create,query,edit]
        Radius of the pipe. Default:1.0
    
    - roundCap : rcp                 (bool)          [create,query,edit]
        To indicate whether we need a round cap Default:false
    
    - subdivisionsAxis : sa          (int)           [create,query,edit]
        Subdivisions around the axis. Default:20
    
    - subdivisionsCaps : sc          (int)           [create,query,edit]
        Subdivisions along the thickness caps. Default:1
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height. Default:1
    
    - texture : tx                   (bool)          [create,query,edit]
        Apply texture or not. this is an old attribute. This is unsupported and would be
        removed in a future release. Default:true
    
    - thickness : t                  (float)         [create,query,edit]
        Thickness of the pipe. Default:0.5                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyPipe`
    """
    pass


def arclen(*args, **kwargs):
    """
    This command returns the arclength of a curve if the history flag is not set
    (the default).  If the history flag is set, a node is created that can produce
    the arclength, and is connected and its name returned.  Having the construction
    history option on makes this command useful for expressions.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.arclen`
    """
    pass


def polyHelix(*args, **kwargs):
    """
    The polyHelix command creates a new polygonal helix.
    
    Flags:
    - axis : ax                      (float, float, float) [query,edit]
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - coils : c                      (float)         [create,query,edit]
        Number of coils. Default:3
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize3: Normalize and
        Preserve Aspect RatioDefault:2
    
    - direction : d                  (int)           [create,query,edit]
        What should be the direction of the coil. 0=Clockwise; 1=Counterclockwise
        Default:1
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - height : h                     (float)         [create,query,edit]
        Height of the helix. Default:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - radius : r                     (float)         [create,query,edit]
        Radius of tube. Default:0.4
    
    - roundCap : rcp                 (bool)          [create,query,edit]
        To indicate whether we need a round cap Default:false
    
    - subdivisionsAxis : sa          (int)           [create,query,edit]
        Subdivisions around the axis. Default:8
    
    - subdivisionsCaps : sc          (int)           [create,query,edit]
        Subdivisions along the thickness caps. Default:0
    
    - subdivisionsCoil : sco         (int)           [create,query,edit]
        Subdivisions along the coil. Default:50
    
    - texture : tx                   (int)           [create,query,edit]
        What texture mechanism to be applied 0=No textures; 1=Object; 2=Faces Default:2
    
    - useOldInitBehaviour : oib      (bool)          [create,query,edit]
        Create the helix with base on the origin as in Maya V8.0 and below Otherwise
        create helix centred at origin Default:false
    
    - width : w                      (float)         [create,query,edit]
        Width of the helix. Default:2.0                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyHelix`
    """
    pass


def nurbsPlane(*args, **kwargs):
    """
    The nurbsPlane command creates a new NURBS Plane and return the name of the new
    surface. It creates an unit plane with center at origin by default.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        The primitive's axis
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface 1 - linear, 2 - quadratic, 3 - cubic, 5 -
        quintic, 7 - heptic Default:3
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - lengthRatio : lr               (float)         [create,query,edit]
        The ratio of lengthto widthof the plane. Default:1.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - patchesU : u                   (int)           [create,query,edit]
        The number of spans in the U direction. Default:1
    
    - patchesV : v                   (int)           [create,query,edit]
        The number of spans in the V direction. Default:1
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The primitive's pivot point
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    - width : w                      (float)         [create,query,edit]
        The width of the plane Default:1.0                  Common flags
    
    
    Derived from mel command `maya.cmds.nurbsPlane`
    """
    pass


def polyMoveUV(*args, **kwargs):
    """
    Moves selected UV coordinates in 2D space. As the selected UVs are adjusted, the
    way the image is mapped onto the object changes accordingly. This command
    manipulates the UV values without changing the 3D geometry of the object.
    
    Flags:
    - axisLen : l                    (float, float)  [create,query,edit]
        AxisLen vector, used to draw the manip handles. Default:1.0, 1.0
    
    - axisLenX : lx                  (float)         [create,query,edit]
        AxisLen X coord.
    
    - axisLenY : ly                  (float)         [create,query,edit]
        AxisLen Y coord.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - pivot : pvt                    (float, float)  [create,query,edit]
        The pivot for scaling and rotation. Default:0.5, 0.5
    
    - pivotU : pvu                   (float)         [create,query,edit]
        Pivot U coord.
    
    - pivotV : pvv                   (float)         [create,query,edit]
        Pivot V coord.
    
    - random : ran                   (float)         [create,query,edit]
        Random value, added to all parameters. Default:0.0
    
    - rotationAngle : ra             (float)         [create,query,edit]
        Angle of rotation. Default:0.0
    
    - scale : s                      (float, float)  [create,query,edit]
        Scaling vector. Default:1.0, 1.0
    
    - scaleU : su                    (float)         [create,query,edit]
        Scaling U coord.
    
    - scaleV : sv                    (float)         [create,query,edit]
        Scaling V coord.
    
    - translate : t                  (float, float)  [create,query,edit]
        Translation vector. Default:0.0, 0.0
    
    - translateU : tu                (float)         [create,query,edit]
        Translation U coord.
    
    - translateV : tv                (float)         [create,query,edit]
        Translation V coord.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMoveUV`
    """
    pass


def polyCopyUV(*args, **kwargs):
    """
    Copy some UVs from a UV set into another.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createNewMap : cm              (bool)          [create]
        Set to true if a new map should be created
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - uvSetNameInput : uvi           (unicode)       [create,query,edit]
        Specifies name of the input uv set to read the UV description from. Default is
        the current UV set.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCopyUV`
    """
    pass


def polySphere(*args, **kwargs):
    """
    The sphere command creates a new polygonal sphere.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the sphere. Q: When
        queried, this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create]
        This flag alows a specific UV mechanism to be selected, while creating the
        sphere. The valid values are 0, 1, or 2. 0 implies that no UVs will be generated
        (No texture to be applied). 1 implies UVs are created with pinched at poles 2
        implies UVs are created with sawtooth at poles For better understanding of these
        options, you may have to open the texture view windowC: Default is 2
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - radius : r                     (float)         [create,query,edit]
        This flag specifies the radius of the sphere. C: Default is 0.5. Q: When
        queried, this flag returns a float.
    
    - subdivisionsAxis : sa          (int)           [create,query,edit]
        Subdivisions around the axis.
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height of the sphere.
    
    - subdivisionsX : sx             (int)           [create,query,edit]
        This specifies the number of subdivisions in the X direction for the sphere. C:
        Default is 20. Q: When queried, this flag returns an int.
    
    - subdivisionsY : sy             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Y direction for the
        sphere. C: Default is 20. Q: When queried, this flag returns an int.
    
    - texture : tx                   (int)           [create]
        This flag is obsolete and will be removed in the next release. The
        -cuv/createUVs flag should be used instead.                  Common poly
        creation operation flags
    
    
    Derived from mel command `maya.cmds.polySphere`
    """
    pass


def projectTangent(*args, **kwargs):
    """
    The project tangent command is used to align (for tangents) a curve to two other
    curves or a surface. A surface isoparm may be selected to define the direction
    (U or V) to align to. The end of the curve must intersect with these other
    objects. Curvature continuity may also be applied if required. Tangent
    continuity means the end of the curve is modified to be tangent at the point it
    meets the other objects. Curvature continuity means the end of the curve is
    modified to be curvature continuous as well as tangent. If the normal tangent
    direction is used, the curvature continuity and rotation do not apply. Also,
    curvature continuity is only available if align to a surface (not with 2
    curves).
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curvature : c                  (bool)          [create,query,edit]
        Curvature continuity is on if true and off otherwise. Default:false
    
    - curvatureScale : cs            (float)         [create,query,edit]
        Curvature scale applied to curvature of curve to align. Available if curvature
        option is true. Default:0.0
    
    - frozen : fzn                   (bool)          []
    
    - ignoreEdges : ie               (bool)          [create,query,edit]
        If false, use the tangents of the trim edge curves if the surface is trimmed. If
        true, use the tangents of the underlying surface in the U/V directions.
        Default:false
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - reverseTangent : rt            (bool)          [create,query,edit]
        Reverse the tangent direction if true and leave it the way it is if false.
        Default:false
    
    - rotate : ro                    (float)         [create,query,edit]
        Amount by which the tangent of the curve to align will be rotated. Available
        only if the normal direction (3) is not used for tangentDirection. Default:0.0
    
    - tangentDirection : td          (int)           [create,query,edit]
        Tangent align direction type legal values: 1=u direction (of surface or use
        first curve), 2=v direction (of surface or use second curve), 3=normal direction
        (at point of intersection). Default:1
    
    - tangentScale : ts              (float)         [create,query,edit]
        Tangent scale applied to tangent of curve to align. Default:1.0
        Common flags
    
    
    Derived from mel command `maya.cmds.projectTangent`
    """
    pass


def polyCloseBorder(*args, **kwargs):
    """
    Closes open borders of objects. For each border edge given, a face is created to
    fill the hole the edge lies on.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCloseBorder`
    """
    pass


def subdiv(*args, **kwargs):
    """
    Provides useful information about the selected subdiv or components, such as the
    deepest subdivided level, the children or parents of the currently selected
    components, etc.            In query mode, return type is based on queried flag.
    
    Flags:
    - currentLevel : cl              (bool)          [create,query]
        When queried, this flag returns an integer representing the level of the
        currently selected subdiv surface component(s). Returns -1, if there are more
        than one level of CVs are selected, (even if they are from different objects)
        Returns -2, if there are no input subdiv CVs to process.
    
    - currentSubdLevel : csl         (bool)          [create,query]
        When queried, this flag returns an integer representing the level of the
        currently selected subdiv surface, regardless of whether components are selected
        or not. Returns -2, if there are no input subdiv CVs to process.
    
    - deepestLevel : dl              (int)           [create,query]
        When queried, this flag returns an integer representing the deepest level to
        which the queried subdiv surface has been subdivided.
    
    - displayLoad : dsl              (bool)          [create,query]
        When queried, this flag prints the display load of selected subdiv
    
    - edgeStats : est                (bool)          [create,query]
        When queried, this flag prints stats on the current subd.
    
    - faceStats : fst                (bool)          [create,query]
        When queried, this flag prints stats on the current subd.
    
    - maxPossibleLevel : mpl         (int)           [create,query]
        When queried, this flag returns an integer representing the maximum possible
        level to which the queried subdiv surface can been subdivided.
    
    - proxyMode : pm                 (int)           [create,query]
        When queried, this flag returns an integer representing whether or not the
        subdivision surface is in polygon proxymode. Proxymode allows the base mesh of a
        subdivision surface without construction history to be edited using the
        polygonal editing tools. Returns 1, if the subdivision surface is in polygon
        proxymode. Returns 0, if the surface is not currently in proxymode, but could be
        put into proxymode since it has no construction history.  (This state is also
        known as standardmode.) Returns 2, if the surface is not in proxymode and cannot
        be put into proxy mode, as it has construction history.
    
    - smallOffsets : so              (bool)          [create,query]
        When queried, this flag prints the number of subdiv vertices in the hierarchy
        that have a small enough offset so that the vertex is not required
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.subdiv`
    """
    pass


def polyBlindData(*args, **kwargs):
    """
    Command creates blindData types (basically creates an instance of
    TdnPolyBlindData). When used with the query flag, it returns the data types that
    define this blindData type. This command is to be used create a blindData node
    \*and\* to edit the same.. The associationType flag \*has\* to be specified at
    all times.. This is because if an instance of the specified BD typeId exists in
    the history chain but if the associationType is not the same, then a new
    polyBlindData node is created.. For object level blind data, only the object
    itself must be specified. A new compound attribute BlindDataNNNN will be created
    on the object. Blind data attribute names must be unique across types for object
    level blind data. So, the command will require the following to be specified:
    - typeId,     - associationType     - longDataName or shortDataName of data
    being edited.     - The actual data being specified.     - The components that
    this data is to be attached to.
    
    Flags:
    - associationType : at           (unicode)       [create,edit]
        Specifies the dataTypes that are part of BlindData node being created. Allowable
        associations are objectfor any object, and vertexedgeand facefor mesh objects.
        Other associations for other geometry types may be added.
    
    - binaryData : bnd               (unicode)       [create,edit]
        Specifies the data type is a binary data value
    
    - booleanData : bd               (bool)          [create,edit]
        Specifies the data type is a boolean logic value
    
    - delete : delete                (bool)          [create,edit]
        Specifies that this will remove the blind data if found
    
    - doubleData : dbd               (float)         [create,edit]
        Specifies the data type is a floating point double value
    
    - int64Data : lid                (int)           [create,edit]
        Specifies the data type is an 64-bit integer value
    
    - intData : ind                  (int)           [create,edit]
        Specifies the data type is an integer value
    
    - longDataName : ldn             (unicode)       [create,edit]
        Specifies the long name of the data that is being modified by this command.
    
    - rescan : res                   (bool)          [create,edit]
        Enables a rescan of blind data nodes for cached information
    
    - reset : rst                    (bool)          [create,edit]
        Specifies that this command will reset the given attribute to default value
    
    - shape : sh                     (bool)          [create,edit]
        For object association only, apply blind data to the shape(s) below this node
        instead of the node itself
    
    - shortDataName : sdn            (unicode)       [create,edit]
        Specifies the short name of the data that is being modified by this command.
    
    - stringData : sd                (unicode)       [create,edit]
        Specifies the data type is a string value
    
    - typeId : id                    (int)           [create,edit]
        Specifies the typeId of the BlindData type being created
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyBlindData`
    """
    pass


def alignSurface(*args, **kwargs):
    """
    The surface align command is used to align surfaces in maya. The main alignment
    options are positional, tangent and curvature continuity. Curvature continuity
    implies tangent continuity. NOTE: this tool is based on Studio's align tool.
    Positional continuity means the surfaces (move) or the ends of the surfaces
    (modify) are changed. Tangent continuity means one of the surfaces is modified
    to be tangent at the points where they meet. Curvature continuity means one of
    the surfaces is modified to be curvature continuous as well as tangent. The
    default behaviour, when no surfaces or flags are passed, is to only do
    positional and tangent continuity on the active list with the end of the first
    surface and the start of the other surface used for alignment.
    
    Flags:
    - attach : at                    (bool)          [create]
        Should surfaces be attached after alignment?
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curvatureContinuity : cc       (bool)          [create,query,edit]
        Curvature continuity is on if true and off otherwise. Default:false
    
    - curvatureScale1 : cs1          (float)         [create,query,edit]
        Curvature scale applied to curvature of first surface for curvature continuity.
        Default:0.0
    
    - curvatureScale2 : cs2          (float)         [create,query,edit]
        Curvature scale applied to curvature of second surface for curvature continuity.
        Default:0.0
    
    - directionU : du                (bool)          [create,query,edit]
        If true use U direction of surface and V direction otherwise. Default:true
    
    - frozen : fzn                   (bool)          []
    
    - joinParameter : jnp            (float)         [create,query,edit]
        Parameter on reference surface where modified surface is to be aligned to.
        Default:123456.0
    
    - keepMultipleKnots : kmk        (bool)          [create]
        Should multiple knots be kept?
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - positionalContinuity : pc      (bool)          [create,query,edit]
        Positional continuity is on if true and off otherwise. Default:true
    
    - positionalContinuityType : pct (int)           [create,query,edit]
        Positional continuity type legal values: 1 - move first surface, 2 - move second
        surface, 3 - move both surfaces, 4 - modify first surface, 5 - modify second
        surface, 6 - modify both surfaces Default:1
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - reverse1 : rv1                 (bool)          [create,query,edit]
        If true, reverse the direction (specified by directionU) of the first input
        surface before doing align. Otherwise, do nothing to the first input surface
        before aligning. NOTE: setting this attribute to random values will cause
        unpredictable results and is not supported. Default:false
    
    - reverse2 : rv2                 (bool)          [create,query,edit]
        If true, reverse the direction (specified by directionU) of the second input
        surface before doing align. Otherwise, do nothing to the second input surface
        before aligning. NOTE: setting this attribute to random values will cause
        unpredictable results and is not supported. Default:false
    
    - swap1 : sw1                    (bool)          [create,query,edit]
        If true, swap the UV directions of the first input surface before doing align.
        Otherwise, do nothing to the first input surface before aligning. NOTE: setting
        this attribute to random values will cause unpredictable results and is not
        supported. Default:false
    
    - swap2 : sw2                    (bool)          [create,query,edit]
        If true, swap the UV directions of the second input surface before doing align.
        Otherwise, do nothing to the second input surface before aligning. NOTE: setting
        this attribute to random values will cause unpredictable results and is not
        supported. Default:false
    
    - tangentContinuity : tc         (bool)          [create,query,edit]
        Tangent continuity is on if true and off otherwise. Default:true
    
    - tangentContinuityType : tct    (int)           [create,query,edit]
        Tangent continuity type legal values: 1 - do tangent continuity on first
        surface, 2 - do tangent continuity on second surface Default:1
    
    - tangentScale1 : ts1            (float)         [create,query,edit]
        Tangent scale applied to tangent of first surface for tangent continuity.
        Default:1.0
    
    - tangentScale2 : ts2            (float)         [create,query,edit]
        Tangent scale applied to tangent of second surface for tangent continuity.
        Default:1.0
    
    - twist : tw                     (bool)          [create,query,edit]
        If true, reverse the second surface in the opposite direction (specified by
        directionU) before doing align. This will avoid twists in the aligned surfaces.
        Otherwise, do nothing to the second input surface before aligning. NOTE: setting
        this attribute to random values will cause unpredictable results and is not
        supported. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.alignSurface`
    """
    pass


def polyFlipEdge(*args, **kwargs):
    """
    Command to flip the edges shared by 2 adjacent triangles. When used with the
    edit flag, new edges can be added to the same node, instead of creating a
    separate node in the chain.
    
    
    Derived from mel command `maya.cmds.polyFlipEdge`
    """
    pass


def subdMapSewMove(*args, **kwargs):
    """
    This command can be used to Move and Sew together separate UV pieces along
    geometric edges. UV pieces that correspond to the same geometric edge, are
    merged together by moving the smaller piece to the larger one. The argument is a
    UV selection list.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - limitPieceSize : lps           (bool)          [create,query,edit]
        When on, this flag specifies that the face number limit described above should
        be used.
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - numberFaces : nf               (int)           [create,query,edit]
        Maximum number of faces in a UV piece. When trying to combine two UV pieces into
        a single one, the merge operation is rejected if the smaller piece has more
        faces than the number specified by this flag.This flag is only used when
        limitPieceSizeis set to on.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        If true, performs the operation in world space coordinates as opposed to local
        space.                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.subdMapSewMove`
    """
    pass


def roundConstantRadius(*args, **kwargs):
    """
    This command generates constant radius NURBS fillets and NURBS corner surfaces
    for matching edge pairs on NURBS surfaces.  An edge pair is a matching pair of
    surface isoparms or trim edges. This command can handle more than one edge pair
    at a time. This command can also handle compoundedges, which is where an edge
    pair is composed of more than two surfaces.  Use the -saand -sbflags in this
    case. The results from this command are three surface var groups plus the name
    of the new roundConstantRadius dependency node, if history was on. The 1st var
    group contains trimmed copies of the original surfaces.  The 2nd var group
    contains the new NURBS fillet surfaces.  The 3rd var group contains the new
    NURBS corners (if any). A simple example of an edge pair is an edge of a NURBS
    cube, where two faces of the cube meet.  This command generates a NURBS fillet
    at the edge and trims back the faces. Another example is a NURBS cylinder with a
    planar trim surface cap. This command will create a NURBS fillet where the cap
    meets the the cylinder and will trim back the cap and the cylinder. Another
    example involves all 12 edges of a NURBS cube.  NURBS fillets are created where
    any face meets another face.  NURBS corners are created whenever 3 edges meet at
    a corner.
    
    Flags:
    - append : a                     (bool)          [create]
        If true, then an edge pair is being added to an existing round dependency node.
        Default is false. When this flag is true, an existing round dependency node must
        be specified. See example below.
    
    - caching : cch                  (bool)          []
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           []
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - radius : r                     (float)         []
    
    - radiuss : rad                  (float)         [create]
        Use this flag to specify radius.  This overrides the r/radiusflag.  If only one
        radflag is used, then it is applied to all edge pairs.  If more than one radflag
        is used, then the number of -radflags must equal the number of edge pairs.  For
        example, for four edge pairs, zero, one or four radflags must be specified.
    
    - side : s                       (unicode, int)  [create]
        Use this flag for compound edges.  It replaces the sidea/sideb flags and is
        compatible with Python.  The first argument must be either aor b.  The same
        number of avalues as bvalues must be specified. If no sides are specified with
        the sideflag (or sidea/sideb flags), then the edges are assumed to be in pairs.
        See also examples below. For example, two faces of a cube meet at an edge pair.
        Suppose one of the faces is then split in two pieces at the middle of the edge,
        so that there is one face on side A, and two pieces on side B.  In this case the
        flag combination: -side a1 -side b2 would be used. The edges must be specified
        in the corresponding order: // MEL roundConstantRadius -side a1 -side b2 isoA
        isoB1 isoB2; # Python maya.cmds.roundConstantRadius( 'isoA', 'isoB1', 'isoB2',
        side=[(a,1), (b,2)] )
    
    - sidea : sa                     (int)           [create]
        Use this flag for compound edges in conjunction with the following -sbflag.
        This flag is not intended for use from Python.  Please see sideflag instead.
        The same number of -saflags as -sbflags must be specified. If no -sanor -sbflags
        are specified, then the edges are assumed to be in pairs. See also examples
        below. For example, two faces of a cube meet at an edge pair. Suppose one of the
        faces is then split in two pieces at the middle of the edge, so that there is
        one face on side A, and two pieces on side B.  In this case, the flag
        combination: -sidea 1 -sideb 2 would be used. The edges must be specified in the
        corresponding order: roundConstantRadius -sidea 1 -sideb 2 isoA isoB1 isoB2;
    
    - sideb : sb                     (int)           [create]
        Use this flag for compound edges in conjunction with the -saflag.  See
        description for the -saflag.  This flag is not intended for use from Python.
        Please see sideflag instead.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    - tolerance : tol                (float)         []
    
    
    Derived from mel command `maya.cmds.roundConstantRadius`
    """
    pass


def polyReduce(*args, **kwargs):
    """
    Simplify a polygonal object by reducing geometry while preserving the overall
    shape of the mesh. The algorithm for polyReduce was changed in 2014 to use a new
    algorithm derived from Softimage. However, the command still defaults to using
    the old algorithm for backwards compatibility.  Therefore, we recommend setting
    the version flag to 1 for best results as the new algorithm is better at
    preserving geometry features.  Additionally, some flags only apply to a specific
    algorithm and this is documented for each flag.
    
    Flags:
    - border : b                     (float)         []
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - cachingReduce : cr             (bool)          [create,query,edit]
        Cache intermediate reductions for speed at the expense of memory. It is
        recommended that caching be enabled when using the new algorithm. (-version 1)
        However, caching is not recommended when using then old algorithm because it can
        cause stability issues. C: Default is false. Q: When queried, this flag returns
        a boolean.
    
    - colorWeights : cwt             (float)         [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. How much consideration vertex color is given in the
        reduction algorithm. A higher weight means the reduction will try harder to
        preserve vertex coloring. C: Default is 0. Q: When queried, this flag returns a
        float.
    
    - compactness : com              (float)         [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. Tolerance for compactness for the generated triangles A
        value of 0 will accept all triangles during decimation A value close to 0 will
        attempt to eliminate triangles that have collinear edges (zero area triangles) A
        value closer to 1 will attempt to eliminate triangles that are not strictly
        equilateral (of equal lengths) The closer to 1.0, the more expensive the
        computation Q: When queried, this flag returns a float.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - detail : d                     (float)         []
    
    - frozen : fzn                   (bool)          []
    
    - geomWeights : gwt              (float)         [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. How much consideration vertex positions are given in
        the reduction algorithm.  A higher weight means the reduction will try harder to
        preserve geometry. C: Default is 1. Q: When queried, this flag returns a float.
    
    - invertVertexWeights : iwt      (bool)          [create,query,edit]
        This flag controls how weight map values are interpreted. If true, a vertex
        weight of 1.0 means a vertex is unlikely to be reduced. If false, a vertex
        weight of 0.0 means a vertex is unlikely to be reduced. This flag only applies
        when using the new algorithm. (-version 1) C: Default is true. Q: When queried,
        this flag returns a boolean.
    
    - keepBorder : kb                (bool)          [create,query,edit]
        If true, reduction will try to retain geometric borders and the border of the
        selection. C: Default is true. Q: When queried, this flag returns a boolean.
    
    - keepBorderWeight : kbw         (float)         [create,query,edit]
        If keepBorder is on, this flag specifies the weight to assign to borders.
        Setting this value to 0 will disable border preservation and a value of 1 will
        exactly preserve all border vertices which is useful for matching adjacent
        meshes.  This flag only applies when using the new algorithm. (-version 1) C:
        Default is 0.5. Q: When queried, this flag returns a float.
    
    - keepColorBorder : kcb          (bool)          [create,query,edit]
        If true, reduction will try to retain color borders.  These are determined
        according to color Ids.  This flag only applies when using the new algorithm.
        (-version 1) C: Default is true. Q: When queried, this flag returns a boolean.
    
    - keepColorBorderWeight : kcw    (float)         [create,query,edit]
        If keepColorBorder is on, this flag specifies the weight to assign to color
        borders.  Setting this value to 0 will disable color border preservation and a
        value of 1 will exactly preserve all color borders.  This flag only applies when
        using the new algorithm. (-version 1) C: Default is 0.5. Q: When queried, this
        flag returns a float.
    
    - keepCreaseEdge : kce           (bool)          [create,query,edit]
        If true, reduction will try to retain crease edges. C: Default is true.  This
        flag only applies when using the new algorithm. (-version 1) C: Default is true.
        Q: When queried, this flag returns a boolean.
    
    - keepCreaseEdgeWeight : cew     (float)         [create,query,edit]
        If keepCreaseEdge is on, this flag specifies the weight to assign to crease
        edges.  Setting this value to 0 will disable crease edge preservation and a
        value of 1 will exactly preserve all crease edges. This flag only applies when
        using the new algorithm. (-version 1) C: Default is 0.5. Q: When queried, this
        flag returns a float.
    
    - keepFaceGroupBorder : kfb      (bool)          [create,query,edit]
        If true, reduction will try to retain borders of face groups, which are mostly
        used to define material assignments.  This flag only applies when using the new
        algorithm. (-version 1) C: Default is true. Q: When queried, this flag returns a
        boolean.
    
    - keepFaceGroupBorderWeight : kfw (float)         [create,query,edit]
        If keepFaceGroupBorder is on, this flag specifies the weight to assign to
        material borders.  Setting this value to 0 will disable group border
        preservation and a value of 1 will exactly preserve all group borders.  This
        flag only applies when using the new algorithm. (-version 1) C: Default is 0.5.
        Q: When queried, this flag returns a float.
    
    - keepHardEdge : khe             (bool)          [create,query,edit]
        If true, reduction will try to retain hard edges. C: Default is true. Q: When
        queried, this flag returns a boolean.
    
    - keepHardEdgeWeight : khw       (float)         [create,query,edit]
        If keepHardEdge is on, this flag specifies the weight to assign to hard edges.
        Setting this value to 0 will disable hard edge preservation and a value of 1
        will exactly preserve all hard edges. This flag only applies when using the new
        algorithm. (-version 1) C: Default is 0.5. Q: When queried, this flag returns a
        float.
    
    - keepMapBorder : kmb            (bool)          [create,query,edit]
        If true, reduction will try to retain UV borders.  A UV border is present if the
        faces on either side of the edge do not share UV Ids. C: Default is true. Q:
        When queried, this flag returns a boolean.
    
    - keepMapBorderWeight : kmw      (float)         [create,query,edit]
        If keepMapBorder is on, this flag specifies the weight to assign to UV map
        borders.  Setting this value to 0 will disable UV map border preservation and a
        value of 1 will exactly preserve all UV borders. This flag only applies when
        using the new algorithm. (-version 1) C: Default is 0.5. Q: When queried, this
        flag returns a float.
    
    - keepOriginalVertices : kev     (bool)          [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. If true, vertices will try to retain their original
        positions and will not be repositioned for optimal shape. NOTE: In the newer
        algorithm vertices always retain their exact original positions. (though the Ids
        will change) C: Default is false. Q: When queried, this flag returns a boolean.
    
    - keepQuadsWeight : kqw          (float)         [create,query,edit]
        This flag controls how much consideration is given to oreserving quad faces
        during reduction.  A higher weight means the reduction will try harder to keep
        quad faces and avoid creation of triangles. If the version flag is set to 1
        (-version 1) and the keepQuadsWeight flag is set to 1.0 then a special quad
        reduction algorithm is used that does a better job of preserving quads. Howver,
        this special quad reduction algorithm does not support symmetry so those flags
        will be ignored when the keepQuadsWeight flag is set to 1.0. C: Default is 0. Q:
        When queried, this flag returns a float.
    
    - line : l                       (float)         []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - percentage : p                 (float)         [create,query,edit]
        This flag specifies how many vertices to remove during reduction as a percentage
        of the original mesh.  This flag only applies if the termination flag is set to
        0 or when using the old algorithm. C: Default is 0. 100 will remove every
        possible vertex, 0 will remove none. Q: When queried, this flag returns a float.
    
    - preserveLocation : pl          (bool)          [create]
        This flag guarantees that if the original geometry is preserved, the new
        geometry will have the same location. C: Default is false.
    
    - preserveTopology : top         (bool)          [create,query,edit]
        this flag guarantees that the topological type will be preserved during
        reduction.  In particular, if the input is manifold then the output will be
        manifold.  This option also prevents holes in the mesh from being closed off.
        This flag only applies when using the new algorithm. (-version 1) C: Default is
        true. Q: When queried, this flag returns a boolean.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace) (not available in all commands). NOTE: This flag
        is intended for use by the Reducemenu item. If 'polyReduce -rpo 0' is executed
        from the command line, Shader information will not be copied from the original
        mesh to the result.
    
    - sharpness : shp                (float)         [create,query,edit]
        Sharpness controls the balance between preserving small, sharp details versus
        larger shapes.  At low values, details that are small relative to the general
        shape of the object are more likely to be collapsed.  At high values, they are
        more likely to be kept.  This flag only applies when using the new algorithm.
        (-version 1) C: Default is 0. Q: When queried, this flag returns a float.
    
    - symmetryPlane : sym            (float, float, float, float) []
    
    - symmetryPlaneW : sw            (float)         [create,query,edit]
        W value of the symmetry plane.  This flag only applies when using the new
        algorithm (-version 1) and the useVirtualSymmetry flag is set to 2. C: Default
        is 0. Q: When queried, this flag returns a float.
    
    - symmetryPlaneX : sx            (float)         [create,query,edit]
        X value of the symmetry plane.  This flag only applies when using the new
        algorithm (-version 1) and the useVirtualSymmetry flag is set to 2. C: Default
        is 0. Q: When queried, this flag returns a float.
    
    - symmetryPlaneY : sy            (float)         [create,query,edit]
        Y value of the symmetry plane.  This flag only applies when using the new
        algorithm (-version 1) and the useVirtualSymmetry flag is set to 2. C: Default
        is 0. Q: When queried, this flag returns a float.
    
    - symmetryPlaneZ : sz            (float)         [create,query,edit]
        Z value of the symmetry plane.  This flag only applies when using the new
        algorithm (-version 1) and the useVirtualSymmetry flag is set to 2. C: Default
        is 0. Q: When queried, this flag returns a float.
    
    - symmetryTolerance : stl        (float)         [create,query,edit]
        Tolerance to use when applying symmetry. For each vertex of the mesh, we find
        its exact symmetric point, then we look for the closest vertex to the exact
        symmetry up to the tolerance distance.  Higher values risk finding more spurious
        symmetries, lower values might miss symmetries. The value is distance in object
        space.  This flag only applies when using the new algorithm (-version 1) and the
        useVirtualSymmetry flag is not set to 0. C: Default is 0. Q: When queried, this
        flag returns a float.
    
    - termination : trm              (int)           [create,query,edit]
        This flag specifies the termination condition to use when reducing the mesh.
        This flag only applies to the new algorithm. (-version 1) 0 Percentage 1 Vertex
        count 2 Triangle count C: Default is 0. Q: When queried, this flag returns an
        integer.
    
    - triangleCount : tct            (int)           [create,query,edit]
        This flag specifies a target number of triangles to retain after reduction. Note
        that other factors such as quad and feature preservation may take precendence
        and cause the actual number of triangles to be different. This flag only applies
        when using the new algorithm (-version 1) and the termination flag is set to 2.
        C: Default is 0. Q: When queried, this flag returns an integer.
    
    - triangulate : t                (bool)          [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. This attribute specifies if the geometry or the
        selected faces has to be triangulated, before performing reduction. C: Default
        is true. Q: When queried, this flag returns a boolean.
    
    - useVirtualSymmetry : uvs       (int)           [create,query,edit]
        This flag controls whether symmetry is preserved during the reduction. This flag
        only applies when using the new algorithm (-version 1) and the keepQuadsWeight
        flag is less than 1.0. 0 No symmetry preservation 1 Automatic. Try to find
        suitable symmetry during reduction. 2 Plane.  Specify a symmetry plane to use
        during reduction. C: Default is 0. Q: When queried, this flag returns an
        integer.
    
    - uvWeights : uwt                (float)         [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. How much consideration uv positions are given in the
        reduction algorithm. A higher weight means the reduction will try harder to
        preserve uv positions. C: Default is 0. Q: When queried, this flag returns a
        float.
    
    - version : ver                  (int)           [create,query,edit]
        Version of the poly reduce algorithm to use. 0 Old algorithm used in Maya 2013
        and prior for backwards compatibility 1 New algorithm derived from Softimage and
        used in Maya 2014 and later The default is 0 for backwards compatibility but for
        best results it is recommended that the new algorithm is used as it is better at
        preserving mesh details. Some flags only apply to a specific algorithm and this
        is documented for each flag. C: Default is 0 for backwards compatibility. Q:
        When queried, this flag returns an integer.
    
    - vertexCount : vct              (int)           [create,query,edit]
        This flag specifies a target number of vertices to retain after reduction. Note
        that other factors such as quad and feature preservation may take precendence
        and cause the actual number of vertices to be different. This flag only applies
        when using the new algorithm (-version 1) and the termination flag is set to 1.
        C: Default is 0. Q: When queried, this flag returns an integer.
    
    - vertexMapName : vmp            (unicode)       [create,query]
        Name of a color set to be added to the output mesh that stores a mapping from
        vertices in the output mesh to vertices in the input mesh.  The color set is
        RGB.  The original vertex Id that maps to an output vertex is of a vertex is
        65536\*r + g where r and g are the red and green channel at a vertex. The blue
        channel is always zero.  Each vertex in the output mesh has a shared color. This
        flag only applies when using the new algorithm. (-version 1) Q: When queried,
        this flag returns a string.
    
    - vertexWeightCoefficient : vwc  (float)         [create,query,edit]
        This flag specifies a constant value to multiply to each weight map value. A
        value of zero turns off the weight map.  This flag only applies when using the
        new algorithm. (-version 1) C: Default is 1. Q: When queried, this flag returns
        a float.
    
    - weightCoefficient : wc         (float)         [create,query,edit]
        This flag only applies when using the old algorithm and is provided for
        backwards compatibility. The weight of each vertex is multiplied with this
        coefficient when the reduction is performed.  This value does not have to be
        edited, normally.  It gives finer control over the weighted reduction. This
        attribute is replaced by vertexWeightCoefficient in the new algorithm when the
        version flag is set to 1. C: Default is 10000. Q: When queried, this flag
        returns a float.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyReduce`
    """
    pass


def offsetCurve(*args, **kwargs):
    """
    The offset command creates new offset curves from the selected curves. The
    connecting type for breaks in offsets is off (no connection), circular (connect
    with an arc) or linear (connect linearly resulting in a sharp corner). If loop
    cutting is on then any loops in the offset curves are trimmed away. For the
    default cut radius of 0.0 a sharp corner is created at each intersection. For
    values greater than 0.0 a small arc of that radius is created at each
    intersection. The cut radius value is only valid when loop cutting is on.
    Offsets (for planar curves) are calculated in the plane of that curve and 3d
    curves are offset in 3d. The subdivisionDensity flag is the maximum number of
    times the offset object can be subdivided (i.e. calculate the offset until the
    offset comes within tolerance or the iteration reaches this maximum.) The
    reparameterize option allows the offset curve to have a different
    parameterization to the original curve. This avoids uneven parameter
    distributions in the offset curve that can occur with large offsets of curves,
    but is more expensive to compute.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - connectBreaks : cb             (int)           [create,query,edit]
        Connect breaks method (between gaps): 0 - off, 1 - circular, 2 - linear
        Default:2
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - cutLoop : cl                   (bool)          [create,query,edit]
        Do loop cutting. Default:false
    
    - cutRadius : cr                 (float)         [create,query,edit]
        Loop cut radius. Only used if cutLoop attribute is set true. Default:0.0
    
    - distance : d                   (float)         [create,query,edit]
        Offset distance Default:1.0
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - normal : nr                    (float, float, float) [create,query,edit]
        Offset plane normal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - reparameterize : rp            (bool)          [create,query,edit]
        Do reparameterization. It is not advisable to change this value. Default:false
    
    - stitch : st                    (bool)          [create,query,edit]
        Stitch curve segments together. It is not advisable to change this value.
        Default:true
    
    - subdivisionDensity : sd        (int)           [create,query,edit]
        Maximum subdivision density per span Default:5
    
    - tolerance : tol                (float)         [create,query,edit]
        Tolerance Default:0.01
    
    - useGivenNormal : ugn           (bool)          [create,query,edit]
        Use the given normal (or, alternativelly, geometry normal) Default:1
        Common flags
    
    
    Derived from mel command `maya.cmds.offsetCurve`
    """
    pass


def polyNormal(*args, **kwargs):
    """
    Control the normals of an object. This command works on faces or polygonal
    objects.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - normalMode : nm                (int)           [create,query,edit]
        Normal mode     : 0=reverse, 1=propagate, 2=conform, 3=reverseAndCut,
        4=reverseAndPropagate Default:0
    
    - userNormalMode : unm           (bool)          [create,query,edit]
        Determines if user normals needs to be reversed as well. Default:true
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyNormal`
    """
    pass


def extrude(*args, **kwargs):
    """
    This command computes a surface given a profile curve and possibly a path curve.
    There are three ways to extrude a profile curve. The most basic method is called
    a distanceextrude where direction and length are specified. No path curve is
    necessary in this case. The second method is called flatextrude. This method
    sweeps the profile curve down the path curve without changing the orientation of
    the profile curve. Finally, the third method is called tubeextrude. This method
    sweeps a profile curve down a path curve while the profile curve rotates so that
    it maintains a relationship with the path curve.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degreeAlongLength : dl         (int)           [create,query,edit]
        Surface degree along the distance when a distance extrude is performed Default:1
    
    - direction : d                  (float, float, float) [create,query,edit]
        The direction in which to extrude. Use only for distance extrudeType and
        useProfileNormal off
    
    - directionX : dx                (float)         [create,query,edit]
        X of the direction Default:0
    
    - directionY : dy                (float)         [create,query,edit]
        Y of the direction Default:1
    
    - directionZ : dz                (float)         [create,query,edit]
        Z of the direction Default:0
    
    - extrudeType : et               (int)           [create,query,edit]
        The extrude type (distance-0, flat-1, or tube-2) Default:2
    
    - fixedPath : fpt                (bool)          [create,query,edit]
        If true, the resulting surface will be placed at the path curve. Otherwise, the
        resulting surface will be placed at the profile curve. Default:false
    
    - frozen : fzn                   (bool)          []
    
    - length : l                     (float)         [create,query,edit]
        The distance to extrude. Use only for distance extrudeType Default:1
    
    - mergeItems : mi                (bool)          [create]
        Merge component results where possible. For example, instead of returning a[1]
        and a[2], return a[1:2].
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The pivot point used for tube extrudeType
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.
    
    - rebuild : rb                   (bool)          [create]
        Rebuild the input curve(s) before using them in the operation.  Use
        nurbsCurveRebuildPref to set the parameters for the conversion.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - reverseSurfaceIfPathReversed : rsp (bool)          [create,query,edit]
        If true, extrude type is tube (2) and path has been internally reversed then
        computed surface is reversed in the direction corresponding to the path.
        Default:false
    
    - rotation : ro                  (float)         [create,query,edit]
        Amount to rotate the profile curve as it sweeps along the path curve.
        Default:0.0
    
    - scale : sc                     (float)         [create,query,edit]
        Amount to scale the profile curve as it sweeps along the path curve. Default:1.0
    
    - subCurveSubSurface : scs       (bool)          [create,query,edit]
        If true, curve range on the path will get applied to the resulting surface
        instead of cut before the extrude. Default:false
    
    - useComponentPivot : ucp        (int)           [create,query,edit]
        Use closest endpoint of the path - 0, component pivot - 1 or the center of the
        bounding box of the profile - 2 Default:0
    
    - useProfileNormal : upn         (bool)          [create,query,edit]
        If true, use the profile curve normal for the direction in which to extrude. Use
        only for distance or tube extrudeType. Default:false                  Common
        flags
    
    
    Derived from mel command `maya.cmds.extrude`
    """
    pass


def filletCurve(*args, **kwargs):
    """
    The curve fillet command creates a fillet curve between two curves. If no
    objects are specified in the command line, then the first two active curves are
    used. The fillet created can be circular (with a radius) or freeform (with a
    type of tangent or blend).
    
    Flags:
    - bias : b                       (float)         [create,query,edit]
        Adjusting the bias value causes the fillet curve to be skewed to one of the
        input curves. Available only if blendControl is true. Default:0.0
    
    - blendControl : bc              (bool)          [create,query,edit]
        If true then depth and bias can be controlled. Otherwise, depth and bias are not
        available options. Default:false
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - circular : cir                 (bool)          [create,query,edit]
        Curve fillet will be created as circular if true or freeform if false.
        Default:true
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveParameter1 : cp1          (float)         [create,query,edit]
        Parameter where fillet curve will contact the primary input curve. Default:0.0
    
    - curveParameter2 : cp2          (float)         [create,query,edit]
        Parameter where fillet curve will contact the secondary input curve. Default:0.0
    
    - depth : d                      (float)         [create,query,edit]
        Adjusts the depth of the fillet curve. Available only if blendControl is true.
        Default:0.5
    
    - freeformBlend : fb             (bool)          [create,query,edit]
        The freeform type is blend if true or tangent if false. Available if the fillet
        type is freeform. Default:false
    
    - frozen : fzn                   (bool)          []
    
    - join : jn                      (bool)          [create]
        Should the fillet be joined?
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - radius : r                     (float)         [create,query,edit]
        The radius if creating a circular fillet. Default:1.0                  Common
        flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).
    
    - trim : t                       (bool)          [create]
        Should the fillet be trimmed?                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.filletCurve`
    """
    pass


def polySoftEdge(*args, **kwargs):
    """
    Selectively makes edges soft or hard. An edge will be made hard if the angle
    between two owning faces is sharper (larger) than the smoothing angle. An edge
    wil be made soft if the angle between two owning facets is flatter (smaller)
    than the smoothing angle.
    
    Flags:
    - angle : a                      (float)         [create,query,edit]
        Smoothing angle. C: Default is 30 degrees. Q: When queried, this flag returns a
        float.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polySoftEdge`
    """
    pass


def cylinder(*args, **kwargs):
    """
    The cylinder command creates a new cylinder and/or a dependency node that
    creates one, and returns their names.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        The primitive's axis
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface: 1 - linear, 3 - cubic Default:3
    
    - endSweep : esw                 (float)         [create,query,edit]
        The angle at which to end the surface of revolution. Default is 2Pi radians, or
        360 degrees. Default:6.2831853
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - heightRatio : hr               (float)         [create,query,edit]
        Ratio of heightto widthDefault:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The primitive's pivot point
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    - radius : r                     (float)         [create,query,edit]
        The radius of the object Default:1.0
    
    - sections : s                   (int)           [create,query,edit]
        The number of sections determines the resolution of the surface in the sweep
        direction. Used only if useTolerance is false. Default:8
    
    - spans : nsp                    (int)           [create,query,edit]
        The number of spans determines the resolution of the surface in the opposite
        direction. Default:1
    
    - startSweep : ssw               (float)         [create,query,edit]
        The angle at which to start the surface of revolution Default:0
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to build the surface. Used only if useTolerance is true
        Default:0.01
    
    - useTolerance : ut              (bool)          [create,query,edit]
        Use the specified tolerance to determine resolution. Otherwise number of
        sections will be used. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.cylinder`
    """
    pass


def polySelectConstraintMonitor(*args, **kwargs):
    """
    Manage the window to display/edit the polygonal selection constraint parameters
    
    Flags:
    - changeCommand : cc             (unicode, unicode) [create]
        Specifies the mel callback to refresh the window. First argument is the
        callback, second is the window name.
    
    - create : c                     (bool)          [create]
        Specifies the Monitor should be created
    
    - delete : d                     (bool)          [create]
        Specifies that the Monitor should be removed                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polySelectConstraintMonitor`
    """
    pass


def cone(*args, **kwargs):
    """
    The cone command creates a new cone and/or a dependency node that creates one,
    and returns their names.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        The primitive's axis
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface: 1 - linear, 3 - cubic Default:3
    
    - endSweep : esw                 (float)         [create,query,edit]
        The angle at which to end the surface of revolution. Default is 2Pi radians, or
        360 degrees. Default:6.2831853
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - heightRatio : hr               (float)         [create,query,edit]
        Ratio of heightto widthDefault:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The primitive's pivot point
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    - radius : r                     (float)         [create,query,edit]
        The radius of the object Default:1.0
    
    - sections : s                   (int)           [create,query,edit]
        The number of sections determines the resolution of the surface in the sweep
        direction. Used only if useTolerance is false. Default:8
    
    - spans : nsp                    (int)           [create,query,edit]
        The number of spans determines the resolution of the surface in the opposite
        direction. Default:1
    
    - startSweep : ssw               (float)         [create,query,edit]
        The angle at which to start the surface of revolution Default:0
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to build the surface. Used only if useTolerance is true
        Default:0.01
    
    - useOldInitBehaviour : oib      (bool)          [create,query,edit]
        Create the cone with base on the origin as in Maya V8.0 and below Otherwise
        create cone centred at origin Default:false
    
    - useTolerance : ut              (bool)          [create,query,edit]
        Use the specified tolerance to determine resolution. Otherwise number of
        sections will be used. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.cone`
    """
    pass


def polyStraightenUVBorder(*args, **kwargs):
    """
    Move border UVs along a simple curve.
    
    Flags:
    - blendOriginal : bo             (float)         [create,query]
        Interpolation factor between the target and original UV shape. When the value is
        0, the UVs will exactly fit the target curve. When the value is 1, no UV move.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - curvature : c                  (float)         [create,query]
        How curved the UV path will be. 0 is a straight line. When the values is 1, the
        mid point of the curve will be moved away from a straight line by 1/2 the length
        of the UV segment.
    
    - frozen : fzn                   (bool)          []
    
    - gapTolerance : gt              (int)           [create,query]
        When non 0, Small gaps between UV selection are filled. The integer number
        represent how many UVs must be traversed to connect togeterh selected pieces.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - preserveLength : pl            (float)         [create,query]
        How much we want to respect the UV edge ratios. When the value is 1, we build
        new UV position along the desired curve, respecting the original UV spacings.
        When the value is 0, new UVs are equally spaced along the curve.
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyStraightenUVBorder`
    """
    pass


def polyAppend(*args, **kwargs):
    """
    Appends a new face to the selected polygonal object. The first argument must be
    a border edge. The new face will be automatically closed. Only works with one
    object selected.
    
    Flags:
    - append : a                     (float, float, float) [create]
        Appends to the given polygon object.  The append flag should be used multiple
        times to specify the edges, points, and holes that make up the new face that is
        being added.  You may specify an edge by passing a single argument which will be
        the edges index.  A point is specified with three arguments which are the
        coordinates of the point in the objects local space.  Pass no arguments
        indicates that the values which follow shall specify a hole.  In Python, pass an
        empty tuple to specify no arguments.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - edge : ed                      (int)           [create]
        Adds the given edge of the selected object to the new face. This edge must be a
        border, which will be then shared by the new face and the neighboring one. The
        new face is oriented according to the orientation of the given edge(s).  Note
        that this flag should be avoided in Python.  You may use the appendflag instead
        and pass one argument.
    
    - hole : hl                      (bool)          [create]
        Add a hole. The following points and edges will define a hole.  Note that this
        flag should be avoided in Python.  You may use the appendflag instead and pass
        an empty tuple ().
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - point : p                      (float, float, float) [create]
        Adds a new point to the new face. Coordinates of free points are given in the
        local object reference.  Note that this flag should be avoided in Python.  You
        may use the appendflag instead and pass three arguments.
    
    - subdivision : s                (int)           [create,query,edit]
        This flag specifies the level of subdivisions. Automatically subdivides new
        edges into the given number of edges. Existing edges cannot be subdivided. C :
        Default is 1 (no subdivision). Q: When queried, this flag returns an int.
    
    - texture : tx                   (int)           [create,query,edit]
        Specifies how new faces are mapped. 0 - None; 1 - Normalize; 2 - Unitize C:
        Default is 0 (no mapping). Q: When queried, this flag returns an intFlag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyAppend`
    """
    pass


def editMetadata(*args, **kwargs):
    """
    This command is used to set metadata elements onto or remove metadata elements
    from an object. Before using this command you must first attach a metadata
    stream type to the object using the addMetadatacommand or an API equivalent. The
    command has four basic variations: Set per-component metadata on meshesRemove
    per-component metadata on meshesSet generic metadata on any objectRemove generic
    metadata on any objectThe difference between the setand removevariations (1,3
    vs. 2,4) is that setrequires both a member name to be set and a new value to be
    set. (The reason removal doesn't use a member name is that you can only remove
    an entire metadata structural element, you cannot remove only a single member
    from it.)  When metadata values are set or removed the action is performed on
    every selected component or index. This provides an easy method to set or remove
    a bunch of metadata en masse.  The general usage (variations 3, 4) lets you
    select specific pieces of metadata through the channelNameand indexflags. Note
    that since indexis a multi-use flag you can select many different elements from
    the same Channel and set or remove the metadata on all of them in one command.
    Metadata on meshes is special in that the Channel types vertex, edge, face, and
    vertexFaceare directly connected to the components of the same name. To make
    setting these metadata Channels easier you can simply select or specify on the
    command line the corresponding components rather than using the channelNameand
    indexflags. For example the selection myMesh.vtx[8:10]corresponds to channelName
    = vertexand index = 8, 9, 10(as a multi-use flag).  Note that the metadata is
    assigned to an object and except in the special case of mesh geometry does not
    flow through the dependency graph. In meshes the metadata will move from node to
    node wherever the geometry is connected, although it will not adjust itself
    automatically for changes in topology. Internal data is arranged to minimize the
    amount of copying no matter how many other nodes are connected to it.  Only a
    single node or scene, component type, channel type, and value type are allowed
    in a single command. This keeps the data simple at the possible cost of
    requiring multiple calls to the command to set more than one structure member's
    value.  Certain nodes have metadata supplied by input attributes. If you edit
    one of those with an incoming connection on such an attribute then the metadata
    edit will not be applied directly it will be put into an 'editMetadata' node for
    application during DG evaluation. Since the details of the metadata are not
    known until the evaluation happens less rigorous compatibility checking is
    performed. The editMetadata node has its own facilities for verifying and
    reporting illegal metadata edits. Successive edits to the same metadata in this
    way appends each edit to the same editMetadata node.
    
    Flags:
    - channelName : cn               (unicode)       [create,query]
        Filter the metadata selection to only recognize metadata belonging to the
        specified named Channel (e.g. vertex). This flag is ignored if the components on
        the selection list are being used to specify the metadata of interest. In query
        mode, this flag can accept a value.
    
    - channelType : cht              (unicode)       [create,query]
        Obsolete - use the 'channelName' flag instead. In query mode, this flag can
        accept a value.
    
    - endIndex : eix                 (unicode)       [create]
        The metadata is stored in a Stream, which is an indexed list. If you have mesh
        components selected then the metadata indices are implicit in the list of
        selected components. If you select only the node or scene then this flag may be
        used in conjunction with the startIndexflag to specify a range of indices from
        which to retrieve the metadata. It is an error to have the value of startIndexbe
        greater than that of endIndex.  See also the indexflag for an alternate way to
        specify multiple indices. This flag can only be used on index types that support
        a range (e.g. integer values - it makes no sense to request a range between two
        strings)  In query mode, this flag can accept a value.
    
    - index : idx                    (unicode)       [create,query]
        In the typical case metadata is indexed using a simple integer value. Certain
        types of data may use other index types. e.g. a vertexFacecomponent will use a
        pairindex type, which is two integer values; one for the face ID of the
        component and the second for the vertex ID.  The indexflag takes a string,
        formatted in the way the specified indexTyperequires. All uses of the indexflag
        have the same indexType. If the type was not specified it is assumed to be a
        simple integer value.  In query mode, this flag can accept a value.
    
    - indexType : idt                (unicode)       [create,query]
        Name of the index type the new Channel should be using. If not specified this
        defaults to a simple integer index. Of the native types only a mesh
        vertexFacechannel is different, using a pairindex type. In query mode, this flag
        can accept a value.
    
    - memberName : mn                (unicode)       [create]
        Name of the Structure member being edited. The names of the members are set up
        in the Structure definition, either through the description passed in through
        the dataStructurecommand or via the API used to create that Structure.
    
    - remove : rem                   (bool)          [create]
        If the removeflag is set then the metadata will be removed rather than have
        values set. In this mode the memberName, value, and stringValueflags are
        ignored. memberNameis ignored because when deleting metadata all members of a
        structure must be removed as a group. The others are ignored since when deleting
        you don't need a value to be set.
    
    - scene : scn                    (bool)          [create,query]
        Use this flag when you want to add metadata to the scene as a whole rather than
        to any individual nodes. If you use this flag and have nodes selected the nodes
        will be ignored and a warning will be displayed.
    
    - startIndex : six               (unicode)       [create]
        The metadata is stored in a Stream, which is an indexed list. If you have mesh
        components selected then the metadata indices are implicit in the list of
        selected components. If you select only the node or scene then this flag may be
        used in conjunction with the endIndexflag to specify a range of indices from
        which to retrieve the metadata. It is an error to have the value of startIndexbe
        greater than that of endIndex.  See also the indexflag for an alternate way to
        specify multiple indices. This flag can only be used on index types that support
        a range (e.g. integer values - it makes no sense to request a range between two
        strings)  In query mode, this flag can accept a value.
    
    - streamName : stn               (unicode)       [create,query]
        Name of the metadata Stream. Depending on context it could be the name of a
        Stream to be created, or the name of the Stream to pass through the filter. In
        query mode, this flag can accept a value.Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    - stringValue : sv               (unicode)       [create]
        String value to be set into the specified metadata locations. This flag can only
        be used when the data member is a numeric type. If the member has N dimensions
        (e.g. string[2]) then this flag must appear N times (e.g. 2 times) The same
        values are applied to the specified metadata member on all affected components
        or metadata indices. Only one of the value, and stringValue flags can be
        specified at once and the type must match the type of the structure member named
        by the memberflag.
    
    - value : v                      (float)         [create]
        Numeric value to be set into the specified metadata locations. This flag can
        only be used when the data member is a numeric type. If the member has N
        dimensions (e.g. float[3]) then this flag must appear N times (e.g. 3 times) The
        same values are applied to the specified metadata member on all affected
        components or metadata indices. All numeric member types should use this type of
        value specification, i.e. everything except string and matrix types. Only one of
        the value, and stringValue flags can be specified at once and the type must
        match the type of the structure member named by the memberflag.
    
    
    Derived from mel command `maya.cmds.editMetadata`
    """
    pass


def polyExtrudeVertex(*args, **kwargs):
    """
    Command that extrudes selected vertices outwards.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - divisions : d                  (int)           [create,query,edit]
        This flag specifies the number of subdivisions. C: Default is 1 Q: When queried,
        this flag returns an int.
    
    - frozen : fzn                   (bool)          []
    
    - length : l                     (float)         [create,query,edit]
        This flag specifies the length of the vertex extrusion. C: Default is 0 Q: When
        queried, this flag returns a float.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - width : w                      (float)         [create,query,edit]
        This flag specifies the width of the vertex extrusion. C: Default is 0 Q: When
        queried, this flag returns a float.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyExtrudeVertex`
    """
    pass


def polyMoveFacetUV(*args, **kwargs):
    """
    Modifies the map by moving all UV values associated with the selected face(s).
    The UV coordinates of the model are manipulated without changing the vertices of
    the 3D object.
    
    Flags:
    - axisLen : l                    (float, float)  [create,query,edit]
        Axis Length vector, used to draw the manip handles. C: Default is 1.0, 1.0 Q:
        When queried, this flag returns a float[2].
    
    - axisLenX : lx                  (float)         [create,query,edit]
        Axis Length in X, used to draw the manip handles. C: Default is 1.0 Q: When
        queried, this flag returns a float.
    
    - axisLenY : ly                  (float)         [create,query,edit]
        Axis Length in Y, used to draw the manip handles. C: Default is 1.0 Q: When
        queried, this flag returns a float.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - pivot : pvt                    (float, float)  [create,query,edit]
        This flag specifies the pivot for scaling and rotation. C: Default is 0.0 0.0.
        Q: When queried, this flag returns a float[2].
    
    - pivotU : pvu                   (float)         [create,query,edit]
        This flag specifies U for the pivot for scaling and rotation. C: Default is 0.0.
        Q: When queried, this flag returns a float.
    
    - pivotV : pvv                   (float)         [create,query,edit]
        This flag specifies V for the pivot for scaling and rotation. C: Default is 0.0.
        Q: When queried, this flag returns a float.
    
    - random : ran                   (float)         [create,query,edit]
        This flag specifies the random value for all parameters. C: Default is 0.0. The
        range is [-10.0, 10.0]. Q: When queried, this flag returns a float.
    
    - rotationAngle : ra             (float)         [create,query,edit]
        Angle of rotation. C: Default is 0.0. Q: When queried, this flag returns a
        float.
    
    - scale : s                      (float, float)  [create,query,edit]
        This flag specifies the scaling vector. C: Default is 1.0 1.0. Q: When queried,
        this flag returns a float.
    
    - scaleU : su                    (float)         [create,query,edit]
        This flag specifies U for the scaling vector. C: Default is 1.0. Q: When
        queried, this flag returns a float.
    
    - scaleV : sv                    (float)         [create,query,edit]
        This flag specifies V for the scaling vector. C: Default is 1.0. Q: When
        queried, this flag returns a float.
    
    - translate : t                  (float, float)  [create,query,edit]
        This flag specifies the translation vector. C: Default is 0.0 0.0. Q: When
        queried, this flag returns a float[2].
    
    - translateU : tu                (float)         [create,query,edit]
        This flag specifies the U translation vector. C: Default is 0.0. Q: When
        queried, this flag returns a float.
    
    - translateV : tv                (float)         [create,query,edit]
        This flag specifies the V translation vector. C: Default is 0.0. Q: When
        queried, this flag returns a float.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMoveFacetUV`
    """
    pass


def nurbsCurveToBezier(*args, **kwargs):
    """
    The nurbsCurveToBezier command attempts to convert an existing NURBS curve to a
    Bezier curve.
    
    
    Derived from mel command `maya.cmds.nurbsCurveToBezier`
    """
    pass


def polyToSubdiv(*args, **kwargs):
    """
    This command converts a polygon and produces a subd surface. The name of the new
    subdivision surface is returned. If construction history is ON, then the name of
    the new dependency node is returned as well.
    
    Flags:
    - absolutePosition : ap          (bool)          [create,query,edit]
        If true, the possible blind data information that comes from the polygon will be
        treated as absolute positions of the vertices, instead of the relative offsets.
        You most likelly just want to use the default of false, unless you know that the
        blind data has the absolute positions in it. Default:false
    
    - addUnderTransform : aut        (bool)          [create]
        If true then add the new subdivision surface under the poly's transform.
    
    - applyMatrixToResult : amr      (bool)          [create,query,edit]
        If true, the matrix on the input geometry is applied to the object and the
        resulting geometry will have identity matrix on it.  If false the conversion is
        done on the local space object and the resulting geometry has the input object's
        matrix on it. Default:true
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - maxEdgesPerVert : me           (int)           [create,query,edit]
        The maximum allowed valence for a vertex on the input mesh Default:32
    
    - maxPolyCount : mpc             (int)           [create,query,edit]
        The maximum number of polygons accepted on the input mesh. Default:1000
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - preserveVertexOrdering : pvo   (bool)          [create,query,edit]
        Preserve vertex ordering in conversion Default:true
    
    - quickConvert : qc              (bool)          [create,query,edit]
        Debug flag to test the performance Default:true
    
    - uvPoints : uvp                 (float, float)  [create,query,edit]
        This is a cached uv point needed to transfer uv data associated with finer level
        vertices (when switching between standard editing mode and poly proxy mode.
    
    - uvPointsU : uvu                (float)         [create,query,edit]
        U value of a cached uv point
    
    - uvPointsV : uvv                (float)         [create,query,edit]
        V value of a cached uv point
    
    - uvTreatment : uvt              (int)           [create,query,edit]
        Treatment of Subd UVs when in proxy mode: 0 - preserve Subd UVs1 - build Subd
        UVs from Poly UVs2 - no UVs on SubdDefault:0                  Common flags
    
    
    Derived from mel command `maya.cmds.polyToSubdiv`
    """
    pass


def revolve(*args, **kwargs):
    """
    This command creates a revolved surface by revolving the given profile curve
    about an axis.  The profile curve can be a curve, curve-on-surface, surface
    isoparm, or trim edge.
    
    Flags:
    - autoCorrectNormal : acn        (bool)          [create,query,edit]
        If this is set to true we will attempt to reverse the direction of the axis in
        case it is necessary to do so for the surface normals to end up pointing to the
        outside of the object. Default:false
    
    - axis : ax                      (float, float, float) [create,query,edit]
        Revolve axis
    
    - axisChoice : aco               (int)           [create,query,edit]
        Only used for computed axis/pivot case.  As we are computing the axis for a
        planar curve, we have two choices for the major axis based axis.  We will choose
        the axis corresponding to the longer dimension of the object (0), or explicitly
        choose one or the other (choices 1 and 2). Default:0
    
    - axisX : axx                    (float)         [create,query,edit]
        X of the axis Default:1
    
    - axisY : axy                    (float)         [create,query,edit]
        Y of the axis Default:0
    
    - axisZ : axz                    (float)         [create,query,edit]
        Z of the axis Default:0
    
    - bridge : br                    (bool)          [create,query,edit]
        If true, we will close a partial revolve to get a pie shaped surface.  The
        surface will be closed, but not periodic the way it is in the full revolve case.
        Default:false
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - computePivotAndAxis : cpa      (int)           [create,query,edit]
        If this is set to 2, we will compute the axis, use the curve position and radius
        to compute the pivot for the revolve internally.  The value of the pivot and
        axis attributes are ignored.  If this is set to 1, we will take the supplied
        axis, but compute the pivot.  If this is set to 0, we will take both the
        supplied axis and pivot. Default:0
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface. Default:3
    
    - endSweep : esw                 (float)         [create,query,edit]
        The value for the end sweep angle, in the current units.  This must be no more
        than the maximum, 360 degrees, or 2 Pi radians. Default:6.2831853
    
    - frozen : fzn                   (bool)          []
    
    - mergeItems : mi                (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pivot : p                      (float, float, float) [create,query,edit]
        Revolve pivot point
    
    - pivotX : px                    (float)         [create,query,edit]
        X of the pivot Default:0
    
    - pivotY : py                    (float)         [create,query,edit]
        Y of the pivot Default:0
    
    - pivotZ : pz                    (float)         [create,query,edit]
        Z of the pivot Default:0
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - radius : r                     (float)         [create,query,edit]
        The pivot point will be this distance away from the bounding box of the curve,
        if computedPivot is set to true.  The value of the pivot attribute is ignored.
        Default:1
    
    - radiusAnchor : ra              (float)         [create,query,edit]
        The position on the curve for the anchor point so that we can compute the pivot
        using the radius value.  If in 0 - 1 range, its on the curve, normalized
        parameter range.  If 0 or 1, its computed based on the bounding box. Default:-1
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.
    
    - rebuild : rb                   (bool)          [create]
        Rebuild the input curve(s) before using them in the operation.  Use
        nurbsCurveRebuildPref to set the parameters for the conversion.
    
    - sections : s                   (int)           [create,query,edit]
        Number of sections of the resulting surface (if tolerance is not used).
        Default:8
    
    - startSweep : ssw               (float)         [create,query,edit]
        The value for the start sweep angle, in the current units.  This must be no more
        than the maximum, 360 degrees, or 2 Pi radians. Default:0
    
    - tolerance : tol                (float)         [create,query,edit]
        Tolerance to build to (if useTolerance attribute is set) Default:0.01
    
    - useLocalPivot : ulp            (bool)          [create,query,edit]
        If true, then the pivot of the profile curve is used as the start point of the
        axis of revolution.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    - useTolerance : ut              (bool)          [create,query,edit]
        Use the tolerance, or the number of sections to control the sections.
        Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.revolve`
    """
    pass


def polyPrimitive(*args, **kwargs):
    """
    Create a polygon primative
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the primitive polygon. Q:
        When queried, this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize Each Face
        Separately3: Normalize Collectively4: Normalize and Preserve Aspect Ratio
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - polyType : pt                  (int)           [create]
        This flag allows a specific primitive poly to be selected for creation of mesh,
        The valid values is 0 0 implies soccer ball to be created. C: Default is 0
    
    - radius : r                     (float)         [create,query,edit]
        This flag specifies the radius of the primitive polygon. C: Default is 1.0. Q:
        When queried, this flag returns a float.
    
    - sideLength : l                 (float)         [create,query,edit]
        This flag specifies the side length of primitive polygon. C: Default is 1.0. Q:
        When queried, this flag returns a float.
    
    - texture : tx                   (int)           [create,query,edit]
        What texture mechanism to be applied 0=No textures, 1=Object, 2=Faces
        Common poly creation operation flags
    
    
    Derived from mel command `maya.cmds.polyPrimitive`
    """
    pass


def untrim(*args, **kwargs):
    """
    Untrim the surface.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveOnSurface : cos           (bool)          [create]
        If possible, create 2D curve as a result.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          [create,query,edit]
        If set then the operation node will be automatically put into pass-through mode.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).
    
    - untrimAll : all                (bool)          [query,edit]
        if true, untrim all the trims for the surface else untrim only the last trim
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.untrim`
    """
    pass


def detachSurface(*args, **kwargs):
    """
    The detachSurface command detaches a surface into pieces, given a list of
    parameter values and a direction.  You can also specify which pieces to keep and
    which to discard using the -kflag. The names of the newly detached surface(s)
    are returned.  If history is on, the name of the resulting dependency node is
    also returned. You can only detach in either U or V (not both) with a single
    detachSurface operation. You can use this command to open a closed surface at a
    particular parameter value.  You would use this command with only one -pflag. If
    you are specifying -kflags, then you must specify one, none or all -kflags.  If
    you are specifying all -kflags, there must be one more -kflag than -pflags.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - direction : d                  (int)           [create,query,edit]
        Direction in which to detach: 0 - V direction, 1 - U direction Default:1
    
    - frozen : fzn                   (bool)          []
    
    - keep : k                       (bool)          [create,query,edit]
        Keep the detached pieces. Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        Parameter at which to detach. Default:0.0                  Common flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.detachSurface`
    """
    pass


def polyDelEdge(*args, **kwargs):
    """
    Deletes selected edges, and merges neighboring faces. If deletion leaves winged
    vertices, they may be deleted as well. Notice : only non border edges can be
    deleted.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - cleanVertices : cv             (bool)          [create,query,edit]
        If on : delete resulting winged vertices. C: Default is off. Q: When queried,
        this flag returns an int.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyDelEdge`
    """
    pass


def globalStitch(*args, **kwargs):
    """
    This command computes a globalStitch of NURBS surfaces. There should be at least
    one  NURBS surface. The NURBS surface(s) should be untrimmed.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - lockSurface : lk               (bool)          [create,query,edit]
        Keep the NURBS surface at the specified multi index unchanged by the fitting.
        Default:false
    
    - maxSeparation : ms             (float)         [create,query,edit]
        Maximum separation that will still be stitched. Default:0.1
    
    - modificationResistance : mr    (float)         [create,query,edit]
        Modification resistance weight for surface CVs. Default:1e-1
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - replaceOriginal : rpo          (bool)          []
    
    - sampling : sam                 (int)           [create,query,edit]
        Sampling when stitching edges. Default:1
    
    - stitchCorners : sc             (int)           [create,query,edit]
        Stitch corners of surfaces. 0 - off 1 - closest point 2 - closest knot Default:1
    
    - stitchEdges : se               (int)           [create,query,edit]
        Stitch edges of surfaces. 0 - off 1 - closest point 2 - matching params
        Default:1
    
    - stitchPartialEdges : spe       (bool)          [create,query,edit]
        Toggle on (off) partial edge stitching. Default:false
    
    - stitchSmoothness : ss          (int)           [create,query,edit]
        Set type of smoothness of edge join. 0 - off 1 - tangent 2 - normal Default:0
        Common flags
    
    
    Derived from mel command `maya.cmds.globalStitch`
    """
    pass


def polyMergeUV(*args, **kwargs):
    """
    Merge UVs of an object based on their distance. UVs are merge only if they
    belong to the same 3D vertex.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - distance : d                   (float)         [create,query,edit]
        This flag specifies the maximum distance to merge UVs. C: Default is 0.0. Q:
        When queried, this flag returns a double.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMergeUV`
    """
    pass


def boundary(*args, **kwargs):
    """
    This command produces a boundary surface given 3 or 4 curves. This resulting
    boundary surface passes through two of the given curves in one direction, while
    in the other direction the shape is defined by the remaining curve(s).  If the
    endPointoption is on, then the curve endpoints must touch before a surface will
    be created.   This is the usual situation where a boundary surface is useful.
    Note that there is no tangent continuity option with this command. Unless all
    the curve end points are touching, the resulting surface will not pass through
    all curves.  Instead, use the birail command.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - endPoint : ep                  (bool)          [create,query,edit]
        True means the curve ends must touch before a surface will be created.
        Default:false
    
    - endPointTolerance : ept        (float)         [create,query,edit]
        Tolerance for end points, only used if endPoint attribute is true. Default:0.1
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - order : order                  (bool)          [create,query,edit]
        True if the curve order is important. Default:true                  Common flags
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.boundary`
    """
    pass


def polyInstallAction(*args, **kwargs):
    """
    Installs/uninstalls several things to help the user to perform the specified
    action : PickmaskInternal selection constraintsDisplay attributes
    
    Flags:
    - commandName : cn               (bool)          [query]
        return as a string the name of the command previously installed
    
    - convertSelection : cs          (bool)          [create]
        convert all polys selected in object mode into their full matching component
        selection. For example : if a polyMesh is selected, polyInstallAction -cs
        polyCloseBorderwill select all border edges.
    
    - installConstraint : ic         (bool)          [create,query]
        C: install selection pickmask and internal constraints for actionnameQ: returns
        1 if any internal constraint is set for current action
    
    - installDisplay : id            (bool)          [create,query]
        C: install display attributes for actionnameQ: returns 1 if any display is set
        for current action
    
    - keepInstances : ki             (bool)          [create]
        Convert components for all selected instances rather than only the first
        selected instance.
    
    - uninstallConstraint : uc       (bool)          [create]
        uninstall internal constraints previously installed
    
    - uninstallDisplay : ud          (bool)          [create]
        uninstall display attributes previously installed                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyInstallAction`
    """
    pass


def polyMapCut(*args, **kwargs):
    """
    Cut along edges of the texture mapping. The cut edges become map borders.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - moveRatio : mr                 (float)         []
    
    - moveratio : mvr                (float)         [query,edit]
        Cut open ratio related to the neighbor edge length of cut edge.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMapCut`
    """
    pass


def loft(*args, **kwargs):
    """
    This command computes a skinned (lofted) surface passing through a number of
    NURBS curves. There must be at least two curves present. The NURBS curves may be
    surface isoparms, curve on surfaces, trimmed edges or polygon edges.
    
    Flags:
    - autoReverse : ar               (bool)          [create,query,edit]
        If set to true, the direction of the curves for the loft is computed
        automatically.  If set to false, the values of the multi-use reverse flag are
        used instead. Default:true
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - close : c                      (bool)          [create,query,edit]
        If set to true, the resulting surface will be closed (periodic) with the start
        (end) at the first curve.  If set to false, the surface will remain open.
        Default:false
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - createCusp : cc                (bool)          [create,query,edit]
        Multi-use flag; each occurence of the flag refers to the matching curve in the
        loft operation; if the flag is set the particular profile will have a cusp
        (tangent break) in the resulting surface. Default:false
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface Default:3
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.
    
    - rebuild : rb                   (bool)          [create]
        Rebuild the input curve(s) before using them in the operation.  Use
        nurbsCurveRebuildPref to set the parameters for the conversion.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - reverse : r                    (bool)          [create,query,edit]
        Multi-use flag; each occurence of the flag refers to the matching curve in the
        loft operation; if the flag is set the particular curve will be reversed before
        being used in the loft operation. Default:false
    
    - reverseSurfaceNormals : rsn    (bool)          [create,query,edit]
        If set, the surface normals on the output NURBS surface will be reversed.  This
        is accomplished by swapping the U and V parametric directions. Default:false
    
    - sectionSpans : ss              (int)           [create,query,edit]
        The number of surface spans between consecutive curves in the loft. Default:1
    
    - uniform : u                    (bool)          [create,query,edit]
        If set to true, the resulting surface will have uniform parameterization in the
        loft direction.  If set to false, the parameterization will be chord length.
        Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.loft`
    """
    pass


def polySmooth(*args, **kwargs):
    """
    Smooth a polygonal object. This command works on polygonal objects or faces.
    
    Flags:
    - boundaryRule : bnr             (int)           []
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - continuity : c                 (float)         [create,query,edit]
        This flag specifies the smoothness parameter. The minimum value of 0.0 specifies
        that the faces should only be subdivided. Maximum value of 1.0 smooths the faces
        as much as possible. C: Default is 1.0 Q: When queried, this flag returns a
        float.
    
    - degree : deg                   (int)           [create]
        Degree of the resulting limit surface
    
    - divisions : dv                 (int)           [create,query,edit]
        This flag specifies the number of recursive smoothing steps. C: Default is 1. Q:
        When queried, this flag returns an int.
    
    - divisionsPerEdge : dpe         (int)           [create]
        Number of subdivisions along one edge for each step.
    
    - frozen : fzn                   (bool)          []
    
    - keepBorder : kb                (bool)          [create,query,edit]
        If on, the border of the object will not move during smoothing operation. C:
        Default is on. Q: When queried, this flag returns an int.
    
    - keepHardEdge : khe             (bool)          [create,query,edit]
        If true, vertices on hard edges will not be modified. C: Default is false. Q:
        When queried, this flag returns a boolean.
    
    - keepMapBorders : kmb           (int)           [create]
        Treatment of UV map borders 0 - all map border edges will be smoothed 1 - map
        borders that are also geometry borders will be smoothed 2 - no map borders will
        be smoothed
    
    - keepSelectionBorder : ksb      (bool)          [create,query,edit]
        If true, vertices on border of the selection will not be modified. C: Default is
        false. Q: When queried, this flag returns a boolean.
    
    - keepTesselation : xkt          (bool)          [create]
        If true: the object will be smoothed consistently from frame to frame. This is
        best when the object is being deformed or animated . If false: non-starlike
        faces will be triangulated before being smoothed.  This avoids self-overlapping
        faces, but could lead to a change in topology (number of vertices/faces) from
        frame to frame, during an animated deformation.
    
    - keepTessellation : kt          (bool)          [create]
        If true: the object will be smoothed consistently from frame to frame. This is
        best when the object is being deformed or animated . If false: non-starlike
        faces will be triangulated before being smoothed.  This avoids self-overlapping
        faces, but could lead to a change in topology (number of vertices/faces) from
        frame to frame, during an animated deformation.
    
    - method : mth                   (int)           [create]
        Type of smoothing algorithm to use 0 - exponential - traditional smoothing 1 -
        linear - number of faces per edge grows linearly
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flags From The
        polySmoothFacet Node
    
    - osdCreaseMethod : ocr          (int)           [create,query,edit]
        Controls how boundary edges and vertices are interpolated.
    
    - osdFvarBoundary : ofb          (int)           [create,query,edit]
        Controls how boundaries are treated for face-varying data (UVs and Vertex
        Colors).
    
    - osdFvarPropagateCorners : ofc  (bool)          [create,query,edit]
    
    - osdSmoothTriangles : ost       (bool)          [create,query,edit]
        Apply a special subdivision rule be applied to all triangular faces that was
        empirically determined to make triangles subdivide more smoothly.
    
    - osdVertBoundary : ovb          (int)           [create,query,edit]
        Controls how boundary edges and vertices are interpolated.
    
    - propagateEdgeHardness : peh    (bool)          [create,query,edit]
        If true, edges which are a result of smoothed edges will be given the same value
        for their edge hardness.  New subdivided edges will always be smooth. C: Default
        is false. Q: When queried, this flag returns a boolean.
    
    - pushStrength : ps              (float)         [create]
        COMMENT 0.0 is approximation, 1.0 is interpolation scheme
    
    - roundness : ro                 (float)         [create]
        When 1.0, push vectors are renormalized to keep length constant
    
    - smoothUVs : suv                (bool)          [create]
        If true: UVs as well as geometry will be smoothed
    
    - subdivisionLevels : sl         (int)           [create]
        Number of times the subdivide and smooth operation is run.
    
    - subdivisionType : sdt          (int)           [create,query,edit]
        The subdivision method used for smoothing. C: Default is 0. 0: Maya Catmull-
        Clark 1: OpenSubdiv Catmull-Clark                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polySmooth`
    """
    pass


def polyWedgeFace(*args, **kwargs):
    """
    Extrude faces about an axis. The axis is the average of all the selected edges.
    If the edges are not aligned, the wedge may not look intuitive.  To separately
    wedge faces about different wedge axes, the command should be issued as many
    times as the wedge axes. (as in the second example)
    
    Flags:
    - axis : ax                      (float, float, float) [create]
        This flag (along with -center) can be used instead of the -edge flag to specify
        the axis about which the wedge is performed. The flag expects three coordinates
        that form a vector about which the rotation is performed.
    
    - axisX : asx                    (float)         []
    
    - axisY : asy                    (float)         []
    
    - axisZ : asz                    (float)         []
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - center : cen                   (float, float, float) [create]
        This flag (along with -axis) can be used instead of the -edge flag to specify
        the location about which the wedge is performed. The flag expects three
        coordinates that define the center of rotation.
    
    - centerX : ctx                  (float)         []
    
    - centerY : cty                  (float)         []
    
    - centerZ : ctz                  (float)         []
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - divisions : d                  (int)           [create]
        This flag specifies the number of subdivisions along the extrusion.
    
    - edge : ed                      (int)           [create]
        This flag specifies the edgeId that should be used to perform the wedge about.
        Multiple edges can be specified. The wedge operation is performed about an axis
        that is the average of all the edges. It is recommended that only colinear edges
        are used, otherwise the result may not look intuitive. Instead of specifying the
        -edge flag, the wedge can be performed about a point and axis. See the -center
        and -axis flags for details.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - wedgeAngle : wa                (float)         [create]
        This flag specifies the angle of rotation.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyWedgeFace`
    """
    pass


def polyRetopo(*args, **kwargs):
    """
    Retopologize a polygonial surface.
    
    Flags:
    - anisotropy : a                 (float)         []
    
    - anisotropyFilter : af          (float)         []
    
    - caching : cch                  (bool)          []
    
    - constructionHistory : ch       (bool)          []
    
    - curveInfluenceDirection : cid  (float)         []
    
    - curveSingularitySeparation : css (float)         []
    
    - frozen : fzn                   (bool)          []
    
    - geodesicRadius : gr            (float)         []
    
    - magnitudeMin : mm              (float)         []
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           []
    
    - resultRefinementLevel : rrl    (int)           []
    
    - resultSmoothing : rs           (bool)          []
    
    - targetEdgeLengthMax : tea      (float)         []
    
    - targetEdgeLengthMin : tem      (float)         []
    
    - targetFaceCount : tfc          (int)           []
    
    
    Derived from mel command `maya.cmds.polyRetopo`
    """
    pass


def attachCurve(*args, **kwargs):
    """
    This attach command is used to attach curves. Once the curves are attached,
    there will be multiple knots at the joined point(s). These can be kept or
    removed if the user wishes. If there are two curves, the end of the first curve
    is attached to the start of the second curve. If there are more than two curves,
    closest endpoints are joined. Note: if the command is done with Keep Original
    off, the first curve is replaced by the attached curve. All other curves will
    remain, the command does not delete them.
    
    Flags:
    - blendBias : bb                 (float)         [create,query,edit]
        Skew the result toward the first or the second curve depending on the blend
        factory being smaller or larger than 0.5. Default:0.5
    
    - blendKnotInsertion : bki       (bool)          [create,query,edit]
        If set to true, insert a knot in one of the original curves (relative position
        given by the parameter attribute below) in order to produce a slightly different
        effect. Default:false
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - keepMultipleKnots : kmk        (bool)          [create,query,edit]
        If true, keep multiple knots at the join parameter. Otherwise remove them.
        Default:true
    
    - method : m                     (int)           [create,query,edit]
        Attach method (connect-0, blend-1) Default:0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        The parameter value for the positioning of the newly inserted knot. Default:0.1
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - reverse1 : rv1                 (bool)          [create,query,edit]
        If true, reverse the first input curve before doing attach. Otherwise, do
        nothing to the first input curve before attaching. NOTE: setting this attribute
        to random values will cause unpredictable results and is not supported.
        Default:false
    
    - reverse2 : rv2                 (bool)          [create,query,edit]
        If true, reverse the second input curve before doing attach. Otherwise, do
        nothing to the second input curve before attaching. NOTE: setting this attribute
        to random values will cause unpredictable results and is not supported.
        Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.attachCurve`
    """
    pass


def offsetSurface(*args, **kwargs):
    """
    The offset command creates new offset surfaces from the selected surfaces. The
    default method is a surface offset, which offsets relative to the surface
    itself. The CV offset method offsets the CVs directly rather than the surface,
    so is usually slightly less accurate but is faster. The offset surface will
    always have the same degree, number of CVs and knot spacing as the original
    surface.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - distance : d                   (float)         [create,query,edit]
        Offset distance Default:1.0
    
    - frozen : fzn                   (bool)          []
    
    - method : m                     (int)           [create,query,edit]
        Offset method 0 - Surface Fit 1 - CV Fit Default:0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.offsetSurface`
    """
    pass


def subdMapCut(*args, **kwargs):
    """
    Cut along edges of the texture mapping. The cut edges become map borders.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.subdMapCut`
    """
    pass


def polyBevel3(*args, **kwargs):
    """
    Bevel edges.
    
    Flags:
    - angleTolerance : at            (float)         [create,query,edit]
        Angular tolerance for creation of extra triangles Note this attribute is for
        compatability only and should not be modified in Maya 7.0 files Default:20.0
    
    - autoFit : af                   (bool)          [create,query,edit]
        If autoFit is on, it computes a smooth roundness :  new facets round off a
        smooth angle. Default:true
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - chamfer : c                    (bool)          [create,query,edit]
        If chamfer is on, the surface is smoothed out at bevels. When it is off, the
        shape of the surface remains the same. Default:true
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - depth : d                      (float)         [create,query,edit]
        The depth of bevel. One means a smooth surface, -1 means maximum depth.
        Default:1.0
    
    - fillNgons : fn                 (bool)          [create,query,edit]
        Subdivide new faces with more than 4 edges Default:false
    
    - forceParallel : fp             (bool)          []
    
    - fraction : f                   (float)         []
    
    - frozen : fzn                   (bool)          []
    
    - maya2015 : m15                 (bool)          []
    
    - maya2016SP3 : m16              (bool)          []
    
    - maya2017Update1 : m17          (bool)          []
    
    - mergeVertexTolerance : mvt     (float)         [create,query,edit]
        Tolerance within which to merge vertices Default:0.0
    
    - mergeVertices : mv             (bool)          [create,query,edit]
        Merge vertices within a tolerance Default:false
    
    - miterAlong : mia               (int)           [create,query,edit]
        Controls in which direction new vertices should we offseted. Default:0
    
    - mitering : m                   (int)           [create,query,edit]
        Controls how the topology should look like at corners. Default:0
    
    - miteringAngle : ma             (float)         [create,query,edit]
        Miter faces that have angles less than this value Default:0.0
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - offset : o                     (float)         [create,query,edit]
        The offset for bevel. Default:0.2
    
    - offsetAsFraction : oaf         (bool)          [create,query,edit]
        If on, the offset value is treated as a fraction between zero and one.
        Default:false
    
    - roundness : r                  (float)         [create,query,edit]
        The roundness of bevel, it is taken into account when autoFit is off.
        Default:0.5
    
    - segments : sg                  (int)           [create,query,edit]
        The number of segments used for beveling. Default:1
    
    - smoothingAngle : sa            (float)         [create,query,edit]
        Create new edges as hard edges if the angle between adjacent faces exceeds this
        value Default:0.0
    
    - subdivideNgons : sn            (bool)          []
    
    - uvAssignment : ua              (int)           [create,query,edit]
        Technique used to compute UVs on new faces 0 computes new UVs by projecting
        along surface normal of original mesh onto new mesh 1 computes new UVs by
        projecting along surface normal of new mesh onto original mesh Default:0
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyBevel3`
    """
    pass


def nurbsSquare(*args, **kwargs):
    """
    The nurbsSquare command creates a square
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - center : c                     (float, float, float) [create,query,edit]
        The center point of the square.
    
    - centerX : cx                   (float)         [create,query,edit]
        X of the center point. Default:0
    
    - centerY : cy                   (float)         [create,query,edit]
        Y of the center point. Default:0
    
    - centerZ : cz                   (float)         [create,query,edit]
        Z of the center point. Default:0
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting circle: 1 - linear, 2 - quadratic, 3 - cubic, 5 -
        quintic, 7 - heptic Default:3
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - normal : nr                    (float, float, float) [create,query,edit]
        The normal of the plane in which the square will lie.
    
    - normalX : nrx                  (float)         [create,query,edit]
        X of the normal direction. Default:0
    
    - normalY : nry                  (float)         [create,query,edit]
        Y of the normal direction. Default:0
    
    - normalZ : nrz                  (float)         [create,query,edit]
        Z of the normal direction. Default:1
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - sideLength1 : sl1              (float)         [create,query,edit]
        The length of a side on the square. Default:1.0
    
    - sideLength2 : sl2              (float)         [create,query,edit]
        The length of an adjacent side on the square. Default:1.0
    
    - spansPerSide : sps             (int)           [create,query,edit]
        The number of spans per side determines the resolution of the square. Default:1
        Common flags
    
    
    Derived from mel command `maya.cmds.nurbsSquare`
    """
    pass


def polyCone(*args, **kwargs):
    """
    The cone command creates a new polygonal cone.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the cone. Q: When queried,
        this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize3: Normalize and
        Preserve Aspect RatioDefault:2
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - height : h                     (float)         [create,query,edit]
        Height of the cone. Default:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - radius : r                     (float)         [create,query,edit]
        Radius of the cone. Default:1.0
    
    - roundCap : rcp                 (bool)          [create,query,edit]
        To indicate whether we need a round cap Default:false
    
    - subdivisionsAxis : sa          (int)           [create,query,edit]
        Subdivisions around the axis. Default:20
    
    - subdivisionsCap : sc           (int)           [create,query,edit]
        Subdivisions on the bottom cap. Default:0
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height. Default:1
    
    - subdivisionsX : sx             (int)           [create,query,edit]
        This specifies the number of subdivisions in the X direction for the cone. C:
        Default is 20. Q: When queried, this flag returns an int.
    
    - subdivisionsY : sy             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Y direction for the cone.
        C: Default is 1. Q: When queried, this flag returns an int.
    
    - subdivisionsZ : sz             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Z direction for the cone.
        C: Default is 0. Q: When queried, this flag returns an int.
    
    - texture : tx                   (bool)          [create,query,edit]
        Apply texture or not. Default:true                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCone`
    """
    pass


def nurbsCube(*args, **kwargs):
    """
    The nurbsCube command creates a new NURBS Cube made up of six planes. It creates
    an unit cube with center at origin by default.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        The primitive's axis
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface. 1 - linear, 2 - quadratic, 3 - cubic, 5 -
        quintic, 7 - heptic Default:3
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - heightRatio : hr               (float)         [create,query,edit]
        Ratio of heightto widthDefault:1.0
    
    - lengthRatio : lr               (float)         [create,query,edit]
        Ratio of lengthto widthDefault:1.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - patchesU : u                   (int)           [create,query,edit]
        Number of sections in U Default:1
    
    - patchesV : v                   (int)           [create,query,edit]
        Number of sections in V Default:1
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The primitive's pivot point
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    - width : w                      (float)         [create,query,edit]
        Width of the object Default:1.0                  Common flags
    
    
    Derived from mel command `maya.cmds.nurbsCube`
    """
    pass


def polyExtrudeEdge(*args, **kwargs):
    """
    Extrude edges separately or together.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createCurve : cc               (bool)          [create]
        If true then the operation can create a curve.
    
    - divisions : d                  (int)           [create,query,edit]
        How many internal edges are creating when pulling. Default:1
    
    - frozen : fzn                   (bool)          []
    
    - gain : ga                      (float)         [create,query,edit]
        Gain factor per component. Can be painted using Artisan. Default:1.0
    
    - inputCurve : inc               (PyNode)        [create]
        This flag specifies the name of the curve to be used as input for the operation.
    
    - keepFacesTogether : kft        (bool)          [create,query,edit]
        How to extrude edges. If on, extruded faces produced from the edges being
        extruded will be kept together. Otherwise they are pulled independently.
        Default:true
    
    - localCenter : lc               (int)           [create,query,edit]
        Local center on the edge : 0=Middle point, 1=Start point, 2=End point. Default:0
    
    - localDirection : ld            (float, float, float) [create,query,edit]
        Direction to determine X axis for local space. Default:1.0, 0.0, 0.0
    
    - localDirectionX : ldx          (float)         [create,query,edit]
        X coord of the X axis.
    
    - localDirectionY : ldy          (float)         [create,query,edit]
        Y coord of the X axis.
    
    - localDirectionZ : ldz          (float)         [create,query,edit]
        Z coord of the X axis.
    
    - localRotate : lr               (float, float, float) [create,query,edit]
        The local rotations. Default:0.0, 0.0, 0.0
    
    - localRotateX : lrx             (float)         [create,query,edit]
        Local rotate X coord. The range is [0, 360].
    
    - localRotateY : lry             (float)         [create,query,edit]
        Local rotate Y coord. The range is [0, 360].
    
    - localRotateZ : lrz             (float)         [create,query,edit]
        Local rotate Z coord : Rotation along the normal. The range is [0, 360].
    
    - localScale : ls                (float, float, float) [create,query,edit]
        Local Scale. Default:1.0, 1.0, 1.0
    
    - localScaleX : lsx              (float)         [create,query,edit]
        Scale X coord.
    
    - localScaleY : lsy              (float)         [create,query,edit]
        Scale Y coord.
    
    - localScaleZ : lsz              (float)         [create,query,edit]
        Scale Z coord.
    
    - localTranslate : lt            (float, float, float) [create,query,edit]
        Local translate. Default:0.0, 0.0, 0.0
    
    - localTranslateX : ltx          (float)         [create,query,edit]
        Local translation X coord.
    
    - localTranslateY : lty          (float)         [create,query,edit]
        Local translation Y coord.
    
    - localTranslateZ : ltz          (float)         [create,query,edit]
        Local translation Z coord : Move along the normal.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - offset : off                   (float)         [create,query,edit]
        Edges are moved this distance in the opposite direction of the edge. Default:0.0
    
    - pivot : pvt                    (float, float, float) [create,query,edit]
        The pivot for scaling and rotation. Default:0.0, 0.0, 0.0
    
    - pivotX : pvx                   (float)         [create,query,edit]
        Pivot X coord.
    
    - pivotY : pvy                   (float)         [create,query,edit]
        Pivot Y coord.
    
    - pivotZ : pvz                   (float)         [create,query,edit]
        Pivot Z coord.
    
    - random : ran                   (float)         [create,query,edit]
        Random value for all parameters. Default:0.0
    
    - rotate : ro                    (float, float, float) [create,query,edit]
        Rotation angles around X, Y, Z. Default:0.0, 0.0, 0.0
    
    - rotateX : rx                   (float)         [create,query,edit]
        Rotation angle around X.
    
    - rotateY : ry                   (float)         [create,query,edit]
        Rotation angle around Y.
    
    - rotateZ : rz                   (float)         [create,query,edit]
        Rotation angle around Z.
    
    - scale : s                      (float, float, float) [create,query,edit]
        Scaling vector. Default:1.0, 1.0, 1.0
    
    - scaleX : sx                    (float)         [create,query,edit]
        Scale X coord.
    
    - scaleY : sy                    (float)         [create,query,edit]
        Scale Y coord.
    
    - scaleZ : sz                    (float)         [create,query,edit]
        Scale Z coord.
    
    - smoothingAngle : sma           (float)         [create,query,edit]
        Angle below which new edges will be smoothed Default:kPi/6.0
    
    - taper : tp                     (float)         [create,query,edit]
        Taper or Scale along the extrusion path Default:1.0
    
    - taperCurve_FloatValue : cfv    (float)         [create,query,edit]
        ?????
    
    - taperCurve_Interp : ci         (int)           [create,query,edit]
        ????? Default:0
    
    - taperCurve_Position : cp       (float)         [create,query,edit]
        ?????
    
    - thickness : tk                 (float)         [create,query,edit]
        Edges are moved this distance in the direction of the connected face normals.
        Default:0.0f
    
    - translate : t                  (float, float, float) [create,query,edit]
        Translation vector. Default:0.0, 0.0, 0.0
    
    - translateX : tx                (float)         [create,query,edit]
        Translation X coord.
    
    - translateY : ty                (float)         [create,query,edit]
        Translation Y coord.
    
    - translateZ : tz                (float)         [create,query,edit]
        Translation Z coord.
    
    - twist : twt                    (float)         [create,query,edit]
        Twist or Rotation along the extrusion path Default:0.0
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyExtrudeEdge`
    """
    pass


def curve(*args, **kwargs):
    """
    The curve command creates a new curve from a list of control vertices (CVs).  A
    string is returned containing the pathname to the newly created curve.  You can
    create a curve from points either in world space or object (local) space, either
    with weights or without. You can replace an existing curve by using the
    -r/replaceflag.  You can append a point to an existing curve by using the
    -a/appendflag. To create a curve-on-surface, use the curveOnSurface command. To
    change the degree of a curve, use the rebuildCurve command. To change the of
    parameter range curve, use the rebuildCurve command.
    
    Flags:
    - append : a                     (bool)          [create]
        Appends point(s) to the end of an existing curve. If you use this flag, you must
        specify the name of the curve to append to, at the end of the command.  (See
        examples below.)
    
    - bezier : bez                   (bool)          [create]
        The created curve will be a bezier curve.
    
    - degree : d                     (float)         [create]
        The degree of the new curve.  Default is 3.  Note that you need (degree+1) curve
        points to create a visible curve span.  eg. you must place 4 points for a degree
        3 curve.
    
    - editPoint : ep                 (float, float, float) [create]
        The x, y, z position of an edit point.  linearmeans that this flag can take
        values with units.  This flag can not be used with the -point or the
        -pointWeight flags.
    
    - knot : k                       (float)         [create]
        A knot value in a knot vector.  One flag per knot value. There must be
        (numberOfPoints + degree - 1) knots and the knot vector must be non-decreasing.
    
    - name : n                       (unicode)       [create]
        Name of the curve
    
    - objectSpace : os               (bool)          [create]
        Points are in object, or localspace.  This is the default. You cannot specify
        both -osand -wsin the same command.
    
    - periodic : per                 (bool)          [create]
        If on, creates a curve that is periodic.  Default is off.
    
    - point : p                      (float, float, float) [create]
        The x, y, z position of a point.  linearmeans that this flag can take values
        with units.
    
    - pointWeight : pw               (float, float, float, float) [create]
        The x,y,z and w values of a point, where the w is a weight value. A rational
        curve will be created if this flag is used. linearmeans that this flag can take
        values with units.
    
    - replace : r                    (bool)          [create]
        Replaces an entire existing curve. If you use this flag, you must specify the
        name of the curve to replace, at the end of the command.  (See examples below.)
    
    - worldSpace : ws                (bool)          [create]
        Points are in world space.  The default is -os. You cannot specify both -osand
        -wsin the same command.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.curve`
    """
    pass


def polyProjectCurve(*args, **kwargs):
    """
    The polyProjectCurve command creates curves by projecting a selected curve onto
    a selected poly mesh.  The direction of projection will be the current view
    direction unless the direction vector is specified with the -direction/-d flag.
    
    Flags:
    - addUnderTransform : aut        (bool)          [create]
        True if the resulting curve should be added under the source transform
    
    - automatic : automatic          (bool)          []
    
    - baryCoord : bc                 (float, float, float) []
    
    - baryCoord1 : bc1               (float)         []
    
    - baryCoord2 : bc2               (float)         []
    
    - baryCoord3 : bc3               (float)         []
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          []
    
    - curveSamples : cs              (int)           []
    
    - direction : d                  (float, float, float) [create,query,edit]
        Direction of projection.
    
    - directionX : dx                (float)         [create,query,edit]
        X direction of projection.
    
    - directionY : dy                (float)         [create,query,edit]
        Y direction of projection.
    
    - directionZ : dz                (float)         [create,query,edit]
        Z direction of projection.
    
    - face : f                       (int)           []
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          []
    
    - pointsOnEdges : poe            (bool)          []
    
    - tolerance : tol                (float)         [create,query,edit]
        Tolerance to fit to.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    - triangle : t                   (int)           []
    
    
    Derived from mel command `maya.cmds.polyProjectCurve`
    """
    pass


def polyPrism(*args, **kwargs):
    """
    The prism command creates a new polygonal prism.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the prism. Q: When queried,
        this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create]
        This flag alows a specific UV mechanism to be selected, while creating the
        primitive. The valid values are 0, 1,  2 or 3. 0 implies that no UVs will be
        generated (No texture to be applied). 1 implies UVs should be created for the
        object as a whole without any normalization. The primitive will be unwrapped and
        then the texture will be applied without any distortion. In the unwrapped
        primitive, the shared edges will have shared UVs. 2 implies the UVs should be
        normalized. This will normalize the U and V direction separately, thereby
        resulting in distortion of textures. 3 implies UVs are created so that the
        texture will not be distorted when applied. The texture lying outside the UV
        range will be truncated (since that cannot be squeezed in, without distorting
        the texture. For better understanding of these options, you may have to open the
        texture view windowC: Default is 2.
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - length : l                     (float)         [create,query,edit]
        This flag specifies the length of the prism. C: Default is 2.0. Q: When queried,
        this flag returns a float.
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - numberOfSides : ns             (int)           [create,query,edit]
        This specifies the number of sides for the prism. C: Default is 3. Q: When
        queried, this flag returns an int.
    
    - numderOfSides : nsi            (int)           [create,query,edit]
        This specifies the number of sides for the prism. C: Default is 3. Q: When
        queried, this flag returns an int.
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - sideLength : w                 (float)         [create,query,edit]
        This flag specifies the edge length of the prism. C: Default is 2.0. Q: When
        queried, this flag returns a float.
    
    - subdivisionsCaps : sc          (int)           [create,query,edit]
        This flag specifies the subdivisions on the caps for the prism. C: Default is 2.
        Q: When queried, this flag returns an int.
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        This specifies the subdivisions along the height for the prism. C: Default is 1.
        Q: When queried, this flag returns an int.
    
    - texture : tx                   (int)           [create]
        This flag is obsolete and will be removed in the next release. The
        -cuv/createUVs flag should be used instead.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyPrism`
    """
    pass


def subdCleanTopology(*args, **kwargs):
    """
    Command cleans topology of subdiv surfaces - at all levels. It cleans the
    geometry of vertices that satisfy the following conditions:                 -
    Zero edits                 - Default uvs (uvs obtained by subdividing parent
    face).                 - No creases.
    
    
    Derived from mel command `maya.cmds.subdCleanTopology`
    """
    pass


def polyPinUV(*args, **kwargs):
    """
    This command is used to pin and unpin UVs. A pinnedUV is one which should not be
    modified.  Each UV has an associated pin weight, that defaults to 0.0 meaning
    that the UV is not pinned. If pin weight is set to 1.0 then it becomes fully
    pinned and UV tools should not modify that UV. If the pin weight is set to a
    value between 0.0 and 1.0 then UV tools should weight their changes to that UV
    accordingly.  UV pinning is not enforced by the shape node: it is up to each
    tool to decide whether it will obey the pin weights.
    
    Flags:
    - createHistory : ch             (bool)          [create,query,edit]
        For objects that have no construction history, this flag can be used to force
        the creation of construction history for pinning.  By default, history is not
        created if the object has no history.  Regardless of this flag, history is
        always created if the object already has history.
    
    - operation : op                 (int)           [create,query,edit]
        Operation to perform.  Valid values are: 0: Set pin weights on the selected UVs.
        1: Set pin weights to zero for the selected UVs. 2: Remove pin weights from the
        entire mesh. 3: Invert pin weights of the entire mesh. Default is 0.
    
    - unpinned : unp                 (bool)          [query,edit]
        List all selected UVs which are not pinned.
    
    - uvSetName : uvs                (unicode)       [create,query,edit]
        Specifies the name of the UV set to edit UVs on. If not specified the current UV
        set will be used if it exists.
    
    - value : v                      (float)         [create,query,edit]
        Specifies the pin value for the selected UV components. When specified multiple
        times, the values are assigned respectively to the specified UVs.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyPinUV`
    """
    pass


def trim(*args, **kwargs):
    """
    This command trims a surface to its curves on surface by first splitting the
    surface and then selecting which regions to keep or discard.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - locatorU : lu                  (float)         [create,query,edit]
        u parameter value to position a locator on the surface. Default:0.5
    
    - locatorV : lv                  (float)         [create,query,edit]
        v parameter value to position a locator on the surface. Default:0.5
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - replaceOriginal : rpo          (bool)          []
    
    - selected : sl                  (int)           [create,query,edit]
        Specify whether to keep or discard selected regions. Default:0
    
    - shrink : sh                    (bool)          [create,query,edit]
        If true, shrink underlying surface to outer boundaries of trimmed surface.
        Default:false
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to trim. Default:0.001                  Common flags
    
    
    Derived from mel command `maya.cmds.trim`
    """
    pass


def insertKnotCurve(*args, **kwargs):
    """
    The insertKnotCurve command inserts knots into a curve given a list of parameter
    values. The number of knots to add at each parameter value and whether the knots
    are added or complemented can be specified. The name of the curve is returned.
    If construction history is on, the name of the resulting dependency node is also
    returned. An edit point will appear where you insert the knot. Also, the number
    of spans and CVs in the curve will increase in the area where the knot is
    inserted. You can insert up to degreeknots at a curve parameter that isn't
    already an edit point. eg. for a degree three curve, you can insert up to 3
    knots. Use this operation if you need more CVs in a local area of the curve. Use
    this operation (or hardenPoint) if you want to create a corner in a curve.
    
    Flags:
    - addKnots : add                 (bool)          [create,query,edit]
        Whether to add knots or complement.  Complement means knots will be added to
        reach the specified number of knots. Default:true
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveOnSurface : cos           (bool)          [create]
        If possible, create 2D curve as a result.
    
    - frozen : fzn                   (bool)          []
    
    - insertBetween : ib             (bool)          [create,query,edit]
        If set to true, and there is more than one parameter value specified, the knots
        will get inserted at equally spaced intervals between the given parameter
        values, rather than at the parameter values themselves. Default:false
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - numberOfKnots : nk             (int)           [create,query,edit]
        How many knots to insert.  At any point on the curve, there can be a maximum of
        degreeknots. Default:1
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        Parameter value(s) where knots are added Default:0.0                  Common
        flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.insertKnotCurve`
    """
    pass


def polyCylinder(*args, **kwargs):
    """
    The cylinder command creates a new polygonal cylinder.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the cylinder. Q: When
        queried, this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize3: Normalize and
        Preserve Aspect RatioDefault:2
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - height : h                     (float)         [create,query,edit]
        Height of the cylinder. Default:2.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - radius : r                     (float)         [create,query,edit]
        Radius of the cylinder. Default:1.0
    
    - roundCap : rcp                 (bool)          [create,query,edit]
        To indicate whether we need a round cap Default:false
    
    - subdivisionsAxis : sa          (int)           [create,query,edit]
        Subdivisions around the axis. Default:20
    
    - subdivisionsCaps : sc          (int)           [create,query,edit]
        Subdivisions on the caps Default:0
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height. Default:1
    
    - subdivisionsX : sx             (int)           [create,query,edit]
        This specifies the number of subdivisions in the X direction for the cylinder.
        C: Default is 20. Q: When queried, this flag returns an int.
    
    - subdivisionsY : sy             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Y direction for the
        cylinder. C: Default is 1. Q: When queried, this flag returns an int.
    
    - subdivisionsZ : sz             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Z direction for the
        cylinder. C: Default is 1. Q: When queried, this flag returns an int.
    
    - texture : tx                   (int)           [create,query,edit]
        What texture mechanism to be applied 0=No textures, 1=Object, 2=Faces Default:2
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCylinder`
    """
    pass


def polyConnectComponents(*args, **kwargs):
    """
    Splits polygon edges according to the selected components. The selected
    components are gathered into connected 'paths' that define continuous splits.
    Mixed components (vertices, edges and faces) can be used at once. The connection
    rules are: \* Edges can connect to other edges in the same face or to vertices
    in the same face (that are not in the edge itself) or to faces connected to
    other edges in the same face. \* Vertices can connect to edges (as above) or to
    vertices in the same face (that are not joined to the first vertex by an edge)
    or to faces adjacent to a face that uses the vertex (except those that also use
    the vertex). \* Faces can connect to vertices or edges (as above) or to adjacent
    faces.
    
    Flags:
    - adjustEdgeFlow : aef           (float)         [create,query,edit]
        The weight value of the edge vertices to be positioned.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - insertWithEdgeFlow : ief       (bool)          [create,query,edit]
        True to enable edge flow. Otherwise, the edge flow is disabled.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyConnectComponents`
    """
    pass


def polyClean(*args, **kwargs):
    """
    polyClean will attempt to remove components that are invalid in the description
    of a poly mesh.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - cleanEdges : ce                (bool)          [create,query,edit]
        If true, the operation will look for and delete edges that are not associated
        with any face in the mesh.
    
    - cleanPartialUVMapping : cpm    (bool)          [create,query,edit]
        If true, the operation will look for any faces on the mesh that do not have
        complete UV mapping.  Maya requires that all vertices that make up a mesh face
        have valid UV data associated with them, or that none of the vertices withing
        the face have associated UVs.
    
    - cleanUVs : cuv                 (bool)          [create,query,edit]
        If true, the operation will look for and delete UVs that are not associated with
        any face in the mesh.
    
    - cleanVertices : cv             (bool)          [create,query,edit]
        If true, the operation will look for and delete vertices that are not associated
        with any face in the mesh.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          [create,query,edit]
        Toggle frozen state for a particular node to keep current evaluation state and
        prevent any other indirect changes to it.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyClean`
    """
    pass


def polySplit(*args, **kwargs):
    """
    Split facets/edges of a polygonal object. The first and last arguments must be
    edges. Intermediate points may lie on either a shared face or an edge which
    neighbors the previous point.
    
    Flags:
    - adjustEdgeFlow : aef           (float)         [create,query,edit]
        The weight value of the edge vertices to be positioned.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - detachEdges : de               (bool)          [create]
        Value of the detachEdges attribute for the resulting poly split node.
    
    - edgepoint : ep                 (int, float)    [create]
        The given edge is split into two new edges by inserting a new vertex located the
        given percentage along the edge. Note:This flag is not recommended for use from
        Python.  See the insertpoint flag instead.
    
    - facepoint : fp                 (int, float, float, float) [create]
        A new vertex is inserted, lying at the given coordinates inside the given face.
        Coordinates are given in the local object space. Note:This flag is not
        recommended for use from Python.  See the insertpoint flag instead.
    
    - insertWithEdgeFlow : ief       (bool)          [create,query,edit]
        True to enable edge flow. Otherwise, the edge flow is disabled.
    
    - insertpoint : ip               (int, float, float, float) [create]
        This flag allows the caller to insert a new vertex into an edge or a face. To
        insert a new vertex in an edge, pass the index of the edge and a percentage
        along the edge at which to insert the new vertex.  When used to insert a vertex
        into an edge, this flag takes two arguments. To insert a new vertex into a face,
        pass the index of the face and three values which define the coordinates for the
        insertion in local object space.  When used to insert a vertex into a face, this
        flag takes four arguments. This flag replaces the edgepoint and facepoint flags.
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    - projectedCurve : pc            (PyNode)        [create]
        Curves to be projected.
    
    - projectedCurveTolerance : pct  (float)         [create]
        Tolerance for curve projection.
    
    - smoothingangle : sma           (float)         [create]
        Subdivide new edges will be soft if less then this angle. C: Default is 0.0
    
    - subdivision : s                (int)           [create,query,edit]
        Subdivide new edges into the given number of sections. Edges involving free
        points won't be subdivided. C: Default is 1 (no subdivision). Q: When queried,
        this flag returns an int.                  Common poly creation operation flags
    
    
    Derived from mel command `maya.cmds.polySplit`
    """
    pass


def polySewEdge(*args, **kwargs):
    """
    Merge border edges within a given threshold.Perform pair-wise comparison of
    selected edges. Pairs whose corresponding vertices meet threshold conditions and
    whose orientations are aligned (i.e. their respective normals point in the same
    direction) are merged, as are the vertices (in other words, vertices are
    shared). Resulting mesh may have extra vertices or edges to ensure geometry is
    valid. Edges must be on the same object to be merged. Default : share only
    vertices lying exactly at the same place. (polySewEdge -t 0.0)
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - texture : tx                   (bool)          [create,query,edit]
        If true : texture is sewn as well as the 3d edge. C: Default is true. Q: When
        queried, this flag returns an int.
    
    - tolerance : t                  (float)         [create,query,edit]
        The tolerance to sew edges (edge distance) C: Default is 0.0. Q: When queried,
        this flag returns a float.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polySewEdge`
    """
    pass


def polyNormalizeUV(*args, **kwargs):
    """
    Normalizes the UVs of input polyFaces. The existing UVs of the faces are
    normalized between 0 and 1.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - centerOnTile : cot             (bool)          [create,query,edit]
        If true, will center UV's on the UV tile they are most over. If false, will
        center UV's in the 0-1 region.
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createNewMap : cm              (bool)          [create]
        Set to true if a new map should be created
    
    - frozen : fzn                   (bool)          []
    
    - insertBeforeDeformers : ibd    (bool)          [create]
        Set to true if the new node created should inserted before any deformer nodes.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - normalizeDirection : nd        (int)           [create,query,edit]
        Scale along U or V or both. 0UV1U2VC:  Default is 0. Q:  When queried, returns
        an int.
    
    - normalizeType : nt             (int)           [create,query,edit]
        Options for normalize. 0Separate1CollectiveC:  Default is 1. Q:  When queried,
        returns an int.
    
    - preserveAspectRatio : pa       (bool)          [create,query,edit]
        Scale uniform along u and v. C: Default is on. Q: When queried, returns an int.
        Common poly modifier operation flags
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyNormalizeUV`
    """
    pass


def bevel(*args, **kwargs):
    """
    The bevel command creates a new bevel surface for the specified curve. The curve
    can be any nurbs curves.
    
    Flags:
    - bevelShapeType : bst           (int)           [create,query,edit]
        Shape type: 1 - straight cut, 2 - curve out, 3 - curve in Default:1
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - cornerType : ct                (int)           [create,query,edit]
        Corner type: 1 - linear, 2 - circular Default:2
    
    - depth : d                      (float)         [create,query,edit]
        The depth for bevel Default:0.5
    
    - extrudeDepth : ed              (float)         [create,query,edit]
        The extrude depth for bevel Default:1.0
    
    - frozen : fzn                   (bool)          []
    
    - joinSurfaces : js              (bool)          [create,query,edit]
        Attach bevelled surfaces into one surface for each input curve. Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - numberOfSides : ns             (int)           [create,query,edit]
        How to apply the bevel. 1 - no bevels2 - bevel at start only3 - bevel at end
        only4 - bevel at start and endDefault:4
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance for bevel offsets Default:0.01
    
    - width : w                      (float)         [create,query,edit]
        The width for bevel Default:0.5                  Common flags
    
    
    Derived from mel command `maya.cmds.bevel`
    """
    pass


def alignCurve(*args, **kwargs):
    """
    The curve align command is used to align curves in maya. The main alignment
    options are positional, tangent and curvature continuity. Curvature continuity
    implies tangent continuity. Positional continuity means the curves (move) or the
    ends of the curves (modify) are changed. Tangent continuity means one of the
    curves is modified to be tangent at the points where they meet. Curvature
    continuity means one of the curves is modified to be curvature continuous as
    well as tangent. The default behaviour, when no curves or flags are passed, is
    to only do positional and tangent continuity on the active list with the end of
    the first curve and the start of the other curve used for alignment.
    
    Flags:
    - attach : at                    (bool)          [create]
        True if the curve is to be attached
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curvatureContinuity : cc       (bool)          [create,query,edit]
        Curvature continuity is on if true and off otherwise. Default:false
    
    - curvatureScale1 : cs1          (float)         [create,query,edit]
        Curvature scale applied to curvature of first curve for curvature continuity.
        Default:0.0
    
    - curvatureScale2 : cs2          (float)         [create,query,edit]
        Curvature scale applied to curvature of second curve for curvature continuity.
        Default:0.0
    
    - frozen : fzn                   (bool)          []
    
    - joinParameter : jnp            (float)         [create,query,edit]
        Parameter on reference curve where modified curve is to be aligned to.
        Default:123456.0
    
    - keepMultipleKnots : kmk        (bool)          [create]
        True if multiple knots should be left as-is.
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - positionalContinuity : pc      (bool)          [create,query,edit]
        Positional continuity is on if true and off otherwise. Default:true
    
    - positionalContinuityType : pct (int)           [create,query,edit]
        Positional continuity type legal values: 1 - move first curve, 2 - move second
        curve, 3 - move both curves, 4 - modify first curve, 5 - modify second curve, 6
        - modify both curves Default:1
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - reverse1 : rv1                 (bool)          [create,query,edit]
        If true, reverse the first input curve before doing align. Otherwise, do nothing
        to the first input curve before aligning. NOTE: setting this attribute to random
        values will cause unpredictable results and is not supported. Default:false
    
    - reverse2 : rv2                 (bool)          [create,query,edit]
        If true, reverse the second input curve before doing align. Otherwise, do
        nothing to the second input curve before aligning. NOTE: setting this attribute
        to random values will cause unpredictable results and is not supported.
        Default:false
    
    - tangentContinuity : tc         (bool)          [create,query,edit]
        Tangent continuity is on if true and off otherwise. Default:true
    
    - tangentContinuityType : tct    (int)           [create,query,edit]
        Tangent continuity type legal values: 1 - do tangent continuity on first curve,
        2 - do tangent continuity on second curve Default:1
    
    - tangentScale1 : ts1            (float)         [create,query,edit]
        Tangent scale applied to tangent of first curve for tangent continuity.
        Default:1.0
    
    - tangentScale2 : ts2            (float)         [create,query,edit]
        Tangent scale applied to tangent of second curve for tangent continuity.
        Default:1.0                  Common flags
    
    
    Derived from mel command `maya.cmds.alignCurve`
    """
    pass


def subdLayoutUV(*args, **kwargs):
    """
    Move UVs in the texture plane to avoid overlaps.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - flipReversed : fr              (bool)          [create,query,edit]
        If this flag is turned on, the reversed UV pieces are fliped.
    
    - frozen : fzn                   (bool)          []
    
    - layout : l                     (int)           [create,query,edit]
        How to move the UV pieces, after cuts are applied: 0 No move is applied. 1
        Layout the pieces along the U axis. 2 Layout the pieces in a square shape.
    
    - layoutMethod : lm              (int)           [create,query,edit]
        Which layout method to use: 0 Block Stacking. 1 Shape Stacking.
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - percentageSpace : ps           (float)         [create,query,edit]
        When layout is set to square, this value is a percentage of the texture area
        which is added around each UV piece. It can be used to ensure each UV piece uses
        different pixels in the texture. Maximum value is 5 percent.
    
    - rotateForBestFit : rbf         (int)           [create,query,edit]
        0 No rotation is applied. 1 Only allow 90 degree rotations. 2 Allow free
        rotations.
    
    - scale : sc                     (int)           [create,query,edit]
        How to scale the pieces, after move and cuts: 0 No scale is applied. 1 Uniform
        scale to fit in unit square. 2 Non proportional scale to fit in unit square.
    
    - separate : se                  (int)           [create,query,edit]
        Which UV edges should be cut: 0 No cuts. 1 Cut only along folds. 2 Make all
        necessary cuts to avoid all intersections.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        If true, performs the operation in world space coordinates as opposed to local
        space.                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.subdLayoutUV`
    """
    pass


def extendCurve(*args, **kwargs):
    """
    This command extends a curve or creates a new curve as an extension
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveOnSurface : cos           (bool)          [create]
        If possible, create 2D curve as a result.
    
    - distance : d                   (float)         [create,query,edit]
        The distance to extend Used only for extendMethod is byDistance. Default:1
    
    - extendMethod : em              (int)           [create,query,edit]
        The method with which to extend: 0 - based on distance, 2 - to a 3D point
        Default:0
    
    - extensionType : et             (int)           [create,query,edit]
        The type of extension: 0 - linear, 1 - circular, 2 - extrapolate Default:0
    
    - frozen : fzn                   (bool)          []
    
    - inputPoint : ip                (float, float, float) [create,query,edit]
        The point to extend to (optional)
    
    - join : jn                      (bool)          [create,query,edit]
        If true, join the extension to original curve Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          [create,query,edit]
        If set then the operation node will be automatically put into pass-through mode.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pointX : px                    (float)         [create,query,edit]
        X of the point to extend to Default:0
    
    - pointY : py                    (float)         [create,query,edit]
        Y of the point to extend to Default:0
    
    - pointZ : pz                    (float)         [create,query,edit]
        Z of the point to extend to Default:0
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.
    
    - removeMultipleKnots : rmk      (bool)          [create,query,edit]
        If true remove multiple knots at join Used only if join is true. Default:false
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - start : s                      (int)           [create,query,edit]
        Which end of the curve to extend. 0 - end, 1 - start, 2 - both Default:1
        Common flags
    
    
    Derived from mel command `maya.cmds.extendCurve`
    """
    pass


def polyColorPerVertex(*args, **kwargs):
    """
    Command associates color(rgb and alpha) with vertices on polygonal objects. When
    used with the query flag, it returns the color associated with the specified
    components.
    
    Flags:
    - alpha : a                      (float)         [create,query,edit]
        Specifies the alpha channel of color
    
    - clamped : cla                  (bool)          [create,query,edit]
        This flag specifies if the color set will truncate any value that is outside 0
        to 1 range.
    
    - colorB : b                     (float)         [create,query,edit]
        Specifies the B channel of color
    
    - colorDisplayOption : cdo       (bool)          [create,query,edit]
        Change the display options on the mesh to display the vertex colors.
    
    - colorG : g                     (float)         [create,query,edit]
        Specifies the G channel of color
    
    - colorR : r                     (float)         [create,query,edit]
        Specifies the R channel of color
    
    - colorRGB : rgb                 (float, float, float) [create,query,edit]
        Specifies the RGB channels of color
    
    - notUndoable : nun              (bool)          [create,query,edit]
        Execute the command, but without having the command be undoable. This option
        will greatly improve performance for large numbers of object. This will make the
        command not undoable regardless of whether undo has been enabled or not.
    
    - relative : rel                 (bool)          [create,query,edit]
        When used, the color values specified are added relative to the current values.
    
    - remove : rem                   (bool)          [create,query,edit]
        When used, the color values are removed from the selected or specified objects
        or components. This option only supports meshes with no construction history, or
        meshes whose construction history includes a recent polyColorPerVertexNode. For
        meshes whose construction history includes a polgon operation the
        polyColorPerVertexNode, consider using the polyColorDel command instead
    
    - representation : rpt           (int)           [create,query,edit]
        This flag corresponds to the color channels to used, for example A(alpha only),
        RGB, and RGBA.                             Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyColorPerVertex`
    """
    pass


def circle(*args, **kwargs):
    """
    The circle command creates a circle or partial circle (arc)
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - center : c                     (float, float, float) [create,query,edit]
        The center point of the circle.
    
    - centerX : cx                   (float)         [create,query,edit]
        X of the center point. Default:0
    
    - centerY : cy                   (float)         [create,query,edit]
        Y of the center point. Default:0
    
    - centerZ : cz                   (float)         [create,query,edit]
        Z of the center point. Default:0
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting circle: 1 - linear, 3 - cubic Default:3
    
    - first : fp                     (float, float, float) [create,query,edit]
        The start point of the circle if fixCenter is false. Determines the orientation
        of the circle if fixCenter is true.
    
    - firstPointX : fpx              (float)         [create,query,edit]
        X of the first point. Default:1
    
    - firstPointY : fpy              (float)         [create,query,edit]
        Y of the first point. Default:0
    
    - firstPointZ : fpz              (float)         [create,query,edit]
        Z of the first point. Default:0
    
    - fixCenter : fc                 (bool)          [create,query,edit]
        Fix the center of the circle to the specified center point. Otherwise the circle
        will start at the specified first point. Default:true
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - normal : nr                    (float, float, float) [create,query,edit]
        The normal of the plane in which the circle will lie.
    
    - normalX : nrx                  (float)         [create,query,edit]
        X of the normal direction. Default:0
    
    - normalY : nry                  (float)         [create,query,edit]
        Y of the normal direction. Default:0
    
    - normalZ : nrz                  (float)         [create,query,edit]
        Z of the normal direction. Default:1
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - radius : r                     (float)         [create,query,edit]
        The radius of the circle. Default:1.0
    
    - sections : s                   (int)           [create,query,edit]
        The number of sections determines the resolution of the circle. Used only if
        useTolerance is false. Default:8
    
    - sweep : sw                     (float)         [create,query,edit]
        The sweep angle determines the completeness of the circle. A full circle is 2Pi
        radians, or 360 degrees. Default:6.2831853
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to build a circle. Used only if useTolerance is true
        Default:0.01
    
    - useTolerance : ut              (bool)          [create,query,edit]
        Use the specified tolerance to determine resolution. Otherwise number of
        sections will be used. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.circle`
    """
    pass


def polySplitRing(*args, **kwargs):
    """
    Splits a series of ring edges of connected quads and inserts connecting edges
    between them.
    
    Flags:
    - adjustEdgeFlow : aef           (float)         [create,query,edit]
        The weight value of the edge vertices to be positioned. Default:1.0f
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - direction : dr                 (bool)          [create,query,edit]
        This attribute is used when doing an absolute split.  If true then the distance
        is taken from the start vertex of the root edge.  If false the distance is taken
        from the end vertext of the root edge. Default:true
    
    - divisions : div                (int)           [create,query,edit]
        Number of divisions. Default:2
    
    - enableProfileCurve : epc       (bool)          [create,query,edit]
        Enables the use of the profile curve. Default:true
    
    - fixQuads : fq                  (bool)          [create,query,edit]
        Fixes splits which go across a quad face leaving a 5 and 3 sided faces by
        splitting from the middle of the new edge to the vertex accross from the edge on
        the 5 sided face. Default:false
    
    - frozen : fzn                   (bool)          []
    
    - insertWithEdgeFlow : ief       (bool)          [create,query,edit]
        True to enable edge flow. Otherwise, the edge flow is disabled. Default:false
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - profileCurveInputOffset : pio  (float)         [create,query,edit]
        Changes the offset to the multisplit profile curve. eg. if the profile curve
        values go between 0 and 1 and this value is set to -1 then the profile curves
        values will be adjusted to go between -1 and 0. Default:0.0f
    
    - profileCurveInputScale : pis   (float)         [create,query,edit]
        Changes the range of values that the profile curve represents. eg. if the
        profile curve values go between 0 and 1 and this value is set to 2 then the
        profile curves values will be adjusted to go between 0 and 2. Default:1.0f
    
    - profileCurve_FloatValue : pfv  (float)         [create,query,edit]
        ?????
    
    - profileCurve_Interp : pi       (int)           [create,query,edit]
        ????? Default:0
    
    - profileCurve_Position : pp     (float)         [create,query,edit]
        ?????
    
    - rootEdge : re                  (int)           [create,query,edit]
        The weight attribute uses the start vertex of this edge to determine where the
        new split occurs. Default:-1
    
    - smoothingAngle : sma           (float)         [create,query,edit]
        Angle below which new edges will be smoothed Default:kPi
    
    - splitType : stp                (int)           [create,query,edit]
        Format: 0 - Absolute, 1 - Relative, 2 - Multi Default:TdnpolySplitRing::Relative
    
    - useEqualMultiplier : uem       (bool)          [create,query,edit]
        Changes how the profile curve effects the offset when doing a multisplit.  If
        true then the verts will be offset the same distance based on the shortest edge
        being split.  If false then each inserted edge loop will be offset a distance
        relative to the length of the edge that is being split. Default:true
    
    - useFaceNormalsAtEnds : fne     (bool)          [create,query,edit]
        When doing a multisplit on a set of non-closed edge ring this will toggle the
        normals at the ends of the split to be calculated as the edge normal or the face
        normal. Default:true
    
    - weight : wt                    (float)         [create,query,edit]
        Weight value controlling the relative positioning of the new points on existing
        edges. Range is [0.0, 1.0]. Value of 0.1 indicates the new edges will be placed
        closer to the start vertex of the first edge of the sequence of edges.
        Default:0.5
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polySplitRing`
    """
    pass


def polyPoke(*args, **kwargs):
    """
    Introduces a new vertex in the middle of the selected face, and connects it to
    the rest of the vertices of the face.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - localTranslate : lt            (float, float, float) [create]
        Translate the new vertex in the local face coordinate.
    
    - localTranslateX : ltx          (float)         [create]
        Translate the new vertex in the local face coordinate along X.
    
    - localTranslateY : lty          (float)         [create]
        Translate the new vertex in the local face coordinate along Y.
    
    - localTranslateZ : ltz          (float)         [create]
        Translate the new vertex in the local face coordinate along Z.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - translate : t                  (float, float, float) [create]
        Translate the new vertex in the world space.
    
    - translateX : tx                (float)         [create]
        Translate the new vertex in the world space along X.
    
    - translateY : ty                (float)         [create]
        Translate the new vertex in the world space along Y.
    
    - translateZ : tz                (float)         [create]
        Translate the new vertex in the world space along Z.
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyPoke`
    """
    pass


def angleBetween(*args, **kwargs):
    """
    Returns the axis and angle required to rotate one vector onto another. If the
    construction history (ch) flag is ON, then the name of the new dependency node
    is returned.
    
    Flags:
    - caching : cch                  (bool)          [create]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - euler : er                     (bool)          [create]
        return the rotation as 3 Euler angles instead of axis + angle
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - vector1 : v1                   (float, float, float) [create]
        vector from which to compute the rotation
    
    - vector1X : v1x                 (float)         [create]
        X coordinate of the vector from which to compute the rotation
    
    - vector1Y : v1y                 (float)         [create]
        Y coordinate of the vector from which to compute the rotation
    
    - vector1Z : v1z                 (float)         [create]
        Z coordinate of the vector from which to compute the rotation
    
    - vector2 : v2                   (float, float, float) [create]
        vector to which to compute the rotation
    
    - vector2X : v2x                 (float)         [create]
        X coordinate of the vector to which to compute the rotation
    
    - vector2Y : v2y                 (float)         [create]
        Y coordinate of the vector to which to compute the rotation
    
    - vector2Z : v2z                 (float)         [create]
        Z coordinate of the vector to which to compute the rotation
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.angleBetween`
    """
    pass


def reverseCurve(*args, **kwargs):
    """
    The reverseCurve command reverses the direction of a curve or curve-on-surface.
    A string is returned containing the pathname of the newly reversed curve and the
    name of the resulting dependency node.  The reversed curve has the same
    parameter range as the original curve.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveOnSurface : cos           (bool)          [create]
        If possible, create 2D curve as a result.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - range : rn                     (bool)          [create]
        Force a curve range on complete input curve.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.reverseCurve`
    """
    pass


def polyDuplicateEdge(*args, **kwargs):
    """
    Duplicates a series of connected edges (edgeLoop)
    
    Flags:
    - adjustEdgeFlow : aef           (float)         [create,query,edit]
        The weight value of the edge vertices to be positioned.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - deleteEdge : de                (bool)          [create,query,edit]
        When true, the end edges are deleted so the end triangles are converted to
        quads.
    
    - endVertexOffset : evo          (float)         [create,query,edit]
        Weight value controlling the offset of the end vertex of the edgeloop.
    
    - frozen : fzn                   (bool)          []
    
    - insertWithEdgeFlow : ief       (bool)          [create,query,edit]
        True to enable edge flow. Otherwise, the edge flow is disabled.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - offset : of                    (float)         [create]
        Weight value controlling the relative positioning of the new edges. The range of
        values is [0.0, 1.0].
    
    - smoothingAngle : sma           (float)         [create,query,edit]
        Angle below which new edges will be smoothed
    
    - splitType : stp                (int)           [create,query,edit]
        Format: 0 - Absolute, 1 - Relative, 2 - Multi
    
    - startVertexOffset : svo        (float)         [create,query,edit]
        Weight value controlling the offset of the start vertex of the edgeloop.
        Common poly modifier operation flags
    
    
    Derived from mel command `maya.cmds.polyDuplicateEdge`
    """
    pass


def transferAttributes(*args, **kwargs):
    """
    Samples the attributes of a source surface (first argument) and transfers them
    onto a target surface (second argument).
    
    Flags:
    - after : af                     (bool)          [create,edit]
        If the default behavior for insertion/appending into/onto the existing chain is
        not the desired behavior then this flag can be used to force the command to
        place the deformer node after the selected node in the chain even if a new
        geometry shape has to be created in order to do so. Works in create mode (and
        edit mode if the deformer has no geometry added yet).
    
    - afterReference : ar            (bool)          [create,edit]
        The -afterReference flag is used to specify deformer ordering in a hybrid way
        that choses between -before and -after automatically. If the geometry being
        deformed is referenced then the -after mode is used when adding the new
        deformer, otherwise the -before mode is used. The net effect when using
        -afterReference to build deformer chains is that internal shape nodes in the
        deformer chain will only appear at reference file boundaries, leading to
        lightweight deformer networks that may be more amicable to reference swapping.
    
    - before : bf                    (bool)          [create,edit]
        If the default behavior for insertion/appending into/onto the existing chain is
        not the desired behavior then this flag can be used to force the command to
        place the deformer node before the selected node in the chain even if a new
        geometry shape has to be created in order to do so. Works in create mode (and
        edit mode if the deformer has no geometry added yet).
    
    - colorBorders : clb             (int)           [create,edit]
        Controls whether color borders are preserved when transferring color data. If
        this is non-zero, any color borders will be mapped onto the nearest edge on the
        target geometry. 0 means any color borders will be smoothly blended onto the
        vertices of the target geometry.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
    - flipUVs : fuv                  (int)           [create,edit]
        Controls how sampled UV data is flipped before being transferred to the target.
        0 means no flipping; 1 means UV data is flipped in the U direction; 2 means UV
        data is flipped in the V direction; and 3 means it is flipped in both
        directions. In conjunction with mirroring, this allows the creation of symmetric
        UV mappings (e.g. the left hand side of the character on one side of the UV map,
        the right hand side on the other).
    
    - frontOfChain : foc             (bool)          [create,edit]
        This command is used to specify that the new deformer node should be placed
        ahead (upstream) of existing deformer and skin nodes in the shape's history (but
        not ahead of existing tweak nodes). The input to the deformer will be the
        upstream shape rather than the visible downstream shape, so the behavior of this
        flag is the most intuitive if the downstream deformers are in their reset
        (hasNoEffect) position when the new deformer is added. Works in create mode (and
        edit mode if the deformer has no geometry added yet).
    
    - geometry : g                   (unicode)       [query,edit]
        The specified object will be added to the list of objects being deformed by this
        deformer object, unless the -rm flag is also specified. When queried, this flag
        returns string string string ...
    
    - geometryIndices : gi           (bool)          [query]
        Complements the -geometry flag in query mode. Returns the multi index of each
        geometry.
    
    - ignoreSelected : ignoreSelected (bool)          [create]
        Tells the command to not deform objects on the current selection list
    
    - includeHiddenSelections : ihs  (bool)          [create]
        Apply the deformer to any visible and hidden objects in the selection list.
        Default is false.
    
    - matchChoice : mch              (int)           [create,edit]
        When using topological component matching, selects between possible matches. If
        the meshes involved in the transfer operation have symmetries in their
        topologies, there may be more than one possible topological match. Maya scores
        the possible matches (by comparing the shapes of the meshes) and assigns them an
        index, starting at zero. Match zero, the default, is considered the best, but in
        the event that Maya chooses the wrong one, changing this value will allow the
        user to explore the other matches.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - parallel : par                 (bool)          [create,edit]
        Inserts the new deformer in a parallel chain to any existing deformers in the
        history of the object. A blendShape is inserted to blend the parallel results
        together. Works in create mode (and edit mode if the deformer has no geometry
        added yet).
    
    - prune : pr                     (bool)          [edit]
        Removes any points not being deformed by the deformer in its current
        configuration from the deformer set.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - sampleSpace : spa              (int)           [create,edit]
        Selects which space the attribute transfer is performed in. 0 is world space, 1
        is model space, 4 is component-based, 5 is topology-based. The default is world
        space.
    
    - searchMethod : sm              (int)           [create,edit]
        Specifies which search method to use when correlating points. 0 is closest along
        normal, 3 is closest to point. The default is closest to point.
    
    - searchScaleX : ssx             (float)         [create,edit]
        Specifies an optional scale that should be applied to the x-axis of the target
        model before transferring data. A value of 1.0 (the default) means no scaling; a
        value of -1.0 would indicate mirroring along the x-axis.
    
    - searchScaleY : ssy             (float)         [create,edit]
        Specifies an optional scale that should be applied to the y-axis of the target
        model before transferring data. A value of 1.0 (the default) means no scaling; a
        value of -1.0 would indicate mirroring along the y-axis.
    
    - searchScaleZ : ssz             (float)         [create,edit]
        Specifies an optional scale that should be applied to the z-axis of the target
        model before transferring data. A value of 1.0 (the default) means no scaling; a
        value of -1.0 would indicate mirroring along the z-axis.
    
    - sourceColorSet : scs           (unicode)       [create]
        Specifies the name of a single color set on the source surface(s) that should be
        transferred to the target. This value is only used when the operation is
        configured to transfer a single color set (see the transferColors flag).
    
    - sourceUvSet : suv              (unicode)       [create]
        Specifies the name of a single UV set on the source surface(s) that should be
        transferred to the target. This value is only used when the operation is
        configured to transfer a single UV set (see the transferUVs flag).
    
    - sourceUvSpace : sus            (unicode)       [create]
        Specifies the name of the UV set on the source surface(s) that should be used as
        the transfer space. This value is only used when the operation is configured to
        transfer attributes in UV space.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - targetColorSet : tcs           (unicode)       [create]
        Specifies the name of a single color set on the target surface that should be
        receive the sampled color data. This value is only used when the operation is
        configured to transfer a single color set (see the transferColors flag).
    
    - targetUvSet : tuv              (unicode)       [create]
        Specifies the name of a single UV set on the target surface that should be
        receive the sampled UV data. This value is only used when the operation is
        configured to transfer a single UV set (see the transferUVs flag).
    
    - targetUvSpace : tus            (unicode)       [create]
        Specifies the name of the UV set on the target surface( that should be used as
        the transfer space. This value is only used when the operation is configured to
        transfer attributes in UV space.
    
    - transferColors : col           (int)           [create,edit]
        Controls color set transfer. 0 means no color sets are transferred, 1 means that
        a single color set (specified by sourceColorSet and targetColorSet) is
        transferred, and 2 means that all color sets are transferred.
    
    - transferNormals : nml          (int)           [create,edit]
        A non-zero value indicates vertex normals should be sampled and written into
        user normals on the target surface.
    
    - transferPositions : pos        (int)           [create,edit]
        A non-zero value indicates vertex position should be sampled, causing the target
        surface to wrapto the source surface(s).
    
    - transferUVs : uvs              (int)           [create,edit]
        Controls UV set transfer. 0 means no UV sets are transferred, 1 means that a
        single UV set (specified by sourceUVSet and targetUVSet) is transferred, and 2
        means that all UV sets are transferred.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.transferAttributes`
    """
    pass


def polyChipOff(*args, **kwargs):
    """
    Extract facets. Faces can be extracted separately or together, and manipulations
    can be performed either in world or object space.
    
    Flags:
    - attraction : att               (float)         [create,query,edit]
        Attraction, related to magnet. The range is [-2.0, 2.0]. Default:0.0
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - duplicate : dup                (bool)          [create,query,edit]
        If on, facets are duplicated, otherwise original facets are removed. C: Default
        is on. Q: When queried, this flag returns an int.
    
    - frozen : fzn                   (bool)          []
    
    - gain : ga                      (float)         [create,query,edit]
        Gain factor per component. Can be painted using Artisan. Default:1.0
    
    - gravity : g                    (float, float, float) [create,query,edit]
        The gravity vector. Default:0.0, -1.0, 0.0
    
    - gravityX : gx                  (float)         [create,query,edit]
        Gravity X coord.
    
    - gravityY : gy                  (float)         [create,query,edit]
        Gravity Y coord.
    
    - gravityZ : gz                  (float)         [create,query,edit]
        Gravity Z coord.
    
    - keepFacesTogether : kft        (bool)          [create,query,edit]
        How to extrude edges. If on, extruded faces produced from the edges being
        extruded will be kept together. Otherwise they are pulled independently.
        Default:true
    
    - keepFacetTogether : xft        (bool)          [create,query,edit]
        How to extrude edges. If on, extruded faces produced from the edges being
        extruded will be kept together. Otherwise they are pulled independently.
        Default:true
    
    - localCenter : lc               (int)           [create,query,edit]
        Local center on the edge : 0=Middle point, 1=Start point, 2=End point. Default:0
    
    - localDirection : ld            (float, float, float) [create,query,edit]
        Direction to determine X axis for local space. Default:1.0, 0.0, 0.0
    
    - localDirectionX : ldx          (float)         [create,query,edit]
        X coord of the X axis.
    
    - localDirectionY : ldy          (float)         [create,query,edit]
        Y coord of the X axis.
    
    - localDirectionZ : ldz          (float)         [create,query,edit]
        Z coord of the X axis.
    
    - localRotate : lr               (float, float, float) [create,query,edit]
        The local rotations. Default:0.0, 0.0, 0.0
    
    - localRotateX : lrx             (float)         [create,query,edit]
        Local rotate X coord. The range is [0, 360].
    
    - localRotateY : lry             (float)         [create,query,edit]
        Local rotate Y coord. The range is [0, 360].
    
    - localRotateZ : lrz             (float)         [create,query,edit]
        Local rotate Z coord : Rotation along the normal. The range is [0, 360].
    
    - localScale : ls                (float, float, float) [create,query,edit]
        Local Scale. Default:1.0, 1.0, 1.0
    
    - localScaleX : lsx              (float)         [create,query,edit]
        Scale X coord.
    
    - localScaleY : lsy              (float)         [create,query,edit]
        Scale Y coord.
    
    - localScaleZ : lsz              (float)         [create,query,edit]
        Scale Z coord.
    
    - localTranslate : lt            (float, float, float) [create,query,edit]
        Local translate. Default:0.0, 0.0, 0.0
    
    - localTranslateX : ltx          (float)         [create,query,edit]
        Local translation X coord.
    
    - localTranslateY : lty          (float)         [create,query,edit]
        Local translation Y coord.
    
    - localTranslateZ : ltz          (float)         [create,query,edit]
        Local translation Z coord : Move along the normal.
    
    - magnX : mx                     (float)         [create,query,edit]
        Magnet X coord.
    
    - magnY : my                     (float)         [create,query,edit]
        Magnet Y coord.
    
    - magnZ : mz                     (float)         [create,query,edit]
        Magnet Z coord.
    
    - magnet : m                     (float, float, float) [create,query,edit]
        The magnet vector. Default:0.0, 0.0, 0.0
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - offset : off                   (float)         [create,query,edit]
        Local offset. Faces are moved this distance towards the inside of the face.
        Default:0.0
    
    - pivot : pvt                    (float, float, float) [create,query,edit]
        The pivot for scaling and rotation. Default:0.0, 0.0, 0.0
    
    - pivotX : pvx                   (float)         [create,query,edit]
        Pivot X coord.
    
    - pivotY : pvy                   (float)         [create,query,edit]
        Pivot Y coord.
    
    - pivotZ : pvz                   (float)         [create,query,edit]
        Pivot Z coord.
    
    - random : ran                   (float)         [create,query,edit]
        Random value for all parameters. Default:0.0
    
    - rotate : ro                    (float, float, float) []
    
    - rotateX : rx                   (float)         []
    
    - rotateY : ry                   (float)         []
    
    - rotateZ : rz                   (float)         []
    
    - scale : s                      (float, float, float) [create,query,edit]
        Scaling vector. Default:1.0, 1.0, 1.0
    
    - scaleX : sx                    (float)         [create,query,edit]
        Scale X coord.
    
    - scaleY : sy                    (float)         [create,query,edit]
        Scale Y coord.
    
    - scaleZ : sz                    (float)         [create,query,edit]
        Scale Z coord.
    
    - translate : t                  (float, float, float) [create,query,edit]
        Translation vector. Default:0.0, 0.0, 0.0
    
    - translateX : tx                (float)         [create,query,edit]
        Translation X coord.
    
    - translateY : ty                (float)         [create,query,edit]
        Translation Y coord.
    
    - translateZ : tz                (float)         [create,query,edit]
        Translation Z coord.
    
    - weight : w                     (float)         [create,query,edit]
        The weight, related to gravity. Default:0.0
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyChipOff`
    """
    pass


def polyMapSew(*args, **kwargs):
    """
    Sew border edges in texture space. Selected edges must be map borders.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMapSew`
    """
    pass


def fitBspline(*args, **kwargs):
    """
    The fitBspline command fits the CVs from an input curve and and returns a 3D
    curve.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - frozen : fzn                   (bool)          []
    
    - keepRange : kr                 (int)           []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    - tolerance : tol                (float)         [create,query,edit]
        Tolerance for the fit.  The resulting curve will be kept within tolerance of the
        given points. Default:0.1                  Common flags
    
    
    Derived from mel command `maya.cmds.fitBspline`
    """
    pass


def polyCollapseEdge(*args, **kwargs):
    """
    Turns each selected edge into a point.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCollapseEdge`
    """
    pass


def polyUnite(*args, **kwargs):
    """
    This command creates a new poly as an union of a list of polys If no objects are
    specified in the command line, then the objects from the active list are used.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - centerPivot : cp               (bool)          [create]
        Set the resulting object's pivot to the center of the selected objects bounding
        box.
    
    - constructionHistory : ch       (bool)          []
    
    - frozen : fzn                   (bool)          []
    
    - mergeUVSets : muv              (int)           [create]
        Specify how UV sets will be merged on the output mesh. The choices are 0 | 1 |
        2. 0 = Do not merge. Each UV set on each mesh will become a new UV set in the
        output. 1 = Merge by name. UV sets with the same name will be merged. 2 = Merge
        by UV links. UV sets will be merged so that UV linking on the input meshes
        continues to work. The default is 1 (merge by name).
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - object : o                     (bool)          []
    
    - objectPivot : op               (bool)          [create]
        Set the resulting object's pivot to last selected object's pivot.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyUnite`
    """
    pass


def polyBoolOp(*args, **kwargs):
    """
    This command creates a new poly as the result of a boolean operation on input
    polys : union, intersection, difference. Only for difference, the order of the
    selected objects is important : result = object1 - object2. If no objects are
    specified in the command line, then the objects from the active list are used.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - classification : cls           (int)           []
    
    - constructionHistory : ch       (bool)          []
    
    - faceAreaThreshold : fat        (float)         [create,query,edit]
        Area threshold to determine whether faces should be collapsed before boolean.
        Attribute is ignored unless useThresholds is set to true Default:0.0001
    
    - frozen : fzn                   (bool)          []
    
    - mergeUVSets : muv              (int)           [create,query,edit]
        Specify how UV sets will be merged on the output mesh. 0 = No Merge: Each UV set
        on each mesh will become a new UV set in the output.1 = Merge By Name: UV sets
        with the same name will be merged.2 = Merge By UV Links: UV sets will be merged
        so that UV linking on the input meshes continues to work.The default is merge by
        name.
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - object : o                     (bool)          []
    
    - operation : op                 (int)           [create,query,edit]
        Boolean operation type. 1=union, 2=difference, 3=intersection. Default type is
        union. Default:kBoolOpUnion
    
    - preserveColor : pcr            (bool)          [create,query,edit]
        If true, boolean op will compute color for the new mesh. If false, the new mesh
        won't have any color set. Default:false
    
    - useThresholds : uth            (bool)          [create,query,edit]
        If true, merge vertices with separations less then vertexDistanceThreshold and
        collapse faces with areas less then faceAreaThreshold. If false, do not merge
        vertices or collapse faces Default:false
    
    - vertexDistanceThreshold : vdt  (float)         [create,query,edit]
        Tolerance to determine whether vertices (and edges) should be merged before
        boolean operation is applied. Attribute is ignored unless useThresholds is set
        to true Default:0.001                  Flags from polyCBoolOpFlags From
        polyUnite Node
    
    
    Derived from mel command `maya.cmds.polyBoolOp`
    """
    pass


def curveIntersect(*args, **kwargs):
    """
    You must specify two curves to intersect. This command either returns the
    parameter values at which the given pair of curves intersect, or returns a
    dependency node that provides the intersection information. If you want to find
    the intersection of the curves in a specific direction you must use BOTH the
    -useDirectionflag and the directionflag.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - direction : d                  (float, float, float) [query,edit]
        The direction that the input curves are projected in before intersecting.  This
        vector is only used if useDirectionflag is true.
    
    - directionX : dx                (float)         [query,edit]
        The X component of the direction that the input curves are projected in before
        intersecting.  This vector is only used if useDirectionflag is true.
    
    - directionY : dy                (float)         [query,edit]
        The Y component of the direction that the input curves are projected in before
        intersecting.  This vector is only used if useDirectionflag is true.
    
    - directionZ : dz                (float)         [query,edit]
        The Z component of the direction that the input curves are projected in before
        intersecting.  This vector is only used if useDirectionflag is true.
    
    - frozen : fzn                   (bool)          []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - tolerance : tol                (float)         [query,edit]
        The tolerance that the intersection is calculated with. For example, given two
        curves end-to-end, the ends must be within tolerance for an intersection to be
        returned. Default:0.001
    
    - useDirection : ud              (bool)          [query,edit]
        If true, use direction flag.  The input curves are first projected in a
        specified direction and then intersected. If false, this command will only find
        true 3D intersections. Default:false                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.curveIntersect`
    """
    pass


def polyNormalPerVertex(*args, **kwargs):
    """
    Command associates normal(x, y, z) with vertices on polygonal objects. When used
    with the query flag, it returns the normal associated with the specified
    components. However, when queried, the command returns all normals (all vtx-face
    combinations) on the vertex, regardless of whether they are shared or not.
    
    Flags:
    - allLocked : al                 (bool)          [create,query,edit]
        Queries if all normals on the selected vertices are locked (frozen) or not
    
    - deformable : deformable        (bool)          [create,query,edit]
        DEFAULT  true OBSOLETE flag. This flag will be removed in the next release.
    
    - freezeNormal : fn              (bool)          [create,query,edit]
        Specifies that the normal values be frozen (locked) at the current value.
    
    - normalX : x                    (float)         [create,query,edit]
        Specifies the x value normal
    
    - normalXYZ : xyz                (float, float, float) [create,query,edit]
        Specifies the xyz values normal If this flag is used singly, the specified
        normal xyz values are used for all selected components. If the flag is used
        multiple times, the number of uses must match the number of selected components,
        and each use specifies the normal of one component.
    
    - normalY : y                    (float)         [create,query,edit]
        Specifies the y value normal
    
    - normalZ : z                    (float)         [create,query,edit]
        Specifies the z value normal
    
    - relative : rel                 (bool)          [create,query,edit]
        When used, the normal values specified are added relative to the current value.
    
    - unFreezeNormal : ufn           (bool)          [create,query,edit]
        Specifies that the normal values that were frozen at the current value be un-
        frozen (un-locked).                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyNormalPerVertex`
    """
    pass


def plane(*args, **kwargs):
    """
    The command creates a sketch plane (also known as a construction plane) in
    space.  To create an object (such as a NURBS curve, joint chain or polygon) on a
    construction plane, you need to first make the plane live. See also the makeLive
    command.
    
    Flags:
    - length : l                     (float)         [create]
        The length of plane. linearmeans that this flag can handle values with units.
    
    - name : n                       (unicode)       [create]
        Name the resulting object.
    
    - position : p                   (float, float, float) [create]
        3D position where the centre of the plane is positioned. linearmeans that this
        flag can handle values with units.
    
    - rotation : r                   (float, float, float) [create]
        The rotation of plane. anglemeans that this flag can handle values with units.
    
    - size : s                       (float)         [create]
        The combined size (size x size) of plane. linearmeans that this flag can handle
        values with units.
    
    - width : w                      (float)         [create]
        The width of plane. linearmeans that this flag can handle values with units.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.plane`
    """
    pass


def polySeparate(*args, **kwargs):
    """
    This command creates new objects from the given poly. A new object will be
    created for each section of the mesh that is distinct (no edges connect it to
    the rest of the mesh). This command can only separate one object at a time.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          []
    
    - endFace : ef                   (int)           []
    
    - frozen : fzn                   (bool)          []
    
    - inPlace : inp                  (bool)          []
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          []
    
    - removeShells : rs              (bool)          [create]
        Remove the shells after creation.
    
    - separateSpecificShell : sss    (int)           [create]
        List of shell ids to be separated.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - startFace : sf                 (int)           []
    
    - userSpecifiedShells : uss      (bool)          []
    
    
    Derived from mel command `maya.cmds.polySeparate`
    """
    pass


def polyBevel(*args, **kwargs):
    """
    Bevel edges.
    
    Flags:
    - angleTolerance : at            (float)         [create,query,edit]
        Angular tolerance for creation of extra triangles Note this attribute is for
        compatability only and should not be modified in Maya 7.0 files Default:20.0
    
    - autoFit : af                   (bool)          [create,query,edit]
        If autoFit is on, it computes a smooth roundness :  new facets round off a
        smooth angle. Default:true
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - fillNgons : fn                 (bool)          []
    
    - fraction : f                   (float)         []
    
    - frozen : fzn                   (bool)          []
    
    - maya2015 : m15                 (bool)          []
    
    - mergeVertexTolerance : mvt     (float)         [create,query,edit]
        Tolerance within which to merge vertices Default:0.0
    
    - mergeVertices : mv             (bool)          [create,query,edit]
        Merge vertices within a tolerance Default:false
    
    - miteringAngle : ma             (float)         [create,query,edit]
        Miter faces that have angles less than this value Default:0.0
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - offset : o                     (float)         [create,query,edit]
        The offset for bevel. Default:0.2
    
    - offsetAsFraction : oaf         (bool)          [create,query,edit]
        If on, the offset value is treated as a fraction between zero and one.
        Default:false
    
    - roundness : r                  (float)         [create,query,edit]
        The roundness of bevel, it is taken into account when autoFit is off.
        Default:0.5
    
    - segments : sg                  (int)           [create,query,edit]
        The number of segments used for beveling. Default:1
    
    - smoothingAngle : sa            (float)         [create,query,edit]
        Create new edges as hard edges if the angle between adjacent faces exceeds this
        value Default:0.0
    
    - subdivideNgons : sn            (bool)          [create,query,edit]
        Subdivide new faces with more than 4 edges Default:false
    
    - useLegacyBevelAlgorithm : com  (bool)          [create,query,edit]
        If on, bevel is done the way maya 2014 did Default:false
    
    - uvAssignment : ua              (int)           [create,query,edit]
        Technique used to compute UVs on new faces 0 computes new UVs by projecting
        along surface normal of original mesh onto new mesh 1 computes new UVs by
        projecting along surface normal of new mesh onto original mesh Default:0
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyBevel`
    """
    pass


def polyLayoutUV(*args, **kwargs):
    """
    Move UVs in the texture plane to avoid overlaps.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - flipReversed : fr              (bool)          [create,query,edit]
        If this flag is turned on, the reversed UV pieces are fliped.
    
    - frozen : fzn                   (bool)          []
    
    - gridU : gu                     (int)           []
    
    - gridV : gv                     (int)           []
    
    - layout : l                     (int)           [create,query,edit]
        How to move the UV pieces, after cuts are applied: 0 No move is applied. 1
        Layout the pieces along the U axis. 2 Layout the pieces in a square shape.
    
    - layoutMethod : lm              (int)           [create,query,edit]
        Which layout method to use: 0 Block Stacking. 1 Shape Stacking.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - percentageSpace : ps           (float)         [create,query,edit]
        When layout is set to square, this value is a percentage of the texture area
        which is added around each UV piece. It can be used to ensure each UV piece uses
        different pixels in the texture. Maximum value is 5 percent.
    
    - rotateForBestFit : rbf         (int)           [create,query,edit]
        0 No rotation is applied. 1 Only allow 90 degree rotations. 2 Allow free
        rotations.
    
    - scale : sc                     (int)           [create,query,edit]
        How to scale the pieces, after move and cuts: 0 No scale is applied. 1 Uniform
        scale to fit in unit square. 2 Non proportional scale to fit in unit square.
    
    - separate : se                  (int)           [create,query,edit]
        Which UV edges should be cut: 0 No cuts. 1 Cut only along folds. 2 Make all
        necessary cuts to avoid all intersections.
    
    - uvSetName : uvs                (unicode)       [create]
        Name of the UV set to be created
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyLayoutUV`
    """
    pass


def polyAverageVertex(*args, **kwargs):
    """
    Moves the selected vertices of a polygonal object to round its shape. Translate,
    move, rotate or scale vertices.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - iterations : i                 (int)           [create,query,edit]
        Number of rounding steps.
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyAverageVertex`
    """
    pass


def polyColorMod(*args, **kwargs):
    """
    Modifies the attributes of a poly color set.
    
    Flags:
    - alphaScale_FloatValue : afv    (float)         [create,query,edit]
        ?????
    
    - alphaScale_Interp : ai         (int)           [create,query,edit]
        ????? Default:0
    
    - alphaScale_Position : ap       (float)         [create,query,edit]
        ?????
    
    - baseColorName : bcn            (unicode)       [create]
        The name of the color set to be modified.
    
    - blueScale_FloatValue : bfv     (float)         [create,query,edit]
        ?????
    
    - blueScale_Interp : bi          (int)           [create,query,edit]
        ????? Default:0
    
    - blueScale_Position : bp        (float)         [create,query,edit]
        ?????
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - greenScale_FloatValue : gfv    (float)         [create,query,edit]
        ?????
    
    - greenScale_Interp : gi         (int)           [create,query,edit]
        ????? Default:0
    
    - greenScale_Position : gp       (float)         [create,query,edit]
        ?????
    
    - huev : h                       (float)         [create,query,edit]
        Huerotates hue value of the final color. Default:0.0
    
    - intensityScale_FloatValue : nfv (float)         [create,query,edit]
        ?????
    
    - intensityScale_Interp : ni     (int)           [create,query,edit]
        ????? Default:0
    
    - intensityScale_Position : np   (float)         [create,query,edit]
        ?????
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - redScale_FloatValue : rfv      (float)         [create,query,edit]
        ?????
    
    - redScale_Interp : ri           (int)           [create,query,edit]
        ????? Default:0
    
    - redScale_Position : rp         (float)         [create,query,edit]
        ?????
    
    - satv : s                       (float)         [create,query,edit]
        Satscales the staturation of the final color. Default:1.0
    
    - value : v                      (float)         [create,query,edit]
        Valuescales the final color value. Default:1.0                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyColorMod`
    """
    pass


def polyTorus(*args, **kwargs):
    """
    The torus command creates a new polygonal torus.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the torus. Q: When queried,
        this flag returns a vector.
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (bool)          [create,query,edit]
        Create UVs or not. Default:true
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - radius : r                     (float)         [create,query,edit]
        Radius of the torus. Default:1.0
    
    - sectionRadius : sr             (float)         [create,query,edit]
        Section of the torus. Default:0.50
    
    - subdivisionsAxis : sa          (int)           [create,query,edit]
        Subdivisions about the vertical axis. Default:20
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height. Default:20
    
    - subdivisionsX : sx             (int)           [create,query,edit]
        This specifies the number of subdivisions in the X direction for the torus
        (number of sections). C: Default is 20. Q: When queried, this flag returns an
        int.
    
    - subdivisionsY : sy             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Y direction for the torus
        (number of segments per section). C: Default is 20. Q: When queried, this flag
        returns an int.
    
    - texture : tx                   (bool)          [create,query,edit]
        Apply texture or not. this is an old attribute. This is unsupported and would be
        removed in a future release. Default:true
    
    - twist : tw                     (float)         [create,query,edit]
        Twist angle of the torus. Default:0.0                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyTorus`
    """
    pass


def reverseSurface(*args, **kwargs):
    """
    The reverseSurface command reverses one or both directions of a surface or can
    be used to swapthe U and V directions (this creates the effect of reversing the
    surface normal). The name of the newly reversed surface and the name of the
    resulting dependency node is returned. The resulting surface has the same
    parameter ranges as the original surface. This command also handles selected
    surface isoparms. For a selected isoparm, imagine that the isoparm curve is
    reversed after the operation. E.g. reverseSurface surface.v[0.1] will reverse in
    the U direction.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - direction : d                  (int)           [create,query,edit]
        The direction to reverse the surface in: 0 - U, 1 - V, 2 - Both U and V, 3 -
        Swap Default:0
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Common flags
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.reverseSurface`
    """
    pass


def polyRemesh(*args, **kwargs):
    """
    Triangulates, then remeshes the given mesh through edge splitting and
    collapsing. Edges longer than the specified refinement threshold are split, and
    edges shorter than the reduction threshold are collapsed.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - interpolationType : ipt        (int)           [create,query,edit]
        Algorithm used for interpolating new vertices
    
    - maxTriangleCount : mtc         (int)           []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - reduceThreshold : rdt          (float)         [create,query,edit]
        A percentage of the refineThreshold. Edges shorter than this percentage will be
        reduced to a single vertex.
    
    - refineThreshold : rft          (float)         [create,query,edit]
        Triangle edges longer than this value will be split into two edges.
    
    - smoothStrength : smt           (float)         [create,query,edit]
        Amount of smoothing applied to the vertices after remeshing.
    
    - tessellateBorders : tsb        (bool)          [create,query,edit]
        Specifies if the borders of the selected region are allowed to be remeshed.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - worldSpace : ws                (bool)          []
    
    
    Derived from mel command `maya.cmds.polyRemesh`
    """
    pass


def _curve(*args, **kwargs):
    """
    Maya Bug Fix:
      - name parameter only applied to transform. now applies to shape as well
    """
    pass


def polyPlatonicSolid(*args, **kwargs):
    """
    The polyPlatonicSolid command creates a new polygonal platonic solid.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the platonic solid. Q: When
        queried, this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create]
        This flag alows a specific UV mechanism to be selected, while creating. The
        valid values are 0, 1,  2 ,3 or 4. 0 implies that no UVs will be generated (No
        texture to be applied). 1 implies UVs should be created for the object as a
        whole without any normalization. The solid will be unwrapped and then the
        texture will be applied without any distortion. In the unwrapped solid, the
        shared edges will have shared UVs. 2 implies UVs are created separately for each
        of the faces of the solid. 3 implies the UVs should be normalized. This will
        normalize the U and V direction separately, thereby resulting in distortion of
        textures. 4 implies UVs are created so that the texture will not be distorted
        when applied. The texture lying outside the UV range will be truncated (since
        that cannot be squeezed in, without distorting the texture. For better
        understanding of these options, you may have to open the texture view windowC:
        Default is 4
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - radius : r                     (float)         [create,query,edit]
        This flag specifies the radius of the platonic solid. C: Default is 1.0. Q: When
        queried, this flag returns a float.
    
    - sideLength : l                 (float)         [create,query,edit]
        This flag specifies the side length of platonic solid. C: Default is 1.0. Q:
        When queried, this flag returns a float.
    
    - solidType : st                 (int)           [create]
        This flag allows a specific platonic solid to be selected for creation of mesh,
        The valid values are 0, 1, 2 and 3. 0 implies dodecahedron to be created. 1
        implies icosahedron to be created. 2 implies octahedron to be created. 3 implies
        tertrahedron to be created. C: Default is 0
    
    - texture : tx                   (int)           [create]
        This flag is obsolete and will be removed in the next release. The
        -cuv/createUVs flag should be used instead.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyPlatonicSolid`
    """
    pass


def polySplitEdge(*args, **kwargs):
    """
    Split Edges.There are two operations for this command depending on the value of
    the -operation flag. If -operation is set to 1 then this command will split
    apart faces along all selected manifold edges. If -operation is set to 0 then
    this command will split non-manifold edges so as to make them manifold edges. It
    creates the minimum number of edges that can be created to make the edge
    manifold. The default value for -operation is 1, operate on manifold edges.
    Resulting mesh may have extra vertices or edges to ensure geometry is valid.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - operation : op                 (int)           [create,query,edit]
        0 means use a Non-Manifold method, 1 means use a Manifold method
        Common poly modifier operation flags
    
    
    Derived from mel command `maya.cmds.polySplitEdge`
    """
    pass


def rebuildSurface(*args, **kwargs):
    """
    This command rebuilds a surface by modifying its parameterization. In some cases
    the shape of the surface may also change. The rebuildType (-rt) attribute
    determines how the surface is rebuilt. The optional second surface can be used
    to specify a reference parameterization.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degreeU : du                   (int)           [create,query,edit]
        The degree of the resulting surface in the u direction 0 - maintain current, 1 -
        linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic Default:3
    
    - degreeV : dv                   (int)           [create,query,edit]
        The degree of the resulting surface in the v direction 0 - maintain current, 1 -
        linear, 2 - quadratic, 3 - cubic, 5 - quintic, 7 - heptic Default:3
    
    - direction : dir                (int)           [create,query,edit]
        The direction in which to rebuild: 0 - U, 1 - V, 2 - Both U and V Default:2
    
    - endKnots : end                 (int)           [create,query,edit]
        End conditions for the surface 0 - uniform end knots, 1 - multiple end knots,
        Default:0
    
    - fitRebuild : fr                (int)           [create,query,edit]
        Specify the type of rebuild method to be used: 0 - Convert Classic, the default
        and original convert method. 1 - Fit using the least squares fit method. 2 -
        Convert Match, alternate matching convert method. 3 - Convert Grid, uses a grid-
        based fit algorithm. Default:0
    
    - frozen : fzn                   (bool)          []
    
    - keepControlPoints : kcp        (bool)          [create,query,edit]
        Use the control points of the input surface. This forces uniform
        parameterization unless rebuildType is 2 (match knots) Default:false
    
    - keepCorners : kc               (bool)          [create,query,edit]
        The corners of the resulting surface will not change from the corners of the
        input surface. Default:true
    
    - keepRange : kr                 (int)           [create,query,edit]
        Determine the parameterization for the resulting surface. 0 - reparameterize the
        resulting surface from 0 to 1; 1 - keep the original surface parameterization; 2
        - reparameterize the result from 0 to number of spans Default:1
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - noChanges : nc                 (bool)          []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)
    
    - rebuildType : rt               (int)           [create,query,edit]
        The rebuild type: 0 - uniform, 1 - reduce spans, 2 - match knots, 3 - remove
        multiple knots, 4 - force non rational 5 - rebuild ends 6 - trim convert
        (uniform) 7 - into Bezier mesh Default:0
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - spansU : su                    (int)           [create,query,edit]
        The number of spans in the u direction in resulting surface. Used only when
        rebuildType is 0 - uniform. If 0, keep the same number of spans as the original
        surface. Default:4
    
    - spansV : sv                    (int)           [create,query,edit]
        The number of spans in the v direction in resulting surface. Used only when
        rebuildType is 0 - uniform. If 0, keep the same number of spans as the original
        surface. Default:4
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to rebuild Default:0.01                  Common flags
    
    
    Derived from mel command `maya.cmds.rebuildSurface`
    """
    pass


def polyUVRectangle(*args, **kwargs):
    """
    Given two vertices, does one of the following: 1) If the vertices define
    opposite corners of a rectangular area of quads, assigns a grid of UVs spanning
    the 0-1 area to that rectangle. 2) If the vertices define an edge in a
    rectangular and topologically cylindrical area of quads, assigns UVs spanning
    the 0-1 area to that cylindrical patch, using the defined edge as the U=0 edge.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyUVRectangle`
    """
    pass


def polyCut(*args, **kwargs):
    """
    This command splits a mesh, or a set of poly faces, along a plane. The position
    and orientation of the plane can be adjusted using the appropriate flags listed
    above.  In addition, the cut operation can also delete the faces lying on one
    side of the cutting plane, or extract those faces by an offset amount.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - cutPlaneCenter : pc            (float, float, float) [create,query,edit]
        The position of the cutting plane. Default:0.0, 0.0, 0.0
    
    - cutPlaneCenterX : pcx          (float)         [create,query,edit]
        Cutting plane center X coord.
    
    - cutPlaneCenterY : pcy          (float)         [create,query,edit]
        Cutting plane center Y coord.
    
    - cutPlaneCenterZ : pcz          (float)         [create,query,edit]
        Cutting plane center Z coord.
    
    - cutPlaneHeight : ph            (float)         [create,query,edit]
        The height of the cutting plane
    
    - cutPlaneRotate : ro            (float, float, float) [create,query,edit]
        The orientation of the cutting plane. Default:0.0, 0.0, 0.0
    
    - cutPlaneRotateX : rx           (float)         [create,query,edit]
        cutting plane X rotate angle.
    
    - cutPlaneRotateY : ry           (float)         [create,query,edit]
        cutting plane Y rotate angle.
    
    - cutPlaneRotateZ : rz           (float)         [create,query,edit]
        cutting plane Z rotate angle.
    
    - cutPlaneSize : ps              (float, float)  [create,query,edit]
        The width and the height of the cutting plane Default:1.0, 1.0
    
    - cutPlaneWidth : pw             (float)         [create,query,edit]
        The width of the cutting plane
    
    - cuttingDirection : cd          (unicode)       [create]
        This flag specifies the direction of the cutting plane. Valid values are x, y,
        zA value of xwill cut the object along the YZ plane cutting through the center
        of the bounding box. A value of ywill cut the object along the ZX plane cutting
        through the center of the bounding box. A value of zwill cut the object along
        the XY plane cutting through the center of the bounding box.
    
    - deleteFaces : df               (bool)          [create,query,edit]
        whether to delete the one-half of the cut-faces of the poly.  If true, they are
        deleted. Default:false
    
    - extractFaces : ef              (bool)          [create,query,edit]
        whether to extract the cut-faces of the poly into a separate shell.  If true,
        they are extracted. Default:false
    
    - extractOffset : eo             (float, float, float) [create,query,edit]
        The displacement offset of the cut faces. Default:0.5, 0.5, 0.5
    
    - extractOffsetX : eox           (float)         [create,query,edit]
        The X-displacement offset of the cut faces.
    
    - extractOffsetY : eoy           (float)         [create,query,edit]
        The Y-displacement offset of the cut faces.
    
    - extractOffsetZ : eoz           (float)         [create,query,edit]
        The Z-displacement offset of the cut faces.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - onObject : oo                  (bool)          [create,query,edit]
        whether to act on the entire polyObject or its selected face components
        Default:true
    
    - worldSpace : ws                (bool)          [create,query,edit]
        This flag specifies which reference to use. If on: all geometrical values are
        taken in world reference. If off: all geometrical values are taken in object
        reference. C: Default is off. Q: When queried, this flag returns an int.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCut`
    """
    pass


def polyMergeEdge(*args, **kwargs):
    """
    Sews two border edges together.The new edge is located either on the first,
    last, or between both selected edges, depending on the mode. Both edges must
    belong to the same object, and orientations must match (i.e. normals on
    corresponding faces must point in the same direction).Edge flags are mandatory.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - firstEdge : fe                 (int)           [create,query,edit]
        First edge to merge. Invalid default value to force the value to be set.
        Default:-1
    
    - frozen : fzn                   (bool)          []
    
    - mergeMode : mm                 (int)           [create,query,edit]
        Merge mode : 0=first, 1=halfway between both edges, 2=second. Default:1
    
    - mergeTexture : mt              (bool)          [create,query,edit]
        Boolean which is used to decide if uv coordinates should be merged or not -
        along with the geometry. Default:false
    
    - name : n                       (unicode)       [create]
        Give a name to the resulting node.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - secondEdge : se                (int)           [create,query,edit]
        Second edge to merge. Invalid default value to force the value to be set.
        Default:-1                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyMergeEdge`
    """
    pass


def torus(*args, **kwargs):
    """
    The torus command creates a new torus and/or a dependency node that creates one,
    and returns their names.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        The primitive's axis
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - degree : d                     (int)           [create,query,edit]
        The degree of the resulting surface: 1 - linear, 3 - cubic Default:3
    
    - endSweep : esw                 (float)         [create,query,edit]
        The angle at which to end the surface of revolution. Default is 2Pi radians, or
        360 degrees. Default:6.2831853
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - heightRatio : hr               (float)         [create,query,edit]
        Ratio of heightto widthDefault:2.0
    
    - minorSweep : msw               (float)         [create,query,edit]
        The sweep angle for the minor circle in the torus Default:6.2831853
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - pivot : p                      (float, float, float) [create,query,edit]
        The primitive's pivot point
    
    - polygon : po                   (int)           [create]
        The value of this argument controls the type of the object created by this
        operation 0: nurbs surface1: polygon (use nurbsToPolygonsPref to set the
        parameters for the conversion)2: subdivision surface (use nurbsToSubdivPref to
        set the parameters for the conversion)3: Bezier surface4: subdivision surface
        solid (use nurbsToSubdivPref to set the parameters for the conversion)Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    - radius : r                     (float)         [create,query,edit]
        The radius of the object Default:1.0
    
    - sections : s                   (int)           [create,query,edit]
        The number of sections determines the resolution of the surface in the sweep
        direction. Used only if useTolerance is false. Default:8
    
    - spans : nsp                    (int)           [create,query,edit]
        The number of spans determines the resolution of the surface in the opposite
        direction. Default:1
    
    - startSweep : ssw               (float)         [create,query,edit]
        The angle at which to start the surface of revolution Default:0
    
    - tolerance : tol                (float)         [create,query,edit]
        The tolerance with which to build the surface. Used only if useTolerance is true
        Default:0.01
    
    - useTolerance : ut              (bool)          [create,query,edit]
        Use the specified tolerance to determine resolution. Otherwise number of
        sections will be used. Default:false                  Common flags
    
    
    Derived from mel command `maya.cmds.torus`
    """
    pass


def detachCurve(*args, **kwargs):
    """
    The detachCurve command detaches a curve into pieces, given a list of parameter
    values.  You can also specify which pieces to keep and which to discard using
    the -kflag. The names of the newly detached curve(s) is returned.  If history is
    on, then the name of the resulting dependency node is also returned. You can use
    this command to open a periodic curve at a particular parameter value.  You
    would use this command with only one -pflag. If you are specifying -kflags, then
    you must specify one, none or all -kflags.  If you are specifying all -kflags,
    there must be one more -kflag than -pflags.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveOnSurface : cos           (bool)          [create]
        If possible, create 2D curve as a result.
    
    - frozen : fzn                   (bool)          []
    
    - keep : k                       (bool)          [create,query,edit]
        Whether or not to keep a detached piece.  This multi attribute should be one
        element larger than the parameter multi attribute. Default:true
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        Parameter values to detach at Default:0.0                  Common flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.detachCurve`
    """
    pass


def polyCube(*args, **kwargs):
    """
    The cube command creates a new polygonal cube.
    
    Flags:
    - axis : ax                      (float, float, float) [create,query,edit]
        This flag specifies the primitive axis used to build the cube. Q: When queried,
        this flag returns a float[3].
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create,query]
        Turn the construction history on or off (where applicable). If construction
        history is on then the corresponding node will be inserted into the history
        chain for the mesh. If construction history is off then the operation will be
        performed directly on the object. Note:If the object already has construction
        history then this flag is ignored and the node will always be inserted into the
        history chain.
    
    - createUVs : cuv                (int)           [create,query,edit]
        Create UVs or not. 0: No UVs1: No Normalization2: Normalize Each Face
        Separately3: Normalize Collectively4: Normalize and Preserve Aspect
        RatioDefault:3
    
    - depth : d                      (float)         [create,query,edit]
        Depth of the cube. Default:1.0
    
    - frozen : fzn                   (bool)          [query,edit]
    
    - height : h                     (float)         [create,query,edit]
        Height of the cube. Default:1.0
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node (where applicable).
    
    - subdivisionsDepth : sd         (int)           [create,query,edit]
        Subdivisions along the depth of the cube. Default:1
    
    - subdivisionsHeight : sh        (int)           [create,query,edit]
        Subdivisions along the height of the cube. Default:1
    
    - subdivisionsWidth : sw         (int)           [create,query,edit]
        Subdivisions along the width of the cube. Default:1
    
    - subdivisionsX : sx             (int)           [create,query,edit]
        This specifies the number of subdivisions in the X direction for the cube. C:
        Default is 1. Q: When queried, this flag returns an int.
    
    - subdivisionsY : sy             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Y direction for the cube.
        C: Default is 1. Q: When queried, this flag returns an int.
    
    - subdivisionsZ : sz             (int)           [create,query,edit]
        This flag specifies the number of subdivisions in the Z direction for the cube.
        C: Default is 1. Q: When queried, this flag returns an int.
    
    - texture : tx                   (int)           [create,query,edit]
        What texture mechanism to be applied 0=No textures; 1=Object; 2=Faces Default:1
    
    - width : w                      (float)         [create,query,edit]
        Width of the cube. Default:1.0                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.polyCube`
    """
    pass


def closeCurve(*args, **kwargs):
    """
    The closeCurve command closes a curve, making it periodic. The pathname to the
    newly closed curve and the name of the resulting dependency node are returned.
    If a curve is not specified in the command, then the first active curve will be
    used.
    
    Flags:
    - blendBias : bb                 (float)         [create,query,edit]
        Skew the result toward the first or the second curve depending on the blend
        value being smaller or larger than 0.5. Default:0.5
    
    - blendKnotInsertion : bki       (bool)          [create,query,edit]
        If set to true, insert a knot in one of the original curves (relative position
        given by the parameter attribute below) in order to produce a slightly different
        effect. Default:false
    
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - constructionHistory : ch       (bool)          [create]
        Turn the construction history on or off.
    
    - curveOnSurface : cos           (bool)          [create]
        If possible, create 2D curve as a result.
    
    - frozen : fzn                   (bool)          []
    
    - name : n                       (unicode)       [create]
        Sets the name of the newly-created node. If it contains namespace path, the new
        node will be created under the specified namespace; if the namespace does not
        exist, it will be created.
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal
    
    - object : o                     (bool)          [create]
        Create the result, or just the dependency node.
    
    - parameter : p                  (float)         [create,query,edit]
        The parameter value for the positioning of the newly inserted knot. Default:0.1
    
    - preserveShape : ps             (int)           [create,query,edit]
        0 - without preserving the shape 1 - preserve shape 2 - blend Default:1
        Common flags
    
    - replaceOriginal : rpo          (bool)          [create]
        Create in place(i.e., replace).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.closeCurve`
    """
    pass


def bezierCurveToNurbs(*args, **kwargs):
    """
    The bezierCurveToNurbs command attempts to convert an existing NURBS curve to a
    Bezier curve.
    
    
    Derived from mel command `maya.cmds.bezierCurveToNurbs`
    """
    pass


def polyCBoolOp(*args, **kwargs):
    """
    This command creates a new poly as the result of a boolean operation on input
    polys : union, intersection, difference. Only for difference, the order of the
    selected objects is important : result = object1 - object2. If no objects are
    specified in the command line, then the objects from the active list are used.
    
    Flags:
    - caching : cch                  (bool)          [create,query,edit]
        Toggle caching for all attributes so that no recomputation is needed
    
    - classification : cls           (int)           [create,query,edit]
        Changes how intersections of open and closed manifolds are treated. 1 for Edge,
        2 for Normal.
    
    - constructionHistory : ch       (bool)          []
    
    - edgeInterpolation : eit        (bool)          []
    
    - faceAreaThreshold : fat        (float)         [create,query,edit]
        Area threshold to determine whether faces should be collapsed before boolean.
        Attribute is ignored unless useThresholds is set to true Default:0.0001
    
    - frozen : fzn                   (bool)          []
    
    - mergeUVSets : muv              (int)           [create,query,edit]
        Specify how UV sets will be merged on the output mesh. 0 = No Merge: Each UV set
        on each mesh will become a new UV set in the output.1 = Merge By Name: UV sets
        with the same name will be merged.2 = Merge By UV Links: UV sets will be merged
        so that UV linking on the input meshes continues to work.The default is merge by
        name.
    
    - name : n                       (unicode)       []
    
    - nodeState : nds                (int)           [create,query,edit]
        Maya dependency nodes have 6 possible states. The Normal (0), HasNoEffect (1),
        and Blocking (2)states can be used to alter how the graph is evaluated.   The
        Waiting-Normal (3), Waiting-HasNoEffect (4), Waiting-Blocking (5)are for
        internal use only. They temporarily shut off parts of the graph during
        interaction (e.g., manipulation). The understanding is that once the operation
        is done, the state will be reset appropriately, e.g. Waiting-Blockingwill reset
        back to Blocking.   The Normaland Blockingcases apply to all nodes, while
        HasNoEffectis node specific; many nodes do not support this option. Plug-ins
        store state in the MPxNode::stateattribute. Anyone can set it or check this
        attribute.  Additional details about each of these 3 states follow.
        StateDescriptionNormalThe normal node state. This is the default.HasNoEffectThe
        HasNoEffectoption (a.k.a. pass-through), is used in cases where there is an
        operation on an input producing an output of the same data type. Nearly all
        deformers support this state, as do a few other nodes. As stated earlier, it is
        not supported by all nodes.  Its typical to implement support for the
        HasNoEffectstate in the nodes compute method and to perform appropriate
        operations. Plug-ins can also support HasNoEffect.  The usual implementation of
        this state is to copy the input directly to the matching output without applying
        the algorithm in the node. For deformers, applying this state leaves the input
        geometry undeformed on the output.  BlockingThis is implemented in the depend
        node base class and applies to all nodes. Blockingis applied during the
        evaluation phase to connections. An evaluation request to a blocked connection
        will return as failures, causing the destination plug to retain its current
        value. Dirty propagation is indirectly affected by this state since blocked
        connections are never cleaned.  When a node is set to Blockingthe behavior is
        supposed to be the same as if all outgoing connections were broken. As long as
        nobody requests evaluation of the blocked node directly it wont evaluate after
        that. Note that a blocked node will still respond to getAttrrequests but a
        getAttron a downstream node will not reevaluate the blocked node.  Setting the
        root transform of a hierarchy to Blockingwont automatically influence child
        transforms in the hierarchy. To do this, youd need to explicitly set all child
        nodes to the Blockingstate.  For example, to set all child transforms to
        Blocking, you could use the following script.  import maya.cmds as cmds def
        blockTree(root): nodesToBlock = [] for node in {child:1 for child in
        cmds.listRelatives( root, path=True, allDescendents=True )}.keys(): nodesToBlock
        += cmds.listConnections(node, source=True, destination=True ) for node in
        {source:1 for source in nodesToBlock}.keys(): cmds.setAttr( '%s.nodeState' %
        node, 2 )  Applying this script would continue to draw objects but things would
        not be animated.  Default:kdnNormal                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    - object : o                     (bool)          []
    
    - operation : op                 (int)           [create,query,edit]
        Boolean operation type. 1=union, 2=difference, 3=intersection. Default type is
        union. Default:kBoolOpUnion
    
    - planarTolerance : ptl          (float)         []
    
    - preserveColor : pcr            (bool)          [create,query,edit]
        If true, boolean op will compute color for the new mesh. If false, the new mesh
        won't have any color set. Default:false
    
    - sortOutput : sop               (bool)          []
    
    - useCarveBooleans : ucb         (bool)          [create,query,edit]
        If true, use the Carve Boolean library
    
    - useThresholds : uth            (bool)          [create,query,edit]
        If true, merge vertices with separations less then vertexDistanceThreshold and
        collapse faces with areas less then faceAreaThreshold. If false, do not merge
        vertices or collapse faces Default:false
    
    - vertexDistanceThreshold : vdt  (float)         [create,query,edit]
        Tolerance to determine whether vertices (and edges) should be merged before
        boolean operation is applied. Attribute is ignored unless useThresholds is set
        to true Default:0.001                  Flags From polyUnite Node
    
    
    Derived from mel command `maya.cmds.polyCBoolOp`
    """
    pass
