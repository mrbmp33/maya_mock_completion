from pymel.internal.pmcmds import convertTessellation
from pymel.internal.pmcmds import renderLayerPostProcess
from pymel.internal.pmcmds import surfaceShaderList
from pymel.internal.pmcmds import displacementToPoly
from pymel.internal.pmcmds import uvLink
from pymel.internal.pmcmds import viewClipPlane
from pymel.internal.pmcmds import renderManip
from pymel.internal.pmcmds import setRenderPassType
from pymel.internal.pmcmds import psdTextureFile
from pymel.internal.pmcmds import mayaHasRenderSetup
from pymel.internal.pmcmds import renderPartition
from pymel.internal.pmcmds import makebot
from pymel.internal.pmcmds import editRenderLayerAdjustment
from pymel.internal.pmcmds import viewHeadOn
from pymel.internal.pmcmds import panZoom
from pymel.internal.pmcmds import iprEngine
from pymel.internal.pmcmds import renderQualityNode
from pymel.internal.pmcmds import surfaceSampler
from pymel.internal.pmcmds import render
from pymel.internal.pmcmds import renderInfo
from pymel.internal.pmcmds import doBlur
from pymel.internal.pmcmds import psdExport
from pymel.internal.pmcmds import renderGlobalsNode
from pymel.internal.pmcmds import hwRender
from pymel.internal.pmcmds import renderPassRegistry
from pymel.internal.pmcmds import showShadingGroupAttrEditor
from pymel.internal.pmcmds import convertSolidTx
from pymel.internal.pmcmds import projectionManip
from pymel.internal.pmcmds import viewLookAt
from pymel.internal.pmcmds import resolutionNode
from pymel.internal.pmcmds import editRenderLayerGlobals
from pymel.internal.pmcmds import tumble
from pymel.internal.pmcmds import glRenderEditor
from pymel.internal.pmcmds import checkDefaultRenderGlobals
from pymel.internal.pmcmds import viewCamera
from pymel.internal.pmcmds import viewSet
from pymel.internal.pmcmds import glRender
from pymel.internal.pmcmds import orbit
from pymel.internal.pmcmds import lightlink
from pymel.internal.pmcmds import nodePreset
from pymel.internal.pmcmds import hwRenderLoad
from pymel.internal.pmcmds import ogsRender
from pymel.internal.pmcmds import convertIffToPsd
from pymel.internal.pmcmds import sampleImage
from pymel.internal.pmcmds import soloMaterial
from pymel.internal.pmcmds import getRenderTasks
from pymel.internal.pmcmds import viewFit
from pymel.internal.pmcmds import preferredRenderer
from pymel.internal.pmcmds import setDefaultShadingGroup
from pymel.internal.pmcmds import frameBufferName
from pymel.internal.pmcmds import lookThru
from pymel.internal.pmcmds import assignViewportFactories
from pymel.internal.pmcmds import track
from pymel.internal.pmcmds import shadingConnection
from pymel.internal.pmcmds import renderThumbnailUpdate
from pymel.internal.pmcmds import perCameraVisibility
from pymel.internal.pmcmds import getRenderDependencies
from pymel.internal.pmcmds import listCameras
from pymel.internal.pmcmds import roll
from pymel.internal.pmcmds import renderSettings
from pymel.internal.pmcmds import shadingNetworkCompare
from pymel.internal.pmcmds import createLayeredPsdFile
from pymel.internal.pmcmds import viewPlace
from pymel.internal.pmcmds import binMembership
from pymel.internal.pmcmds import swatchRefresh
from pymel.internal.pmcmds import dolly
from pymel.internal.pmcmds import psdEditTextureFile
from pymel.internal.pmcmds import editRenderLayerMembers

if False:
    from typing import Dict, List, Tuple, Union, Optional


def cameraView(*args, **kwargs):
    """
    This command creates a preset view for a camera which is then independent of the
    camera. The view stores a camera's eye point, center of interest point, up
    vector, tumble pivot, horizontal aperture, vertical aperature, focal length,
    orthographic width, and whether the camera is orthographic or perspective by
    default. Or you can only store 2D pan/zoom attributes by setting the
    bookmarkType to 1. These settings can be applied to any other camera through the
    set camera flag. This command can be used for creation or edit of camera view
    objects.  This command can only be executed with one of the add bookmark, or
    remove bookmark and one of set camera, or the set view flags set.
    
    Flags:
    - addBookmark : ab               (bool)          [create,edit]
        Associate this view with the camera specified or the camera in the active model
        panel. This flag can be used for creation or edit.
    
    - animate : an                   (bool)          [create,edit]
        Set the animation capability for view switches.
    
    - bookmarkType : typ             (int)           [create]
        Specify the bookmark type, which can be: 0. 3D bookmark; 1. 2D Pan/Zoom
        bookmark.
    
    - camera : c                     (PyNode)        [edit]
        Specify the camera to use. This flag should be used in conjunction with the add
        bookmark, remove bookmark, set camera, or set view flags. If this flag is not
        specified the camera in the active model panel will be used.
    
    - name : n                       (unicode)       [create]
        Set the name of the view. This flag can only be used for creation.
    
    - removeBookmark : rb            (bool)          [edit]
        Remove the association of this view with the camera specified or the camera in
        the active model panel. This can only be used with edit.
    
    - setCamera : sc                 (bool)          [edit]
        Set this view into a camera specified by the camera flag or the camera in the
        active model panel. This flag can only be used with edit.
    
    - setView : sv                   (bool)          [edit]
        Set the camera view to match a camera specified or the active model panel. This
        flag can only be used with edit.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.cameraView`
    """
    pass


def lsThroughFilter(*args, **kwargs):
    """
    List all objects in the world that pass a given filter.
    
    Modifications:
      - returns an empty list when the result is None
      - returns wrapped classes
    
    Flags:
    - item : it                      (unicode)       [create]
        Run the filter on specified node(s), using the fast version of this command.
    
    - nodeArray : na                 (bool)          [create]
        Fast version that runs an entire array of nodes through the filter at one time.
    
    - reverse : rv                   (bool)          [create]
        Only available in conjunction with nodeArray flag. Reverses the order of nodes
        in the returned arrays if true.
    
    - selection : sl                 (bool)          [create]
        Run the filter on selected nodes only, using the fast version of this command.
    
    - sort : so                      (unicode)       [create]
        Only available in conjunction with nodeArray flag. Orders the nodes in the
        returned array. Current options are: byName, byType, and byTime.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.lsThroughFilter`
    """
    pass


def lightList(*args, **kwargs):
    """
    Add/Remove a relationship between an object and the current light. Soon to be
    replaced by the connect-attribute command. In query mode, return type is based
    on queried flag.
    
    Flags:
    - add : add                      (PyNode)        [create]
        add object(s) to light list.
    
    - remove : rm                    (PyNode)        [create]
        remove object(s) to light list.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.lightList`
    """
    pass


def ambientLight(*args, **kwargs):
    """
    TlightCmd is the base class for other light commands. The ambientLight command
    is used to edit the parameters of existing ambientLights, or to create new ones.
    The default behaviour is to create a new ambientlight. This is the commmand that
    instantiates an ambientLight or edits the parameters of an existing one.
    TambientLightCmd inherits from TlightCmd which defines common flags like
    intensity, colour etc. See TlightCmd for a global picture of the light commands.
    Note that the flag fAmbientLightUsed indicates whether the command uses any
    ambient specific flags. That is, if a command doesn't use flags defined here,
    the boolean fAmbientLightUsed is set to false and thus the undo/redo information
    is not saved at this level. TambientLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly different behaviour is
    that it calls up to TlightCmd to complete the functionality of the command.
    Example      parseArgs:  TambientLightCmd defines ambientLight specific
    parameters like -ambientShade however, several other parameters are available in
    TlightCmd such as -intensity etc.  So when parsing the arguments, a call is made
    to TlightCmd::parseArgs to parse common parameters (like Intensity).
    
    Flags:
    - ambientShade : ambientShade    (float)         [create,query,edit]
        ambientShade
    
    - discRadius : drs               (float)         [create,query,edit]
        radius of the disc around the light
    
    - exclusive : exc                (bool)          [create,query]
        True if the light is exclusively assigned
    
    - intensity : i                  (float)         [create,query]
        Intensity of the light
    
    - name : n                       (unicode)       [create,query]
        Name of the light
    
    - position : pos                 (float, float, float) [create,query]
        Position of the light
    
    - rgb : rgb                      (float, float, float) [create,query]
        RGB colour of the light
    
    - rotation : rot                 (float, float, float) [create,query]
        Rotation of the light for orientation, where applicable
    
    - shadowColor : sc               (float, float, float) [create,query]
        Color of the light's shadow
    
    - shadowDither : sd              (float)         [create,query,edit]
        dither the shadow
    
    - shadowSamples : sh             (int)           [create,query,edit]
        number of shadow samples.
    
    - softShadow : ss                (bool)          [create,query,edit]
        soft shadow
    
    - useRayTraceShadows : rs        (bool)          [create,query]
        True if ray trace shadows are to be used                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.ambientLight`
    """
    pass


def rampColorPort(*args, **kwargs):
    """
    This command creates a control that displays an image representing the ramp node
    specified, and supports editing of that node.
    
    Flags:
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
    
    - node : n                       (PyNode)        [create]
        Specifies the name of the newRamp texture node this port will represent.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - selectedColorControl : sc      (unicode)       [create,edit]
        Set the name of the control (if any) which is to be used to show the color of
        the currently selected entry in the ramp. This control will automatically update
        as the user selects different entries in the ramp, and will modify the selected
        entry if edited. The type of control must be an attrColorSliderGrp.
    
    - selectedInterpControl : si     (unicode)       [create,edit]
        Set the name of the control (if any) which is to be used to show the
        interpolation of the currently selected entry in the ramp. This control will
        automatically update as the user selects different entries in the ramp, and will
        modify the selected entry if edited. The type of control must be an
        attrEnumOptionMenuGrp.
    
    - selectedPositionControl : sp   (unicode)       [create,edit]
        Set the name of the control (if any) which is to be used to show the position of
        the currently selected entry in the ramp. This control will automatically update
        as the user selects different entries in the ramp, and will modify the selected
        entry if edited. The type of control must be an attrFieldSliderGrp.
    
    - statusBarMessage : sbm         (unicode)       [create,edit]
        Extra string to display in the status bar when the mouse is over the control.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - verticalLayout : vl            (bool)          [create,query,edit]
        Set the preview's layout.
    
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
    
    
    Derived from mel command `maya.cmds.rampColorPort`
    """
    pass


def spotLightPreviewPort(*args, **kwargs):
    """
    This command creates a 3dPort that displays an image representing the
    illumination provided by the spotLight. It is a picture of a plane being
    illuminated by a light. The optional argument is the name of the 3dPort.
    
    Flags:
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
    
    - spotLight : sl                 (PyNode)        [create]
        Name of the spotLight.
    
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
        overruled by parent layout conditions.
    
    - widthHeight : wh               (int, int)      [create]
        The width and height of the port.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.spotLightPreviewPort`
    """
    pass


def pointLight(*args, **kwargs):
    """
    The pointLight command is used to edit the parameters of existing pointLights,
    or to create new ones. The default behaviour is to create a new pointlight.
    
    Flags:
    - decayRate : d                  (int)           [create,query,edit]
        decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
    
    - discRadius : drs               (float)         [create,query,edit]
        radius of the disc around the light
    
    - exclusive : exc                (bool)          [create,query,edit]
        This flag is obsolete.
    
    - intensity : i                  (float)         [create,query,edit]
        intensity of the light (expressed as a percentage)
    
    - name : n                       (unicode)       [create,query,edit]
        specify the name of the light
    
    - position : pos                 (float, float, float) [create,query,edit]
        This flag is obsolete.
    
    - rgb : rgb                      (float, float, float) [create,query,edit]
        color of the light (0-1)
    
    - rotation : rot                 (float, float, float) [create,query,edit]
        This flag is obsolete.
    
    - shadowColor : sc               (float, float, float) [create,query,edit]
        the shadow color
    
    - shadowDither : sd              (float)         [create,query,edit]
        dither the shadow
    
    - shadowSamples : sh             (int)           [create,query,edit]
        number of shadow samples.
    
    - softShadow : ss                (bool)          [create,query,edit]
        soft shadow
    
    - useRayTraceShadows : rs        (bool)          [create,query,edit]
        ray trace shadows                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pointLight`
    """
    pass


