from pymel.internal.pmcmds import selectKeyframeRegionCtx
from pymel.internal.pmcmds import polySelectCtx
from pymel.internal.pmcmds import latticeDeformKeyCtx
from pymel.internal.pmcmds import wrinkleContext
from pymel.internal.pmcmds import keyframeRegionDirectKeyCtx
from pymel.internal.pmcmds import texSelectContext
from pymel.internal.pmcmds import texMoveUVShellContext
from pymel.internal.pmcmds import createNurbsSquareCtx
from pymel.internal.pmcmds import texManipContext
from pymel.internal.pmcmds import dollyCtx
from pymel.internal.pmcmds import meshRemapContext
from pymel.internal.pmcmds import artSelectCtx
from pymel.internal.pmcmds import modelingToolkitSuperCtx
from pymel.internal.pmcmds import nexTRSContext
from pymel.internal.pmcmds import curveAddPtCtx
from pymel.internal.pmcmds import paintPointsContext
from pymel.internal.pmcmds import xgmCutBrushContext
from pymel.internal.pmcmds import ctxCompletion
from pymel.internal.pmcmds import dynPaintCtx
from pymel.internal.pmcmds import manipScaleLimitsCtx
from pymel.internal.pmcmds import textureLassoContext
from pymel.internal.pmcmds import dynWireCtx
from pymel.internal.pmcmds import tumbleCtx
from pymel.internal.pmcmds import renderWindowSelectContext
from pymel.internal.pmcmds import xgmPresetSnapshotContext
from pymel.internal.pmcmds import createPolyPrismCtx
from pymel.internal.pmcmds import polyCreateFacetCtx
from pymel.internal.pmcmds import distanceDimContext
from pymel.internal.pmcmds import alignCtx
from pymel.internal.pmcmds import xgmWidthBrushContext
from pymel.internal.pmcmds import polyCutUVCtx
from pymel.internal.pmcmds import createNurbsCubeCtx
from pymel.internal.pmcmds import hotkeyCtx
from pymel.internal.pmcmds import createNurbsConeCtx
from pymel.internal.pmcmds import roundCRCtx
from pymel.internal.pmcmds import artSetPaintCtx
from pymel.internal.pmcmds import keyframeRegionMoveKeyCtx
from pymel.internal.pmcmds import nexMultiCutCtx
from pymel.internal.pmcmds import polyMergeEdgeCtx
from pymel.internal.pmcmds import softModCtx
from pymel.internal.pmcmds import nexConnectCtx
from pymel.internal.pmcmds import xgmCombBrushContext
from pymel.internal.pmcmds import boxDollyCtx
from pymel.internal.pmcmds import drawExtrudeFacetCtx
from pymel.internal.pmcmds import igBrushContext
from pymel.internal.pmcmds import targetWeldCtx
from pymel.internal.pmcmds import dragAttrContext
from pymel.internal.pmcmds import SymmetrizeUVContext
from pymel.internal.pmcmds import threePointArcCtx
from pymel.internal.pmcmds import nexCtx
from pymel.internal.pmcmds import curveBezierCtx
from pymel.internal.pmcmds import createPolySoccerBallCtx
from pymel.internal.pmcmds import ctxEditMode
from pymel.internal.pmcmds import texTweakUVContext
from pymel.internal.pmcmds import stitchSurfaceCtx
from pymel.internal.pmcmds import trackCtx
from pymel.internal.pmcmds import texScaleContext
from pymel.internal.pmcmds import keyframeRegionCurrentTimeCtx
from pymel.internal.pmcmds import wireContext
from pymel.internal.pmcmds import skinBindCtx
from pymel.internal.pmcmds import graphTrackCtx
from pymel.internal.pmcmds import polyMergeFacetCtx
from pymel.internal.pmcmds import softSelectOptionsCtx
from pymel.internal.pmcmds import graphDollyCtx
from pymel.internal.pmcmds import insertJointCtx
from pymel.internal.pmcmds import orbitCtx
from pymel.internal.pmcmds import selectKeyCtx
from pymel.internal.pmcmds import twoPointArcCtx
from pymel.internal.pmcmds import createNurbsCylinderCtx
from pymel.internal.pmcmds import setKeyCtx
from pymel.internal.pmcmds import xgmLengthBrushContext
from pymel.internal.pmcmds import keyframeRegionScaleKeyCtx
from pymel.internal.pmcmds import createNurbsCircleCtx
from pymel.internal.pmcmds import filterButterworthCtx
from pymel.internal.pmcmds import createPolyTorusCtx
from pymel.internal.pmcmds import blendCtx
from pymel.internal.pmcmds import greasePencilCtx
from pymel.internal.pmcmds import xgmBifrostBrushContext
from pymel.internal.pmcmds import xgmGuideContext
from pymel.internal.pmcmds import createNurbsSphereCtx
from pymel.internal.pmcmds import polySuperCtx
from pymel.internal.pmcmds import rollCtx
from pymel.internal.pmcmds import createPolyCubeCtx
from pymel.internal.pmcmds import createPolyConeCtx
from pymel.internal.pmcmds import graphSelectContext
from pymel.internal.pmcmds import superCtx
from pymel.internal.pmcmds import artAttrSkinPaintCtx
from pymel.internal.pmcmds import walkCtx
from pymel.internal.pmcmds import curveCVCtx
from pymel.internal.pmcmds import projectionContext
from pymel.internal.pmcmds import curveSketchCtx
from pymel.internal.pmcmds import xgmPlaceBrushContext
from pymel.internal.pmcmds import artPuttyCtx
from pymel.internal.pmcmds import paramDimContext
from pymel.internal.pmcmds import createPolyPlatonicSolidCtx
from pymel.internal.pmcmds import xgmSmoothBrushContext
from pymel.internal.pmcmds import currentCtx
from pymel.internal.pmcmds import texLatticeDeformContext
from pymel.internal.pmcmds import lassoContext
from pymel.internal.pmcmds import arcLenDimContext
from pymel.internal.pmcmds import texturePlacementContext
from pymel.internal.pmcmds import boxZoomCtx
from pymel.internal.pmcmds import artAttrPaintVertexCtx
from pymel.internal.pmcmds import xgmGrabBrushContext
from pymel.internal.pmcmds import panZoomCtx
from pymel.internal.pmcmds import polyVertexNormalCtx
from pymel.internal.pmcmds import view2dToolCtx
from pymel.internal.pmcmds import sculptMeshCacheCtx
from pymel.internal.pmcmds import polyCutCtx
from pymel.internal.pmcmds import texSelectShortestPathCtx
from pymel.internal.pmcmds import polyRetopoCtx
from pymel.internal.pmcmds import createNurbsTorusCtx
from pymel.internal.pmcmds import texMoveContext
from pymel.internal.pmcmds import setEditCtx
from pymel.internal.pmcmds import softModContext
from pymel.internal.pmcmds import xgmFreezeBrushContext
from pymel.internal.pmcmds import keyframeRegionSelectKeyCtx
from pymel.internal.pmcmds import moveKeyCtx
from pymel.internal.pmcmds import xgmNoiseBrushContext
from pymel.internal.pmcmds import snapTogetherCtx
from pymel.internal.pmcmds import xgmDensityBrushContext
from pymel.internal.pmcmds import artBaseCtx
from pymel.internal.pmcmds import polySplitCtx
from pymel.internal.pmcmds import insertKeyCtx
from pymel.internal.pmcmds import snapshotModifyKeyCtx
from pymel.internal.pmcmds import propModCtx
from pymel.internal.pmcmds import selectContext
from pymel.internal.pmcmds import currentTimeCtx
from pymel.internal.pmcmds import manipMoveLimitsCtx
from pymel.internal.pmcmds import createPolyPlaneCtx
from pymel.internal.pmcmds import createPolyPipeCtx
from pymel.internal.pmcmds import nexMultiCutContext
from pymel.internal.pmcmds import dpBirailCtx
from pymel.internal.pmcmds import dynSelectCtx
from pymel.internal.pmcmds import modelCurrentTimeCtx
from pymel.internal.pmcmds import createPolyPyramidCtx
from pymel.internal.pmcmds import curveEPCtx
from pymel.internal.pmcmds import dynParticleCtx
from pymel.internal.pmcmds import texSmudgeUVContext
from pymel.internal.pmcmds import polyCreaseCtx
from pymel.internal.pmcmds import texRotateContext
from pymel.internal.pmcmds import keyframeRegionDollyCtx
from pymel.internal.pmcmds import scaleKeyCtx
from pymel.internal.pmcmds import directKeyCtx
from pymel.internal.pmcmds import retimeKeyCtx
from pymel.internal.pmcmds import xgmSelectBrushContext
from pymel.internal.pmcmds import jointCtx
from pymel.internal.pmcmds import createPolySphereCtx
from pymel.internal.pmcmds import polySelectEditCtx
from pymel.internal.pmcmds import polyAppendFacetCtx
from pymel.internal.pmcmds import curveMoveEPCtx
from pymel.internal.pmcmds import mateCtx
from pymel.internal.pmcmds import ikHandleCtx
from pymel.internal.pmcmds import snapshotBeadCtx
from pymel.internal.pmcmds import polyShortestPathCtx
from pymel.internal.pmcmds import xgmDirectionBrushContext
from pymel.internal.pmcmds import ctxData
from pymel.internal.pmcmds import regionSelectKeyCtx
from pymel.internal.pmcmds import keyframeRegionSetKeyCtx
from pymel.internal.pmcmds import Unfold3DContext
from pymel.internal.pmcmds import createNurbsPlaneCtx
from pymel.internal.pmcmds import texWinToolCtx
from pymel.internal.pmcmds import createPolyHelixCtx
from pymel.internal.pmcmds import ctxAbort
from pymel.internal.pmcmds import clipEditorCurrentTimeCtx
from pymel.internal.pmcmds import texSculptCacheContext
from pymel.internal.pmcmds import xgmPartBrushContext
from pymel.internal.pmcmds import texCutContext
from pymel.internal.pmcmds import trimCtx
from pymel.internal.pmcmds import snapshotBeadContext
from pymel.internal.pmcmds import mpBirailCtx
from pymel.internal.pmcmds import createPolyCylinderCtx
from pymel.internal.pmcmds import xgmClumpBrushContext
from pymel.internal.pmcmds import ikSplineHandleCtx
from pymel.internal.pmcmds import nexQuadDrawContext
from pymel.internal.pmcmds import polySlideEdgeCtx
from pymel.internal.pmcmds import xgmPrimSelectionContext
from pymel.internal.pmcmds import xgmPointsContext
from pymel.internal.pmcmds import meshReorderContext
from pymel.internal.pmcmds import curveEditorCtx
from pymel.internal.pmcmds import keyframeRegionTrackCtx
from pymel.internal.pmcmds import srtContext
from pymel.internal.pmcmds import texSmoothContext
from pymel.internal.pmcmds import nexQuadDrawCtx
from pymel.internal.pmcmds import xgmGuideSculptContext
from pymel.internal.pmcmds import nexConnectContext
from pymel.internal.pmcmds import manipRotateLimitsCtx
from pymel.internal.pmcmds import filterKeyReducerCtx
from pymel.internal.pmcmds import keyframeRegionInsertKeyCtx
from pymel.internal.pmcmds import artFluidAttrCtx
from pymel.internal.pmcmds import ctxTraverse
from pymel.internal.pmcmds import spBirailCtx

if False:
    from typing import Dict, List, Tuple, Union, Optional


def manipScaleContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a scale manip context.
    
    Flags:
    - activeHandle : ah              (int)           [query,edit]
        Sets the default active handle for the manip.  That is, the handle which should
        be initially active when the tool is activated. Values can be: 0 - X axis handle
        is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
        (all axes) is active (default)
    
    - alignAlong : aa                (float, float, float) [create,edit]
        Aligns active handle along vector.
    
    - constrainAlongNormal : xn      (bool)          [query,edit]
        When true, transform constraints are applied along the vertex normal first and
        only use the closest point when no intersection is found along the normal.
    
    - currentActiveHandle : cah      (int)           [query,edit]
        Sets the active handle for the manip. Values can be: 0 - X axis handle is
        active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
        (all axes) is active4 - XY plane handle is active5 - YZ plane handle is active6
        - XZ plane handle is active
    
    - editPivotMode : epm            (bool)          [query]
        Returns true manipulator is in edit pivot mode
    
    - editPivotPosition : epp        (bool)          [query]
        Returns the current position of the edit pivot manipulator.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - lastMode : lm                  (int)           [query]
        Returns the previous scaling mode.
    
    - manipVisible : vis             (bool)          [query]
        Returns true if the scale manipulator is visible.
    
    - mode : m                       (int)           [query,edit]
        Scale mode: 0 - Object Space1 - Local Space2 - World Space (default)3 - Scale
        Along Vertex Normal4 - Scale Along Rotation Axis5 - Scale Along Live Object
        Axis6 - Custom Axis Orientation10 - Component Space
    
    - orientAxes : oa                (float, float, float) [query,edit]
        Orients manipulator rotating around axes by specified angles
    
    - orientObject : oo              (unicode)       [create,edit]
        Orients manipulator to the passed in object/component
    
    - orientTowards : ot             (float, float, float) [create,edit]
        Orients active handle towards world point
    
    - pinPivot : pin                 (bool)          [query,edit]
        Pin component pivot. When the component pivot is set and pinned selection
        changes will not reset the pivot position and orientation.
    
    - pivotOriHandle : poh           (bool)          [query,edit]
        When true, the pivot manipulator will show the orientation handle during
        editing. Default is true.
    
    - position : p                   (bool)          [query]
        Returns the current position of the manipulator.
    
    - postCommand : psc              (script)        [create,edit]
        Specifies a command to be executed when the tool is exited.
    
    - postDragCommand : pod          (script, <type 'unicode'>) [create,edit]
        Specifies a command and a node type. The command will be executed at the end of
        a drag when a node of the specified type is in the selection.
    
    - preCommand : prc               (script)        [create,edit]
        Specifies a command to be executed when the tool is entered.
    
    - preDragCommand : prd           (script, <type 'unicode'>) [create,edit]
        Specifies a command and a node type. The command will be executed at the start
        of a drag when a node of the specified type is in the selection.
    
    - preserveChildPosition : pcp    (bool)          [query,edit]
        When false, the children objects move when their parent is rotated. When true,
        the worldspace position of the children will be maintained as the parent is
        moved. Default is false.
    
    - preserveUV : puv               (bool)          [query,edit]
        When false, the uvs are not changes to match the vertex edit. When true, the uvs
        are edited to project to new values to stop texture swimming as vertices are
        moved.
    
    - preventNegativeScale : pns     (bool)          [query]
        When this is true, negative scale is not allowed.
    
    - reflection : rfl               (bool)          []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionAbout : rab          (int)           []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionAxis : rfa           (int)           []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionTolerance : rft      (float)         []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - scale : sc                     (float, float, float) [query,edit]
        Returns the scale of the manipulator for its current orientation/mode.
    
    - snap : s                       (bool)          [create,query,edit]
        Specify that the manipulation is to use absolute snap
    
    - snapPivotOri : spo             (bool)          [query,edit]
        Snap pivot orientation. Modify pivot orientation when snapping the pivot to a
        component.
    
    - snapPivotPos : spp             (bool)          [query,edit]
        Snap pivot position. Modify pivot position when snapping the pivot to a
        component.
    
    - snapRelative : sr              (bool)          [create,query,edit]
        Specify that the manipulation is to use relative snap
    
    - snapValue : sv                 (float)         [create,query,edit]
        Specify the snapping value
    
    - tweakMode : twk                (bool)          [query,edit]
        When true, the manipulator is hidden and highlighted components can be selected
        and scaled in one step using a click-drag interaction.
    
    - useManipPivot : ump            (bool)          [create,query,edit]
        Specify whether to pivot on the manip
    
    - useObjectPivot : uop           (bool)          [create,query,edit]
        Specify whether to pivot on the object
    
    - xformConstraint : xc           (unicode)       [query,edit]
        none - no transform constraintedge - edge transform constraintsurface - surface
        transform constraintFlag can have multiple arguments, passed either as a tuple
        or a list.
    
    
    Derived from mel command `maya.cmds.manipScaleContext`
    """
    pass


def userCtx(*args, **kwargs):
    """
    Flags:
    - editCommand : ec               (callable)      []
    
    - editPrompt : ep                (unicode)       []
    
    - exists : ex                    (bool)          []
    
    - finalCommand : fc              (unicode)       []
    
    - history : ch                   (bool)          []
    
    - image1 : i1                    (unicode)       []
    
    - image2 : i2                    (unicode)       []
    
    - image3 : i3                    (unicode)       []
    
    - name : n                       (unicode)       []
    
    - noSelectionPrompt : nsp        (int, unicode)  []
    
    - selectionCount : sc            (int, int)      []
    
    - selectionFlag : flg            (int, unicode)  []
    
    - selectionMask : sm             (int, unicode)  []
    
    - selectionPrompt : sp           (unicode)       []
    
    
    Derived from mel command `maya.cmds.userCtx`
    """
    pass


def artUserPaintCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name of
    the context as the last argument as this provides the name of the context to
    create, edit or query. This command executes a scriptable paint (Maya Artisan).
    It allows the user to apply Mel commands/scripts to modify cvs' attributes for
    all cvs under the paint brush.
    
    Flags:
    - accopacity : aco               (bool)          [create,query,edit]
        Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool
        for which it is true by default). Q: When queried, it returns a boolean.
    
    - activeListChangedProc : alp    (unicode)       [create,query,edit]
        Accepts a string that contains a MEL command that is invoked whenever the active
        list changes. There may be some situations where the UI, for example, needs to
        be updated, when objects are selected/deselected in the scene. In query mode,
        the name of the currently registered MEL command is returned and this will be an
        empty string if none is defined.
    
    - afterStrokeCmd : asc           (unicode)       [create,query,edit]
        The passed string is executed as a MEL command immediately after the end of a
        stroke. C: Default is no command. Q: When queried, it returns the current
        command
    
    - alphaclamp : alc               (unicode)       [create,query,edit]
        Specifies if the weight value should be alpha clamped to the lower and upper
        bounds. There are four options here: none- no clamping is performed, lower-
        clamps only to the lower bound, upper- clamps only to the upper bounds, both-
        clamps to the lower and upper bounds. C: Default is none.  Q: When queried, it
        returns a string.
    
    - alphaclamplower : acl          (float)         [create,query,edit]
        Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When
        queried, it returns a float.
    
    - alphaclampupper : acu          (float)         [create,query,edit]
        Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When
        queried, it returns a float.
    
    - attrSelected : asl             (unicode)       [query]
        Returns a name of the currently selected attribute. Q: When queried, it returns
        a string.
    
    - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
        The passed string is executed as a MEL command immediately before the start of a
        stroke. C: Default is no command. Q: When queried, it returns the current
        command
    
    - brushalignment : bra           (bool)          [create,query,edit]
        Specifies the path brush alignemnt. If true, the brush will align to stroke
        path, otherwise it will align to up vector. C: Default is true. Q: When queried,
        it returns a boolean.
    
    - brushfeedback : brf            (bool)          [create,query,edit]
        Specifies if the brush additional feedback should be drawn. C: Default is TRUE.
        Q: When queried, it returns a boolean.
    
    - chunkCommand : cc              (unicode)       [create,query,edit]
        Specifies th name of the Mel script/procedure that is called once for every
        selected surface when a chunk is received on that surface. Q: When queried, it
        returns a string.
    
    - clamp : cl                     (unicode)       [create,query,edit]
        Specifies if the weight value should be clamped to the lower and upper bounds.
        There are four options here: none- no clamping is performed, lower- clamps only
        to the lower bound, upper- clamps only to the upper bounds, both- clamps to the
        lower and upper bounds. C: Default is none.  Q: When queried, it returns a
        string.
    
    - clamplower : cll               (float)         [create,query,edit]
        Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried,
        it returns a float.
    
    - clampupper : clu               (float)         [create,query,edit]
        Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried,
        it returns a float.
    
    - clear : clr                    (bool)          [create,edit]
        Floods all cvs/vertices to the current value.
    
    - colorAlphaValue : cl1          (float)         [create,query,edit]
        The Alpha value of the color.
    
    - colorRGBAValue : cl4           (float, float, float, float) [create,query,edit]
        The RGBA value of the color.
    
    - colorRGBValue : cl3            (float, float, float) [create,query,edit]
        The RGB value of the color.
    
    - colorRamp : cr                 (unicode)       [create,query,edit]
        Allows a user defined color ramp to be used to map values to colors.
    
    - colorfeedback : cf             (bool)          [create,query,edit]
        Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried,
        it returns a boolean.
    
    - colorfeedbackOverride : cfo    (bool)          [create,query,edit]
        Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried,
        it returns a boolean.
    
    - colorrangelower : crl          (float)         [create,query,edit]
        Specifies the value that maps to black when color feedback mode is on. C:
        Default is 0.0.  Q: When queried, it returns a float.
    
    - colorrangeupper : cru          (float)         [create,query,edit]
        Specifies the value that maps to the maximum color when color feedback mode is
        on. C: Default is 1.0.  Q: When queried, it returns a float.
    
    - dataTypeIndex : dti            (int)           [query,edit]
        When the selected paintable attribute is a vectorArray, it specifies which field
        to paint on.
    
    - disablelighting : dl           (bool)          [create,query,edit]
        If color feedback is on, this flag determines whether lighting is disabled or
        not for the surfaces that are affected. C: Default is FALSE.  Q: When queried,
        it returns a boolean.
    
    - dragSlider : dsl               (unicode)       [create,edit]
        Sets the current brush drag state for resizing or offsetting the brush (like the
        'b' and 'm' default hotkeys). The string argument is one of: radius, lowradius,
        opacity, value, depth, displacement, uvvectoror none. C: Default is none.
    
    - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
        The passed string is executed as a MEL command during the stroke, each time the
        mouse is dragged. C: Default is no command. Q: When queried, it returns the
        current command
    
    - dynclonemode : dcm             (bool)          [create,query,edit]
        Enable or disable dynamic clone mode.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - expandfilename : eef           (bool)          [create,edit]
        If true, it will expand the name of the export file and concatenate it with the
        surface name. Otherwise it will take the name as it is. C: Default is true.
    
    - exportaspectratio : ear        (float)         [create,query,edit]
        Value of aspect ratio for export
    
    - exportfilemode : efm           (unicode)       [create,query,edit]
        Specifies the export channel.The valid entries here are: alpha, luminance, rgb,
        rgba. C: Default is luminance/rgb. Q: When queried, it returns a string.
    
    - exportfilesave : esf           (unicode)       [edit]
        Exports the attribute map and saves to a specified file.
    
    - exportfilesizex : fsx          (int)           [create,query,edit]
        Specifies the width of the attribute map to export. C: Default width is 256. Q:
        When queried, it returns an integer.
    
    - exportfilesizey : fsy          (int)           [create,query,edit]
        Specifies the width of the attribute map to export. C: Default width is 256. Q:
        When queried, it returns an integer.
    
    - exportfiletype : eft           (unicode)       [create,query,edit]
        Specifies the image file format. It can be one of the following: iff, tiff,
        jpeg, alias, rgb, fitpostScriptEPS, softimage, wavefrontRLA, wavefrontEXP. C:
        default is tiff. Q: When queried, it returns a string.
    
    - filterNodes : fon              (bool)          [edit]
        Sets the node filter.
    
    - finalizeCmd : fc               (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called at the end of each
        stroke. Q: When queried, it returns a string.
    
    - fullpaths : fp                 (bool)          [create,query,edit]
        Specifies whether full path names should be used when surface names are passed
        to scripts. If false, just the surface name is passed. C: Default is false  Q:
        When queried, it returns a boolean.
    
    - getArrayAttrCommand : gac      (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called once for every
        surface that is selected for painting. This procedure returns a string, which is
        interpreted as a list of names referring to double array attributes on some
        dependency node. Q: When queried, it returns a string.
    
    - getSurfaceCommand : gsc        (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called once for every
        dependency node on the selection list, whenever Artisan processes the selection
        list. It returns the name of the surface to paint on. Q: When queried, it
        returns a string.
    
    - getValueCommand : gvc          (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called every time a value
        on the surface is needed by the scriptable paint tool. Q: When queried, it
        returns a string.
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - importfileload : ifl           (unicode)       [edit]
        Load the attribute map a specified file.
    
    - importfilemode : ifm           (unicode)       [create,query,edit]
        Specifies the channel to import. The valid entries here are: alpha, luminance,
        red, green, blue, and rgbC: Default is alpha. Q: When queried, it returns a
        string.
    
    - importreassign : irm           (bool)          [create,query,edit]
        Specifies if the multiply atrribute maps are to be reassigned while importing.
        Only maps previously exported from within Artisan can be reassigned. C: Default
        is FALSE. Q: When queried, it returns a  boolean.
    
    - initializeCmd : ic             (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called in the beginning
        of each stroke. Q: When queried, it returns a string.
    
    - interactiveUpdate : iu         (bool)          [create,query,edit]
        Specifies how often to transfer the painted values into the attribute. TRUE:
        transfer them continuously(many times per stroke) FALSE: transfer them only at
        the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
        queried, it returns a boolean.
    
    - lastRecorderCmd : lrc          (unicode)       [create,query,edit]
        Value of last recorded command.
    
    - lastStampName : lsn            (unicode)       [create,query,edit]
        Value of the last stamp name.
    
    - lowerradius : lr               (float)         [create,query,edit]
        Sets the lower size of the brush (only apply on tablet).
    
    - makeStroke : mst               (int)           [create,query,edit]
        Stroke point values.
    
    - mappressure : mp               (unicode)       [create,query,edit]
        Sets the tablet pressure mapping when the table is used. There are four options:
        none- the pressure has no effect, opacity- the pressure is mapped to the
        opacity, radius- the is mapped to modify the radius of the brush, both- the
        pressure modifies both the opacity and the radius. C: Default is none. Q: When
        queried, it returns a string.
    
    - maxvalue : mxv                 (float)         [create,query,edit]
        Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When
        queried, it returns a float.
    
    - minvalue : miv                 (float)         [create,query,edit]
        Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When
        queried, it returns a float.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - objattrArray : oaa             (unicode)       [query]
        An array of all paintable attributes. Each element of the array is a string with
        the following information: NodeType.NodeName.AttributeName.MenuType. \*MenuType:
        type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
    
    - opacity : op                   (float)         [create,query,edit]
        Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
    - outline : o                    (bool)          [create,query,edit]
        Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it
        returns a boolean.
    
    - outwhilepaint : owp            (bool)          [create,query,edit]
        Specifies if the brush outline should be drawn while painting. C: Default is
        FALSE. Q: When queried, it returns a boolean.
    
    - paintNodeArray : pna           (unicode)       [query]
        An array of paintable nodes. Q: When queried, it returns a string.
    
    - paintattrselected : pas        (unicode)       [edit]
        An array of selected paintable attributes. Each element of the array is a string
        with the following information: NodeType.NodeName.AttributeName.
    
    - paintmode : pm                 (unicode)       [create,query,edit]
        Specifies the paint mode. There are two possibilities: screenand tangent. C:
        Default is screen. Q: When queried, it returns a string.
    
    - paintoperationtype : pot       (unicode)       [create,query,edit]
        Specifies the operation type used by the Paint Tool.  Currently, we support the
        following paint modes: Paint, Smear, Blur, Eraseand Clone. Default is Paint.
    
    - pickColor : pcm                (bool)          [create,query,edit]
        Set pick color mode on or off
    
    - pickValue : pv                 (bool)          [create,query,edit]
        Toggle for picking
    
    - playbackCursor : plc           (float, float)  [create,query,edit]
        Values for the playback cursor.
    
    - playbackPressure : plp         (float)         [create,query,edit]
        Valus for the playback pressure.
    
    - preserveclonesource : pcs      (bool)          [create,query,edit]
        Whether or not to preserve a clone source.
    
    - profileShapeFile : psf         (unicode)       [query,edit]
        Passes a name of the image file for the stamp shape profile.
    
    - projective : prm               (bool)          [create,query,edit]
        Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it
        returns a boolean.
    
    - radius : r                     (float)         [create,query,edit]
        Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a
        float.
    
    - rampMaxColor : rxc             (float, float, float) [create,query,edit]
        Defines a special color to be used when the value is greater than or equal to
        the maximum value.
    
    - rampMinColor : rmc             (float, float, float) [create,query,edit]
        Defines a special color to be used when the value is less than or equal to the
        minimum value.
    
    - record : rec                   (bool)          [create,query,edit]
        Toggle on for recording.
    
    - reflection : rn                (bool)          [create,query,edit]
        Specifies the reflection mode. C: Default is 'false'. Q: When queried, it
        returns a boolean.
    
    - reflectionaboutorigin : rno    (bool)          [create,query,edit]
        Toggle on to reflect about the origin
    
    - reflectionaxis : ra            (unicode)       [create,query,edit]
        Specifies the reflection axis. There are three possibilities: x, yand z. C:
        Default is x. Q: When queried, it returns a string.
    
    - screenRadius : scR             (float)         [create,query,edit]
        Brush radius on the screen
    
    - selectclonesource : scs        (bool)          [create,query,edit]
        Toggle on to select the clone source
    
    - selectedattroper : sao         (unicode)       [create,query,edit]
        Sets the edit weight operation. Four edit weights operations are provided :
        absolute- the value of the weight is replaced by the current one, additive- the
        value of the weight is added to the current one, scale- the value of the weight
        is multiplied by the current one, smooth- the value of the weight is divided by
        the current one. C: Default is absolute.  Q: When queried, it returns a string.
    
    - setArrayValueCommand : sac     (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called for each paint
        stamp. A stamp may affect one or more values on the surface. This call rolls up
        all the calls that would be made to setValueCommand for the stamp into one call
        with array arguments. Q: When queried, it returns a string.
    
    - setValueCommand : svc          (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called every time a value
        on the surface is changed. Q: When queried, it returns a string.
    
    - showactive : sa                (bool)          [create,query,edit]
        Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When
        queried, it returns a boolean.
    
    - stampDepth : stD               (float)         [create,query,edit]
        Depth of the stamps
    
    - stampProfile : stP             (unicode)       [create,query,edit]
        Sets the brush profile of the current stamp. Currently, the following profiles
        are supported: gaussian, soft, solidand square. C: Default is gaussian. Q: When
        queried, it returns a string.
    
    - stampSpacing : stS             (float)         [create,query,edit]
        Specifies the stamp spacing. Default is 1.0.
    
    - strokesmooth : ssm             (unicode)       [create,query,edit]
        Stroke smoothing type name
    
    - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
        Enables/disables the the display of the effective brush area as affected
        vertices.
    
    - tablet : tab                   (bool)          [query]
        Returns true if the tablet device is present, false if it is absent
    
    - tangentOutline : to            (bool)          [create,query,edit]
        Enables/disables the display of the brush circle tangent to the surface.
    
    - toolCleanupCmd : tcc           (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called when this tool is
        exited. Q: When queried, it returns a string.
    
    - toolOffProc : tfp              (unicode)       [create,query,edit]
        Accepts a strings describing the name of a MEL procedure that is invoked
        whenever the tool is turned off. For example, cloth invokes
        clothPaintToolOffwhen the cloth paint tool is turned on. Define this callback if
        your tool requires special functionality when your tool is deactivated. It is
        typical that if you implement a toolOffProc you will want to implement a
        toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the
        currently registered MEL command is returned and this will be an empty string if
        none is defined.
    
    - toolOnProc : top               (unicode)       [create,query,edit]
        Accepts a strings describing the name of a MEL procedure that is invoked
        whenever the tool is turned on. For example, cloth invokes clothPaintToolOnwhen
        the cloth paint tool is turned on. Define this callback if your tool requires
        special functionality when your tool is activated. It is typical that if you
        implement a toolOnProc you will want to implement a toolOffProc as well (see the
        -toolOffProc flag. In query mode, the name of the currently registered MEL
        command is returned and this will be an empty string if none is defined.
    
    - toolSetupCmd : tsc             (unicode)       [create,query,edit]
        Specifies the name of the Mel script/procedure that is called once for every
        selected surface when an initial click is received on that surface. Q: When
        queried, it returns a string.
    
    - useColorRamp : ucr             (bool)          [create,query,edit]
        Specifies whether the user defined color ramp should be used to map values from
        to colors.  If this is turned off, the default greyscale feedback will be used.
    
    - useMaxMinColor : umc           (bool)          [create,query,edit]
        Specifies whether the out of range colors should be used.  See rampMinColor and
        rampMaxColor flags for further details.
    
    - usepressure : up               (bool)          [create,query,edit]
        Sets the tablet pressure on/off. C: Default is false. Q: When queried, it
        returns a boolean.
    
    - value : val                    (float)         [create,query,edit]
        Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it
        returns a float.
    
    - whichTool : wst                (unicode)       [create,query,edit]
        The string defines the name of the tool to be used for the Artisan context. An
        example is artClothPaint. In query mode, the tool name for the given context is
        returned. Note: due to the way MEL works, always specify the -query flag last
        when specifying a flag that takes arguments.
    
    - worldRadius : wlR              (float)         [create,query,edit]
        Radius in worldspace                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.artUserPaintCtx`
    """
    pass


