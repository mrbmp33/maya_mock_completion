from pymel.internal.pmcmds import movIn
from pymel.internal.pmcmds import wrinkle
from pymel.internal.pmcmds import pose
from pymel.internal.pmcmds import copySkinWeights
from pymel.internal.pmcmds import evaluator
from pymel.internal.pmcmds import ikHandleDisplayScale
from pymel.internal.pmcmds import playblast
from pymel.internal.pmcmds import clipSchedule
from pymel.internal.pmcmds import tangentConstraint as cmd
from pymel.internal.pmcmds import insertJoint
from pymel.internal.pmcmds import timeEditorClipLayer
from pymel.internal.pmcmds import jointDisplayScale
from pymel.internal.pmcmds import hikGlobals
from pymel.internal.pmcmds import ubercam
from pymel.internal.pmcmds import shapeEditor
from pymel.internal.pmcmds import applyTake
from pymel.internal.pmcmds import writeTake
from pymel.internal.pmcmds import animDisplay
from pymel.internal.pmcmds import recordDevice
from pymel.internal.pmcmds import deviceManager
from pymel.internal.pmcmds import clip
from pymel.internal.pmcmds import deformerWeights
from pymel.internal.pmcmds import skeletonEmbed
from pymel.internal.pmcmds import setInfinity
from pymel.internal.pmcmds import setDrivenKeyframe
from pymel.internal.pmcmds import buildKeyframeMenu
from pymel.internal.pmcmds import sound
from pymel.internal.pmcmds import removeJoint
from pymel.internal.pmcmds import percent
from pymel.internal.pmcmds import mirrorJoint
from pymel.internal.pmcmds import defineVirtualDevice
from pymel.internal.pmcmds import clipEditor
from pymel.internal.pmcmds import connectJoint
from pymel.internal.pmcmds import findDeformers
from pymel.internal.pmcmds import autoKeyframe
from pymel.internal.pmcmds import setKeyframeBlendshapeTargetWts
from pymel.internal.pmcmds import reorderDeformers
from pymel.internal.pmcmds import evaluationManager
from pymel.internal.pmcmds import clipMatching
from pymel.internal.pmcmds import playbackOptions
from pymel.internal.pmcmds import ikfkDisplayMethod
from pymel.internal.pmcmds import freezeOptions
from pymel.internal.pmcmds import bindSkin
from pymel.internal.pmcmds import movieInfo
from pymel.internal.pmcmds import setKeyframe
from pymel.internal.pmcmds import bakeClip
from pymel.internal.pmcmds import skinPercent
from pymel.internal.pmcmds import dopeSheetEditor
from pymel.internal.pmcmds import poseEditor
from pymel.internal.pmcmds import shotRipple
from pymel.internal.pmcmds import blendShapeEditor
from pymel.internal.pmcmds import enableDevice
from pymel.internal.pmcmds import ikSystemInfo
from pymel.internal.pmcmds import pathAnimation
from pymel.internal.pmcmds import copyDeformerWeights
from pymel.internal.pmcmds import timeEditorClipOffset
from pymel.internal.pmcmds import animView
from pymel.internal.pmcmds import marker
from pymel.internal.pmcmds import buildBookmarkMenu
from pymel.internal.pmcmds import filterCurve
from pymel.internal.pmcmds import polyUniteSkinned
from pymel.internal.pmcmds import disconnectJoint
from pymel.internal.pmcmds import readTake
from pymel.internal.pmcmds import characterize
from pymel.internal.pmcmds import sculptTarget
from pymel.internal.pmcmds import reroot
from pymel.internal.pmcmds import timeEditorComposition
from pymel.internal.pmcmds import defineDataServer
from pymel.internal.pmcmds import rotationInterpolation
from pymel.internal.pmcmds import copyFlexor
from pymel.internal.pmcmds import play
from pymel.internal.pmcmds import substituteGeometry
from pymel.internal.pmcmds import timeEditorBakeClips
from pymel.internal.pmcmds import effector
from pymel.internal.pmcmds import setKeyPath
from pymel.internal.pmcmds import volumeBind
from pymel.internal.pmcmds import backgroundEvaluationManager

if False:
    from typing import Dict, List, Tuple, Union, Optional


def _poleVectorConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def cluster(*args, **kwargs):
    """
    The cluster command creates a cluster or edits the membership of an existing
    cluster. The command returns the name of the cluster node upon creation of a new
    cluster. After creating a cluster, the cluster's weights can be modified using
    the percent command or the set editor window.
    
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
    
    - bindState : bs                 (bool)          [create]
        When turned on, this flag adds in a compensation to ensure the clustered objects
        preserve their spatial position when clustered. This is required to prevent the
        geometry from jumping at the time the cluster is created in situations when the
        cluster transforms at cluster time are not identity.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - envelope : en                  (float)         [create,query,edit]
        Set the envelope value for the deformer. Default is 1.0
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - relative : rel                 (bool)          [create]
        Enable relative mode for the cluster. In relative mode, Only the transformations
        directly above the cluster are used by the cluster. Default is off.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - resetGeometry : rg             (bool)          [edit]
        Reset the geometry matrices for the objects being deformed by the cluster. This
        flag is used to get rid of undesirable effects that happen if you scale an
        object that is deformed by a cluster.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - weightedNode : wn              (unicode, unicode) [create,query,edit]
        Transform node in the DAG above the cluster to which all percents are applied.
        The second DAGobject specifies the descendent of the first DAGobject from where
        the transformation matrix is evaluated. Default is the cluster handle.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.cluster`
    """
    pass


def mute(*args, **kwargs):
    """
    The mute command is used to disable and enable playback on a channel. When a
    channel is muted, it retains the value that it was at prior to being muted.
    
    Flags:
    - disable : d                    (bool)          [create]
        Disable muting on the channels
    
    - force : f                      (bool)          [create]
        Forceable disable of muting on the channels. If there are keys on the mute
        channel, the animation and mute node will both be removed.  If this flag is not
        set, then mute nodes with animation will only be disabled.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.mute`
    """
    pass


def wire(*args, **kwargs):
    """
    This command creates a wire deformer. In the create mode the selection list is
    treated as the object(s) to be deformed, Wires are specified with the -w flag.
    Each wire can optionally have a holder which helps define the the regon of the
    object that is affected by the deformer.
    
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
    
    - crossingEffect : ce            (float)         [create,query,edit]
        Set the amount of convolution effect. Varies from fully convolved at 0 to a
        simple additive effect at 1 (which is what you get with the filter off). Default
        is 0. This filter should make its way into all blend nodes that deal with
        combining effects from multiple sources.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - dropoffDistance : dds          (int, float)    [create,query,edit]
        Set the dropoff distance (second parameter) for the wire at index (first
        parameter).
    
    - envelope : en                  (float)         [create,query,edit]
        Set the envelope value for the deformer. Default is 1.0
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - groupWithBase : gw             (bool)          [create]
        Groups the wire with the base wire so that they can easily be moved together to
        create a ripple effect. Default is false.
    
    - holder : ho                    (int, unicode)  [create,query,edit]
        Set the specified curve or surface (second parameter  as a holder for the wire
        at index (first parameter).
    
    - ignoreSelected : ignoreSelected (bool)          [create]
        Tells the command to not deform objects on the current selection list
    
    - includeHiddenSelections : ihs  (bool)          [create]
        Apply the deformer to any visible and hidden objects in the selection list.
        Default is false.
    
    - localInfluence : li            (float)         [create,query,edit]
        Set the local control a wire has with respect to other wires irrespective of
        whether it is deforming the surface. Varies from no local effect at 0 to full
        local control at 1. Default is 0.
    
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
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - wire : w                       (unicode)       [create,query,edit]
        Specify or query the wire curve name.
    
    - wireCount : wc                 (int)           [create,query,edit]
        Set the number of wires.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.wire`
    """
    pass


def combinationShape(*args, **kwargs):
    """
    Command to create or edit drive relationship of blend shape targets
    
    Flags:
    - addDriver : add                (bool)          []
        Add drivers to the combination shape
    
    - allDrivers : ald               (bool)          [query]
        All drivers of the combination shape
    
    - blendShape : bs                (unicode)       [create]
        Associated blend shape node of the combination shape In query mode, this flag
        can accept a value.
    
    - combinationTargetIndex : cti   (int)           [create]
        Driven blend shape target index of the combination shape In query mode, this
        flag can accept a value.
    
    - combinationTargetName : ctn    (unicode)       [create]
        Driven blend shape target name of the combination shape In query mode, this flag
        can accept a value.
    
    - combineMethod : cm             (int)           [create,query,edit]
        Combine method of the combination shape: 0 : Multiplication1 : Lowest Weighting2
        : Lowest Weighting (Smooth)
    
    - driverTargetIndex : dti        (int)           [create]
        Driver blend shape target index of the combination shape
    
    - driverTargetName : dtn         (unicode)       [create]
        Driver blend shape target name of the combination shape
    
    - exist : ex                     (bool)          [query]
        If the combination shape exist
    
    - removeDriver : rmd             (bool)          []
        Remove drivers from the combination shape                                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.combinationShape`
    """
    pass