def batchRender(*args, **kwargs):
    """
    The batchRender command is used to spawn off a separate rendering session of the
    current maya file. If no mayaFile is specified, it'll ask you whether you want
    the current job killed. The batchRender will spawn a separate maya process in
    which commands will be communicated to it through a commandPort. If Maya is
    unable to find an available port an error will be produced. Maya will attempt to
    use ports 7835 through 7844.
    
    Flags:
    - filename : f                   (unicode)       [create]
        Filename to be rendered; if empty, a temporary filename will be created.
    
    - melCommand : mc                (unicode)       [create]
        Mel command to execute to run a renderer other than the software renderer.
    
    - numProcs : n                   (int)           [create]
        Number of processors to use (0 means use all available processors).
    
    - preRenderCommand : prc         (unicode)       [create]
        Command to be run prior to invoking a batch render.
    
    - remoteRenderMachine : rm       (unicode)       [create]
        Name of remote render machine. Not available on Windows.
    
    - renderCommandOptions : rco     (unicode)       [create]
        Arguments to the render command for batch rendering.
    
    - showImage : si                 (bool)          [create]
        Show progress of the current rendering job.
    
    - status : st                    (unicode)       [create]
        Status string for displaying the batch render status.
    
    - useRemoteRender : um           (bool)          [create]
        If remote rendering is desired. Not available on Windows.
    
    - useStandalone : us             (bool)          [create]
        Batch rendering is to be done by exporting the scene and rendering with a
        standalone renderer.
    
    - verbosity : v                  (int)           [create]
        Defines the verbosity level to report the batch rendering status:1: display only
        one start message, then one message when all frames are rendered.2: display only
        start and end frame messages.3: display all messages (default).Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.batchRender`
    """
    pass


def _directionalLight(*args, **kwargs):
    """
    Maya Bug Fix:
      - name flag was ignored
    """
    pass


def _ambientLight(*args, **kwargs):
    """
    Maya Bug Fix:
      - name flag was ignored
    """
    pass


def psdChannelOutliner(*args, **kwargs):
    """
    Create a psdChannelOutliner control which is capable of displaying a tree
    structure upto one level.
    
    Flags:
    - addChild : ach                 (unicode, unicode) [edit]
        This flag should be used along with the -psdParent/ppaflag. A string item gets
        added as a child to the parent specifed with -psdParent/ppaflag. The next string
        assigns an associated image name.
    
    - allItems : all                 (bool)          [query]
        Returns all the items in the form parent.child.
    
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
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Add a documentation flag to the control.  The documentation flag has a directory
        structure. (e.g., -dt render/multiLister/createNode/material)
    
    - doubleClickCommand : dcc       (unicode)       [create,edit]
        Specify the command to be executed when an item is double clicked.
    
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
    
    - numberOfItems : ni             (bool)          [query]
        Total number of items in the control.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - psdParent : ppa                (unicode)       [edit]
        Adds an item string to the controls which is treated as parent.
    
    - removeAll : ra                 (bool)          [edit]
        Removes all the items from the control.
    
    - removeChild : rc               (unicode)       [edit]
        Deletes the particular child of the parent as specifed in -psdParent/ppaflag.
    
    - select : sel                   (unicode)       [edit]
        Select the named item.
    
    - selectCommand : sc             (unicode)       [create,edit]
        Specify the command to be executed when an item is selected.
    
    - selectItem : si                (bool)          [query]
        Returns the selected items.
    
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
    
    
    Derived from mel command `maya.cmds.psdChannelOutliner`
    """
    pass


def imagePlane(*args, **kwargs):
    """
    The imagePlane command allows querying of various properties of         an image
    plane and any movie in use by the image plane. It also supports         creating
    and edit.         The object passed to the command may either be an imagePlane
    node,         or a camera, in which case the command uses the image plane
    attached         to the camera (if any). If no object is passed in, the current
    selection is used.         Currently, most movie related queries work only on 64
    bit Windows systems.
    
    Flags:
    - camera : c                     (unicode)       [create,query,edit]
        When creating, it will try to attach the created image plane to the specified
        camera. If the given camera is invalid, creating will fail. When querying, it
        will query which camera current image plane is attaching to. If it has no camera
        attached to (free image plane), it will return an empty string. When edit, it
        will make the image plane attach to the new specified camera. If the camera
        given is invalid, it will do nothing. When the image plane is attached to a
        camera, the image plane's transform node will be set identity. The detach
        command will not restore the original position of the image plane. but the undo
        command will restore the original position of the image plane.
    
    - counter : cn                   (bool)          []
        Query the 'counter' flag of the movie's timecode format. If this is true, the
        timecode returned by the -timeCode flag will be a simple counter. If false, the
        returned timecode will be an array of integers (hours, minutes, seconds,
        frames).
    
    - detach : d                     (bool)          [edit]
        This flag can only be used in the edit mode, when this flag is used in edit, it
        will detach current image plane from any camera it attaches to and make it a
        free image plane.
    
    - dropFrame : df                 (bool)          [query]
        Query the 'drop frame' flag of the movie's timecode format.
    
    - fileName : fn                  (unicode)       [create,edit]
        Set the image name for image plane to read.
    
    - frameDuration : fd             (int)           [query]
        Query the frame duration of the movie's timecode format.
    
    - height : h                     (float)         [create,query,edit]
        Height of the image plane. When creating, if this flag is not specified, it will
        use 10.0 as default height.
    
    - imageSize : iz                 (int, int)      [query]
        Get size of the loaded image.
    
    - lookThrough : lt               (unicode)       [create,query,edit]
        The camera currently used for image plane to look through.
    
    - maintainRatio : mr             (bool)          [create,query,edit]
        Let the image plane respect the picture aspect ratio. When creating, if this
        flag is not specified, it will use true as default value.
    
    - name : n                       (unicode)       [create,query]
        Set the image plane node name when creating or return the image plane name when
        querying.
    
    - negTimesOK : nt                (bool)          [query]
        Query the 'neg times OK' flag of the movie's timecode format.
    
    - numFrames : nf                 (int)           [query]
        Query the whole number of frames per second of the movie's timecode format.
    
    - quickTime : qt                 (bool)          [query]
        Query whether the image plane is using a QuickTime movie.
    
    - showInAllViews : sia           (bool)          [create,query,edit]
        The flag is used to show the current image plane in all views or not.
    
    - timeCode : tc                  (int)           [query]
        Query the whole number of frames per second of the movie's timecode format.
    
    - timeCodeTrack : tt             (bool)          [query]
        Query whether the movie on the image plane has a timecode track.
    
    - timeScale : ts                 (int)           [query]
        Query the timescale of the movie's timecode format.
    
    - twentyFourHourMax : tf         (bool)          [query]
        Query the '24 hour max' flag of the movie's timecode format.
    
    - width : w                      (float)         [create,query,edit]
        Width of the image plane. When creating, if this flag is not specified, it will
        use 10.0 as default width.                                 Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.imagePlane`
    """
    pass