def shadingGeometryRelCtx(*args, **kwargs):
    """
    This command creates a context that can be used for associating geometry to
    shading groups.  You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true.  This means that the shading group is
    selected first then geometry associated with the shading group are highlighted.
    Subsequent selections result in assignments. Specifying -shadingCentric false
    means that the geometry is to be selected first.  The shading group associated
    with the geometry will then be selected and subsequent selections will result in
    assignments being made.
    
    Flags:
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - offCommand : ofc               (unicode)       [create,query,edit]
        command to be issued when context is turned on
    
    - onCommand : onc                (unicode)       [create,query,edit]
        command to be issued when context is turned on
    
    - shadingCentric : s             (bool)          [create,query,edit]
        shading-centric mode.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.shadingGeometryRelCtx`
    """
    pass


def art3dPaintCtx(*args, **kwargs):
    """
    This is a tool context command for 3d Paint tool.                In query mode,
    return type is based on queried flag.
    
    Flags:
    - accopacity : aco               (bool)          [create,query,edit]
        Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool
        for which it is true by default). Q: When queried, it returns a boolean.
    
    - afterStrokeCmd : asc           (unicode)       [create,query,edit]
        The passed string is executed as a MEL command immediately after the end of a
        stroke. C: Default is no command. Q: When queried, it returns the current
        command
    
    - alphablendmode : abm           (unicode)       [create,query,edit]
        Specifies the blend mode used while painting RGB channel. Currently, we support
        the following blend modes: DefaultLightenDarkenDifferenceExclusionHard LightSoft
        LightMultiplyScreenOverlayConstantDefault is Default.
    
    - alwaysKeepFile : akf           (bool)          []
    
    - assigntxt : ast                (bool)          [edit]
        Sends a request to the tool to allocate and assign file textures to the
        specified attibute on the selected shaders.
    
    - attrnames : atn                (unicode)       [create,query,edit]
        Name of attributes
    
    - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
        The passed string is executed as a MEL command immediately before the start of a
        stroke. C: Default is no command. Q: When queried, it returns the current
        command
    
    - brushalignment : bra           (bool)          [create,query,edit]
        Specifies the path brush alignemnt. If true, the brush will align to stroke
        path, otherwise it will align to up vector. C: Default is true. Q: When queried,
        it returns a boolean.
    
    - brushdepth : bd                (float)         [create,query,edit]
        Depth of the brush
    
    - brushfeedback : brf            (bool)          [create,query,edit]
        Specifies if the brush additional feedback should be drawn. C: Default is TRUE.
        Q: When queried, it returns a boolean.
    
    - brushtype : brt                (unicode)       [create,query,edit]
        Name of the brush type
    
    - clear : clr                    (bool)          [create,edit]
        Floods all cvs/vertices to the current value.
    
    - commonattr : cat               (unicode)       [query]
        Returns a string with the names of all common to all the shaders paintable
        attributes and supported by the Paint Texture Tool.
    
    - dragSlider : dsl               (unicode)       [create,edit]
        Sets the current brush drag state for resizing or offsetting the brush (like the
        'b' and 'm' default hotkeys). The string argument is one of: radius, lowradius,
        opacity, value, depth, displacement, uvvectoror none. C: Default is none.
    
    - dynclonemode : dcm             (bool)          [create,query,edit]
        Enable or disable dynamic clone mode.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - expandfilename : eef           (bool)          [create,edit]
        If true, it will expand the name of the export file and concatenate it with the
        surface name. Otherwise it will take the name as it is. C: Default is true.
    
    - exportaspectratio : ear        (float)         [create,query,edit]
        Value of aspect ratio for export
    
    - exportfilemode : efm           (unicode)       [create,query,edit]
        Specifies the export channel.The valid entries here are: alpha, luminance, rgb,
        rgba. C: Default is luminance/rgb. Q: When queried, it returns a string.
    
    - exportfilesave : esf           (unicode)       [edit]
        Exports the attribute map and saves to a specified file.
    
    - exportfilesizex : fsx          (int)           [create,query,edit]
        Specifies the width of the attribute map to export. C: Default width is 256. Q:
        When queried, it returns an integer.
    
    - exportfilesizey : fsy          (int)           [create,query,edit]
        Specifies the width of the attribute map to export. C: Default width is 256. Q:
        When queried, it returns an integer.
    
    - exportfiletype : eft           (unicode)       [create,query,edit]
        Specifies the image file format. It can be one of the following: iff, tiff,
        jpeg, alias, rgb, fitpostScriptEPS, softimage, wavefrontRLA, wavefrontEXP. C:
        default is tiff. Q: When queried, it returns a string.
    
    - extendFillColor : efc          (bool)          [create,query,edit]
        States if the painted textures will be automatically postprocessed on each
        stroke to fill in the background color. Default is true.
    
    - fileformat : eff               (unicode)       [create,query,edit]
        Name of the file format
    
    - filetxtaspectratio : far       (float)         [create,query,edit]
        Specifies the aspect ration of the texture width and height. Default is 1.
    
    - filetxtsizex : ftx             (int)           [create,query,edit]
        Specifies the width of the texture. Default is 256.
    
    - filetxtsizey : fty             (int)           [create,query,edit]
        Specifies the height of the texture. Default is 256.
    
    - floodOpacity : fop             (float)         [create,query,edit]
        Value of the flood opacity
    
    - floodall : fal                 (bool)          [create,query,edit]
        Turn on to flood everything
    
    - floodselect : fsl              (bool)          [create,query,edit]
        Should the selected area be flooded?
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - importfileload : ifl           (unicode)       [edit]
        Load the attribute map a specified file.
    
    - importfilemode : ifm           (unicode)       [create,query,edit]
        Specifies the channel to import. The valid entries here are: alpha, luminance,
        red, green, blue, and rgbC: Default is alpha. Q: When queried, it returns a
        string.
    
    - importreassign : irm           (bool)          [create,query,edit]
        Specifies if the multiply atrribute maps are to be reassigned while importing.
        Only maps previously exported from within Artisan can be reassigned. C: Default
        is FALSE. Q: When queried, it returns a  boolean.
    
    - keepaspectratio : kar          (bool)          [create,query,edit]
        States if the aspect ratio of the file texture sizes should remain constant.
        Default is true. boolean.
    
    - lastRecorderCmd : lrc          (unicode)       [create,query,edit]
        Value of last recorded command.
    
    - lastStampName : lsn            (unicode)       [create,query,edit]
        Value of the last stamp name.
    
    - lowerradius : lr               (float)         [create,query,edit]
        Sets the lower size of the brush (only apply on tablet).
    
    - makeStroke : mst               (int)           [create,query,edit]
        Stroke point values.
    
    - mappressure : mp               (unicode)       [create,query,edit]
        Sets the tablet pressure mapping when the table is used. There are four options:
        none- the pressure has no effect, opacity- the pressure is mapped to the
        opacity, radius- the is mapped to modify the radius of the brush, both- the
        pressure modifies both the opacity and the radius. C: Default is none. Q: When
        queried, it returns a string.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - opacity : op                   (float)         [create,query,edit]
        Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
    - outline : o                    (bool)          [create,query,edit]
        Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it
        returns a boolean.
    
    - outwhilepaint : owp            (bool)          [create,query,edit]
        Specifies if the brush outline should be drawn while painting. C: Default is
        FALSE. Q: When queried, it returns a boolean.
    
    - paintmode : pm                 (unicode)       [create,query,edit]
        Specifies the paint mode. There are two possibilities: screenand tangent. C:
        Default is screen. Q: When queried, it returns a string.
    
    - paintoperationtype : pot       (unicode)       [create,query,edit]
        Specifies the operation type used by the Paint Tool.  Currently, we support the
        following paint modes: Paint, Smear, Blur, Eraseand Clone. Default is Paint.
    
    - painttxtattr : pta             (unicode)       [create,query,edit]
        Specifies the attribute on the shader which the user wants to paint. Currently,
        we support the following attributes: Color, Transparency, Ambient,
        Incandescence, BumpMap, Diffuse, TranslucenceEccentricitySpecularColor,
        Reflectivity, ReflectedColor, and user-defined float, float3, double, and
        double3 attributes. Default is Color.
    
    - painttxtattrname : ptn         (unicode)       [query,edit]
        Returns a string with the names of all paintable attributes supported by the
        Paint Texture Tool.
    
    - pfxScale : psc                 (float)         [query,edit]
        Specifies the scale for Paint Effect brushes.
    
    - pfxWidth : pwd                 (float)         [query,edit]
        Specifies the width for Paint Effect brushes.
    
    - pickColor : pcm                (bool)          [create,query,edit]
        Set pick color mode on or off
    
    - pickValue : pv                 (bool)          [create,query,edit]
        Toggle for picking
    
    - playbackCursor : plc           (float, float)  [create,query,edit]
        Values for the playback cursor.
    
    - playbackPressure : plp         (float)         [create,query,edit]
        Valus for the playback pressure.
    
    - preserveclonesource : pcs      (bool)          [create,query,edit]
        Whether or not to preserve a clone source.
    
    - pressureMapping1 : pm1         (int)           [create,query,edit]
        First pressure mapping value
    
    - pressureMapping2 : pm2         (int)           [create,query,edit]
        Second pressure mapping value
    
    - pressureMapping3 : pm3         (int)           [create,query,edit]
        Third pressure mapping value
    
    - pressureMax1 : px1             (float)         [create,query,edit]
        First pressure maximum value
    
    - pressureMax2 : px2             (float)         [create,query,edit]
        Second pressure maximum value
    
    - pressureMax3 : px3             (float)         [create,query,edit]
        Third pressure maximum value
    
    - pressureMin1 : ps1             (float)         [create,query,edit]
        First pressure minimum value
    
    - pressureMin2 : ps2             (float)         [create,query,edit]
        Second pressure minimum value
    
    - pressureMin3 : ps3             (float)         [create,query,edit]
        Third pressure minimum value
    
    - profileShapeFile : psf         (unicode)       [query,edit]
        Passes a name of the image file for the stamp shape profile.
    
    - projective : prm               (bool)          [create,query,edit]
        Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it
        returns a boolean.
    
    - radius : r                     (float)         [create,query,edit]
        Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a
        float.
    
    - record : rec                   (bool)          [create,query,edit]
        Toggle on for recording.
    
    - reflection : rn                (bool)          [create,query,edit]
        Specifies the reflection mode. C: Default is 'false'. Q: When queried, it
        returns a boolean.
    
    - reflectionaboutorigin : rno    (bool)          [create,query,edit]
        Toggle on to reflect about the origin
    
    - reflectionaxis : ra            (unicode)       [create,query,edit]
        Specifies the reflection axis. There are three possibilities: x, yand z. C:
        Default is x. Q: When queried, it returns a string.
    
    - reloadtexfile : rtf            (bool)          [edit]
        Sends a request to the tool to reload the texture from the disc.
    
    - resizeratio : rr               (float)         [query,edit]
        Specifies the scale by which to resize the current textures.
    
    - resizetxt : rft                (bool)          [edit]
        Sends a request to the tool to resize all the currently in use textures.
    
    - rgbcolor : rgb                 (float, float, float) [create,query,edit]
        Colour value
    
    - rgbflood : fc                  (float, float, float) [create,query,edit]
        Color of the flood
    
    - saveTextureOnStroke : sts      (bool)          [create,query,edit]
        States if the original texture will be automatically saved on each stroke.
        Default is false.
    
    - saveonstroke : sos             (bool)          [create,query,edit]
        States if the temporary texture will be automatically saved on each stroke.
        Default is false.
    
    - savetexture : stx              (bool)          [edit]
        Sends a request to the tool to save the texture to the disc.
    
    - screenRadius : scR             (float)         [create,query,edit]
        Brush radius on the screen
    
    - selectclonesource : scs        (bool)          [create,query,edit]
        Toggle on to select the clone source
    
    - shadernames : hnm              (unicode)       [query]
        Returns a string with the names of all shaders assigned to selected surfaces.
    
    - shapeattr : spa                (bool)          [query,edit]
        States if the attribute to paint is an attribute of the shape and not the
        shader. Default is false.
    
    - shapenames : shn               (unicode)       [query]
        Returns a string with the names of all surfaces which are being painted on.
    
    - showactive : sa                (bool)          [create,query,edit]
        Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When
        queried, it returns a boolean.
    
    - soloAsDiffuse : sod            (bool)          [query,edit]
        States if the currently paintable texture will be rendered as as diffuse texture
        in the viewport. Default is false.
    
    - stampDepth : stD               (float)         [create,query,edit]
        Depth of the stamps
    
    - stampProfile : stP             (unicode)       [create,query,edit]
        Sets the brush profile of the current stamp. Currently, the following profiles
        are supported: gaussian, soft, solidand square. C: Default is gaussian. Q: When
        queried, it returns a string.
    
    - stampSpacing : stS             (float)         [create,query,edit]
        Specifies the stamp spacing. Default is 1.0.
    
    - strokesmooth : ssm             (unicode)       [create,query,edit]
        Stroke smoothing type name
    
    - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
        Enables/disables the the display of the effective brush area as affected
        vertices.
    
    - tablet : tab                   (bool)          [query]
        Returns true if the tablet device is present, false if it is absent
    
    - tangentOutline : to            (bool)          [create,query,edit]
        Enables/disables the display of the brush circle tangent to the surface.
    
    - textureFilenames : tfn         (bool)          [query]
        Returns a string array with the names of all the painted file textures.
    
    - updateEraseTex : uet           (bool)          [create,query,edit]
        Should the erase texture update?
    
    - usepressure : up               (bool)          [create,query,edit]
        Sets the tablet pressure on/off. C: Default is false. Q: When queried, it
        returns a boolean.
    
    - worldRadius : wlR              (float)         [create,query,edit]
        Radius in worldspace                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.art3dPaintCtx`
    """
    pass