def keyTangent(*args, **kwargs):
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
    list or range (see Examples). This command edits or queries tangent properties
    of keyframes in a keyset.  It is also used to edit or query the default tangent
    type of newly created keyframes (see the setKeyframe command for more
    information on how to override this default). Tangents help manage the shape of
    the animation curve and affect the interpolation between keys.  The tangent
    angle specifies the direction the curve will take as it leaves (or enters) a
    key. The tangent weight specifies how much influence the tangent angle has on
    the curve before the curve starts towards the next key. Maya internally
    represents tangents as x and y values.  Refer to the API documentation for
    MFnAnimCurve for a description of the relationship between tangent angle and
    weight and the internal x and y values.
    
    Flags:
    - absolute : a                   (bool)          [create,edit]
        Changes to tangent positions are NOT relative to the current position.
    
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - g : g                          (bool)          [create]
        Required for all operations on the global tangent type. The global tangent type
        is used by the setKeyframe command when tangent types have not been specifically
        applied, except in combination with flags such as 'i/insert' which preserve the
        shape of the curve.  It is also used when keys are set from the menu. The only
        flags that can appear on a keyTangent command with the 'g/global' flag are
        'itt/inTangentType', 'ott/outTangentType' and 'wt/weightedTangents'.
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
    - inAngle : ia                   (float)         [create,query,edit]
        New value for the angle of the in-tangent. Returns a float[] when queried.
    
    - inTangentType : itt            (unicode)       [create,query,edit]
        Specify the in-tangent type.  Valid values are
        spline,linear,fast,slow,flat,step,stepnext,fixed,clamped,plateauand auto.
        Returns a string[] when queried.
    
    - inWeight : iw                  (float)         [create,query,edit]
        New value for the weight of the in-tangent. Returns a float[] when queried.
    
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
    
    - ix : ix                        (float)         [create,query,edit]
        New value for the x-component of the in-tangent. This is a unit independent
        representation of the tangent component. Returns a float[] when queried.
    
    - iy : iy                        (float)         [create,query,edit]
        New value for the y-component of the in-tangent. This is a unit independent
        representation of the tangent component. Returns a float[] when queried.
    
    - lock : l                       (bool)          [create,query,edit]
        Lock a tangent so in and out tangents move together. Returns an int[] when
        queried.
    
    - outAngle : oa                  (float)         [create,query,edit]
        New value for the angle of the out-tangent. Returns a float[] when queried.
    
    - outTangentType : ott           (unicode)       [create,query,edit]
        Specify the out-tangent type.  Valid values are
        spline,linear,fast,slow,flat,step,stepnext,fixed,clamped,plateauand auto.
        Returns a string[] when queried.
    
    - outWeight : ow                 (float)         [create,query,edit]
        New value for the weight of the out-tangent. Returns a float[] when queried.
    
    - ox : ox                        (float)         [create,query,edit]
        New value for the x-component of the out-tangent. This is a unit independent
        representation of the tangent component. Returns a float[] when queried.
    
    - oy : oy                        (float)         [create,query,edit]
        New value for the y-component of the out-tangent. This is a unit independent
        representation of the tangent component. Returns a float[] when queried.
    
    - pluginTangentTypes : ptt       (unicode)       [query]
        Returns a list of the plug-in tangent types that have been loaded. Return type
        is a string array.
    
    - relative : r                   (bool)          [create,edit]
        Changes to tangent positions are relative to the current position.
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - stepAttributes : sa            (bool)          [create,edit]
        The setKeyframe command will automatically set tangents for boolean and
        enumerated attributes to step.  This flag mirrors this behavior for the
        keyTangent command.  When set to false, tangents for these attributes will not
        be edited.  When set to true (the default) tangents for these attributes will be
        edited.
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - unify : uni                    (bool)          [create,edit]
        Unify a tangent so in and out tangents are equal and move together.
    
    - weightLock : wl                (bool)          [create,query,edit]
        Lock the weight of a tangent so it is fixed. Returns an int[] when queried.
        Note: weightLock is only obeyed within the graph editor.  It is not obeyed when
        -inWeight/-outWeight are issued from a command.
    
    - weightedTangents : wt          (bool)          [create,query,edit]
        Specify whether or not the tangents on the animCurve are weighted Note:
        switching a curve from weightedTangents true to false and back to true again
        will not preserve fixed tangents properly. Use undo instead.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyTangent`
    """
    pass


def bufferCurve(*args, **kwargs):
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
    list or range (see Examples). This command helps manage buffer curve for
    animated objects
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - exists : ex                    (bool)          [query]
        Returns true if a buffer curve currently exists on the specified attribute;
        false otherwise.
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
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
    
    - overwrite : ov                 (bool)          [create]
        Create a buffer curve.  truemeans create a buffer curve whether or not one
        already existed.  falsemeans if a buffer curve exists already then leave it
        alone.  If no flag is specified, then the command defaults to -overwrite false
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - swap : sw                      (bool)          [create]
        For animated attributes which have buffer curves, swap the buffer curve with the
        current animation curve
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - useReferencedCurve : urc       (bool)          [create,query]
        In create mode, sets the buffer curve to the referenced curve. Curves which are
        not from file references will ignore this flag. In query mode, returns true if
        the selected keys are displaying their referenced curve as the buffer curve, and
        false if they are not.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.bufferCurve`
    """
    pass


def animCurveEditor(*args, **kwargs):
    """
    Edit a characteristic of a graph editor
    
    Flags:
    - areCurvesSelected : acs        (bool)          [query]
        Returns a boolean to know if at least one curve is selected in the graph editor.
    
    - autoFit : af                   (unicode)       [query,edit]
        on | off | tgl Auto fit-to-view.
    
    - autoFitTime : aft              (unicode)       [query,edit]
        on | off | tgl Auto fit-to-view along the time axis, as well.
    
    - classicMode : cm               (bool)          [query,edit]
        When on, the graph editor is displayed in Classic Mode, otherwise Suites Modeis
        used.
    
    - clipTime : ct                  (unicode)       [query,edit]
        Valid values: onoffDisplay the clips with their offset and scale applied to the
        anim curves in the clip.
    
    - constrainDrag : cd             (int)           [create,query,edit]
        Constrains all Graph Editor animation curve drag operations to either the
        X-axis, the Y-axis, or to neither of those axes. Values to supply are: 0 for not
        constraining any axis, 1 for constraing the X-axis, or 2 for constraining the
        Y-axis. When used in queries, this flag returns the latter values and these
        values have the same interpretation as above. Note: when the shift key is
        pressed before dragging the animation curve, the first mouse movement will
        instead determine (and override) any prior set constrained axis.
    
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - curvesShown : cs               (bool)          [query]
        Returns a string array containing the names of the animCurve nodes currently
        displayed in the graph editor.
    
    - curvesShownForceUpdate : csf   (bool)          [query]
        Returns a string array containing the names of the animCurve nodes currently
        displayed in the graph editor. Unlike the curvesShown flag, this will force an
        update of the graph editor for the case where the mainListConnection has been
        modified since the last refresh.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - denormalizeCurvesCommand : dcc (unicode)       [create,edit]
        Sets the script that is run to denormalize curves in the graph editor. This is
        intended for internal use only.
    
    - displayActiveKeyTangents : dat (unicode)       [edit]
        on | off | tgl Display active key tangents in the editor.
    
    - displayActiveKeys : dak        (unicode)       [edit]
        on | off | tgl Display active keys in the editor.
    
    - displayInfinities : di         (unicode)       [edit]
        on | off | tgl Display infinities in the editor.
    
    - displayKeys : dk               (unicode)       [edit]
        on | off | tgl Display keyframes in the editor.
    
    - displayNormalized : dn         (bool)          [query,edit]
        When on, display all curves normalized to the range -1 to +1.
    
    - displayTangents : dtn          (unicode)       [edit]
        on | off | tgl Display tangents in the editor.
    
    - displayValues : dv             (unicode)       [edit]
        on | off | tgl Display active keys and tangents values in the editor.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - filter : f                     (unicode)       [create,query,edit]
        Specifies the name of an itemFilter object to be used with this editor. This
        filters the information coming onto the main list of the editor.
    
    - forceMainConnection : fmc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object. This is a variant of the -mainListConnection flag in
        that it will force a change even when the connection is locked. This flag is
        used to reduce the overhead when using the -unlockMainConnection ,
        -mainListConnection, -lockMainConnection flags in immediate succession.
    
    - highlightConnection : hlc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its highlight list. Not all editors have a highlight list. For
        those that do, it is a secondary selection list.
    
    - keyingTime : kt                (unicode)       [query]
        The current time in the given curve to be keyed in the graph editor.
    
    - lockMainConnection : lck       (bool)          [create,edit]
        Locks the current list of objects within the mainConnection, so that only those
        objects are displayed within the editor. Further changes to the original
        mainConnection are ignored.
    
    - lookAt : la                    (unicode)       [edit]
        all | selected | currentTime FitView helpers.
    
    - mainListConnection : mlc       (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object.
    
    - menu : m                       (script)        [create]
        Specify a script to be run when the editor is created.  The function will be
        passed one string argument which is the new editor's name.
    
    - normalizeCurvesCommand : ncc   (unicode)       [create,edit]
        Sets the script that is run to normalize curves in the graph editor. This is
        intended for internal use only.
    
    - outliner : o                   (unicode)       [query,edit]
        The name of the outliner that is associated with the graph editor.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - preSelectionHighlight : psh    (bool)          [query,edit]
        When on, the curve/key/tangent under the mouse pointer is highlighted to ease
        selection.
    
    - renormalizeCurves : rnc        (bool)          [edit]
        This flag causes the curve normalization factors to be recalculated.
    
    - resultSamples : rs             (time)          [query,edit]
        Specify the sampling for result curves Note: the smaller this number is, the
        longer it will take to update the display.
    
    - resultScreenSamples : rss      (int)           [query,edit]
        Specify the screen base result sampling for result curves. If 0, then results
        are sampled in time.
    
    - resultUpdate : ru              (unicode)       [query,edit]
        Valid values: interactivedelayedControls how changes to animCurves are reflected
        in the result curves (if results are being shown).  If resultUpdate is
        interactive, then as interactive changes are being made to the animCurve, the
        result curves will be updated.  If modelUpdate is delayed (which is the default
        setting), then result curves are updated once the final change to an animCurve
        has been made.
    
    - selectionConnection : slc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its own selection list. As the user selects things in this
        editor, they will be selected in the selectionConnection object. If the object
        undergoes changes, the editor updates to show the changes.
    
    - showActiveCurveNames : acn     (bool)          [query,edit]
        Display the active curve(s)'s name.
    
    - showBufferCurves : sb          (unicode)       [query,edit]
        Valid values: onofftglDisplay buffer curves.
    
    - showCurveNames : scn           (bool)          [query,edit]
        Display the curves's name.
    
    - showResults : sr               (unicode)       [query,edit]
        Valid values: onofftglDisplay result curves from expression or other non-keyed
        action.
    
    - showUpstreamCurves : suc       (bool)          [query,edit]
        If true, the dependency graph is searched upstream for all curves that drive the
        selected plugs (showing multiple curves for example in a typical driven key
        setup, where first the driven key curve is encountered, followed by the actual
        animation curve that drives the source object). If false, only the first curves
        encountered will be shown. Note that, even if false, multiple curves can be
        shown if e.g. a blendWeighted node is being used to combine multiple curves.
    
    - smoothness : s                 (unicode)       [query,edit]
        Valid values: coarseroughmediumfineSpecify the display smoothness of animation
        curves.
    
    - snapTime : st                  (unicode)       [query,edit]
        none | integer | keyframe Keyframe move snap in time.
    
    - snapValue : sv                 (unicode)       [query,edit]
        none | integer | keyframe Keyframe move snap in values.
    
    - stackedCurves : sc             (bool)          [query,edit]
        Switches the display mode between normal (all curves sharing one set of axes) to
        stacked (each curve on its own value axis, stacked vertically).
    
    - stackedCurvesMax : scx         (float)         [query,edit]
        Sets the maximum value on the per-curve value axis when in stacked mode.
    
    - stackedCurvesMin : scm         (float)         [query,edit]
        Sets the minimum value on the per-curve value axis when in stacked mode.
    
    - stackedCurvesSpace : scs       (float)         [query,edit]
        Sets the spacing between curves when in stacked mode.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - unParent : up                  (bool)          [create,edit]
        Specifies that the editor should be removed from its layout. This cannot be used
        in query mode.
    
    - unlockMainConnection : ulk     (bool)          [create,edit]
        Unlocks the mainConnection, effectively restoring the original mainConnection
        (if it is still available), and dynamic updates.
    
    - updateMainConnection : upd     (bool)          [create,edit]
        Causes a locked mainConnection to be updated from the orginal mainConnection,
        but preserves the lock state.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - valueLinesToggle : vlt         (unicode)       [edit]
        on | off | tgl Display the value lines for high/low/zero of selected curves in
        the editor                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    - viewLeft : vl                  (float)         []
    
    - viewRight : vr                 (float)         []
    
    
    Derived from mel command `maya.cmds.animCurveEditor`
    """
    pass


def timeEditorAnimSource(*args, **kwargs):
    """
    Commands for managing animation sources.
    
    Flags:
    - addObjects : ao                (unicode)       [create,query,edit]
        Populate the given object(s) and their attributes to anim source to Time Editor.
        For multiple object, pass each name separated by semicolon. In query mode,
        return the number of attributes that will be populated given the flags, along
        with the animation's first and last frames for the given object(s). Similar to
        -addSelectedObjectsflag but acts on given object(s) instead. This flag will
        override the flag -addSelectedObjects.
    
    - addRelatedKG : akg             (bool)          [create,query,edit]
        During population, determine if associated keying groups should be populated or
        not. Normally used for populating HIK. By default the value is false.
    
    - addSelectedObjects : aso       (bool)          [create,query,edit]
        Populate the currently selected objects and their attributes to anim source or
        Time Editor. In query mode, return the number of attributes that will be
        populated given the flags, along with the animation's first and last frames.
    
    - addSource : asc                (unicode)       [edit]
        Add single new target attribute with its animation.
    
    - apply : ap                     (bool)          [edit]
        Connect anim source's animation directly to the target objects. If the Time
        Editor is not muted, connect to scene storage instead.
    
    - attribute : at                 (unicode)       [create,edit]
        Populate a specific attribute on a object.
    
    - bakeToAnimSource : bas         (unicode)       [edit]
        Create a new anim source with the same animation as this anim source. All non-
        curve inputs will be baked down, whereas curve sources will be shared.
    
    - calculateTiming : ct           (bool)          [query,edit]
        Adjust start/duration when adding/removing sources. If query it returns the
        [start,duration] pair.
    
    - copyAnimation : cp             (bool)          [edit]
        Copy animation when adding source.
    
    - drivenClips : dc               (bool)          [query]
        Return all clips driven by the given anim source.
    
    - exclusive : exc                (bool)          [create,edit]
        Populate all types of animation sources which are not listed by typeFlag.
    
    - export : ex                    (unicode)       [edit]
        Export given anim source and the animation curves to a specified Maya file.
    
    - importAllFbxTakes : aft        (bool)          [create]
        Import all FBX takes into the new anim sources (for timeEditorAnimSource
        command) or new containers (for timeEditorClip command).
    
    - importFbx : fbx                (unicode)       [create]
        Import an animation from FBX file into the new anim source (for
        timeEditorAnimSource command) or new container (for timeEditorClip command).
    
    - importFbxTakes : ft            (unicode)       [create]
        Import multiple FBX takes (separated by semicolons) into the new anim sources
        (for timeEditorAnimSource command) or new containers (for timeEditorClip
        command).
    
    - importMayaFile : mf            (unicode)       [create]
        Import an animation from Maya file into the new anim sources (for
        timeEditorAnimSource command) or new containers (for timeEditorClip command).
    
    - importOption : io              (unicode)       [edit]
        Option for importing animation source. Specify either 'connect' or 'generate'.
        connect:  Only connect with nodes already existing in the scene.
        Importing an animation source that does not match with any element
        of the current scene will not create any clip.                   (connect is the
        default mode). generate: Import everything and generate new nodes for items not
        existing in the scene.
    
    - importPopulateOption : ipo     (unicode)       [edit]
        Option for population when importing.
    
    - importedContainerNames : icn   (unicode)       [create]
        Internal use only. To be used along with populateImportedAnimSourcesto specify
        names for the created containers.
    
    - includeRoot : irt              (bool)          [create,edit]
        Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.
    
    - isUnique : iu                  (bool)          [query]
        Return true if the anim source node is only driving a single clip.
    
    - populateImportedAnimSources : pia (unicode)       [create]
        Internal use only. Populate the Time Editor with clips using the Animation
        Sources specified (use ; as a delimiter for multiple anim sources).
    
    - poseClip : poc                 (bool)          [create]
        Populate as pose clip with current attribute values.
    
    - recursively : rec              (bool)          [create,edit]
        Populate selection recursively, adding all the children.
    
    - removeSceneAnimation : rsa     (bool)          [create,edit]
        If true, remove animation from scene when creating clips or anim sources. Only
        Time Editor will drive the removed scene animation.
    
    - removeSource : rs              (unicode)       [edit]
        Remove single attribute.
    
    - showAnimSourceRemapping : sar  (bool)          [create]
        Show a remapping dialog when the imported anim source attributes do not match
        the scene attributes.
    
    - takeList : tl                  (unicode)       [create]
        Internal use only. To be used along with populateImportedAnimSourcesto specify
        the imported take names.
    
    - takesToImport : toi            (unicode)       [create]
        Internal use only. To be used along with populateImportedAnimSourcesto specify
        the imported take indices.
    
    - targetIndex : ti               (unicode)       [query]
        Get target index.
    
    - targets : trg                  (bool)          [query]
        Get a list of all targets in this anim source.
    
    - type : typ                     (unicode)       [create,query,edit]
        Only populate the specified type of animation source.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.timeEditorAnimSource`
    """
    pass


def _constraint(func): pass


def ikHandle(*args, **kwargs):
    """
    The handle command is used to create, edit, and query a handle within Maya.  The
    standard edit (-e) and query (-q) flags are used for edit and query functions.
    If there are 2 joints selected and neither -startJoint nor -endEffector flags
    are not specified, then the handle will be created from the selected joints. If
    a single joint is selected and neither -startJoint nor -endEffector flags are
    specified, then the handle will be created with the selected joint as the end-
    effector and the start joint will be the top of the joint chain containing the
    end effector. The default values of the flags are: -name ikHandle#-priority
    1-weight 1.0-positionWeight 1.0-solver ikRPsolver-forceSolver on-
    snapHandleFlagToggle on-sticky off-createCurve true-simplifyCurve true-
    rootOnCurve true-twistType linear-createRootAxis false-parentCurve true-
    snapCurve false-numSpans 1-rootTwistMode false.These attributes can be specified
    in creation mode, edited in edit mode (-e) or queried in query mode (-q).
    
    Flags:
    - autoPriority : ap              (bool)          [edit]
        Specifies that this handle's priority is assigned automatically.  The assigned
        priority will be based on the hierarchy distance from the root of the skeletal
        chain to the start joint of the handle.
    
    - connectEffector : ce           (bool)          [create,edit]
        This option is set to true as default, meaning that end-effector translate is
        connected with the endJoint translate.
    
    - createCurve : ccv              (bool)          [create]
        Specifies if a curve should automatically be created for the ikSplineHandle.
    
    - createRootAxis : cra           (bool)          [create]
        Specifies if a root transform should automatically be created above the joints
        affected by the ikSplineHandle. This option is used to prevent the root flipping
        singularity on a motion path.
    
    - curve : c                      (PyNode)        [create,query,edit]
        Specifies the curve to be used by the ikSplineHandle. Joints will be moved to
        align with this curve. This flag is mandatory if you use the -freezeJoints
        option.
    
    - disableHandles : dh            (bool)          [edit]
        set given handles to full fk (ikBlend attribute = 0.0)
    
    - enableHandles : eh             (bool)          [edit]
        set given handles to full ik (ikBlend attribute = 1.0)
    
    - endEffector : ee               (unicode)       [create,query,edit]
        Specifies the end-effector of the handle's joint chain. The end effector may be
        specified with a joint or an end-effector.  If a joint is specified, an end-
        effector will be created at the same position as the joint and this new end-
        effector will be used as the end-effector.
    
    - exists : ex                    (unicode)       [edit]
        Indicates if the specified handle exists or not.
    
    - forceSolver : fs               (bool)          [create,query,edit]
        Forces the solver to be used everytime. It could also be known as animSticky.
        So, after you set the first key the handle is sticky.
    
    - freezeJoints : fj              (bool)          [create,edit]
        Forces the curve, specfied by -curve option, to align itself along the existing
        joint chain. When false, or unspecified, the joints will be moved to positions
        along the specified curve.
    
    - jointList : jl                 (bool)          [query]
        Returns the list of joints that the handle is manipulating.
    
    - name : n                       (unicode)       [create,query,edit]
        Specifies the name of the handle.
    
    - numSpans : ns                  (int)           [create]
        Specifies the number of spans in the automatically generated curve of the
        ikSplineHandle.
    
    - parentCurve : pcv              (bool)          [create]
        Specifies if the curve should automatically be parented to the parent of the
        first joint affected by the ikSplineHandle.
    
    - positionWeight : pw            (float)         [create,query,edit]
        Specifies the position/orientation weight of a handle. This is used to compute
        the distancebetween the goal position and the end-effector position.  A
        positionWeight of 1.0 computes the distance as the distance between positions
        only and ignores the orientations.  A positionWeight of 0.0 computes the
        distance as the distance between the orientations only and ignores the
        positions.  A positionWeight of 0.5 attempts to weight the distances equally but
        cannot actually compute this due to unit differences. Because there is no way to
        add linear units and angular units.
    
    - priority : p                   (int)           [create,query,edit]
        Sets the priority of the handle.  Logically, all handles with a lower number
        priority are solved before any handles with a higher numbered priority.  (All
        handles of priority 1 are solved before any handles of priority 2 and so on.)
        Handle priorities must be ] 0.
    
    - rootOnCurve : roc              (bool)          [create,query,edit]
        Specifies if the root is locked onto the curve of the ikSplineHandle.
    
    - rootTwistMode : rtm            (bool)          [create,query,edit]
        Specifies whether the start joint is allowed to twist or not. If not, then the
        required twist is distributed over the remaining joints. This applies to all the
        twist types.
    
    - setupForRPsolver : srp         (bool)          [edit]
        If the flag is set and ikSolver is ikRPsolver, call RPRotateSetup for the new
        ikHandle. It is for ikRPsolver only.
    
    - simplifyCurve : scv            (bool)          [create]
        Specifies if the ikSplineHandle curve should be simplified.
    
    - snapCurve : snc                (bool)          [create]
        Specifies if the curve should automatically snap to the first joint affected by
        the ikSplineHandle.
    
    - snapHandleFlagToggle : shf     (bool)          [create,query,edit]
        Specifies that the handle position should be snapped to the end-effector
        position if the end-effector is moved by the user.  Setting this flag on allows
        you to use forward kinematics to pose or adjust your skeleton and then to
        animate it with inverse kinematics.
    
    - snapHandleToEffector : see     (bool)          [edit]
        All handles are immediately moved so that the handle position and orientation
        matches the end-effector position and orientation.
    
    - solver : sol                   (unicode)       [create,query,edit]
        Specifies the solver.  The complete list of available solvers may not be known
        until run-time because some of the solvers may be implemented as plug-ins.
        Currently the only valid solver are ikRPsolver, ikSCsolver and ikSplineSolver.
    
    - startJoint : sj                (unicode)       [create,query,edit]
        Specifies the start joint of the handle's joint chain.
    
    - sticky : s                     (unicode)       [create,query,edit]
        Specifies that this handle is sticky. Valid values are off, sticky, superSticky.
        Sticky handles are solved when the skeleton is being manipulated interactively.
        If a character has sticky feet, the solver will attempt to keep them in the same
        position as the user moves the character's root.  If they were not sticky, they
        would move along with the root.
    
    - twistType : tws                (unicode)       [create,query,edit]
        Specifies the type of interpolation to be used by the ikSplineHandle.  The
        interpolation options are linear, easeIn, easeOut, and easeInOut.
    
    - weight : w                     (float)         [create,query,edit]
        Specifies the handles weight in error calculations.  The weight only applies
        when handle goals are in conflict and cannot be solved simultaneously.  When
        this happens, a solution is computed that weights the distancefrom each goal to
        the solution by the handle's weight and attempts to minimize this value.  The
        weight must be ]= 0.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.ikHandle`
    """
    pass


def shot(*args, **kwargs):
    """
    Use this command to create a shot node or manipulate that node.
    
    Flags:
    - audio : aud                    (unicode)       [create,query,edit]
        Specify the audio clip for this shot. Audio can be linked to a shot to allow
        playback of specific sounds when that shot is being displayed in the Sequencer.
        Refer to the shot node's documentation for details on how audio is used by shots
        and the Sequencer.
    
    - clip : cl                      (unicode)       [create,query,edit]
        The clip associated with this shot. This clip will be posted to the
        currentCamera's imagePlane. Refer to the shot node's documentation for details
        on how cameras are used by shots and the Sequencer.
    
    - clipDuration : cd              (time)          [create,query,edit]
        Length of clip. This is used for the display of the clip indicator bar in the
        Sequencer.
    
    - clipOpacity : co               (float)         [create,query,edit]
        Opacity for the shot's clip, this value is assigned to the currentCamera's
        imagePlane. Refer to the shot node's documentation for details on how cameras
        are used by shots and the Sequencer.
    
    - clipSyncState : css            (bool)          [create,query,edit]
        The viewport synchronization status of the clip associated with this shot.
        Return values are, 0 = no clip associated with this shot 1 = clip is fully in
        sync with viewport, and frames are 1:1 with sequencer 2 = clip is partially in
        sync with viewport, movie may be scaled to match sequencer 3 = clip not in sync
        with viewport (i.e. could have scale/time/camera differences)
    
    - clipZeroOffset : czo           (time)          [create,query,edit]
        Specify which time of the clip corresponds to the beginning of the shot. This is
        used to properly align splitted clips.
    
    - copy : c                       (bool)          [create,query,edit]
        This flag is used to copy a shot to the clipboard. In query mode, this flag
        allows you to query what, if anything, has been copied into the shot clipboard.
    
    - createCustomAnim : cca         (bool)          [edit]
        Creates an animation layer and links the shot node's customAnim attr to the
        weight attr of the animation layer
    
    - currentCamera : cc             (unicode)       [create,query,edit]
        The camera associated with this shot. Refer to the shot node's documentation for
        details on how cameras are used by shots and the Sequencer.
    
    - customAnim : ca                (bool)          [query]
        Returns the name of the animation layer node linked to this shot node's
        customAnim attr
    
    - deleteCustomAnim : dca         (bool)          [edit]
        Disconnects the animation layer from this shot's customAnim attr and deletes the
        animation layer node
    
    - determineTrack : dt            (bool)          [query,edit]
        Determines an available track for the shot. Returns a new track number or the
        existing track number if the current track is available.
    
    - endTime : et                   (time)          [create,query,edit]
        The shot end time in the Maya timeline. Changing the startTime will extend the
        duration of a shot.
    
    - favorite : fav                 (bool)          [create,query,edit]
        Make the shot a favorite. This is a UI indicator only to streamline navigation
        in the Sequencer panel
    
    - flag1 : f1                     (bool)          [create,query,edit]
        User specified state flag 1/12 for this shot
    
    - flag10 : f10                   (bool)          [create,query,edit]
        User specified state flag 10/12 for this shot
    
    - flag11 : f11                   (bool)          [create,query,edit]
        User specified state flag 11/12 for this shot
    
    - flag12 : f12                   (bool)          [create,query,edit]
        User specified state flag 12/12 for this shot
    
    - flag2 : f2                     (bool)          [create,query,edit]
        User specified state flag 2/12 for this shot
    
    - flag3 : f3                     (bool)          [create,query,edit]
        User specified state flag 3/12 for this shot
    
    - flag4 : f4                     (bool)          [create,query,edit]
        User specified state flag 4/12 for this shot
    
    - flag5 : f5                     (bool)          [create,query,edit]
        User specified state flag 5/12 for this shot
    
    - flag6 : f6                     (bool)          [create,query,edit]
        User specified state flag 6/12 for this shot
    
    - flag7 : f7                     (bool)          [create,query,edit]
        User specified state flag 7/12 for this shot
    
    - flag8 : f8                     (bool)          [create,query,edit]
        User specified state flag 8/12 for this shot
    
    - flag9 : f9                     (bool)          [create,query,edit]
        User specified state flag 9/12 for this shot
    
    - hasCameraSet : hcs             (bool)          [create,query,edit]
        Returns true if the camera associated with this shot is a camera set.
    
    - hasStereoCamera : hsc          (bool)          [create,query,edit]
        Returns true if the camera associated with this shot is a stereo camera.
    
    - imagePlaneVisibility : ipv     (bool)          [create,query,edit]
        Visibility of the shot imageplane, this value is assigned to the currentCamera's
        imagePlane.
    
    - linkAudio : la                 (unicode)       [create,query,edit]
        Specify an audio clip to link to this shot. Any currently linked audio will be
        unlinked.
    
    - lock : lck                     (bool)          [create,query,edit]
        Lock a specific shot. This is different than locking an entire track, which is
        done via the shotTrack command
    
    - mute : m                       (bool)          [create,query,edit]
        Mute a specific shot. This is different than muting an entire track, which is
        done via the shotTrack command. Querying this attribute will return true if the
        shot is muted due to its own mute, its shot being muted, or its shot being
        unsoloed. See flag selfmuteto query only the shot's own state.
    
    - paste : p                      (bool)          [create,query,edit]
        This flag is used to paste a shot or shots from the clipboard to the sequence
        timeline. Shots are added to the clipboard using the c/copy flag.
    
    - pasteInstance : pi             (bool)          [create,query,edit]
        This flag is used to paste an instance of a shot or shots from the clipboard to
        the sequence timeline. Unlike the p/paste flag, which duplicates the camera and
        image plane from the original source shot, the pi/pasteInstance flag shares the
        camera and image plane from the source shot. The audio node is duplicated.
    
    - postHoldTime : pst             (time)          [create,query,edit]
        Specify the time length to append to the shot in the sequence timeline. This
        repeats the last frame of the shot, in sequence time, over the specified
        duration.
    
    - preHoldTime : prt              (time)          [create,query,edit]
        Specify the time length to prepend to the shot in the sequence timeline. This
        repeats the first frame of the shot, in sequence time, over the specified
        duration.
    
    - scale : s                      (float)         [create,query,edit]
        Specify an amount to scale the Maya frame range of the shot. This will affect
        the sequenceEndFrame, leaving the sequenceStartFrame unchanged.
    
    - selfmute : sm                  (bool)          [create,query,edit]
        Query if this individual shot's own mute state is set. This is different from
        the flag mute, which will return true if this shot is muted due to the track
        being muted or another track being soloed. Editing this flag will set this
        shot's own mute status (identical behavior as the flag mute).
    
    - sequenceDuration : sqd         (time)          [query,edit]
        Return the sequence duration of the shot, which will include the holds and
        scale. This flag can only be queried.
    
    - sequenceEndTime : set          (time)          [create,query,edit]
        The shot end in the sequence timeline. Changing the endTime of a shot will scale
        it in sequence time.
    
    - sequenceStartTime : sst        (time)          [create,query,edit]
        The shot start in the sequence timeline. Changing the startTime of a shot will
        shift it in sequence time.
    
    - shotName : sn                  (unicode)       [create,query,edit]
        Specify a user-defined name for this shot. This allows the assignment of names
        that are not valid as node names within Maya. Whenever the shotName attribute is
        defined its value is used in the UI.
    
    - sourceDuration : sd            (time)          [query,edit]
        Return the number of source frames in the shot. This flag can only be queried.
    
    - startTime : st                 (time)          [create,query,edit]
        The shot start time in the Maya timeline. Changing the startTime will extend the
        duration of a shot.
    
    - track : trk                    (int)           [query,edit]
        Specify the track in which this shot resides.
    
    - transitionInLength : til       (time)          [create,query,edit]
        Length of the transtion into the shot.
    
    - transitionInType : tit         (int)           [query,edit]
        Specify the the type of transition for the transition into the shot. 0 = Fade 1
        = Dissolve
    
    - transitionOutLength : tol      (time)          [create,query,edit]
        Length of the transtion out of the shot.
    
    - transitionOutType : tot        (int)           [query,edit]
        Specify the the type of transition for the transition out of the shot. 0 = Fade
        1 = Dissolve
    
    - unlinkAudio : ula              (bool)          [query,edit]
        COMMENT Unlinks any currently linked audio.                                Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.shot`
    """
    pass


def _parentConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def poleVectorConstraint(*args, **kwargs):
    """
    Constrains the poleVector of an ikRPsolve handle to point at a target object or
    at the average position of a number of targets. An poleVectorConstraint takes as
    input one or more targetDAG transform nodes at which to aim pole vector for an
    IK handle using the rotate plane solver.  The pole vector is adjust such that
    the in weighted average of the world space position target objects lies is the
    rotate planeof the handle.
    
    Flags:
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.poleVectorConstraint`
    """
    pass


def normalConstraint(*args, **kwargs):
    """
    Constrain an object's orientation based on the normal of the target surface(s)
    at the closest point(s) to the object. A normalConstraint takes as input one or
    more surface shapes (the targets) and a DAG transform node (the object).  The
    normalConstraint orients the constrained object such that the aimVector (in the
    object's local coordinate system) aligns in world space to combined normal
    vector.  The upVector (again the the object's local coordinate system) is
    aligned in world space with the worldUpVector.  The combined normal vector is a
    weighted average of the normal vector for each target surface at the point
    closest to the constrained object.
    
    Flags:
    - aimVector : aim                (float, float, float) [create,query,edit]
        Set the aim vector.  This is the vector in local coordinates that points at the
        target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is
        used.
    
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - upVector : u                   (float, float, float) [create,query,edit]
        Set local up vector.  This is the vector in local coordinates that aligns with
        the world up vector.  If not given at creation time, the default value of (0.0,
        1.0, 0.0) is used.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag
    
    - worldUpObject : wuo            (PyNode)        [create,query,edit]
        Set the DAG object use for worldUpType objectand objectrotation. See worldUpType
        for greater detail. The default value is no up object, which is interpreted as
        world space.
    
    - worldUpType : wut              (unicode)       [create,query,edit]
        Set the type of the world up vector computation. The worldUpType can have one of
        5 values: scene, object, objectrotation, vector, or none. If the value is scene,
        the upVector is aligned with the up axis of the scene and worldUpVector and
        worldUpObject are ignored. If the value is object, the upVector is aimed as
        closely as possible to the origin of the space of the worldUpObject and the
        worldUpVector is ignored. If the value is objectrotationthen the worldUpVector
        is interpreted as being in the coordinate space of the worldUpObject,
        transformed into world space and the upVector is aligned as closely as possible
        to the result. If the value is vector, the upVector is aligned with
        worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if
        the value is noneno twist calculation is performed by the constraint, with the
        resulting upVectororientation based previous orientation of the constrained
        object, and the great circlerotation needed to align the aim vector with its
        constraint. The default worldUpType is vector.
    
    - worldUpVector : wu             (float, float, float) [create,query,edit]
        Set world up vector.  This is the vector in world coordinates that up vector
        should align with. See -wut/worldUpType (below)for greater detail. If not given
        at creation time, the default value of (0.0, 1.0, 0.0) is used.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.normalConstraint`
    """
    pass


def pointOnPolyConstraint(*args, **kwargs):
    """
    Constrain an object's position to the position of the target object or to the
    average position of a number of targets. A pointOnPolyConstraint takes as input
    one or more targetDAG transform nodes at which to position the single constraint
    objectDAG transform node.  The pointOnPolyConstraint positions the constrained
    object at the weighted average of the world space position target objects.
    
    Flags:
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - maintainOffset : mo            (bool)          [create]
        The offset necessary to preserve the constrained object's initial position will
        be calculated and used as the offset.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - offset : o                     (float, float, float) [create,query,edit]
        Sets or queries the value of the offset. Default is 0,0,0.
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - skip : sk                      (unicode)       [create,edit]
        Specify the axis to be skipped. Valid values are x, y, zand none. During
        creation, noneis the default. This flag is multi-use.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pointOnPolyConstraint`
    """
    pass


def blendShape(*args, **kwargs):
    """
    This command creates a blendShape deformer, which blends in specified amounts of
    each target shape to the initial base shape. Each base shape is deformed by its
    own set of target shapes. Every target shape has an index that associates it
    with one of the shape weight values.In the create mode the first item on the
    selection list is treated as the base and the remaining inputs as targets. If
    the first item on the list has multiple shapes grouped beneath it, the targets
    must have an identical shape hierarchy. Additional base shapes can be added in
    edit mode using the deformers -g flag.
    
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
    
    - automatic : at                 (bool)          [create,edit]
        The -automatic flag is used to specify deformer ordering in a way that choses
        between -frontOfChain and -before automatically. If the geometry being deformed
        is only affected by invertible deformers, the -frontOfChain mode is used,
        otherwise the -before mode is used.
    
    - before : bf                    (bool)          [create,edit]
        If the default behavior for insertion/appending into/onto the existing chain is
        not the desired behavior then this flag can be used to force the command to
        place the deformer node before the selected node in the chain even if a new
        geometry shape has to be created in order to do so. Works in create mode (and
        edit mode if the deformer has no geometry added yet).
    
    - copyDelta : cd                 (int, int, int) [edit]
        Set the base, source, and destination delta index values.
    
    - copyInBetweenDelta : cid       (int, int, int, int) [edit]
        Set the base, target, source, and destination delta index values.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - envelope : en                  (float)         [create,query,edit]
        Set the envelope value for the deformer, controlling how much of the total
        deformation gets applied. Default is 1.0.
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
    - export : ep                    (unicode)       [edit]
        Export the shapes to the named file path.
    
    - exportTarget : et              (int, int)      [edit]
        Specify the base and target index pairs for the export.
    
    - flipTarget : ft                (int, int)      [edit]
        Flip the list of base and target pairs.
    
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
    
    - inBetween : ib                 (bool)          [create,edit]
        Indicate that the specified target should serve as an inbetween. An inbetween
        target is one that serves as an intermediate target between the base shape and
        another target.
    
    - inBetweenIndex : ibi           (int)           [edit]
        Only used with the -rtd/-resetTargetDelta flag to remove delta values for points
        in the inbetween target geometry defined by this index.
    
    - inBetweenType : ibt            (unicode)       [create,edit]
        Specify if the in-between target to be created is relative to the hero target or
        if it is absolute. If it is relative to hero targets, the in-between target will
        get any changes made to the hero target. Valid values are relativeand absolute.
        This flag should always be used with the -ib/-inBetween and -t/-target flags.
    
    - includeHiddenSelections : ihs  (bool)          [create]
        Apply the deformer to any visible and hidden objects in the selection list.
        Default is false.
    
    - ip : ip                        (unicode)       [edit]
        Import the shapes from the named file path.
    
    - mergeSource : mgs              (int)           [edit]
        List of source indexes for a merge.
    
    - mergeTarget : mgt              (int)           [edit]
        Target index of a merge
    
    - mirrorDirection : md           (int)           [edit]
        Mirror direction; 0 = negative, 1 = positive
    
    - mirrorTarget : mt              (int, int)      [edit]
        Mirror the list of base and target pairs.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - normalizationGroups : ng       (bool)          [query]
        Returns a list of the used normalization group IDs.
    
    - origin : o                     (unicode)       [create]
        blendShape will be performed with respect to the world by default. Valid values
        are worldand local. The local flag will cause the blend shape to be performed
        with respect to the shape's local origin.
    
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
    
    - resetTargetDelta : rtd         (int, int)      [edit]
        Remove all delta values for points in the target geometry, including all
        sequential targets defined by target index. Parameter list: uint: the base
        object indexuint: the target index
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - suppressDialog : sd            (bool)          [create,edit]
        Suppress dialog box and run the command as defined by the user.
    
    - symmetryAxis : sa              (unicode)       [query,edit]
        Axis for symmetry. Valid values are X, Y, and Z.
    
    - symmetryEdge : se              (unicode)       [query,edit]
        One or two symmetry edge names, separated by a .. See the blendShape node's
        symmetryEdge attribute for legal values.
    
    - symmetrySpace : ss             (int)           [query,edit]
        Space for symmetry. 0 = Topological, 1 = Object, 2 = UV
    
    - tangentSpace : ts              (bool)          [create,edit]
        Indicate that the delta of the specified target should be relative to the
        tangent space of the surface.
    
    - target : t                     (unicode, int, unicode, float) [create,query,edit]
        Set target object as the index target shape for the base shape base object. The
        full influence of target shape takes effect when its shape weight is
        targetValue. Parameter list: string: the base objectint: indexstring: the target
        objectdouble: target value
    
    - topologyCheck : tc             (bool)          [create]
        Set the state of checking for a topology match between the shapes being blended.
        Default is on.
    
    - transform : tr                 (unicode)       [query,edit]
        Set transform for target, then the deltas will become relative to a post
        transform. Typically the best workflow for this option is to choose a joint that
        is related to the fix you have introduced. This flag should be used only if the
        Deformation orderof blendShape node is Before.
    
    - weight : w                     (int, float)    [create,query,edit]
        Set the weight value (second parameter) at index (first parameter).
    
    - weightCount : wc               (int)           [create,query,edit]
        Set the number of shape weight values.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.blendShape`
    """
    pass


def timeWarp(*args, **kwargs):
    """
    This command is used to create a time warp input to a set of animation curves.
    
    Flags:
    - deleteFrame : df               (int)           [edit]
        The flag value indicates the 0-based index of the warp frame to delete. This
        flag can only be used in edit mode.
    
    - frame : f                      (float)         [create,query,edit]
        In create and edit mode, this flag can be used to specify warp frames added to
        the warp operation. In query mode, this flag returns a list of the frame values
        where warping occurs. The moveFrame flag command can be used to query the
        associated warped values.
    
    - g : g                          (bool)          [create,query,edit]
        In create mode, creates a global time warp node which impacts every animated
        object in the scene. In query mode, returns the global time warp node. Note:
        only one global time warp can exist in the scene.
    
    - interpType : it                (int, unicode)  [create,query,edit]
        This flag can be used to set the interpolation type for a given span. Valid
        interpolation types are linear, easeIn and easeOut. When queried, it returns a
        string array of the interpolation types for the specified time warp.
    
    - moveFrame : mf                 (int, float)    [query,edit]
        This flag can be used to move a singular warp frame. The first value specified
        indicates the 0-based index of the warp frame to move. The second value
        indicates the new warp frame value. This flag can only be used in edit and query
        mode. When queried, it returns an array of the warped frame values.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.timeWarp`
    """
    pass


def copyKey(*args, **kwargs):
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
    list or range (see Examples). This command copies curve segments's hierarchies
    from specified targets and puts them in the clipboard.  Source curves are
    unchanged.  The pasteKey command applies these curves to other objects.The shape
    of the copied curve placed in the clipboard depends on the copyKey
    -optionspecified.  Each of these options below will be explained using an
    example.  For all the explanations, let us assume that the source animation
    curve (from which keys will be copied) has 5 keyframes at times 10, 15, 20, 25,
    and 30. copyKey -t 12:22-option keysA 5-frame animation curve with one key at 15
    and another key at 20 is placed into the keyset clipboard.copyKey -t
    12:22-option curveA 10-frame animation is placed into the clipboard. The curve
    contains the original source-curve keys at times 15 and 20, as well as new keys
    inserted at times 12 and 22 to preserve the shape of the curve at the given time
    segment.TbaseKeySetCmd.h
    
    Flags:
    - animLayer : al                 (unicode)       [create]
        Specifies that the keys getting copied should come from this specified animation
        layer. If no keys on the object exist on this layer, then no keys are copied.
    
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - clipboard : cb                 (unicode)       [create]
        Specifies the clipboard to which animation is copied. Valid clipboards are
        apiand anim.  The default clipboard is: anim
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - forceIndependentEulerAngles : fea (bool)          [create]
        Specifies that the rotation curves should always be placed on the clipboard as
        independent Euler Angles. The default value is false.
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
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
    
    - option : o                     (unicode)       [create]
        The option to use when performing the copyKey operation. Valid options are
        keys,and curve.The default copy option is: keys
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.copyKey`
    """
    pass


def keyframeOutliner(*args, **kwargs):
    """
    This command creates/edits/queries a keyframe outliner control.
    
    Flags:
    - animCurve : ac                 (unicode)       [edit]
        Name of the animation curve for which to display keyframes.
    
    - annotation : ann               (unicode)       [create,query,edit]
        Annotate the control with an extra string value.
    
    - backgroundColor : bgc          (float, float, float) [create,query,edit]
        The background color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0. When
        setting backgroundColor, the background is automatically enabled, unless
        enableBackground is also specified with a false value.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - display : dsp                  (unicode)       [query,edit]
        narrow | wide What columns to display.  When narrow, time and value will be
        displayed, when widetangent information will be displayed as well
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Add a documentation flag to the control.  The documentation flag has a directory
        structure. (e.g., -dt render/multiLister/createNode/material)
    
    - dragCallback : dgc             (script)        [create,edit]
        Adds a callback that is called when the middle mouse button is pressed.  The MEL
        version of the callback is of the form: global proc string[] callbackName(string
        $dragControl, int $x, int $y, int $mods) The proc returns a string array that is
        transferred to the drop site. By convention the first string in the array
        describes the user settable message type.  Controls that are application defined
        drag sources may ignore the callback. $mods allows testing for the key modifiers
        CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3
        == CTRL + SHIFT. In Python, it is similar, but there are two ways to specify the
        callback.  The recommended way is to pass a Python function object as the
        argument.  In that case, the Python callback should have the form: def
        callbackName( dragControl, x, y, modifiers ): The values of these arguments are
        the same as those for the MEL version above. The other way to specify the
        callback in Python is to specify a string to be executed.  In that case, the
        string will have the values substituted into it via the standard Python format
        operator.  The format values are passed in a dictionary with the keys
        dragControl, x, y, modifiers.  The dragControlvalue is a string and the other
        values are integers (eg the callback string could be print '%(dragControl)s
        %(x)d %(y)d %(modifiers)d'
    
    - dropCallback : dpc             (script)        [create,edit]
        Adds a callback that is called when a drag and drop operation is released above
        the drop site.  The MEL version of the callback is of the form: global proc
        callbackName(string $dragControl, string $dropControl, string $msgs[], int $x,
        int $y, int $type) The proc receives a string array that is transferred from the
        drag source. The first string in the msgs array describes the user defined
        message type. Controls that are application defined drop sites may ignore the
        callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link. In Python,
        it is similar, but there are two ways to specify the callback.  The recommended
        way is to pass a Python function object as the argument.  In that case, the
        Python callback should have the form: def pythonDropTest( dragControl,
        dropControl, messages, x, y, dragType ): The values of these arguments are the
        same as those for the MEL version above. The other way to specify the callback
        in Python is to specify a string to be executed.  In that case, the string will
        have the values substituted into it via the standard Python format operator.
        The format values are passed in a dictionary with the keys dragControl,
        dropControl, messages, x, y, type.  The dragControlvalue is a string and the
        other values are integers (eg the callback string could be print
        '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'
    
    - enable : en                    (bool)          [create,query,edit]
        The enable state of the control.  By default, this flag is set to true and the
        control is enabled.  Specify false and the control will appear dimmed or greyed-
        out indicating it is disabled.
    
    - enableBackground : ebg         (bool)          [create,query,edit]
        Enables the background color of the control.
    
    - enableKeyboardFocus : ekf      (bool)          [create,query,edit]
        If enabled, the user can navigate to the control with the tab key and select
        values with the keyboard. If not, the user can only use the mouse. This flag
        would typically be used to turn off keyboard focus support from controls that
        get it by default, like Edit and List controls
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - fullPathName : fpn             (bool)          [query]
        Return the full path name of the widget, which includes all the parents.
    
    - height : h                     (int)           [create,query,edit]
        The height of the control.  The control will attempt to be this size if it is
        not overruled by parent layout conditions.
    
    - highlightColor : hlc           (float, float, float) [create,query,edit]
        The highlight color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0.
    
    - isObscured : io                (bool)          [query]
        Return whether the control can actually be seen by the user. The control will be
        obscured if its state is invisible, if it is blocked (entirely or partially) by
        some other control, if it or a parent layout is unmanaged, or if the control's
        window is invisible or iconified.
    
    - manage : m                     (bool)          [create,query,edit]
        Manage state of the control.  An unmanaged control is not visible, nor does it
        take up any screen real estate.  All controls are created managed by default.
    
    - noBackground : nbg             (bool)          [create,edit]
        Clear/reset the control's background. Passing true means the background should
        not be drawn at all, false means the background should be drawn.  The state of
        this flag is inherited by children of this control.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - statusBarMessage : sbm         (unicode)       [create,edit]
        Extra string to display in the status bar when the mouse is over the control.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - visible : vis                  (bool)          [create,query,edit]
        The visible state of the control.  A control is created visible by default.
        Note that a control's actual appearance is also dependent on the visible state
        of its parent layout(s).
    
    - visibleChangeCommand : vcc     (script)        [create,query,edit]
        Command that gets executed when visible state of the control changes.
    
    - width : w                      (int)           [create,query,edit]
        The width of the control.  The control will attempt to be this size if it is not
        overruled by parent layout conditions.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeOutliner`
    """
    pass


def pointConstraint(*args, **kwargs):
    """
    Constrain an object's position to the position of the target object or to the
    average position of a number of targets. A pointConstraint takes as input one or
    more targetDAG transform nodes at which to position the single constraint
    objectDAG transform node.  The pointConstraint positions the constrained object
    at the weighted average of the world space position target objects.
    
    Flags:
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - maintainOffset : mo            (bool)          [create]
        The offset necessary to preserve the constrained object's initial position will
        be calculated and used as the offset.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - offset : o                     (float, float, float) [create,query,edit]
        Sets or queries the value of the offset. Default is 0,0,0.
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - skip : sk                      (unicode)       [create,edit]
        Specify the axis to be skipped. Valid values are x, y, zand none. During
        creation, noneis the default. This flag is multi-use.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pointConstraint`
    """
    pass


def ikSolver(*args, **kwargs):
    """
    The ikSolver command is used to set the attributes for an IK Solver or create a
    new one. The standard edit (-e) and query (-q) flags are used for edit and query
    functions.
    
    Flags:
    - epsilon : ep                   (float)         [create,query,edit]
        max error
    
    - maxIterations : mxi            (int)           [create,query,edit]
        Sets the max iterations for a solution
    
    - name : n                       (unicode)       [create,query,edit]
        Name of solver
    
    - solverType : st                (unicode)       [create,query,edit]
        valid solverType (only ikSystem knows what is valid) for creation of a new
        solver (required)                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.ikSolver`
    """
    pass


def _scaleConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def dropoffLocator(*args, **kwargs):
    """
    This command adds one or more dropoff locators to a wire curve, one for each
    selected curve point. The dropoff locators can be used to provide localized
    tuning of the wire deformation about the curve point. The arguments are two
    floats, the envelope and percentage, followed by the wire node name and then by
    the curve point(s).
    
    
    Derived from mel command `maya.cmds.dropoffLocator`
    """
    pass


def bakeResults(*args, **kwargs):
    """
    This command allows the user to replace a chain of dependency nodes which define
    the value for an attribute with a single animation curve. Command allows the
    user to specify the range and frequency of sampling. This command operates on a
    keyset. A keyset is defined as a group of keys within a specified time range on
    one or more animation curves. The animation curves comprising a keyset depend on
    the value of the -animationflag: keysOrObjects: Any active keys, when no target
    objects or -attribute flags appear on the command line, orAll animation curves
    connected to all keyframable attributes of objects specified as the command
    line's targetList, when there are no active keys.keys: Only act on active keys
    or tangents. If there are no active keys or tangents, do not do anything.
    objects: Only act on specified objects. If there are no objects specified, do
    not do anything. Note that the -animationflag can be used to override the curves
    uniquely identified by the multi-use -attributeflag, which takes an argument of
    the form attributeName, such as translateX. Keys on animation curves are
    identified by either their time values or their indices. Times and indices
    should be specified as a range, as shown below. -time 10:20means all keys in the
    range from 10 to 20, inclusive, in the current time unit.-index 1:5means the
    2nd, 3rd, 4th, 5th, and 6th keys of each animation curve.
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on. Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.See command description for
        details.
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - bakeOnOverrideLayer : bol      (bool)          [create]
        If true, all layered and baked attribute will be added as a top override layer.
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - destinationLayer : dl          (unicode)       [create]
        This flag can be used to specify an existing layer where the baked results
        should be stored. Use this flag with caution. If the destination layer already
        has animation on it that contributes to the final result, it will be replaced by
        the output of the bake. As a result, it is possible that the combined animation
        visible in the scene is different before / after the baking process.
    
    - disableImplicitControl : dic   (bool)          [create]
        Whether to disable implicit control after the anim curves are obtained as the
        result of this command. An implicit control to an attribute is some function
        that affects the attribute without using an explicit dependency graph
        connection. The control of IK, via ik handles, is an example.
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve. Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
    - includeUpperBound : iub        (bool)          [create]
        When the -t/time or -f/float flags represent a range of keys, this flag
        determines whether the keys at the upper bound of the range are included in the
        keyset. Default value: true. This flag is only valid when the argument to the
        -t/time flag is a time range with a lower and upper bound. Note: when used with
        the pasteKeycommand, this flag refers only to the time range of the target curve
        that is replaced, when using options such as replace,fitReplace,or
        scaleReplace.This flag has no effect on the curve pasted from the clipboard.
    
    - index : index                  (int)           [create]
        index of a key on an animCurve
    
    - minimizeRotation : mr          (bool)          [create]
        Specify whether to minimize the local Euler component from key to key during
        baking of rotation channels.
    
    - oversamplingRate : osr         (int)           [create]
        Amount of samples per sampleBy period. Default is 1.
    
    - preserveOutsideKeys : pok      (bool)          [create]
        Whether to preserve keys that are outside the bake range when there are directly
        connected animation curves or a pairBlend node which has an animation curve as
        its direct input. The default (false) is to remove frames outside the bake
        range. If the channel that you are baking is not controlled by a single
        animation curve, then a new animation curve will be created with keys only in
        the bake range. In the case of pairBlend-driven channels, setting pok to true
        will retain both the pairBlend and its input animCurve. The blended values will
        be baked onto the animCurve and the weight of the pairBlend weight will be keyed
        to the animCurve during the baked range.
    
    - removeBakedAnimFromLayer : rba (bool)          [create]
        If true, all baked animation will be removed from the layer. Otherwise all layer
        associated with the baked animation will be muted.
    
    - removeBakedAttributeFromLayer : ral (bool)          [create]
        If true, all baked attribute will be removed from the layer. Otherwise all layer
        associated with the baked attribute will be muted.
    
    - resolveWithoutLayer : rwl      (unicode)       [create]
        This flag can be used to specify a list of layers to be merged together during
        the bake process. This is a multi-use flag. Its name refers to the fact that
        when solving for the value to key, it determines the proper value to key on the
        destination layer to achieve the same result as the merged layers.
    
    - sampleBy : sb                  (time)          [create]
        Amount to sample by. Default is 1.0 in current timeUnit.
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - simulation : sm                (bool)          [create]
        Using this flag instructs the command to preform a simulation instead of just
        evaluating each attribute separately over the range of time. The simulation flag
        is required to bake animation that that depends on the whole scene being
        evaluated at each time step such as dynamics. The default is false.
    
    - smart : sr                     (bool, float)   [create]
        Specify whether to enable smart bake and the optional smart bake tolerance.
    
    - sparseAnimCurveBake : sac      (bool)          [create]
        When this is true and anim curves are being baked, do not insert any keys into
        areas of the curve where animation is defined. And, use as few keys as possible
        to bake the pre and post infinity behavior. When this is false, one key will be
        inserted at each time step. The default is false.
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.bakeResults`
    """
    pass


def timeEditorPanel(*args, **kwargs):
    """
    Time Editor - non-linear animation editor
    
    Flags:
    - activeClipEditMode : ace       (int)           [query,edit]
        Set the appropriate clip edit mode for the editor. 0: Default Mode1: Trim Mode2:
        Scale Mode3: Loop Mode4: Hold Mode
    
    - activeTabRootClipId : atr      (bool)          [query]
        Get the clip id for which current active tab has been opened. In case of main
        tab, this will return -1 meaning there is no root clip.
    
    - activeTabTime : att            (bool)          [query]
        Get current time displayed inside the active tab. This will be global time in
        case of the main tab and local time for others.
    
    - activeTabView : atv            (int)           [query,edit]
        Get/set the index of the tab widget's (active) visible tab. Note: the index is
        zero-based.
    
    - autoFit : af                   (unicode)       [query,edit]
        on | off | tgl Auto fit-to-view.
    
    - autoFitTime : aft              (unicode)       [query,edit]
        on | off | tgl Auto fit-to-view along the time axis, as well.
    
    - contextMenu : cm               (bool)          []
    
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - displayActiveKeyTangents : dat (unicode)       [edit]
        on | off | tgl Display active key tangents in the editor.
    
    - displayActiveKeys : dak        (unicode)       [edit]
        on | off | tgl Display active keys in the editor.
    
    - displayInfinities : di         (unicode)       [edit]
        on | off | tgl Display infinities in the editor.
    
    - displayKeys : dk               (unicode)       [edit]
        on | off | tgl Display keyframes in the editor.
    
    - displayTangents : dtn          (unicode)       [edit]
        on | off | tgl Display tangents in the editor.
    
    - displayValues : dv             (unicode)       [edit]
        on | off | tgl Display active keys and tangents values in the editor.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - filter : f                     (unicode)       [create,query,edit]
        Specifies the name of an itemFilter object to be used with this editor. This
        filters the information coming onto the main list of the editor.
    
    - focusTrack : ft                (unicode)       []
    
    - forceMainConnection : fmc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object. This is a variant of the -mainListConnection flag in
        that it will force a change even when the connection is locked. This flag is
        used to reduce the overhead when using the -unlockMainConnection ,
        -mainListConnection, -lockMainConnection flags in immediate succession.
    
    - groupIdForTabView : gtv        (int)           [query]
        Get the group clip id for the given tab view index. To specify the tab index,
        this flag must appear before the -query flag.
    
    - highlightConnection : hlc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its highlight list. Not all editors have a highlight list. For
        those that do, it is a secondary selection list.
    
    - keyingTarget : kt              (int)           [query,edit]
        Set keying target to specified clip ID. If keying into layer, '-layer' flag must
        be used. In query mode, the clip id is omitted, and the name of the keying
        target will be returned.
    
    - layerId : l                    (int)           [edit]
        Indicate layer ID of keying target.
    
    - lockMainConnection : lck       (bool)          [create,edit]
        Locks the current list of objects within the mainConnection, so that only those
        objects are displayed within the editor. Further changes to the original
        mainConnection are ignored.
    
    - lookAt : la                    (unicode)       [edit]
        all | selected | currentTime FitView helpers.
    
    - mainListConnection : mlc       (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object.
    
    - menu : m                       (script)        [create]
        Specify a script to be run when the editor is created.  The function will be
        passed one string argument which is the new editor's name.
    
    - minClipWidth : mcw             (int)           [query,edit]
        Set the minimum clip width.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - selectionConnection : slc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its own selection list. As the user selects things in this
        editor, they will be selected in the selectionConnection object. If the object
        undergoes changes, the editor updates to show the changes.
    
    - setToPrevClipEditMode : spe    (bool)          [edit]
        Revert to previous clip edit mode.
    
    - snapTime : st                  (unicode)       [query,edit]
        none | integer | keyframe Keyframe move snap in time.
    
    - snapToClip : stc               (bool)          [query,edit]
        Enable/Disable snap-to-clip option in Time Editor while manipulating and drag-
        and-drop clips. When snapToClip is on all manipulated timing will land on a clip
        boundary if it is close to it.
    
    - snapToFrame : stf              (bool)          [query,edit]
        Enable/Disable snap-to-frame option in Time Editor while manipulating and drag-
        and-drop clips. When snapToFrame is on all manipulated timing will land on an
        exact frame.
    
    - snapTolerance : sto            (int)           [query,edit]
        Set the tolerance value for snapping.
    
    - snapValue : sv                 (unicode)       [query,edit]
        none | integer | keyframe Keyframe move snap in values.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - tabView : tv                   (int)           [edit]
        Create a tab view for the given group clip ID.
    
    - timeCursor : tc                (bool)          [query,edit]
        Activate the time cursor in Time Editor for scrubbing.
    
    - togglekeyview : tkv            (bool)          []
    
    - unParent : up                  (bool)          [create,edit]
        Specifies that the editor should be removed from its layout. This cannot be used
        in query mode.
    
    - unlockMainConnection : ulk     (bool)          [create,edit]
        Unlocks the mainConnection, effectively restoring the original mainConnection
        (if it is still available), and dynamic updates.
    
    - updateMainConnection : upd     (bool)          [create,edit]
        Causes a locked mainConnection to be updated from the orginal mainConnection,
        but preserves the lock state.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - viewLeft : vl                  (bool)          []
    
    - viewRight : vr                 (bool)          []
    
    
    Derived from mel command `maya.cmds.timeEditorPanel`
    """
    pass


def flexor(*args, **kwargs):
    """
    This command creates a flexor. A flexor a deformer plus a set of driving
    attributes. For example, a flexor might be a sculpt object that is driven by a
    joint's x rotation and a cube's y position.
    
    Flags:
    - atBones : ab                   (bool)          [create]
        Add a flexor at bones. Flexor will be added at each of the selected bones, or at
        all bones in the selected skeleton if the -ts flag is also specified.
    
    - atJoints : aj                  (bool)          [create]
        Add a flexor at joints. Flexor will be added at each of the selected joints, or
        at all joints in the selected skeleton if the -ts flag is specified.
    
    - deformerCommand : dc           (unicode)       [create]
        String representing underlying deformer command string.
    
    - list : l                       (bool)          [query]
        List all possible types of flexors. Query mode only.
    
    - name : n                       (unicode)       [create]
        This flag is obsolete.
    
    - noScale : ns                   (bool)          [create]
        Do not auto-scale the flexor to the size of the nearby geometry.
    
    - toSkeleton : ts                (bool)          [create]
        Specifies that flexors will be added to the entire skeleton rather than just to
        the selected joints/bones. This flag is used in conjunction with the -ab and -aj
        flags.
    
    - type : typ                     (unicode)       [create]
        Specifies which type of flexor. To see list of valid types, use the flexor
        -query -listcommand.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.flexor`
    """
    pass


def _geometryConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def tension(*args, **kwargs):
    """
    This command is used to create, edit and query tension nodes.
    
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
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - envelope : en                  (float)         [create,query,edit]
        Envelope of the tension node. The envelope determines the percent of
        deformation. Value is clamped to [0, 1] range. Default is 1.
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - inwardConstraint : iwc         (float)         [create,query,edit]
        Constrains the movement of the vertex to not move inward from the input
        deforming shape to preserve the contour. Value is in the [0,1] range. Default is
        0.0.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - outwardConstraint : owc        (float)         [create,query,edit]
        Constrains the movement of the vertex to not move outward from the input
        deforming shape to preserve the contour. Value is in the [0,1] range.
    
    - parallel : par                 (bool)          [create,edit]
        Inserts the new deformer in a parallel chain to any existing deformers in the
        history of the object. A blendShape is inserted to blend the parallel results
        together. Works in create mode (and edit mode if the deformer has no geometry
        added yet).
    
    - pinBorderVertices : pbv        (bool)          [create,query,edit]
        If enabled, vertices on mesh borders will be pinned to their current position
        during smoothing. Default is true.
    
    - prune : pr                     (bool)          [edit]
        Removes any points not being deformed by the deformer in its current
        configuration from the deformer set.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - smoothingIterations : si       (int)           [create,query,edit]
        Number of smoothing iterations performed by the tension node. Default is 10.
    
    - smoothingStep : ss             (float)         [create,query,edit]
        Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A
        higher value may lead to instabilities but converges faster compared to a lower
        value. Default is 0.5.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.tension`
    """
    pass


def character(*args, **kwargs):
    """
    This command is used to manage the membership of a character.  Characters are a
    type of set that gathers together the attributes of a node or nodes that a user
    wishes to animate as a single entity.
    
    Flags:
    - addElement : add               (PyNode)        [edit]
        Adds the list of items to the given character.  If some of the items cannot be
        added to the character because they are in another character, the command will
        fail.  When another character is passed to to -addElement, is is added as a sub
        character.  When a node is passed in, it is expanded into its keyable
        attributes, which are then added to the character.
    
    - addOffsetObject : aoo          (unicode)       [query,edit]
        Indicates that the selected character member objects should be used when
        calculating and applying offsets. The flag argument is used to specify the
        character.
    
    - characterPlug : cp             (bool)          [query]
        Returns the plug on the character that corresponds to the specified character
        member.
    
    - clear : cl                     (PyNode)        [edit]
        An operation which removes all items from the given character.
    
    - empty : em                     (bool)          [create]
        Indicates that the character to be created should be empty. (i.e. it ignores any
        arguments identifying objects to be added to the character.
    
    - excludeDynamic : ed            (bool)          [create]
        When creating the character, exclude dynamic attributes.
    
    - excludeRotate : er             (bool)          [create]
        When creating the character, exclude rotate attributes from transform-type
        nodes.
    
    - excludeScale : es              (bool)          [create]
        When creating the character, exclude scale attributes from transform-type nodes.
    
    - excludeTranslate : et          (bool)          [create]
        When creating the character, exclude translate attributes from transform-type
        nodes. For example, if your character contains joints only, perhaps you only
        want to include rotations in the character.
    
    - excludeVisibility : ev         (bool)          [create]
        When creating the character, exclude visibility attribute from transform-type
        nodes.
    
    - flatten : fl                   (PyNode)        [edit]
        An operation that flattens the structure of the given character. That is, any
        characters contained by the given character will be replaced by its members so
        that the character no longer contains other characters but contains the other
        characters' members.
    
    - forceElement : fe              (PyNode)        [edit]
        For use in edit mode only. Forces addition of the items to the character. If the
        items are in another character which is in the character partition, the items
        will be removed from the other character in order to keep the characters in the
        character partition mutually exclusive with respect to membership.
    
    - include : include              (PyNode)        [edit]
        Adds the list of items to the given character.  If some of the items cannot be
        added to the character, a warning will be issued. This is a less strict version
        of the -add/addElement operation.
    
    - intersection : int             (PyNode)        [query]
        An operation that returns a list of items which are members of all the character
        in the list.  In general, characters should be mutually exclusive.
    
    - isIntersecting : ii            (PyNode)        [query]
        An operation which tests whether or not the characters in the list have common
        members.  In general, characters should be mutually exclusive, so this should
        always return false.
    
    - isMember : im                  (PyNode)        [query]
        An operation which tests whether or not all the given items are members of the
        given character.
    
    - library : lib                  (bool)          [query]
        Returns the clip library associated with this character, if there is one. A clip
        library will only exist if you have created clips on your character.
    
    - memberIndex : mi               (int)           [query]
        Returns the memberIndex of the specified character member if used after the
        query flag. Or if used before the query flag, returns the member that
        corresponds to the specified index.
    
    - name : n                       (unicode)       [create]
        Assigns string as the name for a new character. Valid for operations that create
        a new character.
    
    - noWarnings : nw                (bool)          [create]
        Indicates that warning messages should not be reported such as when trying to
        add an invalid item to a character. (used by UI)
    
    - nodesOnly : no                 (bool)          [query]
        This flag modifies the results of character membership queries. When listing the
        attributes (e.g. sphere1.tx) contained in the character, list only the nodes.
        Each node will only be listed once, even if more than one attribute or component
        of the node exists in the character.
    
    - offsetNode : ofs               (bool)          [query]
        Returns the name of the characterOffset node used to add offsets to the root of
        the character.
    
    - remove : rm                    (PyNode)        [edit]
        Removes the list of items from the given character.
    
    - removeOffsetObject : roo       (unicode)       [edit]
        Indicates that the selected character offset objects should be removed as
        offsets. The flag argument is used to specify the character.
    
    - root : rt                      (unicode)       [create]
        Specifies the transform node which will act as the root of the character being
        created. This creates a characterOffset node in addition to the character node,
        which can be used to add offsets to the character to change the direction of the
        character's animtion without inserting additional nodes in its hierarchy.
    
    - scheduler : sc                 (bool)          [query]
        Returns the scheduler associated with this character, if there is one. A
        scheduler will only exist if you have created clips on your character.
    
    - split : sp                     (PyNode)        [create]
        Produces a new set with the list of items and removes each item in the list of
        items from the given set.
    
    - subtract : sub                 (PyNode)        [query]
        An operation between two characters which returns the members of the first
        character that are not in the second character. In general, characters should be
        mutually exclusive.
    
    - text : t                       (unicode)       [create,query,edit]
        Defines an annotation string to be stored with the character.
    
    - union : un                     (PyNode)        [query]
        An operation that returns a list of all the members of all characters listed.
    
    - userAlias : ua                 (PyNode)        [query]
        Returns the user defined alias for the given attribute on the character or and
        empty string if there is not one.  Characters automatically alias the attributes
        where character animation data is stored.  A user alias will exist when the
        automatic aliases are overridden using the aliasAttr command.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.character`
    """
    pass


def getCurrentTime():
    """
    get the current time as a float
    """
    pass


def skinCluster(*args, **kwargs):
    """
    The skinCluster command is used for smooth skinning in maya. It binds the
    selected geometry to the selected joints or skeleton by means of a skinCluster
    node.  Each point of the bound geometry can be affected by any number of joints.
    The extent to which each joint affects the motion of each point is regulated by
    a corresponding weight factor.  Weight factors can be modified using the
    skinPercent command.  The command returns the name of the new skinCluster.The
    skinCluster binds only a single geometry at a time. Thus, to bind multiple
    geometries, multiple skinCluster commands must be issued.Upon creation of a new
    skinCluster, the command can be used to add and remove transforms (not
    necessarily joints) that influence the motion of the bound skin points.  The
    skinCluster command can also be used to adjust parameters such as the dropoff,
    nurbs samples, polygon smoothness on a particular influence object. Note: Any
    custom weights on a skin point that the influence object affects will be lost
    after adjusting these parameters.
    
    Flags:
    - addInfluence : ai              (unicode)       [edit]
        The specified transform or joint will be added to the list of transforms that
        influence the bound geometry. The maximum number of influences will be observed
        and only the weights of the cv's that the specified transform effects will
        change. This flag is multi-use.
    
    - addToSelection : ats           (bool)          [edit]
        When used in conjunction with the selectInfluenceVerts flag, causes the vertices
        afftected by the influence to be added to the current selection, without first
        de-selecting other vertices.
    
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
    
    - baseShape : bsh                (unicode)       [edit]
        This flag can be used in conjunction with the -addInfluence flag to specify the
        shape that will be used as the base shape when an influence object with geometry
        is added to the skinCluster.  If the flag is not used then the command will make
        a copy of the influence object's shape and use that as a base shape.
    
    - before : bf                    (bool)          [create,edit]
        If the default behavior for insertion/appending into/onto the existing chain is
        not the desired behavior then this flag can be used to force the command to
        place the deformer node before the selected node in the chain even if a new
        geometry shape has to be created in order to do so. Works in create mode (and
        edit mode if the deformer has no geometry added yet).
    
    - bindMethod : bm                (int)           [create,query]
        This flag sets the binding method. 0 - Closest distance between a joint and a
        point of the geometry. 1 - Closest distance between a joint, considering the
        skeleton hierarchy, and a point of the geometry. 2 - Surface heat map diffusion.
        3 - Geodesic voxel binding.  geomBind command must be called after creating a
        skinCluster with this method.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - dropoffRate : dr               (float)         [create,query,edit]
        Sets the rate at which the influence of a transform drops as the distance from
        that transform increases. The valid range is between 0.1 and 10.0.  In Create
        mode it sets the dropoff rate for all the bound joints.  In Edit mode the flag
        is used together with the inf/influence flag to set the dropoff rate of a
        particular influence.  Note: When the flag is used in Edit mode, any custom
        weights on the skin points the given transform influences will be lost.
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
    - forceNormalizeWeights : fnw    (bool)          [edit]
        If the normalization mode is none or post, it is possible (indeed likely) for
        the weights in the skin cluster to no longer add up to 1.  This flag forces all
        weights to add back to 1 again.
    
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
    
    - heatmapFalloff : hmf           (float)         [create]
        This flag sets the heatmap binding falloff. If set to 0.0 (default) the
        deformation will be smoother due to many small weights spread over the mesh
        surface per influence. However, if set to 1.0, corresponding to maximum falloff,
        the number of influences per point will be reduced and points will tend to be
        greatly influenced by their closest joint decreasing the overall spread of small
        weights. This flag only works when using heatmap binding.
    
    - ignoreBindPose : ibp           (bool)          [create,edit]
        This flag is deprecated and no longer used.  It will be ignored if used.
    
    - ignoreHierarchy : ih           (bool)          [create,query]
        Deprecated. Use bindMethod flag instead. Disregard the place of the joints in
        the skeleton hierarchy when computing the closest joints that influence a point
        of the geometry.
    
    - ignoreSelected : ignoreSelected (bool)          [create]
        Tells the command to not deform objects on the current selection list
    
    - includeHiddenSelections : ihs  (bool)          [create]
        Apply the deformer to any visible and hidden objects in the selection list.
        Default is false.
    
    - influence : inf                (unicode)       [query,edit]
        This flag specifies the influence object that will be used for the current edit
        operation. In query mode, returns a string array of the influence objects
        (joints and transform).       In query mode, this flag can accept a value.
    
    - lockWeights : lw               (bool)          [query,edit]
        Lock the weights of the specified influence object to their current value or to
        the value specified by the -weight flag.
    
    - maximumInfluences : mi         (int)           [create,query,edit]
        Sets the maximum number of transforms that can influence a point (have non-zero
        weight for the point) when the skinCluster is first created or a new influence
        is added.  Note: When this flag is used in Edit mode any custom weights will be
        lost and new weights will be reassigned to the whole skin.
    
    - moveJointsMode : mjm           (bool)          [edit]
        If set to true, puts the skin into a mode where joints can be moved without
        modifying the skinning. If set to false, takes the skin out of move joints mode.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - normalizeWeights : nw          (int)           [create,query,edit]
        This flag sets the normalization mode. 0 - none, 1 - interactive, 2 - post
        (default) Interactive normalization makes sure the weights on the influences add
        up to 1.0, always. Everytime a weight is changed, the weights are automatically
        normalized.  This may make it difficult to perform weighting operations, as the
        normalization may interfere with the weights the user has set.  Post
        normalization leaves the weights the user has set as is, and only normalizes the
        weights at the moment it is needed (by dividing by the sum of the weights).
        This makes it easier for users to weight their skins.
    
    - nurbsSamples : ns              (int)           [create,edit]
        Sets the number of sample points that will be used along an influence curve or
        in each direction on an influence NURBS surface to influence the bound skin. The
        more the sample points the more closely the skin follows the influence NURBS
        curve/surface.
    
    - obeyMaxInfluences : omi        (bool)          [create,query,edit]
        When true, the skinCluster will continue to enforce the maximum influences each
        time the user modifies the weight, so that any given point is only weighted by
        the number of influences in the skinCluster's maximumInfluences attribute.
    
    - parallel : par                 (bool)          [create,edit]
        Inserts the new deformer in a parallel chain to any existing deformers in the
        history of the object. A blendShape is inserted to blend the parallel results
        together. Works in create mode (and edit mode if the deformer has no geometry
        added yet).
    
    - polySmoothness : ps            (float)         [create,edit]
        This flag controls how accurately the skin control points follow a given polygon
        influence object. The higher the value of polySmoothnmess the more rounded the
        deformation resulting from a polygonal influence object will be.
    
    - prune : pr                     (bool)          [edit]
        Removes any points not being deformed by the deformer in its current
        configuration from the deformer set.
    
    - recacheBindMatrices : rbm      (bool)          [edit]
        Forces the skinCluster node to recache its bind matrices.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - removeFromSelection : rfs      (bool)          [edit]
        When used in conjunction with the selectInfluenceVerts flag, causes the vertices
        afftected by the influence to be removed from the current selection.
    
    - removeInfluence : ri           (unicode)       [edit]
        Remove the specified transform or joint from the list of transforms that
        influence the bound geometry The weights for the affected points are
        renormalized. This flag is multi-use.
    
    - removeUnusedInfluence : rui    (bool)          [create]
        If this flag is set to true then transform or joint whose weights are all zero
        (they have no effect) will not be bound to the geometry.  Having this option set
        will help speed-up the playback of animation.
    
    - selectInfluenceVerts : siv     (unicode)       [edit]
        Given the name of a transform, this will select the verts or control points
        being influenced by this transform, so users may visualize which vertices are
        being influenced by the transform.
    
    - skinMethod : sm                (int)           [create,query,edit]
        This flag set the skinning method. 0 - classical linear skinning (default). 1 -
        dual quaternion (volume preserving), 2 - a weighted blend between the two.
    
    - smoothWeights : sw             (float)         [edit]
        This flag is used to detect sudden jumps in skin weight values, which often
        indicates bad weighting, and then smooth out those jaggies in skin weights. The
        argument is the error tolerance ranging from 0 to 1.  A value of 1 means that
        the algorithm will smooth a vertex only if there is a 100% change in weight
        values from its neighbors.  The recommended default to use is 0.5 (50% change in
        weight value from the neighbors).
    
    - smoothWeightsMaxIterations : swi (int)           [edit]
        This flag is valid only with the smooth weights flag.  It is possible that not
        all the vertices detected as needing smoothing can be smoothed in 1 iteration
        (because all of their neighbors also have bad weighting and need to be
        smoothed). With more iterations, more vertices can be smoothed.  This flag
        controls the maximum number of iterations the algorithm will attempt to smooth
        weights. The default is 2 for this flag.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - toSelectedBones : tsb          (bool)          [create]
        geometry will be bound to the selected bones only.
    
    - toSkeletonAndTransforms : tst  (bool)          [create]
        geometry will be bound to the skeleton and any transforms in the hierarchy. If
        any of the transforms are also bindable objects, assume that only the last
        object passed to the command is the bindable object. The rest are treated as
        influences.
    
    - unbind : ub                    (bool)          [edit]
        Unbinds the geometry from the skinCluster and deletes the skinCluster node
    
    - unbindKeepHistory : ubk        (bool)          [edit]
        Unbinds the geometry from the skinCluster, but keeps the skinCluster node so
        that its weights can be used when the skin is rebound. To rebind, use the
        skinCluster command.
    
    - useGeometry : ug               (bool)          [edit]
        When adding an influence to a skinCluster, use the geometry parented under the
        influence transform to determine the weight dropoff of that influence.
    
    - volumeBind : vb                (float)         [create]
        Creates a volume bind node and attaches it to the new skin cluster node. This
        node holds hull geometry parameters for a volume based weighting system. This
        system is used in interactive skinning. The value passed will determine the
        minimum weight value when initializing the volume. The volume in be increase to
        enclose all the vertices that are above this value.
    
    - volumeType : vt                (int)           [create]
        Defines the initial shape of the binding volume (see volumeBind). 0 - Default
        (currently set to a capsule) 1 - Capsule, 2 - Cylinder.
    
    - weight : wt                    (float)         [edit]
        This flag is only valid in conjunction with the -addInfluence flag. It sets the
        weight for the influence object that is being added.
    
    - weightDistribution : wd        (int)           [create,query,edit]
        This flag sets the weight distribution mode. 0 - distance (default), 1 -
        neighbors When normalizeWeights is in effect, and a weight has been reduced or
        removed altogether, the sum is usually brought back up to 1.0 by increasing the
        contributions of the other non-zero weights. However, if there are no other non-
        zero weights, the algorithm has to create some weights from thin air and
        distribute the residual weight between them. This attribute controls how that is
        done. Distance- the algorithm calculates weights from the world-space distances
        from the component to the transforms. Neighbors- the algorithm calculates
        weights from the weights on the neighboring components.
    
    - weightedInfluence : wi         (bool)          [query]
        This flag returns a string array of the influence objects (joints and transform)
        that have non-zero weighting.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.skinCluster`
    """
    pass


def findKeyframe(*args, **kwargs):
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
    list or range (see Examples). This command will return the time (in current
    units) of the requested key. For the relative direction methods (next, previous)
    if -time is NOT specified they will use current time. If the specified object is
    not animated the command will return the current time.
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - curve : c                      (bool)          [create]
        Return a list of the existing curves driving the selected object or attributes.
        The which, index, floatRange, timeRange, and includeUpperBound flags are ignored
        when this flag is used.
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
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
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - timeSlider : ts                (bool)          [create]
        Get the next key time from the ticks displayed in the time slider. If this flag
        is set, then the -an/animation flag is ignored.
    
    - which : w                      (unicode)       [create]
        next | previous | first | last How to find the key                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.findKeyframe`
    """
    pass


def animLayer(*args, **kwargs):
    """
    This command creates and edits animation layers.
    
    Flags:
    - addRelatedKG : akg             (bool)          [create,query,edit]
        Used adding attributes to a layer. Determines if associated keying groups should
        be added or not to the layer.
    
    - addSelectedObjects : aso       (bool)          [create,query,edit]
        Adds selected object(s) to the layer.
    
    - affectedLayers : afl           (bool)          [query]
        Return the layers that the currently selected object(s) are members of
    
    - animCurves : anc               (bool)          [create,query,edit]
        In query mode returns the anim curves associated with this layer
    
    - attribute : at                 (unicode)       [create,query,edit]
        Adds a specific attribute on a object to the layer.
    
    - baseAnimCurves : bac           (bool)          [create,query,edit]
        In query mode returns the base layer anim curves associated with this layer, if
        any.
    
    - bestAnimLayer : blr            (bool)          [create,query,edit]
        In query mode returns the best anim layers for keying for the selected objects.
        If used in conjunction with -at, will return the best anim layers for keying for
        the specific plugs (attributes) specified.
    
    - bestLayer : bl                 (bool)          [query]
        Return the layer that will be keyed for specified attribute.
    
    - blendNodes : bld               (bool)          [create,query,edit]
        In query mode returns the blend nodes associated with this layer
    
    - children : c                   (unicode)       [query]
        Get the list of children layers. Return value is a string array.
    
    - collapse : col                 (bool)          [create,query,edit]
        Determine if a layer is collapse in the layer editor.
    
    - copy : cp                      (unicode)       [edit]
        Copy from layer.
    
    - copyAnimation : ca             (unicode)       [create,edit]
        Copy animation from specified layer to destination layer, only animation that
        are on attribute layered by both layer that are concerned.
    
    - copyNoAnimation : cna          (unicode)       [edit]
        Copy from layer without the animation curves.
    
    - excludeBoolean : ebl           (bool)          [create,query,edit]
        When adding selected object(s) to the layer, excludes any boolean attributes.
    
    - excludeDynamic : edn           (bool)          [create,query,edit]
        When adding selected object(s) to the layer, excludes any dynamic attributes.
    
    - excludeEnum : een              (bool)          [create,query,edit]
        When adding selected object(s) to the layer, excludes any enum attributes.
    
    - excludeRotate : ert            (bool)          [create,query,edit]
        When adding selected object(s) to the layer, exclude the rotate attribute.
    
    - excludeScale : esc             (bool)          [create,query,edit]
        When adding selected object(s) to the layer, exclude the scale attribute.
    
    - excludeTranslate : etr         (bool)          [create,query,edit]
        When adding selected object(s) to the layer, excludes the translate attribute.
    
    - excludeVisibility : evs        (bool)          [create,query,edit]
        When adding selected object(s) to the layer, exclude the visibility attribute.
    
    - exists : ex                    (bool)          [query]
        Determine if an layer exists.
    
    - extractAnimation : ea          (unicode)       [create,edit]
        Transfer animation from specified layer to destination layer, only animation
        that are on attribute layered by both layer that are concerned.
    
    - findCurveForPlug : fcv         (unicode)       [query,edit]
        Finds the parameter curve containing the animation data for the specified plug
        on the given layer.
    
    - forceUIRebuild : fur           (bool)          [create]
        Rebuilds the animation layers user interface.
    
    - forceUIRefresh : uir           (bool)          [create]
        Refreshes the animation layers user interface.
    
    - layeredPlug : lp               (unicode)       [query]
        Returns the plug on the blend node corresponding to the specified layer
    
    - lock : l                       (bool)          [create,query,edit]
        Set the lock state of the specified layer. A locked layer cannot receive key.
        Default is false.
    
    - maxLayers : ml                 (bool)          [query]
        Returns the maximum number of anim layers supported by this product.
    
    - moveLayerAfter : mva           (unicode)       [edit]
        Move layer after the specified layer
    
    - moveLayerBefore : mvb          (unicode)       [edit]
        Move layer before the specified layer
    
    - mute : m                       (bool)          [create,query,edit]
        Set the mute state of the specified layer. Default is false.
    
    - override : o                   (bool)          [create,query,edit]
        Set the overide state of the specified layer. Default is false.
    
    - parent : p                     (unicode)       [create,query,edit]
        Set the parent of the specified layer. Default is the animation layer root.
    
    - passthrough : pth              (bool)          [create,query,edit]
        Set the passthrough state of the specified layer. Default is true.
    
    - preferred : prf                (bool)          [create,query,edit]
        Determine if a layer is a preferred layer, the best layer algorithm will try to
        set keyframe in preferred layer first.
    
    - removeAllAttributes : raa      (bool)          [edit]
        Remove all objects from layer.
    
    - removeAttribute : ra           (unicode)       [edit]
        Remove object from layer.
    
    - root : r                       (unicode)       [query]
        Return the base layer if it exist
    
    - selected : sel                 (bool)          [create,query,edit]
        Determine if a layer is selected, a selected layer will be show in the
        timecontrol, graph editor.
    
    - solo : s                       (bool)          [create,query,edit]
        Set the solo state of the specified layer. Default is false.
    
    - weight : w                     (float)         [create,query,edit]
        Set the weight of the specified layer between 0.0 and 1.0. Default is 1.
    
    - writeBlendnodeDestinations : wbd (bool)          [edit]
        In edit mode writes the destination plugs of the blend nodes that belong to the
        layer into the blend node. This is used for layer import/export purposes and is
        not for general use.                               Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.animLayer`
    """
    pass


def pairBlend(*args, **kwargs):
    """
    The pairBlend node allows a weighted combinations of 2 inputs to be blended
    together. It is created automatically when keying or constraining an attribute
    which is already connected.Alternatively, the pairBlend command can be used to
    connect a pairBlend node to connected attributes of a node. The previously
    existing connections are rewired to input1 of the pairBlend node. Additional
    connections can then be made manually to input2 of the pairBlend node. The
    pairBlend command can also be used to query the inputs to an existing pairBlend
    node.
    
    Flags:
    - attribute : at                 (unicode)       [create]
        The name of the attribute(s) which the blend will drive. This flag is required
        when creating the blend.
    
    - input1 : i1                    (bool)          [query]
        Returns a string array of the node(s) connected to input 1.
    
    - input2 : i2                    (bool)          [query]
        Returns a string array of the node(s) connected to input 2.
    
    - node : nd                      (unicode)       [create]
        The name of the node which the blend will drive. This flag is required when
        creating the blend.                                    Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pairBlend`
    """
    pass


def keyframe(*args, **kwargs):
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
    list or range (see Examples). This command edits the time and/or value of keys
    of specified objects and/or parameter curves Unless otherwise specified by the
    -query flag, the command defaults to editing keyframes.
    
    Flags:
    - absolute : a                   (bool)          [create]
        Move amounts are absolute.
    
    - adjustBreakdown : abd          (bool)          [create]
        When false, moving keys will not preserve breakdown timing, when true (the
        default) breakdowns will be adjusted to preserve their timing relationship.
    
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - breakdown : bd                 (bool)          [create,query,edit]
        Sets the breakdown state for the key.  Returns an integer.  Default is false.
        The breakdown state of a key cannot be set in the same command as it is moved
        (i.e., via the -tc or -fc flags).
    
    - clipTime : ct                  (time, time, <type 'float'>) [create]
        Modifies the final time where a key is inserted using an offset, pivot, and
        scale.
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - eval : ev                      (bool)          [create,query]
        Returns the value(s) of the animCurves when evaluated (without regard to input
        connections) at the times given by the -t/time or -f/float flags.  Cannot be
        used in combination with other query flags, and cannot be used with time ranges
        (-t 5:10). When no -t or -f flags appear on the command line, the evals are
        queried at the current time.  Query returns a float[].
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - floatChange : fc               (float)         [create,query,edit]
        How much (with -relative) or where (with -absolute) to move keys (on non-time-
        input animation curves) along the x (float) axis. Returns float[] when queried.
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
    - includeUpperBound : iub        (bool)          [create]
        When the -t/time or -f/float flags represent a range of keys, this flag
        determines whether the keys at the upper bound of the range are included in the
        keyset. Default value: true.  This flag is only valid when the argument to the
        -t/time flag is a time range with a lower and upper bound.  (When used with the
        pasteKeycommand, this flag refers only to the time range of the target curve
        that is replaced, when using options such as replace,fitReplace,or
        scaleReplace.This flag has no effect on the curve pasted from the clipboard.)
    
    - index : index                  (timeRange)     [create]
        index of a key on an animCurve
    
    - indexValue : iv                (bool)          [create,query]
        Query-only flag that returns an int for the key's index.
    
    - keyframeCount : kc             (bool)          [create,query]
        Returns an int for the number of keys found for the targets.
    
    - lastSelected : lsl             (bool)          [create,query]
        When used in queries, this flag returns requested values for the last selected
        key.
    
    - name : n                       (bool)          [create,query]
        Returns the names of animCurves of specified nodes, attributes or keys.
    
    - option : o                     (unicode)       [create,edit]
        Valid values are move,insert,over,and segmentOver.When you movea key, the key
        will not cross over (in time) any keys before or after it. When you inserta key,
        all keys before or after (depending upon the -timeChange value) will be moved an
        equivalent amount. When you overa key, the key is allowed to move to any time
        (as long as a key is not there already). When you segmentOvera set of keys (this
        option only has a noticeable effect when more than one key is being moved) the
        first key (in time) and last key define a segment (unless you specify a time
        range). That segment is then allowed to move over other keys, and keys will be
        moved to make room for the segment.
    
    - relative : r                   (bool)          [create]
        Move amounts are relative to a key's current position.
    
    - selected : sl                  (bool)          [create,query]
        When used in queries, this flag returns requested values for any active keys.
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - tickDrawSpecial : tds          (bool)          [create,edit]
        Sets the special drawing state for this key when it is drawn as a tick in the
        timeline.
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - timeChange : tc                (time)          [create,query,edit]
        How much (with -relative) or where (with -absolute) to move keys (on time-input
        animation curves) along the x (time) axis.  Returns float[] when queried.
    
    - valueChange : vc               (float)         [create,query,edit]
        How much (with -relative) or where (with -absolute) to move keys along the y
        (value) axis. Returns float[] when queried.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframe`
    """
    pass


def keyingGroup(*args, **kwargs):
    """
    This command is used to manage the membership of a keying group.  Keying groups
    allow users to effectively manage related keyframe data, allowing keys on
    attributes in the keying group to be set and edited as a single entity.
    
    Flags:
    - activator : act                (PyNode)        [query,edit]
        Sets the selected node(s) as activators for the given keying group. In query
        mode, returns list of objects that activate the given keying group
    
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
    
    - category : cat                 (unicode)       [create,query,edit]
        Sets the keying group's category. This is what the global, active keying group
        filter will use to match.
    
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
    
    - excludeDynamic : ed            (bool)          [create]
        When creating the keying group, exclude dynamic attributes.
    
    - excludeRotate : er             (bool)          [create]
        When creating the keying group, exclude rotate attributes from transform-type
        nodes.
    
    - excludeScale : es              (bool)          [create]
        When creating the keying group, exclude scale attributes from transform-type
        nodes.
    
    - excludeTranslate : et          (bool)          [create]
        When creating the keying group, exclude translate attributes from transform-type
        nodes. For example, if your keying group contains joints only, perhaps you only
        want to include rotations in the keying group.
    
    - excludeVisibility : ev         (bool)          [create]
        When creating the keying group, exclude visibility attribute from transform-type
        nodes.
    
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
    
    - minimizeRotation : mr          (bool)          [create,query,edit]
        This flag only affects the attribute contained in the immediate keyingGroup. It
        does not affect attributes in sub-keyingGroups. Those will need to set
        minimizeRotation on their respective keyingGroups
    
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
    
    - removeActivator : rac          (PyNode)        [edit]
        Removes the selected node(s) as activators for the given keying group.
    
    - renderable : r                 (bool)          [create,query]
        This flag indicates that a special type of set should be created. This type of
        set (shadingEngine as opposed to objectSet) has certain restrictions on its
        membership in that it can only contain renderable elements such as lights and
        geometry. These sets are referred to as shading groups and are automatically
        connected to the renderPartitionnode when created (to ensure mutual exclusivity
        of the set's members with the other sets in the partition). This flag is for use
        in creation or query mode only. The default value is false which means a normal
        set is created.
    
    - setActiveFilter : fil          (unicode)       [create,query,edit]
        Sets the global, active keying group filter, which will affect activation of
        keying groups. Only keying groups with categories that match the filter will be
        activated. If the setActiveFilter is set to NoKeyingGroups, keying groups will
        not be activated at all. If the setActiveFilter is set to AllKeyingGroups, we
        will activate any keying group rather than just those with matching categories.
    
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
    
    
    Derived from mel command `maya.cmds.keyingGroup`
    """
    pass


def bakeDeformer(*args, **kwargs):
    """
    Given a rigged character, whose mesh shape is determined by a set of deformers,
    bakeDeformer calculates linear blend skin weights most closely approximating
    observed deformations. To do this, a test set of examples is generated by moving
    the rig through a range of motion. Results mesh and pose pairs are then used to
    solve a constrained optimization, solving for skinning weights. bakeDeformer
    automatically binds and applies resulting weights to the destination geometry.
    If the source and destination mesh/skeleton are identical, the command will
    replace the original deformations with a skinCluster and computed weights. See
    the below examples for sample usage.
    
    Flags:
    - colorizeSkeleton : cs          (bool)          [create]
        The new skin cluster created will have its skeleton colorized. Must be used with
        the -srcSkeletonName and -dstSkeletonName flags.
    
    - customRangeOfMotion : rom      (timerange)     [create]
        When this flag is specified with the frames for the range of motion to be used,
        the tool will step through each frame as a separate pose. Otherwise the tool
        will use the existing range of motion in the tool that rotates each influence 45
        degrees. Usage examples:     -rom 10:20means all frames in the range from 10 to
        20, inclusive, in the current time unit. Omitting one end of a range means using
        either end of the animation range (or both), as in the following examples: -rom
        10:means all frames from time 10 (in the current time unit) onwards to the
        maximum time in the animation range (on the timeline). -rom :10means all frames
        from the minimum time on the animation range (on the timeline) up to (and
        including) time 10 (in the current time unit). -rom :is a short form to specify
        all frames, from minimum to maximum time on the current animation range. When
        using this flag, some of the joints in the specified range of motion may not
        have changed sufficiently. To improve bakeDeformer results or avoid algorithm
        errors, the command will return a list of influences that do not move enough in
        the specified range of motion. To detect these joints, the localtransformation
        of each joint is compared between subsequent frames. We consider that a joint
        has sufficiently changed if any of the below criteria are met:     There is a
        rotation of at least 5 degrees, as determined by the shortest rotation between
        transforms.There is a translation of 1% or greater of the size of the largest
        bounding box containing all joints for each frame.There is a scaling change of
        at least 1%. This percentage represents the smallest scaling value over the
        largest scaling value (in absolute value).If a joint has not met any of the
        criteria, it will be added to the warning of joints that have not moved enough.
        The custom range of motion should be considered experimental.
    
    - dstMeshName : dm               (unicode)       [create]
        The destination mesh name.
    
    - dstSkeletonName : ds           (unicode)       [create]
        The destination skeleton name.
    
    - hierarchy : hi                 (bool)          [create]
        All children of the passed joints that are used in the influences flag are used.
    
    - influences : i                 (unicode)       [create]
        A list of joints that are used as the influences to determine new weights.
    
    - maxInfluences : mi             (int)           [create]
        The maximum number of influences per vertex.
    
    - pruneWeights : pw              (float)         [create]
        On the newly created skin cluster, set any weight below the given the value to
        zero (post-processing). This will call the skinPercent command as follows:
        skinPercent -pruneWeights [value] [skinClusterName] [dstMeshName]where [value]
        is the value passed into this flag, [skinClusterName] is the name of the new
        skinCluster node created after running this tool, and [dstMeshName] is the mesh
        provided in the -dstMeshName flag.
    
    - smoothWeights : sw             (int)           [create]
        The number of smoothing iterations for smoothing weights (post-processing). This
        also renormalizes the remaining the weights.
    
    - srcMeshName : sm               (unicode)       [create]
        The source mesh name.
    
    - srcSkeletonName : ss           (unicode)       [create]
        The source skeleton name.                                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.bakeDeformer`
    """
    pass


def _orientConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def blendShapePanel(*args, **kwargs):
    """
    This command creates a panel that derives from the base panel class that houses
    a blendShapeEditor.
    
    Flags:
    - blendShapeEditor : be          (bool)          [query]
        Query only flag that returns the name of an editor to be associated with the
        panel.
    
    - control : ctl                  (bool)          [query]
        Returns the top level control for this panel. Usually used for getting a parent
        to attach popup menus. CAUTION: panels may not have controls at times.  This
        flag can return if no control is present.
    
    - copy : cp                      (unicode)       [edit]
        Makes this panel a copy of the specified panel.  Both panels must be of the same
        type.
    
    - createString : cs              (bool)          [edit]
        Command string used to create a panel
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the Maya panel.
    
    - editString : es                (bool)          [edit]
        Command string used to edit a panel
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - init : init                    (bool)          [create,edit]
        Initializes the panel's default state.  This is usually done automatically on
        file -new and file -open.
    
    - isUnique : iu                  (bool)          [query]
        Returns true if only one instance of this panel type is allowed.
    
    - label : l                      (unicode)       [query,edit]
        Specifies the user readable label for the panel.
    
    - menuBarRepeatLast : mrl        (bool)          [create,query,edit]
        Controls whether clicking on the menu header with the middle mouse button would
        repeat the last selected menu item.
    
    - menuBarVisible : mbv           (bool)          [create,query,edit]
        Controls whether the menu bar for the panel is displayed.
    
    - needsInit : ni                 (bool)          [query,edit]
        (Internal) On Edit will mark the panel as requiring initialization. Query will
        return whether the panel is marked for initialization.  Used during file -new
        and file -open.
    
    - parent : p                     (unicode)       [create]
        Specifies the parent layout for this panel.
    
    - popupMenuProcedure : pmp       (script)        [query,edit]
        Specifies the procedure called for building the panel's popup menu(s). The
        default value is buildPanelPopupMenu.  The procedure should take one string
        argument which is the panel's name.
    
    - replacePanel : rp              (unicode)       [edit]
        Will replace the specified panel with this panel.  If the target panel is within
        the same layout it will perform a swap.
    
    - tearOff : to                   (bool)          [query,edit]
        Will tear off this panel into a separate window with a paneLayout as the parent
        of the panel. When queried this flag will return if the panel has been torn off
        into its own window.
    
    - tearOffCopy : toc              (unicode)       [create]
        Will create this panel as a torn of copy of the specified source panel.
    
    - tearOffRestore : tor           (bool)          [create,edit]
        Restores panel if it is torn off and focus is given to it. If docked, becomes
        the active panel in the docked window. This should be the default flag that is
        added to all panels instead of -to/-tearOffflag which should only be used to
        tear off the panel.
    
    - unParent : up                  (bool)          [edit]
        Specifies that the panel should be removed from its layout. This (obviously)
        cannot be used with query.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.blendShapePanel`
    """
    pass


def tangentConstraint(*args, **kwargs):
    """
    Constrain an object's orientation based on the tangent of the target curve[s] at
    the closest point[s] to the object. A tangentConstraint takes as input one or
    more NURBS curves (the targets) and a DAG transform node (the object).  The
    tangentConstraint orients the constrained object such that the aimVector (in the
    object's local coordinate system) aligns in world space to combined tangent
    vector.  The upVector (again the the object's local coordinate system) is
    aligned in world space with the worldUpVector.  The combined tangent vector is a
    weighted average of the tangent vector for each target curve at the point
    closest to the constrained object.
    
    Flags:
    - aimVector : aim                (float, float, float) [create,query,edit]
        Set the aim vector.  This is the vector in local coordinates that points at the
        target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is
        used.
    
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - upVector : u                   (float, float, float) [create,query,edit]
        Set local up vector.  This is the vector in local coordinates that aligns with
        the world up vector.  If not given at creation time, the default value of (0.0,
        1.0, 0.0) is used.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag
    
    - worldUpObject : wuo            (PyNode)        [create,query,edit]
        Set the DAG object use for worldUpType objectand objectrotation. See worldUpType
        for greater detail. The default value is no up object, which is interpreted as
        world space.
    
    - worldUpType : wut              (unicode)       [create,query,edit]
        Set the type of the world up vector computation. The worldUpType can have one of
        5 values: scene, object, objectrotation, vector, or none. If the value is scene,
        the upVector is aligned with the up axis of the scene and worldUpVector and
        worldUpObject are ignored. If the value is object, the upVector is aimed as
        closely as possible to the origin of the space of the worldUpObject and the
        worldUpVector is ignored. If the value is objectrotationthen the worldUpVector
        is interpreted as being in the coordinate space of the worldUpObject,
        transformed into world space and the upVector is aligned as closely as possible
        to the result. If the value is vector, the upVector is aligned with
        worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if
        the value is noneno twist calculation is performed by the constraint, with the
        resulting upVectororientation based previous orientation of the constrained
        object, and the great circlerotation needed to align the aim vector with its
        constraint. The default worldUpType is vector.
    
    - worldUpVector : wu             (float, float, float) [create,query,edit]
        Set world up vector.  This is the vector in world coordinates that up vector
        should align with. See -wut/worldUpType (below)for greater detail. If not given
        at creation time, the default value of (0.0, 1.0, 0.0) is used.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.tangentConstraint`
    """
    pass


def sculpt(*args, **kwargs):
    """
    This command creates/edits/queries a sculpt object deformer. By default for
    creation mode an implicit sphere will be used as the sculpting object if no
    sculpt tool is specified. The name of the created/edited object is returned.
    
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
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - dropoffDistance : dds          (float)         [create,query,edit]
        Specifies the distance from the surface of the sculpt object at which the sculpt
        object produces no deformation effect. Default is 1.0. When queried, this flag
        returns a float.
    
    - dropoffType : drt              (unicode)       [create,query,edit]
        Specifies how the deformation effect drops off from maximum effect at the
        surface of the sculpt object to no effect at dropoff distance limit. Valid
        values are: linear | none. Default is linear. When queried, this flag returns a
        string.
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - groupWithLocator : gwl         (bool)          [create]
        Groups the sculptor and its locator together under a single transform. Default
        is off.
    
    - ignoreSelected : ignoreSelected (bool)          [create]
        Tells the command to not deform objects on the current selection list
    
    - includeHiddenSelections : ihs  (bool)          [create]
        Apply the deformer to any visible and hidden objects in the selection list.
        Default is false.
    
    - insideMode : im                (unicode)       [create,query,edit]
        Specifies how the deformation algorithm deals with points that are inside the
        sculpting primitve. The choices are: ring | even. The default is even. When
        queried, this flag returns a string. Ring mode will tend to produce a contour
        like ring of points around the sculpt object as it passes through an object
        while even mode will try to spread the points out as evenly as possible across
        the surface of the sculpt object.
    
    - maxDisplacement : mxd          (float)         [create,query,edit]
        Defines the maximum amount the sculpt object may move a point on an object which
        it is deforming. Default is 1.0. When queried, this flag returns a float.
    
    - mode : m                       (unicode)       [create,query,edit]
        Specifies which deformation algorithm the sculpt object should use. The choices
        are: flip | project | stretch. The default is stretch. When queried, this flag
        returns a string.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - objectCentered : oc            (bool)          [create]
        Places the sculpt and locator in the center of the bounding box of the selected
        object(s) or components. Default is off which centers the sculptor and locator
        at the origin.
    
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
    
    - sculptTool : st                (unicode)       [create]
        Use the specified NURBS object as the sculpt tool instead of the default
        implicit sphere.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.sculpt`
    """
    pass


def _tangentConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def pasteKey(*args, **kwargs):
    """
    The pasteKey command pastes curve segment hierarchies from the clipboard onto
    other objects or curves. If the object hierarchy from which the curve segments
    were copied or cut does not match the object hierarchy being pasted to, pasteKey
    will paste as much as it can match in the hierarchy.  If animation from only one
    object is on the clipboard, it will be pasted to each of the target objects. If
    animation from more than one object is on the clipboard, selection list order
    determines what animation is pasted to which object. Valid operations include:
    One attribute to one or more attributes (Clipboard animation is pasted onto all
    target attributes.One attribute to one or more objects (Clipboard animation
    pasted onto target object, when attribute names match.)Many attributes to one or
    more objectsClipboard animation pasted onto targets when attribute names
    match.TbaseKeySetCmd.h The way the keyset clipboard will be pasted to the
    specified object's attributes depends on the paste -optionspecified. Each of
    these options below will be explained using an example. For all the
    explanations, let us assume that there is a curve segment with 20 frames of
    animation on the keyset clipboard (you can put curve segments onto the clipboard
    using the cutKeyor copyKeycommands). We will call the animation curve that we
    are pasting to the target curve: pasteKey -time 5 -option insert1. Shift all
    keyframes on the target curve after time 5 to the right by 20 frames (to make
    room for the 20-frame clipboard segment). 2. Paste the 20-frame clipboard
    segment starting at time 5. pasteKey -time 5:10-option replace1. Remove all keys
    on the target curve from 5 to 10. 2. Paste the 20-frame clipboard curve at time
    5. Keys from frame 11-25 will be overridden if a key is present on the clipboard
    curve. pasteKey -option replaceCompletely1. Remove all keys on the target curve.
    2. Paste the 20-frame clipboard curve, preserving the clipboard curve's original
    keyframe times. pasteKey -time 5 -option merge1.The clipboard curve segment will
    be pasted starting at time 5 for its full 20-frame range until frame 25. 2. If a
    keyframe on the target curve has the same time as a keyframe on the clipboard
    curve, it is overwritten. Otherwise, any keys that existed in the 5:25 range
    before the paste, will remain untouched pasteKey -time 3:10-option scaleInsert1.
    Shift all keyframes on the target curve after time 3 to the right by 7 frames
    (to clear the range 3:10 to paste in) 2. The clipboard curve segment will be
    scaled to fit the specified time range (i.e. the 20 frames on the clipboard will
    be scaled to fit into 7 frames), and then pasted into the range 3:10. pasteKey
    -time 3:10-option scaleReplace1. Any existing keyframes in the target curve in
    the range 3:10 are removed. 2. The clipboard curve segment will be scaled to fit
    the specified time range (i.e. the 20 frames on the clipboard will be scaled to
    fit into 7 frames), and then pasted into the range 3:10. pasteKey -time
    3:10-option scaleMerge1. The clipboard curve segment will be scaled to fit the
    specified time range (i.e. the 20 frames on the clipboard will be scaled to fit
    into 7 frames). 2. If there are keys on the target curve at the same time as
    keys on the clipboard curve, they are overwritten. Otherwise, keyframes on the
    target curve that existed in the 3:10 range before the paste, will remain
    untouched. pasteKey -time 3:10-option fitInsert1. Shift all the keyframes on the
    target curve after time 3 to the right by 7 frames (to clear the range 3:10 to
    paste in) 2. The first 7 frames of the clipboard curve segment will be pasted
    into the range 3:10. pasteKey -time 3:10-option fitReplace1. Any existing frames
    in the target curve in the range 3:10 are removed. 2. The first 7 frames of the
    clipboard curve segment will be pasted into the range 3:10. pasteKey -time
    3:10-option fitMerge1. The first 7 frames of the clipboard curve segment will be
    pasted into the range 3:10. 2. If there are keys on the target curve at the same
    time as keys on the clipboard curve, they are overwritten. Otherwise, keyframes
    on the target curve that existed in the 3:10 range before the paste, will remain
    untouched.
    
    Flags:
    - animLayer : al                 (unicode)       [create]
        Specifies that the keys getting pasted should be pasted onto curves on the
        specified animation layer.If that layer doesn't exist for the specified objects
        or attributes then the keys won't get pasted.
    
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - clipboard : cb                 (unicode)       [create]
        Specifies the clipboard from which animation is pasted. Valid clipboards are
        apiand anim.  The default clipboard is: anim
    
    - connect : c                    (bool)          [create]
        When true, connect the source curve with the destination curve's value at the
        paste time. (This has the effect of shifting the clipboard curve in value to
        connect with the destination curve.) False preserves the source curve's original
        keyframe values. Default is false.
    
    - copies : cp                    (int)           [create]
        The number of times to paste the source curve.
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - floatOffset : fo               (float)         [create]
        How much to offset the pasted keys in time (for non-time-input animation
        curves).
    
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
    
    - matchByName : mn               (bool)          [create]
        When true, we will only paste onto items in the scene whose node and attribute
        names match up exactly with a corresponding item in the clipboard. No hierarchy
        information is used. Default is false, and in this case the usual matching by
        hierarchy occurs.
    
    - option : o                     (unicode)       [create]
        Valid values are insert, replace, replaceCompletely, merge,
        scaleInsert,scaleReplace, scaleMerge, fitInsert, fitReplace, and fitMerge. The
        default paste option is: insert.
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve.  See
        the code examples below on how to format for a single frame or frame ranges.
    
    - timeOffset : to                (time)          [create]
        How much to offset the pasted keys in time (for time-input animation curves).
    
    - valueOffset : vo               (float)         [create]
        How much to offset the pasted keys in value.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pasteKey`
    """
    pass


def movOut(*args, **kwargs):
    """
    Exports a .mov file from the listed attributes. Valid attribute types are
    numeric attributes; time attributes; linear attributes; angular attributes;
    compound attributes made of the types listed previously; and multi attributes
    composed of the types listed previously. Length, angle, and time values will be
    written to the file in the user units. If an unsupported attribute type is
    requested, the action will fail. The .mov file may be read back into Maya using
    the movIn command.
    
    Flags:
    - comment : c                    (bool)          [create]
        If true, the attributes written to the .mov file will be listed in a commented
        section at the top of the .mov file. The default is false.
    
    - file : f                       (unicode)       [create]
        The name of the .mov file. If no extension is used, a .mov will be added.
    
    - precision : pre                (int)           [create]
        Sets the number of digits to the right of the decimal place in the .mov file.C:
        The default is 6.
    
    - time : t                       (timerange)     [create]
        The time range to save as a .mov file. The default is the current time range.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.movOut`
    """
    pass


def jointLattice(*args, **kwargs):
    """
    This command creates/edits/queries a jointLattice deformer. The name of the
    created/edited object is returned. Usually you would make use of this
    functionality through the higher level flexor command.
    
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
    
    - creasing : cr                  (float)         [create,query,edit]
        Affects the bulging of lattice points on the inside of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - joint : j                      (unicode)       [create]
        Specifies the joint which will be used to drive the bulging behaviours.
    
    - lengthIn : li                  (float)         [create,query,edit]
        Affects the location of lattice points on the parent bone.  Positive/negative
        values cause the points to move away/towards the joint. Changing this parameter
        also modifies the regions affected by the creasing, rounding and width
        parameters. Default value is 0.0. When queried, this flag returns a float.
    
    - lengthOut : lo                 (float)         [create,query,edit]
        Affects the location of lattice points on the child bone. Positive/negative
        values cause the points to move away/towards the joint. Changing this parameter
        also modifies the regions affected by the creasing, rounding and width
        parameters. Default value is 0.0. When queried, this flag returns a float.
    
    - lowerBindSkin : lb             (unicode)       [create]
        Specifies the node which is performing the bind skin operation on the geometry
        associated with the lower bone.
    
    - lowerTransform : lt            (unicode)       [create]
        Specifies which dag node is being used to rigidly transform the lower part of
        the lattice which this node is going to deform. If this flag is not specified an
        identity matrix will be assumed.
    
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
    
    - rounding : ro                  (float)         [create,query,edit]
        Affects the bulging of lattice points on the outside of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - upperBindSkin : ub             (unicode)       [create]
        Specifies the node which is performing the bind skin operation on the geometry
        associated with the upper bone.
    
    - upperTransform : ut            (unicode)       [create]
        Specifies which dag node is being used to rigidly transform the upper part of
        the lattice which this node is going to deform. If this flag is not specified an
        identity matrix will be assumed.
    
    - widthLeft : wl                 (float)         [create,query,edit]
        Affects the bulging of lattice points on the left side of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.
    
    - widthRight : wr                (float)         [create,query,edit]
        Affects the bulging of lattice points on the right side of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.jointLattice`
    """
    pass


def characterMap(*args, **kwargs):
    """
    This command is used to create a correlation between the attributes of 2 or more
    characters.
    
    Flags:
    - mapAttr : ma                   (unicode, unicode) [create,query,edit]
        In query mode, this flag can be used to query the mapping stored by the
        specified map node. It returns an array of strings. In non-query mode, this flag
        can be used to create a mapping between the specified character members. Any
        previous mapping on the attributes is removed in favor of the newly specified
        mapping.
    
    - mapMethod : mm                 (unicode)       [create]
        This is is valid in create mode only. It specifies how the mapping should be
        done. Valid options are: byNodeName, byAttrName, and byAttrOrder. byAttrOrderis
        the default. The flags mean the following: byAttrOrdermaps using the order that
        the character stores the attributes internally, byAttrNameuses the attribute
        name to find a correspondence, byNodeNameuses the node name \*and\* the
        attribute name to find a correspondence.
    
    - mapNode : mn                   (unicode, unicode) [create,query]
        This flag can be used to map all the attributes on the source node to their
        matching attributes on the destination node.
    
    - mapping : m                    (unicode)       [query]
        This flag is valid in query mode only. It must be used before the query flag
        with a string argument. It is used for querying the mapping for a particular
        attribute.  A string array is returned.
    
    - proposedMapping : pm           (bool)          [query]
        This flag is valid in query mode only. It is used to get an array of the mapping
        that the character map would prvide if called with the specified characters and
        the (optional) specified mappingMethod. If a character map exists on the
        characters, the map is not affected by the query operation.  A string array is
        returned.
    
    - unmapAttr : ua                 (unicode, unicode) [create,edit]
        This flag can be used to unmap the mapping stored by the specified map node.
    
    - unmapNode : umn                (unicode, unicode) [create]
        This flag can be used to unmap all the attributes on the source node to their
        matching attributes on the destination node. Note that mapped attributes which
        do not have matching names, will not be unmapped.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.characterMap`
    """
    pass


def snapshot(*args, **kwargs):
    """
    This command can be used to create either a series of surfaces evaluated at the
    times specified by the command flags, or a motion trail displaying the
    trajectory of the object's pivot point at the times specified.If the
    constructionHistory flag is true, the output shapes or motion trail will re-
    update when modifications are made to the animation or construction history of
    the original shape. When construction history is used, the forceUpdate flag can
    be set to false to control when the snapshot recomputes, which will typically
    improve performance.
    
    Flags:
    - anchorTransform : at           (unicode)       []
    
    - constructionHistory : ch       (bool)          [create,query]
        update with changes to original geometry
    
    - endTime : et                   (time)          [create,query,edit]
        time to stop copying target geometry Default: 10.0
    
    - increment : i                  (time)          [create,query,edit]
        time increment between copies Default: 1.0
    
    - motionTrail : mt               (bool)          [create]
        Rather than create a series of surfaces, create a motion trail displaying the
        location of the object's pivot point at the specified time steps. Default is
        false.
    
    - motionTrailName : mtn          (unicode)       []
    
    - name : n                       (unicode)       [create,query,edit]
        the name of the snapshot node. Query returns string.
    
    - removeAnchorTransform : rat    (unicode)       []
    
    - startTime : st                 (time)          [create,query,edit]
        time to begin copying target geometry Default: 1.0
    
    - update : u                     (unicode)       [create,query,edit]
        This flag can only be used if the snapshot has constructionHistory. It sets the
        snapshot node's update value. The update value controls whether the snapshot
        updates on demand (most efficient), when keyframes change (efficient), or
        whenever any history changes (least efficient). Valid values are demand,
        animCurve, always. Default: alwaysFlag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.snapshot`
    """
    pass


def timeEditor(*args, **kwargs):
    """
    General Time Editor commands
    
    Flags:
    - allClips : alc                 (unicode)       [create]
        Return an exhaustive (recursive) list of all clip IDs from the active
        composition. Arguments may be used to filter the returning result. An empty
        string will return clip IDs for all clip types: roster container group
    
    - clipId : id                    (int)           [create]
        ID of the clip to be edited.
    
    - commonParentTrack : cpt        (bool)          [create]
        Locate the common parent track node and track index of the given clip IDs.
        Requires a list of clip IDs to be specified using the clipId flag. The format of
        the returned string is track_node:track_index. If the clips specified are on the
        same track node but in different track indexes, only the track node will be
        returned.
    
    - composition : cp               (unicode)       [create]
        A flag to use in conjunction with -dca/drivingClipsForObjto indicate the name of
        composition to use. By default if this flag is not provided, current active
        composition will be used.
    
    - drivingClipsForAttr : dca      (unicode)       [create]
        Return a list of clips driving the specified attribute(s). If the composition is
        not specified, current active composition will be used.
    
    - drivingClipsForObj : dco       (unicode, int)  [create]
        Return a list of clips driving the specified object(s) with an integer value
        indicating the matching mode. If no object is specified explicitly, the selected
        object(s) will be used. Objects that cannot be driven by clips are ignored. If
        the composition is not specified, current active composition will be used.
        Default match mode is 0. 0: Include only the clip that has an exact match1:
        Include any clip that contains all of the specified objects2: Include any clip
        that contains any of the specified objects3: Include all clips that do not
        include any of the specified objects
    
    - includeParent : ip             (bool)          [create]
        A toggle flag to use in conjunction with -dca/drivingClipsForObj. When toggled,
        parent clip is included in selection (the entire hierarchy will be selected).
    
    - mute : m                       (bool)          [create,query]
        Mute/unmute Time Editor.
    
    - selectedClips : sc             (unicode)       [create]
        Return a list of clip IDs of currently selected Time Editor clips. Arguments may
        be used to filter the returning result. An empty string will return clip IDs for
        all clip types: roster container group
    
    - topLevelClips : tlc            (unicode)       [create]
        Return a list of all top-level clip IDs from the active composition. Arguments
        may be used to filter the returning result. An empty string will return clip IDs
        for all clip types: roster container group Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.timeEditor`
    """
    pass


def deformer(*args, **kwargs):
    """
    This command creates a deformer of the specified type. The deformer will deform
    the selected objects.
    
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
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - type : typ                     (unicode)       [create]
        Specify the type of deformer to create. This flag is required in create mode.
        Typically the type should specify a loaded plugin deformer. This command should
        typically not be used to create one of the standard deformers such as sculpt,
        lattice, blendShape, wire and cluster, since they have their own customized
        commands which perform useful specialized functionality.                  Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.deformer`
    """
    pass


def simplify(*args, **kwargs):
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
    list or range (see Examples). This command will simplify (reduce the number of
    keyframes) an animation curve.
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - floatTolerance : ft            (float)         [create]
        Specify the x-axis tolerance (defaults to 0.05) for float-input animCurves such
        as those created by Set Driven Keyframe. This flag is ignored on animCurves
        driven by time. Higher floatTolerance values will result in sparser keys which
        may less accurately represent the initial curve.
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
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
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - timeTolerance : tt             (time)          [create]
        Specify the x-axis tolerance (defaults to 0.05 seconds) for time-input
        animCurves. This flag is ignored on animCurves driven by floats. Higher time
        tolerance values will result in sparser keys which may less accurately represent
        the initial curve.
    
    - valueTolerance : vt            (float)         [create]
        Specify the value tolerance (defaults to 0.01)                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.simplify`
    """
    pass


def _pointConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def softMod(*args, **kwargs):
    """
    The softMod command creates a softMod or edits the membership of an existing
    softMod. The command returns the name of the softMod node upon creation of a new
    softMod.
    
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
    
    - bindState : bs                 (bool)          [create]
        Specifying this flag adds in a compensation to ensure the softModed objects
        preserve their spatial position when softModed. This is required to prevent the
        geometry from jumping at the time the softMod is created in situations when the
        softMod transforms at softMod time are not identity.
    
    - curveInterpolation : ci        (int)           [create]
        Ramp interpolation corresponding to the specified curvePoint position. Integer
        values of 0-3 are valid, corresponding to none, linear, smoothand
        splinerespectively. This flag may only be used in conjunction with the
        curvePoint and curveValue flag.
    
    - curvePoint : cp                (float)         [create]
        Position of ramp value on normalized 0-1 scale. This flag may only be used in
        conjunction with the curveInterpolation and curveValue flags.
    
    - curveValue : cv                (float)         [create]
        Ramp value corresponding to the specified curvePoint position. This flag may
        only be used in conjunction with the curveInterpolation and curvePoint flags.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - envelope : en                  (float)         [create,query,edit]
        Set the envelope value for the deformer. Default is 1.0
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
    - falloffAroundSelection : fas   (bool)          [create]
        Falloff will be calculated around any selected components
    
    - falloffBasedOnX : fbx          (bool)          [create]
        Falloff will be calculated using the X component.
    
    - falloffBasedOnY : fby          (bool)          [create]
        Falloff will be calculated using the Y component.
    
    - falloffBasedOnZ : fbz          (bool)          [create]
        Falloff will be calculated using the Z component.
    
    - falloffCenter : fc             (float, float, float) [create]
        Set the falloff center point of the softMod.
    
    - falloffMasking : fm            (bool)          [create]
        Deformation will be restricted to selected components
    
    - falloffMode : fom              (int)           [create]
        Set the falloff method used for the softMod.
    
    - falloffRadius : fr             (float)         [create]
        Set the falloff radius of the softMod.
    
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
    
    - relative : rel                 (bool)          [create]
        Enable relative mode for the softMod. In relative mode, Only the transformations
        directly above the softMod are used by the softMod. Default is off.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - resetGeometry : rg             (bool)          [edit]
        Reset the geometry matrices for the objects being deformed by the softMod. This
        flag is used to get rid of undesirable effects that happen if you scale an
        object that is deformed by a softMod.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - weightedNode : wn              (unicode, unicode) [create,query,edit]
        Transform node in the DAG above the softMod to which all percents are applied.
        The second node specifies the descendent of the first node from where the
        transformation matrix is evaluated. Default is the softMod handle.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.softMod`
    """
    pass


def shapePanel(*args, **kwargs):
    """
    This command creates a panel that derives from the base panel class that houses
    a shapeEditor.
    
    Flags:
    - control : ctl                  (bool)          [query]
        Returns the top level control for this panel. Usually used for getting a parent
        to attach popup menus. CAUTION: panels may not have controls at times.  This
        flag can return if no control is present.
    
    - copy : cp                      (unicode)       [edit]
        Makes this panel a copy of the specified panel.  Both panels must be of the same
        type.
    
    - createString : cs              (bool)          [edit]
        Command string used to create a panel
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the Maya panel.
    
    - editString : es                (bool)          [edit]
        Command string used to edit a panel
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - init : init                    (bool)          [create,edit]
        Initializes the panel's default state.  This is usually done automatically on
        file -new and file -open.
    
    - isUnique : iu                  (bool)          [query]
        Returns true if only one instance of this panel type is allowed.
    
    - label : l                      (unicode)       [query,edit]
        Specifies the user readable label for the panel.
    
    - menuBarRepeatLast : mrl        (bool)          [create,query,edit]
        Controls whether clicking on the menu header with the middle mouse button would
        repeat the last selected menu item.
    
    - menuBarVisible : mbv           (bool)          [create,query,edit]
        Controls whether the menu bar for the panel is displayed.
    
    - needsInit : ni                 (bool)          [query,edit]
        (Internal) On Edit will mark the panel as requiring initialization. Query will
        return whether the panel is marked for initialization.  Used during file -new
        and file -open.
    
    - parent : p                     (unicode)       [create]
        Specifies the parent layout for this panel.
    
    - popupMenuProcedure : pmp       (script)        [query,edit]
        Specifies the procedure called for building the panel's popup menu(s). The
        default value is buildPanelPopupMenu.  The procedure should take one string
        argument which is the panel's name.
    
    - replacePanel : rp              (unicode)       [edit]
        Will replace the specified panel with this panel.  If the target panel is within
        the same layout it will perform a swap.
    
    - shapeEditor : se               (bool)          [query]
        Query only flag that returns the name of an editor to be associated with the
        panel.
    
    - tearOff : to                   (bool)          [query,edit]
        Will tear off this panel into a separate window with a paneLayout as the parent
        of the panel. When queried this flag will return if the panel has been torn off
        into its own window.
    
    - tearOffCopy : toc              (unicode)       [create]
        Will create this panel as a torn of copy of the specified source panel.
    
    - tearOffRestore : tor           (bool)          [create,edit]
        Restores panel if it is torn off and focus is given to it. If docked, becomes
        the active panel in the docked window. This should be the default flag that is
        added to all panels instead of -to/-tearOffflag which should only be used to
        tear off the panel.
    
    - unParent : up                  (bool)          [edit]
        Specifies that the panel should be removed from its layout. This (obviously)
        cannot be used with query.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.shapePanel`
    """
    pass


def dagPose(*args, **kwargs):
    """
    This command is used to save and restore the matrix information for a dag
    hierarchy. Specifically, the data stored will restore the translate, rotate,
    scale, scale pivot, rotate pivot, rotation order, and (for joints) joint order
    for all the objects on the hierarchy. Data for other attributes is not stored by
    this command. This command can also be used to store a bindPose for an object.
    When you skin an object, a dagPose is automatically created for the skin.
    
    Flags:
    - addToPose : a                  (bool)          [create]
        Allows adding the selected items to the dagPose.
    
    - atPose : ap                    (bool)          [query]
        Query whether the hierarchy is at same position as the pose. Names of hierarchy
        members that are not at the pose position will be returned. An empty return list
        indicates that the hierarchy is at the pose.
    
    - bindPose : bp                  (bool)          [create,query]
        Used to specify the bindPose for the selected hierarchy. Each hierarchy can have
        only a single bindPose, which is saved automatically at the time of a skin bind.
        The bindPose is used when adding influence objects, binding new skins, or adding
        flexors. Take care when modifying the bindPose with the -rs/-reset or
        -rm/-remove flags, since if the bindPose is ill-defined it can cause problems
        with subsequent skinning operations.
    
    - g : g                          (bool)          [create]
        This flag can be used in conjunction with the restore flag to signal that the
        members of the pose should be restored to the global pose. The global pose means
        not only is each object locally oriented with respect to its parents, it is also
        in the same global position that it was at when the pose was saved. If a
        hierarchy's parenting has been changed since the time that the pose was saved,
        you may have trouble reaching the global pose.
    
    - members : m                    (bool)          [query]
        Query the members of the specified pose. The pose should be specified using the
        selection list, the -bp/-bindPose or the -n/-name flag.
    
    - name : n                       (unicode)       [create,query]
        Specify the name of the pose. This can be used during create, restore, reset,
        remove, and query operations to specify the pose to be created or acted upon.
    
    - remove : rm                    (bool)          [create]
        Remove the selected joints from the specified pose.
    
    - reset : rs                     (bool)          [create]
        Reset the pose on the selected joints. If you are resetting pose data for a
        bindPose, take care. It is appropriate to use the -rs/-reset flag if a joint has
        been reparented and/or appears to be exactly at the bindPose. However, a
        bindPose that is much different from the exact bindPose can cause problems with
        subsequent skinning operations.
    
    - restore : r                    (bool)          [create]
        Restore the hierarchy to a saved pose. To specify the pose, select the pose
        node, or use the -bp/-bindPose or -n/-name flag.
    
    - save : s                       (bool)          [create]
        Save a dagPose for the selected dag hierarchy. The name of the new pose will be
        returned.
    
    - selection : sl                 (bool)          [create,query]
        Whether or not to store a pose for all items in the hierarchy, or for only the
        selected items.
    
    - worldParent : wp               (bool)          [create]
        Indicates that the selected pose member should be recalculated as if it is
        parented to the world. This is typically used when you plan to reparent the
        object to world as the next operation.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.dagPose`
    """
    pass


def nonLinear(*args, **kwargs):
    """
    This command creates a functional deformer of the specified type that will
    deform the selected objects.  The deformer consists of three nodes: The deformer
    driver that gets connected to the history of the selected objects, the deformer
    handle transform that controls position and orientation of the axis of the
    deformation and the deformer handle that maintains the deformation parameters.
    The type of the deformer handle shape created depends on the specified type of
    the deformer.  The deformer handle will be positioned at the center of the
    selected objects' bounding box and oriented to match the orientation of the
    leading object in the selection list.  The deformer handle transform will be
    selected when the command is completed. The nonLinear command has some flags
    which are specific to the nonLinear type specified with the -type flag. The
    flags correspond to the primary keyable attributes related to the specific type
    of nonLinear node. For example, if the type is bend, then the flags -curvature,
    -lowBoundand -highBoundmay be used to initialize, edit or query those attribute
    values on the bend node. Examples of this are covered in the example section
    below.
    
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
    
    - autoParent : ap                (bool)          [create]
        Parents the deformer handle under the selected object's transform. This flag is
        valid only when a single object is selected.
    
    - before : bf                    (bool)          [create,edit]
        If the default behavior for insertion/appending into/onto the existing chain is
        not the desired behavior then this flag can be used to force the command to
        place the deformer node before the selected node in the chain even if a new
        geometry shape has to be created in order to do so. Works in create mode (and
        edit mode if the deformer has no geometry added yet).
    
    - commonParent : cp              (bool)          [create]
        Creates a new transform and parents the selected object and the deformer handle
        under it.  This flag is valid only when a single object is selected.
    
    - defaultScale : ds              (bool)          [create]
        Sets the scale of the deformation handle to 1.  By default the deformation
        handle is scaled to the match the largest dimension of the selected objects'
        bounding box. [deformerFlags] The attributes of the deformer handle shape can be
        set upon creation, edited and queried as normal flags using either the long or
        the short attribute name.  e.g.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - type : typ                     (unicode)       [create]
        Specifies the type of deformation. The current valid deformation types are:
        bend, twist, squash, flare, sine and wave                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.nonLinear`
    """
    pass


def blendTwoAttr(*args, **kwargs):
    """
    A blendTwoAttr nodes takes two inputs, and blends the values of the inputs from
    one to the other, into an output value. The blending of the two inputs uses a
    blending function, and the following formula: (1 - blendFunction) \* input[0]  +
    blendFunction \* input[1] The blendTwoAttr command can be used to blend the
    animation of an object to transition smoothly between the animation of two other
    objects. When the blendTwoAttr command is issued, it creates a blendTwoAttr node
    on the specified attributes, and reconnects whatever was previously connected to
    the attributes to the new blend nodes. You may also specify which two attributes
    should be used to blend together. The driver is used when you want to keyframe
    an object after it is being animated by a blend node. The current driver index
    specifies which of the two blended attributes should be keyframed.
    
    Flags:
    - attribute : at                 (unicode)       [create]
        A list of attributes for the selected nodes for which a blendTwoAttr node will
        be created.
    
    - attribute0 : at0               (PyNode)        [create,query,edit]
        The attribute that should be connected to the first input of the new
        blendTwoAttr node. When queried, it returns a string.
    
    - attribute1 : at1               (PyNode)        [create,query,edit]
        The attribute that should be connected to the second input of the new
        blendTwoAttr node. When queried, it returns a string.
    
    - blender : bl                   (PyNode)        [create,query,edit]
        The blender attribute. This is the attribute that will be connected to the newly
        created blendTwoAttr node(s) blender attribute. This attribute controls how much
        of each of the two attributes to use in the blend. If this flag is not
        specified, a new animation curve is created whose value goes from 1 to 0
        throughout the time range specified by the -t flag. If -t is not specified, an
        abrupt change from the value of the first to the value of the second attribute
        will occur at the current time when this command is issued.
    
    - controlPoints : cp             (bool)          [create]
        Explicitly specify whether or not to include the control points of a shape (see
        -sflag) in the list of attributes. Default: false.
    
    - driver : d                     (int)           [create,query,edit]
        The index of the driver attribute for this blend node (0 or 1) When queried, it
        returns an integer.
    
    - name : n                       (unicode)       [create,query]
        name for the new blend node(s)
    
    - shape : s                      (bool)          [create]
        Consider all attributes of shapes below transforms as well, except
        controlPoints. Default: true
    
    - time : t                       (timerange)     [create]
        The time range between which the blending between the 2 attributes should occur.
        If a single time is specified, then the blend will cause an abrupt change from
        the first to the second attribute at that time.  If a range is specified, a
        smooth blending will occur over that time range. The default is to make a sudden
        transition at the current time.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.blendTwoAttr`
    """
    pass


def controller(*args, **kwargs):
    """
    Commands for managing animation sources
    
    Flags:
    - allControllers : ac            (bool)          [create,query,edit]
        When this flag is queried, returns all dependNode attached to a controller in
        the scene.
    
    - children : cld                 (bool)          [query,edit]
        Return true if the specified dependNode is a controller.
    
    - group : g                      (bool)          [create,query,edit]
        Create a controller that is not associated with any object. This new controller
        will be the parent of all the selected objects.
    
    - index : idx                    (int)           [query,edit]
        In query mode, returns the index of the controller in the parent controller's
        list of children. In edit mode, reorder the parent controller's children
        connections so that the current controller is assigned the given index.
    
    - isController : ic              (unicode)       [create,query,edit]
        Returns true if the specified dependNode is a controller.
    
    - parent : p                     (bool)          [create,query,edit]
        Set or query the parent controller of the selected controller node.
    
    - pickWalkDown : pwd             (bool)          [query,edit]
        Return the first child.
    
    - pickWalkLeft : pwl             (bool)          [query,edit]
        Return the previous sibling.
    
    - pickWalkRight : pwr            (bool)          [query,edit]
        Return the next sibling.
    
    - pickWalkUp : pwu               (bool)          [query,edit]
        Return the parent.
    
    - unparent : unp                 (bool)          [query,edit]
        Unparent all selected controller objects from their respective parent.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.controller`
    """
    pass


def _ikHandle(*args, **kwargs):
    """
    Modifications:
        - always converts to PyNodes in create mode, even though results are
          non-unique short names
    """
    pass


def timeEditorClip(*args, **kwargs):
    """
    This command edits/queries Time Editor clips.
    
    Flags:
    - absolute : abs                 (bool)          [query]
        This flag is used in conjunction with other timing flags like -s/start,
        -d/duration, -ed/end, etc. to query (global) absolute time.
    
    - addAttribute : aa              (unicode)       [edit]
        Add new attribute to the clip.
    
    - addObjects : ao                (unicode)       [create,query,edit]
        Populate the given object(s) and their attributes to anim source to Time Editor.
        For multiple object, pass each name separated by semicolon. In query mode,
        return the number of attributes that will be populated given the flags, along
        with the animation's first and last frames for the given object(s). Similar to
        -addSelectedObjectsflag but acts on given object(s) instead. This flag will
        override the flag -addSelectedObjects.
    
    - addRelatedKG : akg             (bool)          [create,query,edit]
        During population, determine if associated keying groups should be populated or
        not. Normally used for populating HIK. By default the value is false.
    
    - addSelectedObjects : aso       (bool)          [create,query,edit]
        Populate the currently selected objects and their attributes to anim source or
        Time Editor. In query mode, return the number of attributes that will be
        populated given the flags, along with the animation's first and last frames.
    
    - allowShrinking : eas           (bool)          [edit]
        When extending clip, allow shrinking.
    
    - animSource : asr               (unicode)       [create,query,edit]
        Populate based on animation source.
    
    - attribute : at                 (unicode)       [create,edit]
        Populate a specific attribute on a object.
    
    - audio : au                     (unicode)       [create]
        Create a clip with audio inside.
    
    - children : chl                 (int)           [query]
        Get children clip IDs.
    
    - clipAfter : ca                 (bool)          [query]
        Get the clip ID of the next clip.
    
    - clipBefore : cb                (bool)          [query]
        Get the clip ID of the previous clip.
    
    - clipDataType : cdt             (bool)          [query]
        Query the type of data being driven by the given clip ID. Return values are: 0 :
        Animation       - Clip drives animation curves1 : Audio           - Clip drives
        audio3 : Group           - Clip is a group
    
    - clipId : id                    (int)           [create,edit]
        ID of the clip to be edited.
    
    - clipIdFromNodeName : idn       (int)           [query]
        Get clip ID from clip node name.
    
    - clipIdFromPath : idp           (bool)          [query]
        Flag for querying the clip ID given the path. Clip path is a vertical-bar-
        delimited string to indicate a hierarchical structure of a clip. Please refer to
        the hierarchical path in outliner to see how it is represented. For example:
        composition1|track1|clip1 Note: To specify the path, this flag must appear
        before -query flag.
    
    - clipNode : cln                 (bool)          [query]
        Flag for querying the name of the clip node.
    
    - clipPath : clp                 (bool)          [query]
        Flag for querying the path given the clip ID. Clip path is a vertical bar
        delimited string to indicate a hierarchical structure of a clip. Please refer to
        the hierarchical path in outliner to see how it is represented. For example:
        composition1|track1|clip1. Note: If the clip is not connected to any track, it
        will return empty string.
    
    - copyClip : ccl                 (bool)          [edit]
        Get the selected clip IDs and store them in a list that could be used for
        pasting.
    
    - crossfadeMode : cfm            (int)           [query,edit]
        Set the crossfading mode between two clips that lie on the same track, and that
        are specified with the -clipId flags: 0 : linear          - Two clips are
        blended with a constant ratio1 : step            - Left clip keeps its value
        until the middle of the crossfading region and then right clip's value is used2
        : hold left       - Use only left clip's value3 : hold right      - Use only
        right clip's value4 : custom          - User defined crossfade curve5 : custom
        (spline) - User defined crossfade curve with spline preset
    
    - crossfadePlug : cfp            (bool)          [query]
        Get plug path for a custom crossfade curve between 2 clips.
    
    - curveTime : cvt                (time)          [query]
        Query the curve local time in relation to the given clip.
    
    - defaultGhostRoot : dgr         (bool)          [query,edit]
        Edit or query default ghost root variable. Determine whether to use the default
        ghost root (object driven by clip).
    
    - drivenAttributes : dat         (bool)          [query]
        Return a list of attributes driven by a clip.
    
    - drivenClipsBySource : dcs      (unicode)       [query]
        Returns the clips driven by the given source. Can filter the return result by
        the specified type, like animCurve, expression, constraint, etc. This flag must
        come before the -query flag.
    
    - drivenObjects : dos            (bool)          [query]
        Return an array of strings consisting of the names of all objects driven by the
        current clip and its children clips.
    
    - drivenRootObjects : dro        (bool)          [query]
        Return an array of strings consisting of the names of all root objects driven by
        this clip and its children clips.
    
    - drivingSources : dsc           (unicode)       [query]
        Return all sources driving the given clip. Can filter the return result by the
        specified type, like animCurve, expression, constraint, etc. If used after the
        -query flag (without an argument), the command returns all sources driving the
        given clip. To specify the type, this flag must appear before the -query flag.
        In query mode, this flag can accept a value.
    
    - duplicateClip : dcl            (bool)          [edit]
        Duplicate clip into two clips with the same timing info.
    
    - duration : d                   (time)          [create,query]
        Relative duration of the new clip.
    
    - emptySource : ems              (bool)          [create]
        Create a clip with an empty source.
    
    - endTime : et                   (time)          [query]
        Query the relative end time of the clip.
    
    - exclusive : exc                (bool)          [create,edit]
        Populate all types of animation sources which are not listed by typeFlag.
    
    - existingOnly : exo             (bool)          [edit]
        This flag can only be used in edit mode, in conjunction with the animSource
        flag. Retain the animSource flag functionality but only bind attributes that are
        already part of the clip. It does not attempt to populate unbound source
        attributes to their default destination.
    
    - exists : exs                   (bool)          [query]
        Return true if the specified clip exists.
    
    - explode : epl                  (int)           [edit]
        Reparent all tracks and their clips within a group out to its parent track node
        and remove the group.
    
    - exportAllClips : eac           (bool)          [edit]
        When used with the ef/exportFbxflag, export all clips.
    
    - exportFbx : ef                 (unicode)       [edit]
        Export currently selected clips to FBX files.
    
    - extend : ex                    (bool)          [edit]
        Extend the clip to encompass all children.
    
    - extendParent : exp             (bool)          [edit]
        Extend parent to fit this clip.
    
    - ghost : gh                     (bool)          [query,edit]
        Enable/disable ghosting for the specified clip.
    
    - ghostRootAdd : gra             (unicode)       [edit]
        Add path to specified node as a custom ghost root.
    
    - ghostRootRemove : grr          (unicode)       [edit]
        Remove path to specified node as a custom ghost root.
    
    - group : grp                    (bool)          [create]
        Specify if the new container should be created as a group, containing other
        specified clips.
    
    - holdEnd : he                   (time)          [query,edit]
        Hold clip's end to time.
    
    - holdStart : hs                 (time)          [query,edit]
        Hold clip's start to time.
    
    - importAllFbxTakes : aft        (bool)          [create]
        Import all FBX takes into the new anim sources (for timeEditorAnimSource
        command) or new containers (for timeEditorClip command).
    
    - importFbx : fbx                (unicode)       [create]
        Import an animation from FBX file into the new anim source (for
        timeEditorAnimSource command) or new container (for timeEditorClip command).
    
    - importFbxTakes : ft            (unicode)       [create]
        Import multiple FBX takes (separated by semicolons) into the new anim sources
        (for timeEditorAnimSource command) or new containers (for timeEditorClip
        command).
    
    - importMayaFile : mf            (unicode)       [create]
        Import an animation from Maya file into the new anim sources (for
        timeEditorAnimSource command) or new containers (for timeEditorClip command).
    
    - importOption : io              (unicode)       [edit]
        Option for importing animation source. Specify either 'connect' or 'generate'.
        connect:  Only connect with nodes already existing in the scene.
        Importing an animation source that does not match with any element
        of the current scene will not create any clip.                   (connect is the
        default mode). generate: Import everything and generate new nodes for items not
        existing in the scene.
    
    - importPopulateOption : ipo     (unicode)       [edit]
        Option for population when importing.
    
    - importTakeDestination : itd    (int)           [create]
        Specify how to organize imported FBX takes: 0 - Import takes into a group
        (default) 1 - Import takes into multiple compositions 2 - Import takes as a
        sequence of clips
    
    - importedContainerNames : icn   (unicode)       [create]
        Internal use only. To be used along with populateImportedAnimSourcesto specify
        names for the created containers.
    
    - includeRoot : irt              (bool)          [create,edit]
        Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.
    
    - isContainer : ict              (bool)          [query]
        Indicate if given clip ID is a container.
    
    - listUserGhostRoot : lug        (bool)          [query]
        Get user defined ghost root object for indicated clips.
    
    - loopEnd : le                   (time)          [query,edit]
        Loop clip's end to time.
    
    - loopStart : ls                 (time)          [query,edit]
        Loop clip's start to time.
    
    - minClipDuration : mcd          (bool)          [query]
        Returns the minimum allowed clip duration.
    
    - modifyAnimSource : mas         (bool)          [create,edit]
        When populating, automatically modify Anim Source without asking the user.
    
    - moveClip : mcl                 (time)          [edit]
        Move clip by adding delta to its start time.
    
    - mute : m                       (bool)          [query,edit]
        Mute/Unmute the clip given a clip ID. In query mode, return the muted state of
        the clip. Clips muted by soloing are not affected by this flag.
    
    - name : n                       (unicode)       [query,edit]
        Name of the clip. A clip will never have an empty name. If an empty string is
        provided, it will be replaced with _.
    
    - parent : p                     (int)           [edit]
        Specify group/object parent ID.
    
    - parentClipId : pid             (int)           [create,query]
        Specify the parent clip ID of a clip to be created.
    
    - parentGroupId : pgd            (bool)          [query]
        Return the parent group ID of the given clip.
    
    - pasteClip : pcl                (time)          [edit]
        Paste clip to the given time and track. Destination track is required to be
        specified through the track flag in the format tracksNode:trackIndex. A
        trackIndex of -1 indicates that a new track will be created.
    
    - path : pt                      (unicode)       [edit]
        Full path of the clip to be edited. For example: composition1|track1|clip1. In
        query mode, this flag can accept a value.
    
    - populateImportedAnimSources : pia (unicode)       [create]
        Internal use only. Populate the Time Editor with clips using the Animation
        Sources specified (use ; as a delimiter for multiple anim sources).
    
    - poseClip : poc                 (bool)          [create]
        Populate as pose clip with current attribute values.
    
    - preserveAnimationTiming : pat  (bool)          [create]
        When used with the population command, it ensures the animation is offset within
        a clip in such way that it matches its original scene timing, regardless of the
        new clip's position.
    
    - razorClip : rcl                (time)          [edit]
        Razor clip into two clips at the specified time.
    
    - recursively : rec              (bool)          [create,edit]
        Populate selection recursively, adding all the children.
    
    - remap : rmp                    (unicode, unicode) [edit]
        Change animation source for a given clip item to a new one, specified by the
        target path. This removes all clips for the roster item and creates new clips
        from the Anim Source for the new target path.
    
    - remapSource : rs               (unicode, unicode) [edit]
        Set animation source to be remapped for a given clip item to new one, specified
        by the target path.
    
    - remappedSourceAttrs : rms      (bool)          [query]
        Return an array of attribute indices and names of the source attributes of a
        remapped clip.
    
    - remappedTargetAttrs : rmt      (bool)          [query]
        Return an array of attribute indices and names of the target attributes of a
        remapped clip.
    
    - removeAttribute : ra           (unicode)       [edit]
        Remove attribute from the clip.
    
    - removeClip : rmc               (bool)          [edit]
        Remove clip of specified ID.
    
    - removeCrossfade : rcf          (bool)          [edit]
        Remove custom crossfade between two clips specified by -clipId flags.
    
    - removeSceneAnimation : rsa     (bool)          [create,edit]
        If true, remove animation from scene when creating clips or anim sources. Only
        Time Editor will drive the removed scene animation.
    
    - removeWeightCurve : rwc        (bool)          [create,query,edit]
        Remove the weight curve connected to the clip.
    
    - resetTiming : rt               (bool)          [edit]
        Reset start and duration of a clip with the given clip ID to the values stored
        in its Anim Source.
    
    - resetTransition : rtr          (bool)          [edit]
        Reset transition intervals between specified clips.
    
    - ripple : rpl                   (bool)          [edit]
        Apply rippling to a clip operation.
    
    - rootClipId : rti               (int)           [edit]
        ID of the root clip. It is used together with various clip editing flags. When
        used, the effect of clip editing and its parameters will be affected by the
        given root clip. For example, moving a clip under the group root (usually in
        group tab view) will be performed in the local time space of the group root.
    
    - rootPath : rpt                 (unicode)       [edit]
        Path of the root clip. It is used together with various clip editing flags. When
        used, the effect of clip editing and its parameters will be affected by the
        given root clip. For example, moving a clip under the group root (usually in
        group tab view) will be performed in the local time space of the group root.
    
    - scaleEnd : sce                 (time)          [edit]
        Scale the end time of the clip to the given time.
    
    - scalePivot : scp               (time)          [edit]
        Scale the time of the clip based on the pivot. This should be used together with
        -scs/scaleStartor -sce/scaleEnd.
    
    - scaleStart : scs               (time)          [edit]
        Scale the start time of the clip to the given time.
    
    - setKeyframe : k                (unicode)       [edit]
        Set keyframe on a specific clip for a specified attribute.
    
    - showAnimSourceRemapping : sar  (bool)          [create]
        Show a remapping dialog when the imported anim source attributes do not match
        the scene attributes.
    
    - speedRamping : src             (int)           [query,edit]
        To control the playback speed of the clip by animation curve: 1 : create -
        Attach a speed curve and a time warp curve to the clip to control the playback
        speed2 : edit - Open the Graph editor to edit the speed curve3 : enable - Create
        a time warp curve from current speed curve and attach to clip4 : disable -
        Remove the time warp curve from clip5 : delete - Delete the attached speed curve
        and time warp curve6 : reset - Reset the speed curve back to the default7 :
        convert to speed curve from time warp8 : convert to time warp from speed curveIn
        query mode, return true if a speed curve is attached to the clip.
    
    - startTime : s                  (time)          [create,query]
        Relative start time of the new clip.
    
    - takeList : tl                  (unicode)       [create]
        Internal use only. To be used along with populateImportedAnimSourcesto specify
        the imported take names.
    
    - takesToImport : toi            (unicode)       [create]
        Internal use only. To be used along with populateImportedAnimSourcesto specify
        the imported take indices.
    
    - timeWarp : tw                  (bool)          [query]
        Return true if the clip is being warped by the speed curve. If no speed curve is
        attached to the clip, it will always return false.
    
    - timeWarpCurve : twc            (bool)          [query]
        Returns the name of the time warp curve connected to the clip.
    
    - timeWarpType : twt             (int)           [query,edit]
        Time warp mode: 0: remapping - Connected time warp curve performs frame by frame
        remapping1: speed curve - Connected time warp curve acts as a speed curveIn
        query mode, return time warp mode of a clip.
    
    - track : trk                    (unicode)       [create,query,edit]
        The new clip container will be created on the track in the format
        trackNode:trackNumber, or on a track path, for example composition1|track1. In
        query mode, return a string containing the track number and tracks node of the
        given clip ID. In create mode, if the track number is '-1' or not given at all,
        then a new track will be created. For example: trackNode:-1; composition1|.
    
    - tracksNode : trn               (bool)          [query]
        Get tracks node if specified clip is a group clip.
    
    - transition : tra               (bool)          [edit]
        Create transition intervals between specified clips.
    
    - trimEnd : tre                  (time)          [edit]
        Trim the end time of the clip to the given time.
    
    - trimStart : trs                (time)          [edit]
        Trim the start time of the clip to the given time.
    
    - truncated : trc                (bool)          [query]
        This flag is used in conjunction with other timing flags like -s/start,
        -d/duration, -ed/end, etc. to query (global) truncated time.
    
    - type : typ                     (unicode)       [create,query,edit]
        Only populate the specified type of animation source.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - uniqueAnimSource : uas         (bool)          [edit]
        If a given clip is sharing its Anim Source node with another clip, make the Anim
        Source of this clip unique.
    
    - userGhostRoot : ugr            (bool)          [query,edit]
        Edit or query custom ghost root variable. Determine whether to use user defined
        ghost root.
    
    - weightCurve : wc               (bool)          [create,query,edit]
        In edit mode, create a weight curve and connect it to the clip. In query mode,
        return the name of the weight curve connected to the clip.
    
    - zeroKeying : zk                (bool)          [edit]
        A toggle flag to use in conjunction with k/setKeyframe, set the value of the key
        frame(s) to be keyed to zero.
    
    
    Derived from mel command `maya.cmds.timeEditorClip`
    """
    pass


def _aimConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def geomBind(*args, **kwargs):
    """
    This command is used to compute weights using geodesic voxel binding algorithm.
    It works by setting the right weights values on an already-existing skinCluster
    node.            In query mode, return type is based on queried flag.
    
    Flags:
    - bindMethod : bm                (int)           [create]
        Specifies which bind algorithm to use. By default, Geodesic Voxel will be used.
        Available algorithms are: 3 - Geodesic Voxel
    
    - falloff : fo                   (float)         [create,query,edit]
        Falloff controlling the bind stiffness. Valid values range from [0..1].
    
    - geodesicVoxelParams : gvp      (int, bool)     [create,query,edit]
        Specifies the geodesic voxel binding parameters. This flag is composed of three
        parameters: 0 - Maximum voxel grid resolution which must be a power of two. (ie.
        64, 128, 256, etc. ) 1 - Performs a post voxel state validation when enabled.
        Default values are 256 true.
    
    - maxInfluences : mi             (int)           [create,query,edit]
        Specifies the maximum influences a vertex can have. By default, all influences
        are used (-1).                              Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.geomBind`
    """
    pass


def lattice(*args, **kwargs):
    """
    This command creates a lattice deformer that will deform the selected objects.
    If the object centered flag is used, the initial lattice will fit around the
    selected objects. The lattice will be selected when the command is completed.
    The lattice deformer has an associated base lattice. Only objects which are
    contained by the base lattice will be deformed by the lattice.
    
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
    
    - commonParent : cp              (bool)          [create]
        Group the base lattice and the deformed lattice under a common transform. This
        means that you can resize the lattice without affecting the deformation by
        resizing the common transform.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - divisions : dv                 (int, int, int) [create,query,edit]
        Set the number of lattice slices in x, y, z. Default is 2, 5, 2. When queried,
        this flag returns float float float. When you change the number of divisions,
        any tweaking or animation of lattice points must be redone.
    
    - dualBase : db                  (bool)          [create]
        Create a special purpose ffd deformer node which accepts 2 base lattices. The
        default is off which results in the creation of a normal ffd deformer node.
        Intended for internal usage only.
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
    - freezeMapping : fm             (bool)          [create,query,edit]
        The base position of the geometries points is fixed at the time this flag is
        set.  When mapping is frozen, moving the geometry with respect to the lattice
        will not cause the deformation to be recomputed.
    
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
    
    - latticeReset : lr              (bool)          [edit]
        Reset the lattice to match its base position. This will undo any deformations
        that the lattice is causing. The lattice will only deform points that are
        enclosed within the lattice's reset (base) position.
    
    - ldivisions : ldv               (int, int, int) [create,query,edit]
        Set the number of local lattice slices in x, y, z.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - objectCentered : oc            (bool)          [create]
        Centers the lattice around the selected object(s) or components. Default is off
        which centers the lattice at the origin.
    
    - outsideFalloffDistance : ofd   (float)         [create]
        Set the falloff distance used when the setting for transforming points outside
        of the base lattice is set to 2. The distance value is a positive number which
        specifies the size of the falloff distance as a multiple of the base lattice
        size, thus a value of 1.0 specifies that only points up to the base lattice
        width/height/depth away are transformed. A value of 0.0 is equivalent to an
        outsideLattice value of 0 (i.e. no points outside the base lattice are
        transformed). A huge value is equivalent to transforming an outsideLattice value
        of 1 (i.e. all points are transformed).
    
    - outsideLattice : ol            (int)           [create]
        Set the mode describing how points outside the base lattice are transformed. 0
        (the default) specifies that no outside points are transformed. 1 specifies that
        all outside points are transformed, and 2 specifies that only those outside
        points which fall within the falloff distance(see the
        -ofd/outsideFalloffDistance flag) are transformed. When querying, the current
        setting for the lattice is returned.
    
    - parallel : par                 (bool)          [create,edit]
        Inserts the new deformer in a parallel chain to any existing deformers in the
        history of the object. A blendShape is inserted to blend the parallel results
        together. Works in create mode (and edit mode if the deformer has no geometry
        added yet).
    
    - position : pos                 (float, float, float) [create]
        Used to specify the position of the newly created lattice.
    
    - prune : pr                     (bool)          [edit]
        Removes any points not being deformed by the deformer in its current
        configuration from the deformer set.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - removeTweaks : rt              (bool)          [edit]
        Remove any lattice deformations caused by moving lattice points.
        Translations/rotations and scales on the lattice itself are not removed.
    
    - rotation : ro                  (float, float, float) [create]
        Used to specify the initial rotation of the newly created lattice.
    
    - scale : s                      (float, float, float) [create]
        Used to specify the initial scale of the newly created lattice.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.lattice`
    """
    pass


def choice(*args, **kwargs):
    """
    The choice command provides a mechanism for changing the inputs to an attribute
    based on some (usually time-based) criteria. For example, an object could be
    animated from frames 1 to 30 by a motion path, then from frames 30 to 50 it
    follows keyframe animation, and after frame 50 it returns to the motion path.
    Or, a revolve surface could change its input curve depending on some transform's
    rotation value.The choice command creates a choice node (if one does not already
    exist) on all specified attributes of the selected objects. If the attribute was
    already connected to something, that something is now reconnected to the i'th
    index of the choice node's input (or the next available input if the -in/index
    flag is not specified). If a source attribute is specified, then that attribute
    is connected to the choice node's i'th input instead.The choice node operates by
    using the value of its selector attribute to determine which of its input
    attributes to pass through to its output. The input attributes can be of any
    type. For example, if the selector attribute was connected by an animation curve
    with keyframes at (1,1), (30,2) and (50,1), then that would mean that the choice
    node would pass on the data from input[1] from time 1 to 30, and after time 50,
    and the data from input[2] between times 30 and 50.This command returns the
    names of the created or modified choice nodes, and if a keyframe was added to
    the animation curve, it specifies the index (or value on the animation curve).
    
    Flags:
    - attribute : at                 (unicode)       [create]
        specifies the attributes onto which choice node(s) should be created. The
        default is all keyable attributes of the given objects. Note that although this
        flag is not queryable, it can be used to qualify which attributes of the given
        objects to query.
    
    - controlPoints : cp             (bool)          [create]
        Explicitly specify whether or not to include the control points of a shape (see
        -sflag) in the list of attributes. Default: false.
    
    - index : index                  (int)           [create,query]
        specifies the multi-input index of the choice node to connect the source
        attribute to. When queried, returns a list of integers one per specified -t/time
        that indicates the multi-index of the choice node to use at that time.
    
    - name : n                       (unicode)       [create,query]
        the name to give to any newly created choice node(s). When queried, returns a
        list of strings.
    
    - selector : sl                  (PyNode)        [create,query]
        specifies the attribute to be used as the choice node's selector. The value of
        the selector at a given time determines which of the choice node's multi-indices
        should be used as the output of the choice node at that time. This flag is only
        editable (it cannot be specified at creation time). When queried, returns a list
        of strings.
    
    - shape : s                      (bool)          [create]
        Consider all attributes of shapes below transforms as well, except
        controlPoints. Default: true
    
    - sourceAttribute : sa           (PyNode)        [create]
        specifies the attribute to connect to the choice node that will be selected at
        the given time(s) specified by -t/time.
    
    - time : t                       (time)          [create]
        specifies the time at which the choice should use the given source attribute, or
        the currently connected attribute if source attribute is not specified. The
        default is the curren time. Note that although this flag is not queryable, it
        can be used to qualify the times at which to query the other attributes.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.choice`
    """
    pass


def scaleConstraint(*args, **kwargs):
    """
    Constrain an object's scale to the scale of the target object or to the average
    scale of a number of targets. A scaleConstraint takes as input one or more
    targetDAG transform nodes to which to scale the single constraint objectDAG
    transform node.  The scaleConstraint scales the constrained object at the
    weighted geometric mean of the world space target scale factors.
    
    Flags:
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - maintainOffset : mo            (bool)          [create]
        The offset necessary to preserve the constrained object's initial scale will be
        calculated and used as the offset.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - offset : o                     (float, float, float) [create,query,edit]
        Sets or queries the value of the offset. Default is 1,1,1.
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - scaleCompensate : sc           (bool)          [create,edit]
        Used only when constraining a joint. It specify if a scaleCompensate will be
        applied on constrained joint. If true it will connect
        Tjoint.aCompensateForParentScale to scaleContraint.aConstraintScaleCompensate.
    
    - skip : sk                      (unicode)       [create,edit]
        Specify the axis to be skipped. Valid values are x, y, zand none. During
        creation, noneis the default. This flag is multi-use.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.scaleConstraint`
    """
    pass


def orientConstraint(*args, **kwargs):
    """
    Constrain an object's orientation to match the orientation of the target or the
    average of a number of targets. An orientConstraint takes as input one or more
    targetDAG transform nodes to control the orientation of the single constraint
    objectDAG transform  The orientConstraint orients the constrained object to
    match the weighted average of the target world space orientations.
    
    Flags:
    - createCache : cc               (float, float)  [edit]
        This flag is used to generate an animation curve that serves as a cache for the
        constraint. The two arguments define the start and end frames.  The cache is
        useful if the constraint has multiple targets and the constraint's interpolation
        type is set to no flip. The no flipmode prevents flipping during playback, but
        the result is dependent on the previous frame.  Therefore in order to
        consistently get the same result on a specific frame, a cache must be generated.
        This flag creates the cache and sets the constraint's interpolation type to
        cache. If a cache exists already, it will be deleted and replaced with a new
        cache.
    
    - deleteCache : dc               (bool)          [edit]
        Delete an existing interpolation cache.
    
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - maintainOffset : mo            (bool)          [create]
        The offset necessary to preserve the constrained object's initial orientation
        will be calculated and used as the offset.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - offset : o                     (float, float, float) [create,query,edit]
        Sets or queries the value of the offset. Default is 0,0,0.
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - skip : sk                      (unicode)       [create,edit]
        Specify the axis to be skipped. Valid values are x, y, zand none. The default
        value in create mode is none. This flag is multi-use.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.orientConstraint`
    """
    pass


def cutKey(*args, **kwargs):
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
    list or range (see Examples). The cutKey command cuts curve segment hierarchies
    from specified targets and puts them in the clipboard.  The pasteKey command
    applies these curves to other objects.The shape of the cut curve placed in the
    clipboard, and the effect of the cutKey command on the source animation curve
    depends on the cutKey -optionspecified.  Each of these options below will be
    explained using an example.  For all the explanations, let us assume that the
    source animation curve (from which keys will be cut) has 5 keyframes at times
    10, 15, 20, 25, and 30.TbaseKeySetCmd.h cutKey -t 12:22-option keysKeyframes at
    times 15 and 20 are removed. All other keys are unchanged.A 5-frame animation
    curve is placed into the keyset clipboard.cutKey -t 12:22-option
    keysCollapseKeyframes at times 15 and 20 are removed.  Shift all keys after time
    20 to the left by 5 frames, preserving all their values.A 5-frame animation
    curve is placed into the keyset clipboard.cutKey -t 12:22-option
    keysConnectKeyframes at times 15 and 20 are removed.  Shift all keys after time
    20 to the left by 5 frames, and place the key that used to be at time 25 at the
    value of the key that used to be at time 15.A 5-frame animation curve is placed
    into the keyset clipboard.cutKey -t 12:22-option curveKeyframes at times 15 and
    20 are removed.  Keys are inserted at times 12 and 22.A 10-frame animation curve
    is placed into the keyset clipboard.cutKey -t 12:22-option
    curveCollapseKeyframes at times 15 and 20 are removed.  Keys are inserted at
    times 12 and 22.  Shift all keys from time 22 to the left by 10 frames,
    preserving their values.A 10-frame animation curve is placed into the keyset
    clipboard.cutKey -t 12:22-option curveConnectKeyframes at times 15 and 20 are
    removed.  Keys are inserted at times 12 and 22.  Shift all keys from time 22 to
    the left by 10 frames, and replace the key inserted at time 12 with the newly
    inserted key at time 22.A 10-frame animation curve is placed into the keyset
    clipboard.cutKey -t 12:22-option areaCollapseKeyframes at times 15 and 20 are
    removed. Shift all keys from time 22 to the left by 10 frames, preserving their
    values.A 10-frame animation curve is placed into the keyset clipboard.
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - clear : cl                     (bool)          [create]
        Just remove the keyframes (i.e. do not overwrite the clipboard)
    
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
    
    - option : o                     (unicode)       [create]
        Option for how to perform the cutKey operation.  Valid values for this flag are
        keys, curve, curveCollapse, curveConnect, areaCollapse.  The default cut option
        is: keys
    
    - selectKey : sl                 (bool)          [create]
        Select the keyframes of curves which have had keys removed
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.cutKey`
    """
    pass


def keyframeStats(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting
    at column 1.  The layout of each control (ie. column) can be customized using
    the -cw/columnWidth, -co/columnOffset, -cat/columnAttach, -cal/columnAlign, and
    -adj/adjustableColumnflags.  By default, columns are left aligned with no offset
    and are 100 pixels wide.  Only one column in any group can be adjustable. This
    command creates, edits, queries a keyframe stats control.
    
    Flags:
    - adjustableColumn : adj         (int)           [create,edit]
        Specifies which column has an adjustable size that changes with the sizing of
        the layout.  The column value is a 1-based index. Passing 0 as argument turns
        off the previous adjustable column.
    
    - adjustableColumn2 : ad2        (int)           [create,edit]
        Specifies which column has an adjustable size that changes with the size of the
        parent layout. Ignored if there are not exactly two columns.
    
    - adjustableColumn3 : ad3        (int)           [create,edit]
        Specifies that the column has an adjustable size that changes with the size of
        the parent layout. Ignored if there are not exactly three columns.
    
    - adjustableColumn4 : ad4        (int)           [create,edit]
        Specifies which column has an adjustable size that changes with the size of the
        parent layout. Ignored if there are not exactly four columns.
    
    - adjustableColumn5 : ad5        (int)           [create,edit]
        Specifies which column has an adjustable size that changes with the size of the
        parent layout. Ignored if there are not exactly five columns.
    
    - adjustableColumn6 : ad6        (int)           [create,edit]
        Specifies which column has an adjustable size that changes with the size of the
        parent layout. Ignored if there are not exactly six columns.
    
    - animEditor : ae                (unicode)       [query,edit]
        The name of the animation editor which is associated with the control
    
    - annotation : ann               (unicode)       [create,query,edit]
        Annotate the control with an extra string value.
    
    - backgroundColor : bgc          (float, float, float) [create,query,edit]
        The background color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0. When
        setting backgroundColor, the background is automatically enabled, unless
        enableBackground is also specified with a false value.
    
    - classicMode : cm               (bool)          [query,edit]
        Edit display mode. True means stats only, otherwise show time value.
    
    - columnAlign : cal              (int, unicode)  [create,edit]
        Arguments are : column number, alignment type. Possible alignments are: left |
        right | center. Specifies alignment type for the specified column.
    
    - columnAlign2 : cl2             (unicode, unicode) [create,edit]
        Sets the text alignment of both columns.  Ignored if there are not exactly two
        columns. Valid values are left, right, and center.
    
    - columnAlign3 : cl3             (unicode, unicode, unicode) [create,edit]
        Sets the text alignment for all three columns.  Ignored if there are not exactly
        three columns. Valid values are left, right, and center.
    
    - columnAlign4 : cl4             (unicode, unicode, unicode, unicode) [create,edit]
        Sets the text alignment for all four columns.  Ignored if there are not exactly
        four columns. Valid values are left, right, and center.
    
    - columnAlign5 : cl5             (unicode, unicode, unicode, unicode, unicode) [create,edit]
        Sets the text alignment for all five columns.  Ignored if there are not exactly
        five columns. Valid values are left, right, and center.
    
    - columnAlign6 : cl6             (unicode, unicode, unicode, unicode, unicode, unicode) [create,edit]
        Sets the text alignment for all six columns.  Ignored if there are not exactly
        six columns. Valid values are left, right, and center.
    
    - columnAttach : cat             (int, unicode, int) [create,edit]
        Arguments are : column number, attachment type, and offset. Possible attachments
        are: left | right | both. Specifies column attachment types and offets.
    
    - columnAttach2 : ct2            (unicode, unicode) [create,edit]
        Sets the attachment type of both columns. Ignored if there are not exactly two
        columns. Valid values are left, right, and both.
    
    - columnAttach3 : ct3            (unicode, unicode, unicode) [create,edit]
        Sets the attachment type for all three columns. Ignored if there are not exactly
        three columns. Valid values are left, right, and both.
    
    - columnAttach4 : ct4            (unicode, unicode, unicode, unicode) [create,edit]
        Sets the attachment type for all four columns. Ignored if there are not exactly
        four columns. Valid values are left, right, and both.
    
    - columnAttach5 : ct5            (unicode, unicode, unicode, unicode, unicode) [create,edit]
        Sets the attachment type for all five columns. Ignored if there are not exactly
        five columns. Valid values are left, right, and both.
    
    - columnAttach6 : ct6            (unicode, unicode, unicode, unicode, unicode, unicode) [create,edit]
        Sets the attachment type for all six columns. Ignored if there are not exactly
        six columns. Valid values are left, right, and both.
    
    - columnOffset2 : co2            (int, int)      [create,edit]
        This flag is used in conjunction with the -columnAttach2 flag.  If that flag is
        not used then this flag will be ignored.  It sets the offset for the two
        columns.  The offsets applied are based on the attachments specified with the
        -columnAttach2 flag.  Ignored if there are not exactly two columns.
    
    - columnOffset3 : co3            (int, int, int) [create,edit]
        This flag is used in conjunction with the -columnAttach3 flag.  If that flag is
        not used then this flag will be ignored.  It sets the offset for the three
        columns.  The offsets applied are based on the attachments specified with the
        -columnAttach3 flag.  Ignored if there are not exactly three columns.
    
    - columnOffset4 : co4            (int, int, int, int) [create,edit]
        This flag is used in conjunction with the -columnAttach4 flag.  If that flag is
        not used then this flag will be ignored.  It sets the offset for the four
        columns.  The offsets applied are based on the attachments specified with the
        -columnAttach4 flag.  Ignored if there are not exactly four columns.
    
    - columnOffset5 : co5            (int, int, int, int, int) [create,edit]
        This flag is used in conjunction with the -columnAttach5 flag.  If that flag is
        not used then this flag will be ignored.  It sets the offset for the five
        columns.  The offsets applied are based on the attachments specified with the
        -columnAttach5 flag.  Ignored if there are not exactly five columns.
    
    - columnOffset6 : co6            (int, int, int, int, int, int) [create,edit]
        This flag is used in conjunction with the -columnAttach6 flag.  If that flag is
        not used then this flag will be ignored.  It sets the offset for the six
        columns.  The offsets applied are based on the attachments specified with the
        -columnAttach6 flag.  Ignored if there are not exactly six columns.
    
    - columnWidth : cw               (int, int)      [create,edit]
        Arguments are : column number, column width. Sets the width of the specified
        column where the first parameter specifies the column (1 based index) and the
        second parameter specifies the width.
    
    - columnWidth1 : cw1             (int)           [create,edit]
        Sets the width of the first column. Ignored if there is not exactly one column.
    
    - columnWidth2 : cw2             (int, int)      [create,edit]
        Sets the column widths of both columns. Ignored if there are not exactly two
        columns.
    
    - columnWidth3 : cw3             (int, int, int) [create,edit]
        Sets the column widths for all 3 columns. Ignored if there are not exactly 3
        columns.
    
    - columnWidth4 : cw4             (int, int, int, int) [create,edit]
        Sets the column widths for all 4 columns. Ignored if there are not exactly 4
        columns.
    
    - columnWidth5 : cw5             (int, int, int, int, int) [create,edit]
        Sets the column widths for all 5 columns. Ignored if there are not exactly 5
        columns.
    
    - columnWidth6 : cw6             (int, int, int, int, int, int) [create,edit]
        Sets the column widths for all 6 columns. Ignored if there are not exactly 6
        columns.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Add a documentation flag to the control.  The documentation flag has a directory
        structure. (e.g., -dt render/multiLister/createNode/material)
    
    - dragCallback : dgc             (script)        [create,edit]
        Adds a callback that is called when the middle mouse button is pressed.  The MEL
        version of the callback is of the form: global proc string[] callbackName(string
        $dragControl, int $x, int $y, int $mods) The proc returns a string array that is
        transferred to the drop site. By convention the first string in the array
        describes the user settable message type.  Controls that are application defined
        drag sources may ignore the callback. $mods allows testing for the key modifiers
        CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3
        == CTRL + SHIFT. In Python, it is similar, but there are two ways to specify the
        callback.  The recommended way is to pass a Python function object as the
        argument.  In that case, the Python callback should have the form: def
        callbackName( dragControl, x, y, modifiers ): The values of these arguments are
        the same as those for the MEL version above. The other way to specify the
        callback in Python is to specify a string to be executed.  In that case, the
        string will have the values substituted into it via the standard Python format
        operator.  The format values are passed in a dictionary with the keys
        dragControl, x, y, modifiers.  The dragControlvalue is a string and the other
        values are integers (eg the callback string could be print '%(dragControl)s
        %(x)d %(y)d %(modifiers)d'
    
    - dropCallback : dpc             (script)        [create,edit]
        Adds a callback that is called when a drag and drop operation is released above
        the drop site.  The MEL version of the callback is of the form: global proc
        callbackName(string $dragControl, string $dropControl, string $msgs[], int $x,
        int $y, int $type) The proc receives a string array that is transferred from the
        drag source. The first string in the msgs array describes the user defined
        message type. Controls that are application defined drop sites may ignore the
        callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link. In Python,
        it is similar, but there are two ways to specify the callback.  The recommended
        way is to pass a Python function object as the argument.  In that case, the
        Python callback should have the form: def pythonDropTest( dragControl,
        dropControl, messages, x, y, dragType ): The values of these arguments are the
        same as those for the MEL version above. The other way to specify the callback
        in Python is to specify a string to be executed.  In that case, the string will
        have the values substituted into it via the standard Python format operator.
        The format values are passed in a dictionary with the keys dragControl,
        dropControl, messages, x, y, type.  The dragControlvalue is a string and the
        other values are integers (eg the callback string could be print
        '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'
    
    - enable : en                    (bool)          [create,query,edit]
        The enable state of the control.  By default, this flag is set to true and the
        control is enabled.  Specify false and the control will appear dimmed or greyed-
        out indicating it is disabled.
    
    - enableBackground : ebg         (bool)          [create,query,edit]
        Enables the background color of the control.
    
    - enableKeyboardFocus : ekf      (bool)          [create,query,edit]
        If enabled, the user can navigate to the control with the tab key and select
        values with the keyboard. If not, the user can only use the mouse. This flag
        would typically be used to turn off keyboard focus support from controls that
        get it by default, like Edit and List controls
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - fullPathName : fpn             (bool)          [query]
        Return the full path name of the widget, which includes all the parents.
    
    - height : h                     (int)           [create,query,edit]
        The height of the control.  The control will attempt to be this size if it is
        not overruled by parent layout conditions.
    
    - highlightColor : hlc           (float, float, float) [create,query,edit]
        The highlight color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0.
    
    - isObscured : io                (bool)          [query]
        Return whether the control can actually be seen by the user. The control will be
        obscured if its state is invisible, if it is blocked (entirely or partially) by
        some other control, if it or a parent layout is unmanaged, or if the control's
        window is invisible or iconified.
    
    - manage : m                     (bool)          [create,query,edit]
        Manage state of the control.  An unmanaged control is not visible, nor does it
        take up any screen real estate.  All controls are created managed by default.
    
    - noBackground : nbg             (bool)          [create,edit]
        Clear/reset the control's background. Passing true means the background should
        not be drawn at all, false means the background should be drawn.  The state of
        this flag is inherited by children of this control.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - precision : pre                (int)           [query,edit]
        Controls the number of digits to the right of the decimal point that will be
        displayed for float-valued channels. Default is 3.  Queried, returns an int.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - rowAttach : rat                (int, unicode, int) [create,edit]
        Arguments are : column, attachment type, offset. Possible attachments are: top |
        bottom | both. Specifies attachment types and offsets for the entire row.
    
    - statusBarMessage : sbm         (unicode)       [create,edit]
        Extra string to display in the status bar when the mouse is over the control.
    
    - timeAnnotation : tan           (unicode)       [create,query,edit]
        Annotate the time field with an extra string value.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - valueAnnotation : van          (unicode)       [create,query,edit]
        Annotate the value field with an extra string value.
    
    - visible : vis                  (bool)          [create,query,edit]
        The visible state of the control.  A control is created visible by default.
        Note that a control's actual appearance is also dependent on the visible state
        of its parent layout(s).
    
    - visibleChangeCommand : vcc     (script)        [create,query,edit]
        Command that gets executed when visible state of the control changes.
    
    - width : w                      (int)           [create,query,edit]
        The width of the control.  The control will attempt to be this size if it is not
        overruled by parent layout conditions.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.keyframeStats`
    """
    pass


def _pointOnPolyConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def ikSystem(*args, **kwargs):
    """
    The ikSystem command is used to set the global snapping flag for handles and set
    the global solve flag for solvers.  The standard edit (-e) and query (-q) flags
    are used for edit and query functions.
    
    Flags:
    - allowRotation : ar             (bool)          [query,edit]
        Set true to allow rotation of an ik handle with keys set on translation.
    
    - autoPriority : ap              (bool)          [edit]
        set autoPriority for all ikHandles
    
    - autoPriorityMC : apm           (bool)          [edit]
        set autoPriority for all multiChain handles
    
    - autoPrioritySC : aps           (bool)          [edit]
        set autoPriority for all singleChain handles
    
    - list : ls                      (int, int)      [query,edit]
        returns the solver execution order when in query mode(list of strings) changes
        execution order when in edit mode (int old position, int new position)
    
    - snap : sn                      (bool)          [query,edit]
        Set global snapping
    
    - solve : sol                    (bool)          [query,edit]
        Set global solve
    
    - solverTypes : st               (bool)          [query]
        returns a list of valid solverTypes ( query only )                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.ikSystem`
    """
    pass


def joint(*args, **kwargs):
    """
    The joint command is used to create, edit, and query, joints within Maya. (The
    standard edit(-e) and query(-q) flags are used for edit and query functions). If
    the object is not specified, the currently selected object (dag object) will be
    used. Multiple objects are allowed only for the edit mode. The same edit flags
    will be applied on all the joints selected, except for -p without -r (set joint
    position in the world space). An ik handle in the object list is equivalent to
    the list of joints the ik handle commands. When -ch/children is present, all the
    child joints of the specified joints, including the joints implied by possible
    ik handles, will also be included. In the creation mode, a new joint will be
    created as a child of a selected transform or starts a hierarchy by itself if no
    transform is selected. An ik handle will be treated as a transform in the
    creation mode. The default values of the arguments are: -degreeOfFreedom xyz
    -name Joint#-position 0 0 0 -absolute -dof xyz-scale 1.0 1.0 1.0
    -scaleCompensate true -orientation 0.0 0.0 0.0 -scaleOrientation 0.0 0.0 0.0
    -limitX -360 360 -limitY -360 360 -limitZ -360 360 -angleX 0.0 -angleY 0.0
    -angleZ 0.0 -stiffnessX 0.0 -stiffnessY 0.0 -stiffnessZ 0.0 -limitSwitchX no
    -limitSwitchY no -limitSwitchZ no -rotationOrder xyz Those arguments can be
    specified in the creation mode, editied in the edit mode (-e), or queried in the
    query mode (-q).
    
    Flags:
    - absolute : a                   (bool)          [create,query,edit]
        The joint center position is in absolute world coordinates. (This is the
        default.)
    
    - angleX : ax                    (float)         [create,query,edit]
        Set the x-axis angle. When queried, this flag returns a float.
    
    - angleY : ay                    (float)         [create,query,edit]
        Set the y-axis angle. When queried, this flag returns a float.
    
    - angleZ : az                    (float)         [create,query,edit]
        Set the z-axis angle. When queried, this flag returns a float.
    
    - assumePreferredAngles : apa    (bool)          [edit]
        Meaningful only in the edit mode. It sets the joint angles to the corresponding
        preferred angles.
    
    - automaticLimits : al           (bool)          [create]
        Meaningful only in edit mode. It sets the joint to appropriate hinge joint with
        joint limits. It modifies the joint only if (a) it connects exactly to two
        joints (one parent, one child), (b) it does not lie on the line drawn between
        the two connected joints, and the plane it forms with the two connected joints
        is perpendicular to one of its rotation axes.
    
    - children : ch                  (bool)          [edit]
        It tells the command to apply all the edit options not only to the selected
        joints, but also to their descendent joints in the DAG.
    
    - component : co                 (bool)          [create,edit]
        Use with the -position switch to position the joint relative to its parent (like
        -relative) but to compute new positions for all children joints so their world
        coordinate positions do not change.
    
    - degreeOfFreedom : dof          (unicode)       [create,query,edit]
        Specifies the degrees of freedom for the IK. Valid strings consist of non-
        duplicate letters from x, y, and z. The letters in the string indicate what
        rotations are to be used by IK. The order a letter appear in the string does not
        matter. Examples are x, yz, xyz. When queried, this flag returns a string.
        Modifying dof will change the locking state of the corresponding rotation
        attributes. The rule is: if an rotation is turned into a dof, it will be
        unlocked if it is currently locked. When it is turned into a non-dof, it will be
        locked if it is not currently locked.
    
    - exists : ex                    (unicode)       [query]
        Does the named joint exist? When queried, this flag returns a boolean.
    
    - limitSwitchX : lsx             (bool)          [create,query,edit]
        Use the limit the x-axis rotation? When queried, this flag returns a boolean.
    
    - limitSwitchY : lsy             (bool)          [create,query,edit]
        Use the limit the y-axis rotation? When queried, this flag returns a boolean.
    
    - limitSwitchZ : lsz             (bool)          [create,query,edit]
        Use the Limit the z-axis rotation? When queried, this flag returns a boolean.
    
    - limitX : lx                    (float, float)  [create,query,edit]
        Set lower and upper limits on the x-axis of rotation.  Also turns on the joint
        limit. When queried, this flag returns 2 floats.
    
    - limitY : ly                    (float, float)  [create,query,edit]
        Set lower and upper limits on the y-axis of rotation.  Also turns on the joint
        limit. When queried, this flag returns 2 floats.
    
    - limitZ : lz                    (float, float)  [create,query,edit]
        Set lower and upper limits on the z-axis of rotation.  Also turns on the joint
        limit. When queried, this flag returns 2 floats.
    
    - name : n                       (unicode)       [create,query,edit]
        Specifies the name of the joint. When queried, this flag returns a string.
    
    - orientJoint : oj               (unicode)       [edit]
        The argument can be one of the following strings: xyz, yzx, zxy, zyx, yxz, xzy,
        none. It modifies the joint orientation and scale orientation so that the axis
        indicated by the first letter in the argument will be aligned with the vector
        from this joint to its first child joint. For example, if the argument is xyz,
        the x-axis will point towards the child joint. The alignment of the remaining
        two joint orient axes are dependent on whether or not the
        -sao/-secondaryAxisOrient flag is used. If the -sao flag is used, see the
        documentation for that flag for how the remaining axes are aligned. In the
        absence of a user specification for the secondary axis orientation, the rotation
        axis indicated by the last letter in the argument will be aligned with the
        vector perpendicular to first axis and the vector from this joint to its parent
        joint. The remaining axis is aligned according the right hand rule. If the
        argument is none, the joint orientation will be set to zero and its effect to
        the hierarchy below will be offset by modifying the scale orientation. The flag
        will be ignored if: A. the joint has non-zero rotations when the argument is not
        none. B. the joint does not have child joint, or the distance to the child joint
        is zero when the argument is not none. C. either flag -o or -so is set.
    
    - orientation : o                (float, float, float) [create,query,edit]
        The joint orientation. When queried, this flag returns 3 floats.
    
    - position : p                   (float, float, float) [create,query,edit]
        Specifies the position of the center of the joint. This position may be relative
        to the joint's parent or in absolute world coordinates (see -r and -a below).
        When queried, this flag returns 3 floats.
    
    - radius : rad                   (float)         [create,query,edit]
        Specifies the joint radius.
    
    - relative : r                   (bool)          [create,query,edit]
        The joint center position is relative to the joint's parent.
    
    - rotationOrder : roo            (unicode)       [create,query,edit]
        The rotation order of the joint. The argument can be one of the following
        strings: xyz, yzx, zxy, zyx, yxz, xzy.
    
    - scale : s                      (float, float, float) [create,query,edit]
        Scale of the joint. When queried, this flag returns 3 floats.
    
    - scaleCompensate : sc           (bool)          [create,query,edit]
        It sets the scaleCompenstate attribute of the joint to the given argument. When
        this is true, the scale of the parent joint will be compensated before any
        rotation of this joint is applied, so that the bone to the joint is scaled but
        not the bones to its child joints. When queried, this flag returns an boolean.
    
    - scaleOrientation : so          (float, float, float) [create,query,edit]
        Set the orientation of the coordinate axes for scaling. When queried, this flag
        returns 3 floats.
    
    - secondaryAxisOrient : sao      (unicode)       [edit]
        The argument can be one of the following strings: xup, xdown, yup, ydown, zup,
        zdown, none. This flag is used in conjunction with the -oj/orientJoint flag. It
        specifies the scene axis that the second axis should align with. For example, a
        flag combination of -oj yzx -sao yupwould result in the y-axis pointing down the
        bone, the z-axis oriented with the scene's positive y-axis, and the x-axis
        oriented according to the right hand rule.
    
    - setPreferredAngles : spa       (bool)          [edit]
        Meaningful only in the edit mode. It sets the preferred angles to the current
        joint angles.
    
    - stiffnessX : stx               (float)         [create,query,edit]
        Set the stiffness (from 0 to 100.0) for x-axis. When queried, this flag returns
        a float.
    
    - stiffnessY : sty               (float)         [create,query,edit]
        Set the stiffness (from 0 to 100.0) for y-axis. When queried, this flag returns
        a float.
    
    - stiffnessZ : stz               (float)         [create,query,edit]
        Set the stiffness (from 0 to 100.0) for z-axis. When queried, this flag returns
        a float.
    
    - symmetry : sym                 (bool)          [create,edit]
        Create a symmetric joint from the current joint.
    
    - symmetryAxis : sa              (unicode)       [create,edit]
        This flag specifies the axis used to mirror symmetric joints. Any combination of
        x, y, z can be used. This option is only used when the symmetry flag is set to
        True.
    
    - zeroScaleOrient : zso          (bool)          [edit]
        It sets the scale orientation to zero and compensate the change by modifing the
        translation and joint orientation for joint or rotation for general transform of
        all its child transformations. The flag will be ignored if the flag -so is set.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.joint`
    """
    pass


def listAnimatable(*args, **kwargs):
    """
    This command list the animatable attributes of a node.  Command flags allow
    filtering by the current manipulator, or node type.
    
    Modifications:
        - returns an empty list when the result is None
        - returns wrapped classes
    
    Flags:
    - active : act                   (bool)          [create]
        This flag is obsolete and no longer supported.
    
    - manip : m                      (bool)          [create]
        Return only those attributes affected by the current manip. If there is no manip
        active and any other flags are specified, output is the same as if the
        -manipflag were not present.
    
    - manipHandle : mh               (bool)          [create]
        Return only those attributes affected by the current manip handle. If there is
        no manip handle active and any other flags are specified, output is the same as
        if the -manipHandleflag were not present.
    
    - shape : s                      (bool)          [create]
        This flag is obsolete and no longer supported.
    
    - type : typ                     (bool)          [create]
        Instead of returning attributes, Return the types of nodes that are currently
        animatable.                  Flag can have multiple arguments, passed either as
        a tuple or a list.
    
    
    Derived from mel command `maya.cmds.listAnimatable`
    """
    pass


def timeEditorTracks(*args, **kwargs):
    """
    Time Editor tracks commands
    
    Flags:
    - activeClipWeight : acw         (time)          [query]
        Get the clip weight at the specified time.
    
    - activeClipWeightId : aci       (time)          [query]
        Get the clip ID carrying the active clip weight at the specified time.
    
    - addTrack : at                  (int)           [edit]
        Add new track at the track index specified. Indices are 0-based. Specify -1 to
        add the track at the end.
    
    - allClips : ac                  (bool)          [query]
        Return a list of clip IDs under the specified track.
    
    - allTracks : atc                (bool)          [query]
        Return a list of strings for all the immediate tracks for the given tracks node
        in the format tracksNode:trackIndex.
    
    - allTracksRecursive : atr       (bool)          [query]
        Return a list of strings for all the tracks for the given tracks node, or return
        a list of strings for all tracks of all tracks nodes in the format
        tracksNode:trackIndex. If the given root tracks node is from a composition, this
        command returns the tracks under that composition, including the tracks within
        groups that is under the same composition.
    
    - composition : cp               (bool)          [query]
        Return the composition the specified track belongs to.
    
    - path : pt                      (unicode)       [edit]
        Full path of a track node or a track on which to operate. For example:
        composition1|track1|group; composition1|track1. In query mode, this flag can
        accept a value.
    
    - plugIndex : pi                 (int)           [query,edit]
        Get the plug index of the specified track.
    
    - removeTrack : rt               (int)           [edit]
        Remove track at given index. It is a multi-use flag.
    
    - removeTrackByPath : rtp        (unicode)       [edit]
        Remove track at given path. It is a multi-use flag. For example:
        composition1|track1|group|track1;
    
    - reorderTrack : rot             (int, int)      [edit]
        Move the track relative to other tracks. The first argument is the track index
        (0-based). The second argument can be a positive or negative number to indicate
        the steps to move. Positive numbers move forward and negative numbers move
        backward.
    
    - resetMute : rm                 (bool)          [create]
        Reset all the muted tracks in the active composition.
    
    - resetSolo : rs                 (bool)          [create]
        Reset the soloing of all tracks on the active composition.
    
    - selectedTracks : st            (bool)          [query]
        Return a list of the indices for all the selected tracks for the given tracks
        node, or return a list of strings for all selected tracks of all tracks nodes in
        the format tracksNode:trackIndex.
    
    - trackGhost : tgh               (bool)          [query,edit]
        Ghost all clips under track.
    
    - trackIndex : ti                (int)           [query,edit]
        Specify the track index. This flag is used in conjunction with the other flags.
        In query mode, this flag can accept a value.
    
    - trackMuted : tm                (bool)          [query,edit]
        Return whether the track is muted.
    
    - trackName : tn                 (unicode)       [query,edit]
        Display name of the track.
    
    - trackSolo : ts                 (bool)          [query,edit]
        Return whether the track is soloed.
    
    - trackType : tt                 (int)           [query,edit]
        Specify the track type. Can only be used together with -at/addTrack. Does not
        work by itself. In query mode, return the integer corresponding to the track
        type. 0: Animation Track (Default)1: Audio Track Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.timeEditorTracks`
    """
    pass


def currentTime(*args, **kwargs):
    """
    When given a time argument (with or without the -edit flag) this command sets
    the current global time.  The model updates and displays at the new time, unless
    -update offis present on the command line.
    
    Modifications:
        - if no args are provided, the command returns the current time
    
    Flags:
    - update : u                     (bool)          [create]
        change the current time, but do not update the world. Default value is true.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.currentTime`
    """
    pass


def _normalConstraint(*args, **kwargs):
    """
    Maya Bug Fix:
      - when queried, angle offsets would be returned in radians, not current angle unit
    
    Modifications:
      - added new syntax for querying the weight of a target object, by passing the constraint first::
    
            aimConstraint('pCube1_aimConstraint1', q=1, weight='pSphere1')
            aimConstraint('pCube1_aimConstraint1', q=1, weight=['pSphere1', 'pCylinder1'])
            aimConstraint('pCube1_aimConstraint1', q=1, weight=True)
    """
    pass


def sequenceManager(*args, **kwargs):
    """
    The sequenceManager command manages sequences, shots, and their related scenes.
    In query mode, return type is based on queried flag.
    
    Flags:
    - addSequencerAudio : asa        (unicode)       [create]
        Add an audio clip to the sequencer by specifying a filename
    
    - attachSequencerAudio : ata     (unicode)       [create]
        Add an audio clip to the sequencer by specifying an audio node
    
    - currentShot : cs               (unicode)       [query]
        Returns the shot that is being used at the current sequence time.
    
    - currentTime : ct               (time)          [create,query]
        Set the current sequence time
    
    - listSequencerAudio : lsa       (unicode)       [create]
        List the audio clips added to the sequencer
    
    - listShots : lsh                (bool)          [create]
        List all the currently defined shots across all scene segments
    
    - modelPanel : mp                (unicode)       [create,query]
        Sets a dedicated modelPanel to be used as the panel that the sequencer will
        control.
    
    - node : nd                      (unicode)       [query]
        Returns the SequenceManager node, of which there is only ever one.
    
    - writableSequencer : ws         (unicode)       [query]
        Get the writable sequencer node.  Create it if it doesn't exist.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.sequenceManager`
    """
    pass


def setCurrentTime(time):
    """
    set the current time
    """
    pass


def boneLattice(*args, **kwargs):
    """
    This command creates/edits/queries a boneLattice deformer. The name of the
    created/edited object is returned. Usually you would make use of this
    functionality through the higher level flexor command.
    
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
    
    - bicep : bi                     (float)         [create,query,edit]
        Affects the bulging of lattice points on the inside of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - joint : j                      (unicode)       [create,query,edit]
        Specifies which joint will be used to drive the bulging behaviors.
    
    - lengthIn : li                  (float)         [create,query,edit]
        Affects the location of lattice points along the upper half of the bone.
        Positive/negative values cause the points to move away/towards the center of the
        bone.  Changing this parameter also modifies the regions affected by the
        creasing, rounding and width parameters. Default value is 0.0. When queried,
        this flag returns a float.
    
    - lengthOut : lo                 (float)         [create,query,edit]
        Affects the location of lattice points along the lower half of the bone.
        Positive/negative values cause the points to move away/towards the center of the
        bone.  Changing this parameter also modifies the regions affected by the
        creasing, rounding and width parameters. Default value is 0.0. When queried,
        this flag returns a float.
    
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
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - transform : t                  (unicode)       [create]
        Specifies which dag node is being used to rigidly transform the lattice which
        this node is going to deform.  If this flag is not specified an identity matrix
        will be assumed.
    
    - tricep : tr                    (float)         [create,query,edit]
        Affects the bulging of lattice points on the outside of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.
    
    - widthLeft : wl                 (float)         [create,query,edit]
        Affects the bulging of lattice points on the left side of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.
    
    - widthRight : wr                (float)         [create,query,edit]
        Affects the bulging of lattice points on the right side of the bend.
        Positive/negative values cause the points to bulge outwards/inwards. Default
        value is 0.0. When queried, this flag returns a float.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.boneLattice`
    """
    pass


def scaleKey(*args, **kwargs):
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
    list or range (see Examples). This command takes keyframes at (or within) the
    specified times (or time ranges) and scales them.  If no times are specified,
    the scale is applied to active keyframes or (if no keys are active) all keys of
    active objects.
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - floatPivot : fp                (float)         [create]
        Scale pivot along the x-axis for float-input animCurves
    
    - floatScale : fs                (float)         [create]
        Amount of scale along the x-axis for float-input animCurves
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
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
    
    - newEndFloat : nef              (float)         [create]
        The end of the float range to which the float-input targets should be scaled.
    
    - newEndTime : net               (time)          [create]
        The end of the time range to which the targets should be scaled.
    
    - newStartFloat : nsf            (float)         [create]
        The start of the float range to which the float-input targets should be scaled.
    
    - newStartTime : nst             (time)          [create]
        The start of the time range to which the time-input targets should be scaled.
    
    - scaleSpecifiedKeys : ssk       (bool)          [create]
        Determines if only the specified keys are affected by the scale. If false, other
        keys may be adjusted with the scale. The default is true.
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - timePivot : tp                 (time)          [create]
        Scale pivot along the time-axis for time-input animCurves
    
    - timeScale : ts                 (float)         [create]
        Amount of scale along the time-axis for time-input animCurves
    
    - valuePivot : vp                (float)         [create]
        Scale pivot along the value-axis
    
    - valueScale : vs                (float)         [create]
        Amount of scale along the value-axis                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.scaleKey`
    """
    pass


def posePanel(*args, **kwargs):
    """
    This command creates a panel that derives from the base panel class that houses
    a poseEditor.
    
    Flags:
    - control : ctl                  (bool)          [query]
        Returns the top level control for this panel. Usually used for getting a parent
        to attach popup menus. CAUTION: panels may not have controls at times.  This
        flag can return if no control is present.
    
    - copy : cp                      (unicode)       [edit]
        Makes this panel a copy of the specified panel.  Both panels must be of the same
        type.
    
    - createString : cs              (bool)          [edit]
        Command string used to create a panel
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the Maya panel.
    
    - editString : es                (bool)          [edit]
        Command string used to edit a panel
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - init : init                    (bool)          [create,edit]
        Initializes the panel's default state.  This is usually done automatically on
        file -new and file -open.
    
    - isUnique : iu                  (bool)          [query]
        Returns true if only one instance of this panel type is allowed.
    
    - label : l                      (unicode)       [query,edit]
        Specifies the user readable label for the panel.
    
    - menuBarRepeatLast : mrl        (bool)          [create,query,edit]
        Controls whether clicking on the menu header with the middle mouse button would
        repeat the last selected menu item.
    
    - menuBarVisible : mbv           (bool)          [create,query,edit]
        Controls whether the menu bar for the panel is displayed.
    
    - needsInit : ni                 (bool)          [query,edit]
        (Internal) On Edit will mark the panel as requiring initialization. Query will
        return whether the panel is marked for initialization.  Used during file -new
        and file -open.
    
    - parent : p                     (unicode)       [create]
        Specifies the parent layout for this panel.
    
    - popupMenuProcedure : pmp       (script)        [query,edit]
        Specifies the procedure called for building the panel's popup menu(s). The
        default value is buildPanelPopupMenu.  The procedure should take one string
        argument which is the panel's name.
    
    - poseEditor : pe                (bool)          [query]
        Query only flag that returns the name of an editor to be associated with the
        panel.
    
    - replacePanel : rp              (unicode)       [edit]
        Will replace the specified panel with this panel.  If the target panel is within
        the same layout it will perform a swap.
    
    - tearOff : to                   (bool)          [query,edit]
        Will tear off this panel into a separate window with a paneLayout as the parent
        of the panel. When queried this flag will return if the panel has been torn off
        into its own window.
    
    - tearOffCopy : toc              (unicode)       [create]
        Will create this panel as a torn of copy of the specified source panel.
    
    - tearOffRestore : tor           (bool)          [create,edit]
        Restores panel if it is torn off and focus is given to it. If docked, becomes
        the active panel in the docked window. This should be the default flag that is
        added to all panels instead of -to/-tearOffflag which should only be used to
        tear off the panel.
    
    - unParent : up                  (bool)          [edit]
        Specifies that the panel should be removed from its layout. This (obviously)
        cannot be used with query.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.posePanel`
    """
    pass


def snapKey(*args, **kwargs):
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
    list or range (see Examples). This command snapsall target key times and/or
    values so that they have times and/or values that are multiples of the specified
    flag arguments.  If neither multiple is specified, default is time snapping with
    a multiple of 1.0. Note that this command will fail to move keys over other
    neighboring keys: a key's index will not change as a result of a snapKey
    operation.TbaseKeySetCmd.h
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
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
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
    
    - timeMultiple : tm              (float)         [create]
        If this flag is present, key times will be snapped to a multiple of the
        specified float value.
    
    - valueMultiple : vm             (float)         [create]
        If this flag is present, key values will be snapped to a multiple of the
        specified float value.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.snapKey`
    """
    pass


def parentConstraint(*args, **kwargs):
    """
    Constrain an object's position and rotation so that it behaves as if it were a
    child of the target object(s). In the case of multiple targets, the overall
    position and rotation of the constrained object is the weighted average of each
    target's contribution to the position and rotation of the object. A
    parentConstraint takes as input one or more targetDAG transform nodes at which
    to position and rotate the single constraint objectDAG transform node.  The
    parentConstraint positions and rotates the constrained object at the weighted
    average of the world space position, rotation and scale target objects.
    
    Flags:
    - createCache : cc               (float, float)  [edit]
        This flag is used to generate an animation curve that serves as a cache for the
        constraint. The two arguments define the start and end frames.  The cache is
        useful if the constraint has multiple targets and the constraint's interpolation
        type is set to no flip. The no flipmode prevents flipping during playback, but
        the result is dependent on the previous frame. Therefore in order to
        consistently get the same result on a specific frame, a cache must be generated.
        This flag creates the cache and sets the constraint's interpolation type to
        cache. If a cache exists already, it will be deleted and replaced with a new
        cache.
    
    - decompRotationToChild : dr     (bool)          [create]
        During constraint creation, if the rotation offset between the constrained
        object and the target object is maintained, this flag indicates close to which
        object the offset rotation is decomposed. Setting this flag will make the
        rotation decomposition close to the constrained object instead of the target
        object, which is the default setting.
    
    - deleteCache : dc               (bool)          [edit]
        Delete an existing interpolation cache.
    
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - maintainOffset : mo            (bool)          [create]
        If this flag is specified the position and rotation of the constrained object
        will be maintained.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - skipRotate : sr                (unicode)       [create]
        Causes the axis specified not to be considered when constraining rotation.
        Valid arguments are x, y, zand none.
    
    - skipTranslate : st             (unicode)       [create]
        Causes the axis specified not to be considered when constraining translation.
        Valid arguments are x, y, zand none.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.parentConstraint`
    """
    pass


def deltaMush(*args, **kwargs):
    """
    This command is used to create, edit and query deltaMush nodes.
    
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
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - envelope : en                  (float)         [create,query,edit]
        Envelope of the delta mush node. The envelope determines the percent of
        deformation. Value is clamped to [0, 1] range. Default is 1.
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - inwardConstraint : iwc         (float)         [create,query,edit]
        Constrains the movement of the vertex to not move inward from the input
        deforming shape to preserve the contour. Value is in the [0,1] range. Default is
        0.0.
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - outwardConstraint : owc        (float)         [create,query,edit]
        Constrains the movement of the vertex to not move outward from the input
        deforming shape to preserve the contour. Value is in the [0,1] range. Default is
        0.0.
    
    - parallel : par                 (bool)          [create,edit]
        Inserts the new deformer in a parallel chain to any existing deformers in the
        history of the object. A blendShape is inserted to blend the parallel results
        together. Works in create mode (and edit mode if the deformer has no geometry
        added yet).
    
    - pinBorderVertices : pbv        (bool)          [create,query,edit]
        If enabled, vertices on mesh borders will be pinned to their current position
        during smoothing. Default is true.
    
    - prune : pr                     (bool)          [edit]
        Removes any points not being deformed by the deformer in its current
        configuration from the deformer set.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - smoothingIterations : si       (int)           [create,query,edit]
        Number of smoothing iterations performed by the delta mush node. Default is 10.
    
    - smoothingStep : ss             (float)         [create,query,edit]
        Step amount used per smoothing iteration. Value is clamped to [0, 1] range. A
        higher value may lead to instabilities but converges faster compared to a lower
        value. Default is 0.5.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.deltaMush`
    """
    pass


def geometryConstraint(*args, **kwargs):
    """
    Constrain an object's position based on the shape of the target surface(s) at
    the closest point(s) to the object. A geometryConstraint takes as input one or
    more surface shapes (the targets) and a DAG transform node (the object).  The
    geometryConstraint position constrained object such object lies on the surface
    of the target with the greatest weight value.  If two targets have the same
    weight value then the one with the lowest index is chosen.
    
    Flags:
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.geometryConstraint`
    """
    pass


def flow(*args, **kwargs):
    """
    The flow command creates a deformation lattice to `bend' the object that is
    animated along a curve of a motion path animation. The motion path animation has
    to have the follow option set to be on.
    
    Flags:
    - divisions : dv                 (int, int, int) [query]
        This flag specifies the number of lattice slices in x,y,z.The default values are
        2 5 2.When queried, it returns the uint32_t uint32_t uint32_t
    
    - localCompute : lc              (bool)          [query]
        This flag specifies whether or not to have local control over the object
        deformation.Default value: is on when the lattice is around the curve, and is
        off when the lattice is around the object. When queried, it returns a boolean
    
    - localDivisions : ld            (int, int, int) [query]
        This flag specifies the extent of the region of effect.Default values are 2 2
        2.When queried, it returns the uint32_t uint32_t uint32_t
    
    - objectCentered : oc            (bool)          [query]
        This flag specifies whether to create the lattice around the selected object at
        its center, or to create the lattice around the curve.Default value is true.When
        queried, it returns a booleanFlag can have multiple arguments, passed either as
        a tuple or a list.
    
    
    Derived from mel command `maya.cmds.flow`
    """
    pass


def _keyframe(*args, **kwargs):
    """
    Modifications:
        - returns an empty list when the result is None
        - if both valueChange and timeChange are queried, the result will be a list of (time,value) pairs
    """
    pass


def clipSchedulerOutliner(*args, **kwargs):
    """
    This command creates/edits/queries a clip scheduler outliner control.
    
    Flags:
    - annotation : ann               (unicode)       [create,query,edit]
        Annotate the control with an extra string value.
    
    - backgroundColor : bgc          (float, float, float) [create,query,edit]
        The background color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0. When
        setting backgroundColor, the background is automatically enabled, unless
        enableBackground is also specified with a false value.
    
    - clipScheduler : cs             (unicode)       [edit]
        Name of the clip scheduler for which to display information.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Add a documentation flag to the control.  The documentation flag has a directory
        structure. (e.g., -dt render/multiLister/createNode/material)
    
    - dragCallback : dgc             (script)        [create,edit]
        Adds a callback that is called when the middle mouse button is pressed.  The MEL
        version of the callback is of the form: global proc string[] callbackName(string
        $dragControl, int $x, int $y, int $mods) The proc returns a string array that is
        transferred to the drop site. By convention the first string in the array
        describes the user settable message type.  Controls that are application defined
        drag sources may ignore the callback. $mods allows testing for the key modifiers
        CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3
        == CTRL + SHIFT. In Python, it is similar, but there are two ways to specify the
        callback.  The recommended way is to pass a Python function object as the
        argument.  In that case, the Python callback should have the form: def
        callbackName( dragControl, x, y, modifiers ): The values of these arguments are
        the same as those for the MEL version above. The other way to specify the
        callback in Python is to specify a string to be executed.  In that case, the
        string will have the values substituted into it via the standard Python format
        operator.  The format values are passed in a dictionary with the keys
        dragControl, x, y, modifiers.  The dragControlvalue is a string and the other
        values are integers (eg the callback string could be print '%(dragControl)s
        %(x)d %(y)d %(modifiers)d'
    
    - dropCallback : dpc             (script)        [create,edit]
        Adds a callback that is called when a drag and drop operation is released above
        the drop site.  The MEL version of the callback is of the form: global proc
        callbackName(string $dragControl, string $dropControl, string $msgs[], int $x,
        int $y, int $type) The proc receives a string array that is transferred from the
        drag source. The first string in the msgs array describes the user defined
        message type. Controls that are application defined drop sites may ignore the
        callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link. In Python,
        it is similar, but there are two ways to specify the callback.  The recommended
        way is to pass a Python function object as the argument.  In that case, the
        Python callback should have the form: def pythonDropTest( dragControl,
        dropControl, messages, x, y, dragType ): The values of these arguments are the
        same as those for the MEL version above. The other way to specify the callback
        in Python is to specify a string to be executed.  In that case, the string will
        have the values substituted into it via the standard Python format operator.
        The format values are passed in a dictionary with the keys dragControl,
        dropControl, messages, x, y, type.  The dragControlvalue is a string and the
        other values are integers (eg the callback string could be print
        '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'
    
    - enable : en                    (bool)          [create,query,edit]
        The enable state of the control.  By default, this flag is set to true and the
        control is enabled.  Specify false and the control will appear dimmed or greyed-
        out indicating it is disabled.
    
    - enableBackground : ebg         (bool)          [create,query,edit]
        Enables the background color of the control.
    
    - enableKeyboardFocus : ekf      (bool)          [create,query,edit]
        If enabled, the user can navigate to the control with the tab key and select
        values with the keyboard. If not, the user can only use the mouse. This flag
        would typically be used to turn off keyboard focus support from controls that
        get it by default, like Edit and List controls
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - fullPathName : fpn             (bool)          [query]
        Return the full path name of the widget, which includes all the parents.
    
    - height : h                     (int)           [create,query,edit]
        The height of the control.  The control will attempt to be this size if it is
        not overruled by parent layout conditions.
    
    - highlightColor : hlc           (float, float, float) [create,query,edit]
        The highlight color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0.
    
    - isObscured : io                (bool)          [query]
        Return whether the control can actually be seen by the user. The control will be
        obscured if its state is invisible, if it is blocked (entirely or partially) by
        some other control, if it or a parent layout is unmanaged, or if the control's
        window is invisible or iconified.
    
    - manage : m                     (bool)          [create,query,edit]
        Manage state of the control.  An unmanaged control is not visible, nor does it
        take up any screen real estate.  All controls are created managed by default.
    
    - noBackground : nbg             (bool)          [create,edit]
        Clear/reset the control's background. Passing true means the background should
        not be drawn at all, false means the background should be drawn.  The state of
        this flag is inherited by children of this control.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - statusBarMessage : sbm         (unicode)       [create,edit]
        Extra string to display in the status bar when the mouse is over the control.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - visible : vis                  (bool)          [create,query,edit]
        The visible state of the control.  A control is created visible by default.
        Note that a control's actual appearance is also dependent on the visible state
        of its parent layout(s).
    
    - visibleChangeCommand : vcc     (script)        [create,query,edit]
        Command that gets executed when visible state of the control changes.
    
    - width : w                      (int)           [create,query,edit]
        The width of the control.  The control will attempt to be this size if it is not
        overruled by parent layout conditions.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.clipSchedulerOutliner`
    """
    pass


def jointCluster(*args, **kwargs):
    """
    The joint cluster command adds high-level controls to manage the cluster
    percentage values on a bound skin around a joint. JointClusters are one way to
    create smooth bending behaviour on skin when joints rotate. .                a
    ---- aboveBound .    ____________a_________ .                a         \ .
    Joint1     a       Joint2 .   _____________a_______    \ .                a
    \    \     b  --- belowBound .                a        \    \  b .
    \    b .                           \ b  \ .                           b\    \ .
    b   \ Joint3 CVs/vertices between Joint1 and aaaaa (aboveBound) receive only
    translation/rotation/scale from Joint1. CVs vertices between aaaa and bbbb
    transition between translation/rotatation/scale from Joint1 and Joint2. CV2
    beyand bbbbb (below bound) receive only translation/ rotation scale from Joint3.
    
    Flags:
    - aboveBound : ab                (float)         [create,query,edit]
        Specifies the where the drop-off begins in the direction of the bone above the
        joint. A value of 100 indicates the entire length of the bone. The default value
        is 10.
    
    - aboveCluster : ac              (bool)          [query]
        Returns the name of the cluster associated with the bone above this joint.
    
    - aboveDropoffType : adt         (unicode)       [create,query,edit]
        Specifies the type of percentage drop-off in the direction of the bone above
        this joint. Valid values are linear, exponential, sineand none. Default is
        linear.
    
    - aboveValue : av                (float)         [create,query,edit]
        Specifies the drop-off percentage of the joint cluster in the direction of the
        bone above the cluster. A value of 100 indicates the entire length of the bone.
        The default value is 50.
    
    - belowBound : bb                (float)         [create,query,edit]
        Specifies where the drop-off ends in the direction of the bone below the joint.
        A value of 100 indicates the entire length of the bone. The default value is 10.
    
    - belowCluster : bc              (bool)          [query]
        Returns the name of the cluster associated with this joint.
    
    - belowDropoffType : bdt         (unicode)       [create,query,edit]
        Specifies the type of type of percentage drop-off in the direction of the bone
        below this joint. Valid values are linear, exponential, sineand none. Default is
        linear.
    
    - belowValue : bv                (float)         [create,query,edit]
        Specifies the drop-off percentage of the joint cluster in the direction of the
        joint below the cluster. A value of 100 indicates the entire length of the bone.
        The default value is 50.
    
    - deformerTools : dt             (bool)          [query]
        Used to query for the helper nodes associated with the jointCluster.
    
    - joint : j                      (unicode)       [create]
        Specifies the joint that the cluster should act about.
    
    - name : n                       (unicode)       [create]
        This flag is obsolete.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.jointCluster`
    """
    pass


def aimConstraint(*args, **kwargs):
    """
    Constrain an object's orientation to point at a target object or at the average
    position of a number of targets. An aimConstraint takes as input one or more
    targetDAG transform nodes at which to aim the single constraint objectDAG
    transform node.  The aimConstraint orients the constrained object such that the
    aimVector (in the object's local coordinate system) points to the in weighted
    average of the world space position target objects.  The upVector (again the the
    object's local coordinate system) is aligned in world space with the
    worldUpVector.
    
    Flags:
    - aimVector : aim                (float, float, float) [create,query,edit]
        Set the aim vector.  This is the vector in local coordinates that points at the
        target.  If not given at creation time, the default value of (1.0, 0.0, 0.0) is
        used.
    
    - layer : l                      (unicode)       [create,edit]
        Specify the name of the animation layer where the constraint should be added.
    
    - maintainOffset : mo            (bool)          [create]
        The offset necessary to preserve the constrained object's initial rotation will
        be calculated and used as the offset.
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the constraint node to the specified name.  Default name is
        constrainedObjectName_constraintType
    
    - offset : o                     (float, float, float) [create,query,edit]
        Sets or queries the value of the offset. Default is 0,0,0.
    
    - remove : rm                    (bool)          [edit]
        removes the listed target(s) from the constraint.
    
    - skip : sk                      (unicode)       [create,edit]
        Specify the axis to be skipped. Valid values are x, y, zand none. During
        creation, noneis the default.
    
    - targetList : tl                (bool)          [query]
        Return the list of target objects.
    
    - upVector : u                   (float, float, float) [create,query,edit]
        Set local up vector.  This is the vector in local coordinates that aligns with
        the world up vector.  If not given at creation time, the default value of (0.0,
        1.0, 0.0) is used.
    
    - weight : w                     (float)         [create,query,edit]
        Sets the weight value for the specified target(s). If not given at creation
        time, the default value of 1.0 is used.
    
    - weightAliasList : wal          (bool)          [query]
        Returns the names of the attributes that control the weight of the target
        objects. Aliases are returned in the same order as the targets are returned by
        the targetList flag
    
    - worldUpObject : wuo            (PyNode)        [create,query,edit]
        Set the DAG object use for worldUpType objectand objectrotation. See worldUpType
        for greater detail. The default value is no up object, which is interpreted as
        world space.
    
    - worldUpType : wut              (unicode)       [create,query,edit]
        Set the type of the world up vector computation. The worldUpType can have one of
        5 values: scene, object, objectrotation, vector, or none. If the value is scene,
        the upVector is aligned with the up axis of the scene and worldUpVector and
        worldUpObject are ignored. If the value is object, the upVector is aimed as
        closely as possible to the origin of the space of the worldUpObject and the
        worldUpVector is ignored. If the value is objectrotationthen the worldUpVector
        is interpreted as being in the coordinate space of the worldUpObject,
        transformed into world space and the upVector is aligned as closely as possible
        to the result. If the value is vector, the upVector is aligned with
        worldUpVector as closely as possible and worldUpMatrix is ignored. Finally, if
        the value is noneno twist calculation is performed by the constraint, with the
        resulting upVectororientation based previous orientation of the constrained
        object, and the great circlerotation needed to align the aim vector with its
        constraint. The default worldUpType is vector.
    
    - worldUpVector : wu             (float, float, float) [create,query,edit]
        Set world up vector.  This is the vector in world coordinates that up vector
        should align with. See -wut/worldUpType (below)for greater detail. If not given
        at creation time, the default value of (0.0, 1.0, 0.0) is used.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.aimConstraint`
    """
    pass


def textureDeformer(*args, **kwargs):
    """
    This command creates a texture deformer for the object. The selected objects are
    the input geometry objects. The deformer node name will be returned.
    
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
    
    - deformerTools : dt             (bool)          [query]
        Returns the name of the deformer tool objects (if any) as string string ...
    
    - direction : d                  (unicode)       [create]
        Set the deformation direction of texture deformer It can only handle three
        types: Normal, Handleand Vector. Normaleach vertices use its own normal vector.
        Handleall vertices use Up vector of the handle. Vectoreach vertices use RGB
        color vector strings.
    
    - envelope : en                  (float)         [create]
        Set the envelope of texture deformer. Envelope determines the percent of
        deformation. The final result is (color \* normal \* strength + offset) \*
        envelope
    
    - exclusive : ex                 (unicode)       [create,query]
        Puts the deformation set in a deform partition.
    
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
    
    - name : n                       (unicode)       [create]
        Used to specify the name of the node being created.
    
    - offset : o                     (float)         [create]
        Set the offset of texture deformer. Offset plus a translation on the final
        deformed vertices.
    
    - parallel : par                 (bool)          [create,edit]
        Inserts the new deformer in a parallel chain to any existing deformers in the
        history of the object. A blendShape is inserted to blend the parallel results
        together. Works in create mode (and edit mode if the deformer has no geometry
        added yet).
    
    - pointSpace : ps                (unicode)       [create]
        Set the point space of texture deformer. It can only handle three strings:
        World, Localand UV. Worldmap world space to color space. Localmap local space to
        color space. UVmap UV space to color space. strings.
    
    - prune : pr                     (bool)          [edit]
        Removes any points not being deformed by the deformer in its current
        configuration from the deformer set.
    
    - remove : rm                    (bool)          [edit]
        Specifies that objects listed after the -g flag should be removed from this
        deformer.
    
    - split : sp                     (bool)          [create,edit]
        Branches off a new chain in the dependency graph instead of inserting/appending
        the deformer into/onto an existing chain. Works in create mode (and edit mode if
        the deformer has no geometry added yet).
    
    - strength : s                   (float)         [create]
        Set the strength of texture deformer. Strength determines how strong the object
        is deformed.
    
    - vectorOffset : vo              (float, float, float) [create]
        Set the vector offset of texture deformer. Vector offset indicates the offset of
        the deformation on the vector mode.
    
    - vectorSpace : vsp              (unicode)       [create]
        Set the vector space of texture deformer. It can only handle three strings:
        Object, Worldand Tangent. Objectuse color vector in object space Worlduse color
        vector in world space Tangentuse color vector in tangent space strings.
    
    - vectorStrength : vs            (float, float, float) [create]
        Set the vector strength of texture deformer. Vector strength determines how
        strong the object is deformed on the vector mode.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.textureDeformer`
    """
    pass


def bakeSimulation(*args, **kwargs):
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
    list or range (see Examples). The bakeSimulation command is obsolete.  Instead,
    bakeResults -simulation trueshould be used.  The bakeSimulation command has
    retained for backwards compatibility. This command allows the user to replace a
    chain of dependency nodes, or implicit relationship, such as those between
    joints and IK handles, which define the value of an attribute, with a single
    animation curve. Command allows the user to specify the range and frequency of
    sampling. Unlike the bakeResults command, this command will actually set the
    time of the current scene to all the times, in sequence, inside the given time
    interval before it sets the time back to when it is started. As a result, it may
    modify the scene. In query mode, return type is based on queried flag.
    
    Flags:
    - animation : an                 (unicode)       [create]
        Where this command should get the animation to act on.  Valid values are
        objects,keys,and keysOrObjectsDefault: keysOrObjects.(See Description for
        details.)
    
    - attribute : at                 (unicode)       [create]
        List of attributes to select
    
    - bakeOnOverrideLayer : bol      (bool)          [create]
        If true, all layered and baked attributes will be added as a top override layer.
    
    - controlPoints : cp             (bool)          [create]
        This flag explicitly specifies whether or not to include the control points of a
        shape (see -sflag) in the list of attributes. Default: false.  (Not valid for
        pasteKeycmd.)
    
    - destinationLayer : dl          (unicode)       [create]
        This flag can be used to specify an existing layer where the baked results
        should be stored.
    
    - disableImplicitControl : dic   (bool)          [create]
        Whether to disable implicit control after the anim curves are obtained as the
        result of this command. An implicit control to an attribute is some function
        that affects the attribute without using an explicit dependency graph
        connection. The control of IK, via ik handles, is an example.
    
    - float : f                      (floatrange)    [create]
        value uniquely representing a non-time-based key (or key range) on a time-based
        animCurve.  Valid floatRange include single values (-f 10) or a string with a
        lower and upper bound, separated by a colon (-f 10:20
    
    - hierarchy : hi                 (unicode)       [create]
        Hierarchy expansion options.  Valid values are above,below,both,and none.(Not
        valid for pasteKeycmd.)
    
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
    
    - minimizeRotation : mr          (bool)          [create]
        Specify whether to minimize the local euler component from key to key during
        baking of rotation channels.
    
    - oversamplingRate : osr         (int)           []
    
    - preserveOutsideKeys : pok      (bool)          [create]
        Whether to preserve keys that are outside the bake range when there are directly
        connected animation curves.  The default (false) is to remove frames outside the
        bake range.  If the channel that you are baking is not controlled by a single
        animation curve, then a new animation curve will be created with keys only in
        the bake range.
    
    - removeBakedAnimFromLayer : rba (bool)          [create]
        If true, all baked animation will be removed from the layer.
    
    - removeBakedAttributeFromLayer : ral (bool)          [create]
        If true, all baked attributes will be removed from the layer.
    
    - resolveWithoutLayer : rwl      (unicode)       [create]
        This flag can be used to specify a list of layers to be merged together during
        the bake process. This is a multi-use flag. Its name refers to the fact that
        when solving for the value to key, it determines the proper value to key on the
        destination layer to achieve the same result as the merged layers.
    
    - sampleBy : sb                  (time)          [create]
        Amount to sample by. Default is 1.0 in current timeUnit
    
    - shape : s                      (bool)          [create]
        Consider attributes of shapes below transforms as well, except controlPoints.
        Default: true.  (Not valid for pasteKeycmd.)
    
    - simulation : sm                (bool)          [create]
        Using this flag instructs the command to preform a simulation instead of just
        evaluating each attribute separately over the range of time. The simulation flag
        is required to bake animation that that depends on the whole scene being
        evaluated at each time step such as dynamics. The default is true.
    
    - smart : sr                     (bool, float)   [create]
        Specify whether to enable smart bake and the optional smart bake tolerance.
    
    - sparseAnimCurveBake : sac      (bool)          [create]
        When baking anim curves, do not insert any keys into areas of the curve where
        animation is defined.  And, use as few keys as possible to bake the pre and post
        infinity behaviors.  When this is false, one key will be inserted at each time
        step.  The default is false.
    
    - time : t                       (timerange)     [create]
        time uniquely representing a key (or key range) on a time-based animCurve. See
        the code examples below on how to format for a single frame or frame ranges.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.bakeSimulation`
    """
    pass


contstraintCmdName = 'tangentConstraint'