def renderWindowEditor(*args, **kwargs):
    """
    Create a editor window that can receive the result of the rendering process
    
    Flags:
    - autoResize : ar                (bool)          [create,query,edit]
        Lets the render view editor automatically resize the viewport or not.
    
    - blendMode : blm                (int)           [create,query,edit]
        Sets the blend mode for the render view. New image sent to the render view will
        be blended with the previous image in the render view, and the composited image
        will appear.
    
    - caption : cap                  (unicode)       [create,query,edit]
        Sets the caption which appears at the bottom of the render view.
    
    - changeCommand : cc             (unicode, unicode, unicode, unicode) [create,query,edit]
        Parameters: First string: commandSecond string: editorNameThird string:
        editorCmdFourth string: updateFuncCall the command when something changes in the
        editor The command should have this prototype :  command(string $editor, string
        $editorCmd, string $updateFunc, int $reason)  The possible reasons could be : 0:
        no particular reason1: scale color2: buffer (single/double)3: axis 4: image
        displayed5: image saved in memory
    
    - clear : cl                     (int, int, float, float, float) [create,query,edit]
        Clear the image with the given color at the given resolution. Argumnets are
        respecively: width height red green blue.
    
    - cmEnabled : cme                (bool)          [query,edit]
        Turn on or off applying color management in the View.  If set, the color
        management configuration set in the current view is used.
    
    - colorManage : com              (bool)          [edit]
        When used with the writeImage flag, causes the written image to be color-managed
        using the settings from the view color manager attached to the view.
    
    - compDisplay : cd               (int)           [create,query,edit]
        0 : disable compositing.1 : displays the composited image immediately. For
        example, when foreground layer tile is sent to the render view window, the
        composited tile is displayed in the render view window, and the original
        foreground layer tile is not displayed.2 : display the un-composited image, and
        keep the composited image for the future command. For example, when foreground
        layer tile is sent to the render view window, the original foreground layer tile
        is not displayed, and the composited tile is stored in a buffer.3 : show the
        current composited image. If there is a composited image in the buffer, display
        it.
    
    - compImageFile : cif            (unicode)       [create,query,edit]
        Open the given image file and blend with the buffer as if the image was just
        rendered.
    
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - currentCamera : crc            (unicode)       [create,query,edit]
        Get or set the current camera. (used when redoing last render)
    
    - currentCameraRig : crg         (unicode)       [create,query,edit]
        Get or set the current camera rig name. If a camera rig is specified, it will be
        used when redoing the last render as opposed to the currentCamera value, as the
        currentCamera value will hold the child camera last used for rendering the
        camera rig.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - displayImage : di              (int)           [query,edit]
        Set a particular image in the Editor Image Stack as the current Editor Image.
        Images are added to the Editor Image Stack using the si/saveImageflag.
    
    - displayImageViewCount : dvc    (int)           [query]
        Query the number of views stored for a given image in the Editor Image Stack.
        This is not the same as querying using viewImageCountwhich returns the number of
        views for the current rendered image.
    
    - displayStyle : dst             (unicode)       [create,query,edit]
        Set the mode to display the image. Valid values are: colorto display the basic
        RGB imagemaskto display the mask channellumto display the luminance of the image
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - doubleBuffer : dbf             (bool)          [create,query,edit]
        Set the display in double buffer mode
    
    - drawAxis : da                  (bool)          [create,query,edit]
        Set or query whether the axis will be drawn.
    
    - editorName : en                (bool)          [query]
        Returns the name of the editor, or an empty string if the editor has not been
        created yet.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - exposure : exp                 (float)         [query,edit]
        The exposure value used by the color management of the current view.
    
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
    
    - frameImage : fi                (bool)          [create,query,edit]
        Frames the image inside the window.
    
    - frameRegion : fr               (bool)          [create,query,edit]
        Frames the region inside the window.
    
    - gamma : ga                     (float)         [query,edit]
        The gamma value used by the color management of the current view.
    
    - highlightConnection : hlc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its highlight list. Not all editors have a highlight list. For
        those that do, it is a secondary selection list.
    
    - loadImage : li                 (unicode)       [edit]
        load an image from disk and set it as the current Editor Image
    
    - lockMainConnection : lck       (bool)          [create,edit]
        Locks the current list of objects within the mainConnection, so that only those
        objects are displayed within the editor. Further changes to the original
        mainConnection are ignored.
    
    - mainListConnection : mlc       (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object.
    
    - marquee : mq                   (float, float, float, float) [create,query,edit]
        The arguments define the four corners of a rectangle: top left bottom right. The
        rectangle defines a marquee for the render computation.
    
    - nbImages : nim                 (bool)          [query]
        returns the number of images
    
    - nextViewImage : nvi            (bool)          [create,edit]
        The render editor has the capability to render multiple cameras within a single
        view. This is different from image binning where an image is saved. Multiple
        image views are useful for comparing two different camera renders side-by-side.
        The nextViewImage flag tells the editor that it should prepare its internal
        image storage mechanism to store to the next view location.
    
    - outputColorManage : ocm        (bool)          [edit]
        When used with the writeImage flag, causes the written image to be color-managed
        using the outpute color space in the color preferences attached to the view.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - pcaption : pca                 (unicode)       [create,query,edit]
        Get or set the permanent caption which appears under the image that is currently
        showing in the render editor.
    
    - realSize : rs                  (bool)          [create,query,edit]
        Display the image with a one to one pixel match.
    
    - refresh : ref                  (bool)          [edit]
        requests a refresh of the current Editor Image.
    
    - removeAllImages : ra           (bool)          [edit]
        remove all the Editor Images from the Editor Image Stack
    
    - removeImage : ri               (bool)          [edit]
        remove the current Editor Image from the Editor Image Stack
    
    - resetRegion : rr               (bool)          [create,query,edit]
        Forces a reset of any marquee/region.
    
    - resetViewImage : rvi           (bool)          [create,edit]
        The render editor has the capability to render multiple cameras within a single
        view. This is different from image binning where an image is saved. Multiple
        image views are useful for comparing two different camera renders side-by-side.
        The resetViewImage flag tells the editor that it should reset its internal image
        storage mechanism to the first image. This would happen at the very start of a
        render view render.
    
    - saveImage : si                 (bool)          [edit]
        save the current Editor Image to memory. Saved Editor Images are stored in an
        Editor Image Stack. The most recently saved image is stored in position 0, the
        second most recently saved image in position 1, and so on... To set the current
        Editor Image to a previously saved image use the di/displayImageflag.
    
    - scaleBlue : sb                 (float)         [create,query,edit]
        Define the scaling factor for the blue component in the View. The default value
        is 1 and can be between -1000 to +1000
    
    - scaleGreen : sg                (float)         [create,query,edit]
        Define the scaling factor for the green component in the View. The default value
        is 1 and can be between -1000 to +1000
    
    - scaleRed : sr                  (float)         [create,query,edit]
        Define the scaling factor for the red component in the View. The default value
        is 1 and can be between -1000 to +1000
    
    - selectionConnection : slc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its own selection list. As the user selects things in this
        editor, they will be selected in the selectionConnection object. If the object
        undergoes changes, the editor updates to show the changes.
    
    - showRegion : srg               (int, int)      [create,query,edit]
        Shows the current region at the given resolution. The two parameters define the
        width and height.
    
    - singleBuffer : sbf             (bool)          [create,query,edit]
        Set the display in single buffer mode
    
    - snapshot : snp                 (unicode, int, int) [create,query,edit]
        Makes a copy of the camera of the model editor at the given size. First argument
        is the editor name, second is the width, third is the height.
    
    - snapshotMode : snm             (bool)          [create,query,edit]
        Get or set the window's snapshot mode.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - stereo : s                     (int)           [create,query,edit]
        Puts the editor into stereo image mode.  The effective resolution of the output
        image is twice the size of the horizontal size. The orientation of the images
        can be set using the stereoOrientation flag.
    
    - stereoImageOrientation : sio   (unicode, unicode) [create,query,edit]
        Specifies the orientation of stereo camera renders.  The first argument
        specifies the orientation value for the firstleft image and the second argument
        specifies the orientation value for the right image. The orientation values are
        'normal', the image appears as seen throught he camera, or 'mirrored', the image
        is mirrored horizontally.
    
    - stereoMode : sm                (unicode)       [create,query,edit]
        Specifies how the image is displayed in the view.  By default the stereo is
        rendered with a side by side image.  The rendered image is a single image that
        is twice the size of a normal image, 'both'. Users can also choose to display as
        'redcyan', 'redcyanlum', 'leftonly', 'rightonly', or 'stereo'.  both - displays
        both the left and right redcyan - displays the images as a red/cyan pair.
        redcyanlum - displays the luminance of the images as a red/cyan pair. leftonly -
        displays the left side only rightonly - displays the right side only stereo -
        mode that supports Crystal Eyes(tm) or Zscreen (tm) renders
    
    - toggle : tgl                   (bool)          [create,query,edit]
        Turns the ground plane display on/off.
    
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
    
    - viewImageCount : vic           (int)           [create,query,edit]
        The render editor has the capability to render multiple cameras within a single
        view. This is different from image binning where an image is saved. Multiple
        image views are useful for comparing two different camera renders side-by-side.
        The viewImageCount flag tells the editor that it should prepare its internal
        image storage mechanism for a given number of views.
    
    - viewTransformName : vtn        (unicode)       [query,edit]
        Sets/gets the view transform to be applied if color management is enabled in the
        current view.
    
    - writeImage : wi                (unicode)       [edit]
        write the current Editor Image to disk                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.renderWindowEditor`
    """
    pass


def defaultLightListCheckBox(*args, **kwargs):
    """
    This command creates a checkBox that controls whether a shadingGroup is
    connected/disconnected from the defaultLightList.
    
    Flags:
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
    
    - label : l                      (unicode)       [create,edit]
        Value of the checkbox label
    
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
    
    - shadingGroup : sg              (PyNode)        [create,edit]
        The shading group that is to be connected/disconnected from the
        defaultLightList.
    
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
    
    
    Derived from mel command `maya.cmds.defaultLightListCheckBox`
    """
    pass


def _spotLight(*args, **kwargs):
    """
    Maya Bug Fix:
      - name flag was ignored
    """
    pass


def layeredTexturePort(*args, **kwargs):
    """
    This command creates a 3dPort that displays an image representing the layered
    texture node specified.
    
    Flags:
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
    
    - node : n                       (PyNode)        [create]
        Specifies the name of the newLayeredTexture node this port will represent.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - selectedAlphaControl : sac     (unicode)       [create]
        Specifies the name of the UI-control that represents the currently selected
        layer's alpha.
    
    - selectedBlendModeControl : sbc (unicode)       [create]
        Specifies the name of the UI-control that represents the currently selected
        layer's blend mode.
    
    - selectedColorControl : scc     (unicode)       [create]
        Specifies the name of the UI-control that represents the currently selected
        layer's color.
    
    - selectedIsVisibleControl : svc (unicode)       [create]
        Specifies the name of the UI-control that represents the currently selected
        layer's visibility.
    
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
    
    
    Derived from mel command `maya.cmds.layeredTexturePort`
    """
    pass