def shadingLightRelCtx(*args, **kwargs):
    """
    This command creates a context that can be used for associating lights to
    shading groups.  You can put the context into shading-centric mode by using the
    -shadingCentric flag and specifying true.  This means that the shading group is
    selected first then lights associated with the shading group are highlighted.
    Subsequent selections result in assignments. Specifying -shadingCentric false
    means that the light is to be selected first. The shading groups associated with
    the light will then be selected and subsequent selections will result in
    assignments being made.
    
    Flags:
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - offCommand : ofc               (unicode)       [create,query,edit]
        command to be issued when context is turned on
    
    - onCommand : onc                (unicode)       [create,query,edit]
        command to be issued when context is turned on
    
    - shadingCentric : s             (bool)          [create,query,edit]
        shading-centric mode.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.shadingLightRelCtx`
    """
    pass


def draggerContext(*args, **kwargs):
    """
    The draggerContext allows the user to program the behavior of the mouse or an
    equivalent dragging device in MEL.
    
    Flags:
    - anchorPoint : ap               (float, float, float) [query]
        Anchor point (double array) where dragger was initially pressed.
    
    - button : bu                    (int)           [query]
        Returns the current mouse button (1,2,3).
    
    - currentStep : cs               (int)           [query]
        Current step (press-drag-release sequence) for dragger context. When queried
        before first press event happened, returns 0.
    
    - cursor : cur                   (unicode)       [create,query,edit]
        Cursor displayed while context is active.  Valid values are: default, hand,
        crossHair, dolly, track, and tumble.
    
    - dragCommand : dc               (script)        [create,query,edit]
        Command called when mouse dragger is dragged.
    
    - dragPoint : dp                 (float, float, float) [query]
        Drag point (double array) current position of dragger during drag.
    
    - drawString : ds                (unicode)       [create,edit]
        A string to be drawn at the current position of the pointer.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - finalize : fnz                 (script)        [create,query,edit]
        Command called when the tool is exited.
    
    - helpString : hs                (unicode)       [query]
        Help string for context
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - holdCommand : hc               (script)        [create,query,edit]
        Command called when mouse dragger is held.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - initialize : inz               (script)        [create,query,edit]
        Command called when the tool is entered.
    
    - modifier : mo                  (unicode)       [query]
        Returns the current modifier type:  ctrl, alt or none.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - plane : pl                     (float, float, float) [create,edit]
        Provide normal of projection plane (see -projection flag for details).
    
    - prePressCommand : ppc          (script)        [create,query,edit]
        Command called when mouse dragger is pressed. It is called before pressCommand,
        so it can be used for initialization of context.
    
    - pressCommand : pc              (script)        [create,query,edit]
        Command called when mouse dragger is pressed.
    
    - projection : pr                (unicode)       [create,query,edit]
        Sets current projection of drag point. Valid types are: viewPlaneproject to view
        planeobjectViewPlaneproject to object plane (parallel to view
        plane)objectPlaneproject to specified plane defined by object location and
        normal (default) 0,1,0planeproject to specified plane defined by origin and
        normal (default) 0,1,0sketchPlaneproject to sketch planexAxisproject to closest
        point on X axisyAxisproject to closest point on Y axiszAxisproject to closest
        point on Z axisboundingSphereproject to closest point on object sphere
        boundsboundingBoxproject to closest point on object bounding box
    
    - releaseCommand : rc            (script)        [create,query,edit]
        Command called when mouse dragger is released.
    
    - snapping : snp                 (bool)          [create,query,edit]
        Enable/disable snapping for dragger context.
    
    - space : sp                     (unicode)       [create,query,edit]
        Sets current space that coordinates are reported in. Types are: worldworld space
        (global)objectobject space (local)screenscreen space
    
    - stepsCount : sc                (int)           [create,query,edit]
        Number of steps (press-drag-release sequences) for dragger context. When
        combined with undoMode flag, several steps might be recorded as single undo
        action.
    
    - undoMode : um                  (unicode)       [create,query,edit]
        Undo queue mode for the context actions. Acceptable values are: alldefault
        behaviour when every action that happens during dragger context activity is
        recorded as an individual undo chunk.step- all the actions that happen between
        each press and release are combined into one undo chunk.sequence- all the
        actions that happen between very first press and very last release are combined
        into single undo chunk. This works exactly the same as stepfor a single step
        dragger context.Flag can have multiple arguments, passed either as a tuple or a
        list.
    
    
    Derived from mel command `maya.cmds.draggerContext`
    """
    pass


