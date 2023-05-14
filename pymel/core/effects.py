from pymel.internal.pmcmds import saveFluid
from pymel.internal.pmcmds import getFluidAttr
from pymel.internal.pmcmds import expressionEditorListen
from pymel.internal.pmcmds import getDefaultBrush
from pymel.internal.pmcmds import pfxstrokes
from pymel.internal.pmcmds import nSoft
from pymel.internal.pmcmds import soft
from pymel.internal.pmcmds import paintEffectsDisplay
from pymel.internal.pmcmds import radial
from pymel.internal.pmcmds import dynExpression
from pymel.internal.pmcmds import particleFill
from pymel.internal.pmcmds import colorAtPoint
from pymel.internal.pmcmds import fluidCacheInfo
from pymel.internal.pmcmds import constrain
from pymel.internal.pmcmds import setParticleAttr
from pymel.internal.pmcmds import dynCache
from pymel.internal.pmcmds import truncateFluidCache
from pymel.internal.pmcmds import particleInstancer
from pymel.internal.pmcmds import dynExport
from pymel.internal.pmcmds import runup
from pymel.internal.pmcmds import loadFluid
from pymel.internal.pmcmds import goal
from pymel.internal.pmcmds import particleRenderInfo
from pymel.internal.pmcmds import getParticleAttr
from pymel.internal.pmcmds import dynPref
from pymel.internal.pmcmds import fluidVoxelInfo
from pymel.internal.pmcmds import dynControl
from pymel.internal.pmcmds import emit
from pymel.internal.pmcmds import setDynamic
from pymel.internal.pmcmds import truncateHairCache
from pymel.internal.pmcmds import saveInitialState
from pymel.internal.pmcmds import resampleFluid
from pymel.internal.pmcmds import particleExists
from pymel.internal.pmcmds import setFluidAttr
from pymel.internal.pmcmds import collision
from pymel.internal.pmcmds import newton

if False:
    from typing import Dict, List, Tuple, Union, Optional


def addDynamic(*args, **kwargs):
    """
    Makes the objectspecified as second argument the source of an existing field or
    emitter specified as the first argument. In practical terms, what this means is
    that a field will emanate its force from its owner object, and an emitter will
    emit from its owner object. addDynamic makes the specified field or emitter a
    child of the owner's transform (adding it to the model if it was not already
    there), and makes the necessary attribute connections. If either of the
    arguments is omitted, addDynamic searches the selection list for objects to use
    instead. If more than one possible owner or field/emitter is selected,
    addDynamic will do nothing. If the specified field/emitter already has a source,
    addDynamic will remove the current source and replace it with the newly
    specified source. If a subset of the owner object's cvs/particles/vertices is
    selected, addDynamic will add the field/emitter to that subset only.
    
    
    Derived from mel command `maya.cmds.addDynamic`
    """
    pass