def camera(*args, **kwargs):
    """
    Create, edit, or query a camera with the specified properties. The resulting
    camera can be repositioned using the viewPlace command. Many of the camera
    settings only affect the resulting rendered image. E.g. the F/Stop, shutter
    speed, the film related options, etc. Scaling the camera icon does not change
    any camera properties.
    
    Flags:
    - aspectRatio : ar               (float)         [create,query,edit]
        The ratio of the film back width to the film back height.
    
    - cameraScale : cs               (float)         [create,query,edit]
        Scale the camera.
    
    - centerOfInterest : coi         (float)         [create,query,edit]
        Set the linear distance from the camera's eye point to the center of interest.
    
    - clippingPlanes : cp            (bool)          [create,query,edit]
        Activate manual clipping planes.
    
    - depthOfField : dof             (bool)          [create,query,edit]
        Determines whether a depth of field calculation is performed to give varying
        focus depending on the distance of the objects.
    
    - displayFieldChart : dfc        (bool)          [create,query,edit]
        Activate display of the video field chart when looking through the camera.
    
    - displayFilmGate : dfg          (bool)          [create,query,edit]
        Activate display of the film gate icons when looking through the camera.
    
    - displayFilmOrigin : dfo        (bool)          [create,query,edit]
        Activate the display of the film origin guide when looking through the camera.
    
    - displayFilmPivot : dfp         (bool)          [create,query,edit]
        Activate display of the film pivot guide when looking through the camera.
    
    - displayGateMask : dgm          (bool)          [create,query,edit]
        Display the gate mask, file or resolution, as a shaded area to the edge of the
        viewport.
    
    - displayResolution : dr         (bool)          [create,query,edit]
        Activate display of the current rendering resolution (as defined in the render
        globals) when looking through the camera.
    
    - displaySafeAction : dsa        (bool)          [create,query,edit]
        Activate display of the video Safe Action guide when looking through the camera.
    
    - displaySafeTitle : dst         (bool)          [create,query,edit]
        Activate display of the video Safe Title guide when looking through the camera.
    
    - fStop : fs                     (float)         [create,query,edit]
        A real lens normally contains a diaphragm or other stop which blocks some of the
        light that would otherwise pass through it. This stop is usually approximately
        round, and its diameter as seen from the front of the lens is called the lens
        diameter. The lens diameter is often described by its relation to the focal
        length of the lens. A lens whose diameter is one-eighth its local length is said
        to have an F-stop of 8. This is an optical property of the lens.
    
    - farClipPlane : fcp             (float)         [create,query,edit]
        Specify the distance to the far clipping plane.
    
    - farFocusDistance : ffd         (float)         [create,query,edit]
        Linear distance to the far focus plane.
    
    - filmFit : ff                   (unicode)       [create,query,edit]
        This describes how the digital image (in pixels) relates to the film back. Since
        the film back is defined in terms of real numbers with some arbitrary film
        aspect, and the digital image is defined in integer pixels with an equally
        arbitrary (and different) resolution, relating the two can get complicated.
        There are 4 choices: horizontal In this case the digital image is made to fit
        the film back exactly in the horizontal direction. This then gives each pixel a
        horizontal size = (film back width) / (horizontal resolution). The pixel height
        is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size,
        resolution gives us a complete image. That image will match the film back
        exactly in width. It will almost never match in height, either being too tall or
        too short. By playing with the numbers you can get it pretty close
        though.verticalThis is the same idea as horizontal fit, only applied vertically.
        Thus the digital image will match the film back exactly in height, but miss in
        width.fillThis is a convenience item. The system calculates both horizontal and
        vertical fits and then applies the one that makes the digital image larger than
        the film back.overscanOverscanning the film gate in the camera view allows us to
        choreograph action outside of the frustum from within the camera view without
        having to resort to a dolly or zoom. This feature is also essential for
        animating image planes.
    
    - filmFitOffset : ffo            (float)         [create,query,edit]
        Since we know from the above that the digital image may not match the film back
        exactly, we now have the question of how to position one relative to the other.
        Thus fit offset. Normally the centers are aligned. Fit offset lets you move the
        smaller image within the larger one. Specify the distance for film offset
        (inches).
    
    - filmRollOrder : fro            (unicode)       [create,query,edit]
        Specifies how the roll is applied with respect to the pivot value. Rotate-
        TranslateThe film back is first rotated then translated by the pivot point value
        .Translate-RotateThe film back is first translated then rotated by the film roll
        value.
    
    - filmRollValue : frv            (float)         [create,query,edit]
        This specifies that amount of rotation around the film back. The roll value is
        specified in degrees. The rotation occurs around the specified pivot point. This
        value is used to compute a film roll matrix, which is a component of the post-
        projection matrix.
    
    - filmTranslateH : fth           (float)         [create,query,edit]
        The horizontal film translation. Values are normalized to the viewing area.
    
    - filmTranslateV : ftv           (float)         [create,query,edit]
        The vertical film translation. Values are normalized to the viewing area.
    
    - focalLength : fl               (float)         [create,query,edit]
        This is the distance along the lens axis between the lens and the film plane
        when focal distanceis infinitely large. This is an optical property of the lens.
        This double precision parameter is always specified in millimeters.
    
    - focusDistance : fd             (float)         [create,query,edit]
        Set the focus at a certain distance in front of the camera.
    
    - homeCommand : hc               (unicode)       [create,query,edit]
        Specify the command to execute when viewSet -homeis applied to this camera. All
        occurances of %camerawill be replaced with the cameras name before viewSet runs
        the command.
    
    - horizontalFieldOfView : hfv    (float)         [create,query,edit]
        This is the film back width as seen by the lens when focused at infinity (ie.,
        focal length away) measured as an angle. Note that it has nothing to do with
        pixels or the digital image or any aspects. Angle of view is a derived field,
        that is, it is not used internally by Alias and can be completely determined
        from other information. It is included as a convenience for the user. Its
        derivation is aov = 2 \* atan( fbw / (2 \* f) ) where aovis the angle of view,
        fbwis the film back width and fis the focal length.
    
    - horizontalFilmAperture : hfa   (float)         [create,query,edit]
        The horizontal width of the camera's film plane. The camera's film is located on
        the film plane. The extent of the film which will be exposed to an image of the
        scene in front of the lens is limited to a rectangular area described by the
        film back. This double precision parameter is always specified in inches.
    
    - horizontalFilmOffset : hfo     (float)         [create,query,edit]
        Horizontal offset from the center of the film back. Normally the film back will
        be centered on the lens axis. However, this need not be so. Film offset is the
        displacement of the center of the film back from the lens axis, also measured in
        inches. Note that offsetting the film back will distort the image, but will not
        alter the focus. This double precision parameter is always specified in inches.
    
    - horizontalPan : hpn            (float)         [create,query,edit]
        Horizontal 2D camera pan (inches)
    
    - horizontalRollPivot : hrp      (float)         [create,query,edit]
        The horizontal pivot point from the center of the film back. The pivot point is
        used during rotation of the film back.  The pivot is the point where the
        rotation occurs around. This double precision parameter corresponds to the
        normalized viewport. This value is a part of the post projection matrix.
    
    - horizontalShake : hs           (float)         [create,query,edit]
        Another horizontal offset from the center of the film back, which can be used
        and stored on the camera in addition to the horizonal film offset attribute.
        This allows for film-based camera shake internal to the camera.  This works in
        exactly the same units and coordinates that the film offset attribute does. The
        effect of this attribute is toggled by the shake enabled attribute.
    
    - journalCommand : jc            (bool)          [create,query,edit]
        Journal interactive camera commands. Commands can be undone when a camera is
        journaled.
    
    - lensSqueezeRatio : lsr         (float)         [create,query,edit]
        This is presently just an information field in the camera editor is meant to
        convey the horizontal distortion of the anamorphic lens normally used with some
        film formats. If it were used, it would do something like pixel aspect. Remember
        however that lens distortion (intentional or not) is slightly different than the
        output hardware's quantization. The fact that a netdistortion parameter could be
        used for both may or may not confuse the issue.
    
    - lockTransform : lt             (bool)          [create,query,edit]
        Lock the camera. When a camera is locked, its transformation information, that
        is, its Translate and Rotate properties cannot be adjusted, and the center of
        interest point cannot be moved. For orthographic cameras, Orthographic Width is
        also locked. For camera groups, Aim and Up locator's translate is also locked.
        For stereo cameras, the root camera is locked.
    
    - motionBlur : mb                (bool)          [create,query,edit]
        Determines whether the camera's image is motion blured (as opposed to an
        object's image). For example, if you want to blur the camera movement when you
        are performing a flyby.
    
    - name : n                       (unicode)       [create,query,edit]
        Name of the camera.
    
    - nearClipPlane : ncp            (float)         [create,query,edit]
        Specify the distance to the NEAR clipping plane.
    
    - nearFocusDistance : nfd        (float)         [create,query,edit]
        Linear distance to the near focus plane.
    
    - orthographic : o               (bool)          [create,query,edit]
        Activate the orthographic camera.
    
    - orthographicWidth : ow         (float)         [create,query,edit]
        Set the orthographic projection width.
    
    - overscan : ovr                 (float)         [create,query,edit]
        Set the percent of overscan.
    
    - panZoomEnabled : pze           (bool)          [create,query,edit]
        Toggle camera 2D pan and zoom
    
    - position : p                   (float, float, float) [create,query,edit]
        Three linear values can be specified to translate the camera.
    
    - postScale : pts                (float)         [create,query,edit]
        The post-scale value.  This value multiplied against the computed projection
        matrix. It is applied after the the film roll.
    
    - preScale : prs                 (float)         [create,query,edit]
        The pre-scale value. The value is multiplied against the computed projection
        matrix. It is applied before the film roll.
    
    - renderPanZoom : rpz            (bool)          [create,query,edit]
        Toggle camera 2D pan and zoom in render
    
    - rotation : rot                 (float, float, float) [create,query,edit]
        Three angular values can be specified to rotate the camera.
    
    - shakeEnabled : se              (bool)          [create,query,edit]
        Toggles the effect of the horizontal and vertical shake attributes.
    
    - shakeOverscan : so             (float)         [create,query,edit]
        Controls the amount of overscan in the output rendered image. For use when
        adding film-based camera shake.  Acts as a multiplier to the film aperture on
        the camera.
    
    - shakeOverscanEnabled : soe     (bool)          [create,query,edit]
        Toggles the effect of the shake overscan attribute.
    
    - shutterAngle : sa              (float)         [create,query,edit]
        Specify the shutter angle (degrees).
    
    - startupCamera : sc             (bool)          [create,query,edit]
        A startup camera is marked undeletable and implicit. This flag can be used to
        set or query the startup state of a camera. There must always be at least one
        startup camera.
    
    - stereoHorizontalImageTranslate : hit (float)         [create,query,edit]
        A film-back offset for use in stereo camera rigs.
    
    - stereoHorizontalImageTranslateEnabled : she (bool)          [create,query,edit]
        Toggles the effect of the stereo HIT attribute.
    
    - verticalFieldOfView : vfv      (float)         [create,query,edit]
        Set the vertical field of view.
    
    - verticalFilmAperture : vfa     (float)         [create,query,edit]
        The vertical height of the camera's film plane. This double precision parameter
        is always specified in inches.
    
    - verticalFilmOffset : vfo       (float)         [create,query,edit]
        Vertical offset from the center of the film back. This double precision
        parameter is always specified in inches.
    
    - verticalLock : vl              (bool)          [create,query,edit]
        Lock the size of the vertical film aperture.
    
    - verticalPan : vpn              (float)         [create,query,edit]
        Vertical 2D camera pan (inches)
    
    - verticalRollPivot : vrp        (float)         [create,query,edit]
        Vertical pivot point used for rotating the film back. This double precision
        parameter corresponds to the normalized viewport. This value is used to compute
        the film roll matrix, which is a component of the post projection matrix.
    
    - verticalShake : vs             (float)         [create,query,edit]
        Vertical offset from the center of the film back.  See horizontal shake
        attribute description.  This is toggled by the shake enabled attribute.
    
    - worldCenterOfInterest : wci    (float, float, float) [create,query,edit]
        Camera world center of interest point.
    
    - worldUp : wup                  (float, float, float) [create,query,edit]
        Camera world up vector.
    
    - zoom : zom                     (float)         [create,query,edit]
        The percent over the film viewable frustum to display                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.camera`
    """
    pass


def shadingNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.
    The shadingNode command classifies any DG node as a shader, texture light, post
    process, or utility so that it can be properly organized in the multi-lister.
    Recall that any DG node can be used a part of a a shader, texture or light -
    regardless of how it is classified by this. command. These classifications are
    provided for convenience in the UI.
    
    Flags:
    - asLight : al                   (bool)          [create]
        classify the current DG node as a light
    
    - asPostProcess : app            (bool)          [create]
        classify the current DG node as a post process
    
    - asRendering : ar               (bool)          [create]
        classify the current DG node as a rendering node
    
    - asShader : asShader            (bool)          [create]
        classify the current DG node as a shader
    
    - asTexture : at                 (bool)          [create]
        classify the current DG node as a texture
    
    - asUtility : au                 (bool)          [create]
        classify the current DG node as a utility
    
    - isColorManaged : icm           (bool)          [create]
        classify the current DG node as being color managed
    
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
    
    
    Derived from mel command `maya.cmds.shadingNode`
    """
    pass


def renderer(*args, **kwargs):
    """
    Command to register renders.  This command allows you to specify the UI name and
    procedure names for renderers. The command also allow you to query the UI name
    and the procedure names for the registered renders.              In query mode,
    return type is based on queried flag.
    
    Flags:
    - addGlobalsNode : agn           (unicode)       [create,query,edit]
        This flag allows the user to add a globals node the specified renderer uses.
    
    - addGlobalsTab : agt            (unicode, unicode, unicode) [create,edit]
        Add a tab associated with the specified renderer for the unified render globals
        window.
    
    - batchRenderOptionsProcedure : bro (unicode)       [create,query,edit]
        Set or query the batch render options procedure associated with the specified
        renderer.
    
    - batchRenderOptionsStringProcedure : bso (unicode)       [create,query,edit]
        Set or query the argument string that will be used with the command line utility
        'Render' when doing a batch render
    
    - batchRenderProcedure : br      (unicode)       [create,query,edit]
        Set or query the batch render procedure associated with the specified renderer.
    
    - cancelBatchRenderProcedure : cbr (unicode)       [create,query,edit]
        Set or query returns the cancel batch render procedure associated with the
        specified renderer.
    
    - changeIprRegionProcedure : cir (unicode)       [create,query,edit]
        Set or query the change IPR region procedure associated with the specified
        renderer.
    
    - commandRenderProcedure : cr    (unicode)       [create,query,edit]
        Set or query the command line rendering procedure associated with the specified
        renderer.
    
    - exists : ex                    (bool)          [query,edit]
        The flag returns true if the specified renderer is registered in the registry,
        and it returns false otherwise.
    
    - globalsNodes : gn              (bool)          [create,query,edit]
        This flag returns the list of render globals nodes the specified renderer uses.
    
    - globalsTabCreateProcNames : gtc (bool)          [create,query,edit]
        This flag returns the names of procedures that are used to create the unified
        render globals window tabs that are associated with the specified renderer.
    
    - globalsTabLabels : gtl         (bool)          [create,query,edit]
        This flag returns the labels of unified render globals window tabs that are
        associated with the specified renderer.
    
    - globalsTabUpdateProcNames : gtu (bool)          [create,query,edit]
        This flag returns the names of procedures that are used to update the unified
        render globals window tabs that are associated with the specified renderer.
    
    - iprOptionsMenuLabel : ipm      (unicode)       [create,query,edit]
        Set or query the label for the IPR update options menu which is under the render
        view's IPR menu.
    
    - iprOptionsProcedure : io       (unicode)       [create,query,edit]
        Set or query the IPR render options procedure associated with the specified
        renderer.
    
    - iprOptionsSubMenuProcedure : ips (unicode)       [create,query,edit]
        Set or query the procedure for creating the sub menu for the IPR update options
        menu which is under the render view's IPR menu.
    
    - iprRenderProcedure : ipr       (unicode)       [create,query,edit]
        Set or query the IPR render command associated with the specified renderer.
    
    - iprRenderSubMenuProcedure : irs (unicode)       [create,query,edit]
        Set or query the procedure for creating the sub menu for the IPR render menu
        which is under the render view's IPR menu.
    
    - isRunningIprProcedure : isr    (unicode)       [create,query,edit]
        Set or query the isRunningIpr command associated with the specified renderer.
    
    - logoCallbackProcedure : lgc    (unicode)       [create,query,edit]
        Set or query the procedure which is a callback associated to the logo for the
        specified renderer.   For example, the logo and the callback can be used in the
        unified render globals window beside the Render UsingoptionMenu.
    
    - logoImageName : log            (unicode)       [create,query,edit]
        Set or query the logo image name for the specified renderer. The logo is a image
        representing the renderer.
    
    - materialViewRendererList : mvl (bool)          [query,edit]
        Returns the names of material view renderers that are currently registered.
    
    - materialViewRendererPause : mvp (bool)          [query,edit]
        Specifies whether to pause the material viewer. Useful for globally halting
        updates to the material viewer. The material view renderer will remain suspended
        while the viewer is paused.
    
    - materialViewRendererSuspend : mvs (bool)          [query,edit]
        Specifies whether to suspend or resume the material view renderer. Useful for
        temporarily stopping the material view renderer while another rendering task is
        running.
    
    - namesOfAvailableRenderers : ava (bool)          [query,edit]
        Returns the names of renderers that are currently registered.
    
    - pauseIprRenderProcedure : psi  (unicode)       [create,query,edit]
        Set or query the pause IPR render procedure associated with the specified
        renderer.
    
    - polyPrelightProcedure : pp     (unicode)       [create,query,edit]
        Set or query the polygon prelight procedure associated with the specified
        renderer.
    
    - refreshIprRenderProcedure : rfi (unicode)       [create,query,edit]
        Set or query the refresh IPR render procedure associated with the specified
        renderer.
    
    - renderDiagnosticsProcedure : rd (unicode)       [create,query,edit]
        Set or query the render diagnostics procedure associated with the specified
        renderer.
    
    - renderGlobalsProcedure : rg    (unicode)       [create,query,edit]
        This flag is obsolete.  It will be removed in the next release.
    
    - renderMenuProcedure : rm       (unicode)       [create,query,edit]
        This flag is obsolete. It will be removed in the next release.
    
    - renderOptionsProcedure : ro    (unicode)       [create,query,edit]
        Set or query the render options procedure associated with the specified
        renderer.
    
    - renderProcedure : r            (unicode)       [create,query,edit]
        Set or query the render command associated with the specified renderer.
    
    - renderRegionProcedure : rr     (unicode)       [create,query,edit]
        Set or query the render region procedure associated with the specified renderer.
    
    - renderSequenceProcedure : rs   (unicode)       [create,query,edit]
        Set or query the sequence rendering procedure associated with the specified
        renderer.
    
    - rendererUIName : ui            (unicode)       [create,query,edit]
        Set or query the rendererUIName for the specified renderer. The rendererUIName
        is the name of the renderer as it would appear in menus.
    
    - renderingEditorsSubMenuProcedure : res (unicode)       [create,query,edit]
        Set or query the procedure reponsible for creating renderer specific editors
        submenu under the Rendering Editorsmenu for the specified renderer.
    
    - showBatchRenderLogProcedure : brl (unicode)       [create,query,edit]
        Set or query the log file batch procedure associated with the specified
        renderer.
    
    - showBatchRenderProcedure : sbr (unicode)       [create,query,edit]
        Set or query the show batch render procedure associated with the specified
        renderer.
    
    - showRenderLogProcedure : srl   (unicode)       [create,query,edit]
        Set or query the log file render procedure associated with the specified
        renderer.
    
    - startIprRenderProcedure : sti  (unicode)       [create,query,edit]
        Set or query the start IPR render procedure associated with the specified
        renderer.
    
    - stopIprRenderProcedure : spi   (unicode)       [create,query,edit]
        Set or query the stop IPR render procedure associated with the specified
        renderer.
    
    - supportColorManagement : scm   (bool)          [query,edit]
        Specifies whether the renderer supports color management.
    
    - textureBakingProcedure : tb    (unicode)       [create,query,edit]
        Set or query the texture baking procedure associated with the specified
        renderer.
    
    - unregisterRenderer : unr       (bool)          [query,edit]
        Unregister the specified renderer.                                 Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.renderer`
    """
    pass


def layeredShaderPort(*args, **kwargs):
    """
    This command creates a 3dPort that displays an image representing the layered
    shader node specified.
    
    Flags:
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
    
    - node : n                       (PyNode)        [create]
        Specifies the name of the newLayeredShader node this port will represent.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - selectedColorControl : scc     (unicode)       [create]
        Specifies the name of the UI-control that represents the currently selected
        layer's color.
    
    - selectedTransparencyControl : stc (unicode)       [create]
        Specifies the name of the UI-control that represents the currently selected
        layer's transparency.
    
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
    
    
    Derived from mel command `maya.cmds.layeredShaderPort`
    """
    pass


def spotLight(*args, **kwargs):
    """
    TlightCmd is the base class for other light commands. TnonAmbientLightCmd is a
    class that looks like a command but is not.  It is a base class for the
    extended/nonExtended lights. TnonExtendedLightCmd is a base class and not a real
    command. It is inherited by several lights: TpointLight, TdirectionalLight,
    TspotLight etc. The spotLight command is used to edit the parameters of existing
    spotLights, or to create new ones. The default behaviour is to create a new
    spotlight.
    
    Flags:
    - barnDoors : bd                 (bool)          [create,query,edit]
        Are the barn doors enabled?
    
    - bottomBarnDoorAngle : bbd      (float)         [create,query,edit]
        Angle of the bottom of the barn door.
    
    - coneAngle : ca                 (float)         [create,query,edit]
        angle of the spotLight
    
    - decayRate : d                  (int)           [create]
        Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
    
    - discRadius : drs               (float)         [create,query]
        Radius of shadow disc.
    
    - dropOff : do                   (float)         [create,query,edit]
        dropOff of the spotLight
    
    - exclusive : exc                (bool)          [create,query]
        True if the light is exclusively assigned
    
    - intensity : i                  (float)         [create,query]
        Intensity of the light
    
    - leftBarnDoorAngle : lbd        (float)         [create,query,edit]
        Angle of the left of the barn door.
    
    - name : n                       (unicode)       [create,query]
        Name of the light
    
    - penumbra : p                   (float)         [create,query,edit]
        specify penumbra region
    
    - position : pos                 (float, float, float) [create,query]
        Position of the light
    
    - rgb : rgb                      (float, float, float) [create,query]
        RGB colour of the light
    
    - rightBarnDoorAngle : rbd       (float)         [create,query,edit]
        Angle of the right of the barn door.
    
    - rotation : rot                 (float, float, float) [create,query]
        Rotation of the light for orientation, where applicable
    
    - shadowColor : sc               (float, float, float) [create,query]
        Color of the light's shadow
    
    - shadowDither : sd              (float)         [create,query]
        Shadow dithering value.
    
    - shadowSamples : sh             (int)           [create,query]
        Numbr of shadow samples to use
    
    - softShadow : ss                (bool)          [create,query]
        True if soft shadowing is to be enabled
    
    - topBarnDoorAngle : tbd         (float)         [create,query,edit]
        Angle of the top of the barn door.
    
    - useRayTraceShadows : rs        (bool)          [create,query]
        True if ray trace shadows are to be used                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.spotLight`
    """
    pass


def _pointLight(*args, **kwargs):
    """
    Maya Bug Fix:
      - name flag was ignored
    """
    pass


def nodeIconButton(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.  The
    icon image displayed is the one that best fits the current size of the control
    given its current style. This command creates a button that can be displayed
    with different icons, with or without a text label. If the button is drag and
    dropped onto other controls (e.g., HyperShade), the command will be executed and
    the return string will be used as the name of a dropped node.
    
    Flags:
    - align : al                     (unicode)       [create,query,edit]
        The label alignment.  Alignment values are left, right, and center. By default,
        the label is aligned center. Currently only available when -st/style is set to
        iconAndTextCentered.
    
    - annotation : ann               (unicode)       [create,query,edit]
        Annotate the control with an extra string value.
    
    - backgroundColor : bgc          (float, float, float) [create,query,edit]
        The background color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0. When
        setting backgroundColor, the background is automatically enabled, unless
        enableBackground is also specified with a false value.
    
    - command : c                    (script)        [create,query,edit]
        Command executed when the control is pressed. The command should return a string
        which will be used to facilitate node drag and drop.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - disabledImage : di             (unicode)       [create,query,edit]
        Image used when the button is disabled. Image size must be the same as the image
        specified with the i/imageflag. This is a Windows only flag.
    
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
    
    - flipX : fx                     (bool)          [create,query,edit]
        Is the image flipped horizontally?
    
    - flipY : fy                     (bool)          [create,query,edit]
        Is the image flipped vertically?
    
    - font : fn                      (unicode)       [create,query,edit]
        The font for the text.  Valid values are boldLabelFont, smallBoldLabelFont,
        tinyBoldLabelFont, plainLabelFont, smallPlainLabelFont, obliqueLabelFont,
        smallObliqueLabelFont, fixedWidthFontand smallFixedWidthFont.
    
    - fullPathName : fpn             (bool)          [query]
        Return the full path name of the widget, which includes all the parents.
    
    - height : h                     (int)           [create,query,edit]
        The height of the control.  The control will attempt to be this size if it is
        not overruled by parent layout conditions.
    
    - highlightColor : hlc           (float, float, float) [create,query,edit]
        The highlight color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0.
    
    - image : i                      (unicode)       [create,query,edit]
        If you are not providing images with different sizes then you may use this flag
        for the control's image. If the iconOnlystyle is set, the icon will be scaled to
        the size of the control.
    
    - image1 : i1                    (unicode)       [create,query,edit]
        First of three possible icons. The icon that best fits the current size of the
        control will be displayed.
    
    - image2 : i2                    (unicode)       [create,query,edit]
        Second of three possible icons. The icon that best fits the current size of the
        control will be displayed.
    
    - image3 : i3                    (unicode)       [create,query,edit]
        Third of three possible icons. The icon that best fits the current size of the
        control will be displayed.
    
    - imageOverlayLabel : iol        (unicode)       [create,query,edit]
        A short string, up to 6 characters, representing a label that will be displayed
        on top of the image.
    
    - isObscured : io                (bool)          [query]
        Return whether the control can actually be seen by the user. The control will be
        obscured if its state is invisible, if it is blocked (entirely or partially) by
        some other control, if it or a parent layout is unmanaged, or if the control's
        window is invisible or iconified.
    
    - label : l                      (unicode)       [create,query,edit]
        The text that appears in the control.
    
    - labelOffset : lo               (int)           [create,query,edit]
        The label offset. Default is 0. Currently only available when -st/style is set
        to iconAndTextCentered.
    
    - ltVersion : lt                 (unicode)       [create,query,edit]
        This flag is used to specify the Maya LT version that this control feature was
        introduced, if the version flag is not specified, or if the version flag is
        specified but its argument is different. This value is only used by Maya LT, and
        otherwise ignored. The argument should be given as a string of the version
        number (e.g. 2013, 2014). Currently only accepts major version numbers (e.g.
        2013 Ext 1, or 2013.5 should be given as 2014).
    
    - manage : m                     (bool)          [create,query,edit]
        Manage state of the control.  An unmanaged control is not visible, nor does it
        take up any screen real estate.  All controls are created managed by default.
    
    - marginHeight : mh              (int)           [create,query,edit]
        The number of pixels above and below the control content. The default value is 1
        pixel.
    
    - marginWidth : mw               (int)           [create,query,edit]
        The number of pixels on either side of the control content. The default value is
        1 pixel.
    
    - noBackground : nbg             (bool)          [create,edit]
        Clear/reset the control's background. Passing true means the background should
        not be drawn at all, false means the background should be drawn.  The state of
        this flag is inherited by children of this control.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - overlayLabelBackColor : olb    (float, float, float, float) [create,query,edit]
        The RGBA color of the shadow behind the label defined by imageOverlayLabel.
        Default is 50% transparent black: 0 0 0 .5
    
    - overlayLabelColor : olc        (float, float, float) [create,query,edit]
        The RGB color of the label defined by imageOverlayLabel. Default is a light
        grey: .8 .8 .8
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - rotation : rot                 (float)         [create,query,edit]
        The rotation value of the image in radians.
    
    - statusBarMessage : sbm         (unicode)       [create,edit]
        Extra string to display in the status bar when the mouse is over the control.
    
    - style : st                     (unicode)       [create,query,edit]
        The draw style of the control.  Valid styles are iconOnly, textOnly,
        iconAndTextHorizontal, iconAndTextVertical, and iconAndTextCentered. (Note:
        iconAndTextCenteredis only available on Windows). If the iconOnlystyle is set,
        the icon will be scaled to the size of the control.
    
    - useAlpha : ua                  (bool)          [create,query,edit]
        Is the image using alpha channel?
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - version : ver                  (unicode)       [create,query,edit]
        Specify the version that this control feature was introduced. The argument
        should be given as a string of the version number (e.g. 2013, 2014). Currently
        only accepts major version numbers (e.g. 2013 Ext 1, or 2013.5 should be given
        as 2014).
    
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
    
    
    Derived from mel command `maya.cmds.nodeIconButton`
    """
    pass