def showManipCtx(*args, **kwargs):
    """
    This command can be used to create a show manip context.  The show manip context
    will display manips for all selected objects that have valid manips defined for
    them.
    
    Flags:
    - currentNodeName : cnn          (bool)          [query]
        Returns the name of the first node that the context is attached to.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - incSnap : incSnap              (int, bool)     [create,query,edit]
        If true, the manipulator owned by the context will use incremental snapping for
        specified mode.
    
    - incSnapRelative : isr          (int, bool)     [create,query,edit]
        If true, the manipulator owned by the context will use relative incremental
        snapping for specified mode.
    
    - incSnapUI : isu                (bool)          [query]
        Returns an array of elements indicating what kind of incremental snap UI is
        required by the manipulator owned by the context. If no UI is required, the
        result array will contain a single element of with the value 0. The other values
        and their meanings are: 1 - UI for linear incremental translate2 - UI for
        incremental rotate3 - UI for inclremental scale
    
    - incSnapValue : isv             (int, float)    [create,query,edit]
        Supply the step value which the manipulator owned by the context will use for
        specified mode.
    
    - lockSelection : ls             (bool)          [create,query,edit]
        If true, this context will never change the current selection. By default this
        is set to false.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - toggleIncSnap : tis            (bool)          [create,edit]
        Toggles (enables/disables) snapping for all modes.
    
    - toolFinish : tf                (script)        [create,query,edit]
        Supply the script that will be run when the user exits the script.
    
    - toolStart : ts                 (script)        [create,query,edit]
        Supply the script that will be run when the user first enters the script
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.showManipCtx`
    """
    pass


def scriptCtx(*args, **kwargs):
    """
    This command allows a user to create their own tools based on the selection
    tool. A number of selection lists can be collected, the behaviour of the
    selection and the selection masks are fully customizable, etc. The command is
    processed prior to being executed.  The keyword $Selection#where # is a number 1
    or greater specifies a selection set.  The context can specify several selection
    sets which are substituted in place of the $Selection# keyword in the form of a
    Mel string array.  Items that are specific per set need to be specified in each
    set, if they are going to be specified for any of the sets.  See examples below.
    In addition, in order to specify the type of selection you need to be making,
    any of the selection type flags from selectTypecommand can be used here.
    
    Flags:
    - allComponents : alc            (bool)          [create,query]
        Set all component selection masks on/off
    
    - allObjects : alo               (bool)          [create,query]
        Set all object selection masks on/off
    
    - animBreakdown : abd            (bool)          [create,query]
        Set animation breakdown selection mask on/off.
    
    - animCurve : ac                 (bool)          [create,query]
        Set animation curve selection mask on/off.
    
    - animInTangent : ait            (bool)          [create,query]
        Set animation in-tangent selection mask on/off.
    
    - animKeyframe : ak              (bool)          [create,query]
        Set animation keyframe selection mask on/off.
    
    - animOutTangent : aot           (bool)          [create,query]
        Set animation out-tangent selection mask on/off.
    
    - baseClassName : bcn            (unicode)       [create,query,edit]
        This string will be used to produce MEL function names for the property sheets
        for the tool.  For example, if myScriptToolwas given, the functions
        myScriptToolValuesand myScriptToolPropertieswill be used for the property
        sheets.  The default is scriptTool.
    
    - byName : bn                    (unicode, int)  []
    
    - camera : ca                    (bool)          [create,query]
        Set camera selection mask on/off. (object flag)
    
    - cluster : cl                   (bool)          [create,query]
        Set cluster selection mask on/off. (object flag)
    
    - collisionModel : clm           (bool)          [create,query]
        Set collision model selection mask on/off. (object flag)
    
    - controlVertex : cv             (bool)          [create,query]
        Set control vertex selection mask on/off. (component flag)
    
    - cumulativeLists : cls          (bool)          [create,query,edit]
        If set, the selection lists will be cumulative.  For example, the second list
        will contain all the items from the first list, the third all the items from the
        second list etc.  Make sure your script specified above takes that into account.
        Relevant if there is more than one selection set.
    
    - curve : c                      (bool)          [create,query]
        Set curve selection mask on/off. (object flag)
    
    - curveKnot : ck                 (bool)          [create,query]
        Set curve knot selection mask on/off. (component flag)
    
    - curveOnSurface : cos           (bool)          [create,query]
        Set curve-on-surface selection mask on/off. (object flag)
    
    - curveParameterPoint : cpp      (bool)          [create,query]
        Set curve parameter point selection mask on/off. (component flag)
    
    - dimension : dim                (bool)          [create,query]
        Set dimension shape selection mask on/off. (object flag)
    
    - dynamicConstraint : dc         (bool)          [create,query]
        Set dynamicConstraint selection mask on/off. (object flag)
    
    - edge : eg                      (bool)          [create,query]
        Set mesh edge selection mask on/off. (component flag)
    
    - editPoint : ep                 (bool)          [create,query]
        Set edit-point selection mask on/off. (component flag)
    
    - emitter : em                   (bool)          [create,query]
        Set emitter selection mask on/off. (object flag)
    
    - enableRootSelection : ers      (bool)          [create,query,edit]
        If set, the items to be selected are at their root transform level. Default is
        false.
    
    - escToQuit : esc                (bool)          [create,query,edit]
        If set to true, exit the tool when press Esc. Default is false.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - exitUponCompletion : euc       (bool)          [create,query,edit]
        If set, completing the last selection set will exit the tool.  Default is true.
    
    - expandSelectionList : esl      (bool)          [create,query,edit]
        If set, the selection lists will expand to have a single component in each item.
        You probably want this as a default, otherwise two isoparms on the same surface
        will show up as 1 item. To ensure that components on the same object are
        returned in the order in which they are selected, use the selectPref
        -trackSelectionOrder oncommand in your -toolStartscript to enable ordered
        selection, then restore it to its original value in your -toolFinishscript.
    
    - facet : fc                     (bool)          [create,query]
        Set mesh face selection mask on/off. (component flag)
    
    - field : fi                     (bool)          [create,query]
        Set field selection mask on/off. (object flag)
    
    - finalCommandScript : fcs       (script)        [create,query,edit]
        Supply the script that will be run when the user presses the enter key and the
        context is completed.  Depending on the number of selection sets you have, the
        script can make use of variables string $Selection1[], $Selection2[], ...
    
    - fluid : fl                     (bool)          [create,query]
        Set fluid selection mask on/off. (object flag)
    
    - follicle : fo                  (bool)          [create,query]
        Set follicle selection mask on/off. (object flag)
    
    - forceAddSelect : fas           (bool)          [create,query,edit]
        If set to true, together with -setAutoToggleSelection (see below) on the first
        selection set, causes the first selection after the computation of the previous
        result to be shiftselection, unless a modifier key is pressed.  Default is
        false. Flags for each selection set.  These flags are multi-use.
    
    - hairSystem : hs                (bool)          [create,query]
        Set hairSystem selection mask on/off. (object flag)
    
    - handle : ha                    (bool)          [create,query]
        Set object handle selection mask on/off. (object flag)
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - hull : hl                      (bool)          [create,query]
        Set hull selection mask on/off. (component flag)
    
    - ignoreInvalidItems : iii       (bool)          [create,query,edit]
        If you have multiple selection sets, the state of the selection set is recorded
        at the time you complete it.  You could then delete some of the items in that
        list and end up with invalid items in one or more of your selection sets.  If
        this flag is set, those items will be detected and ignored.  You will never know
        it happened.  Its as if they were never selected in the first place, except that
        your selection set now does not have as many items as it may need.  If this flag
        is not set, you will get a warning and your final command callback script will
        likely not execute because of an error condition.
    
    - ikEndEffector : iee            (bool)          [create,query]
        Set ik end effector selection mask on/off. (object flag)
    
    - ikHandle : ikh                 (bool)          [create,query]
        Set ik handle selection mask on/off. (object flag)
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - imagePlane : ip                (bool)          [create,query]
        Set image plane selection mask on/off. (component flag)
    
    - implicitGeometry : ig          (bool)          [create,query]
        Set implicit geometry selection mask on/off. (object flag)
    
    - isoparm : iso                  (bool)          [create,query]
        Set surface iso-parm selection mask on/off. (component flag)
    
    - joint : j                      (bool)          [create,query]
        Set ik handle selection mask on/off. (object flag)
    
    - jointPivot : jp                (bool)          [create,query]
        Set joint pivot selection mask on/off. (component flag)
    
    - lastAutoComplete : lac         (bool)          [create,query,edit]
        True if auto complete is set for the last selection set, false otherwise.
        Mostly used for query, but if present in conjuction with -sac/setAutoComplete
        flag, -sac flag takes precedence.
    
    - lattice : la                   (bool)          [create,query]
        Set lattice selection mask on/off. (object flag)
    
    - latticePoint : lp              (bool)          [create,query]
        Set lattice point selection mask on/off. (component flag)
    
    - light : lt                     (bool)          [create,query]
        Set light selection mask on/off. (object flag)
    
    - localRotationAxis : ra         (bool)          [create,query]
        Set local rotation axis selection mask on/off. (component flag)
    
    - locator : lc                   (bool)          [create,query]
        Set locator (all types) selection mask on/off. (object flag)
    
    - locatorUV : luv                (bool)          [create,query]
        Set uv locator selection mask on/off. (object flag)
    
    - locatorXYZ : xyz               (bool)          [create,query]
        Set xyz locator selection mask on/off. (object flag)
    
    - meshComponents : mc            (bool)          []
    
    - meshUVShell : msh              (bool)          []
    
    - motionTrailPoint : mtp         (bool)          []
    
    - motionTrailTangent : mtt       (bool)          []
    
    - nCloth : ncl                   (bool)          [create,query]
        Set nCloth selection mask on/off. (object flag)
    
    - nParticle : npr                (bool)          [create,query]
        Set nParticle point selection mask on/off. (component flag)
    
    - nParticleShape : nps           (bool)          [create,query]
        Set nParticle shape selection mask on/off. (object flag)
    
    - nRigid : nr                    (bool)          [create,query]
        Set nRigid selection mask on/off. (object flag)
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - nonlinear : nl                 (bool)          [create,query]
        Set nonlinear selection mask on/off. (object flag)
    
    - nurbsCurve : nc                (bool)          [create,query]
        Set nurbs-curve selection mask on/off. (object flag)
    
    - nurbsSurface : ns              (bool)          [create,query]
        Set nurbs-surface selection mask on/off. (object flag)
    
    - objectComponent : ocm          (bool)          [create,query]
        Component flags apply to object mode.
    
    - orientationLocator : ol        (bool)          [create,query]
        Set orientation locator selection mask on/off. (object flag)
    
    - particle : pr                  (bool)          [create,query]
        Set particle point selection mask on/off. (component flag)
    
    - particleShape : ps             (bool)          [create,query]
        Set particle shape selection mask on/off. (object flag)
    
    - plane : pl                     (bool)          [create,query]
        Set sketch plane selection mask on/off. (object flag)
    
    - polymesh : p                   (bool)          [create,query]
        Set poly-mesh selection mask on/off. (object flag)
    
    - polymeshEdge : pe              (bool)          [create,query]
        Set poly-mesh edge selection mask on/off. (component flag)
    
    - polymeshFace : pf              (bool)          [create,query]
        Set poly-mesh face selection mask on/off. (component flag)
    
    - polymeshFreeEdge : pfe         (bool)          [create,query]
        Set poly-mesh free-edge selection mask on/off. (component flag)
    
    - polymeshUV : puv               (bool)          [create,query]
        Set poly-mesh UV point selection mask on/off. (component flag)
    
    - polymeshVertex : pv            (bool)          [create,query]
        Set poly-mesh vertex selection mask on/off. (component flag)
    
    - polymeshVtxFace : pvf          (bool)          [create,query]
        Set poly-mesh vertexFace selection mask on/off. (component flag)
    
    - queryByName : qbn              (unicode)       []
    
    - rigidBody : rb                 (bool)          [create,query]
        Set rigid body selection mask on/off. (object flag)
    
    - rigidConstraint : rc           (bool)          [create,query]
        Set rigid constraint selection mask on/off. (object flag)
    
    - rotatePivot : rp               (bool)          [create,query]
        Set rotate pivot selection mask on/off. (component flag)
    
    - scalePivot : sp                (bool)          [create,query]
        Set scale pivot selection mask on/off. (component flag)
    
    - sculpt : sc                    (bool)          [create,query]
        Set sculpt selection mask on/off. (object flag)
    
    - selectHandle : sh              (bool)          [create,query]
        Set select handle selection mask on/off. (component flag)
    
    - setAllowExcessCount : sae      (bool)          [create,edit]
        If set, the number if items is to be interpreted as the minimum.
    
    - setAutoComplete : sac          (bool)          [create,edit]
        If set to true, as soon as the specified number of items is selected the tool
        will start the next selection set or run the command.
    
    - setAutoToggleSelection : sat   (bool)          [create,edit]
        If set to true, it is as if shiftkey is pressed when there are no modifiers
        pressed.  That means that you get the toggle selectbehaviour by default.  This
        only applies to the 3D view, and the selection done in the hypergraph, outliner
        or elsewhere is still a subject to the usual rules.
    
    - setDoneSelectionPrompt : dsp   (unicode)       [create,edit]
        If setAutoComplete is not set (see below) this string will be shown as soon as
        the tool has enough items for a particular selection set.  If this is not set,
        but is needed, the same string as set with -setSelectionPrompt flag will be
        used.
    
    - setNoSelectionHeadsUp : snh    (unicode)       [create,edit]
        Supply a string that will be shown as a heads up prompt when there is nothing
        selected.  This must be set separately for each selection set.
    
    - setNoSelectionPrompt : snp     (unicode)       [create,edit]
        Supply a string that will be shown as help when there is nothing selected.  This
        must be set separately for each selection set.
    
    - setSelectionCount : ssc        (int)           [create,edit]
        The number of items in this selection set.  0 means as many as you need until
        completion.
    
    - setSelectionHeadsUp : ssh      (unicode)       [create,edit]
        Supply a string that will be shown as a heads up prompt when there is something
        selected.  This must be set separately for each selection set.
    
    - setSelectionPrompt : ssp       (unicode)       [create,edit]
        Supply a string that will be shown as help when there is something selected.
        This must be set separately for each selection set.
    
    - showManipulators : sm          (bool)          [create,query,edit]
        If set, the manipulators will be shown for any active objects. Basically, it is
        as if you are in the Show Manipulator tool.
    
    - spring : spr                   (bool)          [create,query]
        Set spring shape selection mask on/off. (object flag)
    
    - springComponent : spc          (bool)          [create,query]
        Set individual spring selection mask on/off. (component flag)
    
    - stroke : str                   (bool)          [create,query]
        Set the Paint Effects stroke selection mask on/off. (object flag)
    
    - subdiv : sd                    (bool)          [create,query]
        Set subdivision surfaces selection mask on/off. (object flag)
    
    - subdivMeshEdge : sme           (bool)          [create,query]
        Set subdivision surfaces mesh edge selection mask on/off. (component flag)
    
    - subdivMeshFace : smf           (bool)          [create,query]
        Set subdivision surfaces mesh face selection mask on/off. (component flag)
    
    - subdivMeshPoint : smp          (bool)          [create,query]
        Set subdivision surfaces mesh point selection mask on/off. (component flag)
    
    - subdivMeshUV : smu             (bool)          [create,query]
        Set subdivision surfaces mesh UV map selection mask on/off. (component flag)
    
    - surfaceEdge : se               (bool)          [create,query]
        Set surface edge selection mask on/off. (component flag)
    
    - surfaceFace : sf               (bool)          [create,query]
        Set surface face selection mask on/off. (component flag)
    
    - surfaceKnot : sk               (bool)          [create,query]
        Set surface knot selection mask on/off. (component flag)
    
    - surfaceParameterPoint : spp    (bool)          [create,query]
        Set surface parameter point selection mask on/off. (component flag)
    
    - surfaceRange : sr              (bool)          [create,query]
        Set surface range selection mask on/off. (component flag)
    
    - surfaceUV : suv                (bool)          [create,query]
        Set surface uv selection mask on/off. (component flag)
    
    - texture : tx                   (bool)          [create,query]
        Set texture selection mask on/off. (object flag)
    
    - title : t                      (unicode)       [create,query,edit]
        Supply a string that will be used as a precursor to all the messages; i.e., the
        nameof the tool.
    
    - toolCursorType : tct           (unicode)       [create,query,edit]
        Supply the string identifier to set the tool cursor type when inside of tool.
        The following are the valid ids: create, dolly, edit, pencil, track,
        trackHorizontal, trackVertical, transformation, tumble, zoom, zoomIn, zoomOut,
        flyThrough, dot, fleur, leftArrow, question, doubleHorizArrow, doubleVertArrow,
        sizing, dollyIn, dollyOut, brush, camera, noAccess, input, output, leftCycle,
        rightCycle, rightExpand, knife.
    
    - toolFinish : tf                (script)        [create,query,edit]
        Supply the script that will be run when the user exits the script.
    
    - toolStart : ts                 (script)        [create,query,edit]
        Supply the script that will be run when the user first enters the script
    
    - totalSelectionSets : tss       (int)           [create,query,edit]
        Total number of selection sets.
    
    - vertex : v                     (bool)          [create,query]
        Set mesh vertex selection mask on/off. (component flag)                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.scriptCtx`
    """
    pass


def manipRotateContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a rotate manip context.
    
    Flags:
    - activeHandle : ah              (int)           [query,edit]
        Sets the default active handle for the manip.  That is, the handle which should
        be initially active when the tool is activated. Values can be: 0 - X axis handle
        is active1 - Y axis handle is active2 - Z axis handle is active3 - View rotation
        handle (outer ring) is active (default)
    
    - alignAlong : aa                (float, float, float) [create,edit]
        Aligns active handle along vector.
    
    - centerTrackball : ctb          (bool)          [create,query,edit]
        Specify if the center is to be handled like a trackball
    
    - constrainAlongNormal : xn      (bool)          [query,edit]
        When true, transform constraints are applied along the vertex normal first and
        only use the closest point when no intersection is found along the normal.
    
    - currentActiveHandle : cah      (int)           [query,edit]
        Sets the active handle for the manip. Values can be: 0 - X axis handle is
        active1 - Y axis handle is active2 - Z axis handle is active3 - View rotation
        handle (outer ring) is active4 - Arc Ball is active
    
    - editPivotMode : epm            (bool)          [query]
        Returns true manipulator is in edit pivot mode
    
    - editPivotPosition : epp        (bool)          [query]
        Returns the current position of the edit pivot manipulator.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - lastMode : lm                  (int)           [query]
        Returns the previous rotation mode.
    
    - manipVisible : vis             (bool)          [query]
        Returns true if the rotate manipulator is visible.
    
    - mode : m                       (int)           [query,edit]
        Rotate mode: 0 - Object Space (default)1 - World Space2 - Gimbal Mode3 - Custom
        Axis Orientation10 - Component Space
    
    - modifyTranslation : mt         (bool)          [query,edit]
        When false, and an object is rotated about a point other than its rotate pivot,
        its rotateTranslate attribute is modified to put the object at the correct
        position. When true, its translate attribute is used instead. Default is false.
    
    - orientAxes : oa                (float, float, float) [query,edit]
        Orients manipulator rotating around axes by specified angles
    
    - orientObject : oo              (unicode)       [create,edit]
        Orients manipulator to the passed in object/component
    
    - orientTowards : ot             (float, float, float) [create,edit]
        Orients active handle towards world point
    
    - pinPivot : pin                 (bool)          [query,edit]
        Pin component pivot. When the component pivot is set and pinned selection
        changes will not reset the pivot position and orientation.
    
    - pivotOriHandle : poh           (bool)          [query,edit]
        When true, the pivot manipulator will show the orientation handle during
        editing. Default is true.
    
    - position : p                   (bool)          [query]
        Returns the current position of the manipulator.
    
    - postCommand : psc              (script)        [create,edit]
        Specifies a command to be executed when the tool is exited.
    
    - postDragCommand : pod          (script, <type 'unicode'>) [create,edit]
        Specifies a command and a node type. The command will be executed at the end of
        a drag when a node of the specified type is in the selection.
    
    - preCommand : prc               (script)        [create,edit]
        Specifies a command to be executed when the tool is entered.
    
    - preDragCommand : prd           (script, <type 'unicode'>) [create,edit]
        Specifies a command and a node type. The command will be executed at the start
        of a drag when a node of the specified type is in the selection.
    
    - preserveChildPosition : pcp    (bool)          [query,edit]
        When false, the children objects move when their parent is rotated. When true,
        the worldspace position of the children will be maintained as the parent is
        moved. Default is false.
    
    - preserveUV : puv               (bool)          [query,edit]
        When false, the uvs are not changes to match the vertex edit. When true, the uvs
        are edited to project to new values to stop texture swimming as vertices are
        moved.
    
    - reflection : rfl               (bool)          []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionAbout : rab          (int)           []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionAxis : rfa           (int)           []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionTolerance : rft      (float)         []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - rotate : ro                    (float, float, float) [query,edit]
        Returns the rotation of the manipulator for its current orientation/mode.
    
    - snap : s                       (bool)          [create,query,edit]
        Specify that the manipulation is to use absolute snap
    
    - snapPivotOri : spo             (bool)          [query,edit]
        Snap pivot orientation. Modify pivot orientation when snapping the pivot to a
        component.
    
    - snapPivotPos : spp             (bool)          [query,edit]
        Snap pivot position. Modify pivot position when snapping the pivot to a
        component.
    
    - snapRelative : sr              (bool)          [create,query,edit]
        Specify that the manipulation is to use relative snap
    
    - snapValue : sv                 (float)         [create,query,edit]
        Specify the snapping value
    
    - tweakMode : twk                (bool)          [query,edit]
        When true, the manipulator is hidden and highlighted components can be selected
        and rotated in one step using a click-drag interaction.
    
    - useCenterPivot : ucp           (bool)          [query,edit]
        When true, use the center of the selection's bounding box as the center of the
        rotation (for all objects).
    
    - useManipPivot : ump            (bool)          [query,edit]
        When true, use the manipulator's center as the center of the rotation (for all
        objects).
    
    - useObjectPivot : uop           (bool)          [query,edit]
        When true, use each object's pivot as the center of its rotation.
    
    - xformConstraint : xc           (unicode)       [query,edit]
        none - no transform constraintedge - edge transform constraintsurface - surface
        transform constraintFlag can have multiple arguments, passed either as a tuple
        or a list.
    
    
    Derived from mel command `maya.cmds.manipRotateContext`
    """
    pass


def artAttrCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the
    base context for attribute painting operations. All commands require the name of
    the context as the last argument as this provides the name of the context to
    create, edit or query. This is a context command to set the flags on the
    Attribute Paint Tool context.
    
    Flags:
    - accopacity : aco               (bool)          [create,query,edit]
        Sets opacity accumulation on/off. C: Default is false (Except for sculpt tool
        for which it is true by default). Q: When queried, it returns a boolean.
    
    - activeListChangedProc : alp    (unicode)       [create,query,edit]
        Accepts a string that contains a MEL command that is invoked whenever the active
        list changes. There may be some situations where the UI, for example, needs to
        be updated, when objects are selected/deselected in the scene. In query mode,
        the name of the currently registered MEL command is returned and this will be an
        empty string if none is defined.
    
    - afterStrokeCmd : asc           (unicode)       [create,query,edit]
        The passed string is executed as a MEL command immediately after the end of a
        stroke. C: Default is no command. Q: When queried, it returns the current
        command
    
    - alphaclamp : alc               (unicode)       [create,query,edit]
        Specifies if the weight value should be alpha clamped to the lower and upper
        bounds. There are four options here: none- no clamping is performed, lower-
        clamps only to the lower bound, upper- clamps only to the upper bounds, both-
        clamps to the lower and upper bounds. C: Default is none.  Q: When queried, it
        returns a string.
    
    - alphaclamplower : acl          (float)         [create,query,edit]
        Specifies the lower bound for the alpha values. C: Default is 0.0.  Q: When
        queried, it returns a float.
    
    - alphaclampupper : acu          (float)         [create,query,edit]
        Specifies the upper bound for the alpha values. C: Default is 1.0.  Q: When
        queried, it returns a float.
    
    - attrSelected : asl             (unicode)       [query]
        Returns a name of the currently selected attribute. Q: When queried, it returns
        a string.
    
    - beforeStrokeCmd : bsc          (unicode)       [create,query,edit]
        The passed string is executed as a MEL command immediately before the start of a
        stroke. C: Default is no command. Q: When queried, it returns the current
        command
    
    - brushalignment : bra           (bool)          [create,query,edit]
        Specifies the path brush alignemnt. If true, the brush will align to stroke
        path, otherwise it will align to up vector. C: Default is true. Q: When queried,
        it returns a boolean.
    
    - brushfeedback : brf            (bool)          [create,query,edit]
        Specifies if the brush additional feedback should be drawn. C: Default is TRUE.
        Q: When queried, it returns a boolean.
    
    - clamp : cl                     (unicode)       [create,query,edit]
        Specifies if the weight value should be clamped to the lower and upper bounds.
        There are four options here: none- no clamping is performed, lower- clamps only
        to the lower bound, upper- clamps only to the upper bounds, both- clamps to the
        lower and upper bounds. C: Default is none.  Q: When queried, it returns a
        string.
    
    - clamplower : cll               (float)         [create,query,edit]
        Specifies the lower bound for the values. C: Default is 0.0.  Q: When queried,
        it returns a float.
    
    - clampupper : clu               (float)         [create,query,edit]
        Specifies the upper bound for the values. C: Default is 1.0.  Q: When queried,
        it returns a float.
    
    - clear : clr                    (bool)          [create,edit]
        Floods all cvs/vertices to the current value.
    
    - colorAlphaValue : cl1          (float)         [create,query,edit]
        The Alpha value of the color.
    
    - colorRGBAValue : cl4           (float, float, float, float) [create,query,edit]
        The RGBA value of the color.
    
    - colorRGBValue : cl3            (float, float, float) [create,query,edit]
        The RGB value of the color.
    
    - colorRamp : cr                 (unicode)       [create,query,edit]
        Allows a user defined color ramp to be used to map values to colors.
    
    - colorfeedback : cf             (bool)          [create,query,edit]
        Sets on/off the color feedback display. C: Default is FALSE.  Q: When queried,
        it returns a boolean.
    
    - colorfeedbackOverride : cfo    (bool)          [create,query,edit]
        Sets on/off the color feedback override. C: Default is FALSE.  Q: When queried,
        it returns a boolean.
    
    - colorrangelower : crl          (float)         [create,query,edit]
        Specifies the value that maps to black when color feedback mode is on. C:
        Default is 0.0.  Q: When queried, it returns a float.
    
    - colorrangeupper : cru          (float)         [create,query,edit]
        Specifies the value that maps to the maximum color when color feedback mode is
        on. C: Default is 1.0.  Q: When queried, it returns a float.
    
    - dataTypeIndex : dti            (int)           [query,edit]
        When the selected paintable attribute is a vectorArray, it specifies which field
        to paint on.
    
    - disablelighting : dl           (bool)          [create,query,edit]
        If color feedback is on, this flag determines whether lighting is disabled or
        not for the surfaces that are affected. C: Default is FALSE.  Q: When queried,
        it returns a boolean.
    
    - dragSlider : dsl               (unicode)       [create,edit]
        Sets the current brush drag state for resizing or offsetting the brush (like the
        'b' and 'm' default hotkeys). The string argument is one of: radius, lowradius,
        opacity, value, depth, displacement, uvvectoror none. C: Default is none.
    
    - duringStrokeCmd : dsk          (unicode)       [create,query,edit]
        The passed string is executed as a MEL command during the stroke, each time the
        mouse is dragged. C: Default is no command. Q: When queried, it returns the
        current command
    
    - dynclonemode : dcm             (bool)          [create,query,edit]
        Enable or disable dynamic clone mode.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - expandfilename : eef           (bool)          [create,edit]
        If true, it will expand the name of the export file and concatenate it with the
        surface name. Otherwise it will take the name as it is. C: Default is true.
    
    - exportaspectratio : ear        (float)         [create,query,edit]
        Value of aspect ratio for export
    
    - exportfilemode : efm           (unicode)       [create,query,edit]
        Specifies the export channel.The valid entries here are: alpha, luminance, rgb,
        rgba. C: Default is luminance/rgb. Q: When queried, it returns a string.
    
    - exportfilesave : esf           (unicode)       [edit]
        Exports the attribute map and saves to a specified file.
    
    - exportfilesizex : fsx          (int)           [create,query,edit]
        Specifies the width of the attribute map to export. C: Default width is 256. Q:
        When queried, it returns an integer.
    
    - exportfilesizey : fsy          (int)           [create,query,edit]
        Specifies the width of the attribute map to export. C: Default width is 256. Q:
        When queried, it returns an integer.
    
    - exportfiletype : eft           (unicode)       [create,query,edit]
        Specifies the image file format. It can be one of the following: iff, tiff,
        jpeg, alias, rgb, fitpostScriptEPS, softimage, wavefrontRLA, wavefrontEXP. C:
        default is tiff. Q: When queried, it returns a string.
    
    - filterNodes : fon              (bool)          [edit]
        Sets the node filter.
    
    - history : ch                   (bool)          [create]
        If this is a tool command, turn the construction history on for the tool in
        question.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - importfileload : ifl           (unicode)       [edit]
        Load the attribute map a specified file.
    
    - importfilemode : ifm           (unicode)       [create,query,edit]
        Specifies the channel to import. The valid entries here are: alpha, luminance,
        red, green, blue, and rgbC: Default is alpha. Q: When queried, it returns a
        string.
    
    - importreassign : irm           (bool)          [create,query,edit]
        Specifies if the multiply atrribute maps are to be reassigned while importing.
        Only maps previously exported from within Artisan can be reassigned. C: Default
        is FALSE. Q: When queried, it returns a  boolean.
    
    - interactiveUpdate : iu         (bool)          [create,query,edit]
        Specifies how often to transfer the painted values into the attribute. TRUE:
        transfer them continuously(many times per stroke) FALSE: transfer them only at
        the end of a stroke (on mouse button release). C: Default is TRUE. Q: When
        queried, it returns a boolean.
    
    - lastRecorderCmd : lrc          (unicode)       [create,query,edit]
        Value of last recorded command.
    
    - lastStampName : lsn            (unicode)       [create,query,edit]
        Value of the last stamp name.
    
    - lowerradius : lr               (float)         [create,query,edit]
        Sets the lower size of the brush (only apply on tablet).
    
    - makeStroke : mst               (int)           [create,query,edit]
        Stroke point values.
    
    - mappressure : mp               (unicode)       [create,query,edit]
        Sets the tablet pressure mapping when the table is used. There are four options:
        none- the pressure has no effect, opacity- the pressure is mapped to the
        opacity, radius- the is mapped to modify the radius of the brush, both- the
        pressure modifies both the opacity and the radius. C: Default is none. Q: When
        queried, it returns a string.
    
    - maxvalue : mxv                 (float)         [create,query,edit]
        Specifies the maximum value for each attribute. C: Default is 1.0.  Q: When
        queried, it returns a float.
    
    - minvalue : miv                 (float)         [create,query,edit]
        Specifies the minimum value for each attribute. C: Default is 0.0.  Q: When
        queried, it returns a float.
    
    - name : n                       (unicode)       [create]
        If this is a tool command, name the tool appropriately.
    
    - objattrArray : oaa             (unicode)       [query]
        An array of all paintable attributes. Each element of the array is a string with
        the following information: NodeType.NodeName.AttributeName.MenuType. \*MenuType:
        type (level) of the item in the Menu (UI). Q: When queried, it returns a string.
    
    - opacity : op                   (float)         [create,query,edit]
        Sets the brush opacity. C: Default is 1.0. Q: When queried, it returns a float.
    
    - outline : o                    (bool)          [create,query,edit]
        Specifies if the brush should be drawn. C: Default is TRUE. Q: When queried, it
        returns a boolean.
    
    - outwhilepaint : owp            (bool)          [create,query,edit]
        Specifies if the brush outline should be drawn while painting. C: Default is
        FALSE. Q: When queried, it returns a boolean.
    
    - paintNodeArray : pna           (unicode)       [query]
        An array of paintable nodes. Q: When queried, it returns a string.
    
    - paintattrselected : pas        (unicode)       [edit]
        An array of selected paintable attributes. Each element of the array is a string
        with the following information: NodeType.NodeName.AttributeName.
    
    - paintmode : pm                 (unicode)       [create,query,edit]
        Specifies the paint mode. There are two possibilities: screenand tangent. C:
        Default is screen. Q: When queried, it returns a string.
    
    - paintoperationtype : pot       (unicode)       [create,query,edit]
        Specifies the operation type used by the Paint Tool.  Currently, we support the
        following paint modes: Paint, Smear, Blur, Eraseand Clone. Default is Paint.
    
    - pickColor : pcm                (bool)          [create,query,edit]
        Set pick color mode on or off
    
    - pickValue : pv                 (bool)          [create,query,edit]
        Toggle for picking
    
    - playbackCursor : plc           (float, float)  [create,query,edit]
        Values for the playback cursor.
    
    - playbackPressure : plp         (float)         [create,query,edit]
        Valus for the playback pressure.
    
    - preserveclonesource : pcs      (bool)          [create,query,edit]
        Whether or not to preserve a clone source.
    
    - profileShapeFile : psf         (unicode)       [query,edit]
        Passes a name of the image file for the stamp shape profile.
    
    - projective : prm               (bool)          [create,query,edit]
        Specifies the projective paint mode. C: Default is 'false'. Q: When queried, it
        returns a boolean.
    
    - radius : r                     (float)         [create,query,edit]
        Sets the size of the brush. C: Default is 1.0 cm. Q: When queried, it returns a
        float.
    
    - rampMaxColor : rxc             (float, float, float) [create,query,edit]
        Defines a special color to be used when the value is greater than or equal to
        the maximum value.
    
    - rampMinColor : rmc             (float, float, float) [create,query,edit]
        Defines a special color to be used when the value is less than or equal to the
        minimum value.
    
    - record : rec                   (bool)          [create,query,edit]
        Toggle on for recording.
    
    - reflection : rn                (bool)          [create,query,edit]
        Specifies the reflection mode. C: Default is 'false'. Q: When queried, it
        returns a boolean.
    
    - reflectionaboutorigin : rno    (bool)          [create,query,edit]
        Toggle on to reflect about the origin
    
    - reflectionaxis : ra            (unicode)       [create,query,edit]
        Specifies the reflection axis. There are three possibilities: x, yand z. C:
        Default is x. Q: When queried, it returns a string.
    
    - screenRadius : scR             (float)         [create,query,edit]
        Brush radius on the screen
    
    - selectclonesource : scs        (bool)          [create,query,edit]
        Toggle on to select the clone source
    
    - selectedattroper : sao         (unicode)       [create,query,edit]
        Sets the edit weight operation. Four edit weights operations are provided :
        absolute- the value of the weight is replaced by the current one, additive- the
        value of the weight is added to the current one, scale- the value of the weight
        is multiplied by the current one, smooth- the value of the weight is divided by
        the current one. C: Default is absolute.  Q: When queried, it returns a string.
    
    - showactive : sa                (bool)          [create,query,edit]
        Sets on/off the display of the surface isoparms. C: Default is TRUE. Q: When
        queried, it returns a boolean.
    
    - stampDepth : stD               (float)         [create,query,edit]
        Depth of the stamps
    
    - stampProfile : stP             (unicode)       [create,query,edit]
        Sets the brush profile of the current stamp. Currently, the following profiles
        are supported: gaussian, soft, solidand square. C: Default is gaussian. Q: When
        queried, it returns a string.
    
    - stampSpacing : stS             (float)         [create,query,edit]
        Specifies the stamp spacing. Default is 1.0.
    
    - strokesmooth : ssm             (unicode)       [create,query,edit]
        Stroke smoothing type name
    
    - surfaceConformedBrushVertices : scv (bool)          [create,query,edit]
        Enables/disables the the display of the effective brush area as affected
        vertices.
    
    - tablet : tab                   (bool)          [query]
        Returns true if the tablet device is present, false if it is absent
    
    - tangentOutline : to            (bool)          [create,query,edit]
        Enables/disables the display of the brush circle tangent to the surface.
    
    - toolOffProc : tfp              (unicode)       [create,query,edit]
        Accepts a strings describing the name of a MEL procedure that is invoked
        whenever the tool is turned off. For example, cloth invokes
        clothPaintToolOffwhen the cloth paint tool is turned on. Define this callback if
        your tool requires special functionality when your tool is deactivated. It is
        typical that if you implement a toolOffProc you will want to implement a
        toolOnProc as well (see the -toolOnProc flag. In query mode, the name of the
        currently registered MEL command is returned and this will be an empty string if
        none is defined.
    
    - toolOnProc : top               (unicode)       [create,query,edit]
        Accepts a strings describing the name of a MEL procedure that is invoked
        whenever the tool is turned on. For example, cloth invokes clothPaintToolOnwhen
        the cloth paint tool is turned on. Define this callback if your tool requires
        special functionality when your tool is activated. It is typical that if you
        implement a toolOnProc you will want to implement a toolOffProc as well (see the
        -toolOffProc flag. In query mode, the name of the currently registered MEL
        command is returned and this will be an empty string if none is defined.
    
    - useColorRamp : ucr             (bool)          [create,query,edit]
        Specifies whether the user defined color ramp should be used to map values from
        to colors.  If this is turned off, the default greyscale feedback will be used.
    
    - useMaxMinColor : umc           (bool)          [create,query,edit]
        Specifies whether the out of range colors should be used.  See rampMinColor and
        rampMaxColor flags for further details.
    
    - usepressure : up               (bool)          [create,query,edit]
        Sets the tablet pressure on/off. C: Default is false. Q: When queried, it
        returns a boolean.
    
    - value : val                    (float)         [create,query,edit]
        Specifies the value for each attribute. C: Default is 0.0.  Q: When queried, it
        returns a float.
    
    - whichTool : wst                (unicode)       [create,query,edit]
        The string defines the name of the tool to be used for the Artisan context. An
        example is artClothPaint. In query mode, the tool name for the given context is
        returned. Note: due to the way MEL works, always specify the -query flag last
        when specifying a flag that takes arguments.
    
    - worldRadius : wlR              (float)         [create,query,edit]
        Radius in worldspace                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.artAttrCtx`
    """
    pass


def manipMoveContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a move manip context. Note
    that the flags -s, -sv, -sr, -scr, -slp, -slf control the global behaviour of
    all move manip context.  Changing one context independently is not allowed.
    Changing a context's behaviour using the above flags, will change all existing
    move manip context.
    
    Flags:
    - activeHandle : ah              (int)           [query,edit]
        Sets the default active handle for the manip.  That is, the handle which should
        be initially active when the tool is activated. Values can be: 0 - X axis handle
        is active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
        (all 3 axes) is active (default)
    
    - activeHandleNormal : ahn       (int)           [query,edit]
        0 - U axis handle is active1 - V axis handle is active2 - N axis handle is
        active ( default )3 - Center handle (all 3 axes) is activeapplicable only when
        the manip mode is 3.
    
    - alignAlong : aa                (float, float, float) [create,edit]
        Aligns active handle along vector.
    
    - constrainAlongNormal : xn      (bool)          [query,edit]
        When true, transform constraints are applied along the vertex normal first and
        only use the closest point when no intersection is found along the normal.
    
    - currentActiveHandle : cah      (int)           [query,edit]
        Sets the active handle for the manip. Values can be: 0 - X axis handle is
        active1 - Y axis handle is active2 - Z axis handle is active3 - Center handle
        (all 3 axes) is active4 - XY plane handle is active5 - YZ plane handle is
        active6 - XZ plane handle is active
    
    - editPivotMode : epm            (bool)          [query]
        Returns true manipulator is in edit pivot mode
    
    - editPivotPosition : epp        (bool)          [query]
        Returns the current position of the edit pivot manipulator.
    
    - exists : ex                    (bool)          [create]
        Returns true or false depending upon whether the specified object exists. Other
        flags are ignored.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons representing the tool associated with the context.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons representing the tool associated with the
        context.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons representing the tool associated with the context.
    
    - interactiveUpdate : iu         (bool)          [query,edit]
        Value can be : true or false. This flag value is valid only if the mode is 3
        i.e. move vertex normal.
    
    - lastMode : lm                  (int)           [query]
        Returns the previous translation mode.
    
    - manipVisible : vis             (bool)          [query]
        Returns true if the main translate manipulator is visible.
    
    - mode : m                       (int)           [query,edit]
        Translate mode: 0 - Object Space1 - Local Space2 - World Space (default)3 - Move
        Along Vertex Normal4 - Move Along Rotation Axis5 - Move Along Live Object Axis6
        - Custom Axis Orientation10 - Component Space
    
    - orientAxes : oa                (float, float, float) [query,edit]
        Orients manipulator rotating around axes by specified angles
    
    - orientJoint : oj               (unicode)       [query,edit]
        Specifies the type of orientation for joint orientation. Valid options are:
        none, xyz, xzy, yxz, yzx, zxy, zyx.
    
    - orientJointEnabled : oje       (bool)          [query,edit]
        Specifies if joints should be reoriented when moved.
    
    - orientObject : oo              (unicode)       [create,edit]
        Orients manipulator to the passed in object/component
    
    - orientTowards : ot             (float, float, float) [create,edit]
        Orients active handle towards world point
    
    - pinPivot : pin                 (bool)          [query,edit]
        Pin component pivot. When the component pivot is set and pinned selection
        changes will not reset the pivot position and orientation.
    
    - pivotOriHandle : poh           (bool)          [query,edit]
        When true, the pivot manipulator will show the orientation handle during
        editing. Default is true.
    
    - position : p                   (bool)          [query]
        Returns the current position of the manipulator
    
    - postCommand : psc              (script)        [create,edit]
        Specifies a command to be executed when the tool is exited.
    
    - postDragCommand : pod          (script, <type 'unicode'>) [create,edit]
        Specifies a command and a node type. The command will be executed at the end of
        a drag when a node of the specified type is in the selection.
    
    - preCommand : prc               (script)        [create,edit]
        Specifies a command to be executed when the tool is entered.
    
    - preDragCommand : prd           (script, <type 'unicode'>) [create,edit]
        Specifies a command and a node type. The command will be executed at the start
        of a drag when a node of the specified type is in the selection.
    
    - preserveChildPosition : pcp    (bool)          [query,edit]
        When false, the children objects move when their parent is moved. When true, the
        worldspace position of the children will be maintained as the parent is moved.
        Default is false.
    
    - preserveUV : puv               (bool)          [query,edit]
        When false, the uvs are not changes to match the vertex edit. When true, the uvs
        are edited to project to new values to stop texture swimming as vertices are
        moved.
    
    - reflection : rfl               (bool)          []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionAbout : rab          (int)           []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionAxis : rfa           (int)           []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - reflectionTolerance : rft      (float)         []
        This flag is obsolete. Reflection is now managed as part of selection itself
        using the symmetricModeling command.
    
    - secondaryAxisOrient : sao      (unicode)       [query,edit]
        Specifies the global axis (in world coordinates) that should be used to should
        be used to align the second axis of the orientJointType triple. Valid options
        are xup, yup, zup, xdown, ydown, zdown, none.
    
    - snap : s                       (bool)          [query,edit]
        Value can be : true or false. Enable/Disable the discrete move. If set to true,
        the move manipulator of all the move contexts would snap at discrete points
        along the active handle during mouse drag.  The interval between the points can
        be controlled using the 'snapValue' flag.
    
    - snapComponentsRelative : scr   (bool)          [query,edit]
        Value can be : true or false. If true, while snapping a group of CVs/Vertices,
        the relative spacing between them will be preserved. If false, all the
        CVs/Vertices will be snapped to the target point (is used during grid
        snap(hotkey 'x'), and point snap(hotkey 'v')) Depress the 'x' key before click-
        dragging the manip handle and check to see the behaviour of moving a bunch of
        CVs, with this flag ON and OFF.
    
    - snapLiveFaceCenter : slf       (bool)          [query,edit]
        Value can be : true or false. If true, while moving on the live polygon object,
        the move manipulator will snap to the face centers of the object.
    
    - snapLivePoint : slp            (bool)          [query,edit]
        Value can be : true or false. If true, while moving on the live polygon object,
        the move manipulator will snap to the vertices of the object.
    
    - snapPivotOri : spo             (bool)          [query,edit]
        Snap pivot orientation. Modify pivot orientation when snapping the pivot to a
        component.
    
    - snapPivotPos : spp             (bool)          [query,edit]
        Snap pivot position. Modify pivot position when snapping the pivot to a
        component.
    
    - snapRelative : sr              (bool)          [query,edit]
        Value can be : true or false. Applicable only when the snap is enabled. If true,
        the snapValue is treated relative to the original position before moving. If
        false, the snapValue is treated relative to the world origin. NOTE:    If in
        local/object Space Mode, the snapRelative should be ON. Absolute discrete move
        is not supported in local/object mode.
    
    - snapValue : sv                 (float)         [query,edit]
        Applicable only when the snap is enabled. The manipulator of all move contexts
        would move in steps of 'snapValue'
    
    - translate : tr                 (float, float, float) [query,edit]
        Returns the translation of the manipulator for its current orientation/mode.
    
    - tweakMode : twk                (bool)          [query,edit]
        When true, the manipulator is hidden and highlighted components can be selected
        and moved in one step using a click-drag interaction.
    
    - xformConstraint : xc           (unicode)       [query,edit]
        none - no transform constraintedge - edge transform constraintsurface - surface
        transform constraintFlag can have multiple arguments, passed either as a tuple
        or a list.
    
    
    Derived from mel command `maya.cmds.manipMoveContext`
    """
    pass