def uniform(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. A uniform field
    pushes objects in a fixed direction.  The field strength, but not the field
    direction, depends on the distance from the object to the field location. The
    transform is the associated dependency node. Use connectDynamic to cause the
    field to affect a dynamic object. If fields are created, this command returns
    the names of each of the fields. If a field was queried, the results of the
    query are returned. If a field was edited, the field name is returned. If object
    names are provided or the active selection list is non-empty, the command
    creates a field for every object in the list and calls addDynamic to add it to
    the object. If the list is empty, the command defaults to -pos 0 0 0. Setting
    the -pos flag with objects named on the command line is an error.
    
    Flags:
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - directionX : dx                (float)         [query,edit]
        X-component of direction.
    
    - directionY : dy                (float)         [query,edit]
        Y-component of direction.
    
    - directionZ : dz                (float)         [query,edit]
        Z-component of direction
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.uniform`
    """
    pass


def emitter(*args, **kwargs):
    """
    Creates, edits or queries an auxiliary dynamics object (for example, a field or
    emitter). Creates an emitter object. If object names are provided or if objects
    are selected, applies the emitter to the named/selected object(s)in the scene.
    Particles will then be emitted from each. If no objects are named or selected,
    or if the -pos option is specified, creates a positional emitter. If an emitter
    was created, the command returns the name of the object owning the emitter, and
    the name of emitter shape. If an emitter was queried, the command returns the
    results of the query. Keyframeable attributes of the emitter node: rate,
    directionX, directionY, directionZ, minDistance, maxDistance, spread.
    
    Flags:
    - alongAxis : alx                (float)         [query,edit]
        Initial velocity multiplier in the direction along the central axis of the
        volume.  See the diagrams in the documentation.  Applies only to volume
        emitters.
    
    - aroundAxis : arx               (float)         [query,edit]
        Initial velocity multiplier in the direction around the central axis of the
        volume.  See the diagrams in the documentation.  Applies only to volume
        emitters.
    
    - awayFromAxis : afx             (float)         [query,edit]
        Initial velocity multiplier in the direction away from the central axis of the
        volume.  See the diagrams in the documentation.  Used only with the cylinder,
        cone, and torus volume emitters.
    
    - awayFromCenter : afc           (float)         [query,edit]
        Initial velocity multiplier in the direction away from the center point of a
        cube or sphere volume emitter. Used only with the cube and sphere volume
        emitters.
    
    - cycleEmission : cye            (unicode)       [query,edit]
        Possible values are noneand frame.Cycling emission restarts the random number
        stream after a specified interval.  This can either be a number of frames or a
        number of emitted particles.  In each case the number is specified by the
        cycleInterval attribute. Setting cycleEmission to frameand cycleInterval to 1
        will then re-start the random stream every frame. Setting cycleInterval to
        values greater than 1 can be used to generate cycles for games work.
    
    - cycleInterval : cyi            (int)           [query,edit]
        Specifies the number of frames or particles between restarts of the random
        number stream.  See cycleEmission.  Has no effect if cycleEmission is set to
        None.
    
    - directionX : dx                (float)         [query,edit]
        x-component of emission direction. Used for directional emitters, and for volume
        emitters with directionalSpeed.
    
    - directionY : dy                (float)         [query,edit]
        y-component of emission direction. Used for directional emitters, and for volume
        emitters with directionalSpeed.
    
    - directionZ : dz                (float)         [query,edit]
        z-component of emission direction. Used for directional emitters, and for volume
        emitters with directionalSpeed.
    
    - directionalSpeed : drs         (float)         [query,edit]
        For volume emitters only, adds a component of speed in the direction specified
        by the directionX, Y, and Z attributes. Applies only to volume emitters. Does
        not apply to other types of emitters.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which emission ends.
    
    - minDistance : mnd              (float)         [query,edit]
        Minimum distance at which emission starts.
    
    - name : n                       (unicode)       [create,query,edit]
        Object name
    
    - needParentUV : nuv             (bool)          [query,edit]
        If aNeedParentUV is true, compute parentUV value from each triangle or each line
        segment, then send out to the target particle object. You also need to add
        parentU and parentV attributes to the particle object to store these values.
    
    - normalSpeed : nsp              (float)         [query,edit]
        Normal speed multiple for point emission. For each emitted particle, multiplies
        the component of the velocity normal to the surface or curve by this amount.
        Surface and curve emitters only.
    
    - position : pos                 (float, float, float) [create,query,edit]
        world-space position
    
    - randomDirection : rnd          (float)         [query,edit]
        Magnitude of a random component of the speed from volume emission.
    
    - rate : r                       (float)         [query,edit]
        Rate at which particles emitted (can be non-integer). For point emission this is
        rate per point per unit time. For surface emission it is rate per square unit of
        area per unit time.
    
    - scaleRateByObjectSize : sro    (bool)          [query,edit]
        Applies to curve and surface emitters, only. If true, number of particles is
        determined by object size (area or length) times rate value.  If false, object
        size is ignored and the rate value is used without modification. The former is
        the way Maya behaved prior to version 3.0.
    
    - scaleSpeedBySize : ssz         (bool)          [query,edit]
        Indicates whether the scale of a volume emitter affects its velocity.
    
    - speed : spd                    (float)         [query,edit]
        Speed multiple.  Multiplies the velocity of the emitted particles by this
        amount. Does not apply to volume emitters.  For that emitter type, use
        directionalSpeed.
    
    - speedRandom : srn              (float)         [query,edit]
        Identifies a range of random variation for the speed of each generated particle.
        If set to a non-zero value, speed becomes the mean value of the generated
        particles, whose speeds vary by a random amount up to plus or minus
        speedRandom/2. For example, speed 5 and speedRandom 2 will make the speeds vary
        between 4 and 6.
    
    - spread : sp                    (float)         [query,edit]
        Random spread (0-1), as a fraction of 90 degrees, along specified direction.
        Directional emitters only.
    
    - tangentSpeed : tsp             (float)         [query,edit]
        Tangent speed multiple for point emission. For each emitted particle, multiplies
        the component of the velocity tangent to the surface  or curve by this amount.
        Surface and curve emitters only.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - type : typ                     (unicode)       [query,edit]
        Type of emitter. The choices are omni | dir | direction | surf | surface | curve
        | curv. The default is omni. The full definition of these types are:
        omnidirectional point emitter, directional point emitter, surface emitter, or
        curve emitter.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the emitter.  Volume offset translates the emission volume by
        the specified amount from the actual emitter location.  This is in the emitter's
        local space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the emitter.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which particles are generated. Values are: cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the emitter.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.emitter`
    """
    pass


def connectDynamic(*args, **kwargs):
    """
    Dynamic connection specifies that the force fields, emitters, or collisions of
    an object affect another dynamic object. The dynamic object that is connected to
    a field, emitter, or collision object is influenced by those fields, emitters
    and collision objects. Connections are made to individual fields, emitters,
    collisions.  So, if an object owns several fields, if the user wants some of the
    fields to affect an object, s/he can specify each field with a -fflag; but if
    the user wants to connect all the fields owned by an object, s/he can specify
    the object name with the -fflag. The same is true for emitters and collisions.
    Different connection types (i.e., for fields vs. emitters) between the same pair
    of objects are logically independent. In other words, an object can be
    influenced by another object's fields without being influenced by its emitters
    or collisions. Each connected object must be a dynamic object. The object
    connected to can be any object that owns fields, emitters, etc.; it need not be
    dynamic. Objects that can own influences are particles, geometry objects (nurbs
    and polys) and lattices.  You can specify either the shape name or the transform
    name of the object to be influenced.
    
    Flags:
    - addScriptHandler : ash         (script)        [create]
        Registers a script that will be given a chance to handle calls to the
        dynamicConnect command. This flag allows other dynamics systems to override the
        behaviour of the connectDynamic command. You must pass a Python function as the
        argument for this flag, and that function must take the following keyword
        arguments: fields, emitters, collisionObjects and objects. The python function
        must return True if it has handled the call to connectDynamic. In the case that
        the script returns true, the connectDynamic command will not do anything as it
        assumes that the work was handled by the script. If all of the callbacks return
        false, the connectDynamic command will proceed as normal.  The addScriptHandler
        flag may not be used with any other flags. When the flag is used, the command
        will return a numerical id that can be used to deregister the callback later
        (see the removeScriptHandler flag)
    
    - collisions : c                 (unicode)       [create]
        Connects each object to the collision models of the given object.
    
    - delete : d                     (bool)          [create]
        Deletes existing connections.
    
    - emitters : em                  (unicode)       [create]
        Connects each object to the emitters of the given object.
    
    - fields : f                     (unicode)       [create]
        Connects each object to the fields of the given object.
    
    - removeScriptHandler : rsh      (int)           [create]
        This flag is used to remove a callback that was previously registered with the
        addScriptHandler flag. The argument to this flag is the numerical id returned by
        dynamicConnect when the addScriptHandler flag was used. If this flag is called
        with an invalid id, then the command will do nothing.  This flag may not be used
        with any other flag.                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.connectDynamic`
    """
    pass


def volumeAxis(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. A volume axis
    field can push particles in four directions, defined with respect to a volume:
    along the axis, away from the axis or center, around the axis, and in a user-
    specified direction.  These are analogous to the emission speed controls of
    volume emitters. The volume axis field also contains a wind turbulence model
    (different from the turbulence field) that simulates an evolving flow of liquid
    or gas. The turbulence has a build in animation that is driven by a connection
    to a time node. The transform is the associated dependency node. Use
    connectDynamic to cause the field to affect a dynamic object. If fields are
    created, this command returns the names of each of the fields. If a field was
    queried, the results of the query are returned. If a field was edited, the field
    name is returned. If object names are provided or the active selection list is
    non-empty, the command creates a field for every object in the list and calls
    addDynamic to add it to the object. If the list is empty, the command defaults
    to -pos 0 0 0. Setting the -pos flag with objects named on the command line is
    an error.
    
    Flags:
    - alongAxis : alx                (float)         [query,edit]
        Initial velocity multiplier in the direction along the central axis of the
        volume.  See the diagrams in the documentation.
    
    - aroundAxis : arx               (float)         [query,edit]
        Initial velocity multiplier in the direction around the central axis of the
        volume.  See the diagrams in the documentation.
    
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - awayFromAxis : afx             (float)         [query,edit]
        Initial velocity multiplier in the direction away from the central axis of the
        volume.  See the diagrams in the documentation.  Used only with the cylinder,
        cone, and torus volumes.
    
    - awayFromCenter : afc           (float)         [query,edit]
        Initial velocity multiplier in the direction away from the center point of a
        cube or sphere volume. Used only with the cube and sphere volumes.
    
    - detailTurbulence : dtr         (float)         [query,edit]
        The relative intensity of a second higher frequency turbulence. This can be used
        to create fine features in large scale flows. Both the speed and the frequency
        on this second turbulence are higher than the primary turbulence. When the
        detailTurbulence is non-zero the simulation may run a bit slower, due to the
        computation of a second turbulence.
    
    - directionX : dx                (float)         [query,edit]
        x-component of force direction.  Used with directional speed.
    
    - directionY : dy                (float)         [query,edit]
        y-component of force direction.  Used with directional speed.
    
    - directionZ : dz                (float)         [query,edit]
        z-component of force direction.  Used with directional speed.
    
    - directionalSpeed : drs         (float)         [query,edit]
        Adds a component of speed in the direction specified by the directionX, Y, and Z
        attributes.
    
    - invertAttenuation : ia         (bool)          [query,edit]
        If this attribute is FALSE, the default, then the attenuation makes the field's
        effect decrease as the affected point is further from the volume's axis and
        closer to its edge.  If the is set to TRUE, then the effect of the field
        increases in this case, making the full effect of the field felt at the volume's
        edge.
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - turbulence : trb               (float)         [query,edit]
        Adds a force simulating a turbulent wind that evolves over time.
    
    - turbulenceFrequencyX : tfx     (float)         [query,edit]
        The repeats of the turbulence function in X.
    
    - turbulenceFrequencyY : tfy     (float)         [query,edit]
        The repeats of the turbulence function in Y.
    
    - turbulenceFrequencyZ : tfz     (float)         [query,edit]
        The repeats of the turbulence function in Z.
    
    - turbulenceOffsetX : tox        (float)         [query,edit]
        The translation of the turbulence function in X.
    
    - turbulenceOffsetY : toy        (float)         [query,edit]
        The translation of the turbulence function in Y.
    
    - turbulenceOffsetZ : toz        (float)         [query,edit]
        The translation of the turbulence function in Z.
    
    - turbulenceSpeed : trs          (float)         [query,edit]
        The rate of change of the turbulence over time. The turbulence loops seamlessly
        every 1.0/turbulenceSpeed seconds. To animate this rate attach a new time node
        to the time input on the volumeAxisNode then animate the time value on the time
        node.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.volumeAxis`
    """
    pass


def turbulence(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. A turbulence
    field causes irregularities (also called 'noise' or 'jitter') in the motion of
    affected objects. Use connectDynamic to cause the field to affect a dynamic
    object. If fields are created, this command returns the names of each of the
    fields. If a field was queried, the results of the query are returned. If a
    field was edited, the field name is returned. If object names are provided or
    the active selection list is non-empty, the command creates a field for every
    object in the list and calls addDynamic to add it to the object. If the list is
    empty, the command defaults to -pos 0 0 0. Setting the -pos flag with objects
    named on the command line is an error.
    
    Flags:
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - frequency : f                  (float)         [query,edit]
        Frequency of turbulence field. This determines how often motion is disrupted.
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - noiseLevel : nsl               (int)           [query,edit]
        If the noiseLevel parameter is greater than zero, the field will do multiple
        lookups in the table.  Each additional lookup is weighted using noiseRatio
        (which see).  The noiseLevel is the number of additional lookups, so if
        noiseLevel is 0, there is just one lookup.  A value of 0 (the default)
        corresponds to the way the field behaved prior to Maya 3.0.
    
    - noiseRatio : nsr               (float)         [query,edit]
        If noiseLevel is greater than zero, then noiseRatio is the relative magnitude
        for each consecutive noise evaluation. These are cumulative: for example, if
        noiseRatio is 0.5, then the first evaluation is weighted 0.5, the second 0.25,
        and so on. Has no effect if noiseLevel is zero.
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - phase : p                      (float)         [query,edit]
        Phase shift of turbulence field. This influences the direction of the
        disruption.  This flag is obsolete and is retained only for backward
        compatibility.  It is replaced by -phaseX, -phaseY, and -phaseZ.  Setting -phase
        is identical to setting -phaseZ (the phase shift was always in the Z dimension).
    
    - phaseX : px                    (float)         [query,edit]
        X component of phase shift of turbulence field. This influences the direction of
        the disruption.
    
    - phaseY : py                    (float)         [query,edit]
        Y component of phase shift of turbulence field. This influences the direction of
        the disruption.
    
    - phaseZ : pz                    (float)         [query,edit]
        Z component of phase shift of turbulence field. This influences the direction of
        the disruption.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.turbulence`
    """
    pass


def stroke(*args, **kwargs):
    """
    The stroke command creates a new Paint Effects stroke node.
    
    Flags:
    - name : n                       (unicode)       [create]
        Sets the name of the stroke to the input string
    
    - pressure : pr                  (bool)          [create]
        On creation, allows the copying of the pressure mapping settings from the Paint
        Effects Tool. Default is false.
    
    - seed : s                       (int)           [create]
        Sets the random seed for this stroke.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.stroke`
    """
    pass


def nParticle(*args, **kwargs):
    """
    The nParticle command creates a new nParticle object from a list of world space
    points. If an nParticle object is created, the command returns the names of the
    new particle shape and its associated particle object dependency node. If an
    object was queried, the results of the query are returned. Per particle
    attributes can be queried using the particleId or the order of the particle in
    the particle array. If an object was edited, nothing is returned.
    
    Flags:
    - attribute : at                 (unicode)       [query,edit]
        Used in per particle attribute query and edit. Specifies the name of the
        attribute being queried or edited.
    
    - cache : ch                     (bool)          [create,query,edit]
        Turns caching on/off for the particle shape.
    
    - conserve : c                   (float)         [query,edit]
        Conservation of momentum control (between 0 and 1).  Specifies the fraction of
        the particle shape's existing momentum which is conserved from frame to frame. A
        value of 1 (the default) corresponds to true Newtonian physics, in which
        momentum is conserved.
    
    - count : ct                     (bool)          [query]
        Returns the number of particles in the object.
    
    - deleteCache : dc               (bool)          [create]
        Deletes the particle shapes cache. This command is not undoable.
    
    - dynamicAttrList : dal          (bool)          [query]
        Returns a list of the dynamic attributes in the object.
    
    - floatValue : fv                (float)         [edit]
        Used only in per particle attribute edit.  Specifies that the edit is of a float
        attribute and must be followed by the new float value.
    
    - gridSpacing : grs              (float)         [create,query]
        Spacing between particles in the grid.
    
    - inherit : i                    (float)         [query,edit]
        Inherit this fraction (0-1) of emitting object's velocity.
    
    - jitterBasePoint : jbp          (float, float, float) [create,query]
        Base point (center point) for jitters.  The command will create one swatch of
        jitters for each base point.  It will pair up other flags with base points in
        the order they are given in the command line.  If not enough instances of the
        other flags are availble, the last one on the line with be used for all other
        instances of -jpb.
    
    - jitterRadius : jr              (float)         [create,query]
        Max radius from the center to place the particle instances.
    
    - lowerLeft : ll                 (float, float, float) [create,query]
        Lower left point of grid.
    
    - name : n                       (unicode)       [query,edit]
        name of particle object
    
    - numJitters : nj                (int)           [create,query]
        Number of jitters (instances) per particle.
    
    - order : order                  (int)           [query,edit]
        Used in per particle attribute query and edit. Specifies the zero-based order
        (index) of the particle whose attribute is being queried  or edited in the
        particle array. Querying the value of a per particle attribute requires the
        -attribute and -id or -order flags and their arguments to precede the -q flag.
    
    - particleId : id                (int)           [query,edit]
        Used in per particle attribute query and edit. Specifies the id of the particle
        whose attribute is being queried or edited. Querying the value of a per particle
        attribute requires the -attribute and -id or -order flags and their arguments to
        precede the -q flag.
    
    - perParticleDouble : ppd        (bool)          [query]
        Returns a list of the per-particle double attributes, excluding initial-state,
        cache, and information-only attributes.
    
    - perParticleVector : ppv        (bool)          [query]
        Returns a list of the per-particle vector attributes, excluding initial-state,
        cache, and information-only attributes.
    
    - position : p                   (float, float, float) []
        World-space position of each particle.
    
    - shapeName : sn                 (unicode)       [query,edit]
        Specify the shape name used for geometry instancing. DO not confuse this with
        the -n flag which names the particle object.
    
    - upperRight : ur                (float, float, float) [create,query]
        Upper right point of grid.
    
    - vectorValue : vv               (float, float, float) [edit]
        Used only in per particle attribute edit.  Specifies that the edit is of a
        vector attribute and must be followed by all three float values for the vector.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.nParticle`
    """
    pass


def addPP(*args, **kwargs):
    """
    Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for an
    attribute of an emitter or field.  The -atr flag identifies the attribute.  If
    no attribute is named, addPP returns a warning and does nothing. The command
    adds any other necessary attributes wherever they are needed, and makes all
    necessary connections.  If any of the attributes already exist, the command
    simply connects to them.  The command also toggles any relevant attributes in
    the emitter or field to indicate that per-point capability is being used. The
    command adds a separate per-point attribute to the owning object for each
    emitter/field.  For example, for emission rate, there is a separate ratePP for
    each emitter.  These attributes are named according to the convention
    emitter/field nameattr namePP.  For example, if a particle shape owned an
    emitter smoke, that shape would get attribute smokeRatePP.The name of the object
    must be the emitter or field for which per-point capability is to be added (or
    the name of its parent transform).  The addPP command adds the per-point
    capability for that emitter or field but not for any others owned by the same
    object.  If per-point capability is not supported for a named object, the
    command will trigger a warning, but will continue executing for any other
    objects which were valid. If no objects are named, addPP uses any objects in the
    current selection list for which the specified attribute is applicable.  (For
    example, it would add per-point rate for all selected emitters.) If addPP
    detects that the owner object has left-over attributes from a deleted emitter,
    it will remove those attributes before adding the new ones.  Thus, you can
    delete the emitter, make a new one, and run addPP again, and addPP will clean up
    after the deleted emitter.  This is most commonly used if you have a geometry
    emitter and then decide to change the geometry.  Likewise, if addPP detects that
    some cvs or vertices have been added to the geometry, then it will expand the
    corresponding multi-attributes as necessary.  However, if it detects that some
    cvs/vertices have been removed, it will not remove any entries from the multi.
    See the user manual for more discussion.
    
    Flags:
    - attribute : atr                (unicode)       [create]
        Name of attribute to which you wish to add PP capability. Currently the only
        attribute supported is rate (for emitters).                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.addPP`
    """
    pass


def drag(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. Drag exerts a
    friction, or braking force proportional to the speed of a moving object. If
    direction is not enabled, the drag acts opposite to the current velocity of the
    object. If direction is enabled, it acts opposite to the component of the
    velocity in the specified direction. The force is independent of the position of
    the affected object. The transform is the associated dependency node. Use
    connectDynamic to cause the field to affect a dynamic object. If fields are
    created, this command returns the names of each of the fields. If a field was
    queried, the results of the query are returned. If a field was edited, the field
    name is returned. If object names are provided or the active selection list is
    non-empty, the command creates a field for every object in the list and calls
    addDynamic to add it to the object. If the list is empty, the command defaults
    to -pos 0 0 0. Setting the -pos flag with objects named on the command line is
    an error.
    
    Flags:
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - directionX : dx                (float)         [query,edit]
        X-component of direction.
    
    - directionY : dy                (float)         [query,edit]
        Y-component of direction.
    
    - directionZ : dz                (float)         [query,edit]
        Z-component of direction
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - useDirection : ud              (bool)          [query,edit]
        Enable/disable direction. Drag will use -dx/-dy/-dz arguments if and only if
        this flag is set true.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.drag`
    """
    pass


def gravity(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. A gravity field
    simulates the Earth's gravitational force.   It pulls objects in a fixed
    direction (generally downward) entirely independent of their position or mass.
    The transform is the associated dependency node. Use connectDynamic to cause the
    field to affect a dynamic object. If fields are created, this command returns
    the names of each of the fields. If a field was queried, the results of the
    query are returned. If a field was edited, the field name is returned. If object
    names are provided or the active selection list is non-empty, the command
    creates a field for every object in the list and calls addDynamic to add it to
    the object. If the list is empty, the command defaults to -pos 0 0 0. Setting
    the -pos flag with objects named on the command line is an error. The default
    for -dx -dy -dz is always the opposite of the current up direction. For example,
    if the current up direction is (0,1,0) (a standard Maya configuration), then the
    gravity default is -dx 0 -dy -1 -dz 0.  The default for -a is 9.8.  9.8 meters
    per second squared happens to be standard Earth gravity, but in fact Maya
    interprets this value as centimeters per second squared.  If we were to use it
    as meters per second squared then with default Maya units, your particles would
    vanish almost in the wink of an eye. If you want a different value, set it in
    the gravity option box.
    
    Flags:
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - directionX : dx                (float)         [query,edit]
        X-component of direction.
    
    - directionY : dy                (float)         [query,edit]
        Y-component of direction.
    
    - directionZ : dz                (float)         [query,edit]
        Z-component of direction
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.gravity`
    """
    pass


def vortex(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. A vortex field
    pulls objects in a circular direction, like a whirlpool or tornado.   Objects
    affected by the vortex field tend to rotate around the axis specified by -ax,
    -ay, and -az. The transform is the associated dependency node. Use
    connectDynamic to cause the field to affect a dynamic object. If fields are
    created, this command returns the names of each of the fields. If a field was
    queried, the results of the query are returned. If a field was edited, the field
    name is returned. If object names are provided or the active selection list is
    non-empty, the command creates a field for every object in the list and calls
    addDynamic to add it to the object. If the list is empty, the command defaults
    to -pos 0 0 0. Setting the -pos flag with objects named on the command line is
    an error.
    
    Flags:
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - axisX : ax                     (float)         [query,edit]
        X-component of vortex axis
    
    - axisY : ay                     (float)         [query,edit]
        Y-component of vortex axis
    
    - axisZ : az                     (float)         [query,edit]
        Z-component of vortex axis
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.vortex`
    """
    pass


def event(*args, **kwargs):
    """
    The event command assigns collision events to a particle object. Collision
    events are stored in multi-attributes in the particle shape. The event command
    returns the event name.
    
    Flags:
    - count : ct                     (int)           [query,edit]
        Collision number (for each particle) to which this event applies. Zero (the
        default) indicates that it applies to all collisions.
    
    - delete : d                     (bool)          [create]
        Delete the specified event.
    
    - dieAtCollision : die           (bool)          [query,edit]
        Particle dies at the collision specified by count.If no count value is given,
        die at first collision.
    
    - emit : em                      (int)           [query,edit]
        Emit n additional particles into the assigned target object. The original
        (colliding) particle survives as well, and remains in its original object.  The
        new particles have age zero and mass equal to the emitting particle. They use
        the velocity inheritance parameter of the target object.
    
    - idNumber : id                  (int)           []
    
    - list : ls                      (bool)          [create]
        List all events for the chosen shape, like this: event1Name event2Name ... If no
        shape identified, list all events for all shapes, like this: shape1Name
        event1Name shape2Name event2Name... Returns a string array.
    
    - name : n                       (unicode)       [create,query,edit]
        Assign a name to an event you are creating, or identify an event you wish to
        edit, query, or delete. See examples.
    
    - proc : pr                      (script)        [create,query,edit]
        Specify a MEL proc to be called each time the event occurs. This must be a
        global proc with arguments as follows: global proc procName( string obj, int id,
        string objHit ); Arguments passed in are the name of the particle object, the id
        of the particle which collided, and the name of the object collided with.  You
        can use particle -id -q to get values of the particle's attributes.
    
    - random : r                     (bool)          [query,edit]
        Used with -split and -emit flags.  If -random is set true and -split or -emit is
        set to n, then a random number of particles uniformly distributed between 1 and
        n will be created at the event.
    
    - rename : re                    (unicode)       [query]
        Assign a new name to an event you are editing. See examples.
    
    - select : s                     (bool)          []
        This flag is obsolete.  See the -name flag.
    
    - split : spl                    (int)           [query,edit]
        Colliding particle splits into specified number of new particles. These new
        particles become part of the assigned target object. If no target has been
        assigned, they become part of the same object.  The new particles inherit the
        current age of the particle that split.  They use the velocity inheritance
        parameter of the target object.  If you set both emit and split, the event will
        do both: first emit new particles, then split the original one. This is a change
        from earlier versions where emit and split were mutually exclusive.
    
    - spread : sp                    (float)         [query,edit]
        Particles created at collision will spread out a random amount from the rebound
        direction of the colliding particle.  The spread is specified as a fraction
        (0-1) of 90 degrees.  If spread is set at 0 (the default) all the new particles
        created may coincide.
    
    - target : t                     (unicode)       [query,edit]
        Target object for emitting or split particles. New particles created through the
        -emit or -split flags join this object.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.event`
    """
    pass


def air(*args, **kwargs):
    """
    For each listed object, the command creates a new field. The field has a shape
    which lives in the DAG and it has an associated dependency node. The field is
    added to the list of fields owned by the object. Use connectDynamic to cause the
    field to affect a dynamic object. Note that if more than one object is listed, a
    separate field is created for each object. If fields are created, this command
    returns the names of each owning shape and of the field shapes themselves. If a
    field was queried, the results of the query are returned. If a field was edited,
    the field name is returned. If no object names are provided but the active
    selection list is non-empty, the command creates a field for every object in the
    list. If the list is empty, the command defaults to -pos 0 0 0. The air field
    simulates the effects of moving air. The affected objects will be accelerated or
    decelerated so that their velocities match that of the air. With the '-vco true'
    flag thrown, only accelerations are applied. By parenting an air field to a
    moving part of an object (ie. a foot of a character) and using '-i 1 -m 0 -s .5
    -vco true' flags, one can simulate the movement of air around the foot as it
    moves, since the TOTAL velocity vector of the field would be only based on the
    movement of the foot. This can be done while the character walks through leaves
    or dust on the ground. For each listed object, the command creates a new field.
    The transform is the associated dependency node. Use connectDynamic to cause the
    field to affect a dynamic object. If fields are created,  this command returns
    the field names. If a field was queried, the results of the query are returned.
    If a field was edited, the field name is returned. If the -pos flag is
    specified, a field is created at the position specified. If not, if object names
    are provided or the active selection list is non-empty, the command creates a
    field for every object in the list and calls addDynamic to add it to the object;
    otherwise the command defaults to -pos 0 0 0. Setting the -pos flag with objects
    named on the command line is an error.
    
    Flags:
    - attenuation : att              (float)         [query,edit]
        Attentuation rate of field
    
    - directionX : dx                (float)         [query,edit]
    
    - directionY : dy                (float)         [query,edit]
    
    - directionZ : dz                (float)         [query,edit]
        Direction that the air will try to match the affected particles' velocity to.
        NOTE: This is not the velocity; this is only the direction. Use the -s flag to
        set the speed.
    
    - enableSpread : es              (bool)          [query,edit]
        This tells the system whether or not to use the spread angle given by '-sp'. If
        this is 'false' then all connected objectswithin the maximum distance will be
        affected. Also, if this is set to 'false', all affected objects are forced to
        match their velocities along the direction vector. If this is set to 'true' and
        spread is used, then the direction of the force is along the direction from the
        field to the object.
    
    - fanSetup : fs                  (bool)          [edit]
        Similar to 'windSetup' except that the effects of a fan or a person blowing air
        are approximated. The user can pass the same flags on the command line to adjust
        them from the defaults. These are the values that get set to approximate a
        'fan': inheritVelocity 1.0 inheritRotation true componentOnly false enableSpread
        true spread .5 (45 degrees from center )
    
    - inheritRotation : iro          (bool)          [query,edit]
        If this is set to 'true', then the direction vector described with -dx, -dy, and
        -dz will be considered local to the owning object. Therefore, if the owning
        object's transform undergoes any rotation (by itself or one of its parents), the
        direction vector of the air field will undergo that same rotation.
    
    - inheritVelocity : iv           (float)         [query,edit]
        Amount (from 0 to 1) of the field-owner's velocity added to the vector
        determined by the direction and speed flags. The combination of these two
        vectors makes up the TOTAL velocity vector for the air field. This allows the
        air to be determined directly by the motion of the owning object.
    
    - magnitude : m                  (float)         [query,edit]
        Strength of field.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which field is exerted. -1 indicates that the field has no
        maximum distance.
    
    - name : n                       (unicode)       [query,edit]
        name of field
    
    - perVertex : pv                 (bool)          [query,edit]
        Per-vertex application. If this flag is set true, then each individual point
        (CV, particle, vertex,etc.) of the chosen object exerts an identical copy of the
        force field. If this flag is set to false, then the froce is exerted only from
        the geometric center of the set of points.
    
    - position : pos                 (float, float, float) [query,edit]
        Position in space (x,y,z) where you want to place a gravity field. The gravity
        then emanates from this position in space rather than from an object. Note that
        you can both use -pos (creating a field at a position) and also provide object
        names.
    
    - speed : s                      (float)         [query,edit]
        How fast the affected objects' speed reaches the speed (based on the -mag, -dx,
        -dy, -dz flags) of the air field. This value gets clamped internally to be
        between 0.0 and 1.0.  A value of 0.0 will make the air field have no effect. A
        value of 1.0 will try to match the air field's speed much quicker, but not
        necessarily immediately.
    
    - spread : sp                    (float)         [query,edit]
        This represents the angle from the direction vector within which objects will be
        affected. The values are in the range of 0 to 1. A value of 0 will result in an
        effect only exactly in front of the air field along the direction vector. A
        value of 1 will result in any object in front of the owning object, 90 degrees
        in all direction from the direction vector.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - velocityComponentOnly : vco    (bool)          [query,edit]
        If this is 'false', the air will accelerate or decelerate the affected objects
        so that their velocities will eventually match the TOTAL velocity vector of the
        air field. If this is 'true', only ACCELERTION is applied to the affected
        objects so that their velocity component along the TOTAL velocity vector matches
        or is greater in magnitude than the TOTAL velocity vector. This will not slow
        objects down to match velocities, only speed them up to match components. This
        is most useful when using the -iv flag with a value 0.
    
    - volumeExclusion : vex          (bool)          [query,edit]
        Volume exclusion of the field.  If true, points outside the volume (defined by
        the volume shape attribute) are affected,  If false, points inside the volume
        are affected.  Has no effect if volumeShape is set to none.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the field.  Volume offset translates the field's volume by the
        specified amount from the actual field location. This is in the field's local
        space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the field.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which the field has effect. Values are: none,cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the field.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.
    
    - wakeSetup : wks                (bool)          [edit]
        Like the 'windSetup' and 'fanSetup', 'wakeSetup' sets certain values in the
        field to approximate the movement of air near a moving object, such as  a
        character's foot or hand. The values that are set are: inheritVelocity 1.0
        inheritRotation false componentOnly true enableSpread false speed 0.0
    
    - windSetup : wns                (bool)          [edit]
        This will set some of the values above in a way that approximates the effects of
        a basic wind. This allows the user to then change certain values as he/she
        wishes on the same command line. First the preset values get set, and then any
        other flags that were passed get taken into account. These are the values that
        get set to approximate 'wind': inheritVelocity 0.0 inheritRotation true
        componentOnly false enableSpread false                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.air`
    """
    pass


def nBase(*args, **kwargs):
    """
    Edits one or more nBase objects. Note that nBase objects include nCloth, nRigid
    and nParticle objects, but the options on this command do not currently apply to
    nParticle objects.
    
    Flags:
    - clearCachedTextureMap : cct    (unicode)       [create,edit]
        Clear the cached texture map for the specified attribute from the nBase.
    
    - clearStart : cs                (bool)          [create,edit]
        Indicates that start state should be cleared
    
    - stuffStart : ss                (bool)          [create,edit]
        Indicates that current state should be stuffed into the start state
    
    - textureToVertex : ttv          (unicode)       [create,edit]
        Transfer the texture map data for the specified attribute into the related per-
        vertex attribute.                                   Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.nBase`
    """
    pass


def particle(*args, **kwargs):
    """
    The particle command creates a new particle object from a list of world space
    points. If a particle object is created, the command returns the names of the
    new particle shape and its associated particle object dependency node. If an
    object was queried, the results of the query are returned. Per particle
    attributes can be queried using the particleId or the order of the particle in
    the particle array. If an object was edited, nothing is returned.
    
    Flags:
    - attribute : at                 (unicode)       [query,edit]
        Used in per particle attribute query and edit. Specifies the name of the
        attribute being queried or edited.
    
    - cache : ch                     (bool)          [create,query,edit]
        Turns caching on/off for the particle shape.
    
    - conserve : c                   (float)         [query,edit]
        Conservation of momentum control (between 0 and 1).  Specifies the fraction of
        the particle shape's existing momentum which is conserved from frame to frame. A
        value of 1 (the default) corresponds to true Newtonian physics, in which
        momentum is conserved.
    
    - count : ct                     (bool)          [query]
        Returns the number of particles in the object.
    
    - deleteCache : dc               (bool)          [create]
        Deletes the particle shapes cache. This command is not undoable.
    
    - dynamicAttrList : dal          (bool)          [query]
        Returns a list of the dynamic attributes in the object.
    
    - floatValue : fv                (float)         [edit]
        Used only in per particle attribute edit.  Specifies that the edit is of a float
        attribute and must be followed by the new float value.
    
    - gridSpacing : grs              (float)         [create,query]
        Spacing between particles in the grid.
    
    - inherit : i                    (float)         [query,edit]
        Inherit this fraction (0-1) of emitting object's velocity.
    
    - jitterBasePoint : jbp          (float, float, float) [create,query]
        Base point (center point) for jitters.  The command will create one swatch of
        jitters for each base point.  It will pair up other flags with base points in
        the order they are given in the command line.  If not enough instances of the
        other flags are availble, the last one on the line with be used for all other
        instances of -jpb.
    
    - jitterRadius : jr              (float)         [create,query]
        Max radius from the center to place the particle instances.
    
    - lowerLeft : ll                 (float, float, float) [create,query]
        Lower left point of grid.
    
    - name : n                       (unicode)       [query,edit]
        name of particle object
    
    - numJitters : nj                (int)           [create,query]
        Number of jitters (instances) per particle.
    
    - order : order                  (int)           [query,edit]
        Used in per particle attribute query and edit. Specifies the zero-based order
        (index) of the particle whose attribute is being queried  or edited in the
        particle array. Querying the value of a per particle attribute requires the
        -attribute and -id or -order flags and their arguments to precede the -q flag.
    
    - particleId : id                (int)           [query,edit]
        Used in per particle attribute query and edit. Specifies the id of the particle
        whose attribute is being queried or edited. Querying the value of a per particle
        attribute requires the -attribute and -id or -order flags and their arguments to
        precede the -q flag.
    
    - perParticleDouble : ppd        (bool)          [query]
        Returns a list of the per-particle double attributes, excluding initial-state,
        cache, and information-only attributes.
    
    - perParticleVector : ppv        (bool)          [query]
        Returns a list of the per-particle vector attributes, excluding initial-state,
        cache, and information-only attributes.
    
    - position : p                   (float, float, float) []
        World-space position of each particle.
    
    - shapeName : sn                 (unicode)       [query,edit]
        Specify the shape name used for geometry instancing. DO not confuse this with
        the -n flag which names the particle object.
    
    - upperRight : ur                (float, float, float) [create,query]
        Upper right point of grid.
    
    - vectorValue : vv               (float, float, float) [edit]
        Used only in per particle attribute edit.  Specifies that the edit is of a
        vector attribute and must be followed by all three float values for the vector.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.particle`
    """
    pass


def fluidEmitter(*args, **kwargs):
    """
    Creates, edits or queries an auxiliary dynamics object (for example, a field or
    emitter). Creates an emitter object. If object names are provided or if objects
    are selected, applies the emitter to the named/selected object(s)in the scene.
    Fluid will then be emitted from each. If no objects are named or selected, or if
    the -pos option is specified, creates a positional emitter. If an emitter was
    created, the command returns the name of the object owning the emitter, and the
    name of emitter shape. If an emitter was queried, the command returns the
    results of the query.
    
    Flags:
    - cycleEmission : cye            (unicode)       [query,edit]
        Possible values are noneand frame.Cycling emission restarts the random number
        stream after a specified interval.  This can either be a number of frames or a
        number of emitted particles.  In each case the number is specified by the
        cycleInterval attribute. Setting cycleEmission to frameand cycleInterval to 1
        will then re-start the random stream every frame. Setting cycleInterval to
        values greater than 1 can be used to generate cycles for games work.
    
    - cycleInterval : cyi            (int)           [query,edit]
        Specifies the number of frames or particles between restarts of the random
        number stream.  See cycleEmission.  Has no effect if cycleEmission is set to
        None.
    
    - densityEmissionRate : der      (float)         [query,edit]
        Rate at which density is emitted.
    
    - fluidDropoff : fdr             (float)         [query,edit]
        Fluid Emission Dropoff in volume
    
    - fuelEmissionRate : fer         (float)         [query,edit]
        Rate at which  is emitted.
    
    - heatEmissionRate : her         (float)         [query,edit]
        Rate at which density is emitted.
    
    - maxDistance : mxd              (float)         [query,edit]
        Maximum distance at which emission ends.
    
    - minDistance : mnd              (float)         [query,edit]
        Minimum distance at which emission starts.
    
    - name : n                       (unicode)       [create,query,edit]
        Object name
    
    - position : pos                 (float, float, float) [create,query,edit]
        world-space position
    
    - rate : r                       (float)         [query,edit]
        Rate at which particles emitted (can be non-integer). For point emission this is
        rate per point per unit time. For surface emission it is rate per square unit of
        area per unit time.
    
    - torusSectionRadius : tsr       (float)         [query,edit]
        Section radius for a torus volume.  Applies only to torus. Similar to the
        section radius in the torus modelling primitive.
    
    - type : typ                     (unicode)       [query,edit]
        Type of emitter. The choices are omni | dir | direction | surf | surface | curve
        | curv. The default is omni. The full definition of these types are:
        omnidirectional point emitter, directional point emitter, surface emitter, or
        curve emitter.
    
    - volumeOffset : vof             (float, float, float) [query,edit]
        Volume offset of the emitter.  Volume offset translates the emission volume by
        the specified amount from the actual emitter location.  This is in the emitter's
        local space.
    
    - volumeShape : vsh              (unicode)       [query,edit]
        Volume shape of the emitter.  Sets/edits/queries the field's volume shape
        attribute.  If set to any value other than none, determines a 3-D volume within
        which particles are generated. Values are: cube,sphere,cylinder,cone,torus.
    
    - volumeSweep : vsw              (float)         [query,edit]
        Volume sweep of the emitter.  Applies only to sphere, cone, cylinder, and torus.
        Similar effect to the sweep attribute in modelling.                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.fluidEmitter`
    """
    pass


def dynGlobals(*args, **kwargs):
    """
    This node edits and queries the attributes of the active dynGlobals node in the
    scene. There can be only one active node of this type. The active dynGlobals
    node is the first one that was created, either with a createNodecommand or by
    accessing/editing any of the attributes on the node through this command.
    
    Flags:
    - active : a                     (bool)          [query]
        This flag returns the name of the active dynGlobals node in the the scene.  Only
        one dynGlobals node is active. It is the first on created.  Any additional
        dynGlobals nodes will be ignored.
    
    - listAll : la                   (bool)          [query]
        This flag will list all of the dynGlobals nodes in the scene.
    
    - overSampling : os              (int)           [query,edit]
        This flag will set the current overSampling value for all of the particle in the
        scene.                  Flag can have multiple arguments, passed either as a
        tuple or a list.
    
    
    Derived from mel command `maya.cmds.dynGlobals`
    """
    pass


def arrayMapper(*args, **kwargs):
    """
    Create an arrayMapper node and connect it to a target object. If the -type flag
    is used, then this command also creates an external node used for computing the
    output values. If the input attribute does not already exist, it will be
    created. The output attribute must exists. If    a flag is omitted, the
    selection list will be used to supply the needed objects. If none are found,
    that action is omitted.
    
    Flags:
    - destAttr : da                  (unicode)       [create]
        Specifies the attribute which will be the downstream connection for the output
        data from the mapper node. The attribute type will be used to determine which
        output attribute to use: float array gets outValuePP, vector array gets
        outColorPP. If the flag is omitted, no output connection is made.
    
    - inputU : iu                    (unicode)       [create]
        Specifies the upstream attribute to connect to the mapper's uCoordPP attribute.
        If the flag is omitted, no input connection is made.
    
    - inputV : iv                    (unicode)       [create]
        Specifies the upstream attribute to connect to the mapper's vCoordPP attribute.
        If the flag is omitted, no input connection is made.
    
    - mapTo : mt                     (unicode)       [create]
        Specifies an existing node to be used to compute the output values. This node
        must be of the appropriate type. Currently, only ramp nodes may be used.
    
    - target : t                     (unicode)       [create]
        Specifies the target object to be connected to.
    
    - type : ty                      (unicode)       [create]
        Specifies the node type to create which will be used to compute the output
        values. Currently, only ramp is valid. If the flag is omitted, no connection is
        made and the external node is not created.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.arrayMapper`
    """
    pass


def rigidSolver(*args, **kwargs):
    """
    This command sets the attributes for the rigid solver            In query mode,
    return type is based on queried flag.
    
    Flags:
    - autoTolerances : at            (bool)          [query,edit]
        Turns the auto tolerance calculation on and off.  The auto tolerances
        calculation will override the default or user defined values of the step size
        and collision tolerance value that is calculated based on the objects in the
        scene. Default: 0 (off)
    
    - bounciness : b                 (bool)          [query,edit]
        Turns bounciness on and off for the an the objects in the simulation. Default
        value: on
    
    - cacheData : cd                 (bool)          [query,edit]
        Turns the cache on fall all rigid bodies in the system. Default value: off
    
    - collide : c                    (bool)          [query,edit]
        Disallows the interpenetration of the two rigid bodies listed. Default: Collide
        is on for all bodies.
    
    - collisionTolerance : ct        (float)         [query,edit]
        Sets the collision tolerance.  This is the error at which two objects are
        considered to have collided. Range:   0.0005 - 1.000 Default: 0.02
    
    - contactData : ctd              (bool)          [query,edit]
        Turns the contact data information on/off for all rigid bodies. Default value:
        off
    
    - create : cr                    (bool)          [create]
        Creates a new rigid solver.
    
    - current : cu                   (bool)          [create]
        Sets rigid solver as the current solver.
    
    - deleteCache : deleteCache      (bool)          [query,edit]
        Deletes the cache for all rigid bodies in the system.
    
    - displayCenterOfMass : dcm      (bool)          [query,edit]
        Displays the center of mass icon. Default value: on
    
    - displayConstraint : dc         (bool)          [query,edit]
        Displays the constraint vectors. Default value: on
    
    - displayVelocity : dv           (bool)          [query,edit]
        Displays the velocity vectors. Default value: off
    
    - dynamics : d                   (bool)          [query,edit]
        Turns dynamics on and off for the an the objects in the simulation. Default
        value: on
    
    - friction : f                   (bool)          [query,edit]
        Turns friction on and off for the an the objects in the simulation. Default
        value: on
    
    - interpenetrate : i             (bool)          [query,edit]
        Allows the two rigid bodies listed to interpenetrate. Default: interpenetration
        is off for all bodies.
    
    - interpenetrationCheck : ic     (bool)          [edit]
        Checks for interpenetrating rigid bodies in the scene.
    
    - name : n                       (unicode)       [create,query,edit]
        Name of the new object
    
    - rigidBodies : rb               (bool)          [query]
        Returns a list of rigid bodies in the solver.
    
    - rigidBodyCount : rbc           (bool)          [query]
        Returns the number of rigid bodies in the solver.
    
    - showCollision : sc             (bool)          [query,edit]
        Displays the colliding objects in a different color.
    
    - showInterpenetration : si      (bool)          [query,edit]
        Displays the interpenetrating objects in a different color.
    
    - solverMethod : sm              (int)           [query,edit]
        Sets the solver method.  The choices are 0 | 1 | 2. 0 = Euler (fastest/least
        acurate), 1 = Runge-Kutta ( slower/more acurate), 2 = adaptive Runge-Kutta
        (slowest/most acurate). The default is 2 (adaptive Runge-Kutta)
    
    - startTime : stt                (float)         [create,query,edit]
        Sets the start time for the solver.
    
    - state : st                     (bool)          [query,edit]
        Turns the rigid solver on or off.
    
    - statistics : sta               (bool)          [query,edit]
        Turns the statistic information on/off for all rigid bodies. Default value: off
    
    - stepSize : s                   (float)         [query,edit]
        Sets the solvers step size.  This is the maximum size of a single step the
        solver will take at one time. Range:   0.0004 - 0.100 Default: 0.0333
    
    - velocityVectorScale : vs       (float)         [query,edit]
        scales the velocity vector display. Default value: 1.0                  Flag can
        have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.rigidSolver`
    """
    pass


def spring(*args, **kwargs):
    """
    The spring command can do any of the following:\* create a new spring object
    (shape plus transform).  The shape contains springs between the points
    (particles, cvs, etc.) of the objects selected or listed on the command line.\*
    create new springs and add them to an existing spring object\* edit or query
    certain attributes of an existing spring objectOne spring objectmay have
    hundreds or even thousands of individual springs. Certain attributes of the
    spring object specify exactly where the springs are attached to which other
    objects.Springs may be attached to the following: particles, vertices of soft
    bodies, CVs or edit points of curves or surfaces, vertices of polygonal objects,
    and points of lattices. In the case where one endpoint of a spring is non-
    dynamic (a CV, edit point, etc.), the spring does not affect its motion, but the
    motion of the point affects the spring. A spring will be created only if at
    least one of the endpoints is dynamic: for example, a spring will never be
    created between two CVs. A single spring object can hold springs which are
    incident to any number of other objects.The spring has creation-only flags and
    editable flags.  Creation-only flags (minDistance, maxDistance, add, exclusive,
    all, wireframe, walklength, checkExisting) can be used only when creating new
    springs (including adding springs to existing spring object).  Editable flags
    modify attributes of an existing spring object.If a spring object is created,
    this command returns the names of the shape and transform.  If a spring object
    is queried, the command returns the results of the query.
    
    Flags:
    - addSprings : add               (bool)          [create]
        If specified, springs will be added to the existing selected set of springs.
        (Default is to create a new spring object.)
    
    - allPoints : all                (bool)          [create,edit]
        If True, sets the mode of spring application to All.  This will add springs
        between all points selected. (Default is False.)
    
    - count : ct                     (bool)          [query]
        Return the number of springs in the shape.  Query-only. We maintain this flag
        only for compatibility with earlier versions of Maya.  To get the count of
        springs, it is much faster and simpler to use the spring shape's count
        attribute: getAttr shapeName.count.
    
    - damp : dmp                     (float)         []
    
    - damping : d                    (float)         [create,query,edit]
        Damping factor for the springs created in the spring object. (Default = 0.2 )
    
    - dampingPS : dPS                (float)         [create,query,edit]
        Damping factor for the springs created in the spring object. This will
        initialize all the entries in dampingPS to the specified value. In both the flag
        and the attribute name, PSstands for per-spring.(Default = 0.2 )
    
    - endForceWeight : efw           (float)         [create,query,edit]
        Amount of the force of the spring that gets applied to the point to which the
        spring ends. Valid range is from 0.0 to 1.0. (Default = 1.0 )
    
    - exclusive : exc                (bool)          [create]
        If true, tells the command to create springs only between pairs of points which
        are not in the same object. (Default is False.)
    
    - length : l                     (float)         [create,query,edit]
        Vestigial form of restLength.Please use restLengthinstead.
    
    - maxDistance : mxd              (float)         [create,edit]
        Maximum distance between two points that a spring would be considered.
    
    - minDistance : mnd              (float)         [create]
        Minimum distance between two points that a spring would be considered. (Default
        = 0.0. See Defaults for more information on this flag's default.)
    
    - minMax : mm                    (bool)          [create]
        If True, sets the mode of the spring application to Min/Max. This will add
        springs between all points from the specified point groups that are between the
        minimum and maximum distance values set with min and max. (Default is False.)
        Note: This gets automatically set if either the min or max flags are used.
    
    - name : n                       (unicode)       [create,query]
        Name of spring object.
    
    - noDuplicate : nd               (bool)          [create]
        Check for existing springs and don't add a new spring between two points already
        connected by a spring in the same object. Only the object the command is working
        on is checked.  This flag is relevant only when using -add. (Default = false)
    
    - restLength : rl                (float)         [create,query,edit]
        Per-object rest length for the new springs. Springs can use either their per-
        object or per-spring rest length.  See the -lPS and -ulp flags.
    
    - restLengthPS : rPS             (float)         [create,query,edit]
        Per-spring rest length for the new springs. This will initialize all the entries
        in restLengthPS to the specified value. If this flag is not thrown, each rest
        length will be initialized to the distance between the two  points at the time
        the spring is created (i.e., the initial length of the spring).   When playing
        back, springs can use either their per-spring or per-object rest length.  See
        the -rl and -urp flags. In both the flag and the attribute name, PSstands for
        per-spring.
    
    - startForceWeight : sfw         (float)         [create,query,edit]
        Amount of the force of the spring that gets applied to the point from which the
        spring starts. Valid range is from 0.0 to 1.0. (Default = 1.0 )
    
    - stiffness : s                  (float)         [create,query,edit]
        Stiffness of the springs created in the spring object. (Default = 1.0 ) -damp
        float Vestigial form of damping.Please use dampinginstead.
    
    - stiffnessPS : sPS              (float)         [create,query,edit]
        Stiffness of the springs created in the spring object. This will initialize all
        the entries in stiffnessPS to the specified value. In both the flag and the
        attribute name, PSstands for per-spring.(Default = 1.0 )
    
    - strength : str                 (float)         []
    
    - useDampingPS : udp             (bool)          [create,query,edit]
        Specifies whether to use dampingPS (per spring damping). If set to false, the
        per object damping attribute value will be used. This flag simply sets the
        useDampingPS attribute of the spring shape. In both the flag and the attribute
        name, PSstands for per-spring.(Default = false )
    
    - useRestLengthPS : urp          (bool)          [create,query,edit]
        Specifies whether to use restLengthPS (per spring restLength). If set to false,
        the per object restLength attribute value will be used. This flag simply sets
        the useRestLengthPS attribute of the spring shape. In both the flag and the
        attribute name, PSstands for per-spring.(Default = false )
    
    - useStiffnessPS : usp           (bool)          [create,query,edit]
        Specifies whether to use stiffnessPS (per spring stiffness). If set to false,
        the per object stiffness attribute value will be used. This flag simply sets the
        useStiffnessPS attribute of the spring shape. In both the flag and the attribute
        name, PSstands for per-spring.(Default = false )
    
    - walkLength : wl                (int)           [create]
        This flag is valid only when doing wireframe creation. It will create springs
        between pairs of points connected by the specified number of edges.  For
        example, if walk length is 2, each pair of points separated by no more than 2
        edges will get a spring.  Walk length measures the distance between pairs of
        vertices just like the number of blocks measures the distance between two
        intersections in a city.
    
    - wireframe : wf                 (bool)          [create]
        If True, sets the mode of the spring application to Wireframe. This is valid
        only for springs created on a soft body. It will add springs along all edges
        connecting the adjacent points (vertices or CV's) of curves and surfaces.
        (Default is False.)                  Flag can have multiple arguments, passed
        either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.spring`
    """
    pass


def expression(*args, **kwargs):
    """
    This command describes an expression that belongs to the current scene. The
    expression is a block of code of unlimited length with a C-like syntax that can
    perform conversions, mathematical operations, and logical decision making on any
    numeric attribute(s) in the scene.  One expression can read and alter any number
    of numeric attributes.  Theoretically, every expression in a scene can be
    combined into one long expression, but it is recommended that they are separated
    for ease of use and editing, as well as efficiency.If this command is being sent
    by the command line or in a script, then the user should be sure to embed
    escaped newlines (\n), tabs (\t) for clarity when reading them in the expression
    editor.  Also, quotes in an expression must be escaped (\) so that they are not
    confused by the system as the end of your string.  When using the expression
    editor, these characters are escaped for you unless they are already within
    quotes.Note, expressions that alter or use per-particle attributes of a particle
    shape should use the 'dynExpression' command.
    
    Flags:
    - alwaysEvaluate : ae            (int)           [create,query,edit]
        If this is TRUE (the default), then the expression will be evaluated whenever
        time changes regardless of whether the other inputs have changed, and an output
        is requested.  If it is FALSE, then the expression will only be evaluated if one
        or more of the inputs changes and an output is requested.  Note, if 'time' or
        'frame' are inputs, then the expression will act as if this was set to TRUE.
    
    - animated : an                  (int)           [create,query,edit]
        Sets the animation mode on the expression node: 0 = Not Animated, 1 = Animated,
        2 = Animated with No Callback.
    
    - attribute : a                  (unicode)       [create,query,edit]
        Sets the name of the attribute to use for the expression
    
    - name : n                       (unicode)       [create,query,edit]
        Sets the name of the dependency graph node to use for the expression
    
    - object : o                     (unicode)       [create,query,edit]
        Sets the defaultobject for the expression.  This allows the expression writer to
        not type the object name for frequently-used objects.  See the examples below.
    
    - safe : sf                      (bool)          [query]
        Returns true if no potential side effect can occurs running that expression.
        Safe expression will be optimized to evaluate only when needed even if flagged
        alwaysEvaluate.
    
    - shortNames : sn                (bool)          [create,query,edit]
        When used with the -q/query flag, tells the command to return the expression
        with attribute names as short as possible. The default is to return the FULL
        attribute name, regardless of how the user entered it into the expression,
        including the object names.  With this flag set, attribute names are returned as
        their short versions, and any attribute that belongs to the default object, if
        there is one specified, will not display the object's name.
    
    - string : s                     (unicode)       [create,query,edit]
        Set the expression string
    
    - timeDependent : td             (bool)          [query]
        Returns true if expression refer to 'time' or 'frame' keywords. Those reference
        force the connection to time. If the expression is flagged as safe and not time
        dependend, then they will always evaluate on depend, even if alwaysEvaluate is
        on. Otherwise time change will dirty the expression.
    
    - unitConversion : uc            (unicode)       [query,edit]
        Insert specified unit conversion nodes at creation: all, none,or
        angularOnly.Default is all.For angularOnly, will insert unit conversion nodes
        only for angular attributes (allowing degrees-to-radians conversion).  This is
        for performance tuning. If queried, returns the option used when the expression
        was created or last edited.                  Flag can have multiple arguments,
        passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.expression`
    """
    pass


def rigidBody(*args, **kwargs):
    """
    This command creates a rigid body from a polygonal or nurbs surface.
    
    Flags:
    - active : act                   (bool)          [create,query,edit]
        Creates a rigid body that is active.  An active rigid body accepts and causes
        collisions and is effected by dynamic fields.  This is the default.
    
    - angularVelocity : av           (bool)          [query]
        Current angular velocity of rigid body.
    
    - applyForceAt : afa             (unicode)       [create,query,edit]
        Determines how forces are applied to the rigid body. The choices are
        centerOfMass | boundingBox | verticesOrCVs. Default: boundingBox
    
    - bounciness : b                 (float)         [create,query,edit]
        Sets the restitution (or bounciness) of the rigid body. Range:   0.0 - 2.0
        Default: 0.6
    
    - cache : c                      (bool)          [create,query,edit]
        Turns caching on (1) or off (0) for the rigid body. Default: off
    
    - centerOfMass : com             (float, float, float) [create,query,edit]
        Sets the center of mass (x,y,z) of the rigid body. Default: actual center of
        mass.
    
    - collisions : cl                (bool)          [create,query,edit]
        Truns collisions on/off for the rigid body.  If the collisions are turned of the
        rigid body will not collide with any other rigid body. Default: on.
    
    - contactCount : cc              (bool)          [query]
        returns the current contact count for the rigid body.
    
    - contactName : cn               (bool)          [query]
        returns all the rigid body names which are in contact with this shape.  One name
        for each contact will be returned.
    
    - contactPosition : cp           (bool)          [query]
        returns all the contact position.  One position for each contact will be
        returned.
    
    - damping : dp                   (float)         [create,query,edit]
        Sets the damping value of the rigid body. Range:   -2.0 - 2.0 Default: 0.0
    
    - deleteCache : dc               (bool)          [edit]
        Deletes the cache (if one exists) of the rigid body.
    
    - dynamicFriction : df           (float)         [create,query,edit]
        Sets the dynamic friction for the rigid body. Range:   0.0 - 1.0 Default: 0.2
    
    - force : f                      (bool)          [query]
        Current force on the rigid body.
    
    - ignore : ig                    (bool)          [create,query,edit]
        Causes the rigid body to be ignored in the rigid solver. Default: off
    
    - impulse : i                    (float, float, float) [create,edit]
        Applies an impulse (instantaneous) force on a rigid body. Default: 0.0 0.0 0.0
    
    - impulsePosition : imp          (float, float, float) [create,edit]
        The position at which the impulse is applied. Default: the bodies center of
        mass.
    
    - initialAngularVelocity : iav   (float, float, float) [create,query,edit]
        Sets the initial angular velocity of the rigid body. Default: 0.0 0.0 0.0
    
    - initialVelocity : iv           (float, float, float) [create,query,edit]
        Sets the initial velocity of the rigid body. Default: 0.0 0.0 0.0
    
    - layer : l                      (int)           [create,query,edit]
        Sets the collision layer of the rigid body.  Only rigid bodies in the same
        collision layer can collide with each other. Range:   = 0 Default: 0.
    
    - lockCenterOfMass : lcm         (bool)          [create,query,edit]
        Locks the center of mass for the rigid body. Default: off
    
    - mass : m                       (float)         [create,query,edit]
        Sets the mass of the rigid body. Range:   0 Default: 1.0
    
    - name : n                       (unicode)       [create,query,edit]
        Assigns the rigid body the given name.
    
    - orientation : o                (float, float, float) [create,query,edit]
        Sets the initial orientation (x,y,z) of the rigid body. Default: current
        orientation.
    
    - particleCollision : pc         (bool)          [create,query,edit]
        Turns the ability for a rigid body to collide with particles on and off.  The
        particles will exert a force on the rigid body. Default: off
    
    - passive : pas                  (bool)          [create,query,edit]
        Creates a rigid body that is passive.  A passive rigid body does not react to
        collisions but active rigid bodies can collide with it. Dynamic Fields will not
        effect a passive rigid body.  Only passive rigid bodies can be keyframed.
    
    - position : p                   (float, float, float) [create,query,edit]
        Sets the initial position (x,y,z) of the rigid body. Default: current position.
    
    - removeShape : rs               (unicode)       [create,query,edit]
        Remove the named shape.
    
    - solver : slv                   (unicode)       [create,query,edit]
        The name of the solver which this rigid node is to resided.  If the solver does
        not exists then the rigid body will not be created.  If the edit flag is thrown
        add the solver exists, the rigid body will be moved to that solver.
    
    - spinImpulse : si               (float, float, float) [create,edit]
        Applies an spin impulse (instantaneous rotational) force on a rigid body.
        Default: 0.0 0.0 0.0
    
    - standInObject : sio            (unicode)       [create,query,edit]
        Causes the simulator to use a stand in object for the simulation. The choices
        are none | cube | sphere. The default is none. Default: none
    
    - staticFriction : sf            (float)         [create,query,edit]
        Sets the static friction for the rigid body. Range:   0.0 - 1.0 Default: 0.2
    
    - tesselationFactor : tf         (int)           [create,query]
        Sets the tesselation factor for a rigid body surface. Range:   = 10 Default:
        200.
    
    - velocity : vel                 (bool)          [query]
        Current velocity of rigid body.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.rigidBody`
    """
    pass


def dynPaintEditor(*args, **kwargs):
    """
    Create a editor window that can be painted into
    
    Flags:
    - activeOnly : ao                (bool)          [query,edit]
        For Scene mode, this determines if only the active strokes will be refreshed.
    
    - autoSave : autoSave            (bool)          [query,edit]
        For Canvas mode, this determines if the buffer will be saved to a disk file
        after every stroke. Good for painting textures and viewing the results in shaded
        display in the model view.
    
    - camera : cam                   (unicode)       [query,edit]
        Sets the name of the camera which the Paint Effects panel looks through.
    
    - canvasMode : cm                (bool)          [query,edit]
        Sets the Paint Effects panel into Canvas mode if true.
    
    - canvasUndo : cu                (bool)          [edit]
        Does a fast undo in Canvas mode. This is a special undo because we are not using
        any history when we paint in Canvas mode so we provide a single level undo for
        the Canvas.
    
    - changeCommand : cc             (unicode, unicode, unicode, unicode) [create,query,edit]
        Parameters: First string: commandSecond string: editorNameThird string:
        editorCmdFourth string: updateFuncCall the command when something changes in the
        editor The command should have this prototype :  command(string $editor, string
        $editorCmd, string $updateFunc, int $reason)  The possible reasons could be : 0:
        no particular reason1: scale color2: buffer (single/double)3: axis 4: image
        displayed5: image saved in memory
    
    - clear : cl                     (float, float, float) [edit]
        Clears the buffer (if in Canvas mode) to the floating point values (R,G,B).
    
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - currentCanvasSize : ccs        (bool)          [query]
        In Query mode, this returns the (X,Y) resolution of the current canvas.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - displayAppearance : dsa        (unicode)       [query,edit]
        Sets the display appearance of the model panel.  Possible values are wireframe,
        points, boundingBox, smoothShaded, flatShaded.  This flag may be used with the
        -interactive and -default flags.  Note that only wireframe, points, and
        boundingBoxare valid for the interactive mode.
    
    - displayFog : dfg               (bool)          [query,edit]
        For Scene mode, this determines if fog will be displayed in the Paint Effects
        panel when refreshing the scene. If fog is on, but this is off, fog will only be
        drawn on the strokes, not the rest of the scene.
    
    - displayImage : di              (int)           [query,edit]
        Set a particular image in the Editor Image Stack as the current Editor Image.
        Images are added to the Editor Image Stack using the si/saveImageflag.
    
    - displayLights : dsl            (unicode)       [query,edit]
        Sets the lighting for shaded mode.  Possible values are selected, active, all,
        default.
    
    - displayStyle : dst             (unicode)       [create,query,edit]
        Set the mode to display the image. Valid values are: colorto display the basic
        RGB imagemaskto display the mask channellumto display the luminance of the image
    
    - displayTextures : dtx          (bool)          [query,edit]
        Turns on or off display of textures in shaded mode
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - doubleBuffer : dbf             (bool)          [create,query,edit]
        Set the display in double buffer mode
    
    - drawAxis : da                  (bool)          [create,query,edit]
        Set or query whether the axis will be drawn.
    
    - drawContext : drc              (bool)          [query]
        Returns the name of the context.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - fastUpdate : fu                (int)           []
        Obsolete - do not use
    
    - fileName : fil                 (unicode)       [query,edit]
        This sets the file to which the canvas will be saved.
    
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
    
    - iconGrab : ig                  (bool)          [edit]
        This puts the Paint Effects panel into Grab Icon mode where the user is expected
        to drag out a section of the screen to be made into an icon.
    
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
    
    - menu : mn                      (unicode)       [create]
        Sets the name of the script used to build a menu in the editor. The script takes
        the editor name as an argument.
    
    - nbImages : nim                 (bool)          [query]
        returns the number of images
    
    - newImage : ni                  (int, int, float, float, float) [query,edit]
        Starts a new image in edit mode, setting the resolution to the integer values
        (X,Y) and clearing the buffer to the floating point values (R,G,B). In Query
        mode, this returns the (X,Y) resolution of the current Image.
    
    - paintAll : pa                  (float)         [edit]
        Redraws the buffer in current refresh mode.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - redrawLast : rl                (bool)          [edit]
        Redraws the last stroke again. Useful when it's brush has just changed. This
        feature does a fast undo and redraws the stroke again.
    
    - refresh : ref                  (bool)          [edit]
        requests a refresh of the current Editor Image.
    
    - refreshMode : rmd              (int)           [query,edit]
        Sets the refresh mode to the specified value. 0 - Do not draw strokes on
        refresh, 1 - Redraw strokes in wireframe mode, 2 - Redraw strokes in final
        rendered mode.
    
    - removeAllImages : ra           (bool)          [edit]
        remove all the Editor Images from the Editor Image Stack
    
    - removeImage : ri               (bool)          [edit]
        remove the current Editor Image from the Editor Image Stack
    
    - rollImage : rig                (float, float)  [edit]
        In Canvas mode, this rolls the image by the floating point values (X,Y). X and Y
        are between 0 (no roll) and 1 (full roll). A value of .5 rolls the image 50%
        (ie. the border moves to the center of the screen.
    
    - saveAlpha : sa                 (bool)          [query,edit]
        For Canvas mode, this determines if the alpha will be saved when storing the
        canvas to a disk file.
    
    - saveBumpmap : sbm              (unicode)       [query,edit]
        Saves the current buffer as a bump map to the specified file.
    
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
    
    - singleBuffer : sbf             (bool)          [create,query,edit]
        Set the display in single buffer mode
    
    - snapShot : snp                 (bool)          [edit]
        Takes a snapshot of the current camera view.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - swap : swp                     (int)           []
        Obsolete - do not use
    
    - tileSize : ts                  (int)           [edit]
        Sets the size of the tile for the hardware texture redraw of the display buffer.
    
    - unParent : up                  (bool)          [create,edit]
        Specifies that the editor should be removed from its layout. This cannot be used
        in query mode.
    
    - undoCache : uc                 (bool)          [edit]
        By default the last image is cached for undo. If this is set false, then undoing
        will be disabled in canvas mode and undo in scene mode will force a full
        refresh. Less memory will be used if this is set false before the first clear or
        refresh of the current scene.
    
    - unlockMainConnection : ulk     (bool)          [create,edit]
        Unlocks the mainConnection, effectively restoring the original mainConnection
        (if it is still available), and dynamic updates.
    
    - updateMainConnection : upd     (bool)          [create,edit]
        Causes a locked mainConnection to be updated from the orginal mainConnection,
        but preserves the lock state.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - wrap : wr                      (bool, bool)    [query,edit]
        For Canvas mode, should the buffer wrap in U, and V (respectively) when
        painting.
    
    - writeImage : wi                (unicode)       [edit]
        write the current Editor Image to disk
    
    - zoom : zm                      (float)         [query,edit]
        Zooms the Canvas image by the specified value.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.dynPaintEditor`
    """
    pass