def prepareRender(*args, **kwargs):
    """
    This command is used to register, manage and invoke render traversals. Render
    traversals are used to configure a scene to prepare it for rendering. This
    command has special support for scene assembly nodes.  To render scene assembly
    nodes, a rendering traversal can activate an appropriate representation, for
    each assembly node in the scene.  When rendering is done, this command can
    correspondingly restore the representation that was active before rendering on
    each assembly. Render traversals are grouped into traversal sets.  A render
    traversal set includes callbacks, or render traversals, for one or more of the
    following steps of rendering, ordered by decreasing level of granularity. A
    render traversal callback is an arbitrary script, either MEL or Python, that can
    transform the Maya scene for rendering purposes. preRenderTraversal run once per
    render, before any rendering is performed.postRenderTraversal run once per
    render, after all rendering has been performed.preRenderLayerTraversal run
    before rendering each render layer.postRenderLayerTraversal run after rendering
    each render layer.preRenderFrameTraversal run before rendering each
    frame.postRenderFrameTraversal run after rendering each frame.During a render
    view or batch render, Maya will run the render traversals from the same
    traversal set, the default traversal set.  Traversal sets are named, so multiple
    traversal sets can be registered with this command, and the default render
    traversal set can be switched to any one of these registered traversal sets.
    When changing the default traversal set, the different render traversal
    callbacks (preRender, preRenderLayer, preRenderFrame, postRender,
    postRenderLayer, postRenderFrame) are switched as a unit. At render time, the
    software rendering code invokes the callbacks of the default traversal set.  The
    prepareRender scripting capability allows for the development of multiple
    rendering preparation scripts, including from plugins, to provide extensibility
    rather than being constrained to a single implementation. A special traversal
    set is the nulltraversal set.  It is the initial default traversal set, and
    cannot be deregistered.  It performs no work, and does not save and restore the
    assembly node active representation configuration.  It will provide WYSIWYG
    (What You See Is What You Get) rendering of assembly nodes, without switching to
    a different representation to render. Render traversals are invoked by Maya
    using this command's create mode. This is done by Maya's rendering
    infrastructure, and should not be required unless developing new render views or
    batch render code.  Most uses of this command will simply use the edit mode to
    register render traversals into a render traversal set, or the query mode to
    query the names of the render traversals in a render traversal set. The
    prepareRender command has support for saving and restoring the active
    representation of assembly nodes in the scene.  Use the saveAssemblyConfig flag
    to indicate that the render traversal set requires saving the assembly node
    active representation before rendering begins, and should restore the assembly
    node active representation after rendering ends. It is the responsibility of
    render traversals that modify the scene in ways other than changing the active
    representation on assembly nodes to restore the scene to its previous state,
    most likely using the postRender, postRenderLayer, and postRenderFrame
    traversals. Note that Maya does not call the prepareRender -restore command on
    batch render completion, since batch rendering is done on a copy of the scene
    which is discarded once rendering terminates.  Implementors of render traversals
    may wish to check whether they are running in batch mode, to implement the same
    optimization.            In query mode, return type is based on queried flag.
    
    Flags:
    - defaultTraversalSet : dt       (unicode)       [query,edit]
        Set or query the default traversal set.  The prepareRender command performs
        operations on the default traversal set, unless the -traversalSet flag is used
        to specify an explicit traversal set.
    
    - deregister : d                 (unicode)       [edit]
        Deregister a registered traversal set.  If the deregistered traversal set is the
        default traversal set, the new default traversal set will be the nulltraversal
        set.
    
    - invokePostRender : ior         (bool)          [create]
        Invoke the postRender render traversal for a given traversal set.  The traversal
        set will be the default traversal set, unless the -traversalSet flag is used to
        specify an explicit traversal set.
    
    - invokePostRenderFrame : iof    (bool)          [create]
        Invoke the postRenderFrame render traversal for a given traversal set.  The
        traversal set will be the default traversal set, unless the -traversalSet flag
        is used to specify an explicit traversal set.
    
    - invokePostRenderLayer : iol    (bool)          [create]
        Invoke the postRenderLayer render traversal for a given traversal set.  The
        traversal set will be the default traversal set, unless the -traversalSet flag
        is used to specify an explicit traversal set.
    
    - invokePreRender : irr          (bool)          [create]
        Invoke the preRender render traversal for a given traversal set.  The traversal
        set will be the default traversal set, unless the -traversalSet flag is used to
        specify an explicit traversal set.
    
    - invokePreRenderFrame : irf     (bool)          [create]
        Invoke the preRenderFrame render traversal for a given traversal set.  The
        traversal set will be the default traversal set, unless the -traversalSet flag
        is used to specify an explicit traversal set.
    
    - invokePreRenderLayer : irl     (bool)          [create]
        Invoke the preRenderLayer render traversal for a given traversal set.  The
        traversal set will be the default traversal set, unless the -traversalSet flag
        is used to specify an explicit traversal set.
    
    - invokeSettingsUI : isu         (bool)          [create]
        Invoke the settings UI callback to populate a layout with UI controls, for a
        given traversal set.  The current UI parent will be a form layout, which the
        callback can query using the setParent command.  The traversal set will be the
        default traversal set, unless the -traversalSet flag is used to specify an
        explicit traversal set.
    
    - label : lbl                    (unicode)       [query,edit]
        Set or query the label for a given traversal set.  The label is used for UI
        display purposes, and can be localized.  The traversal set will be the default,
        unless the -traversalSet flag is used to specify an explicit traversal set.
    
    - listTraversalSets : lt         (bool)          [query]
        Query the supported render traversal sets.
    
    - postRender : por               (script)        [query,edit]
        Set or query the postRender render traversal for a given traversal set.  This
        traversal is run after a render.  The traversal set will be the default
        traversal set, unless the -traversalSet flag is used to specify an explicit
        traversal set.
    
    - postRenderFrame : pof          (script)        [query,edit]
        Set or query the postRenderFrame render traversal for a given traversal set.
        This traversal is run after the render of a single frame, with a render layer.
        The traversal set will be the default traversal set, unless the -traversalSet
        flag is used to specify an explicit traversal set.
    
    - postRenderLayer : pol          (script)        [query,edit]
        Set or query the postRenderLayer render traversal for a given traversal set.
        This traversal is run after a render layer is rendered, within a render.  The
        traversal set will be the default traversal set, unless the -traversalSet flag
        is used to specify an explicit traversal set.
    
    - preRender : prr                (script)        [query,edit]
        Set or query the preRender render traversal for a given traversal set.  This
        traversal is run before a render.  The traversal set will be the default
        traversal set, unless the -traversalSet flag is used to specify an explicit
        traversal set.
    
    - preRenderFrame : prf           (script)        [query,edit]
        Set or query the preRenderFrame render traversal for a given traversal set.
        This traversal is run before the render of a single frame, with a render layer.
        The traversal set will be the default traversal set, unless the -traversalSet
        flag is used to specify an explicit traversal set.
    
    - preRenderLayer : prl           (script)        [query,edit]
        Set or query the preRenderLayer render traversal for a given traversal set.
        This traversal is run before a render layer is rendered, within a render.  The
        traversal set will be the default traversal set, unless the -traversalSet flag
        is used to specify an explicit traversal set.
    
    - restore : rtr                  (bool)          [create]
        Clean up after rendering, including restoring the assembly active representation
        configuration for the whole scene, if the saveAssemblyConfig flag for the
        traversal set is true.  The traversal set will be the default traversal set,
        unless the -traversalSet flag is used to specify an explicit traversal set.
    
    - saveAssemblyConfig : sac       (bool)          [query,edit]
        Set or query whether or not the assembly active representation configuration for
        the whole scene should be saved for a given traversal set.  The traversal set
        will be the default, unless the -traversalSet flag is used to specify an
        explicit traversal set.
    
    - settingsUI : sui               (script)        [query,edit]
        Set or query the settings UI callback for a given traversal set.  The traversal
        set will be the default traversal set, unless the -traversalSet flag is used to
        specify an explicit traversal set.
    
    - setup : stp                    (bool)          [create]
        Setup render preparation, including saving the assembly active representation
        configuration for the whole scene, if the saveAssemblyConfig flag for the
        traversal set is true.  Any previously-saved configuration will be overwritten.
        The traversal set will be the default traversal set, unless the -traversalSet
        flag is used to specify an explicit traversal set.
    
    - traversalSet : ts              (unicode)       [create,query,edit]
        Set or query properties for the specified registered traversal set.
    
    - traversalSetInit : tsi         (script)        [query,edit]
        Set or query the traversal set initialisation callback for a given traversal
        set. The traversal set will be the default traversal set, unless the
        -traversalSet flag is used to specify an explicit traversal set. This callback
        is invoked whenever the specified traversal set becomes the default. traversal
        set.                               Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.prepareRender`
    """
    pass


def cameraSet(*args, **kwargs):
    """
    This command manages camera set nodes. Camera sets allow the users to break a
    single camera shot into layers. Instead of drawing all objects with a single
    camera, you can isolate the camera to only focus on certain objects and layer
    another camera into the viewport that draws the other objects. The situation to
    use camera sets primarily occurs when building stereoscopic scenes. For example,
    a set of stereo parameters may make the background objects divergent beyond the
    tolerable range of the human perceptual system. However, you like the settings
    because the main focus is in the foreground and the depth is important to the
    visual look of the scene.  You can use camera sets to break apart the shot into
    a foreground stereo camera and background stereo camera. The foreground stereo
    camera will retain the original parameters; however, it will only focus on the
    foreground elements.  The background stereo camera will have a different set of
    stereo parameters and will only draw the background element. Camera sets can be
    viewed using the stereo viewer and are currently only designed to work with
    stereo camera rigs.
    
    Flags:
    - active : a                     (bool)          [create,query,edit]
        Gets / sets the active camera layer.
    
    - appendTo : atl                 (bool)          [create,edit]
        Append a new camera and/or object set to then end of the cameraSet layer list.
        This flag cannot be used in conjunction with insert flag. Additionally, it
        requires the camera and/or objectSet flag to be used.
    
    - camera : cam                   (unicode)       [create,query,edit]
        Set/get the camera for a particular layer. When in query mode, You must specify
        the layer with the layer flag.
    
    - clearDepth : cd                (bool)          [create,query,edit]
        Specifies if the drawing buffer should be cleared before beginning the draw for
        that layer.
    
    - deleteAll : da                 (bool)          [create,edit]
        Delete all camera layers
    
    - deleteLayer : d                (bool)          [create,edit]
        Delete a layer from the camera set. You must specify the layer using the layer
        flag.
    
    - insertAt : ins                 (bool)          [create,edit]
        Inserts the specified camera and/or object set at the specified layer. This flag
        cannot be used in conjunction with the append flag. Additionally, this flag
        requires layer and camera (or objectSet) flag to be used.
    
    - layer : l                      (int)           [create,query,edit]
        Specifies the layer index to be used when accessing layer information
    
    - name : n                       (unicode)       [create,query]
        Gets or sets the name for the created camera set.
    
    - numLayers : nl                 (bool)          [create,query]
        Returns the number of layers defined in the specified cameraSet
    
    - objectSet : os                 (unicode)       [create,query,edit]
        Set/get the objectSet for a particular layer. When in query mode, you must
        specify the layer with the layer flag.
    
    - order : o                      (int)           [create,query,edit]
        Set the order in which a particular layer is processed. This flag must be used
        in conjunction with the layer flag.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.cameraSet`
    """
    pass


def createRenderLayer(*args, **kwargs):
    """
    Create a new render layer.  The render layer number will be assigned based on
    the first unassigned number not less than the base index number found in the
    render layer global parameters.  Normally all objects and their descendants will
    be added to the new render layer but if '-noRecurse' is specified then only the
    objects themselves will be added. Only transforms and geometry will be added to
    the new render layer.
    
    Flags:
    - empty : e                      (bool)          [create]
        If set then create an empty render layer. The global flag or specified member
        list will take precidence over  use of this flag.
    
    - g : g                          (bool)          [create]
        If set then create a layer that contains all DAG objects in the scene. Any
        future objects created will also automatically become members of this layer. The
        global flag will take precidence over use of the empty flag or specified member
        list.
    
    - makeCurrent : mc               (bool)          [create]
        If set then make the new render layer the current one.
    
    - name : n                       (unicode)       [create]
        Name of the new render layer being created.
    
    - noRecurse : nr                 (bool)          [create]
        If set then only add specified objects to the render layer.  Otherwise all
        descendants will also be added.
    
    - number : num                   (int)           [create]
        Number for the new render layer being created.                             Flag
        can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.createRenderLayer`
    """
    pass


def textureWindow(*args, **kwargs):
    """
    This command is used to create a UV Editor and to query or edit the texture
    editor settings. The UV Editor displays texture mapped polygon objects in 2D
    texture space. Only active objects are visible in this window. The UV Editor has
    the ability to display two types of images. The Texture Image is a visualisation
    of the current texture and associated placement parameters. The Editor Image is
    a user specified image loaded from disk. A UV Editor can be invoked by selecting
    the Window -UV Texture Editor...menu item from the main maya menu listing that
    appears at the top of the maya window. It can also be invoked by selecting the
    Panel -UV Editoritem under the Panelsmenu item that appears at the top right
    hand corner of the view. As a UV Editor typically exists at start-up time, and
    as only one of these can exist at any given time, this command is normally used
    to query and edit the editor settings.
    
    Flags:
    - activeSelectionOnTop : ast     (bool)          [create,query,edit]
        Display the solid map / distortion of active selection on top of others.
    
    - axesColor : axc                (float, float, float) [create,query,edit]
        The color of axes, default is 0.0 0.0 1.0
    
    - backFacingColor : bfc          (float, float, float, float) [create,query,edit]
        Sets or queries the RGBA back facing color.
    
    - capture : cpt                  (unicode)       [edit]
        Perform an one-time capture of the viewport to the named image file on disk.
    
    - captureSequenceNumber : csn    (int)           [edit]
        When a number greater or equal to 0 is specified each subsequent refresh will
        save an image file to disk if the capture flag has been enabled.  The naming of
        the file is:  {root name}.#.{extension}  if the name {root name}.{extension} is
        used for the capture flag argument. The value of # starts at the number
        specified to for this argument and increments for each subsequent refresh.
        Sequence capture can be disabled by specifying a number less than 0 or an empty
        file name for the capture flag.
    
    - changeCommand : cc             (unicode, unicode, unicode, unicode) [create,query,edit]
        Parameters: First string: commandSecond string: editorNameThird string:
        editorCmdFourth string: updateFuncCall the command when something changes in the
        editor The command should have this prototype :  command(string $editor, string
        $editorCmd, string $updateFunc, int $reason)  The possible reasons could be : 0:
        no particular reason1: scale color2: buffer (single/double)3: axis 4: image
        displayed5: image saved in memory
    
    - checkerColor1 : cc1            (float, float, float) [create,query,edit]
        Sets the first color of the checker and identification pattern, when color mode
        is 2-colors.
    
    - checkerColor2 : cc2            (float, float, float) [create,query,edit]
        Sets the second color of the checker and identification pattern, when color mode
        is 2-colors.
    
    - checkerColorMode : ccm         (int)           [create,query,edit]
        Sets the color mode of the checker and identification pattern. 0: multi-colors;
        1: 2-colors;
    
    - checkerDensity : cd            (int)           [create,query,edit]
        Sets the density of the checker and identification pattern.
    
    - checkerDrawTileLabels : cdt    (bool)          [create,query,edit]
        Toggles the checker tile label display.
    
    - checkerGradient1 : cg1         (float, float, float) [create,query,edit]
        Sets the first gradient of the checker and identification pattern, when color
        mode is 2-colors.
    
    - checkerGradient2 : cg2         (float, float, float) [create,query,edit]
        Sets the second gradient of the checker and identification pattern, when color
        mode is 2-colors.
    
    - checkerGradientOverlay : cgo   (bool)          [create,query,edit]
        Toggle application of the gradient.
    
    - checkerTileLabelColor : ctc    (float, float, float) [create,query,edit]
        Sets the checker tile label color.
    
    - clearImage : ci                (bool)          [edit]
        Clears the current Editor Image.
    
    - cmEnabled : cme                (bool)          [query,edit]
        Turn on or off applying color management in the editor.  If set, the color
        management configuration set in the current editor is used.
    
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - displayAxes : dax              (bool)          [query,edit]
        Specify true to display the grid axes.
    
    - displayCheckered : dct         (bool)          [create,query,edit]
        Display a unique checker and identification pattern for each UV tiles.
    
    - displayDistortion : ddt        (bool)          [create,query,edit]
        Display the layout in shaded colors to indentify areas with stretched/squashed
        UVs
    
    - displayDivisionLines : ddl     (bool)          [query,edit]
        Specify true to display the subdivision lines between grid lines.
    
    - displayGridLines : dgl         (bool)          [query,edit]
        Specify true to display the grid lines.
    
    - displayImage : di              (int)           [query,edit]
        Set a particular image in the Editor Image Stack as the current Editor Image.
        Images are added to the Editor Image Stack using the si/saveImageflag.
    
    - displayIsolateSelectHUD : dih  (bool)          [create,query,edit]
        Show heads-up display of isolate selection
    
    - displayLabels : dl             (bool)          [query,edit]
        Specify true to display the grid line numeric labels.
    
    - displayOverlappingUVCountHUD : doh (bool)          [create,query,edit]
        Show heads-up display of overlapping UV count, as a part UV Statistics HUD
    
    - displayPreselection : dps      (bool)          [create,query,edit]
        Toggles the pre-selection display.
    
    - displayReversedUVCountHUD : drh (bool)          [create,query,edit]
        Show heads-up display of UV Shells, as a part UV Statistics HUD
    
    - displaySolidMap : dsm          (bool)          [create,query,edit]
        Display a solid overlay for the active texture map.
    
    - displayStyle : dst             (unicode)       [create,query,edit]
        Set the mode to display the image. Valid values are: colorto display the basic
        RGB imagemaskto display the mask channellumto display the luminance of the image
    
    - displayTextureBorder : dtb     (bool)          [create,query,edit]
        Toggles the texture borders display.
    
    - displayUVShellCountHUD : dsh   (bool)          [create,query,edit]
        Show heads-up display of UV Shell count, as a part UV Statistics HUD
    
    - displayUVStatisticsHUD : duh   (bool)          [create,query,edit]
        Show heads-up display of UV Statistics
    
    - displayUsedPercentageHUD : dph (bool)          [create,query,edit]
        Show heads-up display of used UV space percentage, as a part UV Statistics HUD
    
    - distortionAlpha : dta          (float)         [create,query,edit]
        Set or query the distortion display alpha.
    
    - distortionPerObject : dpo      (bool)          [create,query,edit]
        Toggles the per-object distortion display.
    
    - divisions : d                  (int)           [create,query,edit]
        Sets the number of subdivisions between main grid lines.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - doubleBuffer : dbf             (bool)          [create,query,edit]
        Set the display in double buffer mode
    
    - drawAxis : da                  (bool)          [create,query,edit]
        Set or query whether the axis will be drawn.
    
    - drawSubregions : dsr           (bool)          [create,query,edit]
        Toggles the subregion display.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - exposure : exp                 (float)         [query,edit]
        The exposure value used by the color management of the current editor.
    
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
    
    - forceRebake : frb              (bool)          [create,edit]
        Forces the current cache texture to refresh.
    
    - frameAll : fa                  (bool)          [create]
        This will zoom on the whole scene.
    
    - frameSelected : fs             (bool)          [create]
        This will zoom on the currently selected objects.
    
    - frontFacingColor : ffc         (float, float, float, float) [create,query,edit]
        Sets or queries the RGBA front facing color.
    
    - gamma : ga                     (float)         [query,edit]
        The gamma value used by the color management of the current editor.
    
    - gridLinesColor : glc           (float, float, float) [create,query,edit]
        The color of grid lines, default is 0.325 0.325 0.325
    
    - gridNumbersColor : gnc         (float, float, float) [create,query,edit]
        The color of grid numbers, default is 0.2 0.2 0.2
    
    - highlightConnection : hlc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its highlight list. Not all editors have a highlight list. For
        those that do, it is a secondary selection list.
    
    - imageBaseColor : ibc           (float, float, float) [create,query,edit]
        The base color of the image, default is white 1.0 1.0 1.0
    
    - imageDim : idm                 (bool)          [create,query,edit]
        Toggles the image dimming.
    
    - imageDisplay : id              (bool)          [query,edit]
        Toggles the Texture Image display.
    
    - imageNames : imn               (bool)          [query]
        List image names for all Texture Images available for display, if any.
    
    - imageNumber : imageNumber      (int)           [query,edit]
        Sets the number of Texture Images to display. This depends on the number of
        textures corresponding to the current selection. If there are N textures, then
        the possible Texture Image numbers are 0 to N-1.
    
    - imagePixelSnap : ip            (bool)          [query,edit]
        Sets a mode so that UV transformations in the UV Texture Editor will cause UV
        values to snap to image pixel corners. Which pixels are used depends on whether
        a Texture Image or an Editor Image is being displayed. If both are displayed,
        the Texture Image pixels will be used.
    
    - imageRatio : imr               (bool)          [query,edit]
        Sets the window to draw using the Texture Image's height versus width ratio. If
        the width is greater than the height, then the width is set to be 1 unitin the
        window, and the height is adjusted by width divided by height. This only affects
        the display of a Texture Image, not an Editor Image.
    
    - imageRatioValue : irv          (float)         [query]
        Query current image ratio value in UV Editor.
    
    - imageSize : imageSize          (bool)          [query]
        Returns the size of the Texture Image currently being displayed. The values
        returned are width followed by height. Image size can only be queried.
    
    - imageTileRange : itr           (float, float, float, float) [query,edit]
        Sets the UV range of the display. The 4 values specify the minimum U, V and
        maximum U, V in that order. When viewing a texture image, these values affect
        how many times the image is tiled based on appropriate parameters (e.g. Repeat
        UV, Mirror, Wrap, etc...) When viewing an Editor Image these values determine
        the visible size of the image. For example, setting the range to ( 0, 0, 2, 1 )
        will cause the Editor Image to be loaded into a 2x1 rectangle, distorting it as
        necessary to fill the available space.
    
    - imageToTextureNumber : itn     (int)           []
    
    - imageUnfiltered : iuf          (bool)          [query,edit]
        Sets the Texture Image to draw unfiltered. The image will appear pixelatedwhen
        the display resolution is higher than the resolution of the image.
    
    - internalFaces : internalFaces  (bool)          [create,query,edit]
        Display contained faces by the selected components.
    
    - isolateSelectSetUpdated : isu  (bool)          []
    
    - labelPosition : lp             (unicode)       [query,edit]
        The position of the grid's numeric labels. Valid values are axisand edge.
    
    - loadImage : li                 (unicode)       [edit]
        load an image from disk and set it as the current Editor Image
    
    - lockMainConnection : lck       (bool)          [create,edit]
        Locks the current list of objects within the mainConnection, so that only those
        objects are displayed within the editor. Further changes to the original
        mainConnection are ignored.
    
    - mainListConnection : mlc       (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object.
    
    - maxResolution : mrs            (int)           [create,query,edit]
        This flag will set the current cached texture's maximum resolution.
    
    - multiColorAlpha : mca          (float)         [create,query,edit]
        Sets the multi-color alpha of shaded UVs.
    
    - nbImages : nim                 (bool)          [query]
        returns the number of images
    
    - nextView : nv                  (bool)          [edit]
        Switches to the next view.
    
    - numUvSets : nuv                (bool)          [create,query,edit]
        This flag will return the number of UV sets for selected objects in the texture
        window.
    
    - numberOfImages : ni            (int)           [query]
        The number of Texture Images currently available. for display.
    
    - numberOfTextures : nt          (int)           [query]
        The number of textures currently available. for display.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - previousView : pv              (bool)          [edit]
        Switches to the previous view.
    
    - realSize : rs                  (bool)          [create]
        This will display the image with the size of the internal buffer. Note: This
        argument no long has any affect on image display.
    
    - refresh : ref                  (bool)          [edit]
        requests a refresh of the current Editor Image.
    
    - relatedFaces : rf              (bool)          [create,query,edit]
        Display connected faces by the selected components.
    
    - removeAllImages : ra           (bool)          [edit]
        remove all the Editor Images from the Editor Image Stack
    
    - removeImage : ri               (bool)          [edit]
        remove the current Editor Image from the Editor Image Stack
    
    - rendererString : rds           (unicode)       [create,query,edit]
        Set or query the string describing the current renderer.
    
    - reset : r                      (bool)          [create]
        Resets the ground plane to its default values.
    
    - saveImage : si                 (bool)          [edit]
        save the current Editor Image to memory. Saved Editor Images are stored in an
        Editor Image Stack. The most recently saved image is stored in position 0, the
        second most recently saved image in position 1, and so on... To set the current
        Editor Image to a previously saved image use the di/displayImageflag.
    
    - scaleBlue : sb                 (float)         [create,query,edit]
        Define the scaling factor for the blue component in the View. The default value
        is 1 and can be between -1000 to +1000
    
    - scaleGreen : sg                (float)         [create,query,edit]
        Define the scaling factor for the green component in the View. The default value
        is 1 and can be between -1000 to +1000
    
    - scaleRed : sr                  (float)         [create,query,edit]
        Define the scaling factor for the red component in the View. The default value
        is 1 and can be between -1000 to +1000
    
    - selectInternalFaces : sif      (bool)          [create,query,edit]
        Add to selectionList the faces which are contained by (internal to) selected
        components.
    
    - selectRelatedFaces : srf       (bool)          [create]
        Add to selectionList the faces which are connected to (non-internally related
        to) selected components.
    
    - selectionConnection : slc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its own selection list. As the user selects things in this
        editor, they will be selected in the selectionConnection object. If the object
        undergoes changes, the editor updates to show the changes.
    
    - setUvSet : suv                 (int)           [create,edit]
        This flag will set the current UV set on one given selected object within the
        texture window.
    
    - singleBuffer : sbf             (bool)          [create,query,edit]
        Set the display in single buffer mode
    
    - size : s                       (float)         [create,query,edit]
        Sets the size of the grid.
    
    - solidMap3dView : s3d           (bool)          [create,query,edit]
        Display a solid overlay for the active texture map in 3D viewport.
    
    - solidMapColorSeed : scs        (int)           [create,query,edit]
        Sets the multi-color seed of shaded UVs.
    
    - solidMapPerShell : sps         (bool)          [create,query,edit]
        Display a solid overlay with a random color per shell.
    
    - spacing : sp                   (float)         [create]
        Sets the spacing between main grid lines.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - style : st                     (int)           [query,edit]
        This flag is obsolete and should not be used.
    
    - subdivisionLinesColor : sdc    (float, float, float) [create,query,edit]
        The color of subdivision lines, default is 0.25 0.25 0.25
    
    - textureBorder3dView : t3d      (bool)          [create,query,edit]
        Toggles the texture borders display in 3d viewport.
    
    - textureBorderColor : tbc       (float, float, float) [create,query,edit]
        Sets the display color of texture border.
    
    - textureBorderWidth : tbw       (int)           [create,query,edit]
        Set the display edge width of texture border.
    
    - textureNames : txn             (bool)          [query]
        Texture names for all Texture Images available for display, if any.
    
    - textureNumber : tn             (int)           [query,edit]
        Sets the number of textures to display This depends on the number of textures
        corresponding to the current selection. If there are N textures, then the
        possible Texture Image numbers are 0 to N-1.
    
    - textureToImageNumber : tin     (int)           []
    
    - tileLabels : tlb               (bool)          [create,query,edit]
        Toggles the texture tile label display.
    
    - tileLinesColor : tlc           (float, float, float) [create,query,edit]
        The color of tile lines, default is 0.0 0.0 0.0
    
    - toggle : tgl                   (bool)          [create,query,edit]
        Toggles the ground plane display.
    
    - toggleExposure : tge           (bool)          [edit]
        Toggles between the current and the default exposure value of the editor.
    
    - toggleGamma : tgg              (bool)          [edit]
        Toggles between the current and the default gamma value of the editor.
    
    - unParent : up                  (bool)          [create,edit]
        Specifies that the editor should be removed from its layout. This cannot be used
        in query mode.
    
    - unlockMainConnection : ulk     (bool)          [create,edit]
        Unlocks the mainConnection, effectively restoring the original mainConnection
        (if it is still available), and dynamic updates.
    
    - updateMainConnection : upd     (bool)          [create,edit]
        Causes a locked mainConnection to be updated from the orginal mainConnection,
        but preserves the lock state.
    
    - useFaceGroup : uf              (bool)          [create,query,edit]
        Display faces that are associated with the groupId that is set on the mesh node
        that is drawn. (The attribute displayFacesWithGroupId
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - usedPercentageHUDRange : upr   (float, float, float, float) [create,query,edit]
        Sets the range when calculating used UV space percentage. The 4 values specify
        the minimum U, V and maximum U, V in that order., default is 0 0 1 1.
    
    - uvSets : uvs                   (bool)          [create,query,edit]
        This flag will return strings containing UV set and object name pairs for
        selected objects in the texture window. The syntax of each pair is objectName |
        uvSetName, where | is a literal character.
    
    - viewPortImage : vpi            (bool)          [create,edit]
        Toggles the view port/ caching Texture Images.
    
    - viewTransformName : vtn        (unicode)       [query,edit]
        Sets the view pipeline to be applied if color management is enabled in the
        current editor.
    
    - wireframeComponentColor : wcc  (float, float, float, float) [create,query,edit]
        Sets or queries the RGBA component wireframe color.
    
    - wireframeObjectColor : woc     (float, float, float, float) [create,query,edit]
        Sets or queries the RGBA object wireframe color.
    
    - writeImage : wi                (unicode)       [edit]
        write the current Editor Image to disk                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.textureWindow`
    """
    pass


def createSurfaceShader(shadertype, name='None'):
    """
    create a shader and shading group
    """
    pass


def hwReflectionMap(*args, **kwargs):
    """
    This command creates a hwReflectionMap node for having reflection on textured
    surfaces that currently have their boolean attribute displayHWEnvironment set to
    true.
    
    Flags:
    - backTextureName : bkn          (unicode)       [query]
        This flag specifies the file texture name for the back side of the cube.Default
        is noneWhen queried, this flag returns a string.
    
    - bottomTextureName : bmn        (unicode)       [query]
        This flag specifies the file texture name for the bottom side of the
        cube.Default is noneWhen queried, this flag returns a string.
    
    - cubeMap : cm                   (bool)          [query]
        If on, the reflection of the textures is done using the cube mapping.Default is
        false. The reflection is done using sphere mapping.When queried, this flag
        returns a boolean.
    
    - decalMode : dm                 (bool)          [query]
        If on, the reflection color replaces the surface shading.Default is false. The
        reflection is multiplied to the surface shading.When queried, this flag returns
        a boolean.
    
    - enable : en                    (bool)          [query]
        If on, enable the corresponding hwReflectionMap node.Default is false.When
        queried, this flag returns a boolean.
    
    - frontTextureName : ftn         (unicode)       [query]
        This flag specifies the file texture name for the front side of the cube.Default
        is noneWhen queried, this flag returns a string.
    
    - leftTextureName : ltn          (unicode)       [query]
        This flag specifies the file texture name for the left side of the cube.Default
        is noneWhen queried, this flag returns a string.
    
    - rightTextureName : rtn         (unicode)       [query]
        This flag specifies the file texture name for the right side of the cube.Default
        is noneWhen queried, this flag returns a string.
    
    - sphereMapTextureName : smn     (unicode)       [query]
        This flag specifies the file texture name for the sphere mapping option.Default
        is noneWhen queried, this flag returns a string.
    
    - topTextureName : tpn           (unicode)       [query]
        This flag specifies the file texture name for the top side of the cube.Default
        is noneWhen queried, this flag returns a string.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.hwReflectionMap`
    """
    pass


def exclusiveLightCheckBox(*args, **kwargs):
    """
    This command creates a checkBox that controls a light's exclusive non-exclusive
    status.  An exclusive light is one that is not hooked up to the default-light-
    list, thus it does not illuminate all objects be default.  However an exclusive
    light can be linked to an object.
    
    Flags:
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
    
    - label : l                      (unicode)       [create,edit]
        Value of the checkbox label
    
    - light : lt                     (PyNode)        [create]
        The light that is to be made exclusive/non-exclusive.
    
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
    
    
    Derived from mel command `maya.cmds.exclusiveLightCheckBox`
    """
    pass


def directionalLight(*args, **kwargs):
    """
    TlightCmd is the base class for other light commands. TnonAmbientLightCmd is a
    class that looks like a command but is not.  It is a base class for the
    extended/nonExtended lights. TnonExtendedLightCmd is a base class and not a real
    command. It is inherited by several lights: TpointLight, TdirectionalLight,
    TspotLight etc. The directionalLight command is used to edit the parameters of
    existing directionalLights, or to create new ones. The default behaviour is to
    create a new directionallight. This is the commmand that instantiates an
    directionalLight or edits the parameters of an existing one.
    TdirectionalLightCmd inherits from TnonExtendedLightCmd which defines softShadow
    flags. See TlightCmd for a global picture of the light commands.
    TdirectionalLightCmd behaves like any other command, it has flags, saves undo
    information etc. the only slightly different behaviour is that it calls up to
    TnonExtendedLightCmd to complete the functionality of the command.
    
    Flags:
    - decayRate : d                  (int)           [create]
        Decay rate of the light (0-no decay, 1-slow, 2-realistic, 3-fast)
    
    - discRadius : drs               (float)         [create,query]
        Radius of shadow disc.
    
    - exclusive : exc                (bool)          [create,query]
        True if the light is exclusively assigned
    
    - intensity : i                  (float)         [create,query]
        Intensity of the light
    
    - name : n                       (unicode)       [create,query]
        Name of the light
    
    - position : pos                 (float, float, float) [create,query]
        Position of the light
    
    - rgb : rgb                      (float, float, float) [create,query]
        RGB colour of the light
    
    - rotation : rot                 (float, float, float) [create,query]
        Rotation of the light for orientation, where applicable
    
    - shadowColor : sc               (float, float, float) [create,query]
        Color of the light's shadow
    
    - shadowDither : sd              (float)         [create,query]
        Shadow dithering value.
    
    - shadowSamples : sh             (int)           [create,query]
        Numbr of shadow samples to use
    
    - softShadow : ss                (bool)          [create,query]
        True if soft shadowing is to be enabled
    
    - useRayTraceShadows : rs        (bool)          [create,query]
        True if ray trace shadows are to be used                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.directionalLight`
    """
    pass
