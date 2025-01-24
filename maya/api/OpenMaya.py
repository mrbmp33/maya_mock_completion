"""
# Copyright 2012 Autodesk, Inc. All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk
# license agreement provided at the time of installation or download,
# or which otherwise accompanies this software in either electronic
# or hard copy form.
"""
import random
import string
import uuid
import weakref
import enum
import math
from typing import Optional, Iterable, Union, Tuple
import maya.mmc_hierarchy as hierarchy
import maya.attribute_properties as attribute_properties
from maya.node_types_literals import NODE_TYPES


def _get_attribute_id(attribute_full_name: str) -> uuid.UUID:
    """Attribute fullname = node_name.attribute_name"""
    return uuid.uuid5(uuid.NAMESPACE_DNS, attribute_full_name)

def _initialize_mplug(owner: 'MObject',
                     mplug: 'MPlug',
                     attribute: 'MObject',
                     mplug_id: uuid.UUID,
                     want_network_plug=False) -> 'MPlug':
    mplug._owner = owner
    mplug._uuid = mplug_id
    mplug._attribute = attribute
    mplug._network_plug = want_network_plug
    owner._cached_plugs[mplug_id] = mplug
    return mplug

def _initialize_attribute(attribute) -> 'MObject':
    if not attribute._alive:
        attribute._init_attribute_fields()
    attribute._api_type = [MFn.kAttribute]
    return attribute

def _get_node_type(mobject: 'MObject') -> str:
    try:
        node_type = _TYPE_INT_TO_STR[mobject._typeId.id()]
        return node_type[1:] if node_type.startswith('k') else node_type
    except AttributeError:
        raise RuntimeError(f'{mobject} does not exist yet. Please "create" it first.')

def _get_attribute_properties(node_type, attr_name) -> Tuple[dict, str, str]:
    properties = attribute_properties.ATTRIBUTES_PROPERTIES.get(node_type, {}).get(attr_name)
    if attr_name in attribute_properties.ATTRIBUTES_SHORT_NAMES_MAP:
        short_name = attr_name
        long_name = attribute_properties.ATTRIBUTES_SHORT_NAMES_MAP[short_name]
        properties = attribute_properties.ATTRIBUTES_PROPERTIES[node_type].get(long_name)
        if not properties:
            raise KeyError(f'Node Type: <{node_type}> does not have attribute <{long_name}>')
    else:
        long_name = attr_name
        short_name = properties['short_name'] if properties else attr_name
    return properties, long_name, short_name


class MColor(object):
    """
    Manipulate color data.
    """

    def __add__(*args, **kwargs):
        args.y_ = """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __div__(*args, **kwargs):
        """
        x.__div__(y) <==> x/y
        """
        pass

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __idiv__(*args, **kwargs):
        """
        x.__idiv__(y) <==> x/=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __radd__(*args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __rdiv__(*args, **kwargs):
        """
        x.__rdiv__(y) <==> y/x
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def getColor(*args, **kwargs):
        """
        Returns a list containing the color's components, in the specified color model.
        """
        pass

    def setColor(*args, **kwargs):
        """
        Sets the color's components and color model.
        """
        pass

    a = None

    b = None

    g = None

    kByte = 1

    kCMY = 2

    kCMYK = 3

    kFloat = 0

    kHSV = 1

    kOpaqueBlack = None

    kRGB = 0

    kShort = 2

    r = None


class MNodeClass(object):
    """
    A class for performing node class-level operations in the dependency graph.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def addExtensionAttribute(*args, **kwargs):
        """
        Adds an extension attribute to the node class. An extension attribute is a class-level attribute which has been added dynamically to a node class. Because it is added at the class level, all nodes of that class will have the given attribute, and will only store the attribute's value if it differs from the default. Returns the type of the object at the end of the path.
        """
        pass

    def attribute(*args, **kwargs):
        """
        If passed an int: Returns the node class's i'th attribute. Raises IndexError if index is out of bounds.  If passed a string, Returns the node class's attribute having the given name. Returns MObject.kNullObj if the class does not have an attribute with that name.
        """
        pass

    def getAttributes(*args, **kwargs):
        """
        Returns an MObjectArray array containing all of the node class's attributes.
        """
        pass

    def hasAttribute(*args, **kwargs):
        """
        Returns True if the node class has an attribute of the given name, False otherwise.
        """
        pass

    def removeExtensionAttribute(*args, **kwargs):
        """
        Removes an extension attribute from the node class. Raises ValueError if attr is not an extension attribute of this node class.
        """
        pass

    def removeExtensionAttributeIfUnset(*args, **kwargs):
        """
        Removes an extension attribute from the node class, but only if there are no nodes in the graph with non-default values for this attribute. Returns True if the attribute was removed, False otherwise. Raises ValueError if attr is not an extension attribute of this node class.
        """
        pass

    attributeCount = None

    classification = None

    pluginName = None

    typeId = None

    typeName = None


class MItMeshFaceVertex(object):
    """
    An iterator for traversing a mesh's face vertices.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def currentItem(*args, **kwargs):
        """
        currentItem() -> MObject

        Returns the current faceVertex as a double-indexed component.
        """
        pass

    def faceId(*args, **kwargs):
        """
        faceId() -> int

        Returns the current face index.
        """
        pass

    def faceVertexId(*args, **kwargs):
        """
        faceVertexId() -> int

        Returns the relative index of the vertex within the current face. This
        index together with the faceId can be used for a fast access to get
        various info stored per vertex (normals, uvs, colors).
        """
        pass

    def geomChanged(*args, **kwargs):
        """
        geomChanged() -> self

        Resets the geom pointer in the MItMeshFaceVertex. If you're using
        MFnMesh to update Normals or Color per vertex while iterating, you
        must call geomChanged on the iterator immediately after the MFnMesh
        call to make sure that your geometry is up to date. A crash may result
        if this method is not called. A similar approach must be taken for
        updating upstream vertex tweaks with an MPlug. After the update, call
        this method.
        """
        pass

    def getBinormal(*args, **kwargs):
        """
        getBinormal(space=MSpace.kObject, uvSet='') -> MVector

        Returns the face vertex binormal associated with the UV set.
        """
        pass

    def getColor(*args, **kwargs):
        """
        getColor(colorSetName='') -> MColor

        Returns a color of the current face vertex.
        """
        pass

    def getColorIndex(*args, **kwargs):
        """
        getColorIndex(colorSetName='') -> int

        Return a color index of the current face vertex.
        """
        pass

    def getNormal(*args, **kwargs):
        """
        getNormal(space=MSpace.kObject) -> MVector

        Returns the face vertex normal.
        """
        pass

    def getTangent(*args, **kwargs):
        """
        getTangent(space=MSpace.kObject, uvSet='') -> MVector

        Returns the face vertex tangent associated with the given UV set. The
        tangent is defined as the surface tangent of the polygon running in
        the U direction.
        """
        pass

    def getUV(*args, **kwargs):
        """
        getUV(uvSet='') -> (float, float)

        Returns the texture coordinate for the current face vertex.
        """
        pass

    def getUVIndex(*args, **kwargs):
        """
        getUVIndex(uvSet='') -> int

        Returns the index of the texture coordinate for the current face
        vertex. This index refers to an element of the mesh's texture
        coordinate array as returned by MFnMesh::getUVs().
        """
        pass

    def hasColor(*args, **kwargs):
        """
        hasColor() -> bool

        Returns whether the current face vertex has a color-per-vertex set.
        """
        pass

    def hasUVs(*args, **kwargs):
        """
        hasUVs(uvSet='') -> bool

        Returns whether the current face vertex has UVs mapped in the given
        set.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Indicates if all of the face vertices have been traversed.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advances to the next face vertex in the iteration.
        """
        pass

    def normalId(*args, **kwargs):
        """
        normalId() -> int

        Returns the normal index for the specified vertex. This index refers
        to an element in the normal array returned by MFnMesh::getNormals().
        These normals are per-face per-vertex normals.
        """
        pass

    def position(*args, **kwargs):
        """
        position(space=MSpace.kObject) -> MPoint

        Returns the position of the current face vertex.
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(mesh) -> self
        reset(mesh, component=None) -> self

        Reset the iterator to the first face vertex of the mesh.

        Reset the iterator to the first face vertex of the specified mesh.

        * mesh (MObject) - The mesh for the iteration

        Reset the iterator with the given mesh and component.
        If component is None then the iteration will be for all face vertices in the mesh.

        * mesh (MDagPath) - The mesh to iterate over
        * component (MObject) - The faces of the mesh to iterate over
        """
        pass

    def setIndex(*args, **kwargs):
        """
        setIndex(faceId, faceVertexId) -> (oldFaceId, oldFaceVertexId)

        Sets the index of the current face vertex to be accessed. The current
        face vertex will no longer be in sync with any previous iteration.

        Returns the indices of the old face and vertex.


        * faceId (int) - Index of desired face to access.
        * faceVertexId (int) - Face-relative index of desired vertex to access.
        * oldFaceId (int) - Index of the face which was current before the change.
        * oldFaceVertexId (int) - Face-relative index of the vertex which was current before the change.
        """
        pass

    def tangentId(*args, **kwargs):
        """
        tangentId() -> int

        Returns the tangent index for the current face vertex. This index
        refers to an element in the array returned by MFnMesh::getTangents.
        These tangents are per-face per-vertex.
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        Tells Maya that mesh has been changed and needs to redraw itself.
        """
        pass

    def vertexId(*args, **kwargs):
        """
        vertexId() -> int

        Returns the global (as opposed to face-relative) index of the
        current vertex.
        """
        pass


class MObjectHandle(object):
    """
    Generic Class for validating MObjects.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(self, mobject: "MObject"):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._mobject = mobject

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def assign(*args, **kwargs):
        """
        assign(source) -> self

        Assigns this MObjectHandle to an instance of another MObjectHandle, or to a MObject instance.

        * source (MObject/MObjectHandle) - other instance to assign from.
        """
        pass

    def hashCode(self, *args, **kwargs):
        """
        hashCode() -> int

        Returns a hash code for the internal Maya object referenced by the MObject within this MObjectHandle. If the MObject is null or no longer alive then 0 will be returned, otherwise the hash code is guaranteed to be non-zero
        """
        return hash(id(self._mobject._name))

    def isAlive(self) -> bool:
        """
        isAlive() -> bool

        Returns the live state of the associated MObject. An object can still be 'alive' but not 'valid' (eg. a deleted object that resides in the undo queue).
        """
        return getattr(self._mobject, '_isAlive', True)

    def isValid(self) -> bool:
        """
        isValid() -> bool

        Returns the validity of the associated MObject.
        """
        return getattr(self._mobject, '_isValid', True)

    def object(self):
        """
        object() -> MObject

        Returns the MObject associated with this handle. The returned MObject will be MObject.kNullObj if the object is invalid.
        """
        return self._mobject


class MInt64Array(object):
    """
    Array of MInt64 values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MColorArray(object):
    """
    Array of MColor values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MAttributeIndex(object):
    """
    The index information for an attribute specification.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source index.

        * source (MAttributeIndex) - The source index to copy from
        """
        pass

    def getLower(*args, **kwargs):
        """
        getLower() -> int/float

        Returns the lower bound of the index.
        """
        pass

    def getUpper(*args, **kwargs):
        """
        getUpper() -> int/float

        Returns the upper bound of the index.
        """
        pass

    def getValue(*args, **kwargs):
        """
        getValue() -> int/float

        Returns the current value of the index.
        Raises an exception if the index is a range.
        """
        pass

    def hasLowerBound(*args, **kwargs):
        """
        hasLowerBound() -> bool

        Returns True if a lower bound is specified.
        """
        pass

    def hasRange(*args, **kwargs):
        """
        hasRange() -> bool

        Returns True if a range was specified.
        """
        pass

    def hasUpperBound(*args, **kwargs):
        """
        hasUpperBound() -> bool

        Returns True if an upper bound is specified.
        """
        pass

    def hasValidRange(*args, **kwargs):
        """
        hasValidRange() -> bool

        Returns True if upper bound is greater than lower bound.
        """
        pass

    def isBounded(*args, **kwargs):
        """
        isBounded() -> bool

        Returns True if the index is bounded.
        """
        pass

    def setLower(*args, **kwargs):
        """
        setLower(value) -> self

        Sets the lower bound of the index.
        """
        pass

    def setType(*args, **kwargs):
        """
        setType(type) -> self

        Sets the type of attribute index.
        See type() for a list of valid index types.

        * type (int) - the index type to set
        """
        pass

    def setUpper(*args, **kwargs):
        """
        setUpper(value) -> self

        Sets the upper bound of the index.
        """
        pass

    def setValue(*args, **kwargs):
        """
        setValue(value) -> self

        Sets the value of the index.

        Remark: calling this method with an integer value will change its type to kInteger, and subsequently calling with a float value will change it to kFloat.
        """
        pass

    def type(*args, **kwargs):
        """
        type() -> int

        Returns the type of attribute index.

        Valid index types:
          kInteger      Integer index (e.g. mesh.cp[5])
          kFloat                Floating-poing index (e.g. curve.u[1.3])
        """
        pass

    kFloat = 1

    kInteger = 0


class MTypeId(object):
    """
    Stores a Maya object type identifier.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(self, value: int = 0, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._value = value

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __repr__(self):
        """
        x.__repr__() <==> repr(x)
        """
        return "{class_name}({value}) <{as_str}>".format(
            class_name=self.__class__.__name__,
            value=self._value,
            as_str=_TYPE_INT_TO_STR.get(self._value, 'kInvalid')
        )

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def id(self) -> int:
        """
        Returns the type id as a long.
        """
        return self._value


class MMeshSmoothOptions(object):
    """
    Options for control of smooth mesh generation.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    boundaryRule = None

    divisions = None

    kCatmullClark = 0

    kCreaseAll = 1

    kCreaseEdge = 2

    kInvalid = -1

    kInvalidSubdivision = -1

    kLast = 3

    kLastSubdivision = 4

    kLegacy = 0

    kOpenSubdivCatmullClarkAdaptive = 3

    kOpenSubdivCatmullClarkUniform = 2

    keepBorderEdge = None

    keepHardEdge = None

    propEdgeHardness = None

    smoothUVs = None

    smoothness = None

    subdivisionType = None


class MItSelectionList(object):
    """
    Class for iterating over the items in an MSelection list.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def getComponent(*args, **kwargs):
        """
        getComponent() -> (MDagPath, MObject)

        This method retrieves the dag path and the component of the current selection item.
        """
        pass

    def getDagPath(*args, **kwargs):
        """
        getDagPath() -> MDagPath

        This method retrieves the dag path of the current selection item.
        """
        pass

    def getDependNode(*args, **kwargs):
        """
        getDependNode() -> MObject

        This method retrieves the dependency node of the current selection itemRaises kFailure if there is no dependency node associated with the current item
        """
        pass

    def getPlug(*args, **kwargs):
        """
        getPlug() -> MPlug

        This method retrieves the plug of the current selection item.
        """
        pass

    def getStrings(*args, **kwargs):
        """
        getStrings() -> list of strings

        Get the string representation of the current item in the selection list.
        It is possible that it will require more than one string to represent the item (the item may contain groups of CVs for example)
        """
        pass

    def hasComponents(*args, **kwargs):
        """
        hasComponents() -> bool

        Returns whether or not the current selection item has components.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Specifies whether or not there is anything more to iterator over.
        """
        pass

    def itemType(*args, **kwargs):
        """
        itemType() -> int

        Returns the current selection item type.

          kDagSelectionItem    selection item is in the DAG
          kAnimSelectionItem   selection item is a keyset
          kDNselectionItem     selection item is a dependency node
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advance to the next item. If components are selected then advance to next component.

        If a filter is specified then the next item will be one that matches the filter.
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self

        Reset the iterator.
        If a filter has been specified then the current item will be the first selected item that matches the filter.
        """
        pass

    def setFilter(*args, **kwargs):
        """
        setFilter(filter) -> self

        Apply a filter to the iteration.
        Selection items not matching the filter type will be excluded from the iteration.
        """
        pass

    kAnimSelectionItem = 1

    kDNselectionItem = 2

    kDagSelectionItem = 0

    kPlugSelectionItem = 3

    kUnknownItem = -1


class MEulerRotation(object):
    """
    X, Y and Z rotations, applied in a specified order.
    """

    kIdentity = (0.0, 0.0, 0.0)
    kTolerance = 1e-10

    # Rotation orders
    kXYZ = 0
    kXZY = 3
    kYXZ = 4
    kYZX = 1
    kZXY = 2
    kZYX = 5

    def __init__(self, x=0.0, y=0.0, z=0.0, order=kXYZ):
        """
        Initializes the rotation with given x, y, z angles and rotation order.
        """
        self.x = x
        self.y = y
        self.z = z
        self.order = order

    def __add__(self, other):
        """
        Adds another rotation to this one.
        """
        if not isinstance(other, MEulerRotation):
            return NotImplemented
        return MEulerRotation(self.x + other.x, self.y + other.y, self.z + other.z, self.order)

    def __iadd__(self, other):
        """
        In-place addition.
        """
        if not isinstance(other, MEulerRotation):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        """
        Subtracts another rotation from this one.
        """
        if not isinstance(other, MEulerRotation):
            return NotImplemented
        return MEulerRotation(self.x - other.x, self.y - other.y, self.z - other.z, self.order)

    def __isub__(self, other):
        """
        In-place subtraction.
        """
        if not isinstance(other, MEulerRotation):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, scalar):
        """
        Scales the rotation by a scalar.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return MEulerRotation(self.x * scalar, self.y * scalar, self.z * scalar, self.order)

    def __imul__(self, scalar):
        """
        In-place scaling.
        """
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def __eq__(self, other):
        """
        Checks equality of two rotations within a tolerance.
        """
        if not isinstance(other, MEulerRotation):
            return NotImplemented
        return (math.isclose(self.x, other.x, abs_tol=self.kTolerance) and
                math.isclose(self.y, other.y, abs_tol=self.kTolerance) and
                math.isclose(self.z, other.z, abs_tol=self.kTolerance))

    def __iter__(self):
        """
        Iterates over x, y, z components.
        """
        yield self.x
        yield self.y
        yield self.z

    def __len__(self):
        """
        Returns the length of the rotation (always 3 components).
        """
        return 3

    def __getitem__(self, index):
        """
        Index-based access to components.
        """
        return (self.x, self.y, self.z)[index]

    def __setitem__(self, index, value):
        """
        Index-based setting of components.
        """
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range for MEulerRotation")

    def __repr__(self):
        """
        Returns a string representation of the rotation.
        """
        return f"MEulerRotation(x={self.x}, y={self.y}, z={self.z}, order={self.order})"

    def asVector(self):
        """
        Returns the X, Y, Z components as a vector.
        """
        return (self.x, self.y, self.z)

    def asMatrix(self):
        """
        Returns the rotation as an equivalent 3x3 matrix.
        """
        # Placeholder: Actual matrix computation should depend on the rotation order.
        return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def asQuaternion(self):
        """
        Returns the rotation as an equivalent quaternion.
        """
        # Placeholder: Actual quaternion computation is needed here.
        return (0, 0, 0, 1)

    def bound(self):
        """
        Returns a new MEulerRotation with components bound within +/- PI.
        """
        def bound_angle(angle):
            while angle > math.pi:
                angle -= 2 * math.pi
            while angle < -math.pi:
                angle += 2 * math.pi
            return angle

        return MEulerRotation(bound_angle(self.x), bound_angle(self.y), bound_angle(self.z), self.order)

    def boundIt(self):
        """
        In-place bounding of components within +/- PI.
        """
        def bound_angle(angle):
            while angle > math.pi:
                angle -= 2 * math.pi
            while angle < -math.pi:
                angle += 2 * math.pi
            return angle

        self.x = bound_angle(self.x)
        self.y = bound_angle(self.y)
        self.z = bound_angle(self.z)

    def isZero(self):
        """
        Returns true if all components are within the tolerance of zero.
        """
        return (math.isclose(self.x, 0.0, abs_tol=self.kTolerance) and
                math.isclose(self.y, 0.0, abs_tol=self.kTolerance) and
                math.isclose(self.z, 0.0, abs_tol=self.kTolerance))

    @staticmethod
    def computeBound(x, y, z):
        """
        Returns equivalent rotations for the given x, y, z, bound within +/- PI.
        """
        def bound_angle(angle):
            while angle > math.pi:
                angle -= 2 * math.pi
            while angle < -math.pi:
                angle += 2 * math.pi
            return angle

        return (bound_angle(x), bound_angle(y), bound_angle(z))


    @staticmethod
    def computeBound(*args, **kwargs):
        """
        Returns an equivalent rotation with each rotation component bound within +/- PI.
        """
        pass

    @staticmethod
    def computeClosestCut(*args, **kwargs):
        """
        Returns the rotation which is full spin multiples of the src and comes closest to target.
        """
        pass

    @staticmethod
    def computeClosestSolution(*args, **kwargs):
        """
        Returns the equivalent rotation which comes closest to a target.
        """
        pass

    @staticmethod
    def decompose(*args, **kwargs):
        """
        Extracts a rotation from a matrix.
        """
        pass

    x = None

    y = None

    z = None


class MAttributeSpec(object):
    """
    Class that encapsulates component/attribute information for generating selection items.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source specification.

        * source (MAttributeSpec) - The source specification to copy from
        """
        pass

    dimensions = None

    name = None


class MDGModifier(object):
    """
    Used to change the structure of the dependency graph.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._queue = []
        self._done = False

    def addAttribute(*args, **kwargs):
        """
        addAttribute(MObject node, MObject attribute) -> self

        Adds an operation to the modifier to add a new dynamic attribute to the
        given dependency node. If the attribute is a compound its children will
        be added as well, so only the parent needs to be added using this method.
        """
        pass

    def addExtensionAttribute(*args, **kwargs):
        """
        addExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

        Adds an operation to the modifier to add a new extension attribute to
        the given node class. If the attribute is a compound its children will be
        added as well, so only the parent needs to be added using this method.
        """
        pass

    def commandToExecute(*args, **kwargs):
        """
        commandToExecute(command) -> self

        Adds an operation to the modifier to execute a MEL command. The command
        should be fully undoable otherwise unexpected results may occur. If
        the command contains no undoable portions whatsoever, the call to
        doIt() may fail, but only after executing the command. It is best to
        use multiple commandToExecute() calls rather than batching multiple
        commands into a single call to commandToExecute(). They will still be
        undone together, as a single undo action by the user, but Maya will
        better be able to recover if one of the commands fails.
        """
        pass

    def connect(*args, **kwargs):
        """
        connect(MPlug source, MPlug dest) -> self
        connect(MObject sourceNode, MObject sourceAttr,
                MObject destNode,   MObject destAttr) -> self

        Adds an operation to the modifier that connects two plugs in the
        dependency graph. It is the user's responsibility to ensure that the
        source and destination attributes are of compatible types. For instance,
        if the source attribute is a nurbs surface then the destination must
        also be a nurbs surface.
        Plugs can either be specified with node and attribute MObjects or with
        MPlugs.
        """
        pass

    def createNode(self, type_id: Union[str, NODE_TYPES, 'MTypeId']) -> 'MObject':
        """
        createNode(typeName) -> MObject
        createNode(MTypeId typeId) -> MObject

        Adds an operation to the modifier to create a node of the given type.
        The new node is created and returned but will not be added to the
        Dependency Graph until the modifier's doIt() method is called. Raises
        TypeError if the named node type does not exist or if it is a DAG node
        type.
        """
        mobject = MObject()
        mobject._alive = True
        # If given a string as input, get the matching MTypeId
        if isinstance(type_id, str):
            # noinspection PyProtectedMember
            mobject._typeId = _TYPE_STR_TO_ID[type_id]
        else:
            mobject._typeId = type_id

        self._queue.append(('create', mobject))

        return mobject

    def deleteNode(self, node: "MObject"):
        """
        deleteNode(MObject node) -> self

        Adds an operation to the modifer which deletes the specified node from
        the Dependency Graph. If the modifier already contains other operations
        on the same node (e.g. a disconnect) then they should be committed by
        calling the modifier's doIt() before the deleteNode operation is added.
        """
        self._queue.append(('delete', node))
        return self

    def disconnect(*args, **kwargs):
        """
        disconnect(MPlug source, MPlug dest) -> self
        disconnect(MObject sourceNode, MObject sourceAttr,
                   MObject destNode,   MObject destAttr) -> self

        Adds an operation to the modifier that breaks a connection between two
        plugs in the dependency graph.
        Plugs can either be specified with node and attribute MObjects or with
        MPlugs.
        """
        pass

    def doIt(self):
        """
        doIt() -> self

        Executes the modifier's operations. If doIt() is called multiple times
        in a row, without any intervening calls to undoIt(), then only the
        operations which were added since the previous doIt() call will be
        executed. If undoIt() has been called then the next call to doIt() will
        do all operations.
        """

        for action in self._queue:
            if action[0] == 'create':
                mobject: 'MObject' = action[1]
                hierarchy.register(mobject)
            elif action[0] == 'delete':
                mobject: 'MObject' = action[1]
                if mobject._parent:
                    mobject._parent._children.remove(mobject)
                hierarchy.deregister(mobject)
            elif action[0] == 'rename':
                mobject: 'MObject' = action[1]
                mobject._name = action[2]
            elif action[0] == 'reparent':
                mobject: 'MObject' = action[1]
                mobject._parent._children.remove(mobject)
                mobject._parent = action[2]
                mobject._parent._children.add(mobject)

        self._done = True
        return self

    def linkExtensionAttributeToPlugin(*args, **kwargs):
        """
        linkExtensionAttributeToPlugin(MObject plugin, MObject attribute) -> self

        The plugin can call this method to indicate that the extension attribute
        defines part of the plugin, regardless of the node type to which it
        attaches itself. This requirement is used when the plugin is checked to
        see if it is in use or if is able to be unloaded or if it is required as
        part of a stored file. For compound attributes only the topmost parent
        attribute may be passed in and all of its children will be included,
        recursively. Thus it's not possible to link a child attribute to a
        plugin by itself. Note that the link is established immediately and is
        not affected by the modifier's doIt() or undoIt() methods.
        """
        pass

    def newPlugValue(*args, **kwargs):
        """
        newPlugValue(MPlug plug, MObject value) -> self

        Adds an operation to the modifier to set the value of a plug, where
        value is an MObject data wrapper, such as created by the various
        MFn*Data classes.
        """
        pass

    def newPlugValueBool(*args, **kwargs):
        """
        newPlugValueBool(MPlug plug, bool value) -> self

        Adds an operation to the modifier to set a value onto a bool plug.
        """
        pass

    def newPlugValueChar(*args, **kwargs):
        """
        newPlugValueChar(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto a char (single
        byte signed integer) plug.
        """
        pass

    def newPlugValueDouble(*args, **kwargs):
        """
        newPlugValueDouble(MPlug plug, float value) -> self

        Adds an operation to the modifier to set a value onto a double-precision
        float plug.
        """
        pass

    def newPlugValueFloat(*args, **kwargs):
        """
        newPlugValueFloat(MPlug plug, float value) -> self

        Adds an operation to the modifier to set a value onto a single-precision
        float plug.
        """
        pass

    def newPlugValueInt(*args, **kwargs):
        """
        newPlugValueInt(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto an int plug.
        """
        pass

    def newPlugValueMAngle(*args, **kwargs):
        """
        newPlugValueMAngle(MPlug plug, MAngle value) -> self

        Adds an operation to the modifier to set a value onto an angle plug.
        """
        pass

    def newPlugValueMDistance(*args, **kwargs):
        """
        newPlugValueMDistance(MPlug plug, MDistance value) -> self

        Adds an operation to the modifier to set a value onto a distance plug.
        """
        pass

    def newPlugValueMTime(*args, **kwargs):
        """
        newPlugValueMTime(MPlug plug, MTime value) -> self

        Adds an operation to the modifier to set a value onto a time plug.
        """
        pass

    def newPlugValueShort(*args, **kwargs):
        """
        newPlugValueShort(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto a short
        integer plug.
        """
        pass

    def newPlugValueString(*args, **kwargs):
        """
        newPlugValueString(MPlug plug, string value) -> self

        Adds an operation to the modifier to set a value onto a string plug.
        """
        pass

    def pythonCommandToExecute(*args, **kwargs):
        """
        pythonCommandToExecute(callable) -> selfpythonCommandToExecute(commandString) -> self

        Adds an operation to the modifier to execute a Python command, which
        can be passed as either a Python callable or a string containing the
        text of the Python code to be executed. The command should be fully
        undoable otherwise unexpected results may occur. If the command
        contains no undoable portions whatsoever, the call to doIt() may fail,
        but only after executing the command. It is best to use multiple calls
        rather than batching multiple commands into a single call to
        pythonCommandToExecute(). They will still be undone together, as a
        single undo action by the user, but Maya will better be able to
        recover if one of the commands fails.
        """
        pass

    def removeAttribute(*args, **kwargs):
        """
        removeAttribute(MObject node, MObject attribute) -> self

        Adds an operation to the modifier to remove a dynamic attribute from the
        given dependency node. If the attribute is a compound its children will
        be removed as well, so only the parent needs to be removed using this
        method. The attribute MObject passed in will be set to kNullObj. There
        should be no function sets attached to the attribute at the time of the
        call as their behaviour may become unpredictable.
        """
        pass

    def removeExtensionAttribute(*args, **kwargs):
        """
        removeExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

        Adds an operation to the modifier to remove an extension attribute from
        the given node class. If the attribute is a compound its children will
        be removed as well, so only the parent needs to be removed using this
        method. The attribute MObject passed in will be set to kNullObj. There
        should be no function sets attached to the attribute at the time of the
        call as their behaviour may become unpredictable.
        """
        pass

    def removeExtensionAttributeIfUnset(*args, **kwargs):
        """
        removeExtensionAttributeIfUnset(MNodeClass nodeClass,
                                        MObject attribute) -> self

        Adds an operation to the modifier to remove an extension attribute from
        the given node class, but only if there are no nodes in the graph with
        non-default values for this attribute. If the attribute is a compound
        its children will be removed as well, so only the parent needs to be
        removed using this method. The attribute MObject passed in will be set
        to kNullObj. There should be no function sets attached to the attribute
        at the time of the call as their behaviour may become unpredictable.
        """
        pass

    def removeMultiInstance(*args, **kwargs):
        """
        removeMultiInstance(MPlug plug, bool breakConnections) -> self

        Adds an operation to the modifier to remove an element of a multi (array) plug.
        """
        pass

    def renameAttribute(*args, **kwargs):
        """
        renameAttribute(MObject node, MObject attribute,
        string newShortName, string newShortName) -> self

        Adds an operation to the modifer that renames a dynamic attribute on the given dependency node.
        """
        pass

    def renameNode(self, node: "MObject", newName: str):
        """
        renameNode(MObject node, string newName) -> self

        Adds an operation to the modifer to rename a node.
        """
        self._queue.append(('rename', node, newName, node._name))
        return self

    def setNodeLockState(*args, **kwargs):
        """
        setNodeLockState(MObject node, bool newState) -> self

        Adds an operation to the modifier to set the lockState of a node.
        """
        pass

    def undoIt(self, *args, **kwargs):
        """
        undoIt() -> self

        Undoes all of the operations that have been given to this modifier. It
        is only valid to call this method after the doIt() method has been
        called.
        """
        if not self._done:
            raise RuntimeError('Must use "doIt" before undoing.')

        for action in self._queue:
            if action[0] == 'create':
                mobject: 'MObject' = action[1]
                mobject._alive = False
                mobject._parent._children.remove(mobject)
                hierarchy.deregister(mobject)
            elif action[0] == 'delete':
                mobject: 'MObject' = action[1]
                mobject._alive = True
                hierarchy.register(mobject)
            elif action[0] == 'rename':
                mobject: 'MObject' = action[1]
                mobject._name = action[3]
            elif action[0] == 'reparent':
                mobject: 'MObject' = action[1]
                mobject._parent = action[3]

        self._done = False
        return self

    def unlinkExtensionAttributeFromPlugin(*args, **kwargs):
        """
        unlinkExtensionAttributeFromPlugin(MObject plugin,
                                           MObject attribute) -> self

        The plugin can call this method to indicate that it no longer requires
        an extension attribute for its operation. This requirement is used when
        the plugin is checked to see if it is in use or if is able to be unloaded
        or if it is required as part of a stored file. For compound attributes
        only the topmost parent attribute may be passed in and all of its
        children will be unlinked, recursively. Thus it's not possible to unlink
        a child attribute from a plugin by itself. Note that the link is broken
        immediately and is not affected by the modifier's doIt() or undoIt()
        methods.
        """
        pass


class MUint64Array(object):
    """
    Array of MUint64 values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MImage(object):
    """
    Manipulate color data.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        create(width, height, channels=4, type=kByte) -> self

        Create a new MImage object. Allocates memory for an RGBA array of pixels
        of the given size. If an object was already in memory, it is released first.

        * width (unsigned int) - the desired image's width in pixels.
        * height (unsigned int) - the desired image's height in pixels.
        * channels (unsigned int) - the desired number of channels per pixel.
        * type (int) - the desired pixel format (kByte or kFloat, see MImage.pixelType() description for details.)
        """
        pass

    def depth(*args, **kwargs):
        """
        depth() -> int

        Get the color depth (in bytes) of the currently opened image.
        """
        pass

    def depthMap(*args, **kwargs):
        """
        depthMap() -> long

        Returns a long containing a C++ 'float' pointer which points to the depth data.
        """
        pass

    def filter(*args, **kwargs):
        """
        filter(sourceFormat, targetFormat, scale=1.0, offset=1.0) -> self

        Modify the content of the image by applying a filter.
        The dimension of the image remains the same; only the RGBA components get affected.

        * sourceFormat (MImageFilterFormat) - the format of the source image.
        * targetFormat (MImageFilterFormat) - the format of the resulting image.* scale (float) - vary depending on the source/target format.
        * offset (float) - vary depending on the source/target format.

        The scale argument for this filter can vary from -256.0 to 256.0, although typical values range from 1.0 to 10.0.
        The offset argument is currently ignored and should be left to the default value of 0.0.
        """
        pass

    def floatPixels(*args, **kwargs):
        """
        floatPixels() -> long

        Returns a long containing a C++ 'float' pointer which points to the pixel data.
        This data is uncompressed and tightly packed, of size (width * height * depth * sizeof( float)) bytes.
        """
        pass

    def getDepthMapRange(*args, **kwargs):
        """
        getDepthMapRange() -> [minValue, maxValue]

        Compute the minimum and maximum depth values (range) for any stored depth buffer.
        """
        pass

    def getDepthMapSize(*args, **kwargs):
        """
        getDepthMapSize() -> [width, height]

        Returns the size of the depth map buffer.
        """
        pass

    def getSize(*args, **kwargs):
        """
        getSize() -> [width, height]

        Get the width and height of the currently opened image.
        """
        pass

    def haveDepth(*args, **kwargs):
        """
        haveDepth() -> bool

        Returns True if this instance of MImage contains a depth map.
        """
        pass

    def isRGBA(*args, **kwargs):
        """
        isRGBA() -> bool

        Query flag which indicates whether the pixel information is in RGBA sequence or BGRA sequence.
        If no pixel data exists, then False will be returned.
        """
        pass

    def pixelType(*args, **kwargs):
        """
        pixelType() -> int

        Get the current pixel format of the image:  kUnknown    Format not known or invalid.
          kByte       One byte per channel, ranging from 0 to 255.
          kFloat      One float per channel, ranging from 0.0 to 1.0.
        """
        pass

    def pixels(*args, **kwargs):
        """
        pixels() -> long

        Returns a long containing a C++ 'unsigned char' pointer which points to the pixel data.
        This data is uncompressed and tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.
        """
        pass

    def readDepthMap(*args, **kwargs):
        """
        readDepthMap(pathname) -> self

        Reads the depth map from the specified file and place the result into the depth map array of this MImage instance.
        """
        pass

    def readFromFile(*args, **kwargs):
        """
        readFromFile(pathname, type=kByte) -> self

        Attempt to identify and open the specified image file.

        * pathname (string) - the full path of the image file that should be opened.
        * type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type.
        """
        pass

    def readFromTextureNode(*args, **kwargs):
        """
        readFromTextureNode(fileTextureObject, type=kByte) -> self

        Attempt to read the content of the given file texture node.


        * fileTextureObject (MObject) - an object that refers to the file texture node that should be read.
        * type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type.
        """
        pass

    def release(*args, **kwargs):
        """
        release() -> self

        Release the current image. If there is no current image, the call is ignored.
        """
        pass

    def resize(*args, **kwargs):
        """
        resize(width, height, preserveAspectRatio=True) -> self

        Resize the currently opened image to the specified dimension, or to the closest
        width/height that is preserves the original aspect ratio.* width (unsigned int) - the desired image's width in pixels.
        * height (unsigned int) - the desired image's height in pixels.
        * preserveAspectRatio (bool) - specifies whether the aspect ratio should be preserved or not.
                 If this flag is set, the given width and height are interpreted as the maximum dimensions allowable.
        """
        pass

    def setDepthMap(*args, **kwargs):
        """
        setDepthMap(depth, width, heigth) -> self

        Specifies the depth map resolution and data.

        * depth (float*) - float buffer that contains depth values.
        * width (unsigned int) - the width of the depth buffer.
        * height (unsigned int) - the height of the depth buffer.

        * depth (MFloatArray) - float array that contains depth values.
        * width (unsigned int) - the width of the depth buffer.
        * height (unsigned int) - the height of the depth buffer.
        """
        pass

    def setFloatPixels(*args, **kwargs):
        """
        setFloatPixels(pixels, width, height, channels=4) -> self

        Copy the uncompressed pixels array passed in into the MImage.
        This array is tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

        * pixels (float*) - the variable containing a block of pixels.
        * width (unsigned int) - the variable that will be set to the image's width in pixels.
        * height (unsigned int) - the variable that will be set to the image's height in pixels.
        * channels (unsigned int) - the number of channels per pixel.
        """
        pass

    def setPixels(*args, **kwargs):
        """
        setPixels(pixels, width, height) -> self

        Copy the uncompressed pixels array passed in into the MImage.
        This array is tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

        * pixels (unsigned char*) - the variable containing a block of pixels.
        * width (unsigned int) - the variable that will be set to the image's width in pixels.
        * height (unsigned int) - the variable that will be set to the image's height in pixels.
        """
        pass

    def setRGBA(*args, **kwargs):
        """
        setRGBA(bool) -> self

        Sets a flag to indicate that pixel information is in RGBA sequence or BGRA sequence.
        Pixel data must have been allocated before this call is made.
        """
        pass

    def verticalFlip(*args, **kwargs):
        """
        verticalFlip() -> bool

        Flips the image vertically.
        """
        pass

    def writeToFile(*args, **kwargs):
        """
        writeToFile(pathname, outputFormat=iff) -> self

        Save the content of this image in a file. By default, the file is saved in IFF format.
        Optionally, the file can also be converted in a variety of image formats.
        """
        pass

    def writeToFileWithDepth(*args, **kwargs):
        """
        writeToFileWithDepth(pathname, outputFormat=iff, writeDepth=False) -> self

        Save the content of this image in a file. By default, the file is saved in IFF format.
        Optionally, the file can also be converted in a variety of image formats.
        If the writeDepth parameter is True then any depth information stored in MImage will be written to file.
        """
        pass

    @staticmethod
    def filterExists(*args, **kwargs):
        """
        filterExists(sourceFormat, targetFormat) -> bool

        Return whether or not a given source format can be directly converted to a given target format.

        * sourceFormat (MImageFilterFormat) - the format of the source image.
        * targetFormat (MImageFilterFormat) - the format of the resulting image.
        """
        pass

    kByte = 1

    kFloat = 2

    kHeightFieldBumpFormat = 1

    kNoFormat = 0

    kNormalMapBumpFormat = 2

    kUnknown = 0

    kUnknownFormat = 3


class MDataBlock(object):
    """
    Dependency node data block.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def context(*args, **kwargs):
        """
        context() -> MDGContext

        Returns a copy of the dependecy graph context for which this data block was created. The context is used to specify how a dependency node is going to be evaluated.
        """
        pass

    def inputArrayValue(*args, **kwargs):
        """
        inputArrayValue(plug) -> MArrayDataHandle
        inputArrayValue(attribute) -> MArrayDataHandle

        Gets an array handle to this data block for the given plug/attribute's data.  This is only valid if the given plug has array data.  The data represented by the handle will be valid.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned.  If the plug has not been set to a particular value, then the default value will be returned.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute whose data you wish to access
        """
        pass

    def inputValue(*args, **kwargs):
        """
        inputValue(plug) -> MDataHandle
        inputValue(attribute) -> MDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  The data represented by the handle is guaranteed to be valid for reading.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned. If the plug has not been set to a particular value, then the default value will be returned.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
        """
        pass

    def isClean(*args, **kwargs):
        """
        isClean(plug) -> bool
        isClean(attribute) -> bool

        Queries the dependency graph to see whether the given plug/attribute is clean.

        * plug (MPlug) - the plug that is to be query
         OR
        * attribute (MObject) - the attribute that is to be query.
        """
        pass

    def outputArrayValue(*args, **kwargs):
        """
        outputArrayValue(plug) -> MArrayDataHandle
        outputArrayValue(attribute) -> MArrayDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  No dependency graph evaluations will be done, and therefore the data is not guaranteed to be valid (i.e. it may be dirty).  Typically, this method is used to get the handle during compute in order to write output data to it.

        Another usage of this method is to access an input array attribute without evaluating any of its array elements. One can then use MArrayDataHandle.jumpToElement() to get to the particular element of interest, and evaluate its value using MArrayDataHandle.inputValue().

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute whose data you wish to access
        """
        pass

    def outputValue(*args, **kwargs):
        """
        outputValue(plug) -> MDataHandle
        outputValue(attribute) -> MDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  The data is not guaranteed to be valid.  No dependency graph evaluations will be done. Therefore, this handle should be used only for writing.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
        """
        pass

    def setClean(*args, **kwargs):
        """
        setClean(plug) -> self
        setClean(attribute) -> self

        Tells the dependency graph that the given plug/attribute has been updated and is now clean.  This should be called after the data in the plug has been recalculated from the inputs of the node.

        * plug (MPlug) - the plug that is to be marked clean
         OR
        * attribute (MObject) - the attribute that is to be marked clean
        """
        pass

    def setContext(*args, **kwargs):
        """
        setContext(ctx) -> self

        Set the dependency graph context for this data block. The context is used to specify how a dependency node is going to be evaluated, thus replacing the context for the given datablock. This does not modify the dirty state of the datablock so that they apply to the new context.

        This function should not be used for timed evaluation.

        * ctx (MDGContext) - the dependency graph context
        """
        pass


class MFloatArray(object):
    """
    Array of float values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MAttributeSpecArray(object):
    """
    Array of MAttributeSpec values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MDoubleArray(object):
    """
    Array of double values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MItDependencyNodes(object):
    """
    Dependency Node iterator.

    Use the dependency node iterator to traverse all the nodes in Maya's
    Dependency Graph.

    With filtering enabled, the iterator checks to see if the node is
    compatible with the type specified by the filter.  See MFn.Type for a
    list of all valid types.

    Since MObjects may be compatible with more than one type (nodes are
    organised in a hierarchy) the MObject.hasFn() method can be used to
    further check for compatible types.

    Any compatible Function Set can be attached to the retrieved object to
    query or or edit it.  Often you will want to use the dependency node
    function set (MFnDependencyNode), which is compatible with all
    dependency nodes, to perform queries on each node as the iterator
    traverses the Dependency Graph.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> Bool

        Indicates end of the iteration.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Moves to the next node matching the filter.  If the filter
        is set to kInvalid, this method advances to the next
        DG node without doing any filtering.
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(filterType = MFn.kInvalid) -> self
        reset(dagInfoObject) -> self


        Resets the iterator.


           dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid.
        """
        pass

    def thisNode(*args, **kwargs):
        """
        thisNode() -> MObject

        Retrieves the dependency node to which the iterator points.
        """
        pass


class MRichSelection(object):
    """
    A selection list supporting soft selection and symmetry.

    The rich selection is split into two halves: the 'normal' side,
    and an optional symmetric component. Components on both sides
    can include weight data which is used to specify both the amount
    of influence and the proximity to the centre of symmetry.

    In addition to the selected objects, the rich selection also
    includes information about the axis of symmetry so that
    operations can determine how to process any symmetric selection
    (e.g. reflect transformations).

    __init__()
    Initializes a new, empty MRichSelection object.

    __init__(MRichSelection other)
    Initializes a new MRichSelection object containing the same
    items as another rich selection.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def clear(*args, **kwargs):
        """
        clear() -> self


        Empties the rich selection.
        """
        pass

    def getRawSymmetryMatrix(*args, **kwargs):
        """
        getRawSymmetryMatrix() -> (MMatrix, space)

        Returns a tuple containing the raw symmetry matrix to use for the
        symmetric components of the rich selection, and the transformation
        space used by the matrix (see MSpace). The caller is responsible for
        handling any necessary transformation space conversions.
        """
        pass

    def getSelection(*args, **kwargs):
        """
        getSelection() -> MSelectionList

        Returns a copy of the non-symmetry component of the rich selection.
        """
        pass

    def getSymmetry(*args, **kwargs):
        """
        getSymmetry() -> MSelectionList

        Returns a copy of the symmetry component of the rich selection.
        """
        pass

    def getSymmetryMatrix(*args, **kwargs):
        """
        getSymmetryMatrix(MDagPath, space) -> MMatrix

        Returns the symmetry matrix to use for the symmetric component of
        the specified DAG object. The matrix will already be converted to
        use the specified transformation space (see MSpace).
        """
        pass

    def getSymmetryPlane(*args, **kwargs):
        """
        getSymmetryPlane(MDagPath, space) -> MPlane

        Returns the plane of symmetry, in the specified transformation space
        (see MSpace). This can be used to enforce seam weights in tools that
        support symmetry. Note that the direction of the plane carries no
        significance. Specifically, having a positive offset from the plane
        does not imply a point is part of the non-symmetric selection.
        """
        pass

    def setSelection(*args, **kwargs):
        """
        setSelection(MSelectionList) -> self

        Sets the non-symmetry component of the rich selection.
        """
        pass


class MEvaluationNode(object):
    """
    A class providing access to Evaluation Manager node information.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def datablock(*args, **kwargs):
        """
        Returns the datablock for this node.
        """
        pass

    def dependencyNode(*args, **kwargs):
        """
        Returns the dependency node this evaluation node represents.
        """
        pass

    def dirtyPlug(*args, **kwargs):
        """
        Returns the top-most plug for the specified attribute if the attribute has dirty plugs. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to access a networked plug which is going to be dirty and computed.
        """
        pass

    def dirtyPlugExists(*args, **kwargs):
        """
        Returns true if the specified attribute has a dirty plug. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to verify which plugs are going to be dirty and computed.
        """
        pass

    def iterator(*args, **kwargs):
        """
        Returns an iterator at the beginning of the dirty plug list.
        """
        pass


class MMatrix(object):
    """
    4x4 matrix with double-precision elements.
    """

    def __add__(self, *args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(self, *args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __eq__(self, *args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(self, *args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(self, *args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(self, *args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(self, *args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __isub__(self, *args, **kwargs):
        """
        x.__isub__(y) <==> x-=y
        """
        pass

    def __le__(self, *args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(self, *args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(self, *args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(self, *args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __radd__(self, *args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __repr__(self):
        """
        x.__repr__() <==> repr(x)
        """
        return self.__str__()

    def __rmul__(self, *args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(self, *args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __setitem__(self, *args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(self):
        """
        x.__str__() <==> str(x)
        """
        return ''

    def __sub__(self, *args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def adjoint(self, *args, **kwargs):
        """
        Returns a new matrix containing this matrix's adjoint.
        """
        pass

    def det3x3(self, *args, **kwargs):
        """
        Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix.
        """
        pass

    def det4x4(self, *args, **kwargs):
        """
        Returns this matrix's determinant.
        """
        pass

    def getElement(self, *args, **kwargs):
        """
        Returns the matrix element for the specified row and column.
        """
        pass

    def homogenize(self, *args, **kwargs):
        """
        Returns a new matrix containing the homogenized version of this matrix.
        """
        pass

    def inverse(self):
        """
        Returns a new matrix containing this matrix's inverse.
        """
        return MMatrix()

    def isEquivalent(self, *args, **kwargs):
        """
        Test for equivalence of two matrices, within a tolerance.
        """
        pass

    def isSingular(self, *args, **kwargs):
        """
        Returns True if this matrix is singular.
        """
        pass

    def setElement(self, *args, **kwargs):
        """
        Sets the matrix element for the specified row and column.
        """
        pass

    def setToIdentity(self, *args, **kwargs):
        """
        Sets this matrix to the identity.
        """
        pass

    def setToProduct(self, *args, **kwargs):
        """
        Sets this matrix to the product of the two matrices passed in.
        """
        pass

    def transpose(self, *args, **kwargs):
        """
        Returns a new matrix containing this matrix's transpose.
        """
        pass

    kIdentity = None

    kTolerance = 1e-10


class MUintArray(object):
    """
    Array of unsigned int values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MUuid(object):
    """
    Manipulate UUID data.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(self):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._uuid = uuid.UUID('00000000-0000-0000-0000-000000000000')

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __str__(self):
        """
        x.__str__() <==> str(x)
        """
        return str(self._uuid).upper()

    def asString(self):
        """
        asString() -> string

        Return the UUID as a string.
        """
        return str(self)

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy method. Assigns the value of one MUuid to another.

        * source (MUuid) - Existing MUuid object to copy.
        """
        pass

    def generate(self):
        """
        generate() -> self

        Generate a new UUID.
        """
        self._uuid = uuid.uuid4()
        return self

    def valid(*args, **kwargs):
        """
        valid() -> bool

        Return whether the UUID is valid.
        """
        pass


class MPxData(object):
    """
    Base Class for User-defined Dependency Graph Data Types.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(src) -> self

        This method initializes an instance of an MPxData derived class from another existing instance.  This method can be thought of as the second half of a copy constructor for the class.  The default constructor has already been called for the instance, and this method is used to set the private data by copying the values from an existing instance.
        This method must be implemented by the derived class.

        * src (MPxData) - The object from which to copy the private data
        """
        pass

    def name(*args, **kwargs):
        """
        name() -> string

        Returns the name of the custom data type.
        This method must be implemented by the derived class.
        """
        pass

    def readASCII(*args, **kwargs):
        """
        readASCII(argList, endOfTheLastParsedElement) -> int

        Creates Data in Data Block as specified by input from ASCII file record.
        Returns the new last argument parsed by this method.

        * argList (MArgList) - List of arguments read from ASCII record* endOfTheLastParsedElement (int) - points to last argument already parsed.
        """
        pass

    def readBinary(*args, **kwargs):
        """
        readBinary(in, length) -> int

        Creates Data in Data Block as specified by binary data from the given stream.
        Returns the numbers of data bytes processed or -1 in case of error.

        * in (bytearray) - Input stream
        * length (int) - Length in bytes of binary data to be read.
        """
        pass

    def typeId(*args, **kwargs):
        """
        typeId() -> MTypeId

        Determines the type id of the Data object.
        This method must be implemented by the derived class.
        """
        pass

    def writeASCII(*args, **kwargs):
        """
        writeASCII() -> string

        Encodes Data in accordance with the ASCII file format and returns as string.
        """
        pass

    def writeBinary(*args, **kwargs):
        """
        writeBinary() -> bytearray

        Encodes Data in accordance with the binary file format and returns as bytearray.
        """
        pass

    kData = 0

    kGeometryData = 1

    kLast = 2


class MPlugArray(object):
    """
    Array of MPlug values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MEvaluationNodeIterator(object):
    """
    A class providing access to the Evaluation Manager node dirty plug list.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def isDone(*args, **kwargs):
        """
        Checks to see if the iterator has reached the end of the iteration.
        """
        pass

    def next(*args, **kwargs):
        """
        Advances the iterator to the next position in the dirty plug list.
        """
        pass

    def plug(*args, **kwargs):
        """
        Returns the dirty plug at the current iterator position. Returns an empty plug if the iterator is illegal.
        """
        pass

    def reset(*args, **kwargs):
        """
        Resets the iterator to the first position in the dirty plug list.
        """
        pass


class MMatrixArray(object):
    """
    Array of MMatrix values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MArgList(object):
    """
    Argument list for passing to commands.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def addArg(*args, **kwargs):
        """
        addArg(arg) -> self , 'arg' is a numeric value, MAngle, MDistance,
        MTime, MPoint or        MVector.

        Add an argument to the end of the arg list.
        """
        pass

    def asAngle(*args, **kwargs):
        """
        asAngle(index) -> MAngle

        Return an argument as an MAngle.
        """
        pass

    def asBool(*args, **kwargs):
        """
        asBool(index) -> bool

        Return an argument as a boolean.
        """
        pass

    def asDistance(*args, **kwargs):
        """
        asDistance(index) -> MDistance

        Return an argument as an MDistance.
        """
        pass

    def asDouble(*args, **kwargs):
        """
        asDouble(index) -> float

        Alias for asFloat().
        """
        pass

    def asDoubleArray(*args, **kwargs):
        """
        asDoubleArray(index) -> MDoubleArray

        Return a sequence of arguments as an MDoubleArray.
        """
        pass

    def asFloat(*args, **kwargs):
        """
        asFloat(index) -> float

        Return an argument as a float.
        """
        pass

    def asInt(*args, **kwargs):
        """
        asInt(index) -> int

        Return an argument as an integer.
        """
        pass

    def asIntArray(*args, **kwargs):
        """
        asIntArray(index) -> MIntArray

        Return a sequence of arguments as an MIntArray.
        """
        pass

    def asMatrix(*args, **kwargs):
        """
        asMatrix(index) -> MMatrix

        Return a sequence of arguments as an MMatrix.
        """
        pass

    def asPoint(*args, **kwargs):
        """
        asPoint(index) -> MPoint

        Return a sequence of arguments as an MPoint.
        """
        pass

    def asString(*args, **kwargs):
        """
        asString(index) -> string

        Return an argument as a string.
        """
        pass

    def asStringArray(*args, **kwargs):
        """
        asStringArray(index) -> list of strings

        Return a sequence of arguments as a list of strings.
        """
        pass

    def asTime(*args, **kwargs):
        """
        asTime(index) -> MTime

        Return an argument as an MTime.
        """
        pass

    def asVector(*args, **kwargs):
        """
        asVector(index) -> MVector

        Return a sequence of arguments as an MVector.
        """
        pass

    def flagIndex(*args, **kwargs):
        """
        flagIndex(shortFlag, longFlag=None) -> int

        Return index of first occurrence of specified flag.
        """
        pass

    def lastArgUsed(*args, **kwargs):
        """
        lastArgUsed() -> int

        Return index of last argument used by the most recent as*() method.
        """
        pass

    kInvalidArgIndex = -1


class MItDag(object):
    """
    DAG Iterator.

    Use the DAG iterator to traverse the DAG either depth first or breadth
    first, visiting each node and, if desired, retrieving the node (as an
    MObject).  The DAG iterator provides a basic filtering capability, so
    that DAG node retrieval can be limited to a  specific type (MFn.Type)
    of node.  With filtering enabled the iterator checks to see if the node
    is compatible with the type of Function Set specified by the filter.
    See MFn.Type for a list of all valid Function set types.

    Since each object, if retrieved, is returned as an MObject, the
    MObject.hasFn() method can be used to further check for compatible
    function set types since an MObjects may be compatible with more than
    one function set).

    Any compatible Function Set can be attached to the retrieved object to
    query or or edit it.  Often you will want to use the DAG node Function
    Set (MFnDagNode), which is compatible with all DAG objects, to perform
    basic queries on each node as the iterator traverses the DAG.

    The iterator also provides the capability to reset the root of the
    iteration, the type of traversal, and the filter.

    Additionally, the iterator can be queried for the root, mode and type
    of traversal, and to determine if the the traversal has been completed.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def currentItem(*args, **kwargs):
        """
        currentItem() -> MObject

        Retrieves DAG node to which the iterator points.
        """
        pass

    def depth(*args, **kwargs):
        """
        depth() -> integer

        Returns the height or depth of the current node in the DAG relative to the
        root node.  The root node has a depth of zero.
        """
        pass

    def fullPathName(*args, **kwargs):
        """
        fullPathName() -> MString

        Return a string representing the full path from the root of the dag to this object.
        """
        pass

    def getAllPaths(*args, **kwargs):
        """
        getAllPaths() -> MDagPathArray

        Determines all DAG Paths to current item in the iteration.
        """
        pass

    def getPath(*args, **kwargs):
        """
        getPath() -> MDagPath

        Determines a DAG Path to the current item in the iteration.
        """
        pass

    def instanceCount(*args, **kwargs):
        """
        instanceCount(total) -> Integer

        Determines the number of times the current item (DAG node) in the iteration
        is instanced.

        If total is False the number of direct instances is returned, which
        is the same as the node's parent count.

        If total is True the total number of instances is returned, including
        indirect instances resulting from instancing higher up the DAG hierarchy
        (i.e. one or more of the node's ancestors also has multiple instances).
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> Bool

        Indicates end of iteration path.
        """
        pass

    def isInstanced(*args, **kwargs):
        """
        isInstanced(indirect = True) -> Bool

        Determines whether the current item (DAG node) in the iteration is directly
        or indirectly instanced.

        If indirect instance flag is False, the result is True if and only if the
        Node itself is multiply instanced (node.parentCount > 1).

        If the indirect flag is True, the result is True if and only if the Node
        itself is multiply instanced (node.parentCount > 1) or if the Node is not
        multiply instanced, but it has a directly instanced parent
        (node.parentCount()=1 and parent.parentCount >1).

        * indirect (Bool) -Indirect instance flag, defaults to True.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Moves to the next node matching the filter in the graph.
        """
        pass

    def partialPathName(*args, **kwargs):
        """
        partialPathName() -> MString

        Return a string representing the partial path from the root of the
        dag to this object.

        The partial path is the minimum path that is still unique. This string
        may contain wildcards.
        """
        pass

    def prune(*args, **kwargs):
        """
        prune() -> self

        Prunes iteration tree at current node.
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
        reset(rootPath, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
        reset(dagInfoObject, rootObject OR rootPath, traversalType = MItDag.kDepthFirst) -> self


        Resets the iterator.
        When used without parameters, the iterator is reset to the previous traversal setting.
        If a dagInfoObject is used, then the type of the provided rootObject or rootPath must
        match dagInfoObject.objectType.

           rootObject (MObject) - Root node to begin the next traversal.
           rootPath (MDagPath) - Root path to to begin the next traversal. Useful with instances.
           dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           traversalType (MItDag.TraversalType) - Enumerated type that determines the direction of the traversal, defaults to kDepthFirst.
           filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid
        """
        pass

    def root(*args, **kwargs):
        """
        root() -> MObject

        Returns the root (start node) of the current traversal.
        The constructor sets the root of traversal to the world node.
        The root can be changed by the reset() method.
        """
        pass

    def traversalType(*args, **kwargs):
        """
        traversalType() -> MItDag.TraversalType

        Returns the direction of the traversal.
        """
        pass

    kBreadthFirst = 2

    kDepthFirst = 1

    kInvalidType = 0

    traverseUnderWorld = None


class MRampAttribute(object):
    """
    Functionset for creating and working with ramp attributes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addEntries(*args, **kwargs):
        """
        Adds entries to the ramp.
        """
        pass

    def deleteEntries(*args, **kwargs):
        """
        Removes from the ramp those entries with the specified indices.
        """
        pass

    def getEntries(*args, **kwargs):
        """
        Returns a tuple containing all of the entries in the ramp.
        """
        pass

    def getValueAtPosition(*args, **kwargs):
        """
        Returns the value of the entry at the given position.
        """
        pass

    def hasIndex(*args, **kwargs):
        """
        Return true if an entry is defined at this index.
        """
        pass

    def numEntries(*args, **kwargs):
        """
        Returns the number of entries in the ramp.
        """
        pass

    def pack(*args, **kwargs):
        """
        Change the indices numbering by re-ordering them from 0.
        """
        pass

    def setInterpolationAtIndex(*args, **kwargs):
        """
        Sets the interpolation of the entry at the given index.
        """
        pass

    def setPositionAtIndex(*args, **kwargs):
        """
        Sets the position of the entry at the given index.
        """
        pass

    def setRamp(*args, **kwargs):
        """
        Set this ramp with one or multiple entries. Current entries are removed before adding the new one(s).
        """
        pass

    def setValueAtIndex(*args, **kwargs):
        """
        Sets the value of the entry at the given index.
        """
        pass

    def sort(*args, **kwargs):
        """
        Sort the ramp by position. Indices are also re-ordered during sort.
        """
        pass

    @staticmethod
    def createColorRamp(*args, **kwargs):
        """
        Creates and returns a new color ramp attribute.
        """
        pass

    @staticmethod
    def createCurveRamp(*args, **kwargs):
        """
        Creates and returns a new curve ramp attribute.
        """
        pass

    @staticmethod
    def createRamp(*args, **kwargs):
        """
        Creates and returns a new color or curve ramp attribute initialized with values.
        """
        pass

    isColorRamp = None

    isCurveRamp = None

    kLinear = 1

    kNone = 0

    kSmooth = 2

    kSpline = 3


val = MRampAttribute


class MPxGeometryIterator(object):
    """
    Base class for user defined geometry iterators.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def component(*args, **kwargs):
        """
        component() -> MObject

        Returns a component for the current item in the iteration.
        """
        pass

    def geometry(*args, **kwargs):
        """
        geometry() -> long/object

        Returns the user geometry that this iterator is iterating over.
        """
        pass

    def hasNormals(*args, **kwargs):
        """
        hasNormals() -> bool

        Returns whether the underlying geometry has normals.
        """
        pass

    def hasPoints(*args, **kwargs):
        """
        hasPoints() -> bool

        Returns whether the underlying geometry has point data.
        """
        pass

    def index(*args, **kwargs):
        """
        index() -> int

        Returns a unique index for the current item in the iteration.
        If the iteration is over the whole geometry then this index is the same as current point. If the iteration is over some elements of the geometry specified by a component then this index is the index in your geometry.
        """
        pass

    def indexUnsimplified(*args, **kwargs):
        """
        indexUnsimplified() -> int

        Returns a unique index for the current item in the iteration.
        Rather than being the iterator index this is the index for the actual item when simplification is skipping items. This index will be equal to index() if no simplification, otherwise it will be larger.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Returns whether all the items have been traversed yet.
        """
        pass

    def iteratorCount(*args, **kwargs):
        """
        iteratorCount() -> int

        Returns an estimate of how many items will be iterated over.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advances to the next component.
        """
        pass

    def point(*args, **kwargs):
        """
        point() -> MPoint

        Returns the current component's positional data.
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self

        Resets the iterator to the start of the components so that another pass over them may be made.
        """
        pass

    def setObject(*args, **kwargs):
        """
        setObject(shape) -> self

        Optional method to set a shape object to iterate over to allow tweaking of the shape's history (input geometry).

        * shape (MPxSurfaceShape) - a user defined shape object.
        """
        pass

    def setPoint(*args, **kwargs):
        """
        setPoint(point) -> self

        Sets the current component's positional data.

        * point (MPoint) - the new positional value to set.
        """
        pass

    def setPointGetNext(*args, **kwargs):
        """
        setPointGetNext(point) -> int

        Sets the current component's positional data, and returns the next index value.

        * point (MPoint) - the positional value to set.
        """
        pass

    currentPoint = None

    maxPoints = None


class MSelectionList(object):
    """
    A heterogenous list of MObjects, MPlugs and MDagPaths.

    __init__()
    Initializes a new, empty MSelectionList object.

    __init__(MSelectionList other)
    Initializes a new MSelectionList object containing the same
    items as another list.
    """

    def __init__(self):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._inner_ls = []

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def add(self,
            item: Union[str, "MPlug", "MObject", "MDagPath", Iterable[Union["MDagPath", "MObject"]]],
            searchChildNamespaces=False,
            mergeWithExisting=True):
        """
        add(pattern, searchChildNamespaces=False) -> self
        add(pattern, searchChildNamespaces=False) -> self
        add(item, mergeWithExisting=True) -> self


        The first version adds to the list any nodes, DAG paths, components
        or plugs which match the given the pattern string.

        The second version adds the specific item to the list, where the
        item can be a plug (MPlug), a node (MObject), a DAG path (MDagPath)
        or a component (tuple of (MDagPath, MObject) ).
        """

        self._inner_ls.append(item)

    def clear(self):
        """
        clear() -> self

        Empties the selection list.
        """
        self._inner_ls: list = []
        return self

    def copy(*args, **kwargs):
        """
        copy(src) -> self

        Replaces the contents of the selection list with a copy of those from src (MSelectionList).
        """
        pass

    def getComponent(*args, **kwargs):
        """
        getComponent(index) -> (MDagPath, MObject)

        Returns the index'th item of the list as a component, represented by
        a tuple containing an MDagPath and an MObject. If the item is just a
        DAG path without a component then MObject.kNullObj will be returned
        in the second element of the tuple. Raises TypeError if the item is
        neither a DAG path nor a component. Raises IndexError if index is
        out of range.
        """
        pass

    def getDagPath(self, index: int) -> "MDagPath":
        """
        getDagPath(index) -> MDagPath

        Returns the DAG path associated with the index'th item of the list.
        Raises TypeError if the item is neither a DAG path nor a component.
        Raises IndexError if index is out of range.
        """
        item = self._inner_ls[index]
        if isinstance(item, str):
            item = MDagPath()
        if not isinstance(item, MDagPath):
            raise TypeError(f'Given index: {index} does not belong to a MPlug object. Current obj: {item}.')
        return item

    # noinspection PyProtectedMember
    def getDependNode(self, index: int) -> "MObject":
        """
        getDependNode(index) -> MObject

        Returns the node associated with the index'th item, whether it be a
        dependency node, DAG path, component or plug.
        Raises kFailure if there is no dependency node associated with the current item.
        Raises IndexError if index is out of range.
        """
        item = self._inner_ls[index]
        # If the item is not an MObject but a string, retrieve the mobject from the pool
        if isinstance(item, str):
            mobject = hierarchy.NodePool.from_name(item)
            if not mobject:
                # For nodes that already exist in the scene but are not inside the pool, initialize them as DependNodes
                mobject = MFnDependencyNode().create('transform', item)  # this very rarely will be the case as it should already be created before adding it to the MSelectionList
                hierarchy.register(mobject)
            # Return converted str to mobject
            return mobject

        elif not isinstance(item, MObject):
            raise TypeError(f'Given index: {index} does not belong to a MPlug object. Current obj: {item}.')
        return item

    def getPlug(self, index: int) -> "MPlug":
        """
        getPlug(index) -> MPlug

        Returns the index'th item of the list as a plug. Raises TypeError if
        the item is not a plug. Raises IndexError if index is out of range.
        """
        item = self._inner_ls[index]
        if isinstance(item, str):
            mplug = MPlug()
            mplug._name = item
            return mplug
        if not isinstance(item, MPlug):
            raise TypeError(f'Given index: {index} does not belong to a MPlug object. Current obj: {item}.')
        return item

    def getSelectionStrings(self, index: str) -> tuple[str]:
        """
        getSelectionStrings(index=None) -> (string, string, ...)

        Returns a tuple containing the string representation of the
        specified item. For nodes, DAG paths, plugs and contiguous
        components the tuple will only contain a single string, but for non-
        contiguous components there will be a separate string for each
        distinct block of contiguous elements. If index is not specified
        then the string representations of all the items in the selection
        list are returned. Raises IndexError if index is out of bounds.
        """
        pass

    def hasItem(*args, **kwargs):
        """
        hasItem(item) -> bool

        Returns True if the given item is on the selection list. For a
        component this means that all of the elements of the component must
        be on the list. A component is passed as a tuple containing the
        MDagPath of the DAG node and an MObject containing the component.
        """
        pass

    def hasItemPartly(*args, **kwargs):
        """
        hasItemPartly(dagPath, component) -> bool

        Returns True if at least one of the component's elements is on the
        selection list. Raises TypeError if dagPath is invalid or component
        does not contain a component.
        """
        pass

    def intersect(*args, **kwargs):
        """
        intersect(other, expandToLeaves=False) -> self

        Modify this list to contain the intersection of itself and the given list.
        """
        pass

    def isEmpty(*args, **kwargs):
        """
        isEmpty() -> bool

        Returns True if the selection list is empty.
        """
        pass

    def length(self) -> int:
        """
        length() -> int

        Returns the number of items on the selection list.
        """
        return len(self._inner_ls)

    def merge(*args, **kwargs):
        """
        merge(other, strategy=kMergeNormal) -> self
        merge(dagPath, component, strategy=kMergeNormal) -> self

        The first version merges the items from another selection list in
        with those already on the list, using the given strategy.

        The second version merges the specified component with those already
        on the list.
        """
        pass

    def remove(*args, **kwargs):
        """
        remove(index) -> self

        Removes the index'th item from the list. Raises IndexError if the
        index is out of range.
        """
        pass

    def replace(*args, **kwargs):
        """
        replace(index, newItem) -> self

        Replaces the index'th item on the list with a new item. A component
        is passed as a tuple containing the MDagPath of the DAG node and an
        MObject containing the component. Raises IndexError if the index is
        out of range.
        """
        pass

    def toggle(*args, **kwargs):
        """
        toggle(dagPath, component) -> self

        Removes from the list those elements of the given component which
        are already on it and adds those which are not.
        """
        pass

    kMergeNormal = 0

    kRemoveFromList = 2

    kXORWithList = 1


class MItMeshPolygon(object):
    """
    This class is the iterator for polygonal surfaces (meshes).
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def center(*args, **kwargs):
        """
        center(space=kObject) -> MPoint

        Return the position of the center of the current polygon

        * space (int) - The coordinate system for this operation
        """
        pass

    def count(*args, **kwargs):
        """
        count() -> int

        Return the number of polygons in the iteration
        """
        pass

    def currentItem(*args, **kwargs):
        """
        currentItem() -> MObject

        Get the current polygon in the iteration as a component.

        Components are used to specify one or more polygons and are usefull in operating on groups of non-contiguous polygons for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
        pass

    def geomChanged(*args, **kwargs):
        """
        geomChanged() -> self

        Reset the geom pointer in the MItMeshPolygon. This is now being handled automatically inside the iterator, and users should no longer need to call this method directly to sync up the iterator to changes made by MFnMesh
        """
        pass

    def getArea(*args, **kwargs):
        """
        getArea(space=kObject) -> float

        This method gets the area of the face

        * space (int) - World Space or Object Space
        """
        pass

    def getColor(*args, **kwargs):
        """
        getColor(colorSetName=None) -> MColor
        getColor(vertexIndex) -> MColor

        This method gets the color of the specified vertex in this face

        * index (int) - The face-relative vertex index on this face

        Or the average color of the all the vertices in this face

        * colorSetName (string) - Name of the color set.
        """
        pass

    def getColorIndex(*args, **kwargs):
        """
        getColorIndex(vertexIndex, colorSetName=None) -> int

        This method returns the colorIndex for a vertex of the current face.

        * vertexIndex (int) - Face-relative index of vertex.
        * colorSetName (string) - Name of the color set.
        """
        pass

    def getColorIndices(*args, **kwargs):
        """
        getColorIndices(colorSetName=None) -> MIntArray

        This method returns the colorIndices for each vertex on the face.

        * colorSetName (string) - Name of the color set.
        """
        pass

    def getColors(*args, **kwargs):
        """
        getColors(colorSetName=None) -> MColorArray

        This method gets the color of the each vertex in the current face.

        * colorSetName (string) - Name of the color set.
        """
        pass

    def getConnectedEdges(*args, **kwargs):
        """
        getConnectedEdges() -> MIntArray

        This method gets the indices of the edges connected to the vertices of the current face, but DOES not include the edges contained in the current face
        """
        pass

    def getConnectedFaces(*args, **kwargs):
        """
        getConnectedFaces() -> MIntArray

        This method gets the indices of the faces connected to the current face.
        """
        pass

    def getConnectedVertices(*args, **kwargs):
        """
        getConnectedVertices() -> MIntArray

        This method gets the object-relative indices of the vertices surrounding the vertices of the current face, but does not include the vertices of the current face
        """
        pass

    def getEdges(*args, **kwargs):
        """
        getEdges() -> MIntArray

        This method gets the indices of the edges contained in the current face.
        """
        pass

    def getNormal(*args, **kwargs):
        """
        getNormal(space=kObject) -> MVector
        getNormal(verexIndex, space=kObject) -> MVector

        Return the face normal of the current polygon.

        * space (int) - The transformation space

        Returns the vertex-face normal for the vertex in the current polygon.

        * index (int) - face-relative vertex index of the vertex whose normal to retrieve
        * space (int) - The transformation space
        """
        pass

    def getNormals(*args, **kwargs):
        """
        getNormals(space=kObject) -> MVectorArray

        Returns the normals for all vertices in the current face

        * space (int) - The transformation space
        """
        pass

    def getPointAtUV(*args, **kwargs):
        """
        getPointAtUV(uvPoint, space=kObject, uvSet=None, tolerance=0) -> MPoint

        Return the position of the point at the given UV value in the current polygon.

        * uvPoint ([float, float]) - The UV value to try to locate
        * space (int) - The coordinate system for this operation
        * uvSet (string) - UV set to work with
        * tolerance (float) - tolerance value to compare float data type
        """
        pass

    def getPoints(*args, **kwargs):
        """
        getPoints(space=kObject) -> MPointArray

        Retrieves the positions of the vertices on the current face/polygon that the iterator is pointing to. Vertex positions will be inserted into the given array and will be indexed using face-relative vertex IDs (ie. ordered from 0 to (vertexCount of the face) - 1), which should not be confused with the vertexIDs of each vertex in relation to the entire mesh object.

        * space (int) - The coordinate system for this operation
        """
        pass

    def getTriangle(*args, **kwargs):
        """
        getTriangle(localTriIndex, space=kObject) -> [MPointArray, MIntArray]

        Get the vertices and vertex positions of the given triangle in the current face's triangulation.

        * localTriIndex (int) - Local index of the desired triangle in this face
        * space (int) - World Space or Object Space
        """
        pass

    def getTriangles(*args, **kwargs):
        """
        getTriangles(space=kObject) -> [MPointArray, MIntArray]

        Get the vertices and vertex positions of all the triangles in the current face's triangulation

        * space (int) - World Space or Object Space
        """
        pass

    def getUV(*args, **kwargs):
        """
        getUV(vertexId, uvSet=None) -> [float, float]

        Return the texture coordinate for the given vertex.

        * vertex (int) - The face-relative vertex index to get UV for
        * uvSet (string) - UV set to work with
        """
        pass

    def getUVArea(*args, **kwargs):
        """
        getUVArea(uvSet=None) -> float

        This method gets the UV area of the face

        * uvSet (string) - UV set to work with
        """
        pass

    def getUVAtPoint(*args, **kwargs):
        """
        getUVAtPoint(pt, space=kObject, uvSet=None) -> [float, float]

        Find the point closest to the given point in the current polygon, and return the UV value at that point.

        * pt (MPoint) - The point to try to get UV for
        * space (int) - The coordinate system for this operation
        * uvSet (string) - UV set to work with
        """
        pass

    def getUVIndex(*args, **kwargs):
        """
        getUVIndex(vertex, uvSet=None) -> int

        Returns the index of the texture coordinate for the given vertex.
        This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

        * vertex (int) - The face-relative vertex index of the current polygon
        * uvSet (string) - UV set to work with
        """
        pass

    def getUVIndexAndValue(*args, **kwargs):
        """
        getUVIndexAndValue(vertex, uvSet=None) -> [int, float, float]

        Return the index and value of the texture coordinate for the given vertex. This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

        * vertex (int) - The face-relative vertex index of the current polygon
        * uvSet (string) - UV set to work with
        """
        pass

    def getUVSetNames(*args, **kwargs):
        """
        getUVSetNames() -> list of strings

        This method is used to find the UV set names mapped to the current face
        """
        pass

    def getUVs(*args, **kwargs):
        """
        getUVs(uvSet=None) -> [MFloatArray, MFloatArray]

        Return the all the texture coordinates for the vertices of this face (in local vertex order).

        * uvSet (string) - UV set to work with
        """
        pass

    def getVertices(*args, **kwargs):
        """
        getVertices() -> MIntArray

        This method gets the indices of the vertices of the current face
        """
        pass

    def hasColor(*args, **kwargs):
        """
        hasColor() -> bool
        hasColor(localVertexIndex) -> bool

        This method determines whether the current face has color-per-vertex set for any or the given vertex

        * localVertexIndex (int) - face-relative vertex index to check for color on
        """
        pass

    def hasUVs(*args, **kwargs):
        """
        hasUVs(uvSet=None) -> bool

        Tests whether this face has UV's mapped or not (either all the vertices for a face should have UV's, or none of them do, so the UV count for a face is either 0, or equal to the number of vertices).

        * uvSet (string) - UV set to work with
        """
        pass

    def hasValidTriangulation(*args, **kwargs):
        """
        hasValidTriangulation() -> bool

        This method checks if the face has a valid triangulation. If it doesn't, then the face was bad geometry: it may gave degenerate points or cross over itself.
        """
        pass

    def index(*args, **kwargs):
        """
        index() -> int

        Returns the index of the current polygon
        """
        pass

    def isConnectedToEdge(*args, **kwargs):
        """
        isConnectedToEdge(index) -> bool

        This method determines whether the given face is adjacent to the current face

        * index (int) - Index of the face to be tested for
        """
        pass

    def isConnectedToFace(*args, **kwargs):
        """
        isConnectedToFace(index) -> bool

        This method determines whether the given face is adjacent to the current face

        * index (int) - Index of the face to be tested for
        """
        pass

    def isConnectedToVertex(*args, **kwargs):
        """
        isConnectedToVertex(index) -> bool

        This method determines whether the given vertex shares an edge with a vertex in the current face

        * index (int) - Index of the face to be tested for
        """
        pass

    def isConvex(*args, **kwargs):
        """
        isConvex() -> bool

        This method checks if the face is convex.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Indicates if all of the polygons have been traversed yet.
        """
        pass

    def isHoled(*args, **kwargs):
        """
        isHoled() -> bool

        This method checks if the face has any holes.
        """
        pass

    def isLamina(*args, **kwargs):
        """
        isLamina() -> bool

        This method checks if the face is a lamina (the face is folded over onto itself).
        """
        pass

    def isPlanar(*args, **kwargs):
        """
        isPlanar() -> bool

        This method checks if the face is planar
        """
        pass

    def isStarlike(*args, **kwargs):
        """
        isStarlike() -> bool

        This method checks if the face is starlike. That is, a line from the centre to any vertex lies entirely within the face.
        """
        pass

    def isUVReversed(*args, **kwargs):
        """
        isUVReversed(faceId) -> bool

        Returns True if the texture coordinates (uv's) for the face are
        reversed (clockwise), False if they are not reversed (counter clockwise).
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advance to the next polygon in the iteration.
        """
        pass

    def normalIndex(*args, **kwargs):
        """
        normalIndex(vertex) -> int

        Returns the normal index for the specified vertex.
        This index refers to an element in the normal array returned by MFnMesh.getNormals.  These normals are per-polygon per-vertex normals. See the MFnMesh description for more information on normals.

        * localVertexIndex (int) - The face-relative index of the vertex to examine for the current polygon
        """
        pass

    def numColors(*args, **kwargs):
        """
        numColors(colorSetName=None) -> int

        This method checks for the number of colors on vertices in this face

        * colorSetName (string) - Name of the color set.
        """
        pass

    def numConnectedEdges(*args, **kwargs):
        """
        numConnectedEdges() -> int

        This method checks for the number of connected edges on the vertices of this face
        """
        pass

    def numConnectedFaces(*args, **kwargs):
        """
        numConnectedFaces() -> int

        This method checks for the number of connected faces
        """
        pass

    def numTriangles(*args, **kwargs):
        """
        numTriangles() -> int

        This Method checks for the number of triangles in this face in the current triangulation
        """
        pass

    def onBoundary(*args, **kwargs):
        """
        onBoundary() -> bool

        This method determines whether the current face is on a boundary
        """
        pass

    def point(*args, **kwargs):
        """
        point(index, space=kObject) -> MPoint

        Return the position of the vertex at index in the current polygon.

        * index (int) - The face-relative index of the vertex in the current polygon
        * space (int) - The coordinate system for this operation
        """
        pass

    def polygonVertexCount(*args, **kwargs):
        """
        polygonVertexCount() -> int

        Return the number of vertices for the current polygon
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(polyObject) -> self
        reset(polyObject, component=None) -> self

        Reset the iterator to the first polygon

        Reset the iterator to the first polygon in the supplied surface

        * polyObject (MObject) - The polygon for the iteration

        Reset the iterator with the given surface and component.
        If component is None then the iteration will be for all polygons in the given surface.

        * polyObject (MDagPath) - The surface (mesh) to iterate over
        * component (MObject) - The polygons (faces) of the polyObject to iterate over
        """
        pass

    def setIndex(*args, **kwargs):
        """
        setIndex(index) -> int

        This method sets the index of the current face to be accessed.
        The current face will no longer be in sync with any previous iteration.
        Returns the index of the current face in the iteration

        * index (int) - The index of desired face to access.
        """
        pass

    def setPoint(*args, **kwargs):
        """
        setPoint(point, index, space=kObject) -> self

        Set the vertex at the given index in the current polygon.

        * point (MPoint) - The new position for the vertex
        * index (int) - The face-relative index of the vertex in the current polygon
        * space (int) - The coordinate system for this operation
        """
        pass

    def setPoints(*args, **kwargs):
        """
        setPoints(pointArray, space=kObject) -> self

        Sets new locations for vertices of the current polygon that the iterator is pointing to.

        * pointArray (MPointArray) - The new positions for the vertices.
        * space (int) - The coordinate system for this operation.
        """
        pass

    def setUV(*args, **kwargs):
        """
        setUV(vertexId, uvPoint, uvSet=None) -> self

        Modify the UV value for the given vertex in the current face.
        If the face is not already mapped, this method will fail.

        * vertexId (int) - face-relative index of the vertex to set UV for.
        * uvPoint ([float, float]) - The UV values to set it to
        * uvSet (string) - UV set to work with
        """
        pass

    def setUVs(*args, **kwargs):
        """
        setUVs(uArray, vArray, uvSet=None) -> self

        Modify the UV value for all vertices in the current face.
        If the face has not already been mapped, this method will fail.

        * uArray (MFloatArray) - All the U values - in local face order
        * vArray (MFloatArray) - The corresponding V values
        * uvSet (string) - UV set to work with
        """
        pass

    def tangentIndex(*args, **kwargs):
        """
        tangentIndex(localVertexIndex) -> int

        Returns the tangent (or binormal) index for the specified vertex.
        This index refers to an element in the normal array returned by MFnMesh.getTangents. These tangent or binormals are per-polygon per-vertex.
        See the MFnMesh description for more information on tangents and binormals.

        * localVertexIndex(int) - The face-relative index of the vertex to examine for the current polygon
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        Signal that this polygonal surface has changed and needs to redraw itself.
        """
        pass

    def vertexIndex(*args, **kwargs):
        """
        vertexIndex(index) -> int

        Returns the object-relative index of the specified vertex of the current polygon.
        The index returned may be used to refer to an element in the vertex list returned by MFnMesh.getPoints.

        * index (int) - The face-relative index of the vertex in the polygon
        """
        pass

    def zeroArea(*args, **kwargs):
        """
        zeroArea() -> bool

        This method checks if its a zero area face
        """
        pass

    def zeroUVArea(*args, **kwargs):
        """
        zeroUVArea(uvSet=None) -> bool

        This method checks if the UV area of the face is zero

        * uvSet (string) - UV set to work with
        """
        pass


class MFloatMatrix(object):
    """
    4x4 matrix with single-precision elements.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __isub__(*args, **kwargs):
        """
        x.__isub__(y) <==> x-=y
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __radd__(*args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(*args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def __sub__(*args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def adjoint(*args, **kwargs):
        """
        Returns a new matrix containing this matrix's adjoint.
        """
        pass

    def det3x3(*args, **kwargs):
        """
        Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix.
        """
        pass

    def det4x4(*args, **kwargs):
        """
        Returns this matrix's determinant.
        """
        pass

    def getElement(*args, **kwargs):
        """
        Returns the matrix element for the specified row and column.
        """
        pass

    def homogenize(*args, **kwargs):
        """
        Returns a new matrix containing the homogenized version of this matrix.
        """
        pass

    def inverse(*args, **kwargs):
        """
        Returns a new matrix containing this matrix's inverse.
        """
        pass

    def isEquivalent(*args, **kwargs):
        """
        Test for equivalence of two matrices, within a tolerance.
        """
        pass

    def setElement(*args, **kwargs):
        """
        Sets the matrix element for the specified row and column.
        """
        pass

    def setToIdentity(*args, **kwargs):
        """
        Sets this matrix to the identity.
        """
        pass

    def setToProduct(*args, **kwargs):
        """
        Sets this matrix to the product of the two matrices passed in.
        """
        pass

    def transpose(*args, **kwargs):
        """
        Returns a new matrix containing this matrix's transpose.
        """
        pass

    kTolerance = 9.999999747378752e-06


class MExternalContentInfoTable(object):
    """
    This is a table of all the external content for a given node.
    """

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def addResolvedEntry(*args, **kwargs):
        """
        addResolvedEntry(key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles) -> self

        Add an entry in the table.

        * key (string) - An arbitrary string defined by the caller. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.
        * unresolvedLocation (string) - Path as stored in the node (i.e. without any token replacement performed).
        * resolvedLocation (string) - Full path to the content if it exists at the time of creation of this object.
        * contextNodeFullName (string) - The fullname of the URI owner (node) if it applies, an empty string otherwise.
        * roles (list of strings) - An enumeration of all roles this content plays in the context of the node. The actual strings are not rigidly defined as of this writing. This is mostly for offline browsing of the content info: to assist in sorting content by role.  A better content type system may be introduced later on to        formalize this.
        """
        pass

    def addUnresolvedEntry(*args, **kwargs):
        """
        addUnresolvedEntry(key, unresolvedLocation, contextNodeFullName, roles=None) -> self

        Add an entry in the table. The resolved location will be inferred from the application's built-in file resolving for the specified file type. This will automatically add entries into the roles vector that correspond to the search rules for this file type.

        * key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * unresolvedLocation (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * contextNodeFullName (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * roles (list of strings) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        """
        pass

    def getEntry(*args, **kwargs):
        """
        getEntry(index) -> [key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

        Retrieves external content entry based on its position in the table.

        * index (unsigned int) - Position of the entry to retrieve information from.
        """
        pass

    def getInfo(*args, **kwargs):
        """
        getInfo(key) -> [unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

        Retrieves external content information based on its key.

        * key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        """
        pass


class MItDependencyGraph(object):
    """
    Dependency Graph Iterator.

    Iterate over Dependency Graph (DG) Nodes or Plugs starting at a specified
    root Node or Plug.


    Set and query the root of the iteration.


    Set and query the direction (downstream or upstream), traversal priority
    (depth first or breadth first) and level of detail (Node level or Plug
    level) of the iteration.


    Set and disable a filter to iterate over only specific types (MFn.Type) of
    Nodes.


    Reset the root, filter, direction, traversal priority and level of detail
    of the iteration.


    Prune branches of the graph from iteration.


    In Maya, all geometry, animation and rendering information is implemented
    in nodes in the Dependency Graph (DG).  The DG includes the Directed Acyclic
    Graph (DAG).  Therefore, all DAG nodes are also DG nodes.  The data on nodes
    is associated with Attributes.  Attributes on nodes are connected to
    Attributes on other nodes via plugs on the Attributes.  Plugs are, in effect
    the external intefaces of Attributes.


    The DG Iterator Class (MItDependencyGraph) provides methods for iterating
    over either nodes or plugs, as well as methods for setting and querying the
    characteristics and behaviour of the iterator.


    This iterator will traverse all connected attributes upstream or
    downstream from the root node of the traversal. For non root nodes,
    only attributes that are affected by the incoming attribute to that
    node will be traversed.  Hence, only nodes to which data from the root
    node is flowing will be traversed.


    By default, the iterator does not traverse world-space attribute
    dependencies (an example of a world-space dependency is that
    translateX affects worldMatrix). The
    setTraversalOverWorldSpaceDependents method can be used to enable such
    traversal. Note that even when world-space traversal is enabled, the
    iterator will only iterate to connected nodes. It does not iterate up
    and down through the dag hierarchy.


    The DG Iterator is used in conjunction with the Maya Object (MObject), plug
    (MPlug), Maya Object Array (MObjectArray) and plug Array (MPlugArray)
    classes.


    It is also useful to use Function Sets specific to the nodes returned by
    the iterator to query and modify the nodes in the DG.


    The DG itself can be modified using a DG Modifer (MDGModifier).


    Additionally, nodes can be added to and retrieved from selection lists using
    the Selection List (MSelectionList) class and Selection List Iterator
    (MItSelectionList).  This can be useful for obtaining the root node for an
    iteration.


    Attributes on the nodes can be manipulated using the Attribute Function Set
    (MFnAttribute) and its derivations.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def currentNode(*args, **kwargs):
        """
        currentNode() -> MObject

        Retrieves the current node of the iteration.  Results in a null object on
        failure or if the node is of a unrecognized type.
        """
        pass

    def currentNodeHasUnknownType(*args, **kwargs):
        """
        currentNodeHasUnknownType() -> Bool

        Indicates whether or not the current node has an unrecognised
        type.  This is useful if an unexpected failure is encountered
        in the next() or currentNode() methods.
        """
        pass

    def currentPlug(*args, **kwargs):
        """
        currentPlug() -> MPlug

        Retrieves the current plug of the iteration.  Results in a null
        plug on failure.
        """
        pass

    def getNodePath(*args, **kwargs):
        """
        getNodePath() -> MObjectArray

        Retrieves the direct path from the current node to the root
        node.  Path does not include the current node.
        State of the provided array is undefined if this method fails.
        """
        pass

    def getNodesVisited(*args, **kwargs):
        """
        getNodesVisited() -> MObjectArray

        Retrieves all nodes visited during the iteration.
        State of the provided array is undefined if this method fails.
        """
        pass

    def getPlugPath(*args, **kwargs):
        """
        getPlugPath() -> MPlugArray

        Retrieves the direct path from the current plug to the root
        plug, with the current plug in element 0 of the array and the root
        plug in the final element of the array.

        Once the iterator is done (i.e. isDone() returns True) there is no
        longer a current plug and this method will return an empty array.

        If this method fails the state of the returned array is undefined.
        """
        pass

    def getPlugsVisited(*args, **kwargs):
        """
        getPlugsVisited() -> MPlugArray

        Retrieves all plugs visited during the iteration.
        State of the provided array is undefined if this method fails.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> Bool

        Indicates whether or not all nodes or plugs have been iterated over
        in accordance with the direction, traversal, level and filter.
        If a valid filter is set, the iterator only visits those nodes that match
        the filter.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Iterates to the next node or plug in accordance with the
        direction, traversal, level and filter.  If a valid filter is
        set, the iterator only visits those nodes that match the
        filter.  When filtering is enabled nodes that have unknown type
        are treated as non-matching nodes.  With filtering disabled,
        iteration to a node with an unknown type is treated as a
        failure.  An attempt to iterate when there is nothing left to
        iterate over has no effect.
        """
        pass

    def previousPlug(*args, **kwargs):
        """
        previousPlug() -> MPlug

        Retrieves the previous plug of the iteration.  Results in a
        null plug on failure.  Null plug may also indicate that the
        current plug is the root plug.
        """
        pass

    def prune(*args, **kwargs):
        """
        prune() -> self

        Prunes the search path at the current plug.  Iterator will not
        visit any of the plugs connected to the pruned plug.
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self

        Clears iterator data and resets the iterator to the root node
        or plug.  If a valid filter is enabled, the iterator
        automatically advances to the next node after the root node
        that matches the filter.  If no matching node is found an
        exception is thrown.
        """
        pass

    def resetFilter(*args, **kwargs):
        """
        resetFilter() -> self

        Resets the node or plug filter to default, MFn.kInvalid
        (filter disabled).  Disables pruning on the filter (default).
        Resets the iterator.
        """
        pass

    def resetTo(*args, **kwargs):
        """
        resetTo(rootObject, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel) -> self
        resetTo(rootPlug, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel) -> self
        resetTo(infoObject, rootObject OR rootPlug, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel) -> self


        Clears iterator data and re-initializes the iterator.  If a
        valid filter is provided, the iterator automatically advances
        to the next node after the root node that matches the filter.
        If no matching node is found an exception is thrown.


           rootObject (MObject) - Root node to begin the next traversal.
           rootPlug (MPlug) - Root plug to to begin the next traversal.
           infoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           filter (MFn.Type) - Function set type, defaults to MFn.kInvalid
           direction (MItDependencyGraph.Direction) - Primary direction of iteration, defaults to MItDependencyGraph.kDownstream
           traversal (MItDependencyGraph.Traversal) - Order of traversal, defaults to MItDependencyGraph.kDepthFirst
           level (MItDependencyGraph.Level) - Level of detail of the iteration, defaults to MItDependencyGraph.kNodeLevel
        """
        pass

    def rootNode(*args, **kwargs):
        """
        rootNode() -> MObject

        Retrieves the root node of the iteration.
        """
        pass

    def rootPlug(*args, **kwargs):
        """
        rootPlug() -> MPlug

        Retrieves the root plug of the iteration.
        """
        pass

    currentDirection = None

    currentFilter = None

    currentLevel = None

    currentTraversal = None

    kBreadthFirst = 1

    kDepthFirst = 0

    kDownstream = 0

    kNodeLevel = 0

    kPlugLevel = 1

    kUpstream = 1

    pruningOnFilter = None

    traversingOverWorldSpaceDependents = None


class MPxAttributePatternFactory(object):
    """
    Base class for custom attribute pattern factories.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass


class MGlobal(object):
    """
    Static class providing common API global functions.
    """

    @staticmethod
    def addToModel(*args, **kwargs):
        """
        addToModel(MObject, MObject) -> None

        This method is used to add new dag objects to the model.  If no parent node
        is specified, then the node is added under the world.  When a node is
        added under the world, then a transform node is automatically created as
        a parent.  This assumes that the node being added is not already a
        transform node.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter will be returned.
        """
        pass

    @staticmethod
    def addToModelAt(*args, **kwargs):
        """
        addToModelAt(MObject, MVector, double[3], double[3], rotateOrder=MTransformationMatrix.kXYZ) -> None

        Adds the specified dag object to the DAG and transform the object
        by the specified arguments.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter
        will be returned.
        """
        pass

    @staticmethod
    def animSelectionMask(*args, **kwargs):
        """
        animSelectionMask() -> MSelectionMask

        Returns the animation selection mask.
        """
        pass

    @staticmethod
    def apiVersion(*args, **kwargs):
        """
        apiVersion() -> int

        Returns a number describing the version of the Maya API at runtime.
        """
        pass

    @staticmethod
    def className(*args, **kwargs):
        """
        className() -> string

        Returns the name of this class.
        """
        pass

    @staticmethod
    def clearSelectionList(*args, **kwargs):
        """
        clearSelectionList() -> None

        Removes all items from the active selection list.
        """
        pass

    @staticmethod
    def closeErrorLog(*args, **kwargs):
        """
        closeErrorLog() -> None

        This method closes the API error log file.  If error logging is currently
        enabled this method disables it.
        The error log is time and date stamped before it is closed.
        After the log is closed the error log path name is reset to the default
        path name.
        If the error log file is already closed, then no action is taken.

        Note that if a log is reopened after it is closed, all information previously
        logged to it is lost.
        """
        pass

    @staticmethod
    def componentSelectionMask(*args, **kwargs):
        """
        componentSelectionMask() -> MSelectionMask

        Returns the component selection mask.
        """
        pass

    @staticmethod
    def currentToolContext(*args, **kwargs):
        """
        currentToolContext() -> MObject

        Returns the current tool context as an MObject.
        """
        pass

    @staticmethod
    def defaultErrorLogPathName(*args, **kwargs):
        """
        defaultErrorLogPathName() -> string

        Determines the default path name of the error log file.
        Returns an empty string on failure.
        """
        pass

    @staticmethod
    def deleteNode(*args, **kwargs):
        """
        deleteNode(MObject) -> None

        Delete the given dag node or dependency graph node.
        """
        pass

    @staticmethod
    def disableStow(*args, **kwargs):
        """
        disableStow() -> bool

        This method is used to query if the disabling of Stowing (hiding)
        and Unstowing (showing) windows is active.
        """
        pass

    @staticmethod
    def displayError(*args, **kwargs):
        """
        displayError(msg) -> None

        Display an error in the script editor.
        """
        pass

    @staticmethod
    def displayInfo(*args, **kwargs):
        """
        displayInfo(msg) -> None

        Display an informational message in the script editor.
        """
        pass

    @staticmethod
    def displayWarning(*args, **kwargs):
        """
        displayWarning(msg) -> None

        Display a warning in the script editor.
        """
        pass

    @staticmethod
    def doErrorLogEntry(*args, **kwargs):
        """
        doErrorLogEntry(string) -> bool

        Logs an entry in the currently open log file.  It is not necessary for error
        logging to be enabled, but a log file must be open.
        A newline is appended to each log entry.
        """
        pass

    @staticmethod
    def errorLogPathName(*args, **kwargs):
        """
        errorLogPathName() -> string

        Determines the path name of the current error log file.
        Returns the null stringon failure.
        """
        pass

    @staticmethod
    def errorLoggingIsOn(*args, **kwargs):
        """
        errorLoggingIsOn() -> bool

        This method determines whether or not API errors are being logged.
        """
        pass

    @staticmethod
    def executeCommandOnIdle(*args, **kwargs):
        """
        executeCommandOnIdle(string, bool displayEnabled=False) -> None

        Sets a MEL command to execute on the next idle event. Since the command
        will likely not be executed until some time after control is returned to
        caller, there is no access to the command results.

        This method is thread safe and can be called from a thread other than
        Maya's main thread. However, that thread must still be part of the Maya
        process. Calling this method from a completely separate process will
        not work and may lead to unpredictable behaviour.
        """
        pass

    @staticmethod
    def executeCommandStringResult(*args, **kwargs):
        """
        executeCommandStringResult(string, bool displayEnabled=False, bool undoEnabled=False) -> string or [string, string, ...]

        Executes a MEL command that returns a string or an array of strings
        result from the command engine depending on the number of return values.
        Optionally allows display of the command in the Command Window to be
        enabled or disabled.  Defaults to disabled.  Optionally allows undo
        for the command to be enabled or disabled.  Defaults to disabled.

        Note: This is not thread safe; you may use executeCommandOnIdle instead
        """
        pass

    @staticmethod
    def getAbsolutePathToResources(*args, **kwargs):
        """
        getAbsolutePathToResources() -> string

        Return the absolute path of Maya's "Resources" fold on the system,
        including the "Resources" folder itself.
        """
        pass

    @staticmethod
    def getActiveSelectionList(*args, **kwargs):
        """
        getActiveSelectionList(orderedSelectionIfAvailable=False) -> MSelectionList

        Return an MSelectionList containing the nodes, components and
        plugs currently selected in Maya. If orderedSelectionIfAvailable
        is True, and tracking is enabled, will return the selected items
        in the order that they were selected.
        """
        return MSelectionList

    @staticmethod
    def getAssociatedSets(*args, **kwargs):
        """
        getAssociatedSets(MSelectionList) -> list

        This utility method finds all the sets that the items in
        the given selection list are members of.
        """
        pass

    @staticmethod
    def getFunctionSetList(*args, **kwargs):
        """
        getFunctionSetList(MObject) -> (string, string, ...)

        Returns a tuple of strings that represent the type of each function
        set that will accept this object.
        """
        pass

    @staticmethod
    def getHiliteList(*args, **kwargs):
        """
        getHiliteList() -> MSelectionList

        Returns a copy of the hilite list.  The hilite list contains all DAG objects
        that are hilited for component selection mode.  (e.g. when the user right clicks
        over a Mesh object and chooses the "vertex" option the Mesh line drawing changes
        color and the mesh is added to the hiliteList.)
        """
        pass

    @staticmethod
    def getLiveList(*args, **kwargs):
        """
        getLiveList() -> MSelectionList

        Returns a copy of the live list. When a user performs a
        "Modify->Make Live" in the user interface the currently selected
        objects are added to the live list.
        """
        pass

    @staticmethod
    def getPreselectionHiliteList(*args, **kwargs):
        """
        getPreselectionHiliteList() -> MSelectionList

        Gets the objects for which Maya is displaying a preselection
        highlight in the viewports.
        """
        pass

    @staticmethod
    def getRichSelection(*args, **kwargs):
        """
        getRichSelection(defaultToActiveSelection=True) -> MRichSelection

        Returns the current rich selection (usually the active selection with
        any soft selection and symmetry applied). If no rich selection exists
        and 'defaultToActiveSelection' is True, the current active selection
        will be returned instead.
        """
        pass

    @staticmethod
    def getSelectionListByName(*args, **kwargs):
        """
        getSelectionListByName(name) -> MSelectionList

        Returns an MSelectionList with all of the objects that match the
        specified name. The name may use the same type of regular expressions
        as can be used in MEL commands. For example, the pattern 'pCube*' will
        match all occurrences of objects whose names begin with 'pCube'.
        """
        pass

    @staticmethod
    def isRedoing(*args, **kwargs):
        """
        isRedoing() -> bool

        true if Maya is currently in the middle of a redo.
        """
        pass

    @staticmethod
    def isSelected(*args, **kwargs):
        """
        isSelected(MObject) -> bool

        Determines whether the given object is on the active selection list.
        """
        pass

    @staticmethod
    def isUndoing(*args, **kwargs):
        """
        isUndoing() -> bool

        true if Maya is currently in the middle of an undo.
        """
        pass

    @staticmethod
    def isYAxisUp(*args, **kwargs):
        """
        isYAxisUp() -> bool

        This method returns true if, currently, the Y-axis is UP.
        """
        pass

    @staticmethod
    def isZAxisUp(*args, **kwargs):
        """
        isZAxisUp() -> bool

        This method returns true if, currently, the Z-axis is UP.
        """
        pass

    @staticmethod
    def mayaState(*args, **kwargs):
        """
        mayaState() -> int

        Returns an enumerated type specifying the way in which Maya was invoked.
          kInteractive  Running with a UI
          kBatch  Running without a UI
          kLibraryApp  Running as a standalone (MLibrary) application.
          kBaseUIMode  Running with UI enabled but Maya's std UI scripts not run.
        """
        pass

    @staticmethod
    def mayaVersion(*args, **kwargs):
        """
        mayaVersion() -> string

        Returns a string describing this version of Maya.
        """
        pass

    @staticmethod
    def miscSelectionMask(*args, **kwargs):
        """
        miscSelectionMask() -> MSelectionMask

        Returns the miscellaneous selection mask.
        """
        pass

    @staticmethod
    def objectSelectionMask(*args, **kwargs):
        """
        objectSelectionMask() -> MSelectionMask

        Returns the object selection mask.
        """
        pass

    @staticmethod
    def optionVarDoubleValue(*args, **kwargs):
        """
        optionVarDoubleValue(string) -> double

        This method is used to get the option variable value of type double
        """
        pass

    @staticmethod
    def optionVarExists(*args, **kwargs):
        """
        optionVarExists(string) -> bool

        This method is used to check if the option variable exists
        """
        pass

    @staticmethod
    def optionVarIntValue(*args, **kwargs):
        """
        optionVarIntValue(string) -> int

        This method is used to get the option variable value of int type
        """
        pass

    @staticmethod
    def optionVarStringValue(*args, **kwargs):
        """
        optionVarStringValue(string) -> MString

        This method is used to get the option variable value of type string
        """
        pass

    @staticmethod
    def removeFromModel(*args, **kwargs):
        """
        removeFromModel(MObject) -> None

        Removes the specified dag node from the scene.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter
        will be returned.

        Note that this method doesn't delete the dag node which means
        the node must be added back to scene by calling either
        MGlobal::addToModel() or MGlobal::addToModelAt() in later
        calls, otherwise the dag node is leaked. To delete the dag node,
        call MGlobal::deleteNode() instead.
        """
        pass

    @staticmethod
    def removeOptionVar(*args, **kwargs):
        """
        removeOptionVar(string) -> None

        This method is used to remove the option variable
        """
        pass

    @staticmethod
    def resetToDefaultErrorLogPathName(*args, **kwargs):
        """
        resetToDefaultErrorLogPathName() -> None

        Closes the current log file if it is open, and then resets the log path to
        the default path.
        Logging is disabled and the log file speicified by the default path is not opened.
        If logging is disabled, it remains disabled.
        Use startErrorLogging() to enable logging to the default log file.
        If the current path is the default path, no action is taken,
        but an invalid parameter error is returned.

        Note that if the default log is reopened after it is closed, all information
        previously logged to it is lost.
        """
        pass

    @staticmethod
    def selectByName(*args, **kwargs):
        """
        selectByName(string, listAdjustment=kReplaceList) -> None

        Puts objects that match the give name on the active selection list.
        """
        pass

    @staticmethod
    def selectCommand(*args, **kwargs):
        """
        selectCommand(MSelectionList, listAdjustment=kReplaceList) -> None

        Set the active selection list, by calling the built in Maya select
        command.  This differs from setActiveSelectionList in that in this
        version Maya takes over the selection list you give it and will be
        responsible for maintaing the necessary information required for
        undo, redo, and journaling.
        """
        pass

    @staticmethod
    def selectFromScreen(*args, **kwargs):
        """
        selectFromScreen(short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None
        selectFromScreen(short, short, short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None

        Perform click-pick type selection on the dag. If an object intersects
        the click point then it is selected according to listAdjustment.
        """
        pass

    @staticmethod
    def selectionMethod(*args, **kwargs):
        """
        selectionMethod() -> int

        Determines the selection method that should be used in the currently active
        viewport.  This is useful as input to the "selectFromScreen" functions.
        """
        pass

    @staticmethod
    def selectionMode(*args, **kwargs):
        """
        selectionMode() -> int

        Get current selection mode:
          kSelectObjectMode     Objects are selected as a whole. Components are not directly accessible.
          kSelectComponentMode  Components such as vertices are selectable in this mode.
          kSelectRootMode       Selecting the child in a hierarchy will also select its root DAG node.
          kSelectLeafMode       Selecting the child in a hierarchy will result only in that child being selected.
          kSelectTemplateMode   Templated objects are selectable in this mode.
        """
        pass

    @staticmethod
    def setActiveSelectionList(*args, **kwargs):
        """
        setActiveSelectionList(MSelectionList, listAdjustment=kReplaceList) -> None

        Set the active selection list.
        The selection items on the given list will update the contents of the active selection
        list as indicated by the listAdjustment parameter.
        Valid listAdjustment values are:
          kReplaceList              #Totally replace the list with the given items.
          kXORWithList              #Any of the items which are already on the list will be removed.
                                #Any which are not already on the list will be added to the end
                                #of the list.
          kAddToList                    #Remove the items from the list.
          kAddToHeadOfList              #Add the items to the beginning of the list.
        """
        pass

    @staticmethod
    def setAnimSelectionMask(*args, **kwargs):
        """
        setAnimSelectionMask(mask) -> selfsetAnimSelectionMask(type) -> self

        Set the animation selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
        pass

    @staticmethod
    def setComponentSelectionMask(*args, **kwargs):
        """
        setComponentSelectionMask(mask) -> selfsetComponentSelectionMask(type) -> self

        Set the component selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
        pass

    @staticmethod
    def setDisableStow(*args, **kwargs):
        """
        setDisableStow(bool) -> None

        This method is used to make the visiblity of all Maya windows unchangable.
        If set to true, it disables any attempts to change the visiblity of any window.
        In addition, all popup windows will be supressed.
        """
        pass

    @staticmethod
    def setDisplayCVs(*args, **kwargs):
        """
        setDisplayCVs(MSelectionList, bool) -> None

        Controls drawing of control points in the specified selection list.

        The selection items on the given list will be marked for drawing. This
        overrides Maya's current draw list and allow, for example, the drawing
        of control points without being in vertex selection mode.
        """
        pass

    @staticmethod
    def setErrorLogPathName(*args, **kwargs):
        """
        setErrorLogPathName(string) -> None

        Determines the default path name of the error log file.
        Returns an empty string on failure.
        """
        pass

    @staticmethod
    def setHiliteList(*args, **kwargs):
        """
        setHiliteList(MSelectionList) -> None

        Sets the current hilite list. The current selection list is unchanged.
        """
        pass

    @staticmethod
    def setMiscSelectionMask(*args, **kwargs):
        """
        setMiscSelectionMask(mask) -> selfsetMiscSelectionMask(type) -> self

        Set the miscellaneous selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
        pass

    @staticmethod
    def setObjectSelectionMask(*args, **kwargs):
        """
        setObjectSelectionMask(mask) -> selfsetObjectSelectionMask(type) -> self

        Set the object selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
        pass

    @staticmethod
    def setOptionVarValue(*args, **kwargs):
        """
        setOptionVarValue(string, int) -> bool
        setOptionVarValue(string name, double) -> bool
        setOptionVarValue(string name, string) -> bool


        This method is used to set the option variable value of int, bool, string type
        """
        pass

    @staticmethod
    def setPreselectionHiliteList(*args, **kwargs):
        """
        setPreselectionHiliteList(MSelectionList) -> None

        Sets the objects for which Maya will display a preselection
        highlight in the viewports.

        The objects/components in the list will be drawn in Maya's
        preselection highlight style on the next viewport refresh
        (if preselection highlighting is enabled in the preferences).

        If preselection highlighting is not enabled, Maya will still
        store the list.
        """
        pass

    @staticmethod
    def setRichSelection(*args, **kwargs):
        """
        setRichSelection(MRichSelection) -> None

        Set the current rich selection.
        """
        pass

    @staticmethod
    def setSelectionMode(*args, **kwargs):
        """
        setSelectionMode(int) -> None

        Set the current selection mode.
        See selectionMode() for a list of valid modes.
        """
        pass

    @staticmethod
    def setTrackSelectionOrderEnabled(*args, **kwargs):
        """
        setTrackSelectionOrderEnabled() -> None

        Set whether Maya should maintain an active selection list which
        maintains object and component selection order.
        """
        pass

    @staticmethod
    def setYAxisUp(*args, **kwargs):
        """
        setYAxisUp() -> None

        This method sets the flag to identify which axis is Up, and
        rotates the ground plane around around the X-axis 90 degrees to get
        the Y-Up from Z-Up.
        """
        pass

    @staticmethod
    def setZAxisUp(*args, **kwargs):
        """
        setZAxisUp() -> None

        This method sets the flag to identify which axis is Up, and
        rotates the ground plane around around the X-axis 90 degrees to get
        the Y-Up from Y-Up.
        """
        pass

    @staticmethod
    def sourceFile(*args, **kwargs):
        """
        sourceFile(string) -> None

        Causes the MEL command engine to open the named file and execute
        the contents of the file as a MEL script.  If the provided fileName
        is a Unix absolute pathname, then that file is opened.  If a relative
        pathname is provided, the directories indicated by the environment
        variable, MAYA_SCRIPT_PATH, will be searched for a matching filename.
        """
        pass

    @staticmethod
    def startErrorLogging(*args, **kwargs):
        """
        startErrorLogging() -> None
        startErrorLogging(string)

        This method enables output to the API error log file specified by the path.
        If another error log file is already open this method time and date stamps
        the log, and closes it.
        The new error log is time and date stamped when it is opened.

        If the new path name is the same as the current path name, this method ensures
        that logging is enabled, but no other action is taken.
        """
        pass

    @staticmethod
    def stopErrorLogging(*args, **kwargs):
        """
        stopErrorLogging() -> None

        This method disables output to the API error log but does not close the log file.
        """
        pass

    @staticmethod
    def trackSelectionOrderEnabled(*args, **kwargs):
        """
        trackSelectionOrderEnabled() -> bool

        Returns whether the selection order is currerntly being tracked.
        """
        pass

    @staticmethod
    def unselect(*args, **kwargs):
        """
        unselect(MObject) -> None
        unselect(MDagPath, MObject) -> None

        Remove the given object/components from the active selection list.
        If components is null then the object will be unselected, otherwise
        the components will be unselected.

        Perform marquee type selection on the dag.  If an object intersects the
        selection rectangle, it is selected according to listAdjustment.
        """
        pass

    @staticmethod
    def unselectByName(*args, **kwargs):
        """
        unselectByName(string) -> None

        Removes objects matching the pattern from the active selection list.
        """
        pass

    @staticmethod
    def upAxis(*args, **kwargs):
        """
        upAxis() -> MVector

        This method returns the model's current up axis.
        """
        pass

    @staticmethod
    def viewFrame(*args, **kwargs):
        """
        viewFrame(double) -> None
        viewFrame(MTime) -> None

        Sets the global time to the specified time.  This function is optimized
        for sequential time values that are monotonically increasing.  While
        one can set the time randomly with this function, a significant
        performance hit will be incurred.
        """
        pass

    kAddToHeadOfList = 4

    kAddToList = 2

    kBaseUIMode = 3

    kBatch = 1

    kInteractive = 0

    kLibraryApp = 2

    kRemoveFromList = 3

    kReplaceList = 0

    kSelectComponentMode = 1

    kSelectLeafMode = 3

    kSelectObjectMode = 0

    kSelectRootMode = 2

    kSelectTemplateMode = 4

    kSurfaceSelectMethod = 0

    kWireframeSelectMethod = 1

    kXORWithList = 1


class MWeight(object):
    """
    Methods for accessing component weight data. This class is currently
    only used to access soft select and symmetry selection weights.
    Other weight data (e.g. deformer weights) does not use this class
    and can be accessed through the corresponding MFn class or directly
    from the node's attributes.

    __init__()
    Initializes a new MWeight object with influence weight of 1 and seam
    weight of 0.
    __init__(MWeight src)
    Initializes a new MWeight object with the same value as src.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    influence = None

    seam = None


class MPlane(object):
    """
    This class describes a mathematical plane.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def distance(*args, **kwargs):
        """
        distance() -> float

        Returns the distance of the plane along the normal.
        """
        pass

    def distanceToPoint(*args, **kwargs):
        """
        distanceToPoint(point, signed=False) -> float

        Returns the distance from the plane to the specified point.

        * point (MVector) - The point from which to calculate the distance
        * signed (bool) - Whether to return a signed or unsigned distance
        """
        pass

    def normal(*args, **kwargs):
        """
        normal() -> MVector

        Returns the normal of the plane.
        """
        pass

    def setPlane(*args, **kwargs):
        """
        setPlane(a, b, c, d) -> self
        setPlane(n, d) -> self

        Set the equation of the plane.

        From values : ax + by + cz + d = 0
        * a (float) - The plane equation's x coefficent
        * b (float) - The plane equation's y coefficent
        * c (float) - The plane equation's z coefficent
        * d (float) - The plane equation's constant distance term

        From a normal and offset
        * n (MVector) - The plane's normal
        * d (float) - The offset of the plane along the normal
        """
        pass


class MSyntax(object):
    """
    Syntax for commands.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addArg(*args, **kwargs):
        """
        Add a command argument.
        """
        pass

    def addFlag(*args, **kwargs):
        """
        Add a flag and its arguments.
        """
        pass

    def makeFlagMultiUse(*args, **kwargs):
        """
        Set whether a flag may be used multiple times on the command line.
        """
        pass

    def makeFlagQueryWithFullArgs(*args, **kwargs):
        """
        Set whether a flag requires its args when queried.
        """
        pass

    def maxObjects(*args, **kwargs):
        """
        Returns the maximum number of objects which can be passed to the command.
        """
        pass

    def minObjects(*args, **kwargs):
        """
        Returns the minimum number of objects which can be passed to the command.
        """
        pass

    def setMaxObjects(*args, **kwargs):
        """
        Sets the maximum number of objects which can be passed to the command.
        """
        pass

    def setMinObjects(*args, **kwargs):
        """
        Sets the minimum number of objects which can be passed to the command.
        """
        pass

    def setObjectType(*args, **kwargs):
        """
        Set the type and number of objects to be passed to the command.
        """
        pass

    def useSelectionAsDefault(*args, **kwargs):
        """
        If set to True then when no objects are provided on the command-line Maya will pass the current selection instead.
        """
        pass

    enableEdit = None

    enableQuery = None

    kAngle = 8

    kBoolean = 2

    kDistance = 7

    kDouble = 4

    kInvalidArgType = 0

    kInvalidObjectFormat = 0

    kLastArgType = 11

    kLastObjectFormat = 4

    kLong = 3

    kNoArg = 1

    kNone = 1

    kSelectionItem = 10

    kSelectionList = 3

    kString = 5

    kStringObjects = 2

    kTime = 9

    kUnsigned = 6


class MArgParser(object):
    """
    Command argument list parser.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def commandArgumentBool(*args, **kwargs):
        """
        commandArgumentBool(argIndex) -> bool

        Returns the specified command argument as a bool.
        """
        pass

    def commandArgumentDouble(*args, **kwargs):
        """
        Alias for commandArgumentFloat().
        """
        pass

    def commandArgumentFloat(*args, **kwargs):
        """
        commandArgumentFloat(argIndex) -> float

        Returns the specified command argument as a float.
        """
        pass

    def commandArgumentInt(*args, **kwargs):
        """
        commandArgumentInt(argIndex) -> int

        Returns the specified command argument as an int.
        """
        pass

    def commandArgumentMAngle(*args, **kwargs):
        """
        commandArgumentMAngle(argIndex) -> MAngle

        Returns the specified command argument as an MAngle.
        """
        pass

    def commandArgumentMDistance(*args, **kwargs):
        """
        commandArgumentMDistance(argIndex) -> MDistance

        Returns the specified command argument as an MDistance.
        """
        pass

    def commandArgumentMTime(*args, **kwargs):
        """
        commandArgumentMTime(argIndex) -> MTime

        Returns the specified command argument as an MTime.
        """
        pass

    def commandArgumentString(*args, **kwargs):
        """
        commandArgumentString(argIndex) -> unicode string

        Returns the specified command argument as a string.
        """
        pass

    def flagArgumentBool(*args, **kwargs):
        """
        flagArgumentBool(flagName, argIndex) -> bool

        Returns the specified argument of the specified single-use flag as
        a bool.
        """
        pass

    def flagArgumentDouble(*args, **kwargs):
        """
        flagArgumentDouble(flagName, argIndex) -> float

        Alias for flagArgumentFloat().
        """
        pass

    def flagArgumentFloat(*args, **kwargs):
        """
        flagArgumentFloat(flagName, argIndex) -> float

        Returns the specified argument of the specified single-use flag as
        a float.
        """
        pass

    def flagArgumentInt(*args, **kwargs):
        """
        flagArgumentInt(flagName, argIndex) -> int

        Returns the specified argument of the specified single-use flag as
        an int.
        """
        pass

    def flagArgumentMAngle(*args, **kwargs):
        """
        flagArgumentMAngle(flagName, argIndex) -> MAngle

        Returns the specified argument of the specified single-use flag as
        an MAngle.
        """
        pass

    def flagArgumentMDistance(*args, **kwargs):
        """
        flagArgumentMDistance(flagName, argIndex) -> MDistance

        Returns the specified argument of the specified single-use flag as
        an MDistance.
        """
        pass

    def flagArgumentMTime(*args, **kwargs):
        """
        flagArgumentMTime(flagName, argIndex) -> MTime

        Returns the specified argument of the specified single-use flag as
        an MTime.
        """
        pass

    def flagArgumentString(*args, **kwargs):
        """
        flagArgumentString(flagName, argIndex) -> string

        Returns the specified argument of the specified single-use flag as
        a string.
        """
        pass

    def getFlagArgumentList(*args, **kwargs):
        """
        getFlagArgumentList(flagName, occurrence) -> MArgList

        Returns the arguments for the specified occurrence of the given
        multi-use flag as an MArgList. Raises RuntimeError if the flag has
        not been enabled for multi-use. Raises IndexError if occurrence is
        out of range.
        """
        pass

    def getFlagArgumentPosition(*args, **kwargs):
        """
        getFlagArgumentPosition(flagName, occurrence) -> int

        Returns the position in the argument list of the specified occurrence
        of the given flag. Raises IndexError if occurrence is out of range.
        """
        pass

    def getObjectStrings(*args, **kwargs):
        """
        getObjectStrings() -> tuple of unicode strings

        If the command's MSyntax has set the object format to kStringObjects
        then this method will return the objects passed to the command as a
        tuple of strings. If any other object format is set then an empty
        tuple will be returned.
        """
        pass

    def isFlagSet(*args, **kwargs):
        """
        isFlagSet(flagName) -> bool

        Returns True if the given flag appears on the command line.
        """
        pass

    def numberOfFlagUses(*args, **kwargs):
        """
        numberOfFlagUses(flagName) -> int

        Returns the number of times that the flag appears on the command
        line.
        """
        pass

    isEdit = None

    isQuery = None

    numberOfFlagsUsed = None


class MExternalContentLocationTable(object):
    """
    This is a table of the all the external content locations for a given node.
    """

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def addEntry(*args, **kwargs):
        """
        addEntry(key, location) -> self

        Adds an external content location and its key to the table.

        * key (string) - An arbitrary string defined by the node. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.* location (string) - Full path to the content referenced by the key.
        """
        pass

    def getEntry(*args, **kwargs):
        """
        getEntry(index) -> [key, location]

        Retrieves external content entry based on its position in the table.

        * index (unsigned int) - Position of the entry to retrieve information from.
        """
        pass

    def getLocation(*args, **kwargs):
        """
        getLocation(key) -> string

        Retrieves an entry's location based on the associated key.

        * key (string) - See documentation of MExternalContentLocationTable.addEntry().
        """
        pass


class _MVectorMeta(type):

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls.kTolerance = 1e-10
        cls.kXaxis = 0
        cls.kYaxis = 1
        cls.kZaxis = 2
        cls.kWaxis = 3
        cls.kZeroVector = cls(0.0, 0.0, 0.0)
        cls.kOneVector = cls(1.0, 1.0, 1.0)
        cls.kXaxisVector = cls(1.0, 0.0, 0.0)
        cls.kXnegAxisVector = cls(-1.0, 0.0, 0.0)
        cls.kYaxisVector = cls(0.0, 1.0, 0.0)
        cls.kYnegAxisVector = cls(0.0, -1.0, 0.0)
        cls.kZaxisVector = cls(0.0, 0.0, 1.0)
        cls.kZnegAxisVector = cls(0.0, 0.0, -1.0)

class MVector(metaclass=_MVectorMeta):
    """
    3D vector with double-precision coordinates.
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return MVector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __delitem__(self, index):
        if index == 0:
            self.x = 0.0
        elif index == 1:
            self.y = 0.0
        elif index == 2:
            self.z = 0.0
        else:
            raise IndexError("Index out of range")

    def __div__(self, scalar):
        return MVector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __eq__(self, other):
        return (abs(self.x - other.x) < MVector.kTolerance and
                abs(self.y - other.y) < MVector.kTolerance and
                abs(self.z - other.z) < MVector.kTolerance)

    def __ge__(self, other):
        return self.length() >= other.length()

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __gt__(self, other):
        return self.length() > other.length()

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __idiv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __le__(self, other):
        return self.length() <= other.length()

    def __len__(self):
        return 3

    def __lt__(self, other):
        return self.length() < other.length()

    def __mul__(self, other: Union[float, int, 'MVector']) -> 'MVector':
        if isinstance(other, (int, float)):  # Scalar multiplication
            return MVector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, MVector):  # Dot product
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'MVector' and '{type(other).__name__}'")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __neg__(self):
        return MVector(-self.x, -self.y, -self.z)

    def __radd__(self, other):
        return self.__add__(other)

    def __rdiv__(self, scalar):
        return MVector(scalar / self.x, scalar / self.y, scalar / self.z)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Division not supported between MVector and {type(scalar)}")
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return MVector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __repr__(self):
        return f'MVector({self.x}, {self.y}, {self.z})'

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __rsub__(self, other):
        return MVector(other.x - self.x, other.y - self.y, other.z - self.z)

    def __rxor__(self, other):
        return self.__xor__(other)

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __sub__(self, other):
        if not isinstance(other, MVector):
            raise TypeError(f"Subtraction not supported between MVector and {type(other).__name__}")
        return MVector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __xor__(self, other):
        return MVector(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def angle(self, other):
        dot_product = self.x * other.x + self.y * other.y + self.z * other.z
        lengths_product = self.length() * other.length()
        return math.acos(dot_product / lengths_product)

    def isEquivalent(self, other, tolerance=1e-10):
        return (abs(self.x - other.x) < tolerance and
                abs(self.y - other.y) < tolerance and
                abs(self.z - other.z) < tolerance)

    def isParallel(self, other, tolerance=1e-10):
        cross_product = self.__xor__(other)
        return cross_product.length() < tolerance

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        length = self.length()
        if length == 0:
            return MVector()
        return self / length

    def normalize(self):
        length = self.length()
        if length == 0:
            return self
        self.x /= length
        self.y /= length
        self.z /= length
        return self

    def rotateBy(self, quaternion):
        # Simplified rotation by quaternion
        return self

    def rotateTo(self, other):
        # Simplified rotation to another vector
        return MQuaternion()

    def transformAsNormal(self, matrix):
        # Simplified transformation as normal
        return self

class MBoundingBox(object):
    """
    3D axis-aligned bounding box.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

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

    def clear(self, *args, **kwargs):
        """
        Empties the bounding box, setting its corners to (0, 0, 0).
        """
        pass

    def contains(self, *args, **kwargs):
        """
        Returns True if a point lies within the bounding box.
        """
        pass

    def expand(self, *args, **kwargs):
        """
        Expands the bounding box to include a point or other bounding box.
        """
        pass

    def intersects(self, *args, **kwargs):
        """
        Returns True if any part of a given bounding box lies within this one.
        """
        pass

    def transformUsing(self, *args, **kwargs):
        """
        Multiplies the bounding box's corners by a matrix.
        """
        pass

    center = None

    depth = None

    height = None

    max = None

    min = None

    width = None


class MVectorArray(object):
    """
    Array of MVector values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MPxCommand(object):
    """
    Base class for custom commands.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def doIt(*args, **kwargs):
        """
        Called by Maya to execute the command.
        """
        pass

    def hasSyntax(*args, **kwargs):
        """
        Called by Maya to determine if the command provides an MSyntax object describing its syntax.
        """
        pass

    def isUndoable(*args, **kwargs):
        """
        Called by Maya to determine if the command supports undo.
        """
        pass

    def redoIt(*args, **kwargs):
        """
        Called by Maya to redo a previously undone command.
        """
        pass

    def syntax(*args, **kwargs):
        """
        Returns the command's MSyntax object, if it has one.
        """
        pass

    def undoIt(*args, **kwargs):
        """
        Called by Maya to undo a previously executed command.
        """
        pass

    @staticmethod
    def appendToResult(*args, **kwargs):
        """
        Append a value to the result to be returned by the command.
        """
        pass

    @staticmethod
    def clearResult(*args, **kwargs):
        """
        Clears the command's result.
        """
        pass

    @staticmethod
    def currentResult(*args, **kwargs):
        """
        Returns the command's current result.
        """
        pass

    @staticmethod
    def currentResultType(*args, **kwargs):
        """
        Returns the type of the current result.
        """
        pass

    @staticmethod
    def displayError(*args, **kwargs):
        """
        Display an error message.
        """
        pass

    @staticmethod
    def displayInfo(*args, **kwargs):
        """
        Display an informational message.
        """
        pass

    @staticmethod
    def displayWarning(*args, **kwargs):
        """
        Display a warning message.
        """
        pass

    @staticmethod
    def isCurrentResultArray(*args, **kwargs):
        """
        Returns true if the command's current result is an array of values.
        """
        pass

    @staticmethod
    def setResult(*args, **kwargs):
        """
        Set the value of the result to be returned by the command.
        """
        pass

    commandString = None

    historyOn = None

    kDouble = 1

    kLong = 0

    kNoArg = 3

    kString = 2


class MDistance(object):
    """
    Manipulate distance data.
    """

    _UNIT_CONST_TO_NAME = {
        6 : 'kCentimeters',
        2 : 'kFeet',
        1 : 'kInches',
        0 : 'kInvalid',
        7 : 'kKilometers',
        9 : 'kLast',
        8 : 'kMeters',
        4 : 'kMiles',
        5 : 'kMillimeters',
        3 : 'kYards',
    }

    _FROM_CENTIMETERS = {
        6: 1,
        2: 1 / 30.48,
        1: 1 / 2.54,
        7: 1 / 100000,
        8: 1 / 100,
        4: 1 / 160934,
        5: 10,
        3: 1 / 91.44,
    }

    # Conversion factors to centimeters from other units
    _TO_CENTIMETERS = {unit: 1 / factor for unit, factor in _FROM_CENTIMETERS.items()}


    def __init__(self, value: float = None, unit: int = None, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._unit = unit or MDistance.kCentimeters
        self._value = value or random.uniform(-100, 100)

    def __repr__(self):
        """
        x.__repr__() <==> repr(x)
        """
        return f'MDistance: <{self._value} {type(self)._UNIT_CONST_TO_NAME[self._unit]}>'

    def __str__(self):
        """
        x.__str__() <==> str(x)
        """
        return f'{self._value} {type(self)._UNIT_CONST_TO_NAME[self._unit]}'

    def asCentimeters(self) -> float:
        """
        Return the distance value, converted to centimeters.
        """
        return self._value / MDistance._FROM_CENTIMETERS[self._unit]

    def asFeet(self) -> float:
        """
        Return the distance value, converted to feet.
        """
        return self.asUnits(MDistance.kFeet)

    def asInches(self) -> float:
        """
        Return the distance value, converted to inches.
        """
        return self.asUnits(MDistance.kInches)

    def asKilometers(self) -> float:
        """
        Return the distance value, converted to kilometers.
        """
        return self.asUnits(MDistance.kKilometers)

    def asMeters(self) -> float:
        """
        Return the distance value, converted to meters.
        """
        return self.asUnits(MDistance.kMeters)

    def asMiles(self) -> float:
        """
        Return the distance value, converted to miles.
        """
        return self.asUnits(MDistance.kMiles)

    def asMillimeters(self) -> float:
        """
        Return the distance value, converted to millimeters.
        """
        return self.asUnits(MDistance.kMillimeters)

    def asUnits(self, unit=6) -> float:
        """
        Return the distance value, converted to the specified units.
        """

        value_in_cm = self.asCentimeters()
        return value_in_cm * MDistance._FROM_CENTIMETERS[unit]

    def asYards(self) -> float:
        """
        Return the distance value, converted to yards.
        """
        return self.asUnits(MDistance.kYards)

    @staticmethod
    def internalToUI(*args, **kwargs):
        """
        Convert a value from Maya's internal units to the units used in the UI.
        """
        pass

    @staticmethod
    def internalUnit(*args, **kwargs):
        """
        Return the distance unit used internally by Maya.
        """
        pass

    @staticmethod
    def setUIUnit(*args, **kwargs):
        """
        Change the units used to display distances in Maya's UI.
        """
        pass

    @staticmethod
    def uiToInternal(*args, **kwargs):
        """
        Convert a value from the units used in the UI to Maya's internal units.
        """
        pass

    @staticmethod
    def uiUnit(*args, **kwargs):
        """
        Return the units used to display distances in Maya's UI.
        """
        pass

    kCentimeters = 6

    kFeet = 2

    kInches = 1

    kInvalid = 0

    kKilometers = 7

    kLast = 9

    kMeters = 8

    kMiles = 4

    kMillimeters = 5

    kYards = 3

    @property
    def unit(self):
        return self._unit

    @property
    def value(self):
        return self._value


class MFloatPoint(object):
    """
    3D point with single-precision coordinates.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __div__(*args, **kwargs):
        """
        x.__div__(y) <==> x/y
        """
        pass

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __isub__(*args, **kwargs):
        """
        x.__isub__(y) <==> x-=y
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __radd__(*args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __rdiv__(*args, **kwargs):
        """
        x.__rdiv__(y) <==> y/x
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(*args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def __sub__(*args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def cartesianize(*args, **kwargs):
        """
        Convert point to cartesian form.
        """
        pass

    def distanceTo(*args, **kwargs):
        """
        Return distance between this point and another.
        """
        pass

    def homogenize(*args, **kwargs):
        """
        Convert point to homogenous form.
        """
        pass

    def isEquivalent(*args, **kwargs):
        """
        Test for equivalence of two points, within a tolerance.
        """
        pass

    def rationalize(*args, **kwargs):
        """
        Convert point to rational form.
        """
        pass

    kOrigin = None

    kTolerance = 9.999999747378752e-06

    w = None

    x = None

    y = None

    z = None


class MItSurfaceCV(object):
    """
    NURBS surface CV iterator.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def currentItem(*args, **kwargs):
        """
        currentItem() -> MObject

        Get the current CV in the iteration as a component.

        Components are used to specify one or more CVs and are useful in operating on groups of non-contiguous CVs for a curve or surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
        pass

    def hasHistoryOnCreate(*args, **kwargs):
        """
        hasHistoryOnCreate() -> bool

        This method determines if the shape was created with history.

        If the object that this iterator is attached to is not a shape then this method will raise.
        """
        pass

    def index(*args, **kwargs):
        """
        index() -> int

        Get the index of the current CV as it appears in CV array for this surface.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Returns True if the iteration is finished, i.e. there are no more CVs to iterate on.
        """
        pass

    def isRowDone(*args, **kwargs):
        """
        isRowDone() -> bool

        Returns True if the current row has no more CVs to iterate over.
        The row can be in the U or V direction depending on what value of useURows has been set in the constructor.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advance to the next CV in the iteration.
        If the iterator is already at the last CV then this method has no effect. Use isDone() to determine if the iterator is at the last CV.
        """
        pass

    def nextRow(*args, **kwargs):
        """
        nextRow() -> self

        Advance to the next row in the iteration.
        The row can be in the U or V direction depending on what value of useURows has been set in the constructor.
        """
        pass

    def position(*args, **kwargs):
        """
        position(space=kObject) -> MPoint

        Returns the position of the current CV in the iteration in the specified space.

        * space (int) - The coordinate space in which the CV is set
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(surface, useURows=True) -> self
        reset(surface, component, useURows=True) -> self

        Reset the iterator to the first CV.

        Or
        Reset the iterator to iterate over all CVs on the specified surface.

        * surface (MObject) - The surface for the iteration
        * useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.

        Or
        Reset the iterator to iterate over the CVs of the given surface that are specified in the given component. If the component is NULL then the iteration will be over all CVs on the surface.

        * surface (MDagPath) - The surface for the iteration
        * component (MObject) - A group of CVs to be iterated on
        * useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.
        """
        pass

    def setPosition(*args, **kwargs):
        """
        setPosition(point, space=kObject) -> self

        Set the position of the current CV in the iteration to the specified point.

        * point (MPoint) - The new position for the current CV in the iteration
        * space (int) - The coordinate space in which the CV is set
        """
        pass

    def translateBy(*args, **kwargs):
        """
        translateBy(vector, space=kObject) -> self

        Move the current CV in the iteration by the sepcified vector.

        * vector (MVector) - The translation vector
        * space (int) - The coordinate space in which the CV is set
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        This method is used to signal the surface that it has been changed and needs to redraw itself.

        When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified.
        """
        pass

    def uvIndices(*args, **kwargs):
        """
        uvIndices() -> (indexU, indexV)

        Get the u and v index of the current CV.
        """
        pass


class MArrayDataBuilder(object):
    """
    Array builder for arrays in data blocks.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def addElement(*args, **kwargs):
        """
        addElement(index) -> MDataHandle

        Adds a new element to the array at the given index.

        * index (int) - the index at which we wish to add the new element

        Returns The handle for the new element
        """
        pass

    def addElementArray(*args, **kwargs):
        """
        addElementArray(index) -> MArrayDataHandle

        Adds a new element to the array at the given index.  The added element is also an array.

        * index (int) - the index at which we wish to add the new element

        Returns The handle for the new array element
        """
        pass

    def addLast(*args, **kwargs):
        """
        addLast() -> MDataHandle

        Adds a new element to the end of the array.  The index of the element will be the current highest index + 1.

        Returns The handle for the new element
        """
        pass

    def addLastArray(*args, **kwargs):
        """
        addLastArray() -> MArrayDataHandle

        Adds a new element to the end of the array.  The added element is also an array.  The index of the element will the current highest index + 1.

        Returns The handle for the new array element
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source builder.

        * source (MArrayDataBuilder) - The source object to copy from
        """
        pass

    def growArray(*args, **kwargs):
        """
        growArray(amount) -> self

        Grows the array storage by the given amount.

        * amount (int) - the amount to grow the array by
        """
        pass

    def removeElement(*args, **kwargs):
        """
        removeElement(index) -> self

        Removes the specified element from the array

        * index (int) - the element of the array to remove
        """
        pass

    def setGrowSize(*args, **kwargs):
        """
        setGrowSize(size) -> self

        Sets the grow size of the array.  As elements are added to the array, the builder will allocate memory in chunks.  This method tells the builder how many elements to allocate each time it grows the array.

        * size (int) - the number of elements to allocate when growing the array
        """
        pass


class MPxNode(object):
    """
    Base class for user defined dependency nodes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addExternalContentForFileAttr(*args, **kwargs):
        """
        addExternalContentForFileAttr(table, attr) -> bool

        This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute.

        The method will not overwrite existing items, i.e. items with the same key. (attribute name).  In this context, overwriting an item means the caller has called this function twice with the same attribute, or that two separate but identically named attributes were used.  If replacing an entry is the desired effect, it is the caller's responsibility to erase the previous item first.

        * table [OUT] (MExternalContentInfoTable) - table The table in which the new entry will be added.
        * attr (MObject) - The attribute for which the plug value will be queried for a location.

        Returns True if an item was sucessfully added to the table.  False if the attribute does not describe a non-empty location, or an item with the same key was already present in the table.
        """
        pass

    def compute(*args, **kwargs):
        """
        compute(plug, dataBlock) -> self

        This method should be overridden in user defined nodes.

        Recompute the given output based on the nodes inputs.  The plug represents the data value that needs to be recomputed, and the data block holds the storage for all of the node's attributes.

        The MDataBlock will provide smart handles for reading and writing this node's attribute values.  Only these values should be used when performing computations.

        When evaluating the dependency graph, Maya will first call the compute method for this node.  If the plug that is provided to the compute indicates that that the attribute was defined by the Maya parent node, the compute method should return None.  When this occurs, Maya will call the internal Maya node from which the user-defined node is derived to compute the plug's value. Returning any othervalue (including self) will tell Maya that this node successfully computed theplug. Raising an exception will tell Maya that this node failed at computingthe plug. Note that in most cases, Maya ignores node compute failures.

        In other words, the compute method should return None to get the Maya parent class to compute the plug. It should return self (or any other value) to indicate that the plug was computed successfully.

        This means that a user defined node does not need to be concerned with computing inherited output attributes.  However, if desired, these can be safely recomputed by this method to change the behaviour of the node.

        * plug (MPlug) - plug representing the attribute that needs to be recomputed.
        * block (MDataBlock) - data block containing storage for the node's attributes.
        """
        pass

    def connectionBroken(*args, **kwargs):
        """
        connectionBroken( plug, otherPlug, asSrc) -> self

        This method gets called when connections are broken with attributes of this node.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """
        pass

    def connectionMade(*args, **kwargs):
        """
        connectionMade(plug, otherPlug, asSrc) -> self

        This method gets called when connections are made to attributes of this node.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """
        pass

    def copyInternalData(*args, **kwargs):
        """
        copyInternalData(node) -> self

        This method is overriden by nodes that store attribute data in some internal format.

        On duplication this method is called on the duplicated node with the node being duplicated passed as the parameter.  Overriding this method gives your node a chance to duplicate any internal data you've been storing and manipulating outside of normal attribute data.

        * node (MPxNode) - the node that is being duplicated.
        """
        pass

    def dependsOn(*args, **kwargs):
        """
        dependsOn( plug, otherPlug) -> bool/None

        This method may be overridden by the user defined node. It should only be required to override this on rare occasions.

        This method determines whether a specific attribute depends on another attribute.

        You should return None to specify that Maya should determines the dependency (default).

        This is mainly to define dependency of dynamic attributes, since attributeAffects does not work with dynamic attributes.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        """
        pass

    def doNotWrite(*args, **kwargs):
        """
        doNotWrite() -> bool

        use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out.
        """
        pass

    def forceCache(*args, **kwargs):
        """
        forceCache(ctx=MDGContext::current()) -> MDataBlock

        Get the datablock for this node. If there is no datablock then one will be created.
        NOTE: This should be used only in places where fast access to the datablock outside of a compute is critical such as the transformUsing method of MPxSurfaceShape.

        * ctx (MDGContext) - The context in which the datablock will be retrieved.
        """
        pass

    def getExternalContent(*args, **kwargs):
        """
        getExternalContent(table) -> self

        The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details.

        Keys used to add items to this table will be the same that get passed to setExternalContent through its MExternalContentLocationTable parameter to perform a batched change of content location.

        When implementing getExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also add their external content to the table.

        The default implementation does nothing.

        * table [OUT] (MExternalContentInfoTable) - Content information table that this method must populate.
        """
        pass

    def getFilesToArchive(*args, **kwargs):
        """
        getFilesToArchive(shortName=False, unresolvedName=False, markCouldBeImageSequence=False) -> list of strings

        Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command.

        Only include files that exist.

        If shortName is True, return just the filename portion of the path. Otherwise, return a full path.

        If unresolvedName is True, return the path before any resolution has been done (i.e leave it as a relative path, include unexpanded environment variables,  tildes, ".."s etc). Otherwise, resolve the file     path and return an absolute path (to resolve with standard Maya path resolution, use MFileObject.resolvedFullName()).

        * shortName (bool) - If True, only add the filename of the path.
        * unresolvedName (bool) - If True, add paths before any resolution, rather than absolute paths.
        * markCouldBeImageSequence (bool) - If True, append an asterisk after any file path that could be an image sequence (note: only used by maya.exe -archive).
        """
        pass

    def getInternalValue(*args, **kwargs):
        """
        getInternalValue(plug, dataHandle) -> bool

        This method is overridden by nodes that store attribute data in some internal format.

        The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

        When internal attribute values are queried via getAttr or MPlug.getValue() this method is called.

        All internal data should respect the current context, which may be obtained from MDGContext::current()

        * plug (MPlug) - the attribute that is being queried.
        * dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
        """
        pass

    def getInternalValueInContext(*args, **kwargs):
        """
        getInternalValueInContext(plug, dataHandle, ctx) -> bool [OBSOLETE]

        This method is obsolete. Override MPxNode.getInternalValue instead.

        * plug (MPlug) - the attribute that is being queried.
        * dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
        * ctx (MDGContext) - the context the method is being evaluated in.
        """
        pass

    def internalArrayCount(*args, **kwargs):
        """
        internalArrayCount(plug) -> int
        internalArrayCount(plug, ctx) -> int  [OBSOLETE]

        This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock. This method is used by Maya to determine the non-sparse count of array elements during file IO. If the internal array is stored sparsely, you should return the maximum index of the array plus one. If the internal array is non-sparse then return the length of the array.

        This method does not need to be implemented for attributes that are stored in the datablock since Maya will use the datablock size.

        If this method is overridden, it should return -1 for attributes which it does not handle. Maya will use the datablock size to determine the array length when -1 is returned.

        All internal data should respect the current context, which may be obtained from MDGContext.current()

        * plug (MPlug) - the array plug.
        * ctx (MDGContext) - the context, default to MDGContext.current().
        """
        pass

    def isAbstractClass(*args, **kwargs):
        """
        isAbstractClass() -> bool

        Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command.

        It is not necessary to override this method.
        """
        pass

    def isPassiveOutput(*args, **kwargs):
        """
        isPassiveOutput(plug) -> bool

        This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user.

        * plug (MPlug) - plug representing output in question.
        """
        pass

    def legalConnection(*args, **kwargs):
        """
        legalConnection(plug, otherPlug, asSrc) -> bool/None

        This method allows you to check for legal connections being made to attributes of this node.

        You should return None to specify that maya should handle this connection if you are unable to determine if it is legal.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """
        pass

    def legalDisconnection(*args, **kwargs):
        """
        legalDisconnection(plug, otherPlug, arsSrc) -> bool/None

        This method allows you to check for legal disconnections being made to attributes of this node.

        You should return None to specify that maya should handle this disconnection if you are unable to determine if it is legal.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (boool) - is this plug a source of the connection.
        """
        pass

    def name(*args, **kwargs):
        """
        name() -> string

        Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL.

        It is not necessary to override this method.

        Returns the name of the node
        """
        pass

    def passThroughToMany(*args, **kwargs):
        """
        passThroughToMany(plug, plugArray) -> bool

        This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes.

        If this method is not implemented or returns False, the base class Maya implementation of this method calls passThroughToOne and returns the results of that call.

        * plug (MPlug) - the plug.
        * plugArray (MPlugArray) - the corresponding plugs.
        """
        pass

    def passThroughToOne(*args, **kwargs):
        """
        passThroughToOne(plug) -> plug

        This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:

        - When this node is deleted, the delete command will rewire the source of the input attribute to the destination of the output attribute if the source and destination are connected to nodes that are not deleted.
        - History traversal algorithms such as the bakePartialHistory command use this method to direct its traversal through a shape's construction history.
        - The base class Maya implementation of passThroughToAll will call this method if passThroughToAll returns False.

        * plug (MPlug) - the plug.
        """
        pass

    def postConstructor(*args, **kwargs):
        """
        postConstructor() -> self

        Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object.
        The association between the these two objects is not made until after the MPxNode constructor is called. This implies that no MPxNode member function can be called from the MPxNode constructor.
        The postConstructor will get called immediately after the constructor when it is safe to call any MPxNode member function.
        """
        pass

    def postEvaluation(*args, **kwargs):
        """
        postEvaluation(context, evalNode, evalType) -> None

        Clean up node's internal state after threaded evaluation.

        After the evaluation graph execution, each node gets a chance to restore / update its internal states.For example, resetting draw state.

        This code has to be thread safe, non - blocking and work only on data owned by the node.

        This call will most likely happen from a worker thread.

        * context (MDGContext) - Context in which the evaluation is happening.
                                 This should be respected and only internal state
                                 information pertaining to it should be modified.
        * evaluationNode (MEvaluationNode) - Evaluation node which contains
                                             information about the dirty plugs the
                                             dirty plugs that were evaluated for this
                                             context.
        * evalType (PostEvaluationType)
          * kEvaluatedIndirectly : The node's compute function handled evaluation.
          * kEvaluatedDirectly   : Evaluation was performed externally and the results injected
                                   back into the node.  This would happen in situations such as
                                   extracting values from an external cache.The node needs to
                                   update any additional internal state based on the new values.
          * kLeaveDirty          : Evaluation was performed without updating this node. Internal
                                   state should be updated to reflect that the node is dirty.
        """
        pass

    def preEvaluation(*args, **kwargs):
        """
        preEvaluation(context, evalNode) -> None

        Prepare a node's internal state for threaded evaluation.

        During the evaluation graph execution each node gets a chance to reset its internal states just before being evaluated.

        This code has to be thread safe, non - blocking and work only on data owned by the node.

        The timing of this callback is at the discretion of evaluation graph dependencies and individual evaluators.This means, it should be used purely to prepare this node for evaluation and no particular order should be assumed.

        This call will most likely happen from a worker thread.

        * context (MDGContext) - Context in which the evaluation is happening.
                                 This should be respected and only internal state
                                 information pertaining to it should be modified.
        * evaluationNode (MEvaluationNode) - Evaluation node which contains
                                             information about the dirty plugs that
                                             are about to be evaluated for the context.
                                             Should be only used to query information.
        """
        pass

    def setDependentsDirty(*args, **kwargs):
        """
        setDependentsDirty(plug, plugArray) -> self

        This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:



        - Allows attributeAffects-style relationships to be handled for dynamically-added attributes. Since MPxNode.attributeAffects() can only be used with non-dynamic attributes, use of this method allows a way for all attributes of a node to affect one another, both dynamic and non-dynamic.

        - Provides more flexible relationships than what is available with MPxNode.attributeAffects(). For example, you may wish to not dirty plugs when the current frame is one. However, as the routine is called during dirty propagation, there are restrictions on what can be done within the routine, most importantly you must not cause any dependency graph computation. For details, see the IMPORTANT NOTE below.



        This method is designed to work harmoniously with MPxNode.attributeAffects() on the same node. Alternately, you can do all affects relationships within a yourNode.setDependentsDirty() implementation.

        The body of a user-implemented setDependentsDirty() implementation might look like the following example, which causes the plug called "B" to be set dirty whever plug "A" is changed, i.e. A affects B.

        * plug (MPlug) - plug which is being set dirty by Maya.
        * plugArray the programmer should add any plugs which they want to set dirty to this list.
        """
        pass

    def setDoNotWrite(*args, **kwargs):
        """
        setDoNotWrite(bool) -> self

        Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out.

        NOTES:
        1. Plug-in "requires" information will be written out with the model when saved.  But a subsequent reload and resave of the file will cause these to go away.
        2. If this node is a DAG and has a parent or children, the "do not write" flag of the parent or children will not be set. It is the developer's responsibility to ensure that the resulting scene file is capable of being read in without errors due to unwritten nodes.
        """
        pass

    def setExternalContent(*args, **kwargs):
        """
        setExternalContent(table) -> self

        This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts.

        The keys in the map must be the same as the ones provided by the node in getExternalContent.  The values are the new locations.

        When implementing setExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also set their external content.

        The default implementation does nothing.

        * table Key->location table with new content locations.
        """
        pass

    def setExternalContentForFileAttr(*args, **kwargs):
        """
        setExternalContentForFileAttr(attr, table) -> bool

        This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name.

        The method will not write to the plug if the attribute is not found in the  table.

        * attr (MObject) - The attribute of the plug we want to write to.
        * table (MExternalContentLocationTable) - A table which may hold or not the value for a given plug.

        Returns True if the plug was successfully written to. False if no entry in the table was named after the attribute or if no plug was found.
        """
        pass

    def setInternalValue(*args, **kwargs):
        """
        setInternalValue(plug, dataHandle) -> bool


        This method is overriden by nodes that store attribute data in some internal format.

        The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

        When internal attribute values are set via setAttr or MPlug.setValue() this method is called.

        Another use for this method is to impose attribute limits.

        All internal data should respect the current context, which may be obtained from MDGContext::current()

        * plug (MPlug) - the attribute that is being set.
        * dataHandle (MDataHandle) - the dataHandle containing the value to set.
        """
        pass

    def setInternalValueInContext(*args, **kwargs):
        """
        setInternalValueInContext(plug, dataHandle, ctx) -> bool  [OBSOLETE]

        This method is obsolete. Override MPxNode.setInternalValue instead.

        * plug (MPlug) - the attribute that is being set.
        * dataHandle (MDataHandle) - the dataHandle containing the value to set.
        * ctx (MDGContext) - the context the method is being evaluated in.
        """
        pass

    def setMPSafe(*args, **kwargs):
        """
        setMPSafe(bool) -> self

        This method is obsolete. Override MPxNode.setSchedulingType instead.

        Set a flag to specify if a user defined shading node is safe for multi-processor rendering. For a shading node to be MP safe, it cannot access any shared global data and should only use attributes in the datablock to get input data and store output data.

        NOTE: This should be called from the postConstructor() method for shading node plug-ins only. If a shading node is non-safe, then it will only be useful during single processor rendering.
        """
        pass

    def shouldSave(*args, **kwargs):
        """
        shouldSave(plug) -> bool/None

        This method may be overridden by the user defined node.  It should only be required to override this on rare occasions.

        This method determines whether a specific attribute of this node should be written out during a file save.  The default behavior is to only write the value if it differs from the default and is not being supplied by a connection.  This behavior should be sufficient in most cases.
        This method is not called for ramp attributes since they should always be written.

        * plug (MPlug) - plug representing the attribute to be saved.
        """
        pass

    def thisMObject(*args, **kwargs):
        """
        thisMObject() -> MObject

        Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes.
        """
        pass

    def type(*args, **kwargs):
        """
        type() -> int

        Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes.

        It is not necessary to override this method.

          kDependNode                    Custom node derived from MPxNode
          kLocatorNode                   Custom locator derived from MPxLocatorNode
          kDeformerNode                  Custom deformer derived from MPxDeformerNode
          kManipContainer                Custom container derived from MPxManipContainer
          kSurfaceShape                  Custom shape derived from MPxSurfaceShape
          kFieldNode                     Custom field derived from MPxFieldNode
          kEmitterNode                   Custom emitter derived from MPxEmitterNode
          kSpringNode                    Custom spring derived from MPxSpringNode
          kIkSolverNode                  Custom IK solver derived from MPxIkSolverNode
          kHardwareShader                Custom shader derived from MPxHardwareShader
          kHwShaderNode                  Custom shader derived from MPxHwShaderNode
          kTransformNode                 Custom transform derived from MPxTransform
          kObjectSet                     Custom set derived from MPxObjectSet
          kFluidEmitterNode              Custom fluid emitter derived from MpxFluidEmitterNode
          kImagePlaneNode                Custom image plane derived from MPxImagePlane
          kParticleAttributeMapperNode   Custom particle attribute mapper derived from MPxParticleAttributeMapperNode
          kCameraSetNode                 Custom director derived from MPxCameraSet
          kConstraintNode                Custom constraint derived from MPxConstraint
          kManipulatorNode               Custom manipulator derived from MPxManipulatorNode
          kClientDeviceNode              Custom threaded device derived from MPxThreadedDeviceNode
          kThreadedDeviceNode            Custom threaded device node
          kAssembly                      Custom assembly derived from MPxAssembly
          kSkinCluster                                  Custom deformer derived from MPxSkinCluster
          kGeometryFilter                               Custom deformer derived from MPxGeometryFilter
                 kBlendShape                                    Custom deformer derived from MPxBlendShape
        """
        pass

    def typeId(*args, **kwargs):
        """
        typeId() -> MTypeId

        Returns the TYPEID of this node.
        """
        pass

    def typeName(*args, **kwargs):
        """
        typeName() -> string

        Returns the type name of this node.  The type name identifies the node type to the ASCII file format
        """
        pass

    @staticmethod
    def addAttribute(*args, **kwargs):
        """
        addAttribute(attr) -> None

        This method adds a new attribute to a user defined node type during the type's initialization.

        This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into  MFnPlugin.registerNode(). The attributes must first be created using one of the MFnAttribute classes, and can then be added using this method.

        For compound attributes, the proper way to use this method is by calling it with the parent attribute. If a compound attribute is passed, this method will add all of its children.
        NOTE: A failure will occur if you attempt to call addAttribute() on the children of a compound attribute.

        * attr (MObject) - new attribute to add.
        """
        pass

    @staticmethod
    def attributeAffects(*args, **kwargs):
        """
        attributeAffects(whenChanges, isAffected) -> None

        This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail.

        This method must be called for every attribute dependency when initializing the node's attributes.  The attributes must first be added using the MPxNode.addAttribute() method.  Failing to call this method will cause the node not to update when its inputs change. If there are no calls to this method in a node's initialization, then the compute method will never be called.

        This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into MFnPlugin.registerNode().  As a result, it does not work with dynamic attributes. For an alternate solution which handles dynamic as well as non-dynamic attributes refer to MPxNode.setDependentsDirty.()

        * whenChanges (MObject) - input attribute - MObject that points to an input attribute that has already been added.
        * isAffected (MObject) - affected output attribute - MObject that points to an output attribute that has already been added.
        """
        pass

    @staticmethod
    def inheritAttributesFrom(*args, **kwargs):
        """
        inheritAttributesFrom(parentClassName) -> None

        This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node.

        This method will only work during the static initialization method of the user defined node class and must be called before any other attributes have been added.  The initialization method is the one that is passed into  MFnPlugin.registerNode().

        A plugin node may only inherit attributes from one other class of plugin node. Attempting to call this method multiple times within a node's initialization method will result in an error.

        Both node classes must be registered using the same MPxNode type, listed in MPxNode.type().

        * parentClassName (string) - class of node to inherit attributes from.
        """
        pass

    kAssembly = 22

    kBlendShape = 25

    kCameraSetNode = 16

    kClientDeviceNode = 20

    kConstraintNode = 17

    kDeformerNode = 2

    kDependNode = 0

    kEmitterNode = 6

    kEvaluatedDirectly = 1

    kEvaluatedIndirectly = 0

    kFieldNode = 5

    kFluidEmitterNode = 13

    kGeometryFilter = 24

    kHardwareShader = 9

    kHwShaderNode = 10

    kIkSolverNode = 8

    kImagePlaneNode = 14

    kLast = 26

    kLeaveDirty = 2

    kLocatorNode = 1

    kManipContainer = 3

    kManipulatorNode = 18

    kMotionPathNode = 19

    kObjectSet = 12

    kParticleAttributeMapperNode = 15

    kPostEvaluationTypeLast = 3

    kSkinCluster = 23

    kSpringNode = 7

    kSurfaceShape = 4

    kThreadedDeviceNode = 21

    kTransformNode = 11


class MFn(object):
    """
    Static class providing constants for all API types.
    """

    kInvalid = 0

    kBase = 1

    kNamedObject = 2

    kModel = 3

    kDependencyNode = 4

    kAddDoubleLinear = 5

    kAffect = 6

    kAnimCurve = 7

    kAnimCurveTimeToAngular = 8

    kAnimCurveTimeToDistance = 9

    kAnimCurveTimeToTime = 10

    kAnimCurveTimeToUnitless = 11

    kAnimCurveUnitlessToAngular = 12

    kAnimCurveUnitlessToDistance = 13

    kAnimCurveUnitlessToTime = 14

    kAnimCurveUnitlessToUnitless = 15

    kResultCurve = 16

    kResultCurveTimeToAngular = 17

    kResultCurveTimeToDistance = 18

    kResultCurveTimeToTime = 19

    kResultCurveTimeToUnitless = 20

    kAngleBetween = 21

    kAudio = 22

    kBackground = 23

    kColorBackground = 24

    kFileBackground = 25

    kRampBackground = 26

    kBlend = 27

    kBlendTwoAttr = 28

    kBlendWeighted = 29

    kBlendDevice = 30

    kBlendColors = 31

    kBump = 32

    kBump3d = 33

    kCameraView = 34

    kChainToSpline = 35

    kChoice = 36

    kCondition = 37

    kContrast = 38

    kClampColor = 39

    kCreate = 40

    kAlignCurve = 41

    kAlignSurface = 42

    kAttachCurve = 43

    kAttachSurface = 44

    kAvgCurves = 45

    kAvgSurfacePoints = 46

    kAvgNurbsSurfacePoints = 47

    kBevel = 48

    kBirailSrf = 49

    kDPbirailSrf = 50

    kMPbirailSrf = 51

    kSPbirailSrf = 52

    kBoundary = 53

    kCircle = 54

    kCloseCurve = 55

    kClosestPointOnSurface = 56

    kCloseSurface = 57

    kCurveFromSurface = 58

    kCurveFromSurfaceBnd = 59

    kCurveFromSurfaceCoS = 60

    kCurveFromSurfaceIso = 61

    kCurveInfo = 62

    kDetachCurve = 63

    kDetachSurface = 64

    kExtendCurve = 65

    kExtendSurface = 66

    kExtrude = 67

    kFFblendSrf = 68

    kFFfilletSrf = 69

    kFilletCurve = 70

    kFitBspline = 71

    kFlow = 72

    kHardenPointCurve = 73

    kIllustratorCurve = 74

    kInsertKnotCrv = 75

    kInsertKnotSrf = 76

    kIntersectSurface = 77

    kNurbsTesselate = 78

    kNurbsPlane = 79

    kNurbsCube = 80

    kOffsetCos = 81

    kOffsetCurve = 82

    kPlanarTrimSrf = 83

    kPointOnCurveInfo = 84

    kPointOnSurfaceInfo = 85

    kPrimitive = 86

    kProjectCurve = 87

    kProjectTangent = 88

    kRBFsurface = 89

    kRebuildCurve = 90

    kRebuildSurface = 91

    kReverseCurve = 92

    kReverseSurface = 93

    kRevolve = 94

    kRevolvedPrimitive = 95

    kCone = 96

    kRenderCone = 97

    kCylinder = 98

    kSphere = 99

    kSkin = 100

    kStitchSrf = 101

    kSubCurve = 102

    kSurfaceInfo = 103

    kTextCurves = 104

    kTrim = 105

    kUntrim = 106

    kDagNode = 107

    kProxy = 108

    kUnderWorld = 109

    kTransform = 110

    kAimConstraint = 111

    kLookAt = 112

    kGeometryConstraint = 113

    kGeometryVarGroup = 114

    kAnyGeometryVarGroup = 115

    kCurveVarGroup = 116

    kMeshVarGroup = 117

    kSurfaceVarGroup = 118

    kIkEffector = 119

    kIkHandle = 120

    kJoint = 121

    kManipulator3D = 122

    kArrowManip = 123

    kAxesActionManip = 124

    kBallProjectionManip = 125

    kCircleManip = 126

    kScreenAlignedCircleManip = 127

    kCircleSweepManip = 128

    kConcentricProjectionManip = 129

    kCubicProjectionManip = 130

    kCylindricalProjectionManip = 131

    kDiscManip = 132

    kFreePointManip = 133

    kCenterManip = 134

    kLimitManip = 135

    kEnableManip = 136

    kFreePointTriadManip = 137

    kPropMoveTriadManip = 138

    kTowPointManip = 139

    kPolyCreateToolManip = 140

    kPolySplitToolManip = 141

    kGeometryOnLineManip = 142

    kCameraPlaneManip = 143

    kToggleOnLineManip = 144

    kStateManip = 145

    kIsoparmManip = 146

    kLineManip = 147

    kManipContainer = 148

    kAverageCurveManip = 149

    kBarnDoorManip = 150

    kBevelManip = 151

    kBlendManip = 152

    kButtonManip = 153

    kCameraManip = 154

    kCoiManip = 155

    kCpManip = 156

    kCreateCVManip = 157

    kCreateEPManip = 158

    kCurveEdManip = 159

    kCurveSegmentManip = 160

    kDirectionManip = 161

    kDofManip = 162

    kDropoffManip = 163

    kExtendCurveDistanceManip = 164

    kExtrudeManip = 165

    kIkSplineManip = 166

    kIkRPManip = 167

    kJointClusterManip = 168

    kLightManip = 169

    kMotionPathManip = 170

    kOffsetCosManip = 171

    kOffsetCurveManip = 172

    kProjectionManip = 173

    kPolyProjectionManip = 174

    kProjectionUVManip = 175

    kProjectionMultiManip = 176

    kProjectTangentManip = 177

    kPropModManip = 178

    kQuadPtOnLineManip = 179

    kRbfSrfManip = 180

    kReverseCurveManip = 181

    kReverseCrvManip = 182

    kReverseSurfaceManip = 183

    kRevolveManip = 184

    kRevolvedPrimitiveManip = 185

    kSpotManip = 186

    kSpotCylinderManip = 187

    kTriplanarProjectionManip = 188

    kTrsManip = 189

    kDblTrsManip = 190

    kPivotManip2D = 191

    kManip2DContainer = 192

    kPolyMoveUVManip = 193

    kPolyMappingManip = 194

    kPolyModifierManip = 195

    kPolyMoveVertexManip = 196

    kPolyVertexNormalManip = 197

    kTexSmudgeUVManip = 198

    kTexLatticeDeformManip = 199

    kTexLattice = 200

    kTexSmoothManip = 201

    kTrsTransManip = 202

    kTrsInsertManip = 203

    kTrsXformManip = 204

    kManipulator2D = 205

    kTranslateManip2D = 206

    kPlanarProjectionManip = 207

    kPointOnCurveManip = 208

    kTowPointOnCurveManip = 209

    kMarkerManip = 210

    kPointOnLineManip = 211

    kPointOnSurfaceManip = 212

    kTranslateUVManip = 213

    kRotateBoxManip = 214

    kRotateManip = 215

    kHandleRotateManip = 216

    kRotateLimitsManip = 217

    kScaleLimitsManip = 218

    kScaleManip = 219

    kScalingBoxManip = 220

    kScriptManip = 221

    kSphericalProjectionManip = 222

    kTextureManip3D = 223

    kToggleManip = 224

    kTranslateBoxManip = 225

    kTranslateLimitsManip = 226

    kTranslateManip = 227

    kTrimManip = 228

    kJointTranslateManip = 229

    kManipulator = 230

    kCirclePointManip = 231

    kDimensionManip = 232

    kFixedLineManip = 233

    kLightProjectionGeometry = 234

    kLineArrowManip = 235

    kPointManip = 236

    kTriadManip = 237

    kNormalConstraint = 238

    kOrientConstraint = 239

    kPointConstraint = 240

    kSymmetryConstraint = 241

    kParentConstraint = 242

    kPoleVectorConstraint = 243

    kScaleConstraint = 244

    kTangentConstraint = 245

    kUnknownTransform = 246

    kWorld = 247

    kShape = 248

    kBaseLattice = 249

    kCamera = 250

    kCluster = 251

    kSoftMod = 252

    kCollision = 253

    kDummy = 254

    kEmitter = 255

    kField = 256

    kAir = 257

    kDrag = 258

    kGravity = 259

    kNewton = 260

    kRadial = 261

    kTurbulence = 262

    kUniform = 263

    kVortex = 264

    kGeometric = 265

    kCurve = 266

    kNurbsCurve = 267

    kNurbsCurveGeom = 268

    kDimension = 269

    kAngle = 270

    kAnnotation = 271

    kDistance = 272

    kArcLength = 273

    kRadius = 274

    kParamDimension = 275

    kDirectedDisc = 276

    kRenderRect = 277

    kEnvFogShape = 278

    kLattice = 279

    kLatticeGeom = 280

    kLocator = 281

    kDropoffLocator = 282

    kMarker = 283

    kOrientationMarker = 284

    kPositionMarker = 285

    kOrientationLocator = 286

    kTrimLocator = 287

    kPlane = 288

    kSketchPlane = 289

    kGroundPlane = 290

    kOrthoGrid = 291

    kSprite = 292

    kSurface = 293

    kNurbsSurface = 294

    kNurbsSurfaceGeom = 295

    kMesh = 296

    kMeshGeom = 297

    kRenderSphere = 298

    kFlexor = 299

    kClusterFlexor = 300

    kGuideLine = 301

    kLight = 302

    kAmbientLight = 303

    kNonAmbientLight = 304

    kAreaLight = 305

    kLinearLight = 306

    kNonExtendedLight = 307

    kDirectionalLight = 308

    kPointLight = 309

    kSpotLight = 310

    kParticle = 311

    kPolyToolFeedbackShape = 312

    kRigidConstraint = 313

    kRigid = 314

    kSpring = 315

    kUnknownDag = 316

    kDefaultLightList = 317

    kDeleteComponent = 318

    kDispatchCompute = 319

    kShadingEngine = 320

    kDisplacementShader = 321

    kDistanceBetween = 322

    kDOF = 323

    kDummyConnectable = 324

    kDynamicsController = 325

    kGeoConnectable = 326

    kExpression = 327

    kExtract = 328

    kFilter = 329

    kFilterClosestSample = 330

    kFilterEuler = 331

    kFilterSimplify = 332

    kGammaCorrect = 333

    kGeometryFilt = 334

    kBendLattice = 335

    kBlendShape = 336

    kCombinationShape = 337

    kBulgeLattice = 338

    kFFD = 339

    kFfdDualBase = 340

    kRigidDeform = 341

    kSculpt = 342

    kTextureDeformer = 343

    kTextureDeformerHandle = 344

    kTweak = 345

    kWeightGeometryFilt = 346

    kClusterFilter = 347

    kSoftModFilter = 348

    kJointCluster = 349

    kDeltaMush = 350

    kTension = 351

    kMorph = 352

    kSolidify = 353

    kProximityWrap = 354

    kWire = 355

    kGroupId = 356

    kGroupParts = 357

    kGuide = 358

    kHsvToRgb = 359

    kHyperGraphInfo = 360

    kHyperLayout = 361

    kHyperView = 362

    kIkSolver = 363

    kMCsolver = 364

    kPASolver = 365

    kSCsolver = 366

    kRPsolver = 367

    kSplineSolver = 368

    kIkSystem = 369

    kImagePlane = 370

    kLambert = 371

    kReflect = 372

    kBlinn = 373

    kPhong = 374

    kPhongExplorer = 375

    kLayeredShader = 376

    kStandardSurface = 377

    kLightInfo = 378

    kLeastSquares = 379

    kLightFogMaterial = 380

    kEnvFogMaterial = 381

    kLightList = 382

    kLightSource = 383

    kLuminance = 384

    kMakeGroup = 385

    kMaterial = 386

    kDiffuseMaterial = 387

    kLambertMaterial = 388

    kBlinnMaterial = 389

    kPhongMaterial = 390

    kLightSourceMaterial = 391

    kMaterialInfo = 392

    kMaterialTemplate = 393

    kMatrixAdd = 394

    kMatrixHold = 395

    kMatrixMult = 396

    kMatrixPass = 397

    kMatrixWtAdd = 398

    kMidModifier = 399

    kMidModifierWithMatrix = 400

    kPolyBevel = 401

    kPolyTweak = 402

    kPolyAppend = 403

    kPolyChipOff = 404

    kPolyCloseBorder = 405

    kPolyCollapseEdge = 406

    kPolyCollapseF = 407

    kPolyCylProj = 408

    kPolyDelEdge = 409

    kPolyDelFacet = 410

    kPolyDelVertex = 411

    kPolyExtrudeFacet = 412

    kPolyMapCut = 413

    kPolyMapDel = 414

    kPolyMapSew = 415

    kPolyMergeEdge = 416

    kPolyMergeFacet = 417

    kPolyMoveEdge = 418

    kPolyMoveFacet = 419

    kPolyMoveFacetUV = 420

    kPolyMoveUV = 421

    kPolyMoveVertex = 422

    kPolyMoveVertexUV = 423

    kPolyNormal = 424

    kPolyPlanProj = 425

    kPolyProj = 426

    kPolyQuad = 427

    kPolySmooth = 428

    kPolySoftEdge = 429

    kPolySphProj = 430

    kPolySplit = 431

    kPolySubdEdge = 432

    kPolySubdFacet = 433

    kPolyTriangulate = 434

    kPolyCreator = 435

    kPolyPrimitive = 436

    kPolyCone = 437

    kPolyCube = 438

    kPolyCylinder = 439

    kPolyMesh = 440

    kPolySphere = 441

    kPolyTorus = 442

    kPolyCreateFacet = 443

    kPolyUnite = 444

    kMotionPath = 445

    kPluginMotionPathNode = 446

    kMultilisterLight = 447

    kMultiplyDivide = 448

    kOldGeometryConstraint = 449

    kOpticalFX = 450

    kParticleAgeMapper = 451

    kParticleCloud = 452

    kParticleColorMapper = 453

    kParticleIncandecenceMapper = 454

    kParticleTransparencyMapper = 455

    kPartition = 456

    kPlace2dTexture = 457

    kPlace3dTexture = 458

    kPluginDependNode = 459

    kPluginLocatorNode = 460

    kPlusMinusAverage = 461

    kPointMatrixMult = 462

    kPolySeparate = 463

    kPostProcessList = 464

    kProjection = 465

    kRecord = 466

    kRenderUtilityList = 467

    kReverse = 468

    kRgbToHsv = 469

    kRigidSolver = 470

    kSet = 471

    kTextureBakeSet = 472

    kVertexBakeSet = 473

    kSetRange = 474

    kShaderGlow = 475

    kShaderList = 476

    kShadingMap = 477

    kSamplerInfo = 478

    kShapeFragment = 479

    kSimpleVolumeShader = 480

    kSl60 = 481

    kSnapshot = 482

    kStoryBoard = 483

    kSummaryObject = 484

    kSuper = 485

    kControl = 486

    kSurfaceLuminance = 487

    kSurfaceShader = 488

    kTextureList = 489

    kTextureEnv = 490

    kEnvBall = 491

    kEnvCube = 492

    kEnvChrome = 493

    kEnvSky = 494

    kEnvSphere = 495

    kTexture2d = 496

    kBulge = 497

    kChecker = 498

    kCloth = 499

    kFileTexture = 500

    kFractal = 501

    kGrid = 502

    kMountain = 503

    kRamp = 504

    kStencil = 505

    kWater = 506

    kTexture3d = 507

    kBrownian = 508

    kCloud = 509

    kCrater = 510

    kGranite = 511

    kLeather = 512

    kMarble = 513

    kRock = 514

    kSnow = 515

    kSolidFractal = 516

    kStucco = 517

    kTxSl = 518

    kWood = 519

    kTime = 520

    kTimeToUnitConversion = 521

    kRenderSetup = 522

    kRenderGlobals = 523

    kRenderGlobalsList = 524

    kRenderQuality = 525

    kResolution = 526

    kHardwareRenderGlobals = 527

    kArrayMapper = 528

    kUnitConversion = 529

    kUnitToTimeConversion = 530

    kUseBackground = 531

    kUnknown = 532

    kVectorProduct = 533

    kVolumeShader = 534

    kComponent = 535

    kCurveCVComponent = 536

    kCurveEPComponent = 537

    kCurveKnotComponent = 538

    kCurveParamComponent = 539

    kIsoparmComponent = 540

    kPivotComponent = 541

    kSurfaceCVComponent = 542

    kSurfaceEPComponent = 543

    kSurfaceKnotComponent = 544

    kEdgeComponent = 545

    kLatticeComponent = 546

    kSurfaceRangeComponent = 547

    kDecayRegionCapComponent = 548

    kDecayRegionComponent = 549

    kMeshComponent = 550

    kMeshEdgeComponent = 551

    kMeshPolygonComponent = 552

    kMeshFrEdgeComponent = 553

    kMeshVertComponent = 554

    kMeshFaceVertComponent = 555

    kOrientationComponent = 556

    kSubVertexComponent = 557

    kMultiSubVertexComponent = 558

    kSetGroupComponent = 559

    kDynParticleSetComponent = 560

    kSelectionItem = 561

    kDagSelectionItem = 562

    kNonDagSelectionItem = 563

    kItemList = 564

    kAttribute = 565

    kNumericAttribute = 566

    kDoubleAngleAttribute = 567

    kFloatAngleAttribute = 568

    kDoubleLinearAttribute = 569

    kFloatLinearAttribute = 570

    kTimeAttribute = 571

    kEnumAttribute = 572

    kUnitAttribute = 573

    kTypedAttribute = 574

    kCompoundAttribute = 575

    kGenericAttribute = 576

    kLightDataAttribute = 577

    kMatrixAttribute = 578

    kFloatMatrixAttribute = 579

    kMessageAttribute = 580

    kOpaqueAttribute = 581

    kPlugin = 582

    kData = 583

    kComponentListData = 584

    kDoubleArrayData = 585

    kIntArrayData = 586

    kUintArrayData = 587

    kLatticeData = 588

    kMatrixData = 589

    kMeshData = 590

    kNurbsSurfaceData = 591

    kNurbsCurveData = 592

    kNumericData = 593

    kData2Double = 594

    kData2Float = 595

    kData2Int = 596

    kData2Short = 597

    kData3Double = 598

    kData3Float = 599

    kData3Int = 600

    kData3Short = 601

    kPluginData = 602

    kPointArrayData = 603

    kMatrixArrayData = 604

    kSphereData = 605

    kStringData = 606

    kStringArrayData = 607

    kVectorArrayData = 608

    kSelectionList = 609

    kTransformGeometry = 610

    kCommEdgePtManip = 611

    kCommEdgeOperManip = 612

    kCommEdgeSegmentManip = 613

    kCommCornerManip = 614

    kCommCornerOperManip = 615

    kPluginDeformerNode = 616

    kTorus = 617

    kPolyBoolOp = 618

    kSingleShadingSwitch = 619

    kDoubleShadingSwitch = 620

    kTripleShadingSwitch = 621

    kNurbsSquare = 622

    kAnisotropy = 623

    kNonLinear = 624

    kDeformFunc = 625

    kDeformBend = 626

    kDeformTwist = 627

    kDeformSquash = 628

    kDeformFlare = 629

    kDeformSine = 630

    kDeformWave = 631

    kDeformBendManip = 632

    kDeformTwistManip = 633

    kDeformSquashManip = 634

    kDeformFlareManip = 635

    kDeformSineManip = 636

    kDeformWaveManip = 637

    kSoftModManip = 638

    kDistanceManip = 639

    kScript = 640

    kCurveFromMeshEdge = 641

    kCurveCurveIntersect = 642

    kNurbsCircular3PtArc = 643

    kNurbsCircular2PtArc = 644

    kOffsetSurface = 645

    kRoundConstantRadius = 646

    kRoundRadiusManip = 647

    kRoundRadiusCrvManip = 648

    kRoundConstantRadiusManip = 649

    kThreePointArcManip = 650

    kTwoPointArcManip = 651

    kTextButtonManip = 652

    kOffsetSurfaceManip = 653

    kImageData = 654

    kImageLoad = 655

    kImageSave = 656

    kImageNetSrc = 657

    kImageNetDest = 658

    kImageRender = 659

    kImageAdd = 660

    kImageDiff = 661

    kImageMultiply = 662

    kImageOver = 663

    kImageUnder = 664

    kImageColorCorrect = 665

    kImageBlur = 666

    kImageFilter = 667

    kImageDepth = 668

    kImageDisplay = 669

    kImageView = 670

    kImageMotionBlur = 671

    kViewColorManager = 672

    kMatrixFloatData = 673

    kSkinShader = 674

    kComponentManip = 675

    kSelectionListData = 676

    kObjectFilter = 677

    kObjectMultiFilter = 678

    kObjectNameFilter = 679

    kObjectTypeFilter = 680

    kObjectAttrFilter = 681

    kObjectRenderFilter = 682

    kObjectScriptFilter = 683

    kSelectionListOperator = 684

    kSubdiv = 685

    kPolyToSubdiv = 686

    kSkinClusterFilter = 687

    kKeyingGroup = 688

    kCharacter = 689

    kCharacterOffset = 690

    kDagPose = 691

    kStitchAsNurbsShell = 692

    kExplodeNurbsShell = 693

    kNurbsBoolean = 694

    kStitchSrfManip = 695

    kForceUpdateManip = 696

    kPluginManipContainer = 697

    kPolySewEdge = 698

    kPolyMergeVert = 699

    kPolySmoothFacet = 700

    kSmoothCurve = 701

    kGlobalStitch = 702

    kSubdivCVComponent = 703

    kSubdivEdgeComponent = 704

    kSubdivFaceComponent = 705

    kUVManip2D = 706

    kTranslateUVManip2D = 707

    kRotateUVManip2D = 708

    kScaleUVManip2D = 709

    kPolyTweakUV = 710

    kMoveUVShellManip2D = 711

    kPluginShape = 712

    kGeometryData = 713

    kSingleIndexedComponent = 714

    kDoubleIndexedComponent = 715

    kTripleIndexedComponent = 716

    kExtendSurfaceDistanceManip = 717

    kSquareSrf = 718

    kSquareSrfManip = 719

    kSubdivToPoly = 720

    kDynBase = 721

    kDynEmitterManip = 722

    kDynFieldsManip = 723

    kDynBaseFieldManip = 724

    kDynAirManip = 725

    kDynNewtonManip = 726

    kDynTurbulenceManip = 727

    kDynSpreadManip = 728

    kDynAttenuationManip = 729

    kDynArrayAttrsData = 730

    kPluginFieldNode = 731

    kPluginEmitterNode = 732

    kPluginSpringNode = 733

    kDisplayLayer = 734

    kDisplayLayerManager = 735

    kPolyColorPerVertex = 736

    kCreateColorSet = 737

    kDeleteColorSet = 738

    kCopyColorSet = 739

    kBlendColorSet = 740

    kPolyColorMod = 741

    kPolyColorDel = 742

    kCharacterMappingData = 743

    kDynSweptGeometryData = 744

    kWrapFilter = 745

    kMeshVtxFaceComponent = 746

    kBinaryData = 747

    kAttribute2Double = 748

    kAttribute2Float = 749

    kAttribute2Short = 750

    kAttribute2Int = 751

    kAttribute3Double = 752

    kAttribute3Float = 753

    kAttribute3Short = 754

    kAttribute3Int = 755

    kReference = 756

    kBlindData = 757

    kBlindDataTemplate = 758

    kPolyBlindData = 759

    kPolyNormalPerVertex = 760

    kNurbsToSubdiv = 761

    kPluginIkSolver = 762

    kInstancer = 763

    kMoveVertexManip = 764

    kStroke = 765

    kBrush = 766

    kStrokeGlobals = 767

    kPluginGeometryData = 768

    kLightLink = 769

    kDynGlobals = 770

    kPolyReduce = 771

    kLodThresholds = 772

    kChooser = 773

    kLodGroup = 774

    kMultDoubleLinear = 775

    kFourByFourMatrix = 776

    kTowPointOnSurfaceManip = 777

    kSurfaceEdManip = 778

    kSurfaceFaceComponent = 779

    kClipScheduler = 780

    kClipLibrary = 781

    kSubSurface = 782

    kSmoothTangentSrf = 783

    kRenderPass = 784

    kRenderPassSet = 785

    kRenderLayer = 786

    kRenderLayerManager = 787

    kPassContributionMap = 788

    kPrecompExport = 789

    kRenderTarget = 790

    kRenderedImageSource = 791

    kImageSource = 792

    kPolyFlipEdge = 793

    kPolyExtrudeEdge = 794

    kAnimBlend = 795

    kAnimBlendInOut = 796

    kPolyAppendVertex = 797

    kUvChooser = 798

    kSubdivCompId = 799

    kVolumeAxis = 800

    kDeleteUVSet = 801

    kSubdHierBlind = 802

    kSubdBlindData = 803

    kCharacterMap = 804

    kLayeredTexture = 805

    kSubdivCollapse = 806

    kParticleSamplerInfo = 807

    kCopyUVSet = 808

    kCreateUVSet = 809

    kClip = 810

    kPolySplitVert = 811

    kSubdivData = 812

    kSubdivGeom = 813

    kUInt64ArrayData = 814

    kInt64ArrayData = 815

    kPolySplitEdge = 816

    kSubdivReverseFaces = 817

    kMeshMapComponent = 818

    kSectionManip = 819

    kXsectionSubdivEdit = 820

    kSubdivToNurbs = 821

    kEditCurve = 822

    kEditCurveManip = 823

    kCrossSectionManager = 824

    kCreateSectionManip = 825

    kCrossSectionEditManip = 826

    kDropOffFunction = 827

    kSubdBoolean = 828

    kSubdModifyEdge = 829

    kModifyEdgeCrvManip = 830

    kModifyEdgeManip = 831

    kScalePointManip = 832

    kTransformBoxManip = 833

    kSymmetryLocator = 834

    kSymmetryMapVector = 835

    kSymmetryMapCurve = 836

    kCurveFromSubdivEdge = 837

    kCreateBPManip = 838

    kModifyEdgeBaseManip = 839

    kSubdExtrudeFace = 840

    kSubdivSurfaceVarGroup = 841

    kSfRevolveManip = 842

    kCurveFromSubdivFace = 843

    kUnused1 = 844

    kUnused2 = 845

    kUnused3 = 846

    kUnused4 = 847

    kUnused5 = 848

    kUnused6 = 849

    kPolyTransfer = 850

    kPolyAverageVertex = 851

    kPolyAutoProj = 852

    kPolyLayoutUV = 853

    kPolyMapSewMove = 854

    kSubdModifier = 855

    kSubdMoveVertex = 856

    kSubdMoveEdge = 857

    kSubdMoveFace = 858

    kSubdDelFace = 859

    kSnapshotShape = 860

    kSubdivMapComponent = 861

    kJiggleDeformer = 862

    kGlobalCacheControls = 863

    kDiskCache = 864

    kSubdCloseBorder = 865

    kSubdMergeVert = 866

    kBoxData = 867

    kBox = 868

    kRenderBox = 869

    kSubdSplitFace = 870

    kVolumeFog = 871

    kSubdTweakUV = 872

    kSubdMapCut = 873

    kSubdLayoutUV = 874

    kSubdMapSewMove = 875

    kOcean = 876

    kVolumeNoise = 877

    kSubdAutoProj = 878

    kSubdSubdivideFace = 879

    kNoise = 880

    kAttribute4Double = 881

    kData4Double = 882

    kSubdPlanProj = 883

    kSubdTweak = 884

    kSubdProjectionManip = 885

    kSubdMappingManip = 886

    kHardwareReflectionMap = 887

    kPolyNormalizeUV = 888

    kPolyFlipUV = 889

    kHwShaderNode = 890

    kPluginHardwareShader = 891

    kPluginHwShaderNode = 892

    kSubdAddTopology = 893

    kSubdCleanTopology = 894

    kImplicitCone = 895

    kImplicitSphere = 896

    kRampShader = 897

    kVolumeLight = 898

    kOceanShader = 899

    kBevelPlus = 900

    kStyleCurve = 901

    kPolyCut = 902

    kPolyPoke = 903

    kPolyWedgeFace = 904

    kPolyCutManipContainer = 905

    kPolyCutManip = 906

    kPolyMirrorManipContainer = 907

    kPolyPokeManip = 908

    kFluidTexture3D = 909

    kFluidTexture2D = 910

    kPolyMergeUV = 911

    kPolyStraightenUVBorder = 912

    kAlignManip = 913

    kPluginTransformNode = 914

    kFluid = 915

    kFluidGeom = 916

    kFluidData = 917

    kSmear = 918

    kStringShadingSwitch = 919

    kStudioClearCoat = 920

    kFluidEmitter = 921

    kHeightField = 922

    kGeoConnector = 923

    kSnapshotPath = 924

    kPluginObjectSet = 925

    kQuadShadingSwitch = 926

    kPolyExtrudeVertex = 927

    kPairBlend = 928

    kTextManip = 929

    kViewManip = 930

    kXformManip = 931

    kMute = 932

    kConstraint = 933

    kTrimWithBoundaries = 934

    kCurveFromMeshCoM = 935

    kFollicle = 936

    kHairSystem = 937

    kRemapValue = 938

    kRemapColor = 939

    kRemapHsv = 940

    kHairConstraint = 941

    kTimeFunction = 942

    kMentalRayTexture = 943

    kObjectBinFilter = 944

    kPolySmoothProxy = 945

    kPfxGeometry = 946

    kPfxHair = 947

    kHairTubeShader = 948

    kPsdFileTexture = 949

    kKeyframeDelta = 950

    kKeyframeDeltaMove = 951

    kKeyframeDeltaScale = 952

    kKeyframeDeltaAddRemove = 953

    kKeyframeDeltaBlockAddRemove = 954

    kKeyframeDeltaInfType = 955

    kKeyframeDeltaTangent = 956

    kKeyframeDeltaWeighted = 957

    kKeyframeDeltaBreakdown = 958

    kPolyMirror = 959

    kPolyCreaseEdge = 960

    kPolyPinUV = 961

    kHikEffector = 962

    kHikIKEffector = 963

    kHikFKJoint = 964

    kHikSolver = 965

    kHikHandle = 966

    kProxyManager = 967

    kPolyAutoProjManip = 968

    kPolyPrism = 969

    kPolyPyramid = 970

    kPolySplitRing = 971

    kPfxToon = 972

    kToonLineAttributes = 973

    kPolyDuplicateEdge = 974

    kFacade = 975

    kMaterialFacade = 976

    kEnvFacade = 977

    kAISEnvFacade = 978

    kLineModifier = 979

    kPolyArrow = 980

    kPolyPrimitiveMisc = 981

    kPolyPlatonicSolid = 982

    kPolyPipe = 983

    kHikFloorContactMarker = 984

    kHikGroundPlane = 985

    kPolyComponentData = 986

    kPolyHelix = 987

    kCacheFile = 988

    kHistorySwitch = 989

    kClosestPointOnMesh = 990

    kUVPin = 991

    kProximityPin = 992

    kTransferAttributes = 993

    kDynamicConstraint = 994

    kNComponent = 995

    kPolyBridgeEdge = 996

    kCacheableNode = 997

    kNucleus = 998

    kNBase = 999

    kCacheBase = 1000

    kCacheBlend = 1001

    kCacheTrack = 1002

    kKeyframeRegionManip = 1003

    kCurveNormalizerAngle = 1004

    kCurveNormalizerLinear = 1005

    kHyperLayoutDG = 1006

    kPluginImagePlaneNode = 1007

    kNCloth = 1008

    kNParticle = 1009

    kNRigid = 1010

    kPluginParticleAttributeMapperNode = 1011

    kCameraSet = 1012

    kPluginCameraSet = 1013

    kContainer = 1014

    kFloatVectorArrayData = 1015

    kNObjectData = 1016

    kNObject = 1017

    kPluginConstraintNode = 1018

    kAsset = 1019

    kPolyEdgeToCurve = 1020

    kAnimLayer = 1021

    kBlendNodeBase = 1022

    kBlendNodeBoolean = 1023

    kBlendNodeDouble = 1024

    kBlendNodeDoubleAngle = 1025

    kBlendNodeDoubleLinear = 1026

    kBlendNodeEnum = 1027

    kBlendNodeFloat = 1028

    kBlendNodeFloatAngle = 1029

    kBlendNodeFloatLinear = 1030

    kBlendNodeInt16 = 1031

    kBlendNodeInt32 = 1032

    kBlendNodeAdditiveScale = 1033

    kBlendNodeAdditiveRotation = 1034

    kPluginManipulatorNode = 1035

    kNIdData = 1036

    kNId = 1037

    kFloatArrayData = 1038

    kMembrane = 1039

    kMergeVertsToolManip = 1040

    kUint64SingleIndexedComponent = 1041

    kPolyToolFeedbackManip = 1042

    kPolySelectEditFeedbackManip = 1043

    kWriteToFrameBuffer = 1044

    kWriteToColorBuffer = 1045

    kWriteToVectorBuffer = 1046

    kWriteToDepthBuffer = 1047

    kWriteToLabelBuffer = 1048

    kStereoCameraMaster = 1049

    kSequenceManager = 1050

    kSequencer = 1051

    kShot = 1052

    kBlendNodeTime = 1053

    kCreateBezierManip = 1054

    kBezierCurve = 1055

    kBezierCurveData = 1056

    kNurbsCurveToBezier = 1057

    kBezierCurveToNurbs = 1058

    kPolySpinEdge = 1059

    kPolyHoleFace = 1060

    kPointOnPolyConstraint = 1061

    kPolyConnectComponents = 1062

    kSkinBinding = 1063

    kVolumeBindManip = 1064

    kVertexWeightSet = 1065

    kNearestPointOnCurve = 1066

    kColorProfile = 1067

    kAdskMaterial = 1068

    kContainerBase = 1069

    kDagContainer = 1070

    kPolyUVRectangle = 1071

    kHardwareRenderingGlobals = 1072

    kPolyProjectCurve = 1073

    kRenderingList = 1074

    kPolyExtrudeManip = 1075

    kPolyExtrudeManipContainer = 1076

    kThreadedDevice = 1077

    kClientDevice = 1078

    kPluginClientDevice = 1079

    kPluginThreadedDevice = 1080

    kTimeWarp = 1081

    kAssembly = 1082

    kClipGhostShape = 1083

    kClipToGhostData = 1084

    kMandelbrot = 1085

    kMandelbrot3D = 1086

    kGreasePlane = 1087

    kGreasePlaneRenderShape = 1088

    kGreasePencilSequence = 1089

    kEditMetadata = 1090

    kCreaseSet = 1091

    kPolyEditEdgeFlow = 1092

    kFosterParent = 1093

    kSnapUVManip2D = 1094

    kToolContext = 1095

    kNLE = 1096

    kShrinkWrapFilter = 1097

    kEditsManager = 1098

    kPolyBevel2 = 1099

    kPolyCBoolOp = 1100

    kGeomBind = 1101

    kColorMgtGlobals = 1102

    kPolyBevel3 = 1103

    kTimeEditorClipBase = 1104

    kTimeEditorClipEvaluator = 1105

    kTimeEditorClip = 1106

    kTimeEditor = 1107

    kTimeEditorTracks = 1108

    kTimeEditorInterpolator = 1109

    kTimeEditorAnimSource = 1110

    kCaddyManipBase = 1111

    kPolyCaddyManip = 1112

    kPolyModifierManipContainer = 1113

    kPolyRemesh = 1114

    kPolyContourProj = 1115

    kContourProjectionManip = 1116

    kNodeGraphEditorInfo = 1117

    kNodeGraphEditorBookmarks = 1118

    kNodeGraphEditorBookmarkInfo = 1119

    kPluginSkinCluster = 1120

    kPluginGeometryFilter = 1121

    kPluginBlendShape = 1122

    kPolyPassThru = 1123

    kTrackInfoManager = 1124

    kPolyClean = 1125

    kShapeEditorManager = 1126

    kOceanDeformer = 1127

    kPoseInterpolatorManager = 1128

    kControllerTag = 1129

    kReForm = 1130

    kCustomEvaluatorClusterNode = 1131

    kPolyCircularize = 1132

    kArubaTesselate = 1133

    kReorderUVSet = 1134

    kUfeProxyTransform = 1135

    kDecomposeMatrix = 1136

    kComposeMatrix = 1137

    kBlendMatrix = 1138

    kPickMatrix = 1139

    kAimMatrix = 1140

    kPrimitiveFalloff = 1141

    kBlendFalloff = 1142

    kUniformFalloff = 1143

    kTransferFalloff = 1144

    kComponentFalloff = 1145

    kProximityFalloff = 1146

    kSubsetFalloff = 1147

    kWeightFunctionData = 1148

    kFalloffEval = 1149

    kComponentMatch = 1150

    kPolyUnsmooth = 1151

    kPolyReFormManipContainer = 1152

    kPolyReFormManip = 1153

    kPolyAxis = 1154

    kAngleToDoubleNode = 1155

    kDoubleToAngleNode = 1156

    kAbsolute = 1157

    kACos = 1158

    kAnd = 1159

    kASin = 1160

    kATan = 1161

    kATan2 = 1162

    kAverage = 1163

    kCeil = 1164

    kClampRange = 1165

    kCos = 1166

    kDeterminant = 1167

    kEqual = 1168

    kFloor = 1169

    kGreaterThan = 1170

    kInverseLinearInterpolation = 1171

    kLength = 1172

    kLessThan = 1173

    kLinearInterpolation = 1174

    kLog = 1175

    kMax = 1176

    kMin = 1177

    kModulo = 1178

    kMultiply = 1179

    kNegate = 1180

    kNormalize = 1181

    kNot = 1182

    kOr = 1183

    kPIConstant = 1184

    kPower = 1185

    kRotateVector = 1186

    kRound = 1187

    kSin = 1188

    kSmoothStep = 1189

    kSum = 1190

    kTan = 1191

    kTruncate = 1192

    kDotProduct = 1193

    kCrossProduct = 1194

    kMultiplyPointByMatrix = 1195

    kMultiplyVectorByMatrix = 1196

    kAxisFromMatrix = 1197

    kDivide = 1198

    kSubtract = 1199

    kTranslationFromMatrix = 1200

    kRowFromMatrix = 1201

    kColumnFromMatrix = 1202

    kScaleFromMatrix = 1203

    kRotationFromMatrix = 1204

    kParentMatrix = 1205


class MDataHandle(object):
    """
    Data handle for information contained in a data block.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def acceptedTypeIds(*args, **kwargs):
        """
        acceptedTypeIds() -> array of MTypeIds

        This method returns an array of MTypeIds.
        """
        pass

    def asAddr(*args, **kwargs):
        """
        asAddr() -> long

        Returns the data represented by this handle in the data block.
        """
        pass

    def asAngle(*args, **kwargs):
        """
        asAngle() -> MAngle

        Returns the data represented by this handle in the data block.
        """
        pass

    def asBool(*args, **kwargs):
        """
        asBool() -> bool

        Returns the data represented by this handle in the data block.
        """
        pass

    def asChar(*args, **kwargs):
        """
        asChar() -> int

        Returns the data represented by this handle in the data block.
        """
        pass

    def asDistance(*args, **kwargs):
        """
        asDistance() -> MDistance

        Returns the data represented by this handle in the data block.
        """
        pass

    def asDouble(*args, **kwargs):
        """
        asDouble() -> float

        Returns the data represented by this handle in the data block.
        """
        pass

    def asDouble2(*args, **kwargs):
        """
        asDouble2() -> [float, float]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asDouble3(*args, **kwargs):
        """
        asDouble3() -> [float, float, float]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asFloat(*args, **kwargs):
        """
        asFloat() -> float

        Returns the data represented by this handle in the data block.
        """
        pass

    def asFloat2(*args, **kwargs):
        """
        asFloat2() -> [float, float]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asFloat3(*args, **kwargs):
        """
        asFloat3() -> [float, float, float]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asFloatMatrix(*args, **kwargs):
        """
        asFloatMatrix() -> MFloatMatrix

        Returns the data represented by this handle in the data block.
        """
        pass

    def asFloatVector(*args, **kwargs):
        """
        asFloatVector() -> MFloatVector

        Returns the data represented by this handle in the data block.
        """
        pass

    def asGenericBool(*args, **kwargs):
        """
        asGenericBool() -> bool

        Returns the generic data represented by this handle in the data block.
        """
        pass

    def asGenericChar(*args, **kwargs):
        """
        asGenericChar() -> int

        Returns the generic data represented by this handle in the data block.
        """
        pass

    def asGenericDouble(*args, **kwargs):
        """
        asGenericDouble() -> float

        Returns the generic data represented by this handle in the data block.
        """
        pass

    def asGenericFloat(*args, **kwargs):
        """
        asGenericFloat() -> float

        Returns the generic data represented by this handle in the data block.
        """
        pass

    def asGenericInt(*args, **kwargs):
        """
        asGenericInt() -> int

        Returns the generic data represented by this handle in the data block.
        """
        pass

    def asGenericShort(*args, **kwargs):
        """
        asGenericShort() -> int

        Returns the generic data represented by this handle in the data block.
        """
        pass

    def asInt(*args, **kwargs):
        """
        asInt() -> int

        Returns the data represented by this handle in the data block.
        """
        pass

    def asInt2(*args, **kwargs):
        """
        asInt2() -> [int, int]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asInt3(*args, **kwargs):
        """
        asInt3() -> [int, int, int]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asMatrix(*args, **kwargs):
        """
        asMatrix() -> MMatrix

        Returns the data represented by this handle in the data block.This method is only valid for attributes created using the MFnMatrixAttribute function set.
        """
        pass

    def asMesh(*args, **kwargs):
        """
        asMesh() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set and iterators.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the mesh function set and iterators.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
        pass

    def asMeshTransformed(*args, **kwargs):
        """
        asMeshTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set (MFnMesh) or any of the mesh iterators.

        If the incoming mesh comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the mesh that is returned will be the mesh as it exists in world space.

        The mesh that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
        pass

    def asNurbsCurve(*args, **kwargs):
        """
        asNurbsCurve() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The curve returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the nurbs curve function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
        pass

    def asNurbsCurveTransformed(*args, **kwargs):
        """
        asNurbsCurveTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set (MFnNurbsCurve) or the nurbs curve CV iterator (MItCurveCV).

        If the incoming curve comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the curve that is returned will be the curve as it exists in world space.

        The curve that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
        pass

    def asNurbsSurface(*args, **kwargs):
        """
        asNurbsSurface() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix.  This means that world space operations may be performed on this object using the nurbs surface function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
        pass

    def asNurbsSurfaceTransformed(*args, **kwargs):
        """
        asNurbsSurfaceTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set (MFnNurbsSurface) or the nurbs surface CV iterator (MItSurfaceCV).

        If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

        The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
        pass

    def asPluginData(*args, **kwargs):
        """
        asPluginData() -> MPxData

        Returns the data represented by this handle in the data block.  The object is returned as plugin data.  This should be used to access data types defined by plugins.
        """
        pass

    def asShort(*args, **kwargs):
        """
        asShort() -> int

        Returns the data represented by this handle in the data block.
        """
        pass

    def asShort2(*args, **kwargs):
        """
        asShort2() -> [int, int]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asShort3(*args, **kwargs):
        """
        asShort3() -> [int, int, int]

        Returns the data represented by this handle in the data block.
        """
        pass

    def asString(*args, **kwargs):
        """
        asString() -> MString

        Returns the data represented by this handle in the data block.
        """
        pass

    def asSubdSurface(*args, **kwargs):
        """
        asSubdSurface() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The subdivision surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space   transformation matrix. This means that world space operations may be performed on this object using the subdivision surface function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
        pass

    def asSubdSurfaceTransformed(*args, **kwargs):
        """
        asSubdSurfaceTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set (MFnSubdSurface) or the subdivision surface iterators (MItSubdVertex, MItSubdFace, MItSubdEdge).

        If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

        The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
        pass

    def asTime(*args, **kwargs):
        """
        asTime() -> MTime

        Returns the data represented by this handle in the data block.
        """
        pass

    def asUChar(*args, **kwargs):
        """
        asUChar() -> int

        Returns the data represented by this handle in the data block.
        """
        pass

    def asVector(*args, **kwargs):
        """
        asVector() -> MVector

        Returns the data represented by this handle in the data block.
        """
        pass

    def child(*args, **kwargs):
        """
        child(MPlug) -> MDataHandle
        child(MObject) -> MDataHandle

        Get a handle to a child of this handle.  This is used if you have a handle to a compound attribute.
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(src) -> self

        Copies the attribute from the src attribute to the attribute referenced by this handle.  This is the only method which can completely copy a compound attribute from one handle to another.  The construct outputHandle.set (inputHandle.data()) will not work for compound or multi attributes.

        * src (MDataHandle) - the handle to the attribute to copy.
        """
        pass

    def copyWritable(*args, **kwargs):
        """
        copyWritable(src) -> self

        Copies the attribute from the <i>src</i> attribute to the attribute referenced by this handle.  When the copy is made it ensures that the data in this handle is writable. That is, if the src handle has a writable copy of the data then it will be duplicated, otherwise this handle will claim the writer status for the data.

        * src (MDataHandle) - the handle to the attribute to copy.
        """
        pass

    def data(*args, **kwargs):
        """
        data() -> MObject

        Returns the data object from this handle.  The object returned should be used with the appropriate data function set.  This method is not valid for simple numeric types.
        """
        pass

    def datablock(*args, **kwargs):
        """
        datablock() -> MDataBlock

        Returns a reference to the datablock assigned to this data handle.
        """
        pass

    def geometryTransformMatrix(*args, **kwargs):
        """
        geometryTransformMatrix() -> MMatrix

        This method returns a reference to the local-to-world transformation matrix that can accompany a geometry data object.  Only use this method on handles to geometry data (curves, surfaces, and meshes).

        If no local-to-world transformation information has been provided then this will be an identity matrix.
        """
        pass

    def isGeneric(*args, **kwargs):
        """
        isGeneric() -> [bool, isNumeric, isNull]

        Returns True if this handle is for generic data.  There are 2 forms of generic data.  The first is for simple data and is used if the isNumeric parameter returns True.  In this case, the asGeneric*() and setGeneric*() methods of this class are used to query and set values.
        The second form of generic data is for more complex attribute types.  As a result the type of the object must be checked and an appropriate attribute function set initialized with the object.Returns isNumeric True if this handle is for simple generic numeric data.
        Returns isNull True if this handle is not set.
        """
        pass

    def isNumeric(*args, **kwargs):
        """
        isNumeric() -> bool

        Returns True if this handle is for simple numeric data. That means that the numeric data is directly accessible through the non-generic as*() and set*() methods of this handle. For example, depending on handle initialization, the asBool() may be called but the asGenericBool() should not be called.
        """
        pass

    def numericType(*args, **kwargs):
        """
        numericType() -> int

        Returns the type of data represented by this handle.  This method is only valid for data handles of simple numeric types.
        """
        pass

    def set2Double(*args, **kwargs):
        """
        set2Double(float, float) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set2Float(*args, **kwargs):
        """
        set2Float(float, float) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set2Int(*args, **kwargs):
        """
        set2Int(int, int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set2Short(*args, **kwargs):
        """
        set2Short(int, int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set3Double(*args, **kwargs):
        """
        set3Double(float, float, float) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set3Float(*args, **kwargs):
        """
        set3Float(float, float, float) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set3Int(*args, **kwargs):
        """
        set3Int(int, int, int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def set3Short(*args, **kwargs):
        """
        set3Short(int, int, int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setBool(*args, **kwargs):
        """
        setBool(bool) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setChar(*args, **kwargs):
        """
        setChar(int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setClean(*args, **kwargs):
        """
        setClean() -> self

        Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.
        """
        pass

    def setDouble(*args, **kwargs):
        """
        setDouble(float) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setFloat(*args, **kwargs):
        """
        setFloat(float) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setGenericBool(*args, **kwargs):
        """
        setGenericBool(bool, force) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setGenericChar(*args, **kwargs):
        """
        setGenericChar(int, force) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setGenericDouble(*args, **kwargs):
        """
        setGenericDouble(float, force) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setGenericFloat(*args, **kwargs):
        """
        setGenericFloat(float, force) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setGenericInt(*args, **kwargs):
        """
        setGenericInt(int, force) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setGenericShort(*args, **kwargs):
        """
        setGenericShort(int, force) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setInt(*args, **kwargs):
        """
        setInt(int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMAngle(*args, **kwargs):
        """
        setMAngle(MAngle) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMDistance(*args, **kwargs):
        """
        setMDistance(MDistance) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMFloatMatrix(*args, **kwargs):
        """
        setMFloatMatrix(MFloatMatrix) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMFloatVector(*args, **kwargs):
        """
        setMFloatVector(MFloatVector) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMMatrix(*args, **kwargs):
        """
        setMMatrix(MMatrix) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMObject(*args, **kwargs):
        """
        setMObject(MObject) -> self

        Set the data that this handle represents in the data block.  This method assumes that the MObject is a dependency graph data object.  These objects can be created using the appropriate MFn..Data function set.
        Note that this method cannot be used to copy compound or multi attributes from one handle to another via the construct outputHandle.set (inputHandle.data()).
        To copy these user defined attributes, the method MDataHandle.copy() must be used.
        """
        pass

    def setMPxData(*args, **kwargs):
        """
        setMPxData(MPxData) -> self

        Set the data that this handle represents in the data block.  This method takes a pointer to a user defined data object.  The data block will become the new owner of the data object that you pass in.  Do not delete it.
        """
        pass

    def setMTime(*args, **kwargs):
        """
        setMTime(MTime) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setMVector(*args, **kwargs):
        """
        setMVector(MVector) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setShort(*args, **kwargs):
        """
        setShort(int) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def setString(*args, **kwargs):
        """
        setString(string) -> self

        Set the data that this handle represents in the data block.
        """
        pass

    def type(*args, **kwargs):
        """
        type() -> int

        Returns the type of data represented by this handle.
        """
        pass

    def typeId(*args, **kwargs):
        """
        typeId() -> MTypeId

        Returns the type of data represented by this handle as a type id.  A type id is a four character code that is used to identify the data type.
        If no data exists for this handle, the type id will be 0x0.
        """
        pass


class MPoint(object):
    """
    3D point with double-precision coordinates.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __div__(*args, **kwargs):
        """
        x.__div__(y) <==> x/y
        """
        pass

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __isub__(*args, **kwargs):
        """
        x.__isub__(y) <==> x-=y
        """
        pass

    def __iter__(self):
        for _ in range(3):
            yield 0.0

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __radd__(*args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __rdiv__(*args, **kwargs):
        """
        x.__rdiv__(y) <==> y/x
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(*args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def __sub__(*args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def cartesianize(*args, **kwargs):
        """
        Convert point to cartesian form.
        """
        pass

    def distanceTo(*args, **kwargs):
        """
        Return distance between this point and another.
        """
        pass

    def homogenize(*args, **kwargs):
        """
        Convert point to homogenous form.
        """
        pass

    def isEquivalent(*args, **kwargs):
        """
        Test for equivalence of two points, within a tolerance.
        """
        pass

    def rationalize(*args, **kwargs):
        """
        Convert point to rational form.
        """
        pass

    kOrigin = None

    kTolerance = 1e-10

    w = None

    x = None

    y = None

    z = None


class MItMeshVertex(object):
    """
    This class is the iterator for polygonal surfaces (meshes).
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def connectedToEdge(*args, **kwargs):
        """
        connectedToEdge(index) -> bool

        This method determines whether the given edge contains the current vertex

        * index (int) - Index of edge to check.
        """
        pass

    def connectedToFace(*args, **kwargs):
        """
        connectedToFace(index) -> bool

        This method determines whether the given face contains the current vertex

        * index (int) - Index of face to check.
        """
        pass

    def count(*args, **kwargs):
        """
        count() -> int

        Return the number of vertices in the iteration
        """
        pass

    def currentItem(*args, **kwargs):
        """
        currentItem() -> MObject

        Get the current vertex in the iteration as a component.

        Components are used to specify one or more vertices and are usefull in operating on groups of non-contiguous vertices for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
        pass

    def geomChanged(*args, **kwargs):
        """
        geomChanged() -> self

        Reset the geom pointer in the MItMeshVertex. If you're using MFnMesh to
        update Normals or Color per vertex while iterating, you must call geomChanged
        on the iteratior immediately after the MFnMesh call to make sure that your
        geometry is up to date. A crash may result if this method is not called.
        A similar approach must be taken for updating upstream vertex tweaks
        with an MPlug. After the update, call this method.
        """
        pass

    def getColor(*args, **kwargs):
        """
        getColor(colorSetName=None) -> MColor
        getColor(faceIndex, colorSetName=None) -> MColor

        This method gets the average color of the vertex

        * colorSetName (string) - Name of the color set.

        This method gets the color of the current vertex in the specified face

        * index (int) - The face to get the color for this vertex for* colorSetName (string) - Name of the color set.
        """
        pass

    def getColorIndices(*args, **kwargs):
        """
        getColorIndices(colorSetName=None) -> MIntArray

        This method returns the colorIndices into the color array see MFnMesh::getColors()
        of the current vertex.

        * colorSetName (string) - Name of the color set.
        """
        pass

    def getColors(*args, **kwargs):
        """
        getColors(colorSetName=None) -> MColorArray

        This method gets the colors of the current vertex for each face it
        belongs to. If no colors are assigned to the vertex at all, the
        return values will be (-1 -1 -1 1). If some but not all of the
        vertex/face colors have been explicitly set, the ones that have not
        been set will be (0, 0, 0, 1).

        * colorSetName (string) - Name of the color set.
        """
        pass

    def getConnectedEdges(*args, **kwargs):
        """
        getConnectedEdges() -> MIntArray

        This method gets the indices of the edges contained in the current vertex.
        """
        pass

    def getConnectedFaces(*args, **kwargs):
        """
        getConnectedFaces() -> MIntArray

        This method gets the indices of the faces connected to the current vertex.
        """
        pass

    def getConnectedVertices(*args, **kwargs):
        """
        getConnectedVertices() -> MIntArray

        This method gets the indices of the vertices surrounding the current vertex.
        """
        pass

    def getNormal(*args, **kwargs):
        """
        getNormal(space=kObject) -> MVector
        getNormal(faceIndex, space=kObject) -> MVector

        Return the normal or averaged normal if unshared of the current vertex.

        * space (int) - The transformation space

        Return the normal of the current vertex in the specified face.

        * faceIndex (int) - face index to get normal for
        * space (int) - The transformation space
        """
        pass

    def getNormalIndices(*args, **kwargs):
        """
        getNormalIndices() -> MIntArray

        This method returns the normal indices of the face/vertex associated
        with the current vertex.
        """
        pass

    def getNormals(*args, **kwargs):
        """
        getNormals(space=kObject) -> MVectorArray

        Return the normals of the current vertex for all faces

        * space (int) - The transformation space
        """
        pass

    def getOppositeVertex(*args, **kwargs):
        """
        getOppositeVertex(edgeId) -> int

        This method gets the other vertex of the given edge

        * edgeId (int) - The edge to get the other vertex for
        """
        pass

    def getUV(*args, **kwargs):
        """
        getUV(uvSet=None) -> [float, float]getUV(faceId, uvSet=None) -> [float, float]

        Get the shared UV value at this vertex.

        * uvSet (string) - Name of the uv set to work with.

        Get the UV value for the give facen at the current vertex.

        * faceId (int) - Index of the required face
        * uvSet (string) - Name of the uv set to work with
        """
        pass

    def getUVIndices(*args, **kwargs):
        """
        getUVIndices(uvSet=None) -> MIntArray

        This method returns the uv indices into the normal array see MFnMesh::getUVs()
        of the current vertex.

        * uvSet (string) - Name of the uv set.
        """
        pass

    def getUVs(*args, **kwargs):
        """
        getUVs(uvSet=None) -> [MFloatArray, MFloatArray, MIntArray]

        Get the UV values for all mapped faces at the current vertex.
        If at least one face was mapped the method will succeed.

        * uvSet (string) - Name of the uv set to work with
        """
        pass

    def hasColor(*args, **kwargs):
        """
        hasColor() -> bool
        hasColor(index) -> bool

        This method determines whether the current Vertex has a color set
        for one or more faces.

        * index (int) - Index of face to check
        """
        pass

    def index(*args, **kwargs):
        """
        index() -> int

        Returns the index of the current vertex in the vertex list for this
        polygonal object.
        Polygonal objects contain a list of vertices. Faces and edges are
        specified as indicies from this list, in this way vertices can
        be shared amoung faces and edges.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Indicates if all of the vertices have been traversed yet.
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advance to the next edge in the iteration.
        """
        pass

    def numConnectedEdges(*args, **kwargs):
        """
        numConnectedEdges() -> int

        This Method checks for the number of connected Edges on this vertex
        """
        pass

    def numConnectedFaces(*args, **kwargs):
        """
        numConnectedFaces() -> int

        This Method checks for the number of Connected Faces
        """
        pass

    def numUVs(*args, **kwargs):
        """
        numUVs(uvSet=None) -> int

        This method returns the number of unique UVs mapped on this vertex

        * uvSet (string) - Name of the uv set to work with
        """
        pass

    def onBoundary(*args, **kwargs):
        """
        onBoundary() -> bool

        This method determines whether the current vertex is on a Boundary
        """
        pass

    def position(*args, **kwargs):
        """
        position(space=kObject) -> MPoint

        Return the position of the current vertex in the specified space.
        Object space ignores all transformations for the polygon, world space
        includes all such transformations.

        * space (int) - The  transformation space
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(polyObject) -> self
        reset(polyObject, component=None) -> self

        Reset the iterator to the first polygon

        Reset the iterator to the first polygon in the supplied polygon

        * polyObject (MObject) - The polygon for the iteration

        Reset the iterator with the given surface and component.
        If component is None then the iteration will be for all vertices in the given polygon.

        * polyObject (MDagPath) - The surface (mesh) to iterate over
        * component (MObject) - The vertices of the polyObject to iterate over
        """
        pass

    def setIndex(*args, **kwargs):
        """
        setIndex(index) -> int

        This method sets the index of the current vertex to be accessed.
        The current vertex will no longer be in sync with any previous iteration.

        * index (int) - The index of desired vertex to access.
        """
        pass

    def setPosition(*args, **kwargs):
        """
        setPosition(point, space=kObject) -> self

        Set the position of the current vertex in the given space.

        * point (MPoint) - The new position for the current vertex
        * space (int) - The Transformation space
        """
        pass

    def setUV(*args, **kwargs):
        """
        setUV(uvPoint, uvSet=None) -> selfsetUV(faceId, uvPoint, uvSet=None) -> self

        Set the shared UV value at this vertex

        * uvPoint ([float, float]) - The UV values to set
        * uvSet (string) - Name of the UV set to work with

        Set the UV value for the given face at the current vertex

        * faceId (int) - Index of required face
        * uvPoint ([float, float]) - The UV values to set
        * uvSet (string) - Name of the UV set to work with
        """
        pass

    def setUVs(*args, **kwargs):
        """
        setUVs(uArray, vArray, faceIds, uvSet=None) -> self

        Set the UV value for the specified faces at the current vertex.
        If the face is not already mapped, the value will not be set.
        If at least ne face was previously mapped, the method should succeed.
        If no faces were mapped, the method will fail.

        * uArray (MFloatArray) - All the U values - in local face order
        * vArray (MFloatArray) - The corresponding V values
        * faceIds (MIntArray) - The corresponding face Ids
        * uvSet (string) - UV set to work with
        """
        pass

    def translateBy(*args, **kwargs):
        """
        translateBy(vector, space=kObject) -> self

        Translate the current vertex by the amount specified
        by the given vector.

        * vector (MVector) - The amount of translation
        * space (int) - The Transformation space
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        Signal that this polygonal surface has changed and needs to redraw itself.
        """
        pass


# noinspection PyPep8Naming
class MObject(object):
    """
    Opaque wrapper for internal Maya objects.
    """

    def __eq__(self, other: 'MObject') -> bool:
        """
        x.__eq__(y) <==> x==y
        """
        return self._uuid == other._uuid

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(self, *args, **kwargs): 
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._uuid = uuid.uuid4()
        self._name = str(self._uuid)
        self._api_type: list[int] = [MFn.kInvalid]
        self._alive: bool = False
        self._typeId: "MTypeId" = None
        self._parent: Optional['MObject'] = None
        self._children = []
        self._is_world = False
        self._cached_plugs = {}
        self._attributes = {}

        # plug-specific properties
        if MFn.kAttribute in self._api_type:
            self._init_attribute_fields()

    def _init_attribute_fields(self):
        self._owner: 'MObject' = None

        self._long_name: str = None
        self._short_name: str = None

        self._value = None

        self._is_array = False
        self._is_compound = False
        self._is_element = False

        self._numeric_type: int = MFnNumericData.kInvalid

        self._affects_appearance = False
        self._affects_world_space = False
        self._channel_box = False
        self._connectable = True
        self._disconnect_behavior = MFnAttribute.kNothing
        self._dynamic = False
        self._extension = None
        self._hidden = False
        self._indeterminant = None
        self._index_matters = False
        self._internal = False
        self._readable = True
        self._render_source = False
        self._storable = False
        self._used_as_color = False
        self._used_as_filename = False
        self._uses_array_data_builder = False
        self._world_space = False
        self._writeable = True

    def _init_numeric_fields(self):
        self._min = None
        self._max = None
        self._soft_min = None
        self._soft_max = None
        self._default = None
        self._numeric_type = None

    def _init_typed_fields(self):
        self._typed_attr_type: int = MFnData.kInvalid

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __repr__(self):
        return f'MObject <{self.apiTypeStr}>; name = {self._name}'

    def apiType(self) -> int:
        """
        Returns the function set type for the object.
        """
        if self._is_world:
            return MFn.kWorld
        elif len(self._api_type) > 0:
            return self._api_type[-1]
        else:
            typ_str = self.apiTypeStr
            return getattr(MFn, f'k{typ_str[0].upper()}{typ_str[1:]}')

    def hasFn(self, compare_fn_type: int) -> bool:
        """
        Tests whether object is compatible with the specified function set.
        """
        return compare_fn_type in self._api_type

    def isNull(self) -> bool:
        """
        Tests whether there is an internal Maya object.
        """
        return not self._alive

    def __hash__(self):
        return hash(self._uuid)

    @property
    def apiTypeStr(self):
        if self._is_world:
            return 'kWorld'
        elif len(self._api_type) > 0:
            return _API_TYPES_INT_TO_STR.get(self._api_type[-1])
        elif self._typeId is not None:
            return _TYPE_INT_TO_STR.get(self._typeId.id(), 'kInvalid')
        else:
            raise TypeError(f'Could not identify api type for: {self}')

    @classmethod
    def kNullObj(cls) -> 'MObject':
        return MObject()


class MFloatPointArray(object):
    """
    Array of MFloatPoint values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MTransformationMatrix(object):
    """
    Manipulate the individual components of a transformation.
    """

    def __eq__(self, *args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(self, *args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(self, *args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __le__(self, *args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(self, *args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(self, *args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def asMatrix(self, *args, **kwargs):
        """
        Interpolates between the identity transformation and that currently in the object, returning the result as an MMatrix.
        """
        pass

    def asMatrixInverse(self, *args, **kwargs):
        """
        Returns the inverse of the matrix representing the transformation.
        """
        pass

    def asRotateMatrix(self, *args, **kwargs):
        """
        Returns the matrix which takes points from object space to the space immediately following the scale/shear/rotation transformations.
        """
        pass

    def asScaleMatrix(self, *args, **kwargs):
        """
        Returns the matrix which takes points from object space to the space immediately following scale and shear transformations.
        """
        pass

    def isEquivalent(self, *args, **kwargs):
        """
        Returns true if this transformation's matrix is within tolerance of another's matrix.
        """
        pass

    def reorderRotation(self, *args, **kwargs):
        """
        Reorders the transformation's rotate component to give the same overall rotation but using a new order or rotations.
        """
        pass

    def rotateBy(self, *args, **kwargs):
        """
        Adds to the transformation's rotation component.
        """
        pass

    def rotateByComponents(self, *args, **kwargs):
        """
        Adds to the transformation's rotation component.
        """
        pass

    def rotatePivot(self, *args, **kwargs):
        """
        Returns the transformation's rotate pivot component.
        """
        pass

    def rotatePivotTranslation(self, *args, **kwargs):
        """
        Returns the transformation's rotate pivot translation component.
        """
        pass

    def rotation(self, *args, **kwargs):
        """
        Returns the transformation's rotation component as either an Euler rotation or a quaternion.
        """
        pass

    def rotationComponents(self, *args, **kwargs):
        """
        Returns a list containing the four components of the transformation's rotate component.
        """
        pass

    def rotationOrder(self, *args, **kwargs):
        """
        Returns the order of rotations when the transformation's rotate component is expressed as an euler rotation.
        """
        pass

    def rotationOrientation(self, *args, **kwargs):
        """
        Returns a quaternion which orients the local rotation space.
        """
        pass

    def scale(self, *args, **kwargs):
        """
        Returns a list containing the transformation's scale components.
        """
        pass

    def scaleBy(self, *args, **kwargs):
        """
        Multiplies the transformation's scale components by the three floats in the provided sequence.
        """
        pass

    def scalePivot(self, *args, **kwargs):
        """
        Returns the transformation's scale pivot component.
        """
        pass

    def scalePivotTranslation(self, *args, **kwargs):
        """
        Returns the transformation's scale pivot translation component.
        """
        pass

    def setRotatePivot(self, *args, **kwargs):
        """
        Sets the transformation's rotate pivot component.
        """
        pass

    def setRotatePivotTranslation(self, *args, **kwargs):
        """
        Sets the transformation's rotate pivot translation component.
        """
        pass

    def setRotation(self, *args, **kwargs):
        """
        Sets the transformation's rotation component.
        """
        pass

    def setRotationComponents(self, *args, **kwargs):
        """
        Sets the transformation's rotate component from the four values in the provided sequence.
        """
        pass

    def setRotationOrientation(self, *args, **kwargs):
        """
        Sets a quaternion which orients the local rotation space.
        """
        pass

    def setScale(self, *args, **kwargs):
        """
        Sets the transformation's scale components to the three floats in the provided sequence.
        """
        pass

    def setScalePivot(self, *args, **kwargs):
        """
        Sets the transformation's scale pivot component.
        """
        pass

    def setScalePivotTranslation(self, *args, **kwargs):
        """
        Sets the transformation's scale pivot translation component.
        """
        pass

    def setShear(self, *args, **kwargs):
        """
        Sets the transformation's shear component.
        """
        pass

    def setToRotationAxis(self, *args, **kwargs):
        """
        Sets the transformation's rotate component to be a given axis vector and angle in radians.
        """
        pass

    def setTranslation(self, *args, **kwargs):
        """
        Sets the transformation's translation component.
        """
        pass

    def shear(self, *args, **kwargs):
        """
        Returns a list containing the transformation's shear components.
        """
        pass

    def shearBy(self, *args, **kwargs):
        """
        Multiplies the transformation's shear components by the three floats in the provided sequence.
        """
        pass

    def translateBy(self, *args, **kwargs):
        """
        Adds a vector to the transformation's translation component.
        """
        pass

    def translation(self, *args, **kwargs):
        """
        Returns the transformation's translation component as a vector.
        """
        pass

    kIdentity = None

    kInvalid = 0

    kLast = 7

    kTolerance = 1e-10

    kXYZ = 1

    kXZY = 4

    kYXZ = 5

    kYZX = 2

    kZXY = 3

    kZYX = 6


class MPointArray(object):
    """
    Array of MPoint values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MMessage(object):
    """
    Base class for message callbacks.
    """

    @staticmethod
    def currentCallbackId(*args, **kwargs):
        """
        currentCallbackId() -> id

        Returns the callback ID of the currently executing callback. If called
        outside of a callback, an invalid MCallbackId and failed status will
        be returned.
        """
        pass

    @staticmethod
    def nodeCallbacks(*args, **kwargs):
        """
        nodeCallbacks(node) -> ids

        Returns a list of callback IDs registered to a given node.

         * node (MObject) - Node to query for callbacks.
         * ids (MCallbackIdArray) - Array to store the list of callback IDs.
        """
        pass

    @staticmethod
    def removeCallback(*args, **kwargs):
        """
        removeCallback(id) -> None

        Removes the specified callback from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.

         * id (MCallbackId) - identifier of callback to be removed
        """
        pass

    @staticmethod
    def removeCallbacks(*args, **kwargs):
        """
        removeCallbacks(ids) -> None

        Removes all of the specified callbacks from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.

         * idList (MCallbackIdArray) - list of callbacks to be removed.
        """
        pass

    kDefaultAction = 0

    kDoAction = 2

    kDoNotDoAction = 1


class MDGContext(object):
    """
    Dependency graph context.
    """

    def __init__(*args, time=None, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__()

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source context.

        * source (MDGContext) - The source object to copy from
        """
        pass

    def getTime(*args, **kwargs):
        """
        Returns the time at which this context is set to evaluate.
        """
        pass

    def isCurrent(*args, **kwargs):
        """
        Returns True if the context is currently being used for evaluation. Returns False if some other context is being used for evaluation.
        """
        pass

    def isNormal(*args, **kwargs):
        """
        Returns True if the context is set to evaluate normally. Returns False if the context is set to evaluate at a specific time.
        """
        pass

    def makeCurrent(*args, **kwargs):
        """
        Makes this context the new current one being used for evaluation. Returns the previous evaluation context.
        """
        pass

    @staticmethod
    def current(*args, **kwargs):
        """
        Returns the current context being used for evaluation.
        """
        pass

    kNormal = None


class MSpace(object):
    """
    Static class providing coordinate space constants.
    """

    kInvalid = 0

    kLast = 5

    kObject = 2

    kPostTransform = 3

    kPreTransform = 2

    kTransform = 1

    kWorld = 4


class MTime(object):
    """
    Manipulate time data.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __div__(*args, **kwargs):
        """
        x.__div__(y) <==> x/y
        """
        pass

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __idiv__(*args, **kwargs):
        """
        x.__idiv__(y) <==> x/=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __isub__(*args, **kwargs):
        """
        x.__isub__(y) <==> x-=y
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __radd__(*args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __rdiv__(*args, **kwargs):
        """
        x.__rdiv__(y) <==> y/x
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(*args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def __sub__(*args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def asUnits(*args, **kwargs):
        """
        Return the time value, converted to the specified units.
        """
        pass

    @staticmethod
    def setUIUnit(*args, **kwargs):
        """
        Change the units used to display time in Maya's UI.
        """
        pass

    @staticmethod
    def ticksPerSecond(*args, **kwargs):
        """
        Returns the number of ticks per second, the smallest unit of time available.
        """
        pass

    @staticmethod
    def uiUnit(*args, **kwargs):
        """
        Return the units used to display time in Maya's UI.
        """
        pass

    k100FPS = 25

    k10FPS = 18

    k1200FPS = 38

    k120FPS = 26

    k125FPS = 27

    k12FPS = 19

    k1500FPS = 39

    k150FPS = 28

    k15FPS = 5

    k16FPS = 20

    k2000FPS = 40

    k200FPS = 29

    k20FPS = 21

    k23_976FPS = 43

    k240FPS = 30

    k24FPS = 6

    k250FPS = 31

    k25FPS = 7

    k29_97DF = 45

    k29_97FPS = 44

    k2FPS = 12

    k3000FPS = 41

    k300FPS = 32

    k30FPS = 8

    k375FPS = 33

    k3FPS = 13

    k400FPS = 34

    k40FPS = 22

    k44100FPS = 48

    k47_952FPS = 46

    k48000FPS = 49

    k48FPS = 9

    k4FPS = 14

    k500FPS = 35

    k50FPS = 10

    k59_94FPS = 47

    k5FPS = 15

    k6000FPS = 42

    k600FPS = 36

    k60FPS = 11

    k6FPS = 16

    k750FPS = 37

    k75FPS = 23

    k80FPS = 24

    k8FPS = 17

    k90FPS = 50

    kFilm = 6

    kGames = 5

    kHours = 1

    kInvalid = 0

    kLast = 52

    kMilliseconds = 4

    kMinutes = 2

    kNTSCField = 11

    kNTSCFrame = 8

    kPALField = 10

    kPALFrame = 7

    kSeconds = 3

    kShowScan = 9

    kUserDef = 51

    unit = None

    value = None


class MArrayDataHandle(object):
    """
    Data block handle for array data.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def builder(*args, **kwargs):
        """
        builder() -> MArrayDataBuilder

        Returns a builder for this handle's array so that it can be expanded.

        This method will raise an exception if the current array does not support array data builders. This can be changed in a node's initialize routine using the usesArrayDataBuilder attribute in MFnAttribute.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source array.

        * source (MArrayDataHandle) - The source object to copy from
        """
        pass

    def elementLogicalIndex(*args, **kwargs):
        """
        elementLogicalIndex() -> int

        Returns the index that we are currently at in the array.  It is possible for the index to be invalid, in which case the return status will report an error.  These may be sparse arrays so the element index returned will be a logical index.

        Raises an exception if there is no current element (e.g. if there are no elements).
        """
        pass

    def inputArrayValue(*args, **kwargs):
        """
        inputArrayValue() -> MArrayDataHandle

        Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
        pass

    def inputValue(*args, **kwargs):
        """
        inputValue() -> MDataHandle

        Gets a handle into this data block for the current array element.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Specifies whether or not there are more elements to iterate over.
        """
        pass

    def jumpToLogicalElement(*args, **kwargs):
        """
        jumpToLogicalElement(index) -> self

        Jump to a specific logical element in the array.
        Since the logical array is sparse its indices may not be consecutive and a binary search is used internally to find the element.
        Thus when iterating through the elements of the array it is much faster to do so using physical indices.

        * index (int) - the logical index to jump to
        """
        pass

    def jumpToPhysicalElement(*args, **kwargs):
        """
        jumpToPhysicalElement(position) -> self

        Jump to a specific physical element in the array.
        Since physical elements are contiguous no search is required.

        * position (int) - the array position to jump to
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> bool

        Advance to the next element in the array.
        Return True if there was a next element and False if there wasn't.
        """
        pass

    def outputArrayValue(*args, **kwargs):
        """
        outputArrayValue() -> MArrayDataHandle

        Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays. The array's elements are not evaluated and may no longer be valid. Therefore, this handle should only be used for writing over the data.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
        pass

    def outputValue(*args, **kwargs):
        """
        outputValue() -> MDataHandle

        Gets a handle into this data block for the current array element. The element is not evaluated so its data may not be valid. Therefore, this handle should only be used for writing over the data.

        This method can also be used to retrieve handles to individual elements of  non-datablock array handles, such as those returned by MPlug.getValue() and MPlug.asMDataHandle().
        """
        pass

    def set(*args, **kwargs):
        """
        set(builder) -> self

        Sets the data for this array from the data in the builder object

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().

        * builder (MArrayDataBuilder) - the builder object
        """
        pass

    def setAllClean(*args, **kwargs):
        """
        setAllClean() -> self

        Marks every element of the array attribute represented by the handle as clean.  This method should be used if a compute function is asked to compute a single element of a multi, but instead calculates all the elements.  Calling <i>setAllClean</i> in this situation will prevent further calls to the node's compute method for the other elements of the multi.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()
        """
        pass

    def setClean(*args, **kwargs):
        """
        setClean() -> self

        Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
        pass


class MIteratorType(object):
    """
    The MIteratorType class is used on iterators where more than one type
    of filters can be specified. It also provides functionalities to set and
    get the filter list or individual types of filter. This class should be
    used in conjunction with DAG/DG/DependencyNodes iterators for using filter
    list (list of MFn::Type objects) on them, thus enabling faster traversal
    thro' iterators.

    Also, the class has functionalities for specifying the type of object the
    iterator will be reset to. This could be an MObject, an MPlug or an MDagPath.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    filterList = None

    filterListEnabled = None

    filterType = None

    kMDagPathObject = 1

    kMObject = 0

    kMPlugObject = 2

    objectType = None


class MFileObject(object):
    """
    Manipulate filenames and search paths.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source file object.

        * source (MFileObject) - The source file object to copy from
        """
        pass

    def exists(*args, **kwargs):
        """
        exists(index=None) -> bool

        Checks to see if the file exists and is readable.
        If index is None tests for the fullName file, else tests the file constructed from the indicated portion of the path element and filename element.

        * index (int) - Index of the path element to be used in searching for the file.
        """
        pass

    def expandedFullName(*args, **kwargs):
        """
        expandedFullName() -> string

        Returns the pathname of a file constructed from the unresolved file object values. The file name will consist of the the expanded raw path and raw name elements.
        All variables in the path element are expanded, and the first path (the part before the first separator (':') in the path) is prepended to the filename element to construct the fullName.

        After expanding environment variables Maya may perform additional modifications to the full file name in order to resolve it to a valid location on disk. This resolved full file name can be accessed through resolvedFullName().
        """
        pass

    def expandedPath(*args, **kwargs):
        """
        expandedPath() -> string

        Returns the raw path element of the unresolved file object with all environment variables expanded. In the case that the path expands to multiple paths, the first expanded path will be returned.

        After expanding environment variables Maya may perform additional modifications to the path in order to resolve it to a valid location on disk. This resolved path can be accessed through resolvedPath().
        """
        pass

    def fullName(*args, **kwargs):
        """
        fullName(index) -> string

        Returns the pathname of a file constructed from the indicated portion of the path element and filename element.
        All variables in the path element are expanded, and the indicated path portion is prepended to the filename element to construct the fullName.

        * index (int) - the index of the desired path portion.
        """
        pass

    def isSet(*args, **kwargs):
        """
        isSet() -> bool

        Checks to see if both file and path elements of the file object have been set.
        """
        pass

    def overrideResolvedFullName(*args, **kwargs):
        """
        overrideResolvedFullName(fullFileName, reresolveType=False) -> self

        Normally when a raw file name is set, Maya will perform a series of operations on it in an attempt to resolve it to a valid file name. This final resolved file name can be accessed through the resolvedName(), resolvedPath(), and resolvedFullFileName() methods and can be quite different from the originally specified raw file name.

        This method will override the normal Maya path resolution process and explicitly set the resolved file name. This path does not have to be a valid file path, but if any '/' characters appear in the given name then the resolved path element of the file object is set to everything in name up to, but not including the last '/'. The resolved filename is set to the part of name after the final '/'.

        Once the resolved file name is set, it is only guaranteed to be retained in the file object so long as the raw file path is not updated. Once the rawPath, rawName or rawFullName are set, the normal Maya path resolution process will be re-invoked and the resolved path and filename will be updated.

        - fullFileName (string) - the string used to override the path and filename.- reresolveType (bool) - if Maya should re-resolve the file type/translator.
        """
        pass

    def path(*args, **kwargs):
        """
        path(index) -> string

        Returns the indicated portion of the path element of the file object.  All variables in the path element are expanded, and the portion indicated by the argument is extracted and returned.

        * index (int) - the index of the desired path portion.
        """
        pass

    def pathCount(*args, **kwargs):
        """
        pathCount() -> int

        Returns the number of paths in the path element of the file object.
        This will be equal to one more than the number of ':' characters specified of the rawPath attribute.
        """
        pass

    def rawFullName(*args, **kwargs):
        """
        rawFullName() -> string

        Returns the unresolved full file name (path plus filename) of the MFileObject with all environment variables unexpanded.

        This method differs from expandedFullName() in that it returns the unexpanded instead of expanded values.
        """
        pass

    def rawName(*args, **kwargs):
        """
        rawName() -> string

        Returns the unresolved filename element of the MFileObject.
        """
        pass

    def rawPath(*args, **kwargs):
        """
        rawPath() -> string

        Returns the path element of the MFileObject with all environment variables unexpanded.
        """
        pass

    def rawURI(*args, **kwargs):
        """
        rawURI() -> MURI

        Returns the unresolved URI of the MFileObject, if any.

        This will be empty if the MFileObject was not resolved from a URI.
        """
        pass

    def resolvedFullName(*args, **kwargs):
        """
        resolvedFullName() -> string

        Returns the first pathname of a file constructed from the path and filename elements.  All variables in the path element are expanded, and the first path (the part before the first ':' in the path) is prepended to the filename element. After expanding all environment     variables Maya may then perform additional modifications, such  as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.

        The resolution is performed using the ResolveMethod of the file object.
        By default, this will be set to kNone. While this is suitable in many situations, it may not be appropriate if the file is expected to exist.
        Refer to getResolvedFullNameAndExistsStatus() for more information about how the  resolution mode is used.

        Failure to resolve the path according to the specifications of the file object will result in an empty return value.
        """
        pass

    def resolvedName(*args, **kwargs):
        """
        resolvedName() -> string

        Returns the resolved filename element of the file object.
        """
        pass

    def resolvedPath(*args, **kwargs):
        """
        resolvedPath() -> string

        Returns the resolved path element of the file object. In order to build the resolved path, Maya first expands all environment variables and then may perform additional modifications, such as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.
        """
        pass

    def setRawFullName(*args, **kwargs):
        """
        setRawFullName(fullFileName) -> self

        This method combines the functions of the setRawName and setRawPath methods in that it sets both the path and filename from the given name.

        If any '/' characters appear in the given name then the path element of the MFileObject is set to everything in name up to, but not including the last '/'.  The filename is set to the part of name after the final '/'.

        If no '/' characters appear in the given name then the path element is set to "." and the filename is set to the given name.

        Note that if the specified fullFileName is relative, contains environment variables, or does not exist, the full names returned by resolvedFullName() and expandedFullName() may not match the fullFileName. See the description of resolvedFullName() and expandedFullName() for more information.

        Also note that for URI-based file paths (e.g. "arrow:uri_path_to_file"),  setRawFullName will not call setRawName and setRawPath (raw name and path will remain empty). Use resolvedName and resolvedPath to retrieve the resolved file path, or rawFullName to retrieve the unresolved file path.

        * fullFileName (string) - The string used to initialize the path and filename.
        """
        pass

    def setRawName(*args, **kwargs):
        """
        setRawName(fileName) -> self

        Set the unresolved filename element of the MFileObject instance.  This name should not contain any '/' characters, it should indicate simply the name of a file.  The directories in which this name will be searched for are specified by setRawPath.

        * fileName (string) - The filename to set.
        """
        pass

    def setRawPath(*args, **kwargs):
        """
        setRawPath(pathName) -> self

        Set the unresolved path element of the MFileObject instance.  This should contain a list of directories, each separated by a single ':' character.  The pathnames can contain Unix environment variables in the form $VARNAME.  These will be expanded when paths to actual filenames are constructed.

        Note that if the specified pathName is relative, contains environment variables, or does not exist, the paths returned by resolvedPath() and expandedPath() may not match the rawPath. See the description of resolvedPath() and expandedPath() for more information.

        * pathName (string) - The path string.
        """
        pass

    def setRawURI(*args, **kwargs):
        """
        setRawURI(uri) -> self

        Set the unresolved URI of the MFileObject instance.

        * uri (string or MURI) - The unresolved URI.
        """
        pass

    @staticmethod
    def getResolvedFullName(*args, **kwargs):
        """
        getResolvedFullName(rawFullName) -> string

        Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful.

        * rawFullName (string) - The fully specified unresolved path.
        """
        pass

    @staticmethod
    def getResolvedFullNameAndExistsStatus(*args, **kwargs):
        """
        getResolvedFullNameAndExistsStatus(rawFullName, method=kNone) -> (string, bool)

        Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful, and a boolean that indicate if the resolved path exists or not.

        * rawFullName (string) - The fully specified unresolved path
        * resolveMethod (int) - To resolve method to use, default is kNone.

        Valid resolve methods:
          kNone                    The resolved path is simply the resulting path after converting
                                   the raw value to its expanded form. If the path contains environment variables,
                                   the resolved value will be the first path returned from their expansion.
                                   Relative paths will be considered to be relative to root of the current project.
                                   The resolution algorithm will not check if this file actually exists - the
                                   resolution will be considered successful whether it exists or not.
                                   With this mode, the resolver will not continue on to attempt to resolve
                                   using any other resolve method.
                                   The user must explicitly check MFileObject.exists() to determine if it is an
                                   existing path.
          kExact                   Checks if expanded paths exist. If paths are relative, assume it's relative to
                                   the current workspace (so check workspace current directory, file-rule directory and
                                   root directory).
          kDirMap                  Checks path against mappings defined with the dirmap command. Only for absolute paths
          kReferenceMappings       Check path against any previously re-mapped reference locations. If kRelative/kBaseName
                                   are set, then even if we have an absolute path, convert to relative and/or baseName and
                                   look for them in directories provided to the missing reference dialog.
          kRelative                Strips away the project directory, and treats path as relative. Relative to the current
                                   workspace, that is. So look in the workspace current directory, file-rules directory
                                   and the root directory.
          kBaseName                Strips away everything but the base file name and look in the current workspace,
          kInputFile               This mode is the default on file open and import, and is suitable for
                                   files that are to be used as input files.  The file will be checked for
                                   existence.
                                   Combination of kExact, kDirMap, kRelative and kBaseName.
          kInputReference          This mode is the default on file reference. In addition to the checks done for
                                   a regular input file, it will also check the reference mappings.
                                   Combination of kInputFile and kReferenceMappings.
          kStrict                  Combination of kExact and kDirMap.
        """
        pass

    @staticmethod
    def isAbsolutePath(*args, **kwargs):
        """
        isAbsolutePath(fileName) -> bool

        Checks a file path string and determines if it represents an absolute file path. An absolute path can uniquely identify a directory or file.

        * fileName (string) - the string used to check if it is absolute
        """
        pass

    kBaseName = 32

    kDirMap = 4

    kExact = 2

    kInputFile = 54

    kInputReference = 62

    kNone = 1

    kReferenceMappings = 8

    kRelative = 16

    kStrict = 6

    resolveMethod = None


class MTimeArray(object):
    """
    Array of MTime values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MMeshIntersector(object):
    """
    Provides methods for efficiently finding the closest point on
    the surface of a mesh. An octree algorithm is used to find the
    closest point.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        create(mesh, matrix) -> self

        Creates the internal data required by the intersector. It is a
        compute-heavy operation and should only be called when necessary.

        mesh (MObject)   - the mesh to be used
        matrix (MMatrix) - transformation to use to bring points into the
        mesh's object space.
        """
        pass

    def getClosestPoint(*args, **kwargs):
        """
        getClosestPoint(referencePoint, maxDistance=sys.float_info.max) -> MPointOnMesh

        Finds the closest point within 'maxDistance' of the reference point
        (MPoint) which lies on the surface of the mesh. The reference point
        will first be transformed by the matrix passed in the create() call,
        so if, for example, you want to specify reference points in world
        space then the matrix passed to create() should provide the mapping
        from world space to the mesh's object space.

        Returns an MPointOnMesh object if a closest point is found, or None
        if no closest point is found (e.g. referencePoint is not within
        maxDistance of the mesh).

        Raises ValueError if create() has not yet been called for this
        intersector.
        """
        pass

    isCreated = None


class MAttributePattern(object):
    """
    Manipulate attribute structure patterns.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def addRootAttr(*args, **kwargs):
        """
        Add the given root attribute to this pattern.
        """
        pass

    def name(*args, **kwargs):
        """
        Return the name of the attribute pattern.
        """
        pass

    def removeRootAttr(*args, **kwargs):
        """
        Return the nth or passed-in root attribute from this pattern.
        """
        pass

    def rootAttr(*args, **kwargs):
        """
        Return the nth root attribute in this pattern.
        """
        pass

    def rootAttrCount(*args, **kwargs):
        """
        Return the number of root attributes in this pattern.
        """
        pass

    @staticmethod
    def attrPattern(*args, **kwargs):
        """
        Return the specified pattern indexed from the global list.
        """
        pass

    @staticmethod
    def attrPatternCount(*args, **kwargs):
        """
        Return the global number of patterns created.
        """
        pass

    @staticmethod
    def findPattern(*args, **kwargs):
        """
        Return a pattern with the given name, None if not found.
        """
        pass


class MMeshIsectAccelParams(object):
    """
    Opaque class used to store parameters used by MFnMesh's
    intersection calculations for later re-use. Use MFnMesh's
    uniformGridParams() or autoUniformGridParams() to create one
    of these to pass into the allIntersections(),
    closestIntersection(), and anyIntersection() methods
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass


class MCallbackIdArray(object):
    """
    Array of MCallbackId values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MNamespace(object):
    """
    Access Maya namespace functionality.
    """

    @staticmethod
    def addNamespace(*args, **kwargs):
        """
        addNamespace(MString name, MString parent=None)

        Create the namespace 'name'. If the `parent' namespace is given
        the new namespace will be a child of `parent', otherwise the new
        namespace will be a child of the current namespace.
        The new namespace is added, but not made current. To make the
        new namespace be current use MNamespace.setCurrentNamespace().
        Note that adding a namespace changes the scene, so any code that calls
        this method needs to handle undo.

             name    The new namespace to create. A qualified or unqualified
                     name may be used. If a qualified name is used and one or
                     more of the higher level namespaces do not already exist,
                     they will be created automatically. For example, if the new
                     name is 'a:b:c' and 'a' does not yet exist, then it will be
                     created automatically and 'b' automatically created beneath
                     it and finally 'c' will be created beneath 'b'.
                     If the supplied name contains invalid characters it will first
                     be modified as per the validateName() method.
             parent  The fully qualified name of the namespace under which
                     the new one is to be created. If not provided then the
                     current namespace will be used. If the name of the new
                     namespace is absolute (i.e. begins with a colon, ':a:b:c')
                     then the 'parent' parameter will be ignored and the new namespace
                     will be created under the root namespace.
        """
        pass

    @staticmethod
    def currentNamespace(*args, **kwargs):
        """
        currentNamespace() -> MString

        Get the name of the current namespace. This name is returned
        as an absolute namepath (i.e. fully qualfied from the root
        namespace downwards, ':a:b:c').
        """
        pass

    @staticmethod
    def getNamespaceFromName(*args, **kwargs):
        """
        getNamespaceFromName(MString fullName) -> MString

        Get namespace from a full name.
        For example, given a full name: 'a:b:c:d:ball' this method
        would return: 'a:b:c:d'.
        """
        pass

    @staticmethod
    def getNamespaceObjects(*args, **kwargs):
        """
        getNamespaceObjects(MString parentNamespace, bool recurse=False) -> MObjectArray

        Return an array of MObjects representing the object contained within
        the specified namespace. To query the current namespace, call this
        method in this way:
        """
        pass

    @staticmethod
    def getNamespaces(*args, **kwargs):
        """
        getNamespaces(MString parentNamespace=None, bool recurse=False) -> [MString]

        Return a list of all namespaces in the current namespace.
        Notes:
            1)  Names returned are always absolute (e.g. :a:b:sphere).
            2)  The list returned is just the child namespaces (and
                descendents if `recurse' is true). It thus never contains
                the root namespace in the list returned.

                   parentNamespace  the namespace to query.
                   recurse          optional parameter to control whether all
                                    namespaces or just top-level namespaces
                                    are returned. A value of false (the
                                    default if unspecified) causes only the
                                    top-level namespaces to be returned. If
                                    true, all namespaces will be listed.
        """
        pass

    @staticmethod
    def makeNamepathAbsolute(*args, **kwargs):
        """
        makeNamepathAbsolute(MString fullName) -> MString

        Make a namepath which is relative to the root into an absolute
        namepath. For example, given the namepath 'a:sphere' this method
        returns ':a:sphere'. It also culls out duplicate and trailing
        separators, e.g. 'a:b::c:' will return ':a:b:c'.
        """
        pass

    @staticmethod
    def moveNamespace(*args, **kwargs):
        """
        moveNamespace(MString src, MString dst, bool force=False)

        Move the contents of the namespace 'src' into the namespace 'dst'.
        Note that moving namespace contents changes the scene, so any code
        that calls this method needs to handle undo.

                  src       source namespace from which objects will be moved.
                  dst       destination namespace to which objects will be moved.
                  force     optional parameter which if true forces the move
                            even if name clashes occur, in which case nodes are
                            renamed to ensure uniqueness. If false, the move
                            will not happen if there are clashes. The default
                            value is false.
        """
        pass

    @staticmethod
    def namespaceExists(*args, **kwargs):
        """
        namespaceExists(MString name) -> bool

        Check if a given namespace exists.
        """
        pass

    @staticmethod
    def parentNamespace(*args, **kwargs):
        """
        parentNamespace() -> MString

        Get the name of the current namespace's parent. This name is returned
        as an absolute namepath (i.e. fully qualfied from the root namespace
        downwards, ':a:b'). If the root namespace is
        current, this method returns an error.
        """
        pass

    @staticmethod
    def relativeNames(*args, **kwargs):
        """
        relativeNames() -> bool

        Query Maya's current 'relative name lookup' state. Relative name
        lookup causes lookups to be relative to the current namespace.
        By default, relative name lookup in Maya is off, which causes
        name lookups to be relative to the root namespace. For example,
        if you have the object :a:b:sphere, and the current namespace is
        ':a:b', in relative name lookup mode you can issue a command like

            setAttr sphere.translateX 10;

        If relative name lookup is off, you need to specify the full
        namepath, e.g.

            setAttr a:b:sphere.translateX 10;
        """
        pass

    @staticmethod
    def removeNamespace(*args, **kwargs):
        """
        removeNamespace(MString name, bool removeContents=False)

        Remove the specified namespace.
        Note that removing a namespace changes the scene, so any code
        that calls this method needs to handle undo.
        """
        pass

    @staticmethod
    def renameNamespace(*args, **kwargs):
        """
        renameNamespace(MString oldName, MString newName, MString parent=None)

        Rename the specified namespace to a new name with optional parent name.
        Note that removing a namespace changes the scene, so any code
        that calls this method needs to handle undo.
        """
        pass

    @staticmethod
    def rootNamespace(*args, **kwargs):
        """
        rootNamespace() -> MString

        Get the name of the root namespace. This name is an absolute
        namepath (i.e. prefixed by a ':').
        """
        pass

    @staticmethod
    def setCurrentNamespace(*args, **kwargs):
        """
        setCurrentNamespace(MString name) -> MString

        Set the specified namespace to be the current namespace. The 'name'
        parameter you specify is relative to whatever namespace is current,
        but any namespace can be specified by passing an absolute name (e.g. :a:b:c).
        Note that making a namespace current changes the scene, so any code
        that calls this method needs to handle undo.

        To make the root namespace become current, use:
            MNamespace.setCurrentNamespace(MNamespace.rootNamespace())
        """
        pass

    @staticmethod
    def setRelativeNames(*args, **kwargs):
        """
        setRelativeNames(bool newState)

        Set relative name lookup mode.

        Note that turning on or off relativeNames mode can change the scene,
        so any code that calls this method needs to handle undo.
        See MNamespace.relativeNames() for details on relative name lookup.

        Note: relative name lookup mode is intended for bracketing user
        code which needs to be namespace-independent. Leaving relative
        name lookup enabled outside of your specific code could cause
        functionality such as 3rd-party plugins that assume absolute
        name lookup to fail.

           newState         true to turn on relative name lookup, false to
                            turn it off. Maya's default setting is false.
        """
        pass

    @staticmethod
    def stripNamespaceFromName(*args, **kwargs):
        """
        stripNamespaceFromName(MString fullName) -> MString

        Strips the namespace from a full name.
        For example, given a full name: 'a:b:c:d:ball' this method
        would return: 'ball'.
        """
        pass

    @staticmethod
    def validateName(*args, **kwargs):
        """
        validateName(MString name) -> MString

        Convert the specified name to a validated name which
        contains no illegal characters.
        The leading illegal characters will be removed and
        other illegal characters will be converted to '_'.

        For example, name '@name@space@' will be converted to 'name_space_'.

        If the entire name consists solely of illegal characters,
        e.g. '123' which contains only leading digits, then the
        returned string will be empty.
        """
        pass


class MDagPath(object):
    """
    Path to a DAG node from the top of the DAG.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)
        self._node: MObject = None

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def apiType(*args, **kwargs):
        """
        Returns the type of the object at the end of the path.
        """
        pass

    def child(*args, **kwargs):
        """
        Returns the specified child of the object at the end of the path.
        """
        pass

    def childCount(*args, **kwargs):
        """
        Returns the number of objects parented directly beneath the object at the end of the path.
        """
        pass

    def exclusiveMatrix(*args, **kwargs):
        """
        Returns the matrix for all transforms in the path, excluding the end object.
        """
        pass

    def exclusiveMatrixInverse(*args, **kwargs):
        """
        Returns the inverse of exclusiveMatrix().
        """
        pass

    def extendToShape(*args, **kwargs):
        """
        Extends the path to the specified shape node parented directly beneath the transform at the current end of the path.
        """
        pass

    def fullPathName(self) -> str:
        """
        Returns a string representation of the path from the DAG root to the path's last node.
        """
        ancestors = [x._name for x in self._iter_ancestors() or ()]
        ancestors.reverse()
        if not ancestors:
            return self._node._name
        return "|".join(ancestors) + f"|{self._node._name}"

    def getDisplayStatus(*args, **kwargs):
        """
        Returns the display status for this path.
        """
        pass

    def getDrawOverrideInfo(*args, **kwargs):
        """
        Returns the draw override information for this path.
        """
        pass

    def getPath(*args, **kwargs):
        """
        Returns the specified sub-path of this path.
        """
        pass

    def hasFn(self, fn: int):
        """
        Returns True if the object at the end of the path supports the given function set.
        """
        return self._node.hasFn(fn)

    def inclusiveMatrix(*args, **kwargs):
        """
        Returns the matrix for all transforms in the path, including the end object, if it is a transform.
        """
        pass

    def inclusiveMatrixInverse(*args, **kwargs):
        """
        Returns the inverse of inclusiveMatrix().
        """
        pass

    def instanceNumber(*args, **kwargs):
        """
        Returns the instance number of this path to the object at the end.
        """
        pass

    def isInstanced(*args, **kwargs):
        """
        Returns True if the object at the end of the path can be reached by more than one path.
        """
        pass

    def isTemplated(*args, **kwargs):
        """
        Returns true if the DAG Node at the end of the path is templated.
        """
        pass

    def isValid(*args, **kwargs):
        """
        Returns True if this is a valid path.
        """
        pass

    def isVisible(*args, **kwargs):
        """
        Returns true if the DAG Node at the end of the path is visible.
        """
        pass

    def length(self):
        """
        Returns the number of nodes on the path, not including the DAG's root node.
        """
        return len(list(self._iter_ancestors()))

    def node(self):
        """
        Returns the DAG node at the end of the path.
        """
        return self._node

    def numberOfShapesDirectlyBelow(*args, **kwargs):
        """
        Returns the number of shape nodes parented directly beneath the transform at the end of the path.
        """
        pass

    def partialPathName(*args, **kwargs):
        """
        Returns the minimum string representation which will uniquely identify the path.
        """
        pass

    def pathCount(*args, **kwargs):
        """
        Returns the number of sub-paths which make up this path.
        """
        pass

    def pop(*args, **kwargs):
        """
        Removes objects from the end of the path.
        """
        pass

    def push(*args, **kwargs):
        """
        Extends the path to the specified child object, which must be parented directly beneath the object currently at the end of the path.
        """
        pass

    def set(*args, **kwargs):
        """
        Replaces the current path held by this object with another.
        """
        pass

    def transform(*args, **kwargs):
        """
        Returns the last transform node on the path.
        """
        pass

    @staticmethod
    def getAPathTo(*args, **kwargs):
        """
        Returns the first path found to the given node.
        """
        pass

    @staticmethod
    def getAllPathsTo(*args, **kwargs):
        """
        Returns all paths to the given node.
        """
        pass

    def _iter_ancestors(self, break_at=None):
        """NOT FROM API, UTILITY METHOD FROM MAYA MOCK COMPLETION"""

        break_at = break_at or WORLD
        current = self._node

        if current._parent is break_at:
            return iter(())

        while current._parent and current.parent is not break_at:
            current = current._parent
            yield current


class MFloatVector(object):
    """
    3D vector with single-precision coordinates.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __div__(*args, **kwargs):
        """
        x.__div__(y) <==> x/y
        """
        pass

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __idiv__(*args, **kwargs):
        """
        x.__idiv__(y) <==> x/=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __isub__(*args, **kwargs):
        """
        x.__isub__(y) <==> x-=y
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __neg__(*args, **kwargs):
        """
        x.__neg__() <==> -x
        """
        pass

    def __radd__(*args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __rdiv__(*args, **kwargs):
        """
        x.__rdiv__(y) <==> y/x
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(*args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __rxor__(*args, **kwargs):
        """
        x.__rxor__(y) <==> y^x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def __sub__(*args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def __xor__(*args, **kwargs):
        """
        x.__xor__(y) <==> x^y
        """
        pass

    def angle(*args, **kwargs):
        """
        Returns the angle, in radians, between this vector and another.
        """
        pass

    def isEquivalent(*args, **kwargs):
        """
        Returns True if this vector and another are within a given tolerance of being equal.
        """
        pass

    def isParallel(*args, **kwargs):
        """
        Returns True if this vector and another are within the given tolerance of being parallel.
        """
        pass

    def length(*args, **kwargs):
        """
        Returns the magnitude of this vector.
        """
        pass

    def normal(*args, **kwargs):
        """
        Returns a new vector containing the normalized version of this one.
        """
        pass

    def normalize(*args, **kwargs):
        """
        Normalizes this vector in-place and returns a new reference to it.
        """
        pass

    def transformAsNormal(*args, **kwargs):
        """
        Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix and then normalizing the result.
        """
        pass

    kOneVector = None

    kTolerance = 9.999999747378752e-06

    kXaxisVector = None

    kXnegAxisVector = None

    kYaxisVector = None

    kYnegAxisVector = None

    kZaxisVector = None

    kZeroVector = None

    kZnegAxisVector = None

    x = None

    y = None

    z = None


class MFnBase(object):
    """
    Base class for function sets.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """

        self._fn_type = MFn.kBase

        if args:
            self._mobject = args[0]
        else:
            self._mobject = MObject()

    def hasObj(self, mobject: 'MObject') -> bool:
        """
        Returns True if the function set is compatible with the specified Maya object.
        """
        return self._mobject.hasFn(self.type())

    def object(self) -> MObject:
        """
        Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none.
        """
        return self._mobject

    def setObject(self, mobject: MObject):
        """
        Attaches the function set to the specified Maya object.
        """
        self._mobject = mobject
        return self

    def type(self) -> int:
        """
        Returns the type of the function set.
        """
        return self._fn_type

    def _create(self):
        self._mobject = MObject()


class MUserData(object):
    """
    Virtual base class for user data caching.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def deleteAfterUse(*args, **kwargs):
        """
        deleteAfterUse() -> bool

        Returns whether or not this user data should be deleted immediately after use instead of being
        maintained until the internal owning object is deleted.
        """
        pass

    def setDeleteAfterUse(*args, **kwargs):
        """
        setDeleteAfterUse(bool) -> self

        Sets whether or not this user data should be deleted immediately after use instead of being
        maintained until the internal owning object is deleted.

        Setting this to false may allow the data to be reused in some situations.
        For example, if the MUserData returned by an MPxDrawOverride instance's prepareForDraw() method has
        its delete-after-use set to false, then Maya will retain the data between draws of that object,
        passing it back to the instance for reuse on subsequent draws.
        """
        pass


class MDagPathArray(object):
    """
    Array of MDagPath values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MDAGDrawOverrideInfo(object):
    """
    A data structure to store the per path draw override information.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    displayType = None

    enableShading = None

    enableTexturing = None

    enableVisible = None

    kDisplayTypeNormal = 0

    kDisplayTypeReference = 1

    kDisplayTypeTemplate = 2

    kLODBoundingBox = 1

    kLODFull = 0

    lod = None

    overrideEnabled = None

    playbackVisible = None


class MPointOnMesh(object):
    """
    This class is used to return information about a point on the
    surface of a mesh: 3D position, normal, barycentric coordinates,
    etc. The point can be anywhere on the mesh, not just at its
    vertices.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    barycentricCoords = None

    face = None

    normal = None

    point = None

    triangle = None


class MAngle(object):
    """
    Manipulate angular data.
    """

    _UNIT_CONST_TO_NAME = {
        3 : 'kAngMinutes',
        4 : 'kAngSeconds',
        2 : 'kDegrees',
        0 : 'kInvalid',
        5 : 'kLast',
        1 : 'kRadians',
    }

    # Conversion factors to radians
    _TO_RADIANS = {
        1: 1,
        2: math.pi / 180,
        3: math.pi / (180 * 60),
        4: math.pi / (180 * 3600),
    }

    # Conversion factors from radians to other units
    _FROM_RADIANS = {
        1: 1,
        2: 180 / math.pi,
        3: (180 * 60) / math.pi,
        4: (180 * 3600) / math.pi,
    }

    def __init__(self, value: float | MEulerRotation = None, unit: int = None, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._unit = unit or MAngle.kRadians
        self._value = value or random.uniform(-2 * math.pi, 2 * math.pi)

    def __repr__(self):
        """
        x.__repr__() <==> repr(x)
        """
        return f'{type(self).__name__}: <{self._value} {type(self)._UNIT_CONST_TO_NAME[self._unit]}>'

    def __str__(self):
        """
        x.__str__() <==> str(x)
        """
        return f'{self._value} {type(self)._UNIT_CONST_TO_NAME[self._unit]}'

    def asAngMinutes(self) -> float:
        """
        Returns the angular value, converted to minutes of arc.
        """
        if self._unit == MAngle.kAngMinutes:
            return self._value
        return self.asDegrees() * 60

    def asAngSeconds(self) -> float:
        """
        Returns the angular value, converted to seconds of arc.
        """
        if self._unit == MAngle.kAngSeconds:
            return self._value
        return self.asDegrees() * 3600

    def asDegrees(self) -> float:
        """
        Returns the angular value, converted to degrees.
        """
        radians = self.asRadians()
        return radians * MAngle._FROM_RADIANS[MAngle.kDegrees]

    def asRadians(self) -> float:
        """
        Returns the angular value, converted to radians.
        """
        return self._value * MAngle._TO_RADIANS[self._unit]

    def asUnits(self, unit=1) -> float:
        """
        Returns the angular value, converted to the specified units.
        """
        unit_to_conversion_func = {
            MAngle.kRadians: self.asRadians,
            MAngle.kDegrees: self.asDegrees,
            MAngle.kAngMinutes: self.asAngMinutes,
            MAngle.kAngSeconds: self.asAngSeconds,
        }
        if unit not in unit_to_conversion_func:
            raise ValueError(f"Unsupported unit: {unit}")
        return unit_to_conversion_func[unit]()

    @staticmethod
    def internalToUI(*args, **kwargs):
        """
        Converts a value from Maya's internal units to the units used in the UI.
        """
        pass

    @staticmethod
    def internalUnit(*args, **kwargs):
        """
        Returns the angular unit used internally by Maya.
        """
        pass

    @staticmethod
    def setUIUnit(*args, **kwargs):
        """
        Sets the angular unit used in Maya's UI.
        """
        pass

    @staticmethod
    def uiToInternal(*args, **kwargs):
        """
        Converts a value from the units used in the UI to Maya's internal units.
        """
        pass

    @staticmethod
    def uiUnit(*args, **kwargs):
        """
        Returns the units used to display angles in Maya's UI.
        """
        pass

    kAngMinutes = 3

    kAngSeconds = 4

    kDegrees = 2

    kInvalid = 0

    kLast = 5

    kRadians = 1

    @property
    def unit(self):
        return self._unit

    @property
    def value(self):
        return self._value


class MFloatVectorArray(object):
    """
    Array of MFloatVector values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MItMeshEdge(object):
    """
    An iterator for traversing a mesh's edges.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def center(*args, **kwargs):
        """
        center(space=kObject) -> MPoint

        Returns the center point of the edge, in the given transformation space.

        * space (MSpace constant) - The  transformation space
        """
        pass

    def connectedToEdge(*args, **kwargs):
        """
        connectedToEdge(index) -> bool

        Determines whether the given edge is connected to the current edge.

        * index (int) - Index of edge to check.
        """
        pass

    def connectedToFace(*args, **kwargs):
        """
        connectedToFace(index) -> bool

        Determines whether the given face contains the current edge.

        * index (int) - Index of face to check.
        """
        pass

    def count(*args, **kwargs):
        """
        count() -> int

        Return the number of edges in the iteration
        """
        pass

    def currentItem(*args, **kwargs):
        """
        currentItem() -> MObject

        Returns the current edge in the iteration as a component.

        Components are used to specify one or more edges and are useful in operating on groups of non-contiguous edges for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
        pass

    def geomChanged(*args, **kwargs):
        """
        geomChanged() -> self

        Resets the geom pointer in the MItMeshEdge. If you're using MFnMesh to
        update Normals or Color per vertex while iterating, you must call geomChanged
        on the iterator immediately after the MFnMesh call to make sure that your
        geometry is up to date. A crash may result if this method is not called.
        A similar approach must be taken for updating upstream vertex tweaks
        with an MPlug. After the update, call this method.
        """
        pass

    def getConnectedEdges(*args, **kwargs):
        """
        getConnectedEdges() -> MIntArray

        Returns the indices of edges connected to the current edge.
        """
        pass

    def getConnectedFaces(*args, **kwargs):
        """
        getConnectedFaces() -> MIntArray

        Returns the indices of the faces connected to the current edge.
        Normally a boundary edge will only have one face connected to it and
        an internal edge will have two, but if the mesh has manifold geometry
        then the edge may have three or more faces connected to it.
        """
        pass

    def index(*args, **kwargs):
        """
        index() -> int

        Returns the index of the current edge in the iteration.
        """
        pass

    def isDone(*args, **kwargs):
        """
        isDone() -> bool

        Indicates if all of the edges have been traversed yet.
        """
        pass

    def length(*args, **kwargs):
        """
        length(space=kObject) -> float

        Returns the length of the edge, in the given transformation space.

        * space (MSpace constant) - The  transformation space
        """
        pass

    def next(*args, **kwargs):
        """
        next() -> self

        Advances to the next edge in the iteration.
        """
        pass

    def numConnectedEdges(*args, **kwargs):
        """
        numConnectedEdges() -> int

        Returns the number of edges connected to the current edge.
        """
        pass

    def numConnectedFaces(*args, **kwargs):
        """
        numConnectedFaces() -> int

        Returns the number of faces connected to the current edge.
        """
        pass

    def onBoundary(*args, **kwargs):
        """
        onBoundary() -> bool

        Determines if the current edge is a border edge.
        """
        pass

    def point(*args, **kwargs):
        """
        point(whichVertex, space=kObject) -> MPoint

        Returns the position of one of the current edge's vertices, int the
        given transformation space.

        * whichVertex    (0 or 1) - Which of the edge's two vertices to return
        * space (MSpace constant) - The transformation space
        """
        pass

    def reset(*args, **kwargs):
        """
        reset() -> self
        reset(mesh) -> self
        reset(mesh, component=None) -> self

        Reset the iterator to the first edge of the mesh.

        Reset the iterator to the first edge of the specified mesh

        * mesh (MObject) - The polygon for the iteration

        Reset the iterator with the given mesh and component.
        If component is None then the iteration will be for all edges in the mesh.

        * mesh (MDagPath) - The mesh to iterate over
        * component (MObject) - The edges of the mesh to iterate over
        """
        pass

    def setIndex(*args, **kwargs):
        """
        setIndex(index) -> int

        Sets the index of the current edge to be accessed. The current edge
        will no longer be in sync with any previous iteration.

        Returns the index of the edge which was current before the change.


        * index (int) - The index of desired edge to access.
        """
        pass

    def setPoint(*args, **kwargs):
        """
        setPoint(point, whichVertex, space=kObject) -> self

        Sets the position of one of the current edge's vertices, in the given
        transformation space.

        * point       (MPoint) - The new position for the specified vertex
        * whichVertex (0 or 1) - Which of the edge's 2 vertices to set.
        * space (MSpace constant) - The transformation space
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        Tells Maya that mesh has been changed and needs to redraw itself.
        """
        pass

    def vertexId(*args, **kwargs):
        """
        vertexId(whichVertex) -> int

        Returns the global index (as opposed to face-relative index) of one of
        the edge's vertices.

        * whichVertex (0 or 1) - Which of the edge's 2 vertices to use.
        """
        pass

    isSmooth = None


class MQuaternion(object):
    """
    Quaternion math.
    """

    def __add__(self, *args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __delitem__(self, *args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __eq__(self, *args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(self, *args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __getitem__(self, *args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __gt__(self, *args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __imul__(self, *args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __le__(self, *args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __len__(self, *args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __lt__(self, *args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __mul__(self, *args, **kwargs):
        """
        x.__mul__(y) <==> x*y
        """
        pass

    def __ne__(self, *args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __neg__(self, *args, **kwargs):
        """
        x.__neg__() <==> -x
        """
        pass

    def __radd__(self, *args, **kwargs):
        """
        x.__radd__(y) <==> y+x
        """
        pass

    def __repr__(self, *args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(self, *args, **kwargs):
        """
        x.__rmul__(y) <==> y*x
        """
        pass

    def __rsub__(self, *args, **kwargs):
        """
        x.__rsub__(y) <==> y-x
        """
        pass

    def __setitem__(self, *args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __str__(self, *args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def __sub__(self, *args, **kwargs):
        """
        x.__sub__(y) <==> x-y
        """
        pass

    def asAxisAngle(self, *args, **kwargs):
        """
        Returns the rotation as a tuple containing an axis vector and an angle in radians about that axis.
        """
        pass

    def asEulerRotation(self, *args, **kwargs):
        """
        Returns the rotation as an equivalent MEulerRotation.
        """
        pass

    def asMatrix(self, *args, **kwargs):
        """
        Returns the rotation as an equivalent rotation matrix.
        """
        pass

    def conjugate(self, *args, **kwargs):
        """
        Returns the conjugate of this quaternion (i.e. x, y and z components negated).
        """
        pass

    def conjugateIt(self, *args, **kwargs):
        """
        In-place conjugation (i.e. negates the x, y and z components).
        """
        pass

    def exp(self, *args, **kwargs):
        """
        Returns a new quaternion containing the exponent of this one.
        """
        pass

    def inverse(self, *args, **kwargs):
        """
        Returns a new quaternion containing the inverse of this one.
        """
        pass

    def invertIt(self, *args, **kwargs):
        """
        In-place inversion.
        """
        pass

    def isEquivalent(self, *args, **kwargs):
        """
        Returns True if the distance between the two quaternions (in quaternion space) is less than or equal to the given tolerance.
        """
        pass

    def log(self, *args, **kwargs):
        """
        Returns a new quaternion containing the natural log of this one.
        """
        pass

    def negateIt(self, *args, **kwargs):
        """
        In-place negation of the x, y, z and w components.
        """
        pass

    def normal(self, *args, **kwargs):
        """
        Returns a new quaternion containing the normalized version of this one (i.e. scaled to unit length).
        """
        pass

    def normalizeIt(self, *args, **kwargs):
        """
        In-place normalization (i.e. scales the quaternion to unit length).
        """
        pass

    def setToXAxis(self, *args, **kwargs):
        """
        Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the X-axis.
        """
        pass

    def setToYAxis(self, *args, **kwargs):
        """
        Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Y-axis.
        """
        pass

    def setToZAxis(self, *args, **kwargs):
        """
        Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Z-axis.
        """
        pass

    def setValue(self, *args, **kwargs):
        """
        Set the value of this quaternion to that of the specified MQuaternion, MEulerRotation, MMatrix or MVector and angle.
        """
        pass

    @staticmethod
    def slerp(*args, **kwargs):
        """
        Returns the quaternion at a given interpolation value along the shortest path between two quaternions.
        """
        pass

    @staticmethod
    def squad(*args, **kwargs):
        """
        Returns the quaternion at a given interpolation value along a cubic curve segment in quaternion space.
        """
        pass

    @staticmethod
    def squadPt(*args, **kwargs):
        """
        Returns a new quaternion representing an intermediate point which when used with squad() will produce a C1 continuous spline.
        """
        pass

    kIdentity = None

    kTolerance = 1e-10

    w = None

    x = None

    y = None

    z = None


class MURI(object):
    """
    Manipulate URIs.
    """

    def __eq__(*args, **kwargs):
        """
        x.__eq__(y) <==> x==y
        """
        pass

    def __ge__(*args, **kwargs):
        """
        x.__ge__(y) <==> x>=y
        """
        pass

    def __gt__(*args, **kwargs):
        """
        x.__gt__(y) <==> x>y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __le__(*args, **kwargs):
        """
        x.__le__(y) <==> x<=y
        """
        pass

    def __lt__(*args, **kwargs):
        """
        x.__lt__(y) <==> x<y
        """
        pass

    def __ne__(*args, **kwargs):
        """
        x.__ne__(y) <==> x!=y
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def addQueryItem(*args, **kwargs):
        """
        addQueryItem(key, value) -> self

        Add a key/value pair to the query string of the URI.
        """
        pass

    def asString(*args, **kwargs):
        """
        asString() -> string

        Returns the string representation of the URI.
        """
        pass

    def clear(*args, **kwargs):
        """
        clear() -> self

        Clears the contents of the MURI object.
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy method. Assigns the value of one MURI to another.

        * source (MURI) - Existing MURI object to copy.
        """
        pass

    def getAllQueryItemKeys(*args, **kwargs):
        """
        getAllQueryItemKeys() -> array

        Returns an array containing the keys from all query string pairs.
        """
        pass

    def getAllQueryItemValues(*args, **kwargs):
        """
        getAllQueryItemValues(key) -> array

        Returns an array containing the values from all query string pairs which have a given key.
        """
        pass

    def getAuthority(*args, **kwargs):
        """
        getAuthority() -> string

        Returns the authority component of the URI.
        """
        pass

    def getDirectory(*args, **kwargs):
        """
        getDirectory() -> string

        Returns just the file directory portion of the URI, without the file name.
        """
        pass

    def getFileName(*args, **kwargs):
        """
        getFileName(bool includeExtension=True) -> string

        Returns just the file name portion of the URI, with or without the extension.
        """
        pass

    def getFragment(*args, **kwargs):
        """
        getFragment() -> string

        Returns the fragment component of the URI.
        """
        pass

    def getHost(*args, **kwargs):
        """
        getHost() -> string

        Returns the host component of the URI.
        """
        pass

    def getPassword(*args, **kwargs):
        """
        getPassword() -> string

        Returns the password component of the URI.
        """
        pass

    def getPath(*args, **kwargs):
        """
        getPath() -> string

        Returns the path component of the URI.
        """
        pass

    def getPort(*args, **kwargs):
        """
        getPort() -> int

        Returns the port component of the URI, or -1 if the port is not defined.
        """
        pass

    def getQueryItemValue(*args, **kwargs):
        """
        getQueryItemValue(key) -> string

        Returns the value from the first query string pair in the URI which has a given key.
        """
        pass

    def getQueryPairDelimiter(*args, **kwargs):
        """
        getQueryPairDelimiter() -> string

        Returns the character used to delimit between key-value pairs in the query string of the URI.
        """
        pass

    def getQueryValueDelimiter(*args, **kwargs):
        """
        getQueryValueDelimiter() -> string

        Returns the character used to delimit keys and values in the query string of the URI.
        """
        pass

    def getScheme(*args, **kwargs):
        """
        getScheme() -> string

        Returns the scheme of the URI.
        """
        pass

    def getUserInfo(*args, **kwargs):
        """
        getUserInfo() -> string

        Returns the user info component of the URI.
        """
        pass

    def getUserName(*args, **kwargs):
        """
        getUserName() -> string

        Returns the user name component of the URI.
        """
        pass

    def isEmpty(*args, **kwargs):
        """
        isEmpty() -> bool

        Determines if the URI does not contain any data.
        """
        pass

    def isValid(*args, **kwargs):
        """
        isValid() -> bool

        Determines if the URI is valid.
        """
        pass

    def removeAllQueryItems(*args, **kwargs):
        """
        removeAllQueryItems(int) -> self

        Removes all query string pairs having a given key from the URI.
        """
        pass

    def removeQueryItem(*args, **kwargs):
        """
        removeQueryItem(int) -> self

        Removes the first query string pair with a given key from the URI.
        """
        pass

    def setAuthority(*args, **kwargs):
        """
        setAuthority(string) -> self

        Set the authority portion of the URI.
        """
        pass

    def setDirectory(*args, **kwargs):
        """
        setDirectory(string) -> self

        Sets just the directory portion of the URI (i.e. not including the filename).
        """
        pass

    def setFileName(*args, **kwargs):
        """
        setFileName(string) -> self

        Sets just the filename portion of the URI (i.e. not including the directory).
        """
        pass

    def setFragment(*args, **kwargs):
        """
        setFragment(string) -> self

        Sets the fragment component of the URI.
        """
        pass

    def setHost(*args, **kwargs):
        """
        setHost(string) -> self

        Set the host component of the URI.
        """
        pass

    def setPassword(*args, **kwargs):
        """
        setPassword(string) -> self

        Sets the password part of the user info component.
        """
        pass

    def setPath(*args, **kwargs):
        """
        setPath(string) -> self

        Sets the path component of the URI.
        """
        pass

    def setPort(*args, **kwargs):
        """
        setPort(int) -> self

        Set the port component of the URI.
        """
        pass

    def setQueryDelimiters(*args, **kwargs):
        """
        setQueryDelimiters(valueDelimiter, pairDelimiter) -> self

        Sets the delimiter characters used in the query string of the URI.
        """
        pass

    def setScheme(*args, **kwargs):
        """
        setScheme(string) -> self

        Sets the scheme component of the URI.
        """
        pass

    def setURI(*args, **kwargs):
        """
        setURI(uri) -> self

        Initialize the MURI from a string value.
        """
        pass

    def setUserInfo(*args, **kwargs):
        """
        setUserInfo(string) -> self

        Decomposes the userInfo string to fill out the userInfo-related component values.
        """
        pass

    def setUserName(*args, **kwargs):
        """
        setUserName(string) -> self

        Sets the user name part of the user info component.
        """
        pass

    @staticmethod
    def isValidURI(*args, **kwargs):
        """
        isValidURI(uri) -> bool

        Determines if a string value represents a valid URI.
        """
        pass


class MObjectArray(object):
    """
    Array of MObject values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MPlug(object):
    """
    Create and access dependency node plugs.
    """

    def __eq__(self, value: Union['MPlug', 'MObject']) -> bool:
        """
        x.__eq__(y) <==> x==y
        """
        if isinstance(value, MPlug):
            value = value.attribute()
        return hash(self.attribute()._name) == hash(value._name)

    def __ge__(self, value: Union['MPlug', 'MObject']) -> bool:
        """
        x.__ge__(y) <==> x>=y
        """
        if isinstance(value, MPlug):
            value = value.attribute()
        return self.attribute() >= value

    def __gt__(self, value: Union['MPlug', 'MObject']) -> bool:
        """
        x.__gt__(y) <==> x>y
        """
        if isinstance(value, MPlug):
            value = value.attribute()
        return self.attribute() > value

    def __init__(self):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        self._owner: 'MObject' = None
        self._uuid: uuid.UUID = uuid.uuid4()
        self._network_plug = None
        self._value = None
        self._children_plug_names = None

        self._connections = {
            'INPUTS': [],
            'OUTPUTS': [],
        }
        self._parent = None

        self._attribute = None

    def __repr__(self):
        if not self._owner:
            return super().__repr__()
        return f'{type(self).__name__} <{self.name()}>'

    def __le__(self, value: Union['MPlug', 'MObject']) -> bool:
        """
        x.__le__(y) <==> x<=y
        """
        if isinstance(value, MPlug):
            value = value.attribute()
        return self.attribute() <= value

    def __lt__(self, value: Union['MPlug', 'MObject']) -> bool:
        """
        x.__lt__(y) <==> x<y
        """
        if isinstance(value, MPlug):
            value = value.attribute()
        return self.attribute() < value

    def __ne__(self, value: Union['MPlug', 'MObject']) -> bool:
        """
        x.__ne__(y) <==> x!=y
        """
        if isinstance(value, MPlug):
            value = value.attribute()
        return self.attribute() != value

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def array(self, *args, **kwargs):
        """
        Returns a plug for the array of plugs of which this plug is an element.
        """
        return [self, ]

    def asBool(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a boolean.
        """
        return bool(self._attribute._value)

    def asChar(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a single-byte integer.
        """
        return int(self._attribute._value or random.randint(-100, 100))

    def asDouble(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a double-precision float.
        """
        return float(self._attribute._value or random.uniform(-100, 100))

    def asFloat(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a single-precision float.
        """
        return float(self._attribute._value or random.uniform(-100, 100))

    def asInt(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a regular integer.
        """
        return int(self._attribute._value or random.randint(-100, 100))

    def asMAngle(self, *args, **kwargs):
        """
        Retrieves the plug's value, as an MAngle.
        """
        return MAngle(self._attribute._value or random.uniform(-360, 360))

    def asMDataHandle(self, *args, **kwargs):
        """
        Retrieve the current value of the attribute this plug references.
        """
        return MDataHandle(self._attribute._value)

    def asMDistance(self, *args, **kwargs):
        """
        Retrieves the plug's value, as an MDistance.
        """
        return MDistance(self._attribute._value or random.uniform(-100, 100))

    def asMObject(self, *args, **kwargs):
        """
        Retrieves the plug's value, as as an MObject containing a direct reference to the plug's data.
        """
        return MObject(self._attribute._value)

    def asMTime(self, *args, **kwargs):
        """
        Retrieves the plug's value, as an MTime.
        """
        return MTime(self._attribute._value or random.randint(0, 1_000_000))

    def asShort(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a short integer.
        """
        return int(self._attribute._value or random.randint(-32767, 32767))

    def asString(self, *args, **kwargs):
        """
        Retrieves the plug's value, as a string.
        """
        value = self._attribute._value
        return str(value) if value is not None else "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(4, 15)))

    def attribute(self):
        """
        Returns the attribute currently referenced by this plug.
        """
        return self._attribute

    def child(self, index) -> 'MPlug':
        """
        Returns a plug for the specified child attribute of this plug.
        """
        if not self.isCompound:
            raise RuntimeError(f'Trying to access children plugs of non-compound attribute: <{self.name()}>')
        child_plug = MFnDependencyNode(self._owner).findPlug(self._attribute._children[index]._long_name, False)
        child_plug._parent = weakref.proxy(self)
        return child_plug

    def connectedTo(*args, **kwargs):
        """
        Returns an array of plugs which are connected to this one.
        """
        pass

    def connectionByPhysicalIndex(*args, **kwargs):
        """
        Returns a plug for the index'th connected element of this plug.
        """
        pass

    def constructHandle(*args, **kwargs):
        """
        Constructs a data handle for the plug.
        """
        pass

    def copy(*args, **kwargs):
        """
        Copies one plug to another.
        """
        pass

    def destinations(*args, **kwargs):
        """
        If this plug is a source, return the destination plugs connected to it.
        If this plug is not a source, a null plug is returned.
        This method will produce the networked version of the connected plug.
        """
        pass

    def destinationsWithConversions(*args, **kwargs):
        """
        If this plug is a source, return the destination plugs connected to it.
        This method is very similar to the destinations() method.  The only difference is that the destinations() method skips over any unit conversion node connected to this source, and returns the destination of the unit conversion node.
        destinationsWithConversionNode() does not skip over unit conversion nodes, and returns the destination plug on a unit conversion node, if present.
        Note that the behavior of connectedTo() is identical to destinationsWithConversions(), that is, do not skip over unit conversion nodes.
        """
        pass

    def destructHandle(*args, **kwargs):
        """
        Destroys a data handle previously constructed using constructHandle().
        """
        pass

    def elementByLogicalIndex(self, index):
        """
        Returns a plug for the element of this plug array having the specified logical index.
        """
        return self._attribute._children[index]


    def elementByPhysicalIndex(*args, **kwargs):
        """
        Returns a plug for the element of this plug array having the specified physical index.
        """
        pass

    def evaluateNumElements(*args, **kwargs):
        """
        Like numElements() but evaluates all connected elements first to ensure that they are included in the count.
        """
        pass

    def getExistingArrayAttributeIndices(*args, **kwargs):
        """
        Returns an array of all the plug's logical indices which are currently in use.
        """
        pass

    def getSetAttrCmds(*args, **kwargs):
        """
        Returns a list of strings containing the setAttr commands (in MEL syntax) for this plug and all of its descendents.
        """
        pass

    def isDefaultValue(*args, **kwargs):
        """
        Returns a value indicating if the plug's value is equivalent to the plug's default value.
        """
        pass

    def isFreeToChange(*args, **kwargs):
        """
        Returns a value indicating if the plug's value can be changed, after taking into account the effects of locking and connections.
        """
        pass

    def logicalIndex(*args, **kwargs):
        """
        Returns this plug's logical index within its parent array.
        """
        pass

    def name(self):
        """
        Returns the name of the plug.
        """
        return self._attribute._name

    def node(self) -> 'MObject':
        """
        Returns the node that this plug belongs to.
        """
        return self._owner

    def numChildren(self, *args, **kwargs):
        """
        Returns the number of children this plug has.
        """
        return len(self._attribute._children)

    def numConnectedChildren(*args, **kwargs):
        """
        Returns the number of this plug's children which have connections.
        """
        pass

    def numConnectedElements(*args, **kwargs):
        """
        Returns the number of this plug's elements which have connections.
        """
        pass

    def numElements(*args, **kwargs):
        """
        Returns the number of the plug's logical indices which are currently in use. Connected elements which have not yet been evaluated may not yet fully exist and may be excluded from the count.
        """
        pass

    def parent(self) -> 'MPlug':
        """
        Returns a plug for the parent of this plug.
        """
        if self._parent:
            return self._parent

    def partialName(self,
                    includeNodeName=False,
                    useLongNames=True,
                    useFullAttributePath=False,
                    includeInstancedIndices=True):
        """
        Returns the name of the plug, formatted according to various criteria.
        """
        owner_name = self._owner._name
        short_name = self._attribute._short_name
        long_name = self._attribute._long_name

        return_str = ''
        if includeNodeName:
            return_str += f'{owner_name}.'
        elif useFullAttributePath:
            return_str += f'{owner_name}'

        if useLongNames:
            return_str += long_name
        else:
            return_str += short_name

        return return_str

    def selectAncestorLogicalIndex(*args, **kwargs):
        """
        Changes the logical index of the specified attribute in the plug's path.
        """
        pass

    def setAttribute(*args, **kwargs):
        """
        Switches the plug to reference the given attribute of the same node as the previously referenced attribute.
        """
        pass

    def setBool(self, value: bool):
        """
        Sets the plug's value as a boolean.
        """
        self._attribute._value = value

    def setChar(self, value: int):
        """
        Sets the plug's value as a single-byte integer.
        """
        self._attribute._value = value

    def setDouble(self, value: float):
        """
        Sets the plug's value as a double-precision float.
        """
        self._attribute._value = value

    def setFloat(self, value: float):
        """
        Sets the plug's value as a single-precision float.
        """
        self._attribute._value = value

    def setInt(self, value: int):
        """
        Sets the plug's value as a regular integer.
        """
        self._attribute._value = value

    def setMAngle(self, value: 'MAngle'):
        """
        Sets the plug's value as an MAngle.
        """

        self._attribute._value = value.asRadians()

    def setMDataHandle(self, value: 'MDataHandle'):
        """
        Sets the plug's value as a data handle.
        """
        self._attribute._value = value

    def setMDistance(self, value: 'MDistance'):
        """
        Sets the plug's value as an MDistance.
        """
        self._attribute._value = value.asCentimeters()

    def setMObject(self, value):
        """
        Sets the plug's value as an MObject.
        """
        self._attribute._value = value

    def setMPxData(self, value):
        """
        Sets the plug's value using custom plug-in data.
        """
        self._attribute._value = value

    def setMTime(self, value: 'MTime'):
        """
        Sets the plug's value as an MTime.
        """
        self._attribute._value = value.value

    def setNumElements(*args, **kwargs):
        """
        Pre-allocates space for count elements in an array of plugs.
        """
        pass

    def setShort(self, value):
        """
        Sets the plug's value as a short integer.
        """
        self._attribute._value = value

    def setString(self, value):
        """
        Sets the plug's value as a string.
        """
        self._attribute._value = value

    def source(*args, **kwargs):
        """
        If this plug is a destination, return the source plug connected to it.
        If this plug is not a destination, a null plug is returned.
        This method will produce the networked version of the connectedplug.
        """
        pass

    def sourceWithConversion(*args, **kwargs):
        """
        If this plug is a destination, return the source plug connected to it.
        This method is very similar to the source() method.  The only difference is that the source() method skips over any unit conversionnode connected to this destination, and returns the source of the unit conversion node.
        sourceWithConversion() does not skip over unitconversion nodes, and returns the source plug on a unit conversionnode, if present.
        Note that the behavior of connectedTo() is identical to sourceWithConversion(), that is, do not skip over unit conversion nodes.
        """
        pass

    info = None

    @property
    def isArray(self) -> bool:
        return self._attribute._is_array

    isCaching = None

    isChannelBox = None

    @property
    def isChild(self) -> bool:
        return True if self._attribute._parent else False

    @property
    def isCompound(self) -> bool:
        return self._attribute._is_compound

    isConnected = None

    isDestination = None

    isDynamic = None

    @property
    def isElement(self):
        return self._attribute._is_element

    isFromReferencedFile = None

    isIgnoredWhenRendering = None

    isKeyable = True

    isLocked = False

    isNetworked = None

    isNull = None

    isProcedural = None

    isSource = None

    kAll = 0

    kChanged = 2

    kChildrenNotFreeToChange = 2

    kFreeToChange = 0

    kLastAttrSelector = 3

    kNonDefault = 1

    kNotFreeToChange = 1


class MIntArray(object):
    """
    Array of int values.
    """

    def __add__(*args, **kwargs):
        """
        x.__add__(y) <==> x+y
        """
        pass

    def __contains__(*args, **kwargs):
        """
        x.__contains__(y) <==> y in x
        """
        pass

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __delslice__(*args, **kwargs):
        """
        x.__delslice__(i, j) <==> del x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __getslice__(*args, **kwargs):
        """
        x.__getslice__(i, j) <==> x[i:j]

        Use of negative indices is not supported.
        """
        pass

    def __iadd__(*args, **kwargs):
        """
        x.__iadd__(y) <==> x+=y
        """
        pass

    def __imul__(*args, **kwargs):
        """
        x.__imul__(y) <==> x*=y
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __mul__(*args, **kwargs):
        """
        x.__mul__(n) <==> x*n
        """
        pass

    def __repr__(*args, **kwargs):
        """
        x.__repr__() <==> repr(x)
        """
        pass

    def __rmul__(*args, **kwargs):
        """
        x.__rmul__(n) <==> n*x
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def __setslice__(*args, **kwargs):
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y

        Use  of negative indices is not supported.
        """
        pass

    def __str__(*args, **kwargs):
        """
        x.__str__() <==> str(x)
        """
        pass

    def append(*args, **kwargs):
        """
        Add a value to the end of the array.
        """
        pass

    def clear(*args, **kwargs):
        """
        Remove all elements from the array.
        """
        pass

    def copy(*args, **kwargs):
        """
        Replace the array contents with that of another or of a compatible Python sequence.
        """
        pass

    def insert(*args, **kwargs):
        """
        Insert a new value into the array at the given index.
        """
        pass

    def remove(*args, **kwargs):
        """
        Remove an element from the array.
        """
        pass

    def setLength(*args, **kwargs):
        """
        Grow or shrink the array to contain a specific number of elements.
        """
        pass

    sizeIncrement = None


class MSelectionMask(object):
    """
    Selection masks provide a way to control what is selectable in Maya.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addMask(*args, **kwargs):
        """
        addMask(selType) -> self

        Add the specified selection type to this mask.

        * selType (int) - the selection type to add.

        Valid selection types:
          kSelectHandles
          kSelectLocalAxis
          kSelectIkHandles
          kSelectIkEndEffectors
          kSelectJoints
          kSelectLights
          kSelectCameras
          kSelectLattices
          kSelectClusters
          kSelectSculpts
          kSelectNurbsCurves
          kSelectNurbsSurfaces
          kSelectMeshes
          kSelectSubdiv
          kSelectSketchPlanes
          kSelectParticleShapes
          kSelectEmitters
          kSelectFields
          kSelectSprings
          kSelectRigidBodies
          kSelectRigidConstraints
          kSelectCollisionModels
          kSelectXYZLocators
          kSelectOrientationLocators
          kSelectUVLocators
          kSelectTextures
          kSelectCurves
          kSelectSurfaces
          kSelectLocators
          kSelectObjectsMask
          kSelectCVs
          kSelectHulls
          kSelectEditPoints
          kSelectMeshVerts
          kSelectMeshEdges
          kSelectMeshFreeEdges
          kSelectMeshFaces
          kSelectSubdivMeshPoints
          kSelectSubdivMeshEdges
          kSelectSubdivMeshFaces
          kSelectMeshUVs
          kSelectVertices
          kSelectEdges
          kSelectFacets
          kSelectMeshLines
          kSelectMeshComponents
          kSelectCurveParmPoints
          kSelectCurveKnots
          kSelectSurfaceParmPoints
          kSelectSurfaceKnots
          kSelectSurfaceRange
          kSelectSurfaceEdge
          kSelectIsoparms
          kSelectCurvesOnSurfaces
          kSelectPPStrokes
          kSelectLatticePoints
          kSelectParticles
          kSelectJointPivots
          kSelectScalePivots
          kSelectRotatePivots
          kSelectPivots
          kSelectComponentsMask
          kSelectAnimCurves
          kSelectAnimKeyframes
          kSelectAnimInTangents
          kSelectAnimOutTangents
          kSelectAnimMask
          kSelectAnimAny
          kSelectTemplates
          kSelectManipulators
          kSelectGuideLines
          kSelectPointsForGravity
          kSelectPointsOnCurvesForGravity
          kSelectPointsOnSurfacesForGravity
          kSelectObjectGroups
          kSelectSubdivMeshMaps
          kSelectFluids
          kSelectHairSystems
          kSelectFollicles
          kSelectNCloths
          kSelectNRigids
          kSelectDynamicConstraints
          kSelectNParticles
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source) -> self

        Copy data from source selection mask.

        * source (MSelectionMask) - The source selection mask to copy from
        """
        pass

    def intersects(*args, **kwargs):
        """
        intersects(mask) -> bool
        intersects(selType) -> bool

        Returns True if the specified selection mask or selection type is contained within this selection mask.

        * mask (MSelectionMask) - the selection mask to test.
        * selType (int) - the selection type to test.  See addMask() for a list of valid selection masks.
        """
        pass

    def setMask(*args, **kwargs):
        """
        setMask(mask) -> self
        setMask(selType) -> self

        Sets the selection mask to the specified selection mask or selection type.

        * mask (MSelectionMask) - the selection mask to be set.
        * selType (int) - the selection type to be set.  See addMask() for a list of valid selection masks.
        """
        pass

    @staticmethod
    def deregisterSelectionType(*args, **kwargs):
        """
        deregisterSelectionType(selTypeName) -> bool

        Unregisters a previously registered selection type.

        * selTypeName (string) - Name of the selection type.
        """
        pass

    @staticmethod
    def getSelectionTypePriority(*args, **kwargs):
        """
        getSelectionTypePriority(selTypeName) -> int

        Gets the selection priority corresponding to a given selection type.

        * selTypeName (string) - Name of the selection type.
        """
        pass

    @staticmethod
    def registerSelectionType(*args, **kwargs):
        """
        registerSelectionType(selTypeName, priority=0) -> bool

        Registers a new selection type. It is perfectly legal for 2 plug-ins to register the same selection type.
        Currently we use the registration count. The selection type is deleted only when deregisterSelectionType() as been called the same number of times as this function - registerSelectionType().

        When registerSelectionType() is invoked and the selection type already exists, we neither enable it nor change its priority, just add its registration count by 1.
        The reason is the user might has modified these values after loading the plug-in that has register the selection type the first time.

        * selTypeName (string) - Name of the selection type.
        * priority (int) - Priority of the selection type.
        """
        pass

    kSelectAnimAny = 68

    kSelectAnimCurves = 63

    kSelectAnimInTangents = 65

    kSelectAnimKeyframes = 64

    kSelectAnimMask = 67

    kSelectAnimOutTangents = 66

    kSelectCVs = 30

    kSelectCameras = 6

    kSelectClusters = 8

    kSelectCollisionModels = 21

    kSelectComponentsMask = 62

    kSelectCurveKnots = 47

    kSelectCurveParmPoints = 46

    kSelectCurves = 26

    kSelectCurvesOnSurfaces = 53

    kSelectDynamicConstraints = 82

    kSelectEdges = 42

    kSelectEditPoints = 32

    kSelectEmitters = 16

    kSelectFacets = 43

    kSelectFields = 17

    kSelectFluids = 77

    kSelectFollicles = 79

    kSelectGuideLines = 71

    kSelectHairSystems = 78

    kSelectHandles = 0

    kSelectHulls = 31

    kSelectIkEndEffectors = 3

    kSelectIkHandles = 2

    kSelectIsoparms = 52

    kSelectJointPivots = 57

    kSelectJoints = 4

    kSelectLatticePoints = 55

    kSelectLattices = 7

    kSelectLights = 5

    kSelectLocalAxis = 1

    kSelectLocators = 28

    kSelectManipulators = 70

    kSelectMeshComponents = 45

    kSelectMeshEdges = 34

    kSelectMeshFaces = 36

    kSelectMeshFreeEdges = 35

    kSelectMeshLines = 44

    kSelectMeshUVs = 40

    kSelectMeshVerts = 33

    kSelectMeshes = 12

    kSelectNCloths = 80

    kSelectNParticles = 83

    kSelectNRigids = 81

    kSelectNurbsCurves = 10

    kSelectNurbsSurfaces = 11

    kSelectObjectGroups = 75

    kSelectObjectsMask = 29

    kSelectOrientationLocators = 23

    kSelectPPStrokes = 54

    kSelectParticleShapes = 15

    kSelectParticles = 56

    kSelectPivots = 60

    kSelectPointsForGravity = 72

    kSelectPointsOnCurvesForGravity = 73

    kSelectPointsOnSurfacesForGravity = 74

    kSelectRigidBodies = 19

    kSelectRigidConstraints = 20

    kSelectRotatePivots = 59

    kSelectScalePivots = 58

    kSelectSculpts = 9

    kSelectSelectHandles = 61

    kSelectSketchPlanes = 14

    kSelectSprings = 18

    kSelectSubdiv = 13

    kSelectSubdivMeshEdges = 38

    kSelectSubdivMeshFaces = 39

    kSelectSubdivMeshMaps = 76

    kSelectSubdivMeshPoints = 37

    kSelectSurfaceEdge = 51

    kSelectSurfaceKnots = 49

    kSelectSurfaceParmPoints = 48

    kSelectSurfaceRange = 50

    kSelectSurfaces = 27

    kSelectTemplates = 69

    kSelectTextures = 25

    kSelectUVLocators = 24

    kSelectVertices = 41

    kSelectXYZLocators = 22


class MFnPlugin(MFnBase):
    """
    Register and deregister plug-in services with Maya.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def apiVersion(*args, **kwargs):
        """
        Return the API version required by the plug-in.
        """
        pass

    def deregisterAttributePatternFactory(*args, **kwargs):
        """
        Deregister a user defined attribute pattern factory type from Maya.
        """
        pass

    def deregisterCommand(*args, **kwargs):
        """
        Deregister a user defined command from Maya.
        """
        pass

    def deregisterData(*args, **kwargs):
        """
        Deregister a user defined data type from Maya.
        """
        pass

    def deregisterDragAndDropBehavior(*args, **kwargs):
        """
        Deregister a user defined drag and drop behavior from Maya.
        """
        pass

    def deregisterNode(*args, **kwargs):
        """
        Deregister a user defined dependency node from Maya.
        """
        pass

    def loadPath(*args, **kwargs):
        """
        Return the full path name of the file from which the plug-in was loaded.
        """
        pass

    def name(*args, **kwargs):
        """
        Return the plug-in's name.
        """
        pass

    def registerAttributePatternFactory(*args, **kwargs):
        """
        Register a new attribute pattern factory type with Maya.
        """
        pass

    def registerCommand(*args, **kwargs):
        """
        Register a new command with Maya.
        """
        pass

    def registerData(*args, **kwargs):
        """
        Register a new data type with Maya.
        """
        pass

    def registerDragAndDropBehavior(*args, **kwargs):
        """
        Register a new drag and drop behavior with Maya.
        Once registered, the new behavior can be used to finish connections between node drag and drops from the hyperGraph/hyperShade to other nodes or Maya UI.
        """
        pass

    def registerNode(*args, **kwargs):
        """
        Register a new dependency node with Maya.
        """
        pass

    def registerShape(*args, **kwargs):
        """
        Register a new user defined shape node with Maya.
        To deregister the shape node use the MFnPlugin.deregisterNode().
        """
        pass

    def setName(*args, **kwargs):
        """
        Set the plug-in's name.
        """
        pass

    def vendor(*args, **kwargs):
        """
        Return the plug-in's vendor string.
        """
        pass

    version = None


class MDagMessage(MMessage):
    """
    Class used to register callbacks for Dag related messages.

    The class also provides the following DagMessage constants which describe the different types of DAG operations:
      kParentAdded
      kParentRemoved
      kChildAdded
      kChildRemoved
      kChildReordered
      kInstanceAdded
      kInstanceRemoved
      kInvalidMsg
    """

    @staticmethod
    def addAllDagChangesCallback(*args, **kwargs):
        """
        addAllDagChangesCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any
        DAG change is made to any DAG node.

         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback (see class
                  docs for a list), a MDagPath to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addAllDagChangesDagPathCallback(*args, **kwargs):
        """
        addAllDagChangesDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a DAG
        change is made to the specified DAG path.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback (see class
                  docs for a list), a MDagPath to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addChildAddedCallback(*args, **kwargs):
        """
        addChildAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        added in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addChildAddedDagPathCallback(*args, **kwargs):
        """
        addChildAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        added to the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addChildRemovedCallback(*args, **kwargs):
        """
        addChildRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        removed in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addChildRemovedDagPathCallback(*args, **kwargs):
        """
        addChildRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        removed from the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addChildReorderedCallback(*args, **kwargs):
        """
        addChildReorderedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        reordered in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addChildReorderedDagPathCallback(*args, **kwargs):
        """
        addChildReorderedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child of
        the specified DAG node is reordered

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addDagCallback(*args, **kwargs):
        """
        addDagCallback(msgType, function, clientData=None) -> id

        This method registers a callback that is called for specified
        DAG changes on all nodes. The callback will also receive the
        DagMessage

         * msgType (DagMessage) - The type of DAG change to trigger the callback
         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback (see class
                  docs for a list), a MDagPath to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addDagDagPathCallback(*args, **kwargs):
        """
        addDagDagPathCallback(node, msgType, function, clientData=None) -> id

        This method registers a callback that is called for specified a DAG
        change is made to the specified DAG path. The callback receives the
        DagMessage as well.

         * node (MDagPath) - the DAG node to register the callback for
         * msgType (DagMessage) - The type of DAG change to trigger the callback
          (see class docs for a list)
         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback, a MDagPath
           to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addInstanceAddedCallback(*args, **kwargs):
        """
        addInstanceAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any node in the DAG
        is instanced.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addInstanceAddedDagPathCallback(*args, **kwargs):
        """
        addInstanceAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever the specified node
        is instanced

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addInstanceRemovedCallback(*args, **kwargs):
        """
        addInstanceRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an instance of any DAG
        node is removed or deleted.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addInstanceRemovedDagPathCallback(*args, **kwargs):
        """
        addInstanceRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever an instance of the specified
        node is removed.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addParentAddedCallback(*args, **kwargs):
        """
        addParentAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        added in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addParentAddedDagPathCallback(*args, **kwargs):
        """
        addParentAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        added to the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addParentRemovedCallback(*args, **kwargs):
        """
        addParentRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        removed in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addParentRemovedDagPathCallback(*args, **kwargs):
        """
        addParentRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        removed from the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addWorldMatrixModifiedCallback(*args, **kwargs):
        """
        addWorldMatrixModifiedCallback(node, function, clientData=None) -> id

        This method registers a callback that is called when a DAG node's worldMatrix
        changes.

        Since a node's worldMatrix is affected by the transforms of its ancestors in
        the DAG, it's possible for there to be two different nodes involved: the
        "trigger" node, whose transform has changed, and the "affected" node, whose
        worldMatrix is affected by the change to the trigger.

        The trigger node may be the same as the affected node, or it may be one of
        its ancestors.

        The callback is placed on the affected node, but it is the trigger node which
        is passed to the callback.

        If the trigger node's transformation is already dirty (i.e. it has not been
        evaluated since it was last changed) then the callback will not be triggered.
        So if the trigger node's transformation is modified multiple times between
        evaluations, only the first one will result in the callback being called.

         * affectedNode (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           whose transformation has changed, a MatrixModifiedFlags constant showing
           what has changed (see below for complete list) and the clientData object
         * clientData - User defined data passed to the callback function

        Available MatrixModifiedFlags constants:
        Individual flags:
          kScaleX               kScaleY                 kScaleZ
          kShearXY              kShearXZ                kShearYZ
          kRotateX              kRotateY                kRotateZ
          kTranslateX   kTranslateY             kTranslateZ
          kScalePivotX  kScalePivotY    kScalePivotZ
          kRotatePivotX kRotatePivotY   kRotatePivotZ
          kScaleTransX  kScaleTransY    kScaleTransZ
          kRotateTransX kRotateTransY   kRotateTransZ
          kRotateOrientX        kRotateOrientY  kRotateOrientZ
          kRotateOrder
        Composite flags
          kAll
          kScale                = kScaleX        | kScaleY        | kScaleZ
          kShear                = kShearXY       | kShearXZ       | kShearYZ
          kRotation             = kRotateX       | kRotateY       | kRotateZ
          kTranslation          = kTranslateX    | kTranslateY    | kTranslateZ
          kScalePivot           = kScalePivotX   | kScalePivotY   | kScalePivotZ
          kRotatePivot          = kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
          kScalePivotTrans      = kScaleTransX   | kScaleTransY   | kScaleTransZ
          kRotatePivotTrans     = kRotateTransX  | kRotateTransY  | kRotateTransZ
          kRotateOrient         = kRotateOrientX | kRotateOrientY | kRotateOrientZ

         * return: Identifier used for removing the callback.
        """
        pass

    kAll = 268435455

    kChildAdded = 2

    kChildRemoved = 3

    kChildReordered = 4

    kInstanceAdded = 5

    kInstanceRemoved = 6

    kInvalidMsg = -1

    kLast = 7

    kParentAdded = 0

    kParentRemoved = 1

    kRotateOrder = 134217728

    kRotateOrient = 117440512

    kRotateOrientX = 16777216

    kRotateOrientY = 33554432

    kRotateOrientZ = 67108864

    kRotatePivot = 229376

    kRotatePivotTrans = 14680064

    kRotatePivotX = 32768

    kRotatePivotY = 65536

    kRotatePivotZ = 131072

    kRotateTransX = 2097152

    kRotateTransY = 4194304

    kRotateTransZ = 8388608

    kRotateX = 64

    kRotateY = 128

    kRotateZ = 256

    kRotation = 448

    kScale = 7

    kScalePivot = 28672

    kScalePivotTrans = 1835008

    kScalePivotX = 4096

    kScalePivotY = 8192

    kScalePivotZ = 16384

    kScaleTransX = 262144

    kScaleTransY = 524288

    kScaleTransZ = 1048576

    kScaleX = 1

    kScaleY = 2

    kScaleZ = 4

    kShear = 56

    kShearXY = 8

    kShearXZ = 16

    kShearYZ = 32

    kTranslateX = 512

    kTranslateY = 1024

    kTranslateZ = 2048

    kTranslation = 3584


class MArgDatabase(MArgParser):
    """
    Command argument list parser which extends MArgParser with the
    ability to return arguments and objects as MSelectionLists
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def commandArgumentMSelectionList(*args, **kwargs):
        """
        commandArgumentMSelectionList(argIndex) -> MSelectionList

        Returns the specified command argument as an MSelectionList.
        """
        pass

    def flagArgumentMSelectionList(*args, **kwargs):
        """
        flagArgumentMSelectionList(flagName, argIndex) -> MSelectionList

        Returns the specified argument of the specified single-use flag as
        an MSelectionList.
        """
        pass

    def getObjectList(*args, **kwargs):
        """
        getObjectList() -> MSelectionList

        If the command's MSyntax has set the object format to kSelectionList
        then this method will return the objects passed to the command as an
        MSelectionList. If any other object format is set then an empty
        selection list will be returned.
        """
        pass


class MDGMessage(MMessage):
    """
    Class used to register callbacks for Dependency Graph related messages.
    """

    @staticmethod
    def addConnectionCallback(*args, **kwargs):
        """
        addConnectionCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a connection
        is made or broken in the dependency graph. This callback is triggered
        after the given connection has been made or broken, unlike the addPreConnectionCallback
        which is triggered before the operation.

         * function - callable which will be passed a MPlug indicating the source
           plug of the connection, a MPlug indicating the destination plug of the
           connection, a boolean set to True if a new connection will be made,
           False if it will be broken and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addDelayedTimeChangeCallback(*args, **kwargs):
        """
        addDelayedTimeChangeCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph, but after the time changed callback.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addDelayedTimeChangeRunupCallback(*args, **kwargs):
        """
        addDelayedTimeChangeRunupCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph, but after the other time changed callbacks
        which can be used to invoke a dynamics solve or runup if needed

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addForceUpdateCallback(*args, **kwargs):
        """
        addForceUpdateCallback(function, clientData=None) -> id

        This method registers a callback that is called after the time
        changes and after all nodes have been evaluated in the
        dependency graph.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeAddedCallback(*args, **kwargs):
        """
        addNodeAddedCallback(function, nodeType, clientData=None) -> id

        This method registers a callback that is called whenever a new node
        is added to the dependency graph.
        The nodeType argument allows you to specify the type of nodes that
        will trigger the callback. The default node type is "dependNode" which
        matches all nodes.

         * function - callable which will be passed a MObject indicating
           the new node and the clientData object
         * nodeType (MString) - type of node that will trigger the callback
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeChangeUuidCheckCallback(*args, **kwargs):
        """
        addNodeChangeUuidCheckCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a node
        may have its UUID changed. Possible causes include the 'rename' command,
        and the UUID for a node being read from a file during file I/O.

        Note that nodes are assigned a UUID when they are created; this does
        not invoke this callback. During file I/O the stored UUID is applied as
        a separate step after creation (which does invoke this callback).

        Depending on the situation Maya may or may not use the new UUID by default.
        For example, when importing a file, Maya reads the UUID from the file
        but does not use it. The boolean argument to the callback function lets
        the callback know whether Maya is intending to use the UUID or not.

        The callback returns a MMessage.Action constant:
                * kDefaultAction - The callback does not want to change whether the
                  UUID is used or not.
                * kDoNotDoAction - Do not use the new UUID.
                * kDoAction - Use the new UUID.

        In any case, the callback may leave the new uuid as is, or may provide
        a new uuid of its own choosing to be used instead.

         * function - callable which will be passed a boolean indicating whether
           the UUID will be applied, a MObject indicating the node whose UUID may
           be changed, the MUuid that may be applied to the node (typically the one
           read from the file, during file I/O) - the callback may provide its own
           uuid to be applied by changing this parameter - and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeRemovedCallback(*args, **kwargs):
        """
        addNodeRemovedCallback(function, nodeType, clientData=None) -> id

        This method registers a callback that is called whenever a new node
        is removed from the dependency graph.
        The nodeType argument allows you to specify the type of nodes that
        will trigger the callback. The default node type is "dependNode" which
        matches all nodes.

         * function - callable which will be passed a MObject indicating
           the node being removed and the clientData object
         * nodeType (MString) - type of node that will trigger the callback
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addPreConnectionCallback(*args, **kwargs):
        """
        addPreConnectionCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any connection
        is made or broken in the dependency graph. This callback is triggered before
        the given connection has been made or broken, unlike the addConnectionCallback
        which is triggered after the operation.

         * function - callable which will be passed a MPlug indicating the source
           plug of the connection, a MPlug indicating the destination plug of the
           connection, a boolean set to True if a new connection will be made,
           False if it will be broken and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addTimeChangeCallback(*args, **kwargs):
        """
        addTimeChangeCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass


class MEventMessage(MMessage):
    """
    Class used to register callbacks for event related messages.
    """

    @staticmethod
    def addEventCallback(*args, **kwargs):
        """
        addEventCallback(eventName, function, clientData=None) -> id

        This method registers a callback for event occurred messages.
        The callback function will be passed the any client data that
        was provided when the callback was registered.

         * eventName (string) - the event to register the
        callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def getEventNames(*args, **kwargs):
        """
        getEventNames() -> (string, string, ...)

        This method returns the list of available event names.

         * return: tuple of available event names.
        """
        pass


class MLockMessage(MMessage):
    """
    Class used to register callbacks for model related messages.
    """

    @staticmethod
    def setNodeLockDAGQueryCallback(*args, **kwargs):
        """
        setNodeLockDAGQueryCallback(dagPath, function, clientData=None) -> id

        This methods registers a callback that is invoked in any situation
        involving a locking condition on DAG level changes.  When called,
        the API user can make a decision on how to handle the given locking
        situation. The programmer can either accept the default action, or
        they can deny the default action. The decision is returned through a
        decision variable which is passed to the callback function.

        The callback function takes the following parameters:
         * dagPath - The DAG path that the event occurred on.
         * otherPath - The other path involved, e.g. the new parent.
         * clientData - User defined data passed to the callback function.
         * eventType - Description of the event.
        And return True to accept the default behavior and False to
        reject it.

         The meanings of the dagPath and otherPath parameters for each
        eventType, and default actions associated with those event types, are
        as follows:

        kGroup
         * dagPath - Path of the node to be grouped.
         * otherPath - Path of the group node.
         * default actions - If dagPath
           is locked then the default action is to not allow the grouping.
           If dagPath is unlocked then dagPath
           can be grouped with otherPath.

        kUnGroup
         * dagPath - Path of the node attempted to ungroup.
         * otherPath - Path of the group node.
         * default actions - If dagPath is locked then
           the default action is to not allow the ungrouping. If dagPath
           is unlocked then dagPath can be ungrouped from otherPath.

        kReparent
         * dagPath - Path of the node which is being reparented.
         * otherPath - Path of the new parent, if any. When
           reparenting to the world, otherPath will be invalid.
         * default actions - If dagPath is locked then
           the default action is to not allow the reparenting. If dagPath
           is unlocked then dagPath can be parented to otherPath.

        kChildReorder
         * dagPath - Path of the child node to be reordered.
         * otherPath - Path of the parent node.
         * default actions - If dagPath is locked then
           the default action is to not allow the reordering. If dagPath
           is unlocked then dagPath can be reordered on otherPath.

        kCreateNodeInstance
         * dagPath - Path of the node which is being instanced.
         * otherPath - Invalid Path.
         * default actions - If dagPath is locked then
           the default action is to not allow the instance to be created.
           If dagPath is unlocked then dagPath can be instanced.

        kCreateChildInstance
         * dagPath - Path of the node whose child is being
           instanced.
         * otherPath - Path of the child node.
         * default actions - If dagPath is locked then
           the default action is to not allow the instance to be created.
           If dagPath is unlocked then dagPath can be instanced.

         * dagPath (MDagPath) - The path to attach the callback.
         * function - the callback function (see below for the description)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def setNodeLockQueryCallback(*args, **kwargs):
        """
        setNodeLockQueryCallback(node, function, clientData=None) -> id

        This methods registers a callback that is invoked in any locking
        condition on node properties, e.g. name, lock status, etc. When
        called, the API user can make a decision on how to handle the given
        locking situation. The programmer can either accept the default
        action, or they can deny the default action. The decision is returned
        through a decision variable which is passed to the callback function.

        The callback function takes the following parameters:
           * node - The node that triggered the callback.
           * aux - Any auxiliary data that may be needed, e.g.
             the attribute about to be added.
           * clientData - User defined data passed to the
             callback function.
           * eventType - Description of the event.
        And return True to accept the default behavior and False to
        reject it.

        The meanings of the node and aux parameters for each
        eventType, and default actions associated with those event types, are
        as follows:

        kRename
           * node - The node that the user is attempting to rename.
           * aux - MObject.kNullObj
           * default actions - If node is locked then the
             default action is to not allow the rename. Otherwise,
             if node is unlocked then node can be renamed.

        kDelete   * node - The node that the user is attempting to delete.
           * aux - MObject.kNullObj
           * default actions - If node is locked then the
             default action is to not allow the delete. If node is unlocked
             then the node can be deleted.

        kLockNode   * node - The node that the user is attempting to lock.
           * aux - MObject.kNullObj
           * default actions - If node is unlocked then the
             default action is to ALLOW the node to be locked. The callback
             is not invoked when the user tries to unlock an already unlocked
             node.

        kUnlockNode   * node - The node that the user is attempting to unlock.
           * aux - MObject.kNullObj
           * default actions - If node is locked then the
             default action is to ALLOW the unlock. The callback is not invoked
             when the user tries to unlock an already unlocked node.

        kAddAttr   * node - The node that is having an attribute added.
           * aux - MObject of the attribute to be added. Note:
             the attribute does not belong to the node yet. You can only
             access the attribute information using MFnAttribute.
           * default actions - If node is locked then the default
             action is to not allow to the addition of aux. If node
             is unlocked then aux can be added to the node.

        kRemoveAttr
           * node - The node that is having an attribute removed.
           * aux - The attribute to be removed. In certain
             situations the user is allowed to do a global delete,
             e.g. "deleteAttr -at AttrName [nodes]". In these cases the plug is not
             created until checks have been performed; so aux ==
             MObject.kNullObj
           * default actions - If node is locked then the default
             action is to not allow the attribute removal. If node is
             unlocked then aux can be removed.

        kRenameAttr
           * node - The node that is having an attribute renamed.
           * aux - The attribute.
           * default actions - If node is locked then the default
             action is to not allow the rename. If node is unlocked then
             aux can be renamed.

        kUnlockAttr
           * node - The node that is having an attribute unlocked.
           * aux - The attribute to be unlocked.
           * default actions - If node is locked then the default
             action is to not allow the unlock. If node is unlocked then
             aux attribute can be unlocked.

        kLockAttr
           * node - The node that is having an attribute locked.
           * aux - The attribute to be locked.
           * default actions - If node is locked then the default
             action is to not allow the locking of aux. If node is
             unlocked then aux can be locked.

         * node (MObject) - The node to register the callback for.
         * function - the callback function (see below for description)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def setPlugLockQueryCallback(*args, **kwargs):
        """
        setPlugLockQueryCallback(plug, function, clientData=None) -> id

        This method registers a callback that is invoked in any locking
        condition on a plug, e.g. plug unlock, plug lock, connections, etc.
        When the callback is invoked, the API programmer can make a decision on
        how to handle the given locking situation. The programmer can either
        accept the default action, or they can deny the default action.
        The decision is made through the decision variable described above.

        The callback function takes the following parameters:
           * plug - The plug that triggered the callback.
           * otherPlug - The other plug involved in the callback.
             This is only valid during connect and disconnect events.
             clientData - User defined data passed to the
             callback function.
           * eventType - Description of the event.
        And return True to accept the default behavior and False to
        reject it.

        The meanings of the plug and otherPlug parameters for each
        eventType, and default actions associated with those event types, are
        as follows:

        kPlugLockAttr
           * plug - The plug that the user is attempting to lock.
           * otherPlug - None.
           * default actions - If plug is unlocked then the
             default action is to allow the plug to be locked.

        kPlugUnlockAttr
           * plug - The plug that the user is attempting to unlock.
           * otherPlug - None.
           * default actions - If plug is locked then the
             default action is to allow the plug to be unlocked.

        kPlugAttrValChange
           * plug - The plug that the user is attempting to change.
           * otherPlug - None.
           * default actions - If plug is locked then the
             default action is to not allow plug to change. If plug is
             unlocked then plug can change.

        kPlugRemoveAttr
           * plug - The plug that the user is attempting to remove.
           * otherPlug - None.
           * default actions - If plug is locked then the
             default action is to not allow removal. Otherwise, if plug is
             unlocked then plug can be removed.

        kPlugRenameAttr
           * plug - The plug that the user is attempting to rename.
           * otherPlug - None.
           * default actions - If plug is locked then the default
             action is to not allow the rename. Otherwise, if plug is
             unlocked then plug can be renamed.

        kPlugConnect
           * plug - The plug that is to be connected (incoming
             connection).
           * otherPlug - The source plug of the connection being made.
           * default actions - If plug is locked then the
             connection is DENIED. If plug is unlocked then otherPlug can
             be connected to plug.

        kPlugDisconnect
           * plug - The plug that it is having an incoming connection broken.
           * otherPlug - The source plug of the connection being made.
           * default actions - If plug is locked then the
             default action is to DENY the connection from being broken. If
             plug is unlocked then otherPlug can be disconnected from
             plug.

         * plug (MPlug) - the plug to attach the callback
         * function - the callback function (see below for description)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    kAddAttr = 5

    kChildReorder = 4

    kCreateChildInstance = 6

    kCreateNodeInstance = 5

    kCreateParentInstance = 7

    kDelete = 2

    kGroup = 1

    kInvalid = 0

    kInvalidDAG = 0

    kInvalidPlug = 0

    kLast = 10

    kLastDAG = 8

    kLastPlug = 8

    kLockAttr = 9

    kLockNode = 3

    kPlugAttrValChange = 3

    kPlugConnect = 6

    kPlugDisconnect = 7

    kPlugLockAttr = 1

    kPlugRemoveAttr = 4

    kPlugRenameAttr = 5

    kPlugUnlockAttr = 2

    kRemoveAttr = 6

    kRename = 1

    kRenameAttr = 7

    kReparent = 3

    kUnGroup = 2

    kUnlockAttr = 8

    kUnlockNode = 4


class MPxGeometryData(MPxData):
    """
    Base Class for User-defined Dependency Graph Geometry Data Types.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def deleteComponent(*args, **kwargs):
        """
        deleteComponent(compList) -> bool

        This method should be overridden if this data is to support component deletion. For user defined shapes (MPxSurfaceShape) which support components, this method must be overridden if component deletion is to be supported when the shape has history.

        Returns True if the deletion was successfull, False otherwise.

        * compList (MObjectArray) - a list of components that are to be deleted
        """
        pass

    def deleteComponentsFromGroups(*args, **kwargs):
        """
        deleteComponentsFromGroups(compList, groupIdArray, groupComponentArray) -> bool

        This method should be overridden to modify the groups that flows along with the geometry, as part of the data, based on the components being deleted. It should intelligently update the groups based on what gets deleted. The class MFnGeometryData can be used to access and modify grouping information for data.

        Returns True if the deletion was successfull, False otherwise.

        The groupIdArray and groupComponentArray should contain the updated grouping information after the deletion has occurred.

        * compList (MObjectArray) - a list of components that are to be deleted
        * groupIdArray [OUT] (MIntArray) - array of group id's
        * groupComponentArray (MObjectArray) - array of updated components, one for each group id
        """
        pass

    def getMatrix(*args, **kwargs):
        """
        getMatrix(matrix) -> bool

        Gets the matrix associated to MPxGeometryData and retursn True if is identity

        * matrix [OUT] (MMatrix) - the returned matrix that takes a point from local object space to world space.
        """
        pass

    def iterator(*args, **kwargs):
        """
        iterator(componentList, component, useComponents, world=None) -> MPxGeometryIterator

        Associates a control point based geometry iterator with this data.
        This method is used in conjunction with MPxSurfaceShape and should be overridden if your shape is to support maya's deformations.

        The useComponents argument specifies whether the iteration is over the given componentList or the component.

        Returns an iterator for your geometry.

        * componentList (MObjectArray) - a list of components that are to be iterated over.
        * component (MObject) - a component to be iterator over.
        * useComponents (bool) - if True then componentList is to be iterated over, otherwise the iteration is on component.
        * world (bool) - specifies whether the iteration is for world space data.
        """
        pass

    def smartCopy(*args, **kwargs):
        """
        smartCopy(srcGeom) -> self

        This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

        This method is used to prvoide maya with an efficient way to copy the source data into the memory of this data with as little memory allocation as possible.

        This method is not mandatory and only needs to be overridden to improve performance of deformations on shapes.

        * srcGeom (MPxGeometryData) - the data to be copied
        """
        pass

    def updateCompleteVertexGroup(*args, **kwargs):
        """
        updateCompleteVertexGroup(component) -> bool

        This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

        This method should make sure that complete vertex group data is up-to-date.
        If the given component is not complete (i.e. it represents all elements of your geometry) then you must mark is as complete using the methods of MFnComponent and return true if the component was updated, false if it was already complete.

        This method is used by deformers when deforming the "whole" object and not just selected components.

        Returns true if the component was updated, false if it was already complete.

        * component (MObject) - the component to test
        """
        pass

    matrix = None


class MModelMessage(MMessage):
    """
    Class used to register callbacks for model related messages.The class also provides the following Message constants which
    describe the different types supported by the addCallback method:
      kActiveListModified           #active selection changes
    """

    @staticmethod
    def addAfterDuplicateCallback(*args, **kwargs):
        """
        addAfterDuplicateCallback(function, clientData=None) -> id

        This method registers a callback that is called after a duplicate
        command is made. The callback will be called after everything is
        duplicated.

         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addBeforeDuplicateCallback(*args, **kwargs):
        """
        addBeforeDuplicateCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a duplicate
        command is made. The callback will be called before anything is
        duplicated.

         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addCallback(*args, **kwargs):
        """
        addCallback(message, function, clientData=None) -> id

        Adds a new callback for the specified model message.


         * message (Message constant, see class doc for a list) - the model
           message that will trigger the callback
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeAddedToModelCallback(*args, **kwargs):
        """
        addNodeAddedToModelCallback(dagNode, function, clientData=None) -> id

        This method registers a callback that is called when a dag node is about
        to be added to the Maya model.

         * dagNode (MObject) - Node that should acquire the callback
         * function - callable which will be passed a MObject indicating
           the node being added to the model and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeRemovedFromModelCallback(*args, **kwargs):
        """
        addNodeRemovedFromModelCallback(dagNode, function, clientData=None) -> id

        This method registers a callback that is called when the
        specified dag node is being removed from the Maya model.

         * dagNode (MObject) - Node that should acquire the callback
         * function - callable which will be passed a MObject indicating
           the node being removed to the model and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    kActiveListModified = 0


class MFnAttribute(MFnBase):
    """
    Base class for attribute functionsets.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)
        self._fn_type = MFn.kAttribute

    def _create(self, long_name:str, short_name:str) -> 'MObject':
        """Regular MFnAttribute does not have this method. Implemented here form commodity and reuse."""

        # Spawn new MObject
        super()._create()
        self._mobject._init_attribute_fields()

        # Set the attribute name
        self._mobject._long_name = long_name
        self._mobject._short_name = short_name
        self._mobject._name = long_name

        # Set valid and attribute type
        self._mobject._alive = True
        self._mobject._api_type = [MFn.kBase, MFn.kAttribute,]

        return self._mobject

    def accepts(*args, **kwargs):
        """
        Returns True if this attribute can accept a connection of the given type.
        """
        pass

    def acceptsAttribute(*args, **kwargs):
        """
        Returns True if this attribute can accept a connection with the given attribute.
        """
        pass

    def addToCategory(*args, **kwargs):
        """
        Adds the attribute to a category
        """
        pass

    def getAddAttrCmd(*args, **kwargs):
        """
        Returns a string containing a MEL 'addAttr' command capable of recreating the attribute.
        """
        pass

    def hasCategory(*args, **kwargs):
        """
        Checks to see if the attribute has a given category
        """
        pass

    def setNiceNameOverride(*args, **kwargs):
        """
        Sets a nice UI name for this attribute rather than using the default derived from it's long name.
        """
        pass

    @property
    def array(self):
        return self._mobject._is_array

    @array.setter
    def array(self, value: bool):
        self._mobject._is_array = value

    @property
    def cached(self) -> bool:
        return self._mobject._is_cached

    @cached.setter
    def cached(self, value: bool):
        self._mobject._is_cached = value

    @property
    def channelBox(self) -> bool:
        return self._mobject._channel_box

    @channelBox.setter
    def channelBox(self, value: bool):
        self._mobject._channel_box = value

    @property
    def connectable(self) -> bool:
        return self._mobject._connectable

    @connectable.setter
    def connectable(self, value: bool):
        self._mobject._connectable = value

    @property
    def disconnectBehavior(self) -> int:
        return self._mobject._disconnect_behavior

    @disconnectBehavior.setter
    def disconnectBehavior(self, value: int):
        self._mobject._disconnect_behavior = value

    @property
    def dynamic(self):
        return self._mobject._dynamic

    @property
    def extension(self):
        return self._mobject._extension

    @property
    def hidden(self) -> bool:
        return self._mobject._hidden

    @hidden.setter
    def hidden(self, value: bool):
        self._mobject._hidden = value

    @property
    def indeterminant(self) -> bool:
        return self._mobject._indeterminant

    @indeterminant.setter
    def indeterminant(self, value: bool):
        self._mobject._indeterminant = value

    @property
    def indexMatters(self) -> bool:
        return self._mobject._index_matters

    @indexMatters.setter
    def indexMatters(self, value: bool):
        self._mobject._indexMatters = value

    @property
    def internal(self) -> bool:
        return self._mobject._internal

    @internal.setter
    def internal(self, value: bool):
        self._mobject._internal = value

    @property
    def isProxyAttribute(self):
        return self._mobject._isProxyAttribute

    @property
    def keyable(self):
        return self._mobject._keyable

    @keyable.setter
    def keyable(self, value: bool):
        self._mobject._keyable = value

    @property
    def name(self):
        return self._mobject._long_name

    @property
    def parent(self):
        parent = self._mobject._parent
        return parent if parent else MObject.kNullObj

    @parent.setter
    def parent(self, value: 'MObject'):
        self._mobject._parent = value

    @property
    def readable(self):
        return self._mobject._readable

    @readable.setter
    def readable(self, value: bool):
        self._mobject._readable = value

    @property
    def renderSource(self):
        return self._mobject._renderSource

    @renderSource.setter
    def renderSource(self, value: bool):
        self._mobject._renderSource = value

    @property
    def shortName(self):
        return self._mobject._short_name

    @property
    def storable(self) -> bool:
        return self._mobject._storable

    @storable.setter
    def storable(self, value: bool):
        self._mobject._storable = value

    @property
    def usedAsColor(self) -> bool:
        return self._mobject._used_as_color

    @usedAsColor.setter
    def usedAsColor(self, value: bool):
        self._mobject._used_as_color = value

    @property
    def usedAsFilename(self) -> bool:
        return self._mobject._used_as_filename

    @usedAsFilename.setter
    def usedAsFilename(self, value: bool):
        self._mobject._used_as_filename = value

    @property
    def usesArrayDataBuilder(self) -> bool:
        return self._mobject._uses_array_data_builder

    @usesArrayDataBuilder.setter
    def usesArrayDataBuilder(self, value: bool):
        self._mobject._uses_array_data_builder = value

    @property
    def worldSpace(self) -> bool:
        return self._mobject._world_space

    @worldSpace.setter
    def worldSpace(self, value: bool):
        self._mobject._world_space = value

    @property
    def writable(self) -> bool:
        return self._mobject._writable

    @writable.setter
    def writable(self, value: bool):
        self._mobject._writable = value

    @property
    def affectsAppearance(self):
        return self._mobject._affects_appearance

    @affectsAppearance.setter
    def affectsAppearance(self, value):
        self._mobject._affects_appearance = value

    @property
    def affectsWorldSpace(self):
        return self._mobject._affects_world_space

    @affectsWorldSpace.setter
    def affectsWorldSpace(self, value):
        self._mobject._affects_world_space = value

    kDelete = 0
    kReset = 1
    kNothing = 2


class MNodeMessage(MMessage):
    """
    Class used to register callbacks for dependency node messages of specific dependency nodes.

    The class also provides the following AttributeMessage constants which describe
    the type of attribute changed/addedOrRemoved messages that has occurred:
      kConnectionMade               #a connection has been made to an attribute of this node
      kConnectionBroken     #a connection has been broken for an attribute of this node
      kAttributeEval                #an attribute of this node has been evaluated
      kAttributeSet         #an attribute value of this node has been set
      kAttributeLocked              #an attribute of this node has been locked
      kAttributeUnlocked    #an attribute of this node has been unlocked
      kAttributeAdded               #an attribute has been added to this node
      kAttributeRemoved     #an attribute has been removed from this node
      kAttributeRenamed     #an attribute of this node has been renamed
      kAttributeKeyable     #an attribute of this node has been marked keyable
      kAttributeUnkeyable   #an attribute of this node has been marked unkeyable
      kIncomingDirection    #the connection was coming into the node
      kAttributeArrayAdded  #an array attribute has been added to this node
      kAttributeArrayRemoved        #an array attribute has been removed from this node
      kOtherPlugSet         #the otherPlug data has been set


    The class also provides the following KeyableChangeMsg constants which
    allows user to prevent attributes from becoming (un)keyable:
      kKeyChangeInvalid
      kMakeKeyable
      kMakeUnkeyable
      kKeyChangeLast
    """

    @staticmethod
    def addAttributeAddedOrRemovedCallback(*args, **kwargs):
        """
        addAttributeAddedOrRemovedCallback(node, function, clientData=None) -> id

        Registers callbacks for attribute add/removed messages.
        This is a more specific version of addAttributeChanged as only attribute
        added and attribute removed messages will trigger the callback.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed an AttributeMessage constant (see
           class doc for a list) containing the kind of attribute change triggering
           the callback, a MObject indicating the node's plug where the connection
           changed and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addAttributeChangedCallback(*args, **kwargs):
        """
        addAttributeChangedCallback(node, function, clientData=None) -> id

        This method registers a callback for attribute changed messages.
        See the AttributeChanged enum for a list of all possible messages
        that will trigger the callback.

        Note: Attribute Changed messages will not be generated
        while Maya is either in playback or scrubbing modes. If you need to
        do something during playback or scrubbing you will have to register
        a callback for the timeChanged message which is the only
        message that is sent during those modes.

        The callback function will be passed the type of attribute message
        that has occurred, the plug(s) for the attributes, and any client
        data that the user wishes to pass in.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed an AttributeMessage constant (see
           class doc for a list) containing the kind of attribute change triggering
           the callback, a MObject indicating the node's plug where the connection
           changed, a MObject indicating the plug opposite the node's plug where the
           connection changed and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addKeyableChangeOverride(*args, **kwargs):
        """
        addKeyableChangeOverride(plug, function, clientData=None) -> id

        This method registers a callback that is invoked by any class that
        changes the keyable state of an attribute.  When the callback is
        invoked, the API programmer can make a decision on how to handle
        the given keyable change event.  The programmer can either accept
        the keyable state change by returning True
        or reject it by returning False.

        Note: you can only attach one callback keyable change override
        callback per attribute.  It is an error to attach more than one
        callback to the same attribute.

         * plug (MPlug) - The plug to which to attach the callback.
         * function - callable which will be passed a MPlug indicating the plug that
           has triggered the callback, the clientData object, and a KeyableChangeMsg
           constant (see class doc for a list) containing the kind of Keyable change
           the callback, a MObject indicating the node's plug where the connection.
           User can return True to accept the keyable state change or False to reject it.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNameChangedCallback(*args, **kwargs):
        """
        addNameChangedCallback(node, function, clientData=None) -> id

        Registers a callback for name changed messages.

         * node (MObject) - the node. If this is a NULL MObject then the callback
           applies to all node name changes.
         * function - callable which will be passed a MObject indicating the node whose
           name's changed, a string containing the previous name of the node and the
           clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeAboutToDeleteCallback(*args, **kwargs):
        """
        addNodeAboutToDeleteCallback(node, function, clientData=None) -> id

        Registers a callback which will get called when a node is about to
        be deleted.

        The callback will be passed the MDGModifer that will be used to
        delete the node. This modifier can be used to do any DG modifications,
        such as disconnections, before the node is deleted.  These operations are
        also stored and performed when the deletion operation is undone or redone.

        The callback registered with this method will only get called when the
        deletion operation is first performed. Undos and redos will be handled solely
        through the MDGModifier which was passed to the callback on the original
        deletion. If you also wish to receive notification of deletion events
        when they are redone, you should register an additional callback using
        addNodePreRemovalCallback().

        When a node is deleted Maya automatically breaks all connections to that
        node. This process takes place after the callback has been called. This
        means that if you use the passed-in MDGModifier to break any
        connections to the node you must be sure to call the modifier's doIt() method
        before returning from the callback. Otherwise Maya will see that the connections
        still exist and try to delete them again, which can lead to errors.

        Note that it uses the passed-in MDGModifier to perform all the disconnections and
        connections. This ensures that if the deletion is undone or redone then all of
        the connections will be restored correctly.

        After it is done breaking connections, the callback calls the
        modifier's doIt() method to commit those disconnections. As noted
        above, this is necessary to ensure that Maya doesn't see the
        connections and try to break them again later on.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node that
           will be deleted, a MDGModifier indicating the DG modifier used to delete the
           node and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeDestroyedCallback(*args, **kwargs):
        """
        addNodeDestroyedCallback(node, function, clientData=None) -> id

        Registers a callback which will get called when a node's destructor is
        called.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeDirtyCallback(*args, **kwargs):
        """
        addNodeDirtyCallback(node, function, clientData=None) -> id

        Registers a callback for node dirty messages.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that has  become dirty and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodeDirtyPlugCallback(*args, **kwargs):
        """
        addNodeDirtyPlugCallback(node, function, clientData=None) -> id

        Registers a callback for node dirty messages.  This callback provides
        the plug on the node that was dirtied.  Only provides dirty information
        on input plugs.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that has  become dirty, a MPlug indicating the plug on the node that has
           become dirty and the clientData object * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addNodePreRemovalCallback(*args, **kwargs):
        """
        addNodePreRemovalCallback(node, function, clientData=None) -> id

        Registers a callback which will get called before a node is deleted.
        This callback is called before connections on the node are removed.
        Unlike the aboutToDelete callback, this callback will be invoked whenever
        the node is deleted, even during a redo.

        Pre-removal and aboutToDelete callbacks serve different purposes.  If DG
        changes need to be made when a node is deleted, the aboutToDelete callback
        should be used to add undoable operations to an MDGModifier to perform
        these changes.  When the desired actions cannot be accomplished using the
        MDGModifier passed to the aboutToDelete callback, this callback can be
        used to receive notification of the deletion event, even during redo.

        Note that this callback method should not perform any DG operations.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that is being deleted and the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addUuidChangedCallback(*args, **kwargs):
        """
        addUuidChangedCallback(node, function, clientData=None) -> id

        Registers a callback for UUID changed messages.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that is being modified, a MUuid containing the previous UUID of the node
           and the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """
        pass

    kAttributeAdded = 64

    kAttributeArrayAdded = 4096

    kAttributeArrayRemoved = 8192

    kAttributeEval = 4

    kAttributeKeyable = 512

    kAttributeLocked = 16

    kAttributeRemoved = 128

    kAttributeRenamed = 256

    kAttributeSet = 8

    kAttributeUnkeyable = 1024

    kAttributeUnlocked = 32

    kConnectionBroken = 2

    kConnectionMade = 1

    kIncomingDirection = 2048

    kKeyChangeInvalid = 0

    kKeyChangeLast = 3

    kLast = 32768

    kMakeKeyable = 1

    kMakeUnkeyable = 2

    kOtherPlugSet = 16384


class MFnComponent(MFnBase):
    """
    This is the base class for all function sets which deal with
    component objects.

    __init__()
    Initializes a new, empty MFnComponent object
    __init__(MObject component)
    Initializes a new MFnComponent function set, attached to the specified component.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def isEqual(*args, **kwargs):
        """
        isEqual(MObject other) -> bool

        Returns True if other refers to the same component as the
        one to which the function set is currently attached.
        """
        pass

    def weight(*args, **kwargs):
        """
        weight(index) -> MWeight

        Returns the weight associated with the specified element,
        where index can range from 0 to elementCount-1.
        """
        pass

    componentType = None

    elementCount = None

    hasWeights = None

    isComplete = None

    isEmpty = None


class MPolyMessage(MMessage):
    """
    Class used to register callbacks for poly related messages.
    """

    @staticmethod
    def addPolyComponentIdChangedCallback(*args, **kwargs):
        """
        addPolyComponentIdChangedCallback(node, (wantVertIds, wantEdgeIds, wantFaceIds), function, clientData=None) -> id

        This method registers a callback that should be called whenever a poly
        component id is modified.
        Currently, there are some cases where the component ids for a polygonal
        mesh can be modified without generating a callback or without generating a
        correct mapping.  These cases are outlined below.

        - Polygonal mesh has construction history enabled, and there is more than
                 one topology changing operation in the history.  In this case, the
                 callback is only called when the component ID mapping changes for the
                 most recent operation, and performs the mapping with respect to the
                 input and output meshes for this operation node.
        - Polygonal mesh has construction history enabled, and the most recent
                 topology changing operation is no longer the most recent operation.
                 In this case, no id remapping callbacks will be invoked when the
                 attributes on the operation node are changed in the history.
        - When undo is used to revert a topology changing operation, the callback
                 will not be invoked.  The MEventMessage class can be used to get
                 notification when undo is performed.


        Component id mapping should always work correctly when construction history
        is off.  It should also work correctly when construction history is on and
        only the most recent operation is permitted to be adjusted (eg. changing
        the distance parameter for a merge vertex node, when merge vertices was the
        most recent operation.)  In either case, undo will not produce a poly
        message callback.

         * node (MObject) - the node the callback function should listen to
         *(wantVertIds, wantEdgeIds, wantFaceIds) - tuple of 3 booleans specifying
           what arrays should be provided to the callback function when it is
           invoked: (vertex indices, edge indices, face indices).
         * function - callable which will be passed a tuple and the clientData object.
           The tuple will contain three MUintArrays which are, respectively, the vertex,
           edge and face ids of the modified components. Only the arrays which were requested
           when the callback was registered will contain data, the others will be empty.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addPolyTopologyChangedCallback(*args, **kwargs):
        """
        addPolyTopologyChangedCallback(node, function, clientData=None) -> id

        This method registers a callback that will be called when a node impacting
        the topology of a meshShape is modified. Because the callback is invoked
        before the mesh has evaluated, the new topology data cannot be
        queried at the time the callback is received. If you want to receive a
        callback at a time when the new mesh data can be queried, use the
        following technique:

        - Use this method to register a topology-changed callback.
        - In the topology-changed callback, add an MNodeMessage.addAttributeChangedCallback on the mesh shape.
        - In the attribute-changed callback, check the inputs for an MNodeMessage.kAttributeEval message received by the "outMesh" plug of the mesh.
        - Once you have received the eval message on that plug, the attribute-changed callback can be removed and the mesh topology can be queried.

         * node (MObject) - the node the callback function should listen to
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass


class MSceneMessage(MMessage):
    """
    Class used to register callbacks for scene related messages.
    """

    @staticmethod
    def addCallback(*args, **kwargs):
        """
        addCallback(message, function, clientData=None) -> id

        Adds a new callback for the specified scene message.
        If a 'before' message is sent, the corresponding 'after' message
        will be as well.
        Callbacks can be added to the following Message constant with this function: kSceneUpdate
         kBeforeNew
         kAfterNew
         kBeforeImport
         kAfterImport
         kBeforeOpen
         kAfterOpen
         kBeforeFileRead
         kAfterFileRead
         kAfterSceneReadAndRecordEdits
         kBeforeExport
         kExportStarted
         kAfterExport
         kBeforeSave
         kAfterSave
         kBeforeCreateReference
         kBeforeCreateReferenceAndRecordEdits
         kAfterCreateReference
         kAfterCreateReferenceAndRecordEdits
         kBeforeRemoveReference
         kAfterRemoveReference
         kBeforeImportReference
         kAfterImportReference
         kBeforeExportReference
         kAfterExportReference
         kBeforeUnloadReference
         kAfterUnloadReference
         kBeforeLoadReference
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReference
         kAfterLoadReferenceAndRecordEdits
         kBeforeSoftwareRender
         kAfterSoftwareRender
         kBeforeSoftwareFrameRender
         kAfterSoftwareFrameRender
         kSoftwareRenderInterrupted
         kMayaInitialized
         kMayaExiting

        Note that for referencing, the creation of the reference (i.e. creation of
        the reference node and associated structures) is separate from the loading
        of the reference itself (i.e. read the nodes from file).

        The kBeforeCreateReference message will be sent when a reference is created.
        So it will happen for both loaded and unloaded references. But the
        kBeforeLoadReference message will only be sent when the file is read from disk.

        When opening a file with a loaded reference, the callback order is as follows:
         kBeforeCreateReference
         kBeforeCreateReferenceAndRecordEdits
         kBeforeCreateReferenceAndRecordEdits
         kAfterCreateReferenceAndRecordEdits

         kBeforeLoadReference
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReference
         kAfterLoadReferenceAndRecordEdits

        By default, edits to referenced objects will not be recorded during the execution
        of file I/O callbacks. A specific set of callbacks are provided that will enable
        the recording of reference edits during their execution as follows:
         kAfterSceneReadAndRecordEdits
         kBeforeCreateReferenceAndRecordEdits
         kAfterCreateReferenceAndRecordEdits
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReferenceAndRecordEdits

        The kExportStarted callback is sent after the kBeforeExport callback, once Maya
        has actually started to process the exported data. One important difference between
        the two callbacks is that the fileInfo command affects the exported scene when used
        in the kExportStarted callback, but affects the current scene in memory when used
        in the kBeforeExport callback.

         * message - the Message constant that will trigger the callback
         * function - callable which will be passed the clientData object
         * clientData - user data that will be passed to the callback function
        """
        pass

    @staticmethod
    def addCheckCallback(*args, **kwargs):
        """
        addCheckCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message.
        The callback will have the ability to abort the current operation
        by returning False.

        Callbacks can be added to the following messages with this function:
         kBeforeNewCheck
         kBeforeImportCheck
         kBeforeOpenCheck
         kBeforeExportCheck
         kBeforeSaveCheck
         kBeforeCreateReferenceCheck
         kBeforeLoadReferenceCheck

         * message - the scene message that will trigger the callback
         * function - callable which will be passed the clientData object,
           return False to abort the current operation.
         * clientData - user data that will be passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addCheckFileCallback(*args, **kwargs):
        """
        addCheckFileCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message. This
        callback has the option to abort the current operation by returning
        False. The file parameter stores the target file for the current
        file IO operation, by modifying this file parameter the target file
        will be changed as well.

        Callbacks can be added to the following messages with this function:
         kBeforeImportCheck
         kBeforeOpenCheck
         kBeforeExportCheck
         kBeforeCreateReferenceCheck
         kBeforeLoadReferenceCheck

         * message - the scene message that will trigger the callback
         * function - callable which will be passed a MFileObject indicating the
           file object that will be acted on by the current file IO operation, any
           modifications to it will be passed back to Maya and change the file being
           acted on, and the clientData object.
           return False to abort the current operation.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addCheckReferenceCallback(*args, **kwargs):
        """
        addCheckReferenceCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message.
        The callback will have the ability to abort the current operation
        by returning False.

        Callbacks can be added to the following Message constant with this function:
         BeforeLoadReferenceCheck

         * message - the scene Message constant that will trigger the callback
         * function - callable which will be passed a MObject indicating the
           reference node, a MFileObject indicating the resolved file path of the
           referenced file, and the clientData object
           return False to abort the current operation
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addConnectionFailedCallback(*args, **kwargs):
        """
        addConnectionFailedCallback(function, clientData=None) -> id

        This method registers a callback that is called when a connection was
        unable to be made.
        Currently, the callback is only triggered during the reading of files (.ma or .mb)
        or of edits files (.editMA or .editMB files created by Maya's offline file support).
        The most common reasons why a connection would fail are:
        - inability to find the specified node or attribute names, or
        - a conflicting existing connection

         * function - callable which will be passed a MPlug indicating the
           source plug of the connection (or None if it could not be found),
           a MPlug indicating destination plug of the connection (or None if
           it could not be found), a string containing the name used to look up
           the source plug, a string containing the name used to look up the
           destination plug and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addReferenceCallback(*args, **kwargs):
        """
        addReferenceCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message.

        Callbacks can be added to the following messages with this function:
         kBeforeRemoveReference
         kBeforeImportReference
         kBeforeUnloadReference
         kAfterUnloadReference
         kBeforeLoadReference
         kAfterLoadReference
         kAfterCreateReference
         kAfterCreateReferenceAndRecordEdits
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReferenceAndRecordEdits

         * message - the scene Message constant that will trigger the callback
         * function - callable which will be passed a MObject indicating the
           reference node, a MFileObject indicating he resolved file path of the
           referenced file and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addStringArrayCallback(*args, **kwargs):
        """
        addStringArrayCallback(message, function, clientData=None) -> id

        Adds a new callback which takes a string array argument, in addition to
        the usual clientData.

        The Message constants which can be used with this method and the contents
        of the string array passed to their callbacks are as follows:
         kBeforePluginLoad - path to plug-in file
         kAfterPluginLoad - path to plug-in file, name of plug-in
         kBeforePluginUnload - name of plug-in
         kAfterPluginUnload - name of plug-in, path to plug-in file

                To allow for future expansion callbacks should not rely on the number
        of array elements being exactly as given above. While there will not
        be fewer elements than given above, there may in future be more.

         * message - the scene Message constant that will trigger the callback
         * function - callable which will be passed a list of strings and the
           clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    kAfterCreateReference = 45

    kAfterCreateReferenceAndRecordEdits = 50

    kAfterExport = 11

    kAfterExportReference = 21

    kAfterFileRead = 8

    kAfterImport = 4

    kAfterImportReference = 19

    kAfterLoadReference = 37

    kAfterLoadReferenceAndRecordEdits = 48

    kAfterNew = 2

    kAfterOpen = 6

    kAfterPluginLoad = 41

    kAfterPluginUnload = 43

    kAfterReference = 15

    kAfterRemoveReference = 17

    kAfterSave = 13

    kAfterSceneReadAndRecordEdits = 9

    kAfterSoftwareFrameRender = 27

    kAfterSoftwareRender = 25

    kAfterUnloadReference = 23

    kBeforeCreateReference = 44

    kBeforeCreateReferenceAndRecordEdits = 49

    kBeforeCreateReferenceCheck = 39

    kBeforeExport = 10

    kBeforeExportCheck = 35

    kBeforeExportReference = 20

    kBeforeFileRead = 7

    kBeforeImport = 3

    kBeforeImportCheck = 34

    kBeforeImportReference = 18

    kBeforeLoadReference = 36

    kBeforeLoadReferenceAndRecordEdits = 47

    kBeforeLoadReferenceCheck = 38

    kBeforeNew = 1

    kBeforeNewCheck = 31

    kBeforeOpen = 5

    kBeforeOpenCheck = 32

    kBeforePluginLoad = 40

    kBeforePluginUnload = 42

    kBeforeReference = 14

    kBeforeReferenceCheck = 39

    kBeforeRemoveReference = 16

    kBeforeSave = 12

    kBeforeSaveCheck = 33

    kBeforeSoftwareFrameRender = 26

    kBeforeSoftwareRender = 24

    kBeforeUnloadReference = 22

    kExportStarted = 46

    kLast = 51

    kMayaExiting = 30

    kMayaInitialized = 29

    kSceneUpdate = 0

    kSoftwareRenderInterrupted = 28


class MObjectSetMessage(MMessage):
    """
    Class used to register callbacks for set modified related messages.
    """

    @staticmethod
    def addSetMembersModifiedCallback(*args, **kwargs):
        """
        addSetMembersModifiedCallback(node, function, clientData=None) -> id

        Registers callbacks for set modified messages.

         * node (MObject) - the set that has triggered a setModified event
         * function (MMessage::MNodeFunction) - the callback function
         * function - callable which will be passed a MObject indicating the
           set that has triggered a setModified event and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass


class MCameraMessage(MMessage):
    """
    Class used to register callbacks for Camera Manipulation Begin and End related messages.
    """

    @staticmethod
    def addBeginManipulationCallback(*args, **kwargs):
        """
        addBeginManipulationCallback(node, function, clientData=None) -> id

        Registers callbacks for camera manipulation beginning messages.

         * node (MObject) - The node to register the callback for.
         * function (MMessage::MNodeFunction) - the callback function
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addEndManipulationCallback(*args, **kwargs):
        """
        addEndManipulationCallback(node, function, clientData=None) -> id

        Registers callbacks for camera manipulation ending messages.

         * node (MObject) - The node to register the callback for.
         * function (MMessage::MNodeFunction) - the callback function
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass


class MPxSurfaceShape(MPxNode):
    """
    Parent class of all user defined shapes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def acceptsGeometryIterator(*args, **kwargs):
        """
        acceptsGeometryIterator(component, writeable=True, forReadOnly=False) -> bool
        acceptsGeometryIterator(writeable=True) -> boolboundingBox() -> MBoundingBox

        Returns True if the shape can supply a component iterator.
        This methods should be overridden to return True. The default is to return False.

        * component (MObject) - the component to test
        * writeable (bool) - is this component type writable by an iterator
        * forReadOnly (bool) - is this component type readable by an iterator
        """
        pass

    def activeComponents(*args, **kwargs):
        """
        activeComponents() -> MObjectArray

        Returns a list of active (selected) components for the shape.
        """
        pass

    def boundingBox(*args, **kwargs):
        """
        boundingBox() -> MBoundingBox

        This method should be overridden to return a bounding box for the shape.
        If this method is overridden, then MPxSurfaceShape.isBounded() should also be overridden to return True.
        """
        pass

    def cachedShapeAttr(*args, **kwargs):
        """
        cachedShapeAttr() -> MObject

        Returns the attribute containing the shape's cached geometry, if it has one.
        """
        pass

    def canMakeLive(*args, **kwargs):
        """
        canMakeLive() -> bool

        This method is used by Maya to determine whether a surface can be made live. It can be overridden to return True if you wish to allow your surface to be made live. If you return True, you will also need to implement both closestPoint() overloads. The default is to return False.
        """
        pass

    def childChanged(*args, **kwargs):
        """
        childChanged(state=kObjectChanged) -> self

        This method can be used to trigger the shape to recalculate its bounding box.

        * state (int) - the type of change that has occurred

        Valid state:
          kObjectChanged         Object geometry changed. Internal caches need to be updated.
          kBoundingBoxChanged    Object geometry is unchanged but its bounding box has changed.
                                 This might happen if the object was moved or an offset changed.
        """
        pass

    def closestPoint(*args, **kwargs):
        """
        closestPoint(toThisPoint, theClosestPoint, tolerance=MPoint.kTolerance) -> self
        closestPoint(raySource, rayDirection, theClosestPoint, theClosestNormal, findClosestOnMiss, tolerance=MPoint.kTolerance) -> bool

        This methods are respectively used by Maya in functions (such as select) that require closest point information from your surface and for snapping queries when your surface is live.

        For selection:
        If you've overridden canMakeLive() to return True, this method is also used by Maya for some snapping queries when your surface is live.

        * toThisPoint (MPoint) - the point to test against.
        * theClosestPoint [OUT] (MPoint) - the closest point on your surface.
        * tolerance (float) - tolerance to use in your calculations.


        For snapping:
        If you override this method, you should set theClosestPoint to the closest point on your surface intersected by the ray defined by raySource and rayDirection. You should also populate the theClosestNormal parameter with the surface normal at that intersection point.

        If no intersection is found and findClosestOnMiss is True, you should still provide a point on your surface closest to the ray defined by raySource and rayDirection. When used for live snapping, this allows the user to click and drag outside the bounds    of a live surface and still have it snap to the nearest point on it within the viewport. Note, performing a pure 3D closest point of approach test in this situation may not give the most natural result for live mesh snapping.
        To provide behavior that matches Maya, you can project your surface onto the plane defined by the ray, then perform your calculations. This will account for view perspective and give accurate live snap points along the silhouette of the surface.

        If findClosestOnMiss is False, you should not provide a point and normal when the ray misses.
        Should return True if theClosestPoint and theClosestNormal have been set, False otherwise.
        canMakeLive() must also be overridden to return True.

        * raySource (MPoint) - the origin of the ray to test against
        * rayDirection (MVector) - the direction of the ray to test against
        * theClosestPoint [OUT] (MPoint) - the closest point on your surface
        * theClosestNormal [OUT] (MVector) - the normal at the closest point on your surface
        * findClosestOnMiss (bool) - when True, you should calculate theClosestPoint and theClosestNormal even if the ray misses your surface.
        * tolerance (float) - tolerance to use in your calculations
        """
        pass

    def componentToPlugs(*args, **kwargs):
        """
        componentToPlugs(component, selectionList) -> self

        Converts the given component into a selection list of plugs.
        This method is used to associate a shapes components into the corresponding attributes (plugs) within the shape. For example, it gets called by the translate manipulator to determine which attributes should be driven by the manipulator, and by the setKeyframe command to determine where to connect animCurves for components.

        This method should be overridden if the shape supports components that can be selected and moved in Maya.

        * component (MObject) - the component to be converted
        * list (MSelectionList) - a selection list where the plug should be added
        """
        pass

    def convertToTweakNodePlug(*args, **kwargs):
        """
        convertToTweakNodePlug(plug) -> bool

        Check if a tweak node is connected to this node. If it is, then reset the supplied plug to contain the controlPoints attribute on the tweak node.
        Returns True if a tweak node was found, False if the plug was unchanged

        * plug (MPlug) - plug which will be set to point to the associated tweak node plug if a tweak node is connected
        """
        pass

    def createFullRenderGroup(*args, **kwargs):
        """
        createFullRenderGroup() -> MObject

        Returns a component containing all of renderable elements in the shape.
        This method is used to create a component containing every renderable element in the object.

        This method is supposed to return non-null object only if the dag object contains renderable components. Type of the return component should is the same as the one returned by MPxSurfaceShape::renderGroupComponentType().
        """
        pass

    def createFullVertexGroup(*args, **kwargs):
        """
        createFullVertexGroup() -> MObject

        Returns a component containing all of the vertices in the shape.
        This method is used to create a component containing every vertex/CV in the object.

        This method is supposed to return non-null object only if the dag object contains vertices/CVs (control points), so derived classes that do should override this method.
        """
        pass

    def deleteComponents(*args, **kwargs):
        """
        deleteComponents(componentList, undoInfo) -> bool

        Returns True if this method was successful, False otherwise.
        This method should be overridden if the shape is to support deletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component can be stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.

        * componentList (MObjectArray) - List of components to be deleted
        * undoInfo (MDoubleArray) - Values used for undo purposes
        """
        pass

    def excludeAsPluginShape(*args, **kwargs):
        """
        excludeAsPluginShape() -> bool

        A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape. By overriding excludeAsPluginShape() to return False, you can change that behaviour so that this shape is still displayed even when the display of "Plugin Shapes" is disabled.
        The default implementation returns True.
        Returns True to have this shape obey the "Plugin Shapes" settings in the viewport's "Show" menu; False to have it ignore that setting.
        """
        pass

    def geometryData(*args, **kwargs):
        """
        geometryData() -> MObject

        Returns the geometry data of the shape. The geometry data must be derived from the MPxGeometryData class.

        The data is used by Maya to add, edit and query component grouping (set) information for the shape. This set information is stored and managed by Maya's shape base class, geometryShape.
        """
        pass

    def geometryIteratorSetup(*args, **kwargs):
        """
        geometryIteratorSetup(componentList, components, forReadOnly=False) -> MPxGeometryIterator

        This method should be overridden by the user to return a geometry iterator compatible with the user's geometry.
        A geometry iterator is used for iterating over the components of a shape, such as the vertices of a mesh, in a generic manner.

        The components to be iterated over are passed to this function in on of two ways, as a list of components, or as a single component.
        Only one of these arguments is used at any particular time.

        * componentList (MObjectArray) - a list of components to be iterated over
        * components (MObject) - the components to be iterated over
        * forReadOnly (bool) - specifies whether the iterator is for read-only
        """
        pass

    def getComponentSelectionMask(*args, **kwargs):
        """
        getComponentSelectionMask() -> MSelectionMask

        Returns the selection mask of the shape.
        This routine must be overridden if the shape is to support interactive component selection in Viewport 2.0 and should provide information about the selection mask of the shape component.
        """
        pass

    def getShapeSelectionMask(*args, **kwargs):
        """
        getShapeSelectionMask() -> MSelectionMask

        Returns the selection mask of the shape.
        This routine must be overridden if the shape is to support interactive object selection in Viewport 2.0 and should provide information about the selection mask of the shape.
        """
        pass

    def getWorldMatrix(*args, **kwargs):
        """
        getWorldMatrix(block, instanceGeom) -> MMatrix

        Returns MMatrix which takes a point from local object space to world space.

        * block (MDataBlock) - a MDataBlock
        * instanceGeom (int) - the instance this MPxSurfaceShape corresponds to
        """
        pass

    def hasActiveComponents(*args, **kwargs):
        """
        hasActiveComponents() -> bool

        This method is used to determine whether or not the shape has active (selected) components.
        """
        pass

    def isBounded(*args, **kwargs):
        """
        isBounded() -> bool

        This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient.
        Returns a boolean value indicating whether a bounding box routine has been supplied
        """
        pass

    def localShapeInAttr(*args, **kwargs):
        """
        localShapeInAttr() -> MObject

        Returns the attribute containing the shape's input geometry in local space.

        This method will be called by Maya to determine if the shape has construction history and must be overridden if the shape is to support deformers.
        """
        pass

    def localShapeOutAttr(*args, **kwargs):
        """
        localShapeOutAttr() -> MObject

        Returns the attribute containing the shape's output geometry in local space.

        This method must be overridden if the shape is to support deformers.
        """
        pass

    def match(*args, **kwargs):
        """
        match(mask, componentList) -> bool

        This method is used to check for matches between a selection type (or mask) and a given component. If your shape has components representing attributes then this method is used to match up your components with selection masks.

        This is used by sets and deformers to make sure that the selected components fall into the "vertex only" category. This is useful when you want to make sure that only a particular component can be deformed.

        * mask (MSelectionMask) - the selection mask to test against
        * componentList (MObjectArray) - a list of components to be tested
        """
        pass

    def matchComponent(*args, **kwargs):
        """
        matchComponent(item, spec, list) -> int

        This method is used to convert the string representation of a component into a component object and to validate that the indices.

        This method should be overridden if the shape has components.

        * item (MSelectionList) - DAG selection item for the object being matched
        * spec (MAttributeSpecArray) - attribute specification object
        * list (MSelectionList) - list to add components to

        List of valid component match result:
          kMatchOk                       The component was matched without error.
          kMatchNone                     No component was matched.
          kMatchTooMany                  Not used.
          kMatchInvalidName              One of the names in the attribute specification was not valid.
          kMatchInvalidAttribute         Not used.
          kMatchInvalidAttributeIndex    The attribute specification contained an index for a non-array attribute.
          kMatchInvalidAttributeRange    An attribute index was out of range.
          kMatchInvalidAttributeDim      The attribute specification provided the wrong number of dimensions for an attribute.
        """
        pass

    def newControlPointComponent(*args, **kwargs):
        """
        newControlPointComponent() -> MObject

        The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent) in order to support rigid skinning binds.

        This method can be overridden to support other types of components such as MFnDoubleIndexedComponent and MFnTripleIndexedComponent      and should return a new component of that type.  The types allowed are those listed in the create() method docs for each MFn*IndexedComponent.
        """
        pass

    def pointAtParm(*args, **kwargs):
        """
        pointAtParm(atThisParm, evaluatedPoint) -> bool

        This method is used by Maya in functions (such as select) that require point at parameter values. This only makes sense for parametric surfaces such as NURBS.
        Returns True if a point was found, False otherwise

        * atThisParm (MPoint) - the parameter to check
        * evaluatedPoint [OUT] (MPoint) - the surface point
        """
        pass

    def renderGroupComponentType(*args, **kwargs):
        """
        renderGroupComponentType() -> int

        This method is used to return the type of renderable components for this shape. It should return a type among MFn::kMeshPolygonComponent, MFn::kSubdivFaceComponent and MFn::kSurfaceFaceComponent, which is used in the creation of per-face/patch shader assignment.

        Returns the type of renderable components for this shape.
        See MFnSet.addMember()
        """
        pass

    def transformUsing(*args, **kwargs):
        """
        transformUsing(matrix, componentList, cachingMode=None, pointCache=None) -> self

        Transform the given components using the specified transformation matrix.
        This method should be overridden if the shape supports components that can be transformed using maya's move, scale, and rotate tools.

        * matrix (MMatrix) - the matrix representing the transformation that is to be applied to the components
        * componentList (MObjectArray) - a list of components to be transformed. If the list is empty, it indicates that every point in the geometry should be transformed.
        * cachingMode (int) - whether the points should be cached in the pointCache argument, or restored from the pointCache
        * pointCache (MPointArray) - used to store for undo and restore points during undo

        List of valid caching modes:
          kNoPointCaching             No point caching.
          kSavePoints                 Points should be saved for undo in the point cache.
          kRestorePoints              Points should be restored from the point cache.
          kUpdatePoints               Transform and update the points in the point cache.
          kTransformOriginalPoints    Transform using use the original pre-transformation values stored in the pointCache.
        """
        pass

    def tweakUsing(*args, **kwargs):
        """
        tweakUsing(matrix, componentList, cachingMode, pointCache, handle) -> self

        Transform the given components using the specified transformation matrix.
        This method should be overridden if the shape supports components that can be transformed using maya's move, scale, and rotate tools. This method is called when the shape has history & connected to a tweak node. The most common reason why the shape would be connected to a tweak node is if it is being deformed. When a shape is connected to a tweak node, transformations applied to the points are placed in the tweak node rather than in the shape itself.

        * matrix (MMatrix) - the matrix representing the transformation that is to be applied to the components
        * componentList (MObjectArray) - a list of components to be tranformed. If the list is empty, it indicates that every point in the geometry should be transformed.
        * cachingMode (int) - whether the points should be cached in the pointCache argument, or restored from the pointCache
        * pointCache (MPointArray) - used to store for undo and restore points during undo
        * handle (MArrayDataHandle) - array data handle where the tweaks are stored

        See transformUsing() for a list of valid caching mode
        """
        pass

    def undeleteComponents(*args, **kwargs):
        """
        undeleteComponents(componentList, undoInfo) -> bool

        This method should be overridden if the shape is to support undeletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component is stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.
        Returns True if this method was successful, False otherwise

        * componentList (MObjectArray) - List of components that were deleted
        * undoInfo (MDoubleArray) - Values used for undo purposes
        """
        pass

    def vertexOffsetDirection(*args, **kwargs):
        """
        vertexOffsetDirection(component, direction, mode, normalize) -> bool

        This method should be overridden if the shape supports components that can be moved in the direction of the normal or UV's using the move vertex normal tool.

        This method should calculate the offset direction for a vertex components. The direction vector array is an array of offsets corresponding to the elements in the component. The mode argument specifies the type of movement that is being performed.

        The default for this method is to return False, i.e. no support for move normal tool.
        Returns True if the shape supports the current mode, False if the shape cannot do the requested vertex move

        * component (MObject)
        * direction (MVectorArray)
        * mode (int) - The type of vertex movement
        * normalize (bool) - specifies whether the offset vectors should be normalized

        List of valid types:
          kNormal       Move in normal direction.
          kUTangent     Move in u tangent direction.
          kVTangent     Move in v tangent direction.
          kUVNTriad     Calculate u, v, and normal offsets.
        """
        pass

    def weightedTransformUsing(*args, **kwargs):
        """
        weightedTransformUsing(xform, space, componentList, cachingMode, pointCache, freezePlane) -> self

        Transform the given components with interpolation using the specified transformation matrix.

        If not overridden, then a default implementation will be used to perform the transformation and interpolation.
        The default implementation calls setPoint() for each transformed point.

        * xform (MTransformationMatrix) - the matrix representing the transformation that is to be applied to the components.
        * space (MMatrix) - the matrix representing the transformation space to perform the interpolated transformation. A value of None indicates it should be ignored.
        * componentList (MObjectArray) - a list of components to be transformed and their weights. This list will not be empty.* cachingMode (int) - whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using use the original values in the pointCache.
        * pointCache (MPointArray) - used to store for undo and restore points during undo
        * freezePlane (MPlane) - used for symmetric transformation of components. A value of None indicates it is not used and there is no symmetric transformation.

        See transformUsing() for a list of valid caching mode
        """
        pass

    def weightedTweakUsing(*args, **kwargs):
        """
        weightedTweakUsing(xform, space, componentList, cachingMode, pointCache, freezePlane, handle) -> self

        Transform the given components with interpolation using the specified transformation matrix.
        This method is called for transforming components using maya's move, scale, and rotate tools when the shape has history and is connected to a tweak node. The most common reason why the shape would be connected to a tweak node is if it is being deformed. When a shape is connected to a tweak node, transformations applied to the points are placed in the tweak node rather than in the shape itself.

        If not overridden, then a default implementation will be used to perform the transformation and interpolation.
        The default implementation calls setPoint() for each transformed point.

        * xform (MTransformationMatrix) - the matrix representing the transformation that is to be applied to the components
        * space (MMatrix) - the matrix representing the transformation space to perform the interpolated transformation. A value of None indicates it should be ignored.
        * componentList (MObjectArray) - a list of components to be transformed and their weights. This list will not be empty.
        * cachingMode (int) - whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using the original values in the pointCache.
        * pointCache (MPointArray) - used to store for undo and restore points during undo
        * freezePlane (MPlane) - used for symmetric transformation of components. A value of None indicates it is not used and there is no symmetric transformation.
        * handle (MArrayDataHandle) - array data handle where the tweaks are stored

        See transformUsing() for a list of valid caching mode
        """
        pass

    def worldShapeOutAttr(*args, **kwargs):
        """
        worldShapeOutAttr() -> MObject

        Returns the attribute containing the shape's output geometry in world space.

        This method must be overridden if the shape is to support deformers.
        """
        pass

    boundingBoxCenterX = None

    boundingBoxCenterY = None

    boundingBoxCenterZ = None

    center = None

    instObjGroups = None

    intermediateObject = None

    inverseMatrix = None

    isRenderable = None

    isTemplated = None

    kBoundingBoxChanged = 1

    kMatchInvalidAttribute = 4

    kMatchInvalidAttributeDim = 7

    kMatchInvalidAttributeIndex = 5

    kMatchInvalidAttributeRange = 6

    kMatchInvalidName = 3

    kMatchNone = 1

    kMatchOk = 0

    kMatchTooMany = 2

    kNoPointCaching = 0

    kNormal = 0

    kObjectChanged = 0

    kRestorePoints = 2

    kSavePoints = 1

    kTransformOriginalPoints = 4

    kUTangent = 1

    kUVNTriad = 3

    kUpdatePoints = 3

    kVTangent = 2

    mControlPoints = None

    mControlValueX = None

    mControlValueY = None

    mControlValueZ = None

    mHasHistoryOnCreate = None

    matrix = None

    nodeBoundingBox = None

    nodeBoundingBoxMax = None

    nodeBoundingBoxMaxX = None

    nodeBoundingBoxMaxZ = None

    nodeBoundingBoxMin = None

    nodeBoundingBoxMinX = None

    nodeBoundingBoxMinY = None

    nodeBoundingBoxMinZ = None

    nodeBoundingBoxSize = None

    nodeBoundingBoxSizeX = None

    nodeBoundingBoxSizeY = None

    nodeBoundingBoxSizeZ = None

    objectColor = None

    objectGroupColor = None

    objectGroupId = None

    objectGroups = None

    objectGrpCompList = None

    parentInverseMatrix = None

    parentMatrix = None

    useObjectColor = None

    visibility = None

    worldInverseMatrix = None

    worldMatrix = None


class MCommandMessage(MMessage):
    """
    Class used to register callbacks for command related messages.

    The class also provides the following MessageType constants which
    describe the different types of output messages:
      kHistory              #Command history
      kDisplay              #String to display unmodified
      kInfo         #General information
      kWarning              #Warning message
      kError                #Error message
      kResult               #Result from a command execution in the command window
      kStackTrace   #Stack trace
    """

    @staticmethod
    def addCommandCallback(*args, **kwargs):
        """
        addCommandCallback(function, clientData=None) -> id

        This method registers a callback for command messages that are
        issued every time a MEL command is executed. It is only called
        when actual commands are executed and not when scripts are
        executed.

        NOTE: Setting up a callback using this method will
        degrade the performance of Maya since the installed callback will be
        invoked repeatedly as MEL operations are processed.

         * function - callable which will be passed a string containing the
           MEL command being executed, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addCommandOutputCallback(*args, **kwargs):
        """
        addCommandOutputCallback(function, clientData=None) -> id

        This method registers a callback for whenever commands generate
        output such as that which is printed into the command window.

         * function - callable which will be passed a string containing the
           MEL command being executed, a MessageType constant (see class docs
           for a list) indicating the message type and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addCommandOutputFilterCallback(*args, **kwargs):
        """
        addCommandOutputFilterCallback(function, clientData=None) -> id

        This method registers a callback for whenever commands generate
        output such as that which is printed into the command window.

        Returning True in the callback will filter the output from the
        script editor and command line., returning False will keep the output.

         * function - callable which will be passed a string containing the
           MEL command being executed, a MessageType constant (see class docs
           for a list) indicating the message type and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addProcCallback(*args, **kwargs):
        """
        addProcCallback(function, clientData=None) -> id

        This method registers a callback that is executed every time a MEL
        procedure is run. The callback will be executed once when the procedure
        is about to be executed, and again when it has exited. If a non-existent
        procedure is called the callback will be called once for entry but there
        will be no call on exit.

        The callback cannot be registered multiple times. To register a new
        callback function for this, please de-register the original callback first

        NOTE: Setting up a callback using this method can potentially degrade the
        performance of Maya since the installed callback will be invoked
        repeatedly as MEL procedures are executed.

         * function - callable which will be passed a string containing the name
           of the procedure being invoked, an integer indicating the ID for the
           procedure's invocation, a bool set to True if the procedure is being entered,
           false otherwise, a ProcType constant (see below for a list) indicating the
           type of call this is (MEL proc or MEL command), and the clientData object
           ProcType constant can take the folowing values:
             kMELProc
             kMELCommand
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    kDisplay = 1

    kError = 4

    kHistory = 0

    kInfo = 2

    kMELCommand = 1

    kMELProc = 0

    kResult = 5

    kStackTrace = 6

    kWarning = 3


class MTimerMessage(MMessage):
    """
    Class used to register callbacks for timer related messages.
    """

    @staticmethod
    def addTimerCallback(*args, **kwargs):
        """
        addTimerCallback(period, function, clientData=None) -> id

        This method registers a callback which is called repeatedly with a
        specified period of time between calls. Each time the timer fires the
        callback will be placed on the idle queue for execution in the next
        idle cycle. If the timer fires again, before the previous invocation
        has completed execution, the new firing will be skipped.

        If the execution time of the callback exceeds half of its period then
        the next timeout will be skipped to give Maya time to process other tasks.

        The maximum resolution for this callback is about 1ms.  The response
        is, however, not guaranteed because while multitasking, the OS may
        delay for an unspecified length of time before returning control to
        Maya.

         * period (float) - the period at which the callback will be
        executed (Measured in seconds)
         * function - callable which will be passed a float indicating
           the elapsed time since this function was last called, a float
           indicating the execution time of this function the last time
           it was called, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass


class MConditionMessage(MMessage):
    """
    Class used to register callbacks for condition related messages.
    """

    @staticmethod
    def addConditionCallback(*args, **kwargs):
        """
        addConditionCallback(conditionName, function, clientData=None) -> id

        This method registers a callback for condition changed messages.
        The callback function will be passed the new state of the
        condition and any client data that the user wishes to pass in.

         * conditionName (string) - the condition to register the
        callback for
         * function - callable which will be passed a bool indicating
           the new state of the condition, and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def getConditionNames(*args, **kwargs):
        """
        getConditionNames() -> (string, string, ...)

        This method returns the list of available condition names.

         * return: tuple of available condition names.
        """
        pass

    @staticmethod
    def getConditionState(*args, **kwargs):
        """
        getConditionState(name) -> bool

        This method returns the current state of a condition.

         * name (string) - the name of the condition.


         * return: The current state of the condition.
        """
        pass


class MUserEventMessage(MMessage):
    """
    Class used to register callbacks for user event messages.
    """

    @staticmethod
    def addUserEventCallback(*args, **kwargs):
        """
        addUserEventCallback(eventName, function, clientData=None) -> id

        This method registers a callback for user-defined messages.

        The parameter clientData will be passed to callbacks registered for this
        event whenever the event is triggered.  To override the data that is passed
        to the callback whenever the event is posted, you can supply a clientData
        pointer to postUserEvent()..

         * eventName (string) - the event name to register the callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def deregisterUserEvent(*args, **kwargs):
        """
        deregisterUserEvent(eventName)

        Removes the event type with the given event name.  If callbacks have been
        registered with this event type, they will become invalid after a
        successful call to this method.

         * eventName (string) - the name of the new event to deregister.
        """
        pass

    @staticmethod
    def isUserEvent(*args, **kwargs):
        """
        isUserEvent(eventName) -> bool

        Checks if an event type exists with the given event name.

         * eventName (string) - the name of the new event to check.
        """
        pass

    @staticmethod
    def postUserEvent(*args, **kwargs):
        """
        postUserEvent(eventName, clientData=None)

        Notifies all callbacks attached to the given event type of the occurence
        of the event.

        If clientData is specified, this data will be passed to all callbacks that
        receive the event.  If clientData is None (the default), the clientData
        registered with addUserEventCallback will be passed to the callbacks.


         * eventName (string) - the name of the new event.
         * clientData - User defined data.
        """
        pass

    @staticmethod
    def registerUserEvent(*args, **kwargs):
        """
        registerUserEvent(eventName)

        Adds a new event type with the given string identifier.  The string
        identifier can then be used in all other MUserEventMessage methods to operate
        on the new event type.

         * eventName (string) - the name of the new event to register.  Any
           non-empty string may be used as an event name.
        """
        pass


class MContainerMessage(MMessage):
    """
    Class used to register callbacks for container related messages.
    """

    @staticmethod
    def addBoundAttrCallback(*args, **kwargs):
        """
        addBoundAttrCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an attribute
        is bound or unbound on a container.

         * function - callable which will be passed a Node (the container)
           ,a string indicating the name of the bound attr, and
           the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass

    @staticmethod
    def addPublishAttrCallback(*args, **kwargs):
        """
        addPublishAttrCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an attribute
        is published or unpublished from a container.

         * function - callable which will be passed a Node (the container)
           ,a string indicating the name of the published attr, and
           the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
        pass


# noinspection PyProtectedMember,PyUnresolvedReferences
class MFnDependencyNode(MFnBase):
    """
    Function set for operating on dependency nodes.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)
        self._fn_type = MFn.kDependencyNode

    def absoluteName(*args, **kwargs):
        """
        Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).
        """
        pass

    def addAttribute(self, attribute: 'MObject') -> 'MFnDependencyNode':
        """
        Adds a new dynamic attribute to the node.
        """

        assert attribute._alive is True, 'Attribute MObject must be valid to be added to a node.'
        attribute._dynamic = True
        attribute._owner = self._mobject
        dict_key = _get_attribute_id(f'{self._mobject._name}.{attribute._long_name}')
        self._mobject._attributes[dict_key] = attribute

        # For compound attrs, add the children in the map as well
        for child in attribute._children:
            self._mobject._attributes[_get_attribute_id(f'{self._mobject._name}.{child._long_name}')] = child

        return self

    def addExternalContentForFileAttr(*args, **kwargs):
        """
        Adds content info to the specified table from a file path attribute.
        """
        pass

    def affectsAnimation(*args, **kwargs):
        """
        Returns true if the changes to the node may affect animation.
        """
        pass

    def attribute(self, attr_name: str) -> 'MObject':
        """
        Returns an attribute of the node, given either its index or name.
        """
        try:
            mplug = self.findPlug(attr_name, False)
            if not mplug or mplug.attribute().isNull():
                raise KeyError
            return mplug._attribute

        except KeyError as k_err:
            raise KeyError(f'Node Type: <{self._mobject._name}> does not have attribute <{attr_name}>.')

    def attributeClass(*args, **kwargs):
        """
        Returns the class of the specified attribute.
        """
        pass

    def attributeCount(*args, **kwargs):
        """
        Returns the number of attributes on the node.
        """
        pass

    def canBeWritten(*args, **kwargs):
        """
        Returns true if the node will be written to file.
        """
        pass

    def create(self, type_id: Union["MTypeId", str], name: str = None) -> MObject:
        """
        Creates a new node of the given type.
        """
        mobject = MObject()
        # If given a string as input, get the matching MTypeId
        if isinstance(type_id, str):
            # noinspection PyProtectedMember
            mobject._typeId = _TYPE_STR_TO_ID[type_id]
            name = name if name else f'{type_id}1'
            type_str = type_id
        else:
            mobject._typeId = type_id
            type_str = _TYPE_INT_TO_STR[type_id.id()]
            name = name if name else f'{type_str}1'

        # Add kDependencyNode in list of types and then the actual node type
        mobject._api_type = [MFn.kBase, MFn.kNamedObject, MFn.kDependencyNode]
        mobject._api_type.append(getattr(MFn, f'k{type_str[0].upper()}{type_str[1:]}'))

        # Build name
        mobject._name = hierarchy.find_first_available_name(name)

        # Set valid flag
        self._mobject = mobject
        mobject._alive = True

        hierarchy.register(mobject)

        return self._mobject

    def dgCallbackIds(*args, **kwargs):
        """
        Returns DG timing information for a specific callback type, broken down by callbackId.
        """
        pass

    def dgCallbacks(*args, **kwargs):
        """
        Returns DG timing information broken down by callback type.
        """
        pass

    def dgTimer(*args, **kwargs):
        """
        Returns a specific DG timer metric for a given timer type.
        """
        pass

    def dgTimerOff(*args, **kwargs):
        """
        Turns DG timing off for this node.
        """
        pass

    def dgTimerOn(*args, **kwargs):
        """
        Turns DG timing on for this node.
        """
        pass

    def dgTimerQueryState(*args, **kwargs):
        """
        Returns the current DG timer state for this node.
        """
        pass

    def dgTimerReset(*args, **kwargs):
        """
        Resets all DG timers for this node.
        """
        pass

    def findAlias(*args, **kwargs):
        """
        Returns the attribute which has the given alias.
        """
        pass

    def findPlug(self, attr_name: str, want_network_plug):
        """
        Returns a plug for the given attribute.
        """

        # See if the attribute and/or the plug are already cached
        attribute_id = _get_attribute_id(f'{self._mobject._name}.{attr_name}')
        attribute = self._mobject._attributes.get(attribute_id)
        mplug = self._mobject._cached_plugs.get(attribute_id)

        # Fast return if both attr and mplug are cached
        if attribute and mplug:
            if mplug._attribute == attribute:
                return mplug

        # If only the plug is not cached, initialize a new one
        elif attribute and not mplug:
            return _initialize_mplug(self._mobject,
                                     MPlug(),
                                     attribute,
                                     attribute_id,
                                     want_network_plug=want_network_plug)

        # Else, assume it's the first time the attribute is being accessed
        mplug = MPlug()
        mplug._owner = self._mobject
        attribute = _initialize_attribute(attribute or MObject())

        # Try to find attribute in list of known attributes based on the node type
        node_type = _get_node_type(self._mobject)
        properties, long_name, short_name = _get_attribute_properties(node_type, attr_name)

        attribute_name = f'{self._mobject._name}.{long_name}'
        attribute_id = _get_attribute_id(attribute_name)
        mplug_id = attribute_id

        # Try to find the mplug in the list of cached plugs. Just in case it was given the short name
        cached_plug = self._mobject._cached_plugs.get(mplug_id)
        if cached_plug:
            return cached_plug

        # Initialize the mplug and attribute
        mplug._uuid = mplug_id
        attribute._uuid = attribute_id
        attribute._name = attribute_name
        attribute._long_name = long_name
        attribute._short_name = short_name
        mplug._network_plug = want_network_plug


        # Fill-in maya native attributes based on dict info
        if properties:
            attribute._is_array = properties['is_array']
            attribute._is_compound = properties['is_compound']
            attribute._is_element = properties['is_element']

            # Add type constant based on the type str
            attr_type = getattr(MFn, properties['type_str'])
            if attr_type not in attribute._api_type:
                attribute._api_type.append(attr_type)

            # Only for numeric attributes
            if properties.get('numeric_type'):
                attribute._numeric_type = properties['numeric_type']

            # Only for compound attributes
            if properties.get('children'):
                mplug._children_plug_names = properties['children']

        # Update the plugs & attrs cache
        self._mobject._cached_plugs[mplug._uuid] = mplug
        self._mobject._attributes[attribute._uuid] = attribute

        # Flag the attribute as a valid MObject and set it as the attribute of the mplug
        attribute._alive = True
        mplug._attribute = attribute

        return mplug

    def getAffectedAttributes(*args, **kwargs):
        """
        Returns all of the attributes which are affected by the specified attribute.
        """
        pass

    def getAffectingAttributes(*args, **kwargs):
        """
        Returns all of the attributes which affect the specified attribute.
        """
        pass

    def getAliasAttr(*args, **kwargs):
        """
        Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases.
        """
        pass

    def getAliasList(*args, **kwargs):
        """
        Returns all of the node's attribute aliases.
        """
        pass

    def getConnections(*args, **kwargs):
        """
        Returns all the plugs which are connected to attributes of this node.
        """
        pass

    def getExternalContent(*args, **kwargs):
        """
        Gets the external content (files) that this node depends on.
        """
        pass

    def hasAttribute(self, attribute_name: str) -> bool:
        """
        Returns True if the node has an attribute with the given name.
        """
        return True if self.attribute(attribute_name) else False

    def uniqueName(self):
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root
        namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name.
        """
        return self._mobject._name

    def hasUniqueName(*args, **kwargs):
        """
        Returns True if the node's name is unique.
        """
        pass

    def isFlagSet(*args, **kwargs):
        """
        Returns the state of the specified node flag.
        """
        pass

    def isNewAttribute(*args, **kwargs):
        """
        Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files.
        """
        pass

    def isTrackingEdits(*args, **kwargs):
        """
        Returns True if the node is referenced or in an assembly that is tracking edits.
        """
        pass

    def name(self) -> str:
        """
        Returns the node's name.
        """
        return self._mobject._name

    def plugsAlias(*args, **kwargs):
        """
        Returns the alias for a plug's attribute.
        """
        pass

    def removeAttribute(*args, **kwargs):
        """
        Removes a dynamic attribute from the node.
        """
        pass

    def reorderedAttribute(*args, **kwargs):
        """
        Returns one of the node's attribute, based on the order in which they are written to file.
        """
        pass

    def setAffectsAnimation(*args, **kwargs):
        """
        Specifies that modifications to a node could potentially affect the animation.
        """
        pass

    def setAlias(*args, **kwargs):
        """
        Adds or removes an attribute alias.
        """
        pass

    def setDoNotWrite(*args, **kwargs):
        """
        Used to prevent the node from being written to file.
        """
        pass

    def setExternalContent(*args, **kwargs):
        """
        Changes the location of external content.
        """
        pass

    def setExternalContentForFileAttr(*args, **kwargs):
        """
        Sets content info in the specified attribute from the table.
        """
        pass

    def setFlag(*args, **kwargs):
        """
        Sets the state of the specified node flag.
        """
        pass

    def setName(*args, **kwargs):
        """
        Sets the node's name.
        """
        pass

    def setUuid(*args, **kwargs):
        """
        Sets the node's UUID.
        """
        pass

    def userNode(*args, **kwargs):
        """
        Returns the MPxNode object for a plugin node.
        """
        pass

    def uuid(self) -> MUuid:
        """
        Returns the node's UUID.
        """
        return self._mobject._uuid

    @staticmethod
    def allocateFlag(*args, **kwargs):
        """
        Allocates a flag on all nodes for use by the named plugin and returns the flag's index.
        """
        pass

    @staticmethod
    def classification(*args, **kwargs):
        """
        Returns the classification string for the named node type.
        """
        pass

    @staticmethod
    def deallocateAllFlags(*args, **kwargs):
        """
        Deallocates all node flags which are currently allocated to the named plugin.
        """
        pass

    @staticmethod
    def deallocateFlag(*args, **kwargs):
        """
        Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag().
        """
        pass

    isDefaultNode = None

    isFromReferencedFile = None

    isLocked = None

    isShared = None

    kExtensionAttr = 3

    kInvalidAttr = 4

    kLocalDynamicAttr = 1

    kNormalAttr = 2

    kTimerInvalidState = 3

    kTimerMetric_callback = 0

    kTimerMetric_callbackNotViaAPI = 6

    kTimerMetric_callbackViaAPI = 5

    kTimerMetric_compute = 1

    kTimerMetric_computeDuringCallback = 7

    kTimerMetric_computeNotDuringCallback = 8

    kTimerMetric_dirty = 2

    kTimerMetric_draw = 3

    kTimerMetric_fetch = 4

    kTimerMetrics = 9

    kTimerOff = 0

    kTimerOn = 1

    kTimerType_count = 2

    kTimerType_inclusive = 1

    kTimerType_self = 0

    kTimerTypes = 3

    kTimerUninitialized = 2

    namespace = None

    pluginName = None

    @property
    def typeId(self):
        return self._mobject._typeId

    @property
    def typeName(self):
        try:
            return _TYPE_INT_TO_STR[self._mobject._typeId.id()]
        except AttributeError:
            if not self._mobject:
                raise RuntimeError('No MObject associated with this function set. Enusure the MObject has been created'
                                   'first before adding it to the function set.')
            if not self._mobject._alive:
                raise RuntimeError(f'MObject: {self._mobject._name} does not exist yet. Cannot return type.')


class MDagModifier(MDGModifier):
    """
    Used to change the structure of the DAG
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)

    def createNode(self, type_id: Union[str, NODE_TYPES, 'MObject'], parent: Optional['MObject'] = None):
        """
        createNode(typeName, parent=MObject.kNullObj) -> new DAG node MObject
        createNode(typeId,   parent=MObject.kNullObj) -> new DAG node MObject

        Adds an operation to the modifier to create a DAG node of the specified
        type. If a parent DAG node is provided the new node will be parented
        under it. If no parent is provided and the new DAG node is a transform
        type then it will be parented under the world. In both of these cases
        the method returns the new DAG node.

        If no parent is provided and the new DAG node is not a transform type
        then a transform node will be created and the child parented under that. The new transform will be parented under the world and it is the
        transform node which will be returned by the method, not the child.

        None of the newly created nodes will be added to the DAG until the
        modifier's doIt() method is called.
        """
        mobject = super().createNode(type_id)
        self._queue.pop(-1)

        if not parent:
            parent = WORLD
        mobject._parent = parent
        parent._children.add(mobject)

        self._queue.append(('create', mobject))
        return mobject

    def reparentNode(self, node: 'MObject', new_parent: 'MObject' = None):
        """
        reparentNode(MObject node, newParent=MObject.kNullObj) -> self

        Adds an operation to the modifier to reparent a DAG node under a
        specified parent.

        If no parent is provided then the DAG node will be reparented under the
        world, so long as it is a transform type. If it is not a transform type
        then the doIt() will raise a RuntimeError.
        """

        if not new_parent:
            new_parent = MObject().kNullObj
        self._queue.append(('reparent', node, new_parent, node._parent))

        return self


class MFnData(MFnBase):
    """
    Base class for dependency graph data function sets.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    kAny = 24

    kComponentList = 13

    kDoubleArray = 7

    kDynArrayAttrs = 19

    kDynSweptGeometry = 20

    kFloatArray = 8

    kIntArray = 9

    kInvalid = 0

    kLast = 25

    kLattice = 15

    kMatrix = 5

    kMatrixArray = 12

    kMesh = 14

    kNId = 23

    kNObject = 22

    kNumeric = 1

    kNurbsCurve = 16

    kNurbsSurface = 17

    kPlugin = 2

    kPluginGeometry = 3

    kPointArray = 10

    kSphere = 18

    kString = 4

    kStringArray = 6

    kSubdSurface = 21

    kVectorArray = 11


class MFnNumericAttribute(MFnAttribute):
    """
    Functionset for creating and working with numeric attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)

    def child(self, index: int) -> 'MObject':
        """
        Returns the specified child attribute of the parent attribute currently attached to the function set.
        """
        return self._mobject._children[index]

    def create(self, long_name: str, short_name: str, numeric_type: int, default_value: float=0) -> 'MObject':
        """Creates a new simple or compound numeric attribute, attaches it to the function set and returns it in an MObject.

        You will have to provide a "numeric type constant" to specify the type of numeric attribute you want to create. You will find
        the values of those constants on the MFnNumericData class.

        Args:
            long_name (str): Attr long name.
            short_name (str): Attr short name.
            numeric_type (int): MFnNumericData type constant.
            default_value (float, optional): The default value of the attr upon being generated. Defaults to 0.

        Returns:
            MObject: Numeric Attribute MObject.
        """

        super()._create(long_name=long_name, short_name=short_name)

        # Initialize numeric fields
        self._mobject._init_numeric_fields()

        self._mobject._api_type.append(MFn.kNumericAttribute)
        self._mobject._numeric_type = numeric_type

        self._mobject._value = default_value
        self._mobject._default = default_value

        return self._mobject

    def createAddr(self, long_name: str, short_name: str, default_value: float=0) -> 'MObject':
        """
        Creates a new address attribute, attaches it to the function set and returns it in an MObject.

        Args:
            long_name (str): Attr long name.
            short_name (str): Attr short name.
            default_value (float, long, optional): The default value of the attr upon being generated. Defaults to 0.

        Returns:
            MObject: Numeric Attribute Addr MObject.
        """
        return self.create(long_name=long_name, short_name=short_name, numeric_type=MFnNumericData.kAddr, default_value=default_value)

    def createColor(self, long_name: str, short_name: str) -> 'MObject':
        """
        Creates a new color attribute, attaches it to the function set and returns it in an MObject.

        Args:
            long_name (str): Attr long name.
            short_name (str): Attr short name.

        Returns:
            MObject: Numeric Attribute Color MObject.
        """
        return self.create(long_name=long_name, short_name=short_name, numeric_type=MFnNumericData.k3Double)

    def createPoint(self, long_name: str, short_name: str) -> 'MObject':
        """
        Creates a new 3D point attribute, attaches it to the function set and returns it in an MObject.
        Args:
            long_name (str): Attr long name.
            short_name (str): Attr short name.

        Returns:
            MObject: Numeric Attribute Color MObject.
        """
        return self.create(long_name=long_name, short_name=short_name, numeric_type=MFnNumericData.k3Double)

    def getMax(self) -> float | Tuple[float]:
        """
        Returns the attribute's hard maximum value(s).
        """
        if self._mobject._max is None:
            raise RuntimeError(f'Attribute: {self._mobject._name} does not have a maximum value.')
        return self._mobject._max

    def getMin(self) -> float | Tuple[float]:
        """
        Returns the attribute's hard minimum value(s).
        """
        if self._mobject._min is None:
            raise RuntimeError(f'Attribute: {self._mobject._name} does not have a minimum value.')
        return self._mobject._min

    def getSoftMax(self) -> float | Tuple[float]:
        """
        Returns the attribute's soft maximum value.
        """
        if self._mobject._soft_max is None:
            raise RuntimeError(f'Attribute: {self._mobject._name} does not have a soft maximum value.')
        return self._mobject._soft_max

    def getSoftMin(self) -> float | Tuple[float]:
        """
        Returns the attribute's soft minimum value.
        """
        if self._mobject._soft_min is None:
            raise RuntimeError(f'Attribute: {self._mobject._name} does not have a soft minimum value.')
        return self._mobject._soft_min

    def hasMax(self) -> bool:
        """
        Returns True if a hard maximum value has been specified for the attribute.
        """
        return True if self._mobject._max else False

    def hasMin(self) -> bool:
        """
        Returns True if a hard minimum value has been specified for the attribute.
        """
        return True if self._mobject._min else False

    def hasSoftMax(self) -> bool:
        """
        Returns True if a soft maximum value has been specified for the attribute.
        """
        return True if self._mobject._soft_max else False

    def hasSoftMin(self) -> bool:
        """
        Returns True if a soft minimum value has been specified for the attribute.
        """
        return True if self._mobject._soft_min else False

    def numericType(self):
        """
        Returns the numeric type of the attribute currently attached to the function set.
        """
        return self._mobject._numeric_type

    def setMax(self, new_value: float) -> 'MFnNumericAttribute':
        """
        Sets the attribute's hard maximum value(s).
        """
        self._mobject._max = new_value
        return self

    def setMin(self, new_value: float) -> 'MFnNumericAttribute':
        """
        Sets the attribute's hard minimum value(s).
        """
        self._mobject._min = new_value
        return self

    def setSoftMax(self, new_value: float) -> 'MFnNumericAttribute':
        """
        Sets the attribute's soft maximum value.
        """
        self._mobject._soft_max = new_value
        return self

    def setSoftMin(self, new_value: float) -> 'MFnNumericAttribute':
        """
        Sets the attribute's soft minimum value.
        """
        self._mobject._soft_min = new_value
        return self

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, value: float):
        self._default = value


class MFnStringArrayData(MFnData):
    """
    Function set for node data consisting of an array of string.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as a list of unicode objects.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new string array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnDoubleArrayData(MFnData):
    """
    Function set for node data consisting of an array of doubles.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as an MDoubleArray.
        """
        pass

    def copyTo(*args, **kwargs):
        """
        Replaces the elements of an array with those in the encapsulated array.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new double array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnEnumAttribute(MFnAttribute):
    """
    Functionset for creating and working with enumeration attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)
        self._enum_items = {}

    def addField(self, name: str, value: int) -> 'MFnEnumAttribute':
        """
        Add an item to the enumeration with a specified UI name and corresponding attribute value.
        """
        self._enum_items[name] = value
        return self

    def create(self, long_name: str, short_name: str, default: int = 0) -> 'MObject':
        """
        Creates a new enumeration attribute, attaches it to the function set and returns it as an MObject.
        """
        super()._create(long_name=long_name, short_name=short_name)
        self._mobject._api_type.append(MFn.kEnumAttribute)
        self._mobject._default = default
        self._mobject._value = default
        return self._mobject

    def fieldName(self, value: int) -> str:
        """
        Returns the name of the enumeration item which has a given value.
        """
        for name, val in self._enum_items.items():
            if val == value:
                return name
        raise ValueError(f"No field with value {value}")

    def fieldValue(self, name: str) -> int:
        """
        Returns the value of the enumeration item which has a given name.
        """
        if name in self._enum_items:
            return self._enum_items[name]
        raise ValueError(f"No field with name {name}")

    def getMax(self) -> int:
        """
        Returns the maximum value of all the enumeration items.
        """
        if not self._enum_items:
            raise ValueError("No fields in the enumeration")
        return max(self._enum_items.values())

    def getMin(self) -> int:
        """
        Returns the minimum value of all the enumeration items.
        """
        if not self._enum_items:
            raise ValueError("No fields in the enumeration")
        return min(self._enum_items.values())

    def setDefaultByName(self, name: str) -> 'MFnEnumAttribute':
        """
        Set the default value using the name of an enumeration item. Equivalent to: attr.default = attr.fieldValue(name)
        """
        self._default = self.fieldValue(name)
        return self

    @property
    def default(self) -> int:
        return self._default

    @default.setter
    def default(self, value: int):
        self._default = value


class MFnTypedAttribute(MFnAttribute):
    """
    Functionset for creating and working typed attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)

    def attrType(self):
        """
        Returns the type of data handled by the attribute.
        """
        return self._mobject._typed_attr_type

    def create(self, long_name: str, short_name: str, data_type: int, default_value=None) -> 'MObject':
        """
        Creates a new type attribute, attaches it to the function set and returns it as an MObject.

        You may choose a type form MFnData class to specify the type of data the attribute will handle.
        """
        super()._create(long_name=long_name, short_name=short_name)

        # Initialize typed attribute fields
        self._mobject._init_typed_fields()

        self._mobject._api_type.append(MFn.kTypedAttribute)
        self._mobject._typed_attr_type = data_type

        # Handle defaults based on specific data types
        if data_type == MFnData.kString:
            default_value = ''

        self._mobject._value = default_value
        self._mobject._default = default_value

        return self._mobject

    @property
    def default(self):
        return self._mobject._default

    @default.setter
    def default(self, value):
        self._mobject._default = value


class MFnUInt64ArrayData(MFnData):
    """
    Function set for node data consisting of an array of MUint64.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as an MUint64Array.
        """
        pass

    def copyTo(*args, **kwargs):
        """
        Replaces the elements of an array with those in the encapsulated array.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new MUint64 array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnContainerNode(MFnDependencyNode):
    """
    Function set for containers.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def clear(*args, **kwargs):
        """
        clear()

        Delete all members of the container.
        """
        pass

    def getMembers(*args, **kwargs):
        """
        getMembers() -> MObjectArray

        Return an array of the nodes included in this container.
        """
        pass

    def getParentContainer(*args, **kwargs):
        """
        getParentContainer() -> MObject

        Return the parent container, if there is one. Otherwise return an empty MObject.
        """
        pass

    def getPublishedNames(*args, **kwargs):
        """
        getPublishedNames(unboundOnly=bool) -> [MString]

        Return a list of published names on the container. Depending on the arguments, either all published names or only unbound published names will be returned.
        """
        pass

    def getPublishedNodes(*args, **kwargs):
        """
        getPublishedNodes(publishNodeType=MPublishNodeType) -> ([MString] publishedNames, MObjectArray publishedNodes)

        Return a list of the published nodes of a given type. For any names that have assigned nodes, return the node at the corresponding array index. For any names that do not have assigned nodes, a NULL MObject will be at the corresponding array index.
        """
        pass

    def getPublishedPlugs(*args, **kwargs):
        """
        getPublishedPlugs() -> (MPlugArray publishedPlugs, [MString] publishedNames)

        Return a tuple of plugs that have been published on this container and the names of those plugs.
        """
        pass

    def getRootTransform(*args, **kwargs):
        """
        getRootTransform() -> MObject

        Return the root transform, if there is one. Otherwise return an empty MObject.
        """
        pass

    def getSubcontainers(*args, **kwargs):
        """
        getSubcontainers() -> MObjectArray

        Return an array of the container nodes included in this container.
        """
        pass

    def isCurrent(*args, **kwargs):
        """
        isCurrent() -> bool

        Return whether the container node managed by this function set is the current container.
        """
        pass

    def makeCurrent(*args, **kwargs):
        """
        makeCurrent(isCurrent) -> self

        Set or clear whether the container managed by this function set is denoted as the
        the current container.  If the flag is true and the container is allowed to be
        current, then the current container is set to be the container.  Otherwise, if the
        container managed by the function set is the current container, then the current
        container is cleared.

        * isCurrent (True/False) - Specifies whether this container shall be current.
        """
        pass

    @staticmethod
    def getCurrentAsMObject(*args, **kwargs):
        """
        getCurrentAsMObject() -> MObject

        Retrieve the current container node.
        """
        pass

    kChildAnchor = 1

    kGeneric = 2

    kParentAnchor = 0


class MFnNumericData(MFnData):
    """
    Function set for non-simple numeric node data.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new numeric data object.
        """
        pass

    def getData(*args, **kwargs):
        """
        Returns a list containing the attached data object's data.
        """
        pass

    def numericType(*args, **kwargs):
        """
        Returns the type of data in the attached data object.
        """
        pass

    def setData(*args, **kwargs):
        """
        Sets the value of the data in the attached data object.
        """
        pass

    k2Double = 15

    k2Float = 12

    k2Int = 8

    k2Long = 8

    k2Short = 5

    k3Double = 16

    k3Float = 13

    k3Int = 9

    k3Long = 9

    k3Short = 6

    k4Double = 17

    kAddr = 18

    kBoolean = 1

    kByte = 2

    kChar = 3

    kDouble = 14

    kFloat = 11

    kInt = 7

    kInt64 = 10

    kInvalid = 0

    kLast = 19

    kLong = 7

    kShort = 4


class MFnDagNode(MFnDependencyNode):
    """
    Function set for operating on DAG nodes.

    __init__()
    Initializes a new, empty MFnDagNode functionset.

    __init__(MObject)
    Initializes a new MFnDagNode functionset and attaches it to a
    DAG node.

    __init__(MDagPath)
    Initializes a new MFnDagNode functionset and attaches it to a
    DAG path.
    """

    def __init__(self, mobject : Optional['MObject']=None):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(mobject)

    def addChild(*args, **kwargs):
        """
        addChild(node, index=kNextPos, keepExistingParents=False) -> self

        Makes a node a child of this one.
        """
        pass

    def child(*args, **kwargs):
        """
        child(index) -> MObject

        Returns the specified child of this node.
        """
        pass

    def childCount(*args, **kwargs):
        """
        childCount() -> int

        Returns the number of nodes which are children of this one.
        """
        pass

    def create(self, node_type: Union[str, MTypeId], name: Optional[str] = None,
               parent: Optional[MObject] = None) -> MObject:
        """
        create(type, name=None, parent=MObject.kNullObj) -> MObject

        Creates a new DAG node of the specified type, with the given name.
        The type may be either a type name or a type ID. If no name is given
        then a unique name will be generated by combining the type name with
        an integer.

        If a parent is given then the new node will be parented under it and
        the functionset will be attached to the newly-created node. The
        newly-created node will be returned.

        If no parent is given and the new node is a transform, it will be
        parented under the world and the functionset will be attached to the
        newly-created transform. The newly-created transform will be returned.

        If no parent is given and the new node is not a transform then a
        transform node will be created under the world, the new node will be
        parented under it, and the functionset will be attached to the
        transform. The transform will be returned.
        """

        mobject = super().create(node_type, name)
        mobject._api_type.insert(mobject._api_type.index(MFn.kDependencyNode) + 1, MFn.kDagNode)
        if parent:
            mobject._parent = parent
            mobject._parent._children.add(mobject)
        else:
            mobject._parent = WORLD

        return mobject

    def dagPath(*args, **kwargs):
        """
        dagPath() -> MDagPath

        Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path.
        """
        pass

    def dagRoot(self):
        """
        dagRoot() -> MObject

        Returns the root node of the first path leading to this node.
        """
        pass

    def duplicate(*args, **kwargs):
        """
        duplicate(instance=False, instanceLeaf=False) -> MObject

        Duplicates the DAG hierarchy rooted at the current node.
        """
        pass

    def fullPathName(*args, **kwargs):
        """
        fullPathName() -> string

        Returns the full path of the attached object, from the root of the DAG on down.
        """
        pass

    def getAllPaths(*args, **kwargs):
        """
        getAllPaths() -> MDagPathArray

        Returns all of the DAG paths which lead to the object to which this function set is attached.
        """
        pass

    def getConnectedSetsAndMembers(*args, **kwargs):
        """
        getConnectedSetsAndMembers(instance, renderableSetsOnly) -> (MObjectArray, MObjectArray)

        Returns a tuple containing an array of sets and an array of the
        components of the DAG object which are in those sets. If the entire object is in a set, then the corresponding entry in the comps array will have no elements in it.
        """
        pass

    def getPath(self) -> 'MDagPath':
        """
        getPath() -> MDagPath

        Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject.
        """
        dag_path = MDagPath()
        dag_path._node = self._mobject
        return dag_path


    def hasChild(*args, **kwargs):
        """
        hasChild(node) -> bool

        Returns True if the specified node is a child of this one.
        """
        pass

    def hasParent(*args, **kwargs):
        """
        hasParent(node) -> bool

        Returns True if the specified node is a parent of this one.
        """
        pass

    def instanceCount(*args, **kwargs):
        """
        instanceCount(indirect) -> int

        Returns the number of instances for this node.
        """
        pass

    def isChildOf(*args, **kwargs):
        """
        isChildOf(node) -> bool

        Returns True if the specified node is a parent of this one.
        """
        pass

    def isInstanced(*args, **kwargs):
        """
        isInstanced(indirect=True) -> bool

        Returns True if this node is instanced.
        """
        pass

    def isInstancedAttribute(*args, **kwargs):
        """
        isInstancedAttribute(attr) -> bool

        Returns True if the specified attribute is an instanced attribute of this node.
        """
        pass

    def isParentOf(*args, **kwargs):
        """
        isParentOf(node) -> bool

        Returns True if the specified node is a child of this one.
        """
        pass

    def parent(self, index: int):
        """
        parent(index) -> MObject

        Returns the specified parent of this node.
        """
        if index > 0:
            raise NotImplementedError('Not implemented for parent values greater than 0, sorry.')
        return self._mobject._parent or WORLD

    def parentCount(*args, **kwargs):
        """
        parentCount() -> int

        Returns the number of parents this node has.
        """
        pass

    def partialPathName(*args, **kwargs):
        """
        partialPathName() -> string

        Returns the minimum path string necessary to uniquely identify the attached object.
        """
        pass

    def removeChild(*args, **kwargs):
        """
        removeChild(node) -> self

        Removes the child, specified by MObject, reparenting it under the world.
        """
        pass

    def removeChildAt(*args, **kwargs):
        """
        removeChildAt(index) -> self

        Removes the child, specified by index, reparenting it under the world.
        """
        pass

    def setObject(self, mobject: Union['MObject', 'MDagPath']):
        """
        setObject(MObject or MDagPath) -> self

        Attaches the function set to the specified node or DAG path.
        """
        if isinstance(mobject, MDagPath):
            self._dag_path = mobject
        else:
            self._mobject = mobject
        return self

    def transformationMatrix(*args, **kwargs):
        """
        transformationMatrix() -> MMatrix

        Returns the object space transformation matrix for this DAG node.
        """
        pass

    boundingBox = None

    inModel = None

    inUnderWorld = None

    isInstanceable = None

    isIntermediateObject = None

    kNextPos = 255

    objectColor = None

    objectColorRGB = None

    objectColorType = None

    useObjectColor = None


class MFnGenericAttribute(MFnAttribute):
    """
    Functionset for creating and working with attributes which can accept several different types of data.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addDataType(*args, **kwargs):
        """
        Adds the specified Maya data type to the list of those accepted by the attribute.
        """
        pass

    def addNumericType(*args, **kwargs):
        """
        Adds the specified numeric type to the list of those accepted by the attribute.
        """
        pass

    def addTypeId(*args, **kwargs):
        """
        Adds the specified data typeId to the list of those accepted by the attribute.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new generic attribute, attaches it to the function set and returns it as an MObject.
        """
        pass

    def removeDataType(*args, **kwargs):
        """
        Removes the specified Maya data type from the list of those accepted by the attribute.
        """
        pass

    def removeNumericType(*args, **kwargs):
        """
        Removes the specified numeric type from the list of those accepted by the attribute.
        """
        pass

    def removeTypeId(*args, **kwargs):
        """
        Removes the specified data typeId from the list of those accepted by the attribute.
        """
        pass


class MFnDoubleIndexedComponent(MFnComponent):
    """
    This function set allows you to create, edit, and query double indexed
    components. Double indexed components store 2 dimensional index values.

    __init__()
    Initializes a new, empty MFnDoubleIndexedComponent object

    __init__(MObject component)
    Initializes a new MFnDoubleIndexedComponent function set, attached
    to the specified component.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addElement(*args, **kwargs):
        """
        addElement(uIndex, vIndex) -> self
        addElement([uIndex, vIndex]) -> self

        Adds the element identified by (uIndex, vIndex) to the component.
        """
        pass

    def addElements(*args, **kwargs):
        """
        addElements(sequence of [uIndex, vIndex]) -> self

        Adds the specified elements to the component. Each item in the
        elements sequence is itself a sequence of two ints which are the U and
        V indices of an element to be added.
        """
        pass

    def create(*args, **kwargs):
        """
        create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """
        pass

    def getCompleteData(*args, **kwargs):
        """
        getCompleteData() -> (numU, numV)

        Returns a tuple containing the number of U and V indices in the complete
        component, or (0,0) if the component is not complete.
        """
        pass

    def getElement(*args, **kwargs):
        """
        getElement(index) -> (uIndex, vIndex)

        Returns the index'th element of the component as a tuple containing the
        element's U and V indices.
        """
        pass

    def getElements(*args, **kwargs):
        """
        getElements() -> list of (uIndex, vIndex)

        Returns all of the component's elements as a list of tuples with each
        tuple containing the U and V indices of a single element.
        """
        pass

    def setCompleteData(*args, **kwargs):
        """
        setCompleteData(numU, numV) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numU and numV indicate the number of U and V indices in the complete
        component (i.e. the max U index is numU-1 and the max V index is numV-1).
        """
        pass


class MFnVectorArrayData(MFnData):
    """
    Function set for node data consisting of an array of MVectors.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as an MVectorArray.
        """
        pass

    def copyTo(*args, **kwargs):
        """
        Replaces the elements of an array with those in the encapsulated array.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new MVector array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnUnitAttribute(MFnAttribute):
    """
    Functionset for creating and working with angle, distance and time attributes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new unit attribute, attaches it to the function set and returns it as an MObject.
        """
        pass

    def getMax(*args, **kwargs):
        """
        Returns the attribute's hard maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively
        """
        pass

    def getMin(*args, **kwargs):
        """
        Returns the attribute's hard minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively
        """
        pass

    def getSoftMax(*args, **kwargs):
        """
        Returns the attribute's soft maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively
        """
        pass

    def getSoftMin(*args, **kwargs):
        """
        Returns the attribute's soft minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively
        """
        pass

    def hasMax(*args, **kwargs):
        """
        Returns True if the attribute has a hard maximum value.
        """
        pass

    def hasMin(*args, **kwargs):
        """
        Returns True if the attribute has a hard minimum value.
        """
        pass

    def hasSoftMax(*args, **kwargs):
        """
        Returns True if the attribute has a soft maximum value.
        """
        pass

    def hasSoftMin(*args, **kwargs):
        """
        Returns True if the attribute has a soft minimum value.
        """
        pass

    def setMax(*args, **kwargs):
        """
        Sets the attribute's hard maximum value.
        """
        pass

    def setMin(*args, **kwargs):
        """
        Sets the attribute's hard minimum value.
        """
        pass

    def setSoftMax(*args, **kwargs):
        """
        Sets the attribute's soft maximum value.
        """
        pass

    def setSoftMin(*args, **kwargs):
        """
        Sets the attribute's soft minimum value.
        """
        pass

    def unitType(*args, **kwargs):
        """
        Returns the type of data handled by the attribute.
        """
        pass

    default = None

    kAngle = 1

    kDistance = 2

    kInvalid = 0

    kLast = 4

    kTime = 3


class MFnReference(MFnDependencyNode):
    """
    Function set for reference nodes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def associatedNamespace(*args, **kwargs):
        """
        associatedNamespace(bool shortName) -> MString

        Returns the namespace associated with this reference.
        """
        pass

    def containsNode(*args, **kwargs):
        """
        containsNode(MObject) -> bool

        Returns true if the specified node is from this reference or one of its child references. The containsNodeExactly method can be used to test membership without including the child references.
        """
        pass

    def containsNodeExactly(*args, **kwargs):
        """
        containsNodeExactly(MObject) -> bool

        Returns true if the specified node is from this reference. Membership in child references is not checked. The containsNode method may be used to test membership in a reference and its child references.
        """
        pass

    def fileName(*args, **kwargs):
        """
        fileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

        Returns the name of file associated with this reference.
        """
        pass

    def isExportEditsFile(*args, **kwargs):
        """
        isExportEditsFile() -> bool

        Returns true if the reference is an export edits file. An export edits file is a file of type '.editMA' or '.editMB' which was created using Maya's offline file functionality.
        """
        pass

    def isLoaded(*args, **kwargs):
        """
        isLoaded() -> bool

        Returns true if the reference is loaded.
        """
        pass

    def isLocked(*args, **kwargs):
        """
        isLocked() -> bool

        Returns true if the reference is locked or if the referenced file was saved as locked.
        """
        pass

    def nodes(*args, **kwargs):
        """
        nodes() -> MObjectArray

        Returns an array of the nodes associated with this reference.
        """
        pass

    def parentAssembly(*args, **kwargs):
        """
        parentAssembly() -> MObject

        Returns the parent assembly node that contains this reference. See MFnAssembly documentation for more details.
        """
        pass

    def parentFileName(*args, **kwargs):
        """
        parentFileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

        Returns the name of parent file associated with this reference.
        """
        pass

    def parentReference(*args, **kwargs):
        """
        parentReference() -> MObject

        Returns the reference node associated with the parent reference.
        """
        pass

    @staticmethod
    def ignoreReferenceEdits(*args, **kwargs):
        """
        ignoreReferenceEdits() -> bool

        Indicates whether reference edits will be tracked and logged or not.
        """
        pass

    @staticmethod
    def setIgnoreReferenceEdits(*args, **kwargs):
        """
        setIgnoreReferenceEdits(bool) -> None

        Specify whether reference edits should be tracked and logged or not.
        This should be treated as a temporary state and should be enabled
        around a batch of operations where reference edits should be ignored.
        Restore the previous value when the batch of operations is complete.
        """
        pass


class MFnLightDataAttribute(MFnAttribute):
    """
    Functionset for creating and working with light data attributes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def child(*args, **kwargs):
        """
        Returns one of the attribute's children, specified by index.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new light data attribute, attaches it to the function set and returns it as an MObject.
        """
        pass

    default = None


class MFnPluginData(MFnData):
    """
    MFnPluginData allows the creation and manipulation of plugin
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnPluginData object

    __init__(MObject)
    Initializes a new MFnPluginData function set, attached
    to the specified object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        create(id) -> MObject

        Create an instance of the specified user defined data type and attach it to this functionset.

        * id (MTypeId) - the unique MTypeId of the user defined data class derived from MPxData.
        """
        pass

    def data(*args, **kwargs):
        """
        data() -> MPxData

        Return the user defined data held in this instance
        """
        pass

    def typeId(*args, **kwargs):
        """
        typeId() -> MTypeId

        Return the unique MTypeId of the user defined data that is held by this instance
        """
        pass


class MFnGeometryData(MFnData):
    """
    This class is the function set for geometry data.

    Geometry data adds matrix and grouping (set) information to regular
    data and is used to pass geometry types such as mesh, lattice, and
    NURBS shape data through DG connections.

    __init__()
    Initializes a new, empty MFnGeometryData object

    __init__(MObject)
    Initializes a new MFnGeometryData function set, attached
    to the specified object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addObjectGroup(*args, **kwargs):
        """
        addObjectGroup(id) -> self

        Adds an object group with the given id to the object.
        """
        pass

    def addObjectGroupComponent(*args, **kwargs):
        """
        addObjectGroupComponent(id, MObject component) -> self

        Adds the members of the given component to the object group
        with the given id.
        """
        pass

    def changeObjectGroupId(*args, **kwargs):
        """
        changeObjectGroupId(sourceId, destId) -> self

        Changes the id of the object group with the given id to the new id.
        """
        pass

    def copyObjectGroups(*args, **kwargs):
        """
        copyObjectGroups(MObject inGeom) -> self

        Copies the object groups from the given geometry data object.
        """
        pass

    def hasObjectGroup(*args, **kwargs):
        """
        hasObjectGroup(id) -> self

        Returns True if an object group with the given id is
        contained in the data.
        """
        pass

    def objectGroup(*args, **kwargs):
        """
        objectGroup(index) -> int

        Returns the id of the index'th object group contained by the object.
        """
        pass

    def objectGroupComponent(*args, **kwargs):
        """
        objectGroupComponent(id) -> MObject

        Returns a component which contains the members of the object group
        with the given id.
        """
        pass

    def objectGroupType(*args, **kwargs):
        """
        objectGroupType(id) -> MFn Type constant

        Returns the type of the component that the object group with the
        given id contains.
        """
        pass

    def removeObjectGroup(*args, **kwargs):
        """
        removeObjectGroup(id) -> self

        Removes an object group with the given id from the object.
        """
        pass

    def removeObjectGroupComponent(*args, **kwargs):
        """
        removeObjectGroupComponent(id, MObject component) -> self

        Removes the members of the given component from the object group
        with the given id.
        """
        pass

    def setObjectGroupComponent(*args, **kwargs):
        """
        setObjectGroupComponent(id, MObject component) -> self

        Sets the members of the object group with the given id
        to be only those in the given component.
        """
        pass

    isIdentity = None

    isNotIdentity = None

    matrix = None

    objectGroupCount = None


class MFnSingleIndexedComponent(MFnComponent):
    """
    This function set allows you to create, edit, and query single indexed components.
    Single indexed components store 1 dimensional index values.

    __init__()
    Initializes a new, empty MFnSingleIndexedComponent object

    __init__(MObject component)
    Initializes a new MFnSingleIndexedComponent function set, attached to the specified component.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addElement(*args, **kwargs):
        """
        addElement(int element) -> self

        Adds the specified element to the component.
        """
        pass

    def addElements(*args, **kwargs):
        """
        addElements([int]) -> self
        addElements(MIntArray) -> self

        Adds the specified elements to the component.
        """
        pass

    def create(*args, **kwargs):
        """
        create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """
        pass

    def element(*args, **kwargs):
        """
        element(index) -> int

        Returns the index'th element of the component.
        """
        pass

    def getCompleteData(*args, **kwargs):
        """
        getCompleteData() -> int

        Returns the number of elements in the complete component, or 0 if the component is not complete.
        """
        pass

    def getElements(*args, **kwargs):
        """
        getElements() -> MIntArray

        Returns all of the component's elements.
        """
        pass

    def setCompleteData(*args, **kwargs):
        """
        setCompleteData(numElements) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numElements indicates the number of elements in the complete component.
        """
        pass

    elementMax = None


class MFnMatrixAttribute(MFnAttribute):
    """
    Functionset for creating and working with matrix attributes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new matrix attribute, attaches it to the function set and returns it as an MObject.
        """
        pass

    default = None

    kDouble = 1

    kFloat = 0


class MFnSet(MFnDependencyNode):
    """
    Function set for sets.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addMember(*args, **kwargs):
        """
        addMember( object ) -> self

        Add a new object to the set.

        The added object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """
        pass

    def addMembers(*args, **kwargs):
        """
        addMembers( MSelectionList ) -> self

        Add a list of new objects to the set.
        """
        pass

    def annotation(*args, **kwargs):
        """
        annotation() -> string

        Returns the annotation string for this set.  This allows a description of the set to be stored with it.
        """
        pass

    def clear(*args, **kwargs):
        """
        clear() -> self

        Removes all elements from this set.
        """
        pass

    def create(*args, **kwargs):
        """
        create(members, restriction=kNone) -> MObject

        Creates a new set dependency node and puts it in the dependency graph.

        * members (MSelectionList) - list of members for new set
        * restriction (MFnSet.Restriction) - restriction applied to members
        """
        pass

    def getIntersection(*args, **kwargs):
        """
        getIntersection( otherSet ) -> MSelectionList

        This method calculates the intersection of two sets.  The result will be the intersection of this set and the set passed into the method.

        * otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set
        """
        pass

    def getMembers(*args, **kwargs):
        """
        getMembers( flatten ) -> MSelectionList

        Get the members of this set as a selection list.  This information is providedas a selection list so that all of the path information is retained forDAG nodes.

        It is possible to ask for the returned list to be flattened.  This means thatall sets that exist inside this set will be expanded into a list of theircontents.

        * flatten (bool) - whether to flatten the returned list
        """
        pass

    def getUnion(*args, **kwargs):
        """
        getUnion( otherSet ) -> MSelectionList

        This method calculates the union of two sets.  The result will be the union of this set and the set passed into the method.

        * otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set
        """
        pass

    def hasRestrictions(*args, **kwargs):
        """
        hasRestrictions() -> bool

        Returns true if this function set has restrictions on the type of objects that it may contain.
        """
        pass

    def intersectsWith(*args, **kwargs):
        """
        intersectsWith( otherSet ) -> self

        Returns true if this set intersects with the given set.  An intersection occurs if there are any common members between the two sets.
        """
        pass

    def isMember(*args, **kwargs):
        """
        isMember( object ) -> bool

        Returns true if the given object is a member of this set.

        The object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """
        pass

    def removeMember(*args, **kwargs):
        """
        removeMember( object ) -> self

        Remove an object from the set.

        The removed object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """
        pass

    def removeMembers(*args, **kwargs):
        """
        removeMembers( MSelectionList ) -> self

        Remove items of the selection list from the set.
        """
        pass

    def restriction(*args, **kwargs):
        """
        restriction() -> MFnSet.Restriction

        Returns the type of membership restriction that this set has.
        """
        pass

    def setAnnotation(*args, **kwargs):
        """
        setAnnotation( annotation ) -> self

        Sets the annotation string for this set.  This allows a description of the set to be stored with it.
        """
        pass

    kEdgesOnly = 2

    kEditPointsOnly = 4

    kFacetsOnly = 3

    kNone = 0

    kRenderableOnly = 5

    kVerticesOnly = 1


class MFnIntArrayData(MFnData):
    """
    Function set for node data consisting of an array of ints.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as an MIntArray.
        """
        pass

    def copyTo(*args, **kwargs):
        """
        Replaces the elements of an array with those in the encapsulated array.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new int array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnTripleIndexedComponent(MFnComponent):
    """
    This function set allows you to create, edit, and query triple indexed
    components. Triple indexed components store 3 dimensional index values.

    __init__()
    Initializes a new, empty MFnTripleIndexedComponent object

    __init__(MObject component)
    Initializes a new MFnTripleIndexedComponent function set, attached
    to the specified component.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addElement(*args, **kwargs):
        """
        addElement(sIndex, tIndex, uIndex) -> self
        addElement([sIndex, tIndex, uIndex]) -> self

        Adds the element identified by (sIndex, tIndex, uIndex) to the component.
        """
        pass

    def addElements(*args, **kwargs):
        """
        addElements(sequence of [sIndex, tIndex, uIndex]) -> self

        Adds the specified elements to the component. Each item in the
        elements sequence is itself a sequence of three ints which are the
        S, T and U indices of an element to be added.
        """
        pass

    def create(*args, **kwargs):
        """
        create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """
        pass

    def getCompleteData(*args, **kwargs):
        """
        getCompleteData() -> (numS, numT, numU)

        Returns a tuple containing the number of S, T and U indices in
        the complete component, or (0,0,0) if the component is not complete.
        """
        pass

    def getElement(*args, **kwargs):
        """
        getElement(index) -> (sIndex, tIndex, uIndex)

        Returns the index'th element of the component as a tuple containing the
        element's S, T and U indices.
        """
        pass

    def getElements(*args, **kwargs):
        """
        getElements() -> list of (sIndex, tIndex, uIndex)

        Returns all of the component's elements as a list of tuples with each
        tuple containing the S, T and U indices of a single element.
        """
        pass

    def setCompleteData(*args, **kwargs):
        """
        setCompleteData(numS, numT, numU) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numS, numT and numU indicate the number of S, T and U indices
        in the complete component (i.e. the max S index is numS-1, the max T
        index is numT-1 and the max U index is numU-1).
        """
        pass


class MFnMessageAttribute(MFnAttribute):
    """
    Functionset for creating and working with message attributes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new message attribute, attaches it to the function set and returns it as an MObject.
        """
        pass


class MFnPointArrayData(MFnData):
    """
    Function set for node data consisting of an array of MPoints.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as an MPointArray.
        """
        pass

    def copyTo(*args, **kwargs):
        """
        Replaces the elements of an array with those in the encapsulated array.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new MPoint array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnMatrixArrayData(MFnData):
    """
    Function set for node data consisting of an array of MMatrix.
    """

    def __delitem__(*args, **kwargs):
        """
        x.__delitem__(y) <==> del x[y]
        """
        pass

    def __getitem__(*args, **kwargs):
        """
        x.__getitem__(y) <==> x[y]
        """
        pass

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def __len__(*args, **kwargs):
        """
        x.__len__() <==> len(x)
        """
        pass

    def __setitem__(*args, **kwargs):
        """
        x.__setitem__(i, y) <==> x[i]=y
        """
        pass

    def array(*args, **kwargs):
        """
        Returns the encapsulated array as an MMatrixArray.
        """
        pass

    def copyTo(*args, **kwargs):
        """
        Replaces the elements of an array with those in the encapsulated array.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new MMatrix array data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets values in the encapsulated array.
        """
        pass


class MFnComponentListData(MFnData):
    """
    MFnComponentListData allows the creation and manipulation of component list
    (represented as MObjects) data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnComponentListData object.

    __init__(MObject)
    Initializes a new MFnComponentListData function set, attached
    to the specified object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def add(*args, **kwargs):
        """
        add(MObject) -> self

        Adds the specified component to the end of the list.
        """
        pass

    def clear(*args, **kwargs):
        """
        clear() -> self

        Removes all of the components from the list.
        """
        pass

    def create(*args, **kwargs):
        """
        create() -> MObject

        Creates a new, empty component list, attaches it to the
        function set and returns an MObject which references it.
        """
        pass

    def get(*args, **kwargs):
        """
        get(index) -> MObject

        Returns a copy of the component at the specified index.
        Raises IndexError if the index is out of range.
        """
        pass

    def has(*args, **kwargs):
        """
        has(MObject) -> bool

        Returns True if the list contains the specified
        component, False otherwise.
        """
        pass

    def length(*args, **kwargs):
        """
        length() -> int

        Returns the number of components in the list.
        """
        pass

    def remove(*args, **kwargs):
        """
        remove(MObject) -> self
        remove(index) -> self

        Removes the specified component from the list.
        No exception is raised if the component is not in the list,
        raises IndexError if index is out of range
        """
        pass


class MFnStringData(MFnData):
    """
    Function set for string node data.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new string data object.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets the value of the encapsulated string.
        """
        pass

    def string(*args, **kwargs):
        """
        Returns the encapsulated string as a unicode object.
        """
        pass


class MFnCompoundAttribute(MFnAttribute):
    """
    Functionset for creating and working with compound attributes.
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        super().__init__(*args, **kwargs)
        
        self._fn_type = MFn.kCompoundAttribute

    def addChild(self, child: 'MObject') -> 'MFnCompoundAttribute':
        """
        Add a child attribute.
        """
        assert child._alive is True, 'Child MObject must be valid to be added to a compound attribute.'
        self._mobject._children.append(child)
        child._parent = self._mobject
        return self

    def child(self, index: int) -> 'MObject':
        """
        Returns one of the attribute's children, specified by index.
        """
        return self._mobject._children[index]

    def create(self, long_name: str, short_name: str) -> 'MObject':
        """
        Creates a new compound attribute, attaches it to the function set and returns it as an MObject.
        """
        super()._create(long_name=long_name, short_name=short_name)
        self._mobject._api_type.append(MFn.kCompoundAttribute)
        self._mobject._is_compound = True
        return self._mobject

    def getAddAttrCmds(self) -> list:
        """
        Returns a list of MEL 'addAttr' commands capable of recreating the attribute and all of its children.
        """
        cmds = [f'addAttr -ln "{self._mobject._long_name}" -sn "{self._mobject._short_name}" -at compound']
        for child in self._mobject._children:
            cmds.append(f'addAttr -p "{self._mobject._long_name}" -ln "{child._long_name}" -sn "{child._short_name}" -at {child._api_type[-1]}')
        return cmds

    def numChildren(self) -> int:
        """
        Returns number of child attributes currently parented under the compound attribute.
        """
        return len(self._mobject._children)

    def removeChild(self, child: 'MObject') -> 'MFnCompoundAttribute':
        """
        Remove a child attribute.
        """
        self._mobject._children.remove(child)
        child._parent = None
        return self


class MFnMatrixData(MFnData):
    """
    Function set for matrix node data.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new matrix data object.
        """
        pass

    def isTransformation(*args, **kwargs):
        """
        Returns True if the attached object is an MTransformationMatrix, False if it is an MMatrix.
        """
        pass

    def matrix(*args, **kwargs):
        """
        Returns the encapsulated matrix as an MMatrix.
        """
        pass

    def set(*args, **kwargs):
        """
        Sets the value of the encapsulated matrix.
        """
        pass

    def transformation(*args, **kwargs):
        """
        Returns the encapsulated matrix as an MTransformationMatrix.
        """
        pass


class MFnTransform(MFnDagNode):
    """
    Function set for operating on transform nodes.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def clearRestPosition(*args, **kwargs):
        """
        Clears the transform's rest position matrix.
        """
        pass

    def create(*args, **kwargs):
        """
        Creates a new transform node and attaches it to the function set.
        """
        pass

    def enableLimit(*args, **kwargs):
        """
        Enables or disables a specified limit type.
        """
        pass

    def isLimited(*args, **kwargs):
        """
        Returns True if the specified limit type is enabled.
        """
        pass

    def limitValue(*args, **kwargs):
        """
        Returns the value of the specified limit.
        """
        pass

    def resetFromRestPosition(*args, **kwargs):
        """
        Resets the transform from its rest position matrix.
        """
        pass

    def restPosition(*args, **kwargs):
        """
        Returns the transform's rest position matrix.
        """
        pass

    def rotateBy(*args, **kwargs):
        """
        Adds an MEulerRotation or MQuaternion to the transform's rotation.
        """
        pass

    def rotateByComponents(*args, **kwargs):
        """
        Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion.
        """
        pass

    def rotateOrientation(*args, **kwargs):
        """
        Returns the MQuaternion which orients the local rotation space.
        """
        pass

    def rotatePivot(*args, **kwargs):
        """
        Returns the transform's rotate pivot.
        """
        pass

    def rotatePivotTranslation(*args, **kwargs):
        """
        Returns the transform's rotate pivot translation.
        """
        pass

    def rotation(*args, **kwargs):
        """
        Returns the transform's rotation as an MEulerRotation or MQuaternion.
        """
        pass

    def rotationComponents(*args, **kwargs):
        """
        Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion.
        """
        pass

    def rotationOrder(*args, **kwargs):
        """
        Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation.
        """
        pass

    def scale(*args, **kwargs):
        """
        Returns a list containing the transform's XYZ scale components.
        """
        pass

    def scaleBy(*args, **kwargs):
        """
        Multiplies the transform's XYZ scale components by a sequence of three floats.
        """
        pass

    def scalePivot(*args, **kwargs):
        """
        Returns the transform's scale pivot.
        """
        pass

    def scalePivotTranslation(*args, **kwargs):
        """
        Returns the transform's scale pivot translation.
        """
        pass

    def setLimit(*args, **kwargs):
        """
        Sets the value of the specified limit.
        """
        pass

    def setRestPosition(*args, **kwargs):
        """
        Sets the transform's rest position matrix.
        """
        pass

    def setRotateOrientation(*args, **kwargs):
        """
        Sets the MQuaternion which orients the local rotation space.
        """
        pass

    def setRotatePivot(*args, **kwargs):
        """
        Sets the transform's rotate pivot.
        """
        pass

    def setRotatePivotTranslation(*args, **kwargs):
        """
        Sets the transform's rotate pivot translation.
        """
        pass

    def setRotation(*args, **kwargs):
        """
        Sets the transform's rotation using an MEulerRotation or MQuaternion.
        """
        pass

    def setRotationComponents(*args, **kwargs):
        """
        Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion.
        """
        pass

    def setRotationOrder(*args, **kwargs):
        """
        Sets the transform's rotation order.
        """
        pass

    def setScale(*args, **kwargs):
        """
        Sets the transform's scale components.
        """
        pass

    def setScalePivot(*args, **kwargs):
        """
        Sets the transform's scale pivot.
        """
        pass

    def setScalePivotTranslation(*args, **kwargs):
        """
        Sets the transform's scale pivot translation.
        """
        pass

    def setShear(*args, **kwargs):
        """
        Sets the transform's shear.
        """
        pass

    def setTransformation(*args, **kwargs):
        """
        Sets the transform's attribute values to represent the given transformation matrix.
        """
        pass

    def setTranslation(*args, **kwargs):
        """
        Sets the transform's translation.
        """
        pass

    def shear(*args, **kwargs):
        """
        Returns a list containing the transform's shear components.
        """
        pass

    def shearBy(*args, **kwargs):
        """
        Multiplies the transform's shear components by a sequence of three floats.
        """
        pass

    def transformation(*args, **kwargs):
        """
        Returns the transformation matrix represented by this transform.
        """
        pass

    def translateBy(*args, **kwargs):
        """
        Adds an MVector to the transform's translation.
        """
        pass

    def translation(*args, **kwargs):
        """
        Returns the transform's translation as an MVector.
        """
        pass

    kRotateMaxX = 13

    kRotateMaxY = 15

    kRotateMaxZ = 17

    kRotateMinX = 12

    kRotateMinY = 14

    kRotateMinZ = 16

    kScaleMaxX = 1

    kScaleMaxY = 3

    kScaleMaxZ = 5

    kScaleMinX = 0

    kScaleMinY = 2

    kScaleMinZ = 4

    kShearMaxXY = 7

    kShearMaxXZ = 9

    kShearMaxYZ = 11

    kShearMinXY = 6

    kShearMinXZ = 8

    kShearMinYZ = 10

    kTranslateMaxX = 19

    kTranslateMaxY = 21

    kTranslateMaxZ = 23

    kTranslateMinX = 18

    kTranslateMinY = 20

    kTranslateMinZ = 22


class MFnMeshData(MFnGeometryData):
    """
    MFnMeshData allows the creation and manipulation of Mesh
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnMeshData object

    __init__(MObject)
    Initializes a new MFnMeshData function set, attached
    to the specified object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        create() -> MObject

        Creates a new mesh data object, attaches it to this function set
        and returns an MObject which references it.
        """
        pass


class MFnNurbsCurveData(MFnGeometryData):
    """
    MFnNurbsCurveData allows the creation and manipulation of Nurbs Curve
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnNurbsCurveData object

    __init__(MObject)
    Initializes a new MFnNurbsCurveData function set, attached
    to the specified object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        create() -> MObject

        Creates a new nurbs curve data object, attaches it to this function set
        and returns an MObject which references it.
        """
        pass


class MFnCamera(MFnDagNode):
    """
    Function set for cameras.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def aspectRatio(*args, **kwargs):
        """
        aspectRatio() -> float

        Returns the aspect ratio for the camera.
        """
        pass

    def centerOfInterestPoint(*args, **kwargs):
        """
        centerOfInterestPoint(space=kObject) -> MPoint

        Returns the center of interest point for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    def computeDepthOfField(*args, **kwargs):
        """
        computeDepthOfField(nearLimit=None) -> self

        Compute the depth of field

        * nearLimit (float) - the near limit
        """
        pass

    def copyViewFrom(*args, **kwargs):
        """
        copyViewFrom(otherCamera) -> self

        Copy the camera settings related to the perspective from the given camera view.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * otherCamera (MDagPath) - Camera to copy view from
        """
        pass

    def create(*args, **kwargs):
        """
        create(parent=None) -> MObject

        Creates a perspective camera. A parent can be specified for the new camera, otherwise a transform is created.

        The camera is positioned at (0, 0, 0), its center of interest at (0, 0, -1), which implies that the view-direction is pointing in the direction of the negative z-axis, and its up-direction along the positive Y axis.

        * parent (MObject) - The parent of the new camera
        """
        pass

    def eyePoint(*args, **kwargs):
        """
        eyePoint(space=kObject) -> MPoint

        Returns the eye point for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    def getAspectRatioLimits(*args, **kwargs):
        """
        getAspectRatioLimits() -> (float, float)

        Returns the minimum and maximum aspect ratio limits for the camera.
        """
        pass

    def getFilmApertureLimits(*args, **kwargs):
        """
        getFilmApertureLimits() -> (float, float)

        Returns the maximum and minimum film aperture limits for the camera.
        """
        pass

    def getFilmFrustum(*args, **kwargs):
        """
        getFilmFrustum(distance, applyPanZoom=False) -> (float, float, float, float)

        Returns the film frustum for the camera (horizontal size, vertical size, horizontal offset and vertical offset). The frustum defines the projective transformation.

        * distance (float) - Specifies the focal length
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
        pass

    def getFilmFrustumCorners(*args, **kwargs):
        """
        getFilmFrustumCorners(distance, applyPanZoom=False) -> MPointArray

        Returns the film frustum for the camera. The frustum defines the projective transformation.

         element 0 is the bottom left
         element 1 is the top left
         element 2 is the top right
         element 3 is the bottom right

        * distance (float) - Specifies the focal length
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
        pass

    def getFocalLengthLimits(*args, **kwargs):
        """
        getFocalLengthLimits() -> (float, float)

        Returns the maximum and minimum focal length limits for the camera.
        """
        pass

    def getPortFieldOfView(*args, **kwargs):
        """
        getPortFieldOfView(int, int) -> (float, float)

        Returns the horizontal and vertical field of view in radians from the given viewport width and height.

        * width (int) - width of viewport
        * height (int) - height of viewport
        """
        pass

    def getRenderingFrustum(*args, **kwargs):
        """
        getRenderingFrustum(windowAspect) -> (float, float, float, float)

        Returns the rendering frustum (left, right, bottom and top) for the camera.
        This is the frustum that the maya renderer uses.

        * windowAspect (float) - windowAspect
        """
        pass

    def getViewParameters(*args, **kwargs):
        """
        getViewParameters(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

        Returns the intermediate viewing frustum (apertureX, apertureY, offsetX and offsetY) parameters for the camera. The aperture and offset are used by getViewingFrustum() and getRenderingFrustum() to compute the extent (left, right, top, bottom) of the frustum in the following manner:

         left = focal_to_near * (-0.5*apertureX + offsetX)
         right = focal_to_near * (0.5*apertureX + offsetX)
         bottom = focal_to_near * (-0.5*apertureY + offsetY)
         top = focal_to_near * (0.5*apertureY + offsetY)

        Here, focal_to_near is equal to cameraScale if the camera is orthographic, or it is equal to ((nearClippingPlane / (focalLength * MM_TO_INCH)) * cameraScale) where MM_TO_INCH equals 0.03937.

        * windowAspect (float) - windowAspect
        * applyOverscan (bool) - specifies whether to apply overscan
        * applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
        pass

    def getViewingFrustum(*args, **kwargs):
        """
        getViewingFrustum(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

        Returns the viewing frustum (left, right, bottom and top) for the camera.

        * windowAspect (float) - windowAspect
        * applyOverscan (bool) - specifies whether to apply overscan
        * applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
        pass

    def hasSamePerspective(*args, **kwargs):
        """
        hasSamePerspective(otherCamera) -> bool

        Returns True if the camera has same perspective settings as the given camera.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * otherCamera (MDagPath) - Camera to compare perspective with
        """
        pass

    def horizontalFieldOfView(*args, **kwargs):
        """
        horizontalFieldOfView() -> float

        Returns the horizontal field of view for the camera.
        """
        pass

    def isOrtho(*args, **kwargs):
        """
        isOrtho() -> bool

        Returns True if the camera is in orthographic mode.
        """
        pass

    def postProjectionMatrix(*args, **kwargs):
        """
        postProjectionMatrix(context=None) -> MFloatMatrix

        Returns the post projection matrix used to compute film roll on the film back plane.

        * context (MDGContext) - DG time-context to specify time of evaluation
        """
        pass

    def projectionMatrix(*args, **kwargs):
        """
        projectionMatrix(context=None) -> MFloatMatrix

        Returns the orthographic or perspective projection matrix for the camera.
        The projection matrix that maya's software renderer uses is almost identical to the OpenGL projection matrix. The difference is that maya uses a left hand coordinate system and so the entries [2][2] and [3][2] are negated.

        * context (MDGContext) - DG time-context to specify time of evaluation
        """
        pass

    def rightDirection(*args, **kwargs):
        """
        rightDirection(space=kObject) -> MVector

        Returns the right direction vector for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    def set(*args, **kwargs):
        """
        set(wsEyeLocation, wsViewDirection, wsUpDirection, horizFieldOfView, aspectRatio) -> self

        Convenience routine to set the camera viewing parameters. The specified values should be in world space where applicable.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * wsEyeLocation (MPoint) - Eye location to set in world space
        * wsViewDirection (MVector) - View direction to set in world space
        * wsUpDirection (MVector) - Up direction to set in world space
        * horizFieldOfView (float) - The horizontal field of view to set
        * aspectRatio (float) - The aspect ratio to set
        """
        pass

    def setAspectRatio(*args, **kwargs):
        """
        setAspectRatio(aspectRatio) -> self

        Set the aspect ratio of the View.  The aspect ratio is expressed as width/height.  This also modifies the entity's scale transformation to reflect the new aspect ratio.

        * aspectRatio (float) - The aspect ratio to be set
        """
        pass

    def setCenterOfInterestPoint(*args, **kwargs):
        """
        setCenterOfInterestPoint(centerOfInterest, space=kObject) -> self

        Positions the center-of-interest of the camera keeping the eye-point fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * centerOfInterest (MPoint) - Center of interest point to be set
        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    def setEyePoint(*args, **kwargs):
        """
        setEyePoint(eyeLocation, space=kObject) -> self

        Positions the eye-point of the camera keeping the center of interest fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * eyeLocation (MPoint) - The eye location to set
        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    def setHorizontalFieldOfView(*args, **kwargs):
        """
        setHorizontalFieldOfView(fov) -> self

        Sets the horizontal field of view for the camera.

        * fov (float) - The horizontal field of view value to be set
        """
        pass

    def setIsOrtho(*args, **kwargs):
        """
        setIsOrtho(orthoState, useDist=None) -> self

        Switch the camera in and out of orthographic mode.  When the switch happens, the camera has to calculate a new fov or ortho width, each of which is based on the other and a set distance.  The caller can specify the distance; otherwise the center of interest is used.

        * orthoState (bool) - If True then the camera will be orthographic
        * useDist (float) - distance to use.
        """
        pass

    def setNearFarClippingPlanes(*args, **kwargs):
        """
        setNearFarClippingPlanes(near, far) -> self

        Set the distances to the Near and Far Clipping Planes.

        * near (float) - The near clipping plane value to be set
        * far (float) - The far clipping plane value to be set
        """
        pass

    def setVerticalFieldOfView(*args, **kwargs):
        """
        setVerticalFieldOfView(fov) -> self

        Sets the vertical field of view for the camera.

        * fov (float) - The vertical field of view value to be set
        """
        pass

    def upDirection(*args, **kwargs):
        """
        upDirection(space=kObject) -> MVector

        Returns the up direction vector for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    def verticalFieldOfView(*args, **kwargs):
        """
        verticalFieldOfView() -> float

        Returns the vertical field of view for the camera.
        """
        pass

    def viewDirection(*args, **kwargs):
        """
        viewDirection(space=kObject) -> MVector

        Returns the view direction for the camera

        * space (int) - Specifies the coordinate system for this operation
        """
        pass

    cameraScale = None

    centerOfInterest = None

    fStop = None

    farClippingPlane = None

    farFocusDistance = None

    filmFit = None

    filmFitOffset = None

    filmRollOrder = None

    filmRollValue = None

    filmTranslateH = None

    filmTranslateV = None

    focalLength = None

    focusDistance = None

    horizontalFilmAperture = None

    horizontalFilmOffset = None

    horizontalPan = None

    horizontalRollPivot = None

    horizontalShake = None

    isClippingPlanes = None

    isDepthOfField = None

    isDisplayFilmGate = None

    isDisplayGateMask = None

    isMotionBlur = None

    isVerticalLock = None

    kFillFilmFit = 0

    kHorizontalFilmFit = 1

    kInvalid = 4

    kOverscanFilmFit = 3

    kRotateTranslate = 0

    kTranslateRotate = 1

    kVerticalFilmFit = 2

    lensSqueezeRatio = None

    nearClippingPlane = None

    nearFocusDistance = None

    orthoWidth = None

    overscan = None

    panZoomEnabled = None

    postScale = None

    preScale = None

    renderPanZoom = None

    shakeEnabled = None

    shakeOverscan = None

    shakeOverscanEnabled = None

    shutterAngle = None

    stereoHIT = None

    stereoHITEnabled = None

    tumblePivot = None

    usePivotAsLocalSpace = None

    verticalFilmAperture = None

    verticalFilmOffset = None

    verticalPan = None

    verticalRollPivot = None

    verticalShake = None

    zoom = None


class MFnMesh(MFnDagNode):
    """
    Function set for operation on meshes (polygonal surfaces).

    __init__()
    Initializes a new, empty MFnMesh object.

    __init__(MDagPath path)
    Initializes a new MFnMesh object and attaches it to the DAG path
    of a mesh node.

    __init__(MObject nodeOrData)
    Initializes a new MFnMesh object and attaches it to a mesh
    node or mesh data object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def addHoles(*args, **kwargs):
        """
        addHoles(faceIndex, vertices, loopCounts, mergeVertices=True, pointTolerance=kPointTolerance) -> self

        Adds holes to a mesh polygon.
        loopCounts is an array of vertex counts.
        The first entry gives the count of vertices that make up the
        first hole to add to the polygon (using that many entries in vertexArray). The following
        entries in loopCounts give the count of vertices that make up each remaining hole,
        using the following entries in vertexArray.
        Therefore the sum of the entries of loopCounts should equal the total
        length of vertexArray.
        Note that holes should normally be specified with the opposite winding order
        to the exterior polygon.
        """
        pass

    def addPolygon(*args, **kwargs):
        """
        addPolygon(vertices, mergeVertices=True, pointTolerance=kPointTolerance, loopCounts=None) -> faceId

        Adds a new polygon to the mesh, returning the index of the new
        polygon. If mergeVertices is True and a new vertex is within
        pointTolerance of an existing one, then they are 'merged' by reusing
        the existing vertex and discarding the new one.

        loopCounts allows for polygons with holes. If supplied, it is an array of integer vertex
        counts. The first entry gives the count of vertices that make up the
        exterior of the polygon (using that many entries in vertexArray). The following
        entries in loopCounts give the count of vertices that make up each hole,
        using the following entries in vertexArray.
        Therefore the sum of the entries of loopCounts should equal the total
        length of vertexArray.
        Note that holes should normally be specified with the opposite winding order
        to the exterior polygon.
        """
        pass

    def allIntersections(*args, **kwargs):
        """
        allIntersections(raySource, rayDirection, space, maxParam,
            testBothDirections, faceIds=None, triIds=None, idsSorted=False,
            accelParams=None, tolerance=kIntersectTolerance, sortHits=False)
          -> (hitPoints, hitRayParams, hitFaces, hitTriangles, hitBary1s, hitBary2s)

        Finds all intersection of a ray starting at raySource and travelling
        in rayDirection with the mesh.

        If faceIds is specified, then only those faces will be considered
        for intersection. If both faceIds and triIds are given, then the
        triIds will be interpreted as face-relative and each pair of entries
        will be taken as a (face, triangle) pair to be considered for
        intersection. Thus, the face-triangle pair (10, 0) means the first
        triangle on face 10. If neither faceIds nor triIds is given, then
        all face-triangles in the mesh will be considered.

        The maxParam and testBothDirections flags can be used to control the
        radius of the search around the raySource point.

        The search proceeds by testing all applicable face-triangles looking
        for intersections. If the accelParams parameter is given then the
        mesh builds an intersection acceleration structure based on it. This
        acceleration structure is used to speed up the intersection
        operation, sometimes by a factor of several hundred over the non-
        accelerated case. Once created, the acceleration structure is cached
        and will be reused the next time this method (or anyIntersection()
        or allIntersections()) is called with an identically-configured
        MMeshIsectAccelParams object. If a different MMeshIsectAccelParams
        object is used, then the acceleration structure will be deleted and
        re-created according to the new settings. Once created, the
        acceleration structure will persist until either the object is
        destroyed (or rebuilt by a construction history operation), or the
        freeCachedIntersectionAccelerator() method is called. The
        cachedIntersectionAcceleratorInfo() and
        globalIntersectionAcceleratorsInfo() methods provide useful
        information about the resource usage of individual acceleration
        structures, and of all such structures in the system.
        If the ray hits the mesh, the details of the intersection points
        will be returned as a tuple containing the following:
        * hitPoints (MFloatPointArray) - coordinates of the points hit, in
          the space specified by the caller.* hitRayParams (MFloatArray) - parametric distances along the ray to
          the points hit.* hitFaces (MIntArray) - IDs of the faces hit
        * hitTriangles (MIntArray) - face-relative IDs of the triangles hit
        * hitBary1s (MFloatArray) - first barycentric coordinate of the
          points hit. If the vertices of the hitTriangle are (v1, v2, v3)
          then the barycentric coordinates are such that the hitPoint =
          (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3.* hitBary2s (MFloatArray) - second barycentric coordinate of the
          points hit.
        If no point was hit then the arrays will all be empty.
        """
        pass

    def anyIntersection(*args, **kwargs):
        """
        anyIntersection(raySource, rayDirection, space, maxParam,
            testBothDirections, faceIds=None, triIds=None, idsSorted=False,
            accelParams=None, tolerance=kIntersectTolerance)
          -> (hitPoint, hitRayParam, hitFace, hitTriangle, hitBary1, hitBary2)

        Finds any intersection of a ray starting at raySource and travelling
        in rayDirection with the mesh.

        If faceIds is specified, then only those faces will be considered
        for intersection. If both faceIds and triIds are given, then the
        triIds will be interpreted as face-relative and each pair of entries
        will be taken as a (face, triangle) pair to be considered for
        intersection. Thus, the face-triangle pair (10, 0) means the first
        triangle on face 10. If neither faceIds nor triIds is given, then
        all face-triangles in the mesh will be considered.

        The maxParam and testBothDirections flags can be used to control the
        radius of the search around the raySource point.

        The search proceeds by testing all applicable face-triangles looking
        for intersections. If the accelParams parameter is given then the
        mesh builds an intersection acceleration structure based on it. This
        acceleration structure is used to speed up the intersection
        operation, sometimes by a factor of several hundred over the non-
        accelerated case. Once created, the acceleration structure is cached
        and will be reused the next time this method (or anyIntersection()
        or allIntersections()) is called with an identically-configured
        MMeshIsectAccelParams object. If a different MMeshIsectAccelParams
        object is used, then the acceleration structure will be deleted and
        re-created according to the new settings. Once created, the
        acceleration structure will persist until either the object is
        destroyed (or rebuilt by a construction history operation), or the
        freeCachedIntersectionAccelerator() method is called. The
        cachedIntersectionAcceleratorInfo() and
        globalIntersectionAcceleratorsInfo() methods provide useful
        information about the resource usage of individual acceleration
        structures, and of all such structures in the system.
        If the ray hits the mesh, the details of the intersection point
        will be returned as a tuple containing the following:
        * hitPoint (MFloatPoint) - coordinates of the point hit, in
          the space specified by the caller.* hitRayParam (float) - parametric distance along the ray to
          the point hit.* hitFace (int) - ID of the face hit
        * hitTriangle (int) - face-relative ID of the triangle hit
        * hitBary1 (float) - first barycentric coordinate of the
          point hit. If the vertices of the hitTriangle are (v1, v2, v3)
          then the barycentric coordinates are such that the hitPoint =
          (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3.* hitBary2 (float) - second barycentric coordinate of the point hit.
        If no point was hit then the arrays will all be empty.
        """
        pass

    def assignColor(*args, **kwargs):
        """
        assignColor(faceId, vertexIndex, colorId, colorSet='') -> self

        Assigns a color from a colorSet to a specified vertex of a face.
        """
        pass

    def assignColors(*args, **kwargs):
        """
        assignColors(colorIds, colorSet=') -> self

        Assigns colors to all of the mesh's face-vertices. The colorIds
        sequence must contain an entry for every vertex of every face, in
        face order, meaning that the entries for all the vertices of face 0
        come first, followed by the entries for the vertices of face 1, etc.
        """
        pass

    def assignUV(*args, **kwargs):
        """
        assignUV(faceId, vertexIndex, uvId, uvSet='') -> self

        Assigns a UV coordinate from a uvSet to a specified vertex of a face.
        """
        pass

    def assignUVs(*args, **kwargs):
        """
        assignUVs(uvCounts, uvIds, uvSet='') -> self

        Assigns UV coordinates to the mesh's face-vertices.

        uvCounts contains the number of UVs to assign for each of the mesh's
        faces. That number must equal the number of vertices in the
        corresponding face or be 0 to indicate that no UVs will be assigned
        to that face.
        """
        pass

    def booleanOp(*args, **kwargs):
        """
        (Deprecated: Please use booleanOps instead) booleanOp(Boolean Operation constant, MFnMesh, MFnMesh) -> self

        Replaces this mesh's geometry with the result of a boolean operation
        on the two specified meshes.
        """
        pass

    def booleanOps(*args, **kwargs):
        """
        booleanOps(Boolean Operation constant, MObjectArray, bool) -> self

        Replaces this mesh's geometry with the result of a boolean operation
        on the specified meshes.
        """
        pass

    def cachedIntersectionAcceleratorInfo(*args, **kwargs):
        """
        cachedIntersectionAcceleratorInfo() -> string

        Retrieves a string that describes the intersection acceleration
        structure for this object, if any. The string will be of the
        following form:

          10x10x10 uniform grid, (build time 0.5s), (memory footprint 2000KB)

        It describes the configuration of the cached intersection
        accelerator, as well as how long it took to build it, and how much
        memory it is currently occupying. If the mesh has no cached
        intersection accelerator, the empty string is returned.
        """
        pass

    def cleanupEdgeSmoothing(*args, **kwargs):
        """
        cleanupEdgeSmoothing() -> self

        Updates the mesh after setEdgeSmoothing has been done. This should
        be called only once, after all the desired edges have been had their
        smoothing set. If you don't call this method, the normals may not be
        correct, and the object will look odd in shaded mode.
        """
        pass

    def clearBlindData(*args, **kwargs):
        """
        clearBlindData(compType) -> self
        clearBlindData(compType, blindDataId, compId=None, attr='') -> self


        The first version deletes all blind data from all the mesh's
        components of the given type (an MFn Type constant).

        The second version deletes values of the specified blind data type
        from the mesh's components of a given type. If a component ID is
        provided then the data is only deleted from that component,
        otherwise it is deleted from all of the mesh's components of the
        specified type. If a blind data attribute name is provided then only
        data for that attribute is deleted, otherwise data for all of the
        blind data type's attributes is deleted.
        """
        pass

    def clearColors(*args, **kwargs):
        """
        clearColors(colorSet='') -> self

        Clears out all colors from a colorSet, and leaves behind an empty
        colorset. This method should be used if it is needed to shrink the
        actual size of the color set. In this case, the user should call
        clearColors(), setColors() and then assignColors() to rebuild the
        mapping info.

        When called on mesh data, the colors are removed. When called on a
        shape with no history, the colors are removed and the attributes are
        set on the shape. When called on a shape with history, the
        polyColorDel command is invoked and a polyColorDel node is created.

        If no colorSet is specified the mesh's current color set will be used.
        """
        pass

    def clearUVs(*args, **kwargs):
        """
        clearUVs(uvSet='') -> self

        Clears out all uvs from a uvSet, and leaves behind an empty
        uvset. This method should be used if it is needed to shrink the
        actual size of the uv set. In this case, the user should call
        clearUVs(), setUVs() and then assignUVs() to rebuild the
        mapping info.

        When called on mesh data, the uvs are removed. When called on a
        shape with no history, the uvs are removed and the attributes are
        set on the shape. When called on a shape with history, the
        polyMapDel command is invoked and a polyMapDel node is created.

        If no uvSet is specified the mesh's current uv set will be used.
        """
        pass

    def closestIntersection(*args, **kwargs):
        """
        closestIntersection(raySource, rayDirection, space, maxParam,
            testBothDirections, faceIds=None, triIds=None, idsSorted=False,
            accelParams=None, tolerance=kIntersectTolerance)
          -> (hitPoint, hitRayParam, hitFace, hitTriangle, hitBary1, hitBary2)

        Finds the closest intersection of a ray starting at raySource and
        travelling in rayDirection with the mesh.

        If faceIds is specified, then only those faces will be considered
        for intersection. If both faceIds and triIds are given, then the
        triIds will be interpreted as face-relative and each pair of entries
        will be taken as a (face, triangle) pair to be considered for
        intersection. Thus, the face-triangle pair (10, 0) means the first
        triangle on face 10. If neither faceIds nor triIds is given, then
        all face-triangles in the mesh will be considered.

        The maxParam and testBothDirections flags can be used to control the
        radius of the search around the raySource point.

        The search proceeds by testing all applicable face-triangles looking
        for intersections. If the accelParams parameter is given then the
        mesh builds an intersection acceleration structure based on it. This
        acceleration structure is used to speed up the intersection
        operation, sometimes by a factor of several hundred over the non-
        accelerated case. Once created, the acceleration structure is cached
        and will be reused the next time this method (or anyIntersection()
        or allIntersections()) is called with an identically-configured
        MMeshIsectAccelParams object. If a different MMeshIsectAccelParams
        object is used, then the acceleration structure will be deleted and
        re-created according to the new settings. Once created, the
        acceleration structure will persist until either the object is
        destroyed (or rebuilt by a construction history operation), or the
        freeCachedIntersectionAccelerator() method is called. The
        cachedIntersectionAcceleratorInfo() and
        globalIntersectionAcceleratorsInfo() methods provide useful
        information about the resource usage of individual acceleration
        structures, and of all such structures in the system.
        If the ray hits the mesh, the details of the intersection point
        will be returned as a tuple containing the following:
        * hitPoint (MFloatPoint) - coordinates of the point hit, in
          the space specified by the caller.* hitRayParam (float) - parametric distance along the ray to
          the point hit.* hitFace (int) - ID of the face hit
        * hitTriangle (int) - face-relative ID of the triangle hit
        * hitBary1 (float) - first barycentric coordinate of the
          point hit. If the vertices of the hitTriangle are (v1, v2, v3)
          then the barycentric coordinates are such that the hitPoint =
          (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3.* hitBary2 (float) - second barycentric coordinate of the point hit.
        If no point was hit then the arrays will all be empty.
        """
        pass

    def collapseEdges(*args, **kwargs):
        """
        collapseEdges(seq of int) -> self

        Collapses edges into vertices. The two vertices that create each
        given edge are replaced in turn by one vertex placed at the average
        of the two initial vertex.
        """
        pass

    def collapseFaces(*args, **kwargs):
        """
        collapseFaces(seq of int) -> self

        Collapses faces into vertices. Adjacent faces will be collapsed
        together into a single vertex. Non-adjacent faces will be collapsed
        into their own, separate vertices.
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(MObject, parent=kNullObj) -> MObject

        Creates a new mesh with the same geometry as the source. Raises
        TypeError if the source is not a mesh node or mesh data object or it
        contains an empty mesh.

        If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create())
        then a mesh data object will be created and returned and the wrapper
        will be set to reference it.

        If the parent is a transform type node then a mesh node will be
        created and parented beneath it and the return value will be the
        mesh node.

        If the parent is any other type of node a TypeError will be raised.

        If no parent is provided then a transform node will be created and
        returned and a mesh node will be created and parented under the
        transform.
        """
        pass

    def copyInPlace(*args, **kwargs):
        """
        copyInPlace(MObject) -> self

        Replaces the current mesh's geometry with that from the source.
        Raises TypeError if the source is not a mesh node or mesh data
        object or it contains an empty mesh.
        """
        pass

    def copyUVSet(*args, **kwargs):
        """
        copyUVSet(fromName, toName, modifier=None) -> string

        Copies the contents of one UV set into another.

        If the source UV set does not exist, or if it has the same name as
        the destination, then no copy will be made.

        If the destination UV set exists then its contents will be replace
        by a copy of the source UV set.

        If the destination UV set does not exist then a new UV set will be
        created and the source UV set will be copied into it. The name of
        the UV set will be that provided with a number appended to the end
        to ensure uniqueness.
        The final name of the destination UV set will be returned.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
        pass

    def create(*args, **kwargs):
        """
        create(vertices, polygonCounts, polygonConnects, uValues=None, vValues=None, parent=kNullObj) -> MObject
        create(vertices, edges, edgeConnectsCount, edgeFaceConnects, edgeFaceDesc, storeDoubles=False, parent=kNullObj) -> MObject

        Creates a new polygonal mesh and sets this function set to operate
        on it. This method is meant to be as efficient as possible and thus
        assumes that all the given data is topologically correct.
        If UV values are supplied both parameters must be given and they
        must contain the same number of values, otherwise IndexError will be
        raised. Note that the UVs are simply stored in the mesh, not
        assigned to any vertices. To assign them use assignUVs().
        If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create())
        then a mesh data object will be created and returned and the wrapper
        will be set to reference it.
        If the parent is a transform type node then a mesh node will be
        created and parented beneath it and the return value will be the
        mesh node.
        If the parent is any other type of node a TypeError will be raised.

        If no parent is provided then a transform node will be created and
        returned and a mesh node will be created and parented under the
        transform.
        """
        pass

    def createBlindDataType(*args, **kwargs):
        """
        createBlindDataType(blindDataId, ((longName, shortName, typeName), ...)) -> self

        Create a new blind data type with the specified attributes.

        Each element of the attrs sequence is a tuple containing the long
        name, short name and type name of the attribute. Valid type names
        are 'int', 'float', 'double', 'boolean', 'string' or 'binary'.

        Raises RuntimeError if the blind data id is already in use or an
        invalid format was specified.
        """
        pass

    def createColorSet(*args, **kwargs):
        """
        createColorSet(name, clamped, rep=kRGBA, modifier=None, instances=None) -> string

        Creates a new, empty color set for this mesh.

        If no name is provided 'colorSet#' will be used, where # is a number
        that makes the name unique for this mesh. If a name is provided but
        it conflicts with that of an existing color set then a number will
        be appended to the proposed name to make it unique.
        The return value is the final name used for the new color set.

        This method will only work when the functionset is attached to a
        mesh node, not mesh data.
        """
        pass

    def createInPlace(*args, **kwargs):
        """
        createInPlace(vertices, polygonCounts, polygonConnects) -> self

        Replaces the existing polygonal mesh with a new one. This method is
        meant to be as efficient as possible and thus assumes that all the
        given data is topologically correct.

        The vertices may be given as a sequence of MFloatPoint's or a
        sequence of MPoint's, but not a mix of the two.
        """
        pass

    def createUVSet(*args, **kwargs):
        """
        createUVSet(name, modifier=None, instances=None) -> string

        Creates a new, empty UV set for this mesh.

        If a UV set with proposed name already exists then a number will be
        appended to the proposed name to name it unique.

        If the proposed name is empty then a name of the form uvSet# will be
        used where '#' is a number chosen to ensure that the name is unique.

        The name used for the UV set will be returned.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
        pass

    def currentColorSetName(*args, **kwargs):
        """
        currentColorSetName(instance=kInstanceUnspecified) -> string

        Get the name of the 'current' color set. The current color set is
        the one used for color operations when no color set is explicitly
        specified.
        On instanced meshes, color sets may be applied on a per-instance
        basis or may be shared across all instances. When the color sets are
        per-instance, the concept of the current color set has two levels of
        granularity. Namely, the current color set applies to one or more
        instances, plus there are other color sets in the same color set
        family that apply to different instances. The instance arguement is
        used to indicate that if this is a per-instance color set, you are
        interested in the name of the color set that applies to the
        specified instance. When the index is not specified, the current
        color set will be returned regardless of which instance it is for.
        If there is no current color set, then an empty string will be
        returned.
        """
        pass

    def currentUVSetName(*args, **kwargs):
        """
        currentUVSetName(instance=kInstanceUnspecified) -> string

        Get the name of the 'current' uv set. The current uv set is
        the one used for uv operations when no uv set is explicitly
        specified.
        On instanced meshes, uv sets may be applied on a per-instance
        basis or may be shared across all instances. When the uv sets are
        per-instance, the concept of the current uv set has two levels of
        granularity. Namely, the current uv set applies to one or more
        instances, plus there are other uv sets in the same uv set
        family that apply to different instances. The instance arguement is
        used to indicate that if this is a per-instance uv set, you are
        interested in the name of the uv set that applies to the
        specified instance. When the index is not specified, the current
        uv set will be returned regardless of which instance it is for.
        If there is no current uv set, then an empty string will be
        returned.
        """
        pass

    def deleteColorSet(*args, **kwargs):
        """
        deleteColorSet(colorSet, modifier=None, currentSelection=None) -> self

        Deletes a color set from the mesh.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
        pass

    def deleteEdge(*args, **kwargs):
        """
        deleteEdge(edgeId, modifier=None) -> self

        Deletes the specified edge.
        """
        pass

    def deleteFace(*args, **kwargs):
        """
        deleteFace(faceId, modifier=None) -> self

        Deletes the specified face.
        """
        pass

    def deleteUVSet(*args, **kwargs):
        """
        deleteUVSet(uvSet, modifier=None, currentSelection=None) -> self

        Deletes a uv set from the mesh.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
        pass

    def deleteVertex(*args, **kwargs):
        """
        deleteVertex(vertexId, modifier=None) -> self

        Deletes the specified vertex.
        """
        pass

    def duplicateFaces(*args, **kwargs):
        """
        duplicateFaces(faces, translation=None) -> self

        Duplicates a set of faces and detaches them from the rest of the
        mesh. The resulting mesh will contain one more independant piece of
        geometry.
        """
        pass

    def extractFaces(*args, **kwargs):
        """
        extractFaces(faces, translation=None) -> self

        Detaches a set of faces from the rest of the mesh. The resulting
        mesh will contain one more independant piece of geometry.
        """
        pass

    def extrudeEdges(*args, **kwargs):
        """
        extrudeEdges(edges, extrusionCount=1, translation=None, extrudeTogether=True, thickness=0.0, offset=0.0) -> self

        Extrude the given edges along a vector. The resulting mesh will have
        extra parallelograms coming out of the given edges and going to the
        new extruded edges. The length of the new polygon is determined by
        the length of the vector. The extrusionCount parameter is the number
        of subsequent extrusions per edges and represents the number of
        polygons that will be created from each given edge to the extruded
        edges.
        The difference between using thickness or offset instead of providing
        a vector with the translation variable is that the translation will
        be applied to each vertex in the extrusion along its local direction.  This
        can result in vertices being moved the same distance, but the angles between
        the original components are not maintained so the overall shape is not the
        same.
        Both the thickness and offset variables will attempt to move the components
        a distance that will maintain angles between edges at the border of the
        extrusion.
        """
        pass

    def extrudeFaces(*args, **kwargs):
        """
        extrudeFaces(faces, extrusionCount=1, translation=None, extrudeTogether=True, thickness=0.0, offset=0.0) -> self

        Extrude the given faces along a vector. The resulting mesh will have
        extra parallelograms coming out of the given faces and going to the
        new extruded faces. The length of the new polygon is determined by
        the length of the vector. The extrusionCount parameter is the number
        of subsequent extrusions per faces and represents the number of
        polygons that will be created from each given face to the extruded
        faces.
        The difference between using thickness or offset instead of providing
        a vector with the translation variable is that the translation will
        be applied to each vertex in the extrusion along its local direction.  This
        can result in vertices being moved the same distance, but the angles between
        the original components are not maintained so the overall shape is not the
        same.
        Both the thickness and offset variables will attempt to move the components
        a distance that will maintain angles between edges at the border of the
        extrusion.
        """
        pass

    def freeCachedIntersectionAccelerator(*args, **kwargs):
        """
        freeCachedIntersectionAccelerator() -> self

        If the mesh has a cached intersection accelerator structure, then
        this routine forces it to be deleted. Ordinarily, these structures
        are cached so that series of calls to the closestIntersection(),
        allIntersections(), and anyIntersection() methods can reuse the same
        structure. Once the client is finished with these intersection
        operations, however, they are responsible for freeing the acceleration
        structure, which is what this method does.
        """
        pass

    def generateSmoothMesh(*args, **kwargs):
        """
        generateSmoothMesh(parent=kNullObj, options=None) -> MObject

        Creates a new polygonal mesh which is a smoothed version of the one
        to which the functionset is attached. If an options object is supplied
        it will be used to direct the smoothing operation, otherwise the
        mesh's Smooth Mesh Preview attributes will be used.

        If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create())
        then a mesh data object will be created and returned.
        If the parent is a transform type node then a mesh node will be
        created and parented beneath it and the return value will be the
        mesh node.
        If the parent is any other type of node a TypeError will be raised.

        If no parent is provided then a transform node will be created and
        returned and a mesh node will be created and parented under the
        transform.

        Note that, unlike the create functions, this function does not set
        the functionset to operate on the new mesh, but leaves it attached
        to the original mesh.
        """
        pass

    def getAssignedUVs(*args, **kwargs):
        """
        getAssignedUVs(uvSet='') -> (counts, uvIds)

        Returns a tuple containing all of the UV assignments for the specified
        UV set. The first element of the tuple is an array of counts giving
        the number of UVs assigned to each face of the mesh. The count will
        either be zero, indicating that that face's vertices do not have UVs
        assigned, or else it will equal the number of the face's vertices.
        The second element of the tuple is an array of UV IDs for all of the
        face-vertices which have UVs assigned.
        """
        pass

    def getAssociatedColorSetInstances(*args, **kwargs):
        """
        getAssociatedColorSetInstances(colorSet) -> MIntArray

        Returns the instance numbers associated with the specified Color set.
        If the color map is shared across all instances, an empty array will
        be returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
        pass

    def getAssociatedUVSetInstances(*args, **kwargs):
        """
        getAssociatedUVSetInstances(uvSet) -> MIntArray

        Returns the instance numbers associated with the specified UV set.
        If the uv map is shared across all instances, an empty array will be
        returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
        pass

    def getAssociatedUVSetTextures(*args, **kwargs):
        """
        getAssociatedUVSetTextures(uvSet) -> MObjectArray

        Returns the texture nodes which are using the specified UV set. If
        the texture has a 2d texture placement, the texture, and not the
        placement will be returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
        pass

    def getBinaryBlindData(*args, **kwargs):
        """
        getBinaryBlindData(compId, compType, blindDataId, attr) -> string
        getBinaryBlindData(compType, blindDataId, attr)
          -> (MIntArray, [string, string, ...])

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of 'binary'
        type.
        """
        pass

    def getBinormals(*args, **kwargs):
        """
        getBinormals(space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns the binormal vectors for all face-vertices.

        This method is not threadsafe.
        """
        pass

    def getBlindDataAttrNames(*args, **kwargs):
        """
        getBlindDataAttrNames(blindDataId) -> ((longName, shortName, typeName), ...)

        Returns a tuple listing the attributes of the given blind data type.
        Each element of the tuple is itself a tuple containing the long
        name, short name and type name of the attribute. Type names can be
        'int', 'float', 'double', 'boolean', 'string' or 'binary'.
        """
        pass

    def getBlindDataTypes(*args, **kwargs):
        """
        getBlindDataTypes(MFn Type constant) -> MIntArray

        Returns all the blind data ID's associated with the given component
        type on this mesh.
        """
        pass

    def getBoolBlindData(*args, **kwargs):
        """
        getBoolBlindData(compId, compType, blindDataId, attr) -> bool
        getBoolBlindData(compType, blindDataId, attr) -> (MIntArray, MIntArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'boolean' type.
        """
        pass

    def getClosestNormal(*args, **kwargs):
        """
        getClosestNormal(MPoint, space=MSpace.kObject) -> (MVector, int)

        Returns a tuple containing the normal at the closest point on the
        mesh to the given point and the ID of the face in which that closest
        point lies.
        """
        pass

    def getClosestPoint(*args, **kwargs):
        """
        getClosestPoint(MPoint, space=MSpace.kObject) -> (MPoint, int)

        Returns a tuple containing the closest point on the mesh to the
        given point and the ID of the face in which that closest point lies.

        This method is not threadsafe.
        """
        pass

    def getClosestPointAndNormal(*args, **kwargs):
        """
        getClosestPointAndNormal(MPoint, space=MSpace.kObject)
          -> (MPoint, MVector, int)

        Returns a tuple containing the closest point on the mesh to the
        given point, the normal at that point, and the ID of the face in
        which that point lies.

        This method is not threadsafe.
        """
        pass

    def getClosestUVs(*args, **kwargs):
        """
        getClosestUVs(u, v, uvSet='') -> MIntArray

        Returns the IDs of the UVs which are nearest in uv space to the
        given texture coordinate in the specified UV set. All these UVs
        locate at the same distance to the given coordinate.
        """
        pass

    def getColor(*args, **kwargs):
        """
        getColor(colorId, colorSet='') -> MColor

        Returns a color from a colorSet. Raises IndexError if the colorId is
        out of range.
        """
        pass

    def getColorIndex(*args, **kwargs):
        """
        getColorIndex(faceId, localVertexId, colorSet='') -> int

        Returns the index into the specified colorSet of the color used by a
        specific face-vertex. This can be used to index into the sequence
        returned by getColors().
        """
        pass

    def getColorRepresentation(*args, **kwargs):
        """
        getColorRepresentation(colorSet) -> Color Representation constant

        Returns the Color Representation used by the specified color set.
        """
        pass

    def getColorSetFamilyNames(*args, **kwargs):
        """
        getColorSetFamilyNames() -> (string, ...)

        Returns the names of all of the color set families on this object. A
        color set family is a set of per-instance sets with the same name
        with each individual set applying to one or more instances. A set
        which is shared across all instances will be the sole member of its
        family.

        Given a color set family name, getColorSetsInFamily() may be used to
        determine the names of the associated individual sets.
        """
        pass

    def getColorSetNames(*args, **kwargs):
        """
        getColorSetNames() -> (string, ...)

        Returns the names of all the color sets on this object.
        """
        pass

    def getColorSetsInFamily(*args, **kwargs):
        """
        getColorSetsInFamily(familyName) -> (string, ...)

        Returns the names of all of the color sets that belong to the
        specified family. Per-instance sets will have multiple sets in a
        family, with each individual set applying to one or more instances.
        A set which is shared across all instances will be the sole member
        of its family and will share the same name as its family.
        """
        pass

    def getColors(*args, **kwargs):
        """
        getColors(colorSet='') -> MColorArray

        Returns all of the colors in a colorSet. If no colorSet is specified
        then the default colorSet is used.

        Use the index returned by getColorIndex() to access the returned
        array.
        """
        pass

    def getConnectedShaders(*args, **kwargs):
        """
        getConnectedShaders(instance) -> (MObjectArray, MIntArray)

        Returns a tuple containing an array of shaders (sets) and an array
        of ints mapping the mesh's polygons onto those shaders. For each
        polygon in the mesh there will be corresponding value in the second
        array. If it is -1 that means that the polygon is not assigned to a
        shader, otherwise it indicates the index into the first array of the
        shader to which that polygon is assigned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
        pass

    def getCreaseEdges(*args, **kwargs):
        """
        getCreaseEdges() -> (MUintArray, MDoubleArray)

        Returns a tuple containing two arrays. The first contains the mesh-
        relative/global IDs of the mesh's creased edges and the second
        contains the associated crease data.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned
        by Pixar(R).
        """
        pass

    def getCreaseVertices(*args, **kwargs):
        """
        getCreaseVertices() -> (MUintArray, MDoubleArray)

        Returns a tuple containing two arrays. The first contains the mesh-
        relative/global IDs of the mesh's creased vertices and the second
        contains the associated crease data.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned
        by Pixar(R).
        """
        pass

    def getDoubleBlindData(*args, **kwargs):
        """
        getDoubleBlindData(compId, compType, blindDataId, attr) -> float
        getDoubleBlindData(compType, blindDataId, attr) -> (MIntArray, MDoubleArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'double' type.
        """
        pass

    def getEdgeVertices(*args, **kwargs):
        """
        getEdgeVertices(edgeId) -> (int, int)

        Returns a tuple containing the mesh-relative/global IDs of the
        edge's two vertices. The indices can be used to refer to the
        elements in the array returned by the getPoints() method.
        """
        pass

    def getFaceAndVertexIndices(*args, **kwargs):
        """
        getFaceAndVertexIndices(faceVertexIndex, localVertex=True) -> (int, int)

        Returns a tuple containg the faceId and vertexIndex represented by
        the given face-vertex index. This is the reverse of the operation
        performed by getFaceVertexIndex().

        If localVertex is True then the returned vertexIndex is the face-
        relative/local index, otherwise it is the mesh-relative/global index.
        """
        pass

    def getFaceNormalIds(*args, **kwargs):
        """
        getFaceNormalIds(faceId) -> MIntArray

        Returns the IDs of the normals for all the vertices of a given face.
        These IDs can be used to index into the arrays returned by getNormals().
        """
        pass

    def getFaceUVSetNames(*args, **kwargs):
        """
        getFaceUVSetNames(faceId) -> (string, ...)

        Returns the names of all of the uv sets mapped to the specified face.

        This method is not threadsafe.
        """
        pass

    def getFaceVertexBinormal(*args, **kwargs):
        """
        getFaceVertexBinormal(faceId, vertexId, space=MSpace.kObject, uvSet='') -> MVector

        Returns the binormal vector at a given face vertex.

        This method is not threadsafe.
        """
        pass

    def getFaceVertexBinormals(*args, **kwargs):
        """
        getFaceVertexBinormals(faceId, space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns all the per-vertex-per-face binormals for a given face.

        This method is not threadsafe.
        """
        pass

    def getFaceVertexColors(*args, **kwargs):
        """
        getFaceVertexColors(colorSet='', defaultUnsetColor=None) -> MColorArray

        Returns colors for all the mesh's face-vertices.

        The colors are returned in face order: e.g. F0V0, F0V1.. F0Vn, F1V0,
        etc... Use the index returned by getFaceVertexIndex() if you wish to
        index directly into the returned color array.

        If no face has color for that vertex, the entry returned will be
        defaultUnsetColor. If a color was set for some but not all the faces
        for that vertex, the ones where the color has not been explicitly set
        will return (0,0,0). If a vertex has shared color, the same value
        will be set for all its vertes/faces.

        If the colorSet is not specified, the default color set will be used.
        If the defaultUnsetColor is not given, then (-1, -1, -1, -1) will be
        used.
        """
        pass

    def getFaceVertexIndex(*args, **kwargs):
        """
        getFaceVertexIndex(faceId, vertexIndex, localVertex=True) -> int

        Returns the index for a specific face-vertex into an array of face-
        vertex values, such as those returned by getFaceVertexBinormals(),
        getFaceVertexColors(), getFaceVertexNormals(), etc.

        The values in the target arrays are presumed to be in face order:
        F0V0, F0V1.. F0Vn, F1V0, etc...
        If localVertex is True then vertexIndex must be a face-relative/local
        index. If localVertex is False then vertexIndex must be a mesh-
        relative/global index.

        The opposite operation is performed by the getFaceAndVertexIndices()
        method.
        """
        pass

    def getFaceVertexNormal(*args, **kwargs):
        """
        getFaceVertexNormal(faceId, vertexId, space=MSpace.kObject) -> MVector

        Returns the per-vertex-per-face normal for a given face and vertex.

        This method is not threadsafe.
        """
        pass

    def getFaceVertexNormals(*args, **kwargs):
        """
        getFaceVertexNormals(faceId, space=MSpace.kObject) -> MFloatVectorArray

        Returns the normals for a given face.

        This method is not threadsafe.
        """
        pass

    def getFaceVertexTangent(*args, **kwargs):
        """
        getFaceVertexTangent(faceId, vertexId, space=MSpace.kObject, uvSet='') -> MVector

        Return the normalized tangent vector at a given face vertex.

        The tangent is defined as the surface tangent of the polygon running
        in the U direction defined by the uv map.
        This method is not threadsafe.
        """
        pass

    def getFaceVertexTangents(*args, **kwargs):
        """
        getFaceVertexTangents(faceId, space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns all the per-vertex-per-face tangents for a given face.

        The tangent is defined as the surface tangent of the polygon running
        in the U direction defined by the uv map.

        This method is not threadsafe.
        """
        pass

    def getFloatBlindData(*args, **kwargs):
        """
        getFloatBlindData(compId, compType, blindDataId, attr) -> float
        getFloatBlindData(compType, blindDataId, attr) -> (MIntArray, MFloatArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'float' type.
        """
        pass

    def getFloatPoints(*args, **kwargs):
        """
        getFloatPoints(space=MSpace.kObject) -> MFloatPointArray

        Returns an MFloatPointArray containing the mesh's vertices.
        """
        pass

    def getHoles(*args, **kwargs):
        """
        getHoles() -> ((face, (v1, v2, ...)), (face, (v1, v2, ...)), ...)

        Returns a tuple describing the holes in the mesh. Each element of the
        tuple is itself a tuple. The first element of the sub-tuple is the
        integer ID of the face in which the hole occurs. The second element
        of the sub-tuple is another tuple containing the mesh-relative/global
        IDs of the vertices which make up the hole.

        Take the following return value as an example:

            ((3, (7, 2, 6)), (5, (11, 10, 3, 4)))

        This says that the mesh has two holes. The first hole is in face 3
        and consists of vertices 7, 2 and 6. The second hole is in face 5 and
        consists of vertices 11, 10, 3 and 4.
        """
        pass

    def getIntBlindData(*args, **kwargs):
        """
        getIntBlindData(compId, compType, blindDataId, attr) -> int
        getIntBlindData(compType, blindDataId, attr) -> (MIntArray, MIntArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'int' type.
        """
        pass

    def getInvisibleFaces(*args, **kwargs):
        """
        getInvisibleFaces() -> MUintArray

        Returns the invisible faces of the mesh. Invisible faces are like
        lightweight holes in that they are not rendered but do not require
        additional geometry the way that holes do. They have the advantage
        over holes that if the mesh is smoothed then their edges will be
        smoothed as well, while holes will retain their hard edges.

        Invisible faces can be set using the setInvisibleFaces() method or
        the polyHole command.
        """
        pass

    def getNormalIds(*args, **kwargs):
        """
        getNormalIds() -> (MIntArray, MIntArray)

        Returns the normal IDs for all of the mesh's polygons as a tuple of
        two int arrays. The first array contains the number of vertices for
        each polygon and the second contains the normal IDs for each polygon-
        vertex. These IDs can be used to index into the array returned by
        getNormals().
        """
        pass

    def getNormals(*args, **kwargs):
        """
        getNormals(space=MSpace.kObject) -> MFloatVectorArray

        Returns a copy of the mesh's normals. The normals are the per-polygon
        per-vertex normals. To find the normal for a particular vertex-face,
        use getFaceNormalIds() to get the index into the array.

        This method is not threadsafe.
        """
        pass

    def getPoint(*args, **kwargs):
        """
        getPoint(vertexId, space=MSpace.kObject) -> MPoint

        Returns the position of specified vertex.
        """
        pass

    def getPointAtUV(*args, **kwargs):
        """
        getPointAtUV(faceId, u, v, space=MSpace.kObject, uvSet='', tolerance=0.0) -> MPoint

        Returns the position of the point at the give UV value in the
        specified face.

        This method is not threadsafe.
        """
        pass

    def getPoints(*args, **kwargs):
        """
        getPoints(space=MSpace.kObject) -> MPointArray

        Returns a copy of the mesh's vertex positions as an MPointArray.
        """
        pass

    def getPointsAtUV(*args, **kwargs):
        """
        getPointsAtUV(u, v, space=MSpace.kObject, uvSet='', tolerance=0.0) -> MPoint

        Returns the position of the point at the give UV value
        """
        pass

    def getPolygonNormal(*args, **kwargs):
        """
        getPolygonNormal(polygonId, space=MSpace.kObject) -> MVector

        Returns the per-polygon normal for the given polygon.

        This method is not threadsafe.
        """
        pass

    def getPolygonTriangleVertices(*args, **kwargs):
        """
        getPolygonTriangleVertices(polygonId, triangleId) -> (int, int, int)

        Returns the mesh-relative/global IDs of the 3 vertices of the
        specified triangle of the specified polygon. These IDs can be used
        to index into the arrays returned by getPoints() and getFloatPoints().
        """
        pass

    def getPolygonUV(*args, **kwargs):
        """
        getPolygonUV(polygonId, vertexId, uvSet='') -> (float, float)

        Returns a tuple containing the U and V values at a specified vertex
        of a specified polygon.

        This method is not threadsafe.
        """
        pass

    def getPolygonUVid(*args, **kwargs):
        """
        getPolygonUVid(polygonId, vertexId, uvSet='') -> int

        Returns the ID of the UV at a specified vertex of a specified polygon.

        This method is not threadsafe.
        """
        pass

    def getPolygonVertices(*args, **kwargs):
        """
        getPolygonVertices(polygonId) -> MIntArray

        Returns the mesh-relative/global vertex IDs the specified polygon.
        These IDs can be used to index into the arrays returned by getPoints()
        and getFloatPoints().
        """
        pass

    def getSmoothMeshDisplayOptions(*args, **kwargs):
        """
        getSmoothMeshDisplayOptions() -> MMeshSmoothOptions

        Returns the options currently in use when smoothing the mesh for display.
        """
        pass

    def getStringBlindData(*args, **kwargs):
        """
        getStringBlindData(compId, compType, blindDataId, attr) -> string
        getStringBlindData(compType, blindDataId, attr)
          -> (MIntArray, [string, string, ...])

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of 'string'
        type.
        """
        pass

    def getTangentId(*args, **kwargs):
        """
        getTangentId(faceId, vertexId) -> int

        Returns the ID of the tangent for a given face and vertex.
        """
        pass

    def getTangents(*args, **kwargs):
        """
        getTangents(space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Return the tangent vectors for all face vertices. The tangent is
        defined as the surface tangent of the polygon running in the U
        direction defined by the uv map.

        This method is not threadsafe.
        """
        pass

    def getTriangleOffsets(*args, **kwargs):
        """
        getTriangleOffsets() -> (MIntArray, MIntArray)

        Returns the number of triangles for every polygon face and the
        offset into the vertex indices array for each triangle vertex (see getVertices()).
        The triangleVertices array holds each vertex for each triangle in sequence,
        so it has three times as many elements as there are triangles.
        (i.e. three times the sum of the elements of the triangleCounts array)
        """
        pass

    def getTriangles(*args, **kwargs):
        """
        getTriangles() -> (MIntArray, MIntArray)

        Returns a tuple describing the mesh's triangulation. The first
        element of the tuple is an array giving the number of triangles for
        each of the mesh's polygons. The second tuple gives the ids of the
        vertices of all the triangles.
        """
        pass

    def getUV(*args, **kwargs):
        """
        getUV(uvId, uvSet='') -> (float, float)

        Returns a tuple containing the u and v values of the specified UV.
        """
        pass

    def getUVAtPoint(*args, **kwargs):
        """
        getUVAtPoint(point, space=MSpace.kObject, uvSet='') -> (float, float, int)

        Returns a tuple containing the u and v coordinates of the point on
        the mesh closest to the given point, and the ID of the face
        containing that closest point.

        This method is not threadsafe.
        """
        pass

    def getUVSetFamilyNames(*args, **kwargs):
        """
        getUVSetFamilyNames() -> (string, ...)

        Returns the names of all of the uv set families on this object. A
        uv set family is a set of per-instance sets with the same name
        with each individual set applying to one or more instances. A set
        which is shared across all instances will be the sole member of its
        family.

        Given a uv set family name, getUVSetsInFamily() may be used to
        determine the names of the associated individual sets.
        """
        pass

    def getUVSetNames(*args, **kwargs):
        """
        getUVSetNames() -> (string, ...)

        Returns the names of all the uv sets on this object.
        """
        pass

    def getUVSetsInFamily(*args, **kwargs):
        """
        getUVSetsInFamily(familyName) -> (string, ...)

        Returns the names of all of the uv sets that belong to the
        specified family. Per-instance sets will have multiple sets in a
        family, with each individual set applying to one or more instances.
        A set which is shared across all instances will be the sole member
        of its family and will share the same name as its family.
        """
        pass

    def getUVs(*args, **kwargs):
        """
        getUVs(uvSet='') -> (MFloatArray, MFloatArray)

        Returns a tuple containing an array of U values and an array of V
        values, representing all of the UVs for the given UV set.
        """
        pass

    def getUvShellsIds(*args, **kwargs):
        """
        getUvShellsIds(uvSet='') -> (int, MIntArray)

        Returns a tuple containing describing how the specified UV set's UVs
        are grouped into shells. The first element of the tuple is the number
        of distinct shells. The second element of the tuple is an array of
        shell indices, one per uv, indicating which shell that uv is part of.
        """
        pass

    def getVertexColors(*args, **kwargs):
        """
        getVertexColors(colorSet='', defaultUnsetColor=None) -> MColorArray

        Gets colors for all vertices of the given colorSet. If no face has
        color for that vertex, the entry returned will be defaultUnsetColor.
        If a color was set for some or all the faces for that vertex, an
        average of those vertex/face values where the color has been set will
        be returned.

        If the colorSet is not specified, the default color set will be used.
        If the defaultUnsetColor is not given, then (-1, -1, -1, -1) will be
        used.
        """
        pass

    def getVertexNormal(*args, **kwargs):
        """
        getVertexNormal(vertexId, angleWeighted, space=MSpace.kObject) -> MVector

        Returns the normal at the given vertex. The returned normal is a
        single per-vertex normal, so unshared normals at a vertex will be
        averaged.

        If angleWeighted is set to true, the normals are computed by an
        average of surrounding face normals weighted by the angle subtended
        by the face at the vertex. If angleWeighted is set to false, a simple
        average of surround face normals is returned.

        The simple average evaluation is significantly faster than the angle-
        weighted average.

        This method is not threadsafe.
        """
        pass

    def getVertexNormals(*args, **kwargs):
        """
        getVertexNormals(angleWeighted, space=MSpace.kObject) -> MFloatVectorArray

        Returns all the vertex normals. The returned normals are per-vertex
        normals, so unshared normals at a vertex will be averaged.

        If angleWeighted is set to True, the normals are computed by an
        average of surrounding face normals weighted by the angle subtended
        by the face at the vertex. If angleWeighted is set to false, a simple
        average of surround face normals is returned.

        The simple average evaluation is significantly faster than the angle-
        weighted average.

        This method is not threadsafe.
        """
        pass

    def getVertices(*args, **kwargs):
        """
        getVertices() -> (MIntArray, MIntArray)

        Returns the mesh-relative/global vertex IDs for all of the mesh's
        polygons as a tuple of two int arrays. The first array contains the
        number of vertices for each polygon and the second contains the mesh-
        relative IDs for each polygon-vertex. These IDs can be used to index
        into the arrays returned by getPoints() and getFloatPoints().
        """
        pass

    def hasAlphaChannels(*args, **kwargs):
        """
        hasAlphaChannels(colorSet) -> bool

        Returns True if the color set has an alpha channel.
        """
        pass

    def hasBlindData(*args, **kwargs):
        """
        hasBlindData(compType, compId=None, blindDataId=None) -> bool

        Returns true if any component of the given type on this mesh has
        blind data. If a component ID is provided then only that particular
        component is checked. If a blind data ID is provided then only blind
        data of that type is checked.
        """
        pass

    def hasColorChannels(*args, **kwargs):
        """
        hasColorChannels(colorSet) -> bool

        Returns True if the color set has RGB channels.
        """
        pass

    def intersectFaceAtUV(*args, **kwargs):
        """
        intersectFaceAtUV(u, v, uvSet='') -> int

        Returns the IDs of the UVs on this surface which are nearest
        in uv space to the given uv set and coordinate.All these UVs
        locate at the same distance to the given coordinate.

        This method is not threadsafe.
        """
        pass

    def isBlindDataTypeUsed(*args, **kwargs):
        """
        isBlindDataTypeUsed(blindDataId) -> bool

        Returns True if the blind data type is already in use anywhere in the scene.
        """
        pass

    def isColorClamped(*args, **kwargs):
        """
        isColorClamped(colorSet) -> bool

        Returns True if the color sets RGBA components are clamped to the
        range 0 to 1.
        """
        pass

    def isColorSetPerInstance(*args, **kwargs):
        """
        isColorSetPerInstance(colorSet) -> bool

        Returns True if the color set is per-instance, and False if it is
        shared across all instances.
        """
        pass

    def isEdgeSmooth(*args, **kwargs):
        """
        isEdgeSmooth(edgeId) -> bool

        Returns True if the edge is smooth, False if it is hard.
        """
        pass

    def isNormalLocked(*args, **kwargs):
        """
        isNormalLocked(normalId) -> bool

        Returns True if the normal is locked, False otherwise.
        """
        pass

    def isPolygonConvex(*args, **kwargs):
        """
        isPolygonConvex(faceId) -> bool

        Returns True if the polygon is convex, False if it is concave.
        """
        pass

    def isPolygonUVReversed(*args, **kwargs):
        """
        isPolygonUVReversed(faceId) -> bool

        Returns True if the texture coordinates (uv's) for specified polygon are
        reversed (clockwise), False if they are not reversed (counter clockwise).
        """
        pass

    def isRightHandedTangent(*args, **kwargs):
        """
        isRightHandedTangent(tangentId, uvSet='') -> bool

        Returns True if the normal, tangent, and binormal form a right handed
        coordinate system, False otherwise.
        """
        pass

    def isUVSetPerInstance(*args, **kwargs):
        """
        isUVSetPerInstance(uvSet) -> bool

        Returns True if the UV set is per-instance, and False if it is shared
        across all instances.
        """
        pass

    def lockFaceVertexNormals(*args, **kwargs):
        """
        lockFaceVertexNormals(seq of faceIds, seq of vertIds) -> self

        Locks the normals for the given face/vertex pairs.
        """
        pass

    def lockVertexNormals(*args, **kwargs):
        """
        lockVertexNormals(sequence of vertIds) -> self

        Locks the shared normals for the specified vertices.
        """
        pass

    def numColors(*args, **kwargs):
        """
        numColors(colorSet='') -> int

        Returns the number of colors in the given color set. If no color set
        is specified then the mesh's current color set will be used.
        """
        pass

    def numUVs(*args, **kwargs):
        """
        numUVs(uvSet='') -> int

        Returns the number of UVs (texture coordinates) in the given UV set.
        If no UV set is specified then the mesh's current UV set will be used.
        """
        pass

    def onBoundary(*args, **kwargs):
        """
        onBoundary(faceId) -> bool

        Returns true if the face is on the border of the mesh, meaning that
        one or more of its edges is a border edge.
        """
        pass

    def polygonVertexCount(*args, **kwargs):
        """
        polygonVertexCount(faceId) -> int

        Returns the number of vertices in the given polygon. Raises
        ValueError if the polygon ID is invalid.
        """
        pass

    def removeFaceColors(*args, **kwargs):
        """
        removeFaceColors(seq of faceIds) -> self

        Removes colors from all vertices of the specified faces.
        """
        pass

    def removeFaceVertexColors(*args, **kwargs):
        """
        removeFaceVertexColors(seq of faceIds, seq of vertexIds) -> self

        Removes colors from the specified face/vertex pairs.
        """
        pass

    def removeVertexColors(*args, **kwargs):
        """
        removeVertexColors(seq of vertexIds) -> self

        Removes colors from the specified vertices in all of the faces which
        share those vertices.
        """
        pass

    def renameUVSet(*args, **kwargs):
        """
        renameUVSet(origName, newName, modifier=None) -> self

        Renames a UV set. The set must exist and the new name cannot be the
        same as that of an existing set.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """
        pass

    def setBinaryBlindData(*args, **kwargs):
        """
        setBinaryBlindData(compId, compType, blindDataId, attr, data) -> self
        setBinaryBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'binary' blind data attribute
        on a single component of the mesh. The data must be a single string.

        The second version sets the value of a 'binary' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        strings then it must provide a value for each component in compIds.
        If it is a single string then all of the specified components will
        have their blind data set to that value.
        """
        pass

    def setBoolBlindData(*args, **kwargs):
        """
        setBoolBlindData(compId, compType, blindDataId, attr, data) -> self
        setBoolBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'boolean' blind data attribute
        on a single component of the mesh. The data must be a single boolean.

        The second version sets the value of a 'boolean' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        booleans then it must provide a value for each component in compIds.
        If it is a single boolean then all of the specified components will
        have their blind data set to that value.
        """
        pass

    def setColor(*args, **kwargs):
        """
        setColor(colorId, MColor, colorSet='', rep=kRGBA) -> self

        Sets a color in the specified colorSet. If no colorSet is given the
        current colorSet will be used. If the colorId is greater than or
        equal to numColors() then the colorSet will be grown to accommodate
        the specified color.
        """
        pass

    def setColors(*args, **kwargs):
        """
        setColors(seq of MColor, colorSet='', rep=kRGBA) -> self

        Sets all the colors of the specified colorSet. If no colorSet is
        given the current colorSet will be used. After using this method to
        set the color values, you can call assignColors() to assign the
        corresponding color ids to the geometry.

        The color sequence must be at least as large as the current color set
        size. You can determine the color set size by calling numColors() for
        the default color set, or numColors(colorSet) for a named color set.
        If the sequence is larger than the color set size, then the color set
        for this mesh will be expanded to accommodate the new color values.

        In order to shrink the colorSet you have to clear its existing
        colors. E.g: clearColors(), setColors( ... ), assignColors()
        """
        pass

    def setCreaseEdges(*args, **kwargs):
        """
        setCreaseEdges(edgeIds, seq of float) -> self


        Sets the specified edges of the mesh as crease edges.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned by
        Pixar(R).
        """
        pass

    def setCreaseVertices(*args, **kwargs):
        """
        setCreaseVertices(edgeIds, seq of float) -> self


        Sets the specified edges of the mesh as crease edges.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned by
        Pixar(R).
        """
        pass

    def setCurrentColorSetName(*args, **kwargs):
        """
        setCurrentColorSetName(colorSet, modifier=None, currentSelection=None) -> self

        Sets the 'current' color set for this object. The current color set
        is the one used when no color set name is specified for a color
        operation. If the specified color set does not exist then the current
        color set will not be changed.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.

        This method may change the current selection. If the 'currentSelection'
        (MSelectionList) parameter is provided then the current selection
        will be saved to it prior to the change. This is useful for
        supporting full undo of the change.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """
        pass

    def setCurrentUVSetName(*args, **kwargs):
        """
        setCurrentUVSetName(uvSet, modifier=None, currentSelection=None) -> self

        Sets the 'current' uv set for this object. The current uv set is the
        one used when no uv set name is specified for a uv operation. If the
        specified uv set does not exist then the current uv set will not be
        changed.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.

        This method may change the current selection. If the 'currentSelection'
        (MSelectionList) parameter is provided then the current selection
        will be saved to it prior to the change. This is useful for
        supporting full undo of the change.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """
        pass

    def setDoubleBlindData(*args, **kwargs):
        """
        setDoubleBlindData(compId, compType, blindDataId, attr, data) -> self
        setDoubleBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'double' blind data attribute
        on a single component of the mesh. The data must be a single float.

        The second version sets the value of a 'double' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        floats then it must provide a value for each component in compIds.
        If it is a single float then all of the specified components will
        have their blind data set to that value.
        """
        pass

    def setEdgeSmoothing(*args, **kwargs):
        """
        setEdgeSmoothing(edgeId, smooth=True) -> self

        Sets the specified edge to be hard or smooth. You must use the
        cleanupEdgeSmoothing() method after all the desired edges on your
        mesh have had setEdgeSmoothing() done. Use the updateSurface() method
        to indicate the mesh needs to be redrawn.
        """
        pass

    def setEdgeSmoothings(*args, **kwargs):
        """
        setEdgeSmoothings(edgeIds, smooths) -> self

        Sets the specified edges to be hard or smooth. You must use the
        cleanupEdgeSmoothing() method after all the desired edges on your
        mesh have had setEdgeSmoothings() done. Use the updateSurface() method
        to indicate the mesh needs to be redrawn.
        """
        pass

    def setFaceColor(*args, **kwargs):
        """
        setFaceColor(color, faceId, rep=kRGBA) -> self

        Sets the face-vertex color for all vertices on this face.
        """
        pass

    def setFaceColors(*args, **kwargs):
        """
        setFaceColors(colors, faceIds, rep=kRGBA) -> self

        Sets the colors of the specified faces. For each face in the faceIds
        sequence the corresponding color from the colors sequence will be
        applied to all of its vertices.
        """
        pass

    def setFaceVertexColor(*args, **kwargs):
        """
        setFaceVertexColor(color, faceId, vertexId, modifier=None, rep=kRGBA) -> self

        Sets a face-specific normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
        pass

    def setFaceVertexColors(*args, **kwargs):
        """
        setFaceVertexColors(colors, faceIds, vertexIds, modifier=None, rep=kRGBA) -> self

        Sets the colors of the specified face/vertex pairs.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
        pass

    def setFaceVertexNormal(*args, **kwargs):
        """
        setFaceVertexNormal(normal, faceId, vertexId, space=MSpace.kObject, modifier=None) -> self

        Sets a face-specific normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
        pass

    def setFaceVertexNormals(*args, **kwargs):
        """
        setFaceVertexNormal(normals, faceIds, vertexIds, space=MSpace.kObject) -> self

        Sets normals for the given face/vertex pairs.
        """
        pass

    def setFloatBlindData(*args, **kwargs):
        """
        setFloatBlindData(compId, compType, blindDataId, attr, data) -> self
        setFloatBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'float' blind data attribute
        on a single component of the mesh. The data must be a single float.

        The second version sets the value of a 'float' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        floats then it must provide a value for each component in compIds.
        If it is a single float then all of the specified components will
        have their blind data set to that value.
        """
        pass

    def setIntBlindData(*args, **kwargs):
        """
        setIntBlindData(compId, compType, blindDataId, attr, data) -> self
        setIntBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'int' blind data attribute
        on a single component of the mesh. The data must be a single int.

        The second version sets the value of a 'int' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        ints then it must provide a value for each component in compIds.
        If it is a single int then all of the specified components will
        have their blind data set to that value.
        """
        pass

    def setInvisibleFaces(*args, **kwargs):
        """
        setInvisibleFaces(faceIds, makeVisible=False) -> self

        Sets the specified faces of the mesh to be visible or invisible. See
        the getInvisibleFaces() method for a description of invisible faces.
        """
        pass

    def setIsColorClamped(*args, **kwargs):
        """
        setIsColorClamped(colorSet, clamped) -> self

        Sets whether the color set's RGBA components should be clamped to the
        range 0 to 1.
        """
        pass

    def setNormals(*args, **kwargs):
        """
        setNormals(normals, space=MSpace.kObject) -> self

        Sets the mesh's normals (user normals).
        """
        pass

    def setPoint(*args, **kwargs):
        """
        setPoint(vertexId, MPoint, space=MSpace.kObject) -> self

        Sets the position of specified vertex.

        Note that if you modify the position of a vertex for a mesh node (as
        opposed to mesh data), a tweak will be created. If you have a node
        with no history, the first time that a tweak is created, the
        underlying pointers under the MFnMesh object may change. You will
        need to call syncObject() to make sure that the object is valid.
        Subsequent calls to setPoint() on the same object do not require a
        syncObject() call.
        """
        pass

    def setPoints(*args, **kwargs):
        """
        setPoints(points, space=MSpace.kObject) -> self

        Sets the positions of the mesh's vertices. The positions may be
        given as a sequence of MFloatPoint's or a sequence of MPoint's, but
        not a mix of the two.
        """
        pass

    def setSmoothMeshDisplayOptions(*args, **kwargs):
        """
        setSmoothMeshDisplayOptions(MMeshSmoothOptions) -> self

        Sets the options to use when smoothing the mesh for display.
        """
        pass

    def setSomeColors(*args, **kwargs):
        """
        setSomeColors(colorIds, colors, colorSet='', rep=kRGBA) -> self

        Sets specific colors in a colorSet.

        If the largest colorId in the sequence is larger than numColors()
        then the colorSet will be grown to accommodate the new color values.
        If you have added new colorIds, you can call assignColors to assign
        the colorIds to the geometry. If you are modifying existing colors,
        they will already be referenced by the existing mesh data.
        """
        pass

    def setSomeUVs(*args, **kwargs):
        """
        setSomeUVs(uvIds, uValues, vValues, uvSet='') -> self

        Sets the specified texture coordinates (uv's) for this mesh. The uv
        value sequences and the uvIds sequence must all be of equal size. If
        the largest uvId in the array is larger than numUVs() then the uv
        list for this mesh will be grown to accommodate the new uv values.
        If a named uv set is given, the array will be grown when the largest
        uvId is larger than numUVs(uvSet).

        If you have added new uvIds, you must call one of the assignUV
        methods to assign the uvIds to the geometry. If you are modifying
        existing UVs, you do not need to call one of the assignUV methods.
        """
        pass

    def setStringBlindData(*args, **kwargs):
        """
        setStringBlindData(compId, compType, blindDataId, attr, data) -> self
        setStringBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'string' blind data attribute
        on a single component of the mesh. The data must be a single string.

        The second version sets the value of a 'string' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        strings then it must provide a value for each component in compIds.
        If it is a single string then all of the specified components will
        have their blind data set to that value.
        """
        pass

    def setUV(*args, **kwargs):
        """
        setUV(uvId, u, v, uvSet='') -> self

        Sets the specified texture coordinate.

        The uvId is the element in the uv list that will be set. If the uvId
        is greater than or equal to numUVs() then the uv list will be grown
        to accommodate the specified uv. If the UV being added is new, thenyou must call one of the assignUV methods in order to update the
        geometry.
        """
        pass

    def setUVs(*args, **kwargs):
        """
        setUVs(uValues, vValues, uvSet='') -> self

        Sets all of the texture coordinates (uv's) for this mesh. The uv
        value sequences must be of equal size and must be at least as large
        as the current UV set size. You can determine the UV set size by
        calling numUVs() for the default UV set, or numUVs(uvSet) for a
        named UV set.

        If the sequences are larger than the UV set size, then the uv list
        for this mesh will be grown to accommodate the new uv values.

        After using this method to set the UV values, you must call one of
        the assignUV methods to assign the corresponding UV ids to the
        geometry.

        In order to shrink the uvs array, do the following: clearUVs(),
        setUVs(...), assignUVs(). These steps will let you to create an
        array of uvs which is smaller than the original one.
        """
        pass

    def setVertexColor(*args, **kwargs):
        """
        setVertexColor(color, vertexId, modifier=None, rep=kRGBA) -> self

        Sets the color for a vertex in all the faces which share it.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
        pass

    def setVertexColors(*args, **kwargs):
        """
        setVertexColors(colors, vertexIds, modifier=None, rep=kRGBA) -> self

        Sets the colors of the specified vertices. For each vertex in the
        vertexIds sequence, the corresponding color from the colors sequence
        will be applied to the vertex in all of the faces which share it.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
        pass

    def setVertexNormal(*args, **kwargs):
        """
        setVertexNormal(normal, vertexId, space=MSpace.kObject, modifier=None) -> self

        Sets the shared normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
        pass

    def setVertexNormals(*args, **kwargs):
        """
        setVertexNormal(normals, vertexIds, space=MSpace.kObject) -> self

        Sets the shared normals for the given vertices.
        """
        pass

    def sortIntersectionFaceTriIds(*args, **kwargs):
        """
        sortIntersectionFaceTriIds(faceIds, triIds=none) -> self

        Convenience routine for sorting faceIds or face/triangle ids before
        passing them into the closestIntersection(), allIntersections(), or
        anyIntersection() methods. When using an acceleration structure with
        an intersection operation it is essential that any faceId or
        faceId/triId arrays be sorted properly to ensure optimal performance.

        Both arguments must be MIntArray's.
        """
        pass

    def split(*args, **kwargs):
        """
        split(((kOnEdge, int, float), (kInternalPoint, MFloatPoint), ...)) -> self

        Each tuple in the placements sequence consists of a Split Placement
        constant followed by one or two parameters.

        If the Split Placement is kOnEdge then the tuple will contain two
        more elements giving the int id of the edge to split, and a float
        value between 0 and 1 indicating how far along the edge to do the
        split. The same edge cannot be split more than once per call.

        If the Split Placement is kInternalPoint then the tuple will contain
        just one more element giving an MFloatPoint within the face.

        All splits must begin and end on an edge meaning that the first and
        last tuples in the placements sequence must be kOnEdge placements.
        """
        pass

    def subdivideEdges(*args, **kwargs):
        """
        subdivideEdges(edges, numDivisions) -> self

        Subdivides edges at regular intervals. For example, if numDivisions
        is 2 then two equally-spaced vertices will be added to each of the
        specified edges: one 1/3 of the way along the edge and a second 2/3
        of the way along the edge.
        """
        pass

    def subdivideFaces(*args, **kwargs):
        """
        subdivideFaces(faces, numDivisions) -> self

        Subdivides each specified face into a grid of smaller faces.
        Triangles are subdivided into a grid of smaller triangles and quads
        are subdivided into a grid of smaller quads. Faces with more than
        four edges are ignored.

        The numDivisions parameter tells how many times to subdivide each
        edge of the face. Internal points and edges are introduced as needed
        to create a grid of smaller faces.
        """
        pass

    def syncObject(*args, **kwargs):
        """
        syncObject() -> self

        If a non-api operation happens that many have changed the
        underlying Maya object attached to this functionset, calling this
        method will make sure that the functionset picks up those changes.
        In particular this call should be used after calling mel commands
        which might affect the mesh. Note that this only applies when the
        functionset is attached to a mesh node. If it's attached to mesh
        data the it is not necessary to call this method.
        """
        pass

    def unlockFaceVertexNormals(*args, **kwargs):
        """
        unlockFaceVertexNormals(seq of faceIds, seq of vertIds) -> self

        Unlocks the normals for the given face/vertex pairs.
        """
        pass

    def unlockVertexNormals(*args, **kwargs):
        """
        unlockVertexNormals(sequence of vertIds) -> self

        Unlocks the shared normals for the specified vertices.
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        Signal that this polygonal mesh has changed and needs to be redrawn.
        """
        pass

    @staticmethod
    def autoUniformGridParams(*args, **kwargs):
        """
        autoUniformGridParams() -> MMeshIsectAccelParams

        Creates an object which specifies a uniform voxel grid structure
        which can be used by the intersection routines to speed up their
        operation. The number of voxel cells to use will be determined
        automatically based on the density of triangles in the mesh. The
        grid acceleration structure will be cached with the mesh, so that
        if the same MMeshIsectAccelParams configuration is used on the next
        intersect call, the acceleration structure will not need to be rebuilt.
        """
        pass

    @staticmethod
    def clearGlobalIntersectionAcceleratorInfo(*args, **kwargs):
        """
        clearGlobalIntersectionAcceleratorInfo()

        Clears the 'total count', 'total build time', and 'peak memory'
        fields from the information string returned by
        globalIntersectionAcceleratorsInfo(). It will not cause information
        about currently existing accelerators to be lost.
        """
        pass

    @staticmethod
    def globalIntersectionAcceleratorsInfo(*args, **kwargs):
        """
        globalIntersectionAcceleratorsInfo() -> string

        Returns a string that describes the system-wide resource usage for
        cached mesh intersection accelerators. The string will be of the
        following form:
          total 10 accelerators created (2 currently active - total current memory = 10000KB), total build time = 10.2s, peak memory = 14567.1KB

        This means that:

        * a total of 10 intersection accelerators have been created as
          instructed by calls to closestIntersection(), allIntersections(),
          or anyIntersection() with non-NULL accelParams values. Thesen  structures are destroyed and re-created when intersection requests
          with differing acceleration parameters are passed in for the same
          mesh, so it is useful to see this value, which is the total count
          of how many have been created. In this case, 8 of the 10 created
          have been destroyed, either automatically or via calls to the
          freeCachedIntersectionAccelerator() method

        * the total memory footprint for the 2 accelerators currently in
          existence is 10,000KB

        * the total build time for all 10 structures that have been created
          is 10.2 seconds
        * the peak of total memory usage for all accelerators in the system
          was 14567.1KB
        Calling clearGlobalIntersectionAcceleratorInfo() will clear the
        'total count', 'total build time', and 'peak memory' fields from
        this information. It will not cause information about currently
        existing accelerators to be lost.
        """
        pass

    @staticmethod
    def uniformGridParams(*args, **kwargs):
        """
        uniformGridParams(xDiv, yDiv, zDiv) -> MMeshIsectAccelParams

        Creates an object which specifies a uniform voxel grid structure
        which can be used by the intersection routines to speed up their
        operation. This object specifies the number of voxel cells to be
        used in the x, y, and z dimensions. The grid acceleration structure
        will be cached with the mesh, so that if the same MMeshIsectAccelParams
        configuration is used on the next intersect call, the acceleration
        structure will not need to be rebuilt.
        """
        pass

    checkSamePointTwice = None

    displayColors = None

    kAlpha = 1

    kDifference = 2

    kInstanceUnspecified = -1

    kInternalPoint = 1

    kIntersectTolerance = 1e-06

    kIntersection = 3

    kInvalid = 2

    kOnEdge = 0

    kPointTolerance = 1e-10

    kRGB = 3

    kRGBA = 4

    kUnion = 1

    numColorSets = None

    numEdges = None

    numFaceVertices = None

    numNormals = None

    numPolygons = None

    numUVSets = None

    numVertices = None


class MFnNurbsSurfaceData(MFnGeometryData):
    """
    MFnNurbsSurfaceData allows the creation and manipulation of Nurbs Surface
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnNurbsSurfaceData object

    __init__(MObject)
    Initializes a new MFnNurbsSurfaceData function set, attached
    to the specified object.
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def create(*args, **kwargs):
        """
        create() -> MObject

        Creates a new nurbs surface data object, attaches it to this function set
        and returns an MObject which references it.
        """
        pass


class MFnNurbsSurface(MFnDagNode):
    """
    NURBS (Non-Uniform Rational B-Spline) surface function set.

    The shape of a NURBS surface is defined by an array of CVs
    (control vertices), an array of knot values in the U direction
    and an array of knot values in the V direction, a degree in U
    and in V, and a form in U and in V.

    The U and V knot vectors for NURBS surfaces are of size
    (spansInU + 2*degreeInU -1) and (spansInV + 2*degreeInV -1).
    Note: spans = numCVs - degree.

    There are 3 possible forms for the surface in the U and V
    directions: open, closed and periodic. These forms are described
    below. Note that the descriptions below apply to both the U and
    V directions.

    The open and closed forms are quite similar, and in fact a
    closed surface will become an open surface if either the first
    or last CV is moved so that they are no longer coincident. To
    create an open or closed surface, of degree N, with M spans, you
    must provide M+N CVs. This implies that for a degree N surface,
    you must specify at least N+1 CVs to get a surface with a single
    span.

    The number of knots required for the surface is M + 2N - 1.  If
    you want the surface to start exactly at the first CV and end
    exactly at the last CV, then the knot vector must be structured
    to have degree N multiplicity at the beginning and end. This
    means that the first N knots must be identical, and the last N
    knots must be identical.

    A periodic surface is a special case of a closed surface.
    Instead of having just the first and last CVs coincident, the
    last N CVs in the surface, where N is equal to the degree,
    overlap the first N CVs. This results in a surface with no
    tangent break where the ends meet. The last N CVs in a periodic
    surface are permanently bound to the first N CVs, and Maya will
    not allow those last N CVs to be repositioned. If one or more
    of the first N CVs of the surface are repositioned, the
    overlapping CV's will remain bound, and will also be moved.

    In order to create a periodic surface, you must specify at least
    2N+1 CVs, so that that last N can overlap the first N and you
    still have 1 non-overlapping CV left.  The number of CVs
    required to create a periodic surface is still N+M (with a
    lower limit of 2N+1), but you must ensure that the positions
    of the last N CVs are identical to the positions of the
    first N.

    You still need M + 2N - 1 knots for a periodic surface, but
    the knot values required are more restrictive than for open
    or closed surfaces because of the overlap of the last N CVs.
    The first N knots should be specified at the beginning of
    the knot array as values { -(N-1), -(N-2), ... 0 } in order
    to implement the overlap.  Additionally there can be no knot
    multiplicity at the end of the surface, because that would
    compromise the tangent continuity property.

    Note that some third party applications use a different
    format for knots, where the number of knots required for a
    surface is M+2N+1 rather than M+2N-1 as used in Maya. Both
    knot representations are equivalent mathematically. To
    convert from one of these external representations into the
    Maya representation, simply omit the first and last knots
    from the external representation when creating the Maya
    representation. To convert from the Maya representation into
    the external representation, add two new knots at the
    beginning and end of the Maya knot sequence. The value of
    these new knots depends on the existing knot sequence. For a
    knot sequence with multiple end knots, simply duplicate the
    existing first and last knots once more, for example:

    Maya representation: {0,0,0,...,N,N,N}
    External representation: {0,0,0,0,...,N,N,N,N}

    For a knot sequence with uniform end knots, create the new
    knots offset at an interval equal to the existing first and
    last knot intervals, for example:

    Maya representation: {0,1,2,...,N,N+1,N+2}
    External representation: {-1,0,1,2,...,N,N+1,N+2,N+3}
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def area(*args, **kwargs):
        """
        area(space=kObject, tolerance=kPointTolerance) -> float

        Returns the surface's area, or 0.0 if the area cannot be determined.
        """
        pass

    def assignUV(*args, **kwargs):
        """
        assignUV(patchId, cornerIndex, uvId) -> self

        Maps a texture coordinate (uv) to a the specified corner of a patch.

        Note that API methods that modify uv data will work correctly when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * patchId     (int) - Patch to map to.
        * cornerIndex (int) - Corner of the patch to map to.
        * uvId        (int) - Index into the uv list of the UV to map.
        """
        pass

    def assignUVs(*args, **kwargs):
        """
        assignUVs(uvCounts, uvIds) -> self

        Maps all texture coordinates for the surface. setUV() and setUVs()
        are used to create the texture coordinate table for the surface.
        After the table is created, this method is used to map those values
        to each patch on a per-corner basis.

        The uvCounts array should contain the number of uvs per patch.
        Since uvs are mapped per-patch per-corner, the entries in this array
        should match the corner counts for each patch in the surface.
        If an entry in this array is '0' then the corresponding patch will
        not be mapped.

        The sum of all the entries in the uvCounts array must be equal to
        the size of the uvIds array or this method will fail.

        The uvIds array should contain the UV indices that will be mapped to
        each patch-corner in the surface. The entries in this array specify
        which uvs in the surface's uv table are mapped to each patch-corner.
        Each entry in the uvIds array must be less than numUVs().
        The size of the uvIds array is equivalent to adding up all of the
        entries in the uvCounts array, so for a cube with all patches mapped
        there would be 24 entries.

        Note that API methods that modify uv data will work correctly when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * uvCounts (MIntArray or seq of int)
                     - UV counts for each patch in the surface.
        * uvIds    (MIntArray or seq of int)
                     - UV indices to be mapped to each patch-corner.
        """
        pass

    def boundaryType(*args, **kwargs):
        """
        boundaryType(region, boundary) -> int

        Returns the type of the specified boundary. The surface must be a
        trimmed surface. Valid boundary types are:

            kInner           - an inner (clockwise) boundary
            kOuter           - an outser (counter clockwise) boundary
            kSegment         - a curve on a patch
            kClosedSegment   - a closed curve on a patch
            kInvalidBoundary - an invalid boundary type

        * region (int)   - Region containing the boundary
        * boundary (int) - Index of the boundary within the region.
        """
        pass

    def clearUVs(*args, **kwargs):
        """
        clearUVs() -> self

        Clears out all texture coordinates for the nurbsSurface, and leaves
        behind an empty UVset.

        This method should be used if it is needed to shrink the size of the
        UV table. In this case, the user should call clearUVs, setUVs and
        then assignUVs to rebuild the mapping info.

        When called on a dataNurbsSurface the UVs are removed. When called
        on a shape with no history, the UVs are removed and the attributes
        are set on the shape. When called on a shape with history, the
        polyDelMap command is invoked and a polyMapDel node is created.
        """
        pass

    def closestPoint(*args, **kwargs):
        """
        closestPoint(testPoint, uStart=None, vStart=None,
            ignoreTrimBoundaries=False, tolerance=kPointTolerance,
            space=kObject) -> (MPoint, float, float)

        Returns the closest point on the surface to the specified test point
        The return value is a tuple containing the position of the point and
        and its U and V texture parameters.

        Performance can be greatly increased by supplying starting U and V
        parameter values which are reasonably close to the final point.
        Specifying these values will invoke a special algorithm which will
        begin to search for the closest point at the given parameter value,
        and will check the local surface to see which direction will bring
        it closer to the given point. It then offsets in this direction and
        repeats the process, iteratively traversing the surface until it
        finds the closest point.
        This algorithm will fail if it encounters a seam before reaching
        the closest point, or if it finds a local closest point, such as a
        bulge on a mesh where an offset in any direction will take it
        further from the given point, even if that is not the true closest
        point on the mesh. For this reason it is advisable to avoid using
        this option unless absolutely sure that the initial point will be
        a good enough approximation to the final point that these
        conditions will not occur.

        * testPoint (MPoint) - Position of the point to be checked
        * uStart     (float) - Initial guess of a U parameter near where the
                               where the closest point is expected to be.
        * vStart     (float) - Initial guess of a V parameter near where the
                               where the closest point is expected to be.
        * ignoreTrimBoundaries (bool)
                             - For trimmed surfaces, if this is true the
                               trim curves will be ignored and the entire
                               untrimmed surface searched.
        * tolerance  (float) - How close to the surface must a point be to
                               be considered 'on' the surface.
        * space        (int) - an MSpace constant giving the coordinate
                               space which 'testPoint' is in. The returned
                               point will be in the same space.
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source, parent=kNullObj) -> MObject

        Returns a new NURBS surface, which is a copy of the source surface,
        and sets the functionset to operate on it.

        * source (MObject)- The surface to copy.
        * parent (MObject)- The parent/owner of the new surface. If it's a
                            NURBS surface data wrapper (MFn.kNurbsSurfaceData)
                            then the created surface will be returned as a
                            geometry object (MFn.kNurbsSurfaceGeom) owned by
                            the wrapper. If 'parent' is a DAG node then the
                            new surface will be returned as nurbsSurface node
                            parented under it. If 'parent' is not provided
                            then a new top-level transform will be created
                            with the new surface parented beneath it as a
                            nurbsSurface node. In this last case it will be
                            the transform node which is returned.
        """
        pass

    def create(*args, **kwargs):
        """
        create(cvs, uKnots, vKnots, uDegree, vDegree, uForm, vForm,
            rational, parent=kNullObj) -> MObject

        Returns a new NURBS surface created from the specified data and sets
        the function set to operate on it.

        * cvs (MPointArray or seq of MPoint)
                          - The control vertices.
        * uKnots (MDoubleArray or seq of float)
                          - Parameter values for the knots in the U direction.
        * vKnots (MDoubleArray or seq of float)
                          - Parameter values for the knots in the V direction.
        * uDegree   (int) - Degree of the basis functions in the U direction.
        * vDegree   (int) - Degree of the basis functions in the V direction.
        * uForm     (int) - A Form constant (kOpen, kClosed, kPeriodic) giving
                            the surface's form in the U direction.
        * vForm     (int) - A Form constant (kOpen, kClosed, kPeriodic) giving
                            the surface's form in the V direction.
        * rational (bool) - Create as rational (True) or non-rational (False)
                            surface.
        * parent (MObject)- The parent/owner of the new surface. If it's a
                            NURBS surface data wrapper (MFn.kNurbsSurfaceData)
                            then the created surface will be returned as a
                            geometry object (MFn.kNurbsSurfaceGeom) owned by
                            the wrapper. If 'parent' is a DAG node then the
                            new surface will be returned as nurbsSurface node
                            parented under it. If 'parent' is not provided
                            then a new top-level transform will be created
                            with the new surface parented beneath it as a
                            nurbsSurface node. In this last case it will be
                            the transform node which is returned.
        """
        pass

    def cv(*args, **kwargs):
        """
        cv(uIndex, vIndex) -> MObject

        Returns a component for the specified control vertex.

        * uIndex (int) - U index of the CV.
        * vIndex (int) - V index of the CV.
        """
        pass

    def cvPosition(*args, **kwargs):
        """
        cvPosition(uIndex, vIndex, space=kObject) -> MPoint

        Returns the position of the specified control vertex.

        * uIndex (int) - U index of the CV.
        * vIndex (int) - V index of the CV.
        * space  (int) - an MSpace constant giving the coordinate
                         space which the point should be returned.
        """
        pass

    def cvPositions(*args, **kwargs):
        """
        cvPositions(space=kObject) -> MPointArray

        Returns the positions of all the surface's control vertices.

        * space  (int) - an MSpace constant giving the coordinate
                         space which the points should be returned.
        """
        pass

    def cvsInU(*args, **kwargs):
        """
        cvsInU(startUIndex, endUIndex, vIndex) -> MObject

        Returns a component for a set of control vertices in the U direction.

        * startUIndex (int) - U index of the first CV to return.
        * endUIndex   (int) - U index of the last CV to return.
        * vIndex      (int) - V index for all of the returned CVs.
        """
        pass

    def cvsInV(*args, **kwargs):
        """
        cvsInV(startVIndex, endVIndex, uIndex) -> MObject

        Returns a component for a set of control vertices in the V direction.

        * startVIndex (int) - V index of the first CV to return.
        * endVIndex   (int) - V index of the last CV to return.
        * uIndex      (int) - U index for all of the returned CVs.
        """
        pass

    def distanceToPoint(*args, **kwargs):
        """
        distanceToPoint(point, space=kObject) -> float

        Returns the distance from the given point to the closest point on
        the surface.

        * point (MPoint) - Point to calculate distance to.
        * space  (int)   - An MSpace constant giving the coordinate space in
                           which the point has been specified.
        """
        pass

    def edge(*args, **kwargs):
        """
        edge(region, boundary, edge, paramEdge=False) -> MObjectArray

        Return the specified edge of a trim boundary.

        For each region of a trimmed surface there may be several boundary
        curves: an outer curve and possibly several inner boundary curves
        (which define holes). These boundary curves are made up of one or
        more curves called edges.

        The edge is returned as an MObjectArray as it may consist of more
        than one curve. The returned edge, or trim curve, can be a 2D parameter
        edge or a 3D edge curve. Note that for closed surfaces some of the
        3d edges may be 0 length in which case an empty MObjectArray is
        returned. An example of this is the poles of a sphere.

        * region     (int) - Index of trimmed region containing the edge.
        * boundary   (int) - Index of boundary within trimmed region.
        * edge       (int) - Index of the edge within the boundary.
        * paramEdge (bool) - If True a 2D parameter edge is returned,
                             otherwise a 3D edge is returned.
        """
        pass

    def getAssignedUVs(*args, **kwargs):
        """
        getAssignedUVs() -> (MIntArray, MIntArray)

        Returns the indices of all UVs which have been mapped to the surface.
        The return value is a tuple with an array containing the number
        of UVs for each patch in the surface, and a second array containing
        the indices of the UVs mapped to each corner of those patches. This
        is the same format as the arrays taken by the assignUVs() method.
        """
        pass

    def getConnectedShaders(*args, **kwargs):
        """
        getConnectedShaders(instanceNumber) -> (MObjectArray, MIntArray)

        Returns a tuple containing an array of all the shaders (sets)
        connected to the specified instance of this surface, and an array of
        patch/shader assignments. The second array will hold, for each patch
        in the surface, an index into the first array. If a patch does not
        have a shader assigned to it, the value of the index will be -1.
        The shader objects can be derived from the sets returned.

        Note: This method will only work with a MFnNurbsSurface function set
              which has been initialized with an MFn::kNurbsSurface.

        See also getConnectedSetsAndMembers.

        * instanceNumber (int) - Determines which instance of the surface to
                                 query. This will be zero if there is only
                                 one instance.
        """
        pass

    def getDerivativesAtParam(*args, **kwargs):
        """
        getDerivativesAtParam(uParam, vParam, space=kObject, secondOrder=False)
            -> (MPoint, MVector, MVector)
            -> (MPoint, MVector, MVector, MVector, MVector, MVector)

        Evaluates the surface at the given (u,v) coordinates, returning a
        tuple containing the position at that point, the first derivative
        vector in U, and the first derivative vector in V. If 'secondOrder'
        is True then the tuple will also contain three additional vectors:
        the second order partial derivative with respect to U (dUU), the
        second order partial derivative with respect to V (dVV), and the
        second order partial derivative with respect to U then V (dUV).
        None of the vectors will be normalized.

        * uParam (float) - U parameter value at which to do the evaluation.
        * vParam (float) - V parameter value at which to do the evaluation.
        * space    (int) - An MSpace constant giving the coordinate space in
                           which to perform the calculation.
        * secondOrder (bool)
                         - If True, second order derivatives will be included
                           in the result. Note that this will increase
                           computation time.
        """
        pass

    def getParamAtPoint(*args, **kwargs):
        """
        getParamAtPoint(point, ignoreTrimBoundaries, tolerance=kPointTolerance,
            space=kObject) -> (float, float)

        Returns a tuple containing the parameter values corresponding to the
        given point on the surface (or underlying surface).

        * point    (MPoint) - Location of the parameter to obtain.
        * ignoreTrimBoundaries (bool)
                            - For trimmed surfaces, if this is true the
                              trim curves will be ignored and the entire
                              untrimmed surface searched.
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation.
        """
        pass

    def getPatchUV(*args, **kwargs):
        """
        getPatchUV(patchId, cornerIndex) -> (float, float)

        Returns a tuple containing the texture texture coordinate for a
        corner of a patch. Since texture coordinates (UVs) are stored
        per-patch per-corner you must specify both the patch and the corner
        that the u and v values are mapped to.
        * patchId (int)     - Patch of interest.
        * cornerIndex (int) - Corner of interest.
        """
        pass

    def getPatchUVid(*args, **kwargs):
        """
        getPatchUVid(patchId, cornerIndex) -> int

        Returns the id of the texture coordinate for a single corner of a patch.

        * patchId (int)     - Patch of interest.
        * cornerIndex (int) - Corner of interest.
        """
        pass

    def getPatchUVs(*args, **kwargs):
        """
        getPatchUVs(patchId) -> (MFloatArray, MFloatArray)

        Returns a tuple containing the values of the texture coordinates on
        all corners of the specified patch. The tuple contains an array of U
        coordinates and an array of V coordinates, both the same length.

        * patchId (int)     - Patch of interest.
        """
        pass

    def getPointAtParam(*args, **kwargs):
        """
        getPointAtParam(uParam, vParam, space=kObject) -> MPoint
        """
        pass

    def getUV(*args, **kwargs):
        """
        getUV(uvId) -> (float, float)

        Returns a tuple containing the U and V values for the a texture coordinate

        * uvId (int) - Id of the texture coordinate of intest.
        """
        pass

    def getUVs(*args, **kwargs):
        """
        getUVs() -> (MFloatArray, MFloatArray)

        Returns all of the surface's texture coordinates as a tuple containing
        an array of U values and an array of V values.
        """
        pass

    def intersect(*args, **kwargs):
        """
        intersect(rayStart, rayDir, tolerance=kPointTolerance, space=kObject,
            distance=False, exactHit=False, all=False)
            -> (MPoint, float, float[, float][, bool])
            -> (MPointArray, MDoubleArray, MDoubleArray[, MDoubleArray][, bool])
            -> None

        Returns the closest point of intersection of a ray with the surface
        as a tuple containing the point of intersection and the U and V
        parameters at that point.
        * rayStart (MPoint) - Starting point for the ray.
        * rayDir  (MVector) - Direction of the ray
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation.* distance   (bool) - If True the distance from 'rayStart' to the
                              point of intersection will be appended to the
                              returned tuple.
        * exactHit   (bool) - If True then a boolean value indicating if the
                              point of intersection was an exact hit will be
                              appended to the returned tuple.
        * all        (bool) - If True then all points of intersection will
                              be returned. In this case the point of
                              intersection, U and V parameters, and distance
                              (if requested) will all be returned as arrays.
        """
        pass

    def isFlipNorm(*args, **kwargs):
        """
        isFlipNorm(region) -> bool

        Checks whether the normal for the specified region is flipped
        This method is only valid for trimmed surfaces.

        region (int) - Region to check.
        """
        pass

    def isKnotU(*args, **kwargs):
        """
        isKnotU(param) -> bool

        Checks if the specified parameter value is a knot value in the U
        direction.

        * param (float) - Parameter value to check.
        """
        pass

    def isKnotV(*args, **kwargs):
        """
        isKnotV(param) -> bool

        Checks if the specified parameter value is a knot value in the V
        direction.

        * param (float) - Parameter value to check.
        """
        pass

    def isParamOnSurface(*args, **kwargs):
        """
        isParamOnSurface(uParam, vParam) -> bool

        Checks if the specified parameter point is on this surface.

        * uParam (float) - U parameter value.
        * vParam (float) - V parameter value.
        """
        pass

    def isPointInTrimmedRegion(*args, **kwargs):
        """
        isPointInTrimmedRegion(uParam, vParam) -> bool

        Checks if the given point is in a trimmed away region of a trimmed
        surface. A trimmed away region is the part of the surface that is
        cut away as a result of a trim operation.

        * uParam (float) - U parameter of the point to check.
        * vParam (float) - V parameter of the point to check.
        """
        pass

    def isPointOnSurface(*args, **kwargs):
        """
        isPointOnSurface(point, tolerance=kPointTolerance, space=kObject) -> bool

        Checks if the given point is on this surface.

        * point    (MPoint) - Point to check.
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation
        """
        pass

    def knotInU(*args, **kwargs):
        """
        knotInU(index) -> float

        Returns the knot value at the specified U index. U knots are indexed
        from 0 to numKnotsInU-1.
        * index (int) - Index of the U knot to return.
        """
        pass

    def knotInV(*args, **kwargs):
        """
        knotInV(index) -> float

        Returns the knot value at the specified V index. V knots are indexed
        from 0 to numKnotsInV-1.
        * index (int) - Index of the V knot to return.
        """
        pass

    def knotsInU(*args, **kwargs):
        """
        knotsInU() -> MDoubleArray

        Returns all of the surface's knots in the U direction.
        """
        pass

    def knotsInV(*args, **kwargs):
        """
        knotsInV() -> MDoubleArray

        Returns all of the surface's knots in the V direction.
        """
        pass

    def normal(*args, **kwargs):
        """
        normal(uParam, vParam, space=kObject) -> MVector

        Returns the normal at the given parameter value on the surface.

        * uParam (float) - U parameter at which to obtain normal.
        * vParam (float) - V parameter at which to obtain normal.
        * space    (int) - An MSpace constant giving the coordinate space
                           in which to perform the operation
        """
        pass

    def numBoundaries(*args, **kwargs):
        """
        numBoundaries(region) -> unsigned int

        Returns the number of boundaries for the specified region. The
        surface must be a trimmed surface.

        For each region there may be several boundary curves, an outer curve
        and possibly several inner boundary curves which define holes. These
        boundary curves are made up of one or more curves called edges.

        * region (int) - Region of interest.
        """
        pass

    def numEdges(*args, **kwargs):
        """
        numEdges(region, boundary) -> unsigned int

        Returns the number of edges for the specified trim boundary.
        For each region there may be several boundary curves, an outer curve
        and possibly several inner boundary curves which define holes. These
        boundary curves are made up of one or more curves called edges.

        * region   (int) - Region of interest.
        * boundary (int) - Boundary of interest
        """
        pass

    def projectCurve(*args, **kwargs):
        """
        projectCurve(curve[, direction], keepHistory=False) -> self

        Projects the given curve onto the surface, creating a curve on surface.

        * direction (MVector) - Direction of projection. If not supplied
                                then surface normals will be used.
        * keepHistory  (bool) - Determines whether the construction history
                                of the projection should be retained.
        """
        pass

    def removeKnotInU(*args, **kwargs):
        """
        removeKnotInU(param, removeAll=False) -> self

        Removes one or more U knots at the specified parameter value from
        from the surface.

        * param    (float) - U parameter value of the knot to remove.
        * removeAll (bool) - If True and there are multiple knots at the
                             parameter value then they will all be removed.
                             Otherwise, all but one will be removed.
        """
        pass

    def removeKnotInV(*args, **kwargs):
        """
        removeKnotInV(param, removeAll=False) -> self

        Removes one or more V knots at the specified parameter value from
        from the surface.

        * param    (float) - V parameter value of the knot to remove.
        * removeAll (bool) - If True and there are multiple knots at the
                             parameter value then they will all be removed.
                             Otherwise, all but one will be removed.
        """
        pass

    def removeOneKnotInU(*args, **kwargs):
        """
        removeOneKnotInU(param) -> self

        Removes one U knot at the specified parameter value. If there are
        multiple knots at that the value the others are retained.

        * param (float) - U parameter value of the knot to remove.
        """
        pass

    def removeOneKnotInV(*args, **kwargs):
        """
        removeOneKnotInV(param) -> self

        Removes one V knot at the specified parameter value. If there are
        multiple knots at that the value the others are retained.

        * param (float) - V parameter value of the knot to remove.
        """
        pass

    def setCVPosition(*args, **kwargs):
        """
        setCVPosition(uIndex, vIndex, point, space=kObject) -> self
        """
        pass

    def setCVPositions(*args, **kwargs):
        """
        setCVPositions(points, space=kObject) -> self

        Set the positions of all of the surface's CVs.
        (numCVsInU * numCVsInV) points must be provided. Converting from
        U and V indices to array indices is done by:

                array index = numCVsInV * U index + V index

        To keep this method as fast as possible, no checking of the data is
        performed beyond ensuring that the total number of CVs passed in is
        correct. It is up to the caller to ensure that the CVs provide a
        valid surface, for example by ensuring that overlapping CVs in
        periodic surfaces have the same positions.

        * points (MPointArray or seq of MPoint)
                       - Positions of the CVs.
        * space  (int) - An MSpace constant giving the coordinate space
                         in which to perform the operation
        """
        pass

    def setKnotInU(*args, **kwargs):
        """
        setKnotInU(index, param) -> self

        Sets the value of an existing U knot. U knots are indexed from 0 to
        numKnotsInU-1. Note that this method does not insert a new knot, it
        simply changes the value of an existing knot.

        If a knot value is set that breaks the non-decreasing requirement
        for the knot array, the knot value will be changed and an exception
        raised.

        * index   (int) - U index of the knot to set.
        * param (float) - New parameter value for the knot.
        """
        pass

    def setKnotInV(*args, **kwargs):
        """
        setKnotInV(index, param) -> self

        Sets the value of an existing V knot. V knots are indexed from 0 to
        numKnotsInV-1. Note that this method does not insert a new knot, it
        simply changes the value of an existing knot.

        If a knot value is set that breaks the non-decreasing requirement
        for the knot array, the knot value will be changed and an exception
        raised.

        * index   (int) - V index of the knot to set.
        * param (float) - New parameter value for the knot.
        """
        pass

    def setKnotsInU(*args, **kwargs):
        """
        setKnotsInU(params, startIndex, endIndex) -> self

        Sets the values of a range of U knots.

        * params     (MDoubleArray or seq of float)
                           - Parameter values to set at the knots. One value
                             per knot in the range.
        * startIndex (int) - Index of the first U knot to set.
        * endIndex   (int) - Index of the last U knot to set.
        """
        pass

    def setKnotsInV(*args, **kwargs):
        """
        setKnotsInV(params, startIndex, endIndex) -> self

        Sets the values of a range of V knots.

        * params     (MDoubleArray or seq of float)
                           - Parameter values to set at the knots. One value
                             per knot in the range.
        * startIndex (int) - Index of the first V knot to set.
        * endIndex   (int) - Index of the last V knot to set.
        """
        pass

    def setUV(*args, **kwargs):
        """
        setUV(uvId, u, v) -> self

        Sets a single texture coordinate. If 'uvId' is greater than or equal
        to numUVs then the surface's uv list will be grown to accommodate it.

        Note that API methods that modify uv data work correctly either when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * uvId (int) - Index of the element in the surface's uv list to set.
        * u  (float) - U value to set the uv to.
        * v  (float) - V value to set the uv to.
        """
        pass

    def setUVs(*args, **kwargs):
        """
        setUVs(uList, vList) -> self

        Sets all of the texture coordinates (uvs) for this surface. The
        arrays must be of equal length and must be at least of length numUVs.
        If the arrays are larger than numUVs then the uv list for this surface
        will be grown to accommodate the new uv values.

        After using this method to set the UV values, you can call
        assignUVs to assign the corresponding UVids to the geometry.

        Note that API methods that modify uv data work correctly either when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * uList (MFloatArray or seq of float) - U values to set
        * vList (MFloatArray or seq of float) - V values to set
        """
        pass

    def tangents(*args, **kwargs):
        """
        tangents(uParam, vParam, space=kObject) -> (MVector, MVector)

        Returns the tangents in the U and V directions at a given parameter
        value on the surface. The returned tangent vectors are normalized.

        This method does not fail if the given parameter lies within a
        trimmed away region of a trimmed surface. Use isPointInTrimmedRegion()
        to determine if the uv point lies within such a region.

        * uParam (float) - U parameter value at which to obtain the tangents.
        * vParam (float) - V parameter value at which to obtain the tangents.
        * space    (int) - An MSpace constant giving the coordinate space
                           in which to perform the operation
        """
        pass

    def trim(*args, **kwargs):
        """
        trim(regionsToKeepU, regionsToKeepV, keepHistory=False) -> self

        Trims the surface to its curves on surface. Regions which are kept
        are specified by passing in arrays of u,v parameters.

        This method will create a new trimmed surface in the DAG. The surface
        attached to this function set will remain unchanged.

        * regionsToKeepU (MDoubleArray or seq of float)
                                - U parameters of points within the regions
                                  to be kept.
        * regionsToKeepV (MDoubleArray or seq of float)
                                - V parameters of points within the regions
                                  to be kept.
        * keepHistory    (bool) - Determines whether the construction history
                                  of the operation should be retained.
        """
        pass

    def updateSurface(*args, **kwargs):
        """
        updateSurface() -> self

        Signals that this surface has changed and needs to be recalculated.

        This method is useful when a large number of CVs for the surface are
        being modified. Instead of updating the surface every time a CV is
        changed it is more efficient to call this method once after all the
        updates are complete.
        """
        pass

    dataObject = None

    degreeInU = None

    degreeInV = None

    formInU = None

    formInV = None

    hasHistoryOnCreate = None

    isBezier = None

    isFoldedOnBispan = None

    isTrimmedSurface = None

    isUniform = None

    kClosed = 2

    kClosedSegment = 4

    kInner = 2

    kInvalid = 0

    kInvalidBoundary = 0

    kLast = 4

    kOpen = 1

    kOuter = 1

    kPeriodic = 3

    kPointTolerance = 0.001

    kSegment = 3

    knotDomainInU = None

    knotDomainInV = None

    numCVsInU = None

    numCVsInV = None

    numKnotsInU = None

    numKnotsInV = None

    numNonZeroSpansInU = None

    numNonZeroSpansInV = None

    numPatches = None

    numPatchesInU = None

    numPatchesInV = None

    numRegions = None

    numSpansInU = None

    numSpansInV = None

    numUVs = None


class MFnNurbsCurve(MFnDagNode):
    """
    NURBS (Non-Uniform Rational B-Spline) curve function set.

    The shape of a NURBS curve is defined by an array of CVs
    (control vertices), an array of knot values, a degree, and a
    form.  There are 3 possible 'forms' for the curve: open,
    closed and periodic.

    The open and closed forms are quite similar, and in fact a
    closed curve will become an open curve if either the first
    or last CV is moved so that they are no longer coincident.
    To create an open or closed curve of degree N with M spans,
    you must provide M+N CVs.  This implies that for a degree N
    curve, you must specify at least N+1 CVs to get a curve with
    a single span.

    The number of knots required for a curve is M + 2N - 1. If
    you want the curve to start exactly at the first CV and end
    exactly at the last CV, then the knot vector must be
    structured to have degree N 'multiplicity' at the beginning
    and end.  This means that the first N knots must be
    identical, and the last N knots must be identical.

    A periodic curve is a special case of a closed curve.
    Instead of having just the first and last CVs coincident,
    the last N CVs in the curve must overlap the first N CVs.
    This results in a curve with no tangent break at the seam
    where the ends meet.  The last N CVs in a periodic curve are
    permanently bound to the first N CVs, and Maya will not
    allow those last N CVs to be repositioned.  If one or more
    of the first N CVs of the curve are repositioned, the
    overlapping CV's will remain bound, and will also be moved.

    In order to create a periodic curve, you must specify at
    least 2N+1 CVs, so that that last N can overlap the first N
    and you still have 1 non-overlapping CV left.  The number of
    CVs required to create a periodic curve is still N+M (with a
    lower limit of 2N+1), but you must ensure that the positions
    of the last N CVs are identical to the positions of the
    first N.

    You still need M + 2N - 1 knots for a periodic curve, but
    the knot values required are more restrictive than for open
    or closed curves because of the overlap at the ends, The
    difference between the first N pairs of knots values should
    be equal to the difference between the last N pairs.
    Additionally there can be no knot multiplicity at the ends
    of the curve, because that would compromise the tangent
    continuity property. So an example knot sequence could begin
    with knots at { -(N-2), -(N-1), ... , 0}.

    Note that some third party applications use a different
    format for knots, where the number of knots required for a
    curve is M+2N+1 rather than M+2N-1 as used in Maya. Both
    knot representations are equivalent mathematically. To
    convert from one of these external representations into the
    Maya representation, simply omit the first and last knots
    from the external representation when creating the Maya
    representation. To convert from the Maya representation into
    the external representation, add two new knots at the
    beginning and end of the Maya knot sequence. The value of
    these new knots depends on the existing knot sequence. For a
    knot sequence with multiple end knots, simply duplicate the
    existing first and last knots once more, for example:

    Maya representation: {0,0,0,...,N,N,N}
    External representation: {0,0,0,0,...,N,N,N,N}

    For a knot sequence with uniform end knots, create the new
    knots offset at an interval equal to the existing first and
    last knot intervals, for example:

    Maya representation: {0,1,2,...,N,N+1,N+2}
    External representation: {-1,0,1,2,...,N,N+1,N+2,N+3}
    """

    def __init__(*args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        pass

    def area(*args, **kwargs):
        """
        area(tolerance=kPointTolerance) -> float

        Returns the area bounded by the curve. The curve must be closed and
        planar. A value of 0.0 will be returned if area cannot be determined.

        * tolerance (float) - Amount of error allowed in the calculation
        """
        pass

    def closestPoint(*args, **kwargs):
        """
        closestPoint(testPoint, guess=None, tolerance=kPointTolerance,
            space=kObject) -> (MPoint, float)

        Returns a tuple containing the point on the curve which is closest
        to 'testPoint', and the parameter value at which that point occurs.

        * testPoint (MPoint) - point to get closest to
        * guess      (float) - a guess as to roughly where on the curve the
                               closest point will be. If the guess is in the
                               correct span than it can significantly speed
                               up the search. If not then it may slow down
                               the search a bit. If no guess is supplied
                               then the search will begin at the start of
                               the curve.
        * tolerance  (float) - maximum allowed distance between the curve
                               and the returned point.
        * space (MSpace constant) - coordinate space to use for the points
        """
        pass

    def copy(*args, **kwargs):
        """
        copy(source, parent=MObject.kNullObj) -> MObject

        Returns a new NURBS curve which is a copy of 'source' and resets
        the functionset to operate on it.

        * parent (MObject)
                     - the parent/owner of the new curve. If it's a NURBS
                       curve data wrapper (MFn.kNurbsCurveData) then the
                       created curve will be returned as a geometry object
                       (MFn.kNurbsCurveGeom) owned by the wrapper. If
                       'parent' is a DAG node then the new curve will be
                       returned as nurbsCurve node parented under it. If
                       'parent' is not provided then a new top-level
                       transform will be created with the new curve parented
                       beneath it as a nurbsCurve node. In this last case it
                       will be the transform node which is returned.
        """
        pass

    def create(*args, **kwargs):
        """
        create(cvs, knots, degree, form, is2D, rational, parent=kNullObj)
            -> self
        create(subCurves, parent=kNullObj) -> self

        Returns a newly created curve and resets the functionset to operate
        on it. The first version creates the curve based on the control
        vertices and knots provided while the second creates the curve as a
        copy of the provided subCurves, all joined together.

        * cvs (MPointArray or seq of MPoint)
                     - positions of the control vertices
        * knots (MDoubleArray seq of float)
                     - parameter values of the knots. There must be
                       (# spans + 2*degree - 1) knots provided and they must
                       appear in non-decreasing order.
        * degree (int) - degree of the curve to create
        * form (int) - one of kOpen, kClosed or kPeriodic
        * is2d (bool)- if True the Z-coordinates of 'cvs' will be ignored,
                       giving a curve in the local XY plane.
        * rational (bool)
                     - set True if you want the new curve to be rational
        * parent (MObject)
                     - the parent/owner of the new curve. If it's a NURBS
                       curve data wrapper (MFn.kNurbsCurveData) then the
                       created curve will be returned as a geometry object
                       (MFn.kNurbsCurveGeom) owned by the wrapper. If
                       'parent' is a DAG node then the new curve will be
                       returned as nurbsCurve node parented under it. If
                       'parent' is not provided then a new top-level
                       transform will be created with the new curve parented
                       beneath it as a nurbsCurve node. In this last case it
                       will be the transform node which is returned.
        * subCurves (MObjectArray or seq of MObject)
                     - array of curves from which the new curve will be built
                       The curves must all be in the same direction, must not
                       intersect themselves or each other, the start of each
                       curve in the array must be coincident with the end of
                       the previous curve in the array, and the curves must be
                       be at least C0 continuous (i.e. tangent breaks are okay).
        """
        pass

    def createWithEditPoints(*args, **kwargs):
        """
        createWithEditPoints(eps, degree, form, is2D, rational, uniform,
            parent=kNullObj) -> MObject

        Returns a new curve based on the given edit points (i.e. points
        which lie on the curve) and resets the functionset to operate on it.

        * eps (MPointArray or seq of MPoint)
                     - positions of the edit points
        * degree (int) - degree of the curve to create
        * form (int) - one of kOpen, kClosed or kPeriodic
        * is2d (bool)- if True the Z-coordinates of 'eps' will be ignored,
                       giving a curve in the local XY plane.
        * rational (bool)
                     - set True if you want the new curve to be rational
        * uniform (bool)
                     - if True then parameter values of the knots will be
                       uniformly spaced, otherwise they will be based on
                       chord length.
        * parent (MObject)
                     - the parent/owner of the new curve. If it's a NURBS
                       curve data wrapper (MFn.kNurbsCurveData) then the
                       created curve will be returned as a geometry object
                       (MFn.kNurbsCurveGeom) owned by the wrapper. If
                       'parent' is a DAG node then the new curve will be
                       returned as nurbsCurve node parented under it. If
                       'parent' is not provided then a new top-level
                       transform will be created with the new curve parented
                       beneath it as a nurbsCurve node. In this last case it
                       will be the transform node which is returned.
        """
        pass

    def cvPosition(*args, **kwargs):
        """
        cvPosition(index, space=kObject) -> MPoint

        Returns the position of a single control vertex.

        * index (int) - index of the CV to return
        * space (int) - an MSpace constant giving the coordinate space in
                        which the point is given
        """
        pass

    def cvPositions(*args, **kwargs):
        """
        cvPositions(space=kObject) -> MPointArray

        Returns the positions of all of the curve's control vertices.

        * space (int) - an MSpace constant giving the coordinate space in
                        which the point is given
        """
        pass

    def cvs(*args, **kwargs):
        """
        cvs(startIndex[, endIndex]) -> MObject

        Returns a CV or a range of CVs as a component. MItCurveCV can be
        used to examine or modify the CVs in the component. Any modifications
        made to them will affect the curve. After all modifications are done,
        updateCurve() should be called to have the curve recalculate its
        cached geometry.

        * startIndex (int) - start of the range of CVs to return.
        * endIndex   (int) - end of the range of CVs to return. If not
                             provided then only the CV specified by
                             startIndex will be returned.
        """
        pass

    def distanceToPoint(*args, **kwargs):
        """
        distanceToPoint(point, space=kObject) -> float

        Returns the distance from the given point to the point on the curve
        which is closest to it.

        * point (MPoint) - the point to calculate the distance to
        * space (int)    - an MSpace constant giving the coordinate space in
                           which the point is given
        """
        pass

    def findLengthFromParam(*args, **kwargs):
        """
        findLengthFromParam(param) -> float

        Returns the length along the curve corresponding to a given
        parameter value on the curve. If the length cannot be found for
        the given parameter value then a length of zero is returned.

        * param (float) - parameter value on the curve
        """
        pass

    def findParamFromLength(*args, **kwargs):
        """
        findParamFromLength(length) -> float

        Returns the parameter value corresponding to a given length along
        the curve. If the parameter value cannot be determined then the value
        for the end point of the curve is returned.

        * length (float) - distance along the curve
        """
        pass

    def getDerivativesAtParam(*args, **kwargs):
        """
        getDerivativesAtParam(param, space=kObject) -> (MPoint, MVector[, MVector])

        Evaluates the curve at the given parameter value, returning a tuple
        containing the position and first derivative at that value. If 'dUU'
        is True then the returned tuple will include the second derivative
        as well as its third element.

        * param (float) - parameter value at which to do the evaluation
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the point is given
        * dUU    (bool) - if True include the second derivative in the result.
        """
        pass

    def getParamAtPoint(*args, **kwargs):
        """
        getParamAtPoint(point, tolerance=kPointTolerance, space=kObject) -> float

        Returns the parameter value corresponding to the given point on the
        curve.

        * point    (MPoint) - point on curve.
        * tolerance (float) - max distance 'point' can be from the curve and
                              still be considered to lie on it.
        * space       (int) - an MSpace constant giving the coordinate space
                              in which the point is given
        """
        pass

    def getPointAtParam(*args, **kwargs):
        """
        getPointAtParam(param, space=kObject) -> MPoint

        Returns the point on the curve at the given parameter value.

        * param (float) - parameter value at which to find the point
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the point should be returned
        """
        pass

    def isParamOnCurve(*args, **kwargs):
        """
        isParamOnCurve(param) -> bool

        Returns True if the given parameter value lies on the curve (i.e. is
        within the curve's knot domain), False otherwise.

        * param (float) - parameter value to test
        """
        pass

    def isPointOnCurve(*args, **kwargs):
        """
        isPointOnCurve(point, tolerance=kPointTolerance, space=kObject) -> bool

        Returns True if the given point lies on the curve, False otherwise.

        * point    (MPoint) - point to test.
        * tolerance (float) - max distance 'point' can be from the curve and
                              still be considered to lie on it.
        * space       (int) - an MSpace constant giving the coordinate space
                              in which the point is given
        """
        pass

    def knot(*args, **kwargs):
        """
        knot(index) -> float

        Returns the parameter value of a single knot.

        * index (int) - index of the knot to return. These range from 0 to
                        (numKnots - 1)
        """
        pass

    def knots(*args, **kwargs):
        """
        knots() -> MDoubleArray

        Returns the parameter values for all of the curve's knots.
        """
        pass

    def length(*args, **kwargs):
        """
        length(tolerance=kPointTolerance) -> float

        Returns the arc length of this curve or 0.0 if it cannot be computed.

        * tolerance (float) - max error allowed in the calculation.
        """
        pass

    def makeMultipleEndKnots(*args, **kwargs):
        """
        makeMultipleEndKnots() -> self

        Sets the curve's end knots to have full multiplicity. This ensures
        that the end points interpolate the first and last CVs (i.e. lie
        directly on them). It can also be used to convert a periodic curve
        to a closed curve.
        """
        pass

    def normal(*args, **kwargs):
        """
        normal(param, space=kObject) -> MVector

        Returns the normal at the given parameter value on the curve. For
        degree 1 curves the normal is the vector at right angles to the
        curve that lies in the average plane of the curve. For higher degrees
        the normal is defined by the local curvature at the parameter.

        * param (float) - parameter value at which to find the normal
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the normal should be returned
        """
        pass

    def removeKnot(*args, **kwargs):
        """
        removeKnot(param, removeAll=False) -> self

        Removes one or more knots at the given parameter value.

        If there are multiple knots at the parameter value then 'removeAll'
        determines which ones will be removed. If it is True then they will
        all be removed. If it is False then all but one will be removed.

        * param     (float) - parameter of the knot
        * removeAll  (bool) - how to handle multiple knots at the same param
        """
        pass

    def reverse(*args, **kwargs):
        """
        reverse() -> self

        Reverses the direction of the curve.
        """
        pass

    def setCVPosition(*args, **kwargs):
        """
        setCVPosition(index, point, space=kObject) -> self

        Sets the position of a single control vertex of the curve.

        * index    (int) - index of the cv
        * point (MPoint) - new position for the cv
        * space    (int) - an MSpace constant giving the coordinate space
                           in which the point is given
        """
        pass

    def setCVPositions(*args, **kwargs):
        """
        setCVPositions(points, space=kObject) -> self

        Sets the positions of all of the curve's control vertices.

        * points (MPointArray or seq of MPoint)
                       - the points to be set. The array/sequence must
                         contain exactly the same number of points as the
                         curve has control vertices.
        * space  (int) - an MSpace constant giving the coordinate space
                         in which the points are given
        """
        pass

    def setKnot(*args, **kwargs):
        """
        setKnot(index, param) -> self

        Sets the parameter value of a single knot.
        * index   (int) - index of the knot
        * param (float) - new parameter value for the knot
        """
        pass

    def setKnots(*args, **kwargs):
        """
        setKnots(params, startIndex, endIndex) -> self

        Sets the parameter values of a contiguous group of knots.

        * params (MDoubleArray of seq of float)
                           - the parameter values to set, one per knot in
                             the range
        * startIndex (int) - first knot in the range to be set
        * endIndex   (int) - last knot in the range to be set
        """
        pass

    def tangent(*args, **kwargs):
        """
        tangent(param, space=kObject) -> MVector

        Returns the normalized tangent vector at the given parameter value
        on the curve.

        * param (float) - parameter value at which to find the tangent
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the tangent should be returned
        """
        pass

    def updateCurve(*args, **kwargs):
        """
        updateCurve() -> self

        Tells the shape node which represents the curve in the scene, if
        any, that the curve has changed and needs to be redrawn.
        """
        pass

    degree = None

    form = None

    hasHistoryOnCreate = None

    isPlanar = None

    kClosed = 2

    kInvalid = 0

    kLast = 4

    kOpen = 1

    kPeriodic = 3

    kPointTolerance = 0.001

    knotDomain = None

    numCVs = None

    numKnots = None

    numSpans = None

    planeNormal = None


py2dict = {}

key = 'MRampAttribute'

ourdict = {}


class World(MObject):

    def __init__(self):
        super().__init__()
        self._is_world = True
        self._alive = True
        self._name = 'world'
        self._api_type.append(MFn.kWorld)


class _NodeTypeIds(enum.Enum):
    AISEnvFacade = MTypeId(0x52454656)
    AboutToSetValueTestNode = MTypeId(0x4153564e)
    AbsOverride = MTypeId(0x58000378)
    AbsUniqueOverride = MTypeId(0x580003a0)
    Absolute = MTypeId(0x41425344)
    Acos = MTypeId(0x41434f53)
    AddDoubleLinear = MTypeId(0x4441444c)
    AddMatrix = MTypeId(0x44414d58)
    AdskMaterial = MTypeId(0x4144534d)
    AimConstraint = MTypeId(0x44414d43)
    AimMatrix = MTypeId(0x414d4154)
    AirField = MTypeId(0x59414952)
    AirManip = MTypeId(0x554d4958)
    AlignCurve = MTypeId(0x4e414c43)
    AlignManip = MTypeId(0x554d4144)
    AlignSurface = MTypeId(0x4e414c53)
    AmbientLight = MTypeId(0x414d424c)
    And = MTypeId(0x414e4442)
    AngleBetween = MTypeId(0x4e414254)
    AngleDimension = MTypeId(0x4147444e)
    AnimBlend = MTypeId(0x41424e44)
    AnimBlendInOut = MTypeId(0x4142494f)
    AnimBlendNodeAdditive = MTypeId(0x41424e41)
    AnimBlendNodeAdditiveDA = MTypeId(0x41424141)
    AnimBlendNodeAdditiveDL = MTypeId(0x4142414c)
    AnimBlendNodeAdditiveF = MTypeId(0x41424146)
    AnimBlendNodeAdditiveFA = MTypeId(0x41424641)
    AnimBlendNodeAdditiveFL = MTypeId(0x4142464c)
    AnimBlendNodeAdditiveI16 = MTypeId(0x41424153)
    AnimBlendNodeAdditiveI32 = MTypeId(0x41424149)
    AnimBlendNodeAdditiveRotation = MTypeId(0x41424e52)
    AnimBlendNodeAdditiveScale = MTypeId(0x41424e53)
    AnimBlendNodeBoolean = MTypeId(0x4142424f)
    AnimBlendNodeEnum = MTypeId(0x41424e45)
    AnimBlendNodeTime = MTypeId(0x41425449)
    AnimClip = MTypeId(0x434c504e)
    AnimCurveTA = MTypeId(0x50435441)
    AnimCurveTL = MTypeId(0x5043544c)
    AnimCurveTT = MTypeId(0x50435454)
    AnimCurveTU = MTypeId(0x50435455)
    AnimCurveUA = MTypeId(0x50435541)
    AnimCurveUL = MTypeId(0x5043554c)
    AnimCurveUT = MTypeId(0x50435554)
    AnimCurveUU = MTypeId(0x50435555)
    AnimLayer = MTypeId(0x414e4c52)
    Anisotropic = MTypeId(0x52414e49)
    AnnotationShape = MTypeId(0x414e4e53)
    AovChildCollection = MTypeId(0x5800039c)
    AovCollection = MTypeId(0x5800039b)
    ApplyAbs2FloatsOverride = MTypeId(0x58000397)
    ApplyAbs3FloatsOverride = MTypeId(0x58000381)
    ApplyAbsBoolOverride = MTypeId(0x5800038a)
    ApplyAbsEnumOverride = MTypeId(0x5800038c)
    ApplyAbsFloatOverride = MTypeId(0x5800037d)
    ApplyAbsIntOverride = MTypeId(0x58000391)
    ApplyAbsStringOverride = MTypeId(0x58000393)
    ApplyConnectionOverride = MTypeId(0x58000384)
    ApplyRel2FloatsOverride = MTypeId(0x58000399)
    ApplyRel3FloatsOverride = MTypeId(0x58000383)
    ApplyRelFloatOverride = MTypeId(0x5800037f)
    ApplyRelIntOverride = MTypeId(0x58000392)
    ArcLengthDimension = MTypeId(0x41444d4e)
    AreaLight = MTypeId(0x41524c54)
    ArrayMapper = MTypeId(0x44414d50)
    ArrowManip = MTypeId(0x554d4152)
    ArubaTessellate = MTypeId(0x41544553)
    Asin = MTypeId(0x4153494e)
    Atan = MTypeId(0x4154414e)
    Atan2 = MTypeId(0x41544132)
    AttachCurve = MTypeId(0x4e415443)
    AttachSurface = MTypeId(0x4e415453)
    AttrHierarchyTest = MTypeId(0x41544854)
    Audio = MTypeId(0x41554449)
    Average = MTypeId(0x41565244)
    AvgCurves = MTypeId(0x4e414352)
    AvgNurbsSurfacePoints = MTypeId(0x4e414e50)
    AvgSurfacePoints = MTypeId(0x4e415350)
    AxisFromMatrix = MTypeId(0x584d4154)
    BallProjManip = MTypeId(0x554d4250)
    BarnDoorManip = MTypeId(0x554d4c4e)
    BaseLattice = MTypeId(0x46424153)
    BasicSelector = MTypeId(0x58000375)
    Bevel = MTypeId(0x4e42564c)
    BevelPlus = MTypeId(0x4e425356)
    BezierCurve = MTypeId(0x42435256)
    BezierCurveToNurbs = MTypeId(0x42544e52)
    BlendColorSets = MTypeId(0x50424353)
    BlendColors = MTypeId(0x52424c32)
    BlendDevice = MTypeId(0x424c4456)
    BlendFalloff = MTypeId(0x42464f46)
    BlendMatrix = MTypeId(0x424d4154)
    BlendShape = MTypeId(0x46424c53)
    BlendTwoAttr = MTypeId(0x41424c32)
    BlendWeighted = MTypeId(0x41424c57)
    BlindDataTemplate = MTypeId(0x424c4454)
    Blinn = MTypeId(0x52424c4e)
    BoneLattice = MTypeId(0x4642554c)
    Boolean = MTypeId(0x4e424f4c)
    Boundary = MTypeId(0x4e424e44)
    Brownian = MTypeId(0x5246424d)
    Brush = MTypeId(0x42525348)
    Bulge = MTypeId(0x52544255)
    Bump2d = MTypeId(0x5242554d)
    Bump3d = MTypeId(0x52425533)
    ButtonManip = MTypeId(0x55465054)
    CacheBlend = MTypeId(0x4354524b)
    CacheFile = MTypeId(0x43434846)
    Camera = MTypeId(0x4443414d)
    CameraManip = MTypeId(0x554d4958)
    CameraPlaneManip = MTypeId(0x554d4350)
    CameraSet = MTypeId(0x44525452)
    CameraView = MTypeId(0x44434156)
    Ceil = MTypeId(0x43454944)
    CenterManip = MTypeId(0x434e4d50)
    Character = MTypeId(0x43484152)
    CharacterMap = MTypeId(0x434d4150)
    CharacterOffset = MTypeId(0x584f4646)
    Checker = MTypeId(0x52544348)
    Choice = MTypeId(0x43484345)
    Chooser = MTypeId(0x43484f4f)
    CircleManip = MTypeId(0x554d434c)
    CircleSweepManip = MTypeId(0x5543534d)
    Clamp = MTypeId(0x52434c33)
    ClampRange = MTypeId(0x434c414d)
    ClipGhostShape = MTypeId(0x43475348)
    ClipLibrary = MTypeId(0x434c4950)
    ClipScheduler = MTypeId(0x43534348)
    ClipToGhostData = MTypeId(0x43324744)
    CloseCurve = MTypeId(0x4e434355)
    CloseSurface = MTypeId(0x4e435355)
    ClosestPointOnMesh = MTypeId(0x43504f4d)
    ClosestPointOnSurface = MTypeId(0x4e435053)
    Cloth = MTypeId(0x5254434c)
    Cloud = MTypeId(0x52544344)
    Cluster = MTypeId(0x46434c53)
    ClusterFlexorShape = MTypeId(0x464a4346)
    ClusterHandle = MTypeId(0x46434c48)
    CoiManip = MTypeId(0x55465054)
    Collection = MTypeId(0x58000373)
    CollisionModel = MTypeId(0x59434f4c)
    ColorManagementGlobals = MTypeId(0x434d4742)
    ColorProfile = MTypeId(0x434f4c50)
    ColumnFromMatrix = MTypeId(0x434d4154)
    CombinationShape = MTypeId(0x46434e53)
    CompactPlugArrayTest = MTypeId(0x43504154)
    ComponentFalloff = MTypeId(0x47464f46)
    ComponentManip = MTypeId(0x5554544d)
    ComponentMatch = MTypeId(0x544f504d)
    ComponentTagBase = MTypeId(0x43544253)
    ComposeMatrix = MTypeId(0x58000301)
    ConcentricProjManip = MTypeId(0x554d434f)
    Condition = MTypeId(0x52434e44)
    ConnectionOverride = MTypeId(0x58000385)
    ConnectionUniqueOverride = MTypeId(0x580003a2)
    Container = MTypeId(0x434f4e54)
    ContainerBase = MTypeId(0x434f4241)
    Contrast = MTypeId(0x52434f4e)
    Controller = MTypeId(0x43475250)
    CopyColorSet = MTypeId(0x43504353)
    CopyUVSet = MTypeId(0x43505553)
    Cos = MTypeId(0x434f5349)
    CpManip = MTypeId(0x554d4350)
    Crater = MTypeId(0x52533430)
    CreaseSet = MTypeId(0x43524541)
    CreateColorSet = MTypeId(0x43524353)
    CreateUVSet = MTypeId(0x43525553)
    CrossProduct = MTypeId(0x43524f50)
    CubicProjManip = MTypeId(0x554d4355)
    CurveFromMeshCoM = MTypeId(0x4e434d43)
    CurveFromMeshEdge = MTypeId(0x4e434d45)
    CurveFromSubdivEdge = MTypeId(0x53435345)
    CurveFromSubdivFace = MTypeId(0x53435346)
    CurveFromSurfaceBnd = MTypeId(0x4e435342)
    CurveFromSurfaceCoS = MTypeId(0x4e435343)
    CurveFromSurfaceIso = MTypeId(0x4e435349)
    CurveInfo = MTypeId(0x4e43494e)
    CurveIntersect = MTypeId(0x4e434349)
    CurveNormalizerAngle = MTypeId(0x434e5241)
    CurveNormalizerLinear = MTypeId(0x434e524c)
    CurveSegmentManip = MTypeId(0x554d5043)
    CurveVarGroup = MTypeId(0x4e435647)
    CylindricalProjManip = MTypeId(0x554d4359)
    DagContainer = MTypeId(0x44414743)
    DagPose = MTypeId(0x46504f53)
    DataBlockTest = MTypeId(0x44425453)
    DecomposeMatrix = MTypeId(0x58000300)
    DefaultLightList = MTypeId(0x4445464c)
    DefaultRenderUtilityList = MTypeId(0x4452554c)
    DefaultRenderingList = MTypeId(0x44524e4c)
    DefaultShaderList = MTypeId(0x5244534c)
    DefaultTextureList = MTypeId(0x5244544c)
    DeformBend = MTypeId(0x46444244)
    DeformFlare = MTypeId(0x4644464c)
    DeformSine = MTypeId(0x4644534e)
    DeformSquash = MTypeId(0x46445351)
    DeformTwist = MTypeId(0x46445457)
    DeformWave = MTypeId(0x46445756)
    DeleteColorSet = MTypeId(0x444c4353)
    DeleteComponent = MTypeId(0x44454354)
    DeleteUVSet = MTypeId(0x444c4d53)
    DeltaMush = MTypeId(0x444c544d)
    DetachCurve = MTypeId(0x4e445443)
    DetachSurface = MTypeId(0x4e445453)
    Determinant = MTypeId(0x4445544d)
    DirectedDisc = MTypeId(0x44445343)
    DirectionManip = MTypeId(0x55465054)
    DirectionalLight = MTypeId(0x4449524c)
    DiscManip = MTypeId(0x5544534d)
    DiskCache = MTypeId(0x44534b43)
    DisplacementShader = MTypeId(0x52445348)
    DisplayLayer = MTypeId(0x4453504c)
    DisplayLayerManager = MTypeId(0x44504c4d)
    DistanceBetween = MTypeId(0x44444254)
    DistanceDimShape = MTypeId(0x44444d4e)
    DistanceManip = MTypeId(0x554d444d)
    Divide = MTypeId(0x44495644)
    Dof = MTypeId(0x444f4644)
    DofManip = MTypeId(0x554d4350)
    DotProduct = MTypeId(0x444f5450)
    DoubleShadingSwitch = MTypeId(0x53574832)
    DpBirailSrf = MTypeId(0x4e444253)
    DragField = MTypeId(0x59445247)
    DropoffLocator = MTypeId(0x444c4354)
    DynAttenuationManip = MTypeId(0x554d444d)
    DynController = MTypeId(0x5943544c)
    DynGlobals = MTypeId(0x5944474c)
    DynHolder = MTypeId(0x59484c44)
    DynSpreadManip = MTypeId(0x554d444d)
    DynamicConstraint = MTypeId(0x44434f4e)
    EditMetadata = MTypeId(0x454d5444)
    EditsManager = MTypeId(0x454d4752)
    EmitterManip = MTypeId(0x554d4958)
    EnableManip = MTypeId(0x454e4d50)
    EnvBall = MTypeId(0x5245424c)
    EnvChrome = MTypeId(0x52454348)
    EnvCube = MTypeId(0x52454342)
    EnvFacade = MTypeId(0x52454643)
    EnvFog = MTypeId(0x52454647)
    EnvSky = MTypeId(0x5245534b)
    EnvSphere = MTypeId(0x52455350)
    EnvironmentFog = MTypeId(0x454e5646)
    Equal = MTypeId(0x4551554c)
    ExplodeNurbsShell = MTypeId(0x4e455348)
    Expression = MTypeId(0x44455850)
    ExtendCurve = MTypeId(0x4e455843)
    ExtendSurface = MTypeId(0x4e455853)
    Extrude = MTypeId(0x4e455852)
    Facade = MTypeId(0x4446434e)
    FalloffEval = MTypeId(0x45464f46)
    FfBlendSrf = MTypeId(0x4e424c54)
    FfBlendSrfObsolete = MTypeId(0x4e424c53)
    FfFilletSrf = MTypeId(0x4e464653)
    Ffd = MTypeId(0x46464644)
    FieldManip = MTypeId(0x554d4958)
    FieldsManip = MTypeId(0x554d4958)
    File = MTypeId(0x52544654)
    FilletCurve = MTypeId(0x4e464352)
    FitBspline = MTypeId(0x4e465443)
    FlexorShape = MTypeId(0x464c5848)
    Floor = MTypeId(0x464c4f4f)
    Flow = MTypeId(0x464c4f57)
    FluidEmitter = MTypeId(0x46454d49)
    FluidShape = MTypeId(0x464c5549)
    FluidSliceManip = MTypeId(0x46534c4d)
    FluidTexture2D = MTypeId(0x464c5454)
    FluidTexture3D = MTypeId(0x464c5458)
    Follicle = MTypeId(0x48435256)
    ForceUpdateManip = MTypeId(0x554d4655)
    FosterParent = MTypeId(0x4650524e)
    FourByFourMatrix = MTypeId(0x4642464d)
    Fractal = MTypeId(0x52543246)
    FrameCache = MTypeId(0x46434348)
    FreePointManip = MTypeId(0x554d4650)
    FreePointTriadManip = MTypeId(0x55465054)
    GammaCorrect = MTypeId(0x5247414d)
    GeoConnectable = MTypeId(0x5947434f)
    GeoConnector = MTypeId(0x59474354)
    GeomBind = MTypeId(0x4742494e)
    GeometryConstraint = MTypeId(0x44474e43)
    GeometryFilter = MTypeId(0x44474649)
    GeometryOnLineManip = MTypeId(0x554d474c)
    GeometryVarGroup = MTypeId(0x4e475647)
    GlobalCacheControl = MTypeId(0x4743434c)
    GlobalStitch = MTypeId(0x4e475354)
    Granite = MTypeId(0x52544752)
    GravityField = MTypeId(0x59475241)
    GreasePencilSequence = MTypeId(0x47505351)
    GreasePlane = MTypeId(0x4447504c)
    GreasePlaneRenderShape = MTypeId(0x47505253)
    GreaterThan = MTypeId(0x47525448)
    Grid = MTypeId(0x52544744)
    Group = MTypeId(0x580003a5)
    GroupId = MTypeId(0x47504944)
    GroupParts = MTypeId(0x47525050)
    Guide = MTypeId(0x46475549)
    HairConstraint = MTypeId(0x4850494e)
    HairSystem = MTypeId(0x48535953)
    HairTubeShader = MTypeId(0x52485442)
    HardenPoint = MTypeId(0x4e484450)
    HardwareRenderGlobals = MTypeId(0x48575247)
    HardwareRenderingGlobals = MTypeId(0x48525247)
    HeightField = MTypeId(0x4f435050)
    HierarchyTestNode1 = MTypeId(0x48544e31)
    HierarchyTestNode2 = MTypeId(0x48544e32)
    HierarchyTestNode3 = MTypeId(0x48544e33)
    HikEffector = MTypeId(0x4446494b)
    HikFKJoint = MTypeId(0x4a54494b)
    HikFloorContactMarker = MTypeId(0x4846434d)
    HikGroundPlane = MTypeId(0x48474e44)
    HikHandle = MTypeId(0x4b484948)
    HikIKEffector = MTypeId(0x494b4546)
    HikSolver = MTypeId(0x4b48494b)
    HistorySwitch = MTypeId(0x48495353)
    HoldMatrix = MTypeId(0x4450484d)
    HsvToRgb = MTypeId(0x52483252)
    HwReflectionMap = MTypeId(0x4857524d)
    HwRenderGlobals = MTypeId(0x59485244)
    HyperGraphInfo = MTypeId(0x48595052)
    HyperLayout = MTypeId(0x4859504c)
    HyperView = MTypeId(0x44485056)
    IkEffector = MTypeId(0x4b454646)
    IkHandle = MTypeId(0x4b48444c)
    IkMCsolver = MTypeId(0x4b4d4353)
    IkPASolver = MTypeId(0x4b504153)
    IkRPsolver = MTypeId(0x4b525053)
    IkSCsolver = MTypeId(0x4b534353)
    IkSplineSolver = MTypeId(0x4b535053)
    IkSystem = MTypeId(0x4b535953)
    ImagePlane = MTypeId(0x4449504c)
    ImplicitBox = MTypeId(0x46494258)
    ImplicitCone = MTypeId(0x4649434f)
    ImplicitSphere = MTypeId(0x46495350)
    IndexManip = MTypeId(0x554d4958)
    InsertKnotCurve = MTypeId(0x4e494b43)
    InsertKnotSurface = MTypeId(0x4e494b53)
    Instancer = MTypeId(0x594e5354)
    IntersectSurface = MTypeId(0x4e495346)
    InverseLerp = MTypeId(0x494c5250)
    Jiggle = MTypeId(0x4a474446)
    Joint = MTypeId(0x4a4f494e)
    JointCluster = MTypeId(0x464a434c)
    JointFfd = MTypeId(0x46464442)
    JointLattice = MTypeId(0x4642454c)
    KeyframeRegionManip = MTypeId(0x4b46524d)
    KeyingGroup = MTypeId(0x4b475250)
    Lambert = MTypeId(0x524c414d)
    Lattice = MTypeId(0x464c4154)
    LayeredShader = MTypeId(0x4c595253)
    LayeredTexture = MTypeId(0x4c595254)
    LeastSquaresModifier = MTypeId(0x4e4c534d)
    Leather = MTypeId(0x52544c45)
    Length = MTypeId(0x4c454e47)
    Lerp = MTypeId(0x4c455250)
    LessThan = MTypeId(0x4c535448)
    LightEditor = MTypeId(0x580003e3)
    LightFog = MTypeId(0x52464f47)
    LightGroup = MTypeId(0x580003e2)
    LightInfo = MTypeId(0x524c494e)
    LightItem = MTypeId(0x580003e1)
    LightLinker = MTypeId(0x524c4c4b)
    LightList = MTypeId(0x4c4c5354)
    LightManip = MTypeId(0x554d4958)
    LightsChildCollection = MTypeId(0x5800039a)
    LightsCollection = MTypeId(0x58000394)
    LightsCollectionSelector = MTypeId(0x580003a4)
    LimitManip = MTypeId(0x4c544d50)
    LineManip = MTypeId(0x554d4c4e)
    LineModifier = MTypeId(0x4c4d4f44)
    Locator = MTypeId(0x4c4f4354)
    LodGroup = MTypeId(0x4c4f4447)
    LodThresholds = MTypeId(0x4c4f4454)
    Loft = MTypeId(0x4e534b4e)
    Log = MTypeId(0x4c4f4744)
    LookAt = MTypeId(0x444c4154)
    Luminance = MTypeId(0x524c554d)
    MakeGroup = MTypeId(0x504d4752)
    MakeIllustratorCurves = MTypeId(0x4e4d4943)
    MakeNurbCircle = MTypeId(0x4e435243)
    MakeNurbCone = MTypeId(0x4e434e45)
    MakeNurbCube = MTypeId(0x4e435542)
    MakeNurbCylinder = MTypeId(0x4e43594c)
    MakeNurbPlane = MTypeId(0x4e504c4e)
    MakeNurbSphere = MTypeId(0x4e535048)
    MakeNurbTorus = MTypeId(0x4e544f52)
    MakeNurbsSquare = MTypeId(0x4e535152)
    MakeTextCurves = MTypeId(0x4e545843)
    MakeThreePointCircularArc = MTypeId(0x4e334341)
    MakeTwoPointCircularArc = MTypeId(0x4e324341)
    Mandelbrot = MTypeId(0x52544d41)
    Mandelbrot3D = MTypeId(0x52544d33)
    Manip2DContainer = MTypeId(0x554d3243)
    ManipContainer = MTypeId(0x554d4343)
    Marble = MTypeId(0x52544d52)
    MarkerManip = MTypeId(0x554d4d41)
    MaterialFacade = MTypeId(0x524d4643)
    MaterialInfo = MTypeId(0x444d5449)
    MaterialOverride = MTypeId(0x58000387)
    MaterialTemplate = MTypeId(0x4d544c41)
    MaterialTemplateOverride = MTypeId(0x58000389)
    Max = MTypeId(0x4d415844)
    Membrane = MTypeId(0x4d454d42)
    Mesh = MTypeId(0x444d5348)
    MeshVarGroup = MTypeId(0x4e4d5647)
    Min = MTypeId(0x4d494e44)
    Modulo = MTypeId(0x4d4f4444)
    Morph = MTypeId(0x4d525048)
    MotionPath = MTypeId(0x4d505448)
    MotionPathManip = MTypeId(0x554d4d41)
    MotionTrail = MTypeId(0x4d4f5452)
    MotionTrailShape = MTypeId(0x4d4f5348)
    Mountain = MTypeId(0x52544d54)
    MoveVertexManip = MTypeId(0x554d4650)
    Movie = MTypeId(0x52544d56)
    MpBirailSrf = MTypeId(0x4e4d4253)
    MultDoubleLinear = MTypeId(0x444d444c)
    MultMatrix = MTypeId(0x444d544d)
    MultilisterLight = MTypeId(0x4d554c4c)
    Multiply = MTypeId(0x4d554c54)
    MultiplyDivide = MTypeId(0x524d4449)
    MultiplyPointByMatrix = MTypeId(0x4d50424d)
    MultiplyVectorByMatrix = MTypeId(0x4d56424d)
    Mute = MTypeId(0x4d555445)
    NCloth = MTypeId(0x4e434c4f)
    NComponent = MTypeId(0x4e434d50)
    NParticle = MTypeId(0x4e504152)
    NRigid = MTypeId(0x4e524744)
    NearestPointOnCurve = MTypeId(0x4e504f43)
    Negate = MTypeId(0x4e454754)
    Network = MTypeId(0x4e54574b)
    NewtonField = MTypeId(0x594e4557)
    NewtonManip = MTypeId(0x554d4958)
    Noise = MTypeId(0x52544e33)
    NonLinear = MTypeId(0x464e4c44)
    NormalConstraint = MTypeId(0x444e4332)
    Normalize = MTypeId(0x4e4f524d)
    Not = MTypeId(0x4e4f5442)
    Nucleus = MTypeId(0x4e535953)
    NurbsCurve = MTypeId(0x4e435256)
    NurbsCurveToBezier = MTypeId(0x4e525442)
    NurbsSurface = MTypeId(0x4e535246)
    NurbsTessellate = MTypeId(0x4e544553)
    NurbsToSubdiv = MTypeId(0x534e5453)
    NurbsToSubdivProc = MTypeId(0x534e5450)
    ObjectAttrFilter = MTypeId(0x4f464154)
    ObjectBinFilter = MTypeId(0x4f4b464c)
    ObjectFilter = MTypeId(0x4f464c54)
    ObjectMultiFilter = MTypeId(0x4f4d464c)
    ObjectNameFilter = MTypeId(0x4f4e464c)
    ObjectRenderFilter = MTypeId(0x4f52464c)
    ObjectScriptFilter = MTypeId(0x4f53464c)
    ObjectSet = MTypeId(0x4f425354)
    ObjectTypeFilter = MTypeId(0x4f54464c)
    Ocean = MTypeId(0x52544f43)
    OceanShader = MTypeId(0x524f5053)
    OffsetCos = MTypeId(0x4e4f4353)
    OffsetCurve = MTypeId(0x4e4f4355)
    OffsetSurface = MTypeId(0x4e4f5355)
    OldBlindDataBase = MTypeId(0x42444454)
    OldGeometryConstraint = MTypeId(0x44474d43)
    OldNormalConstraint = MTypeId(0x444e5243)
    OldTangentConstraint = MTypeId(0x44544e43)
    OpticalFX = MTypeId(0x4f504658)
    Or = MTypeId(0x4f52424f)
    OrientConstraint = MTypeId(0x444f5243)
    OrientationMarker = MTypeId(0x4f52544d)
    PairBlend = MTypeId(0x4150424c)
    ParamDimension = MTypeId(0x52444d4e)
    ParentConstraint = MTypeId(0x44504152)
    ParentMatrix = MTypeId(0x50524d54)
    Particle = MTypeId(0x59504152)
    ParticleAgeMapper = MTypeId(0x50414d41)
    ParticleCloud = MTypeId(0x50434c44)
    ParticleColorMapper = MTypeId(0x50434d41)
    ParticleIncandMapper = MTypeId(0x50494d41)
    ParticleSamplerInfo = MTypeId(0x5053494e)
    ParticleTranspMapper = MTypeId(0x50544d41)
    Partition = MTypeId(0x5052544e)
    PassContributionMap = MTypeId(0x5053434d)
    PassMatrix = MTypeId(0x4450534d)
    PfxHair = MTypeId(0x50464841)
    PfxToon = MTypeId(0x5046544f)
    Phong = MTypeId(0x5250484f)
    PhongE = MTypeId(0x52504845)
    Pi = MTypeId(0x50494b44)
    PickMatrix = MTypeId(0x504d4154)
    PivotAndOrientManip = MTypeId(0x50414f4d)
    Place2dTexture = MTypeId(0x52504c32)
    Place3dTexture = MTypeId(0x52504c44)
    PlanarProjManip = MTypeId(0x554d5050)
    PlanarTrimSurface = MTypeId(0x4e504c54)
    PlusMinusAverage = MTypeId(0x52504d41)
    PointConstraint = MTypeId(0x44505443)
    PointEmitter = MTypeId(0x59454d49)
    PointLight = MTypeId(0x504f4954)
    PointMatrixMult = MTypeId(0x44504d4d)
    PointOnCurveInfo = MTypeId(0x4e504349)
    PointOnCurveManip = MTypeId(0x554d5043)
    PointOnLineManip = MTypeId(0x554d504c)
    PointOnPolyConstraint = MTypeId(0x44505043)
    PointOnSurfManip = MTypeId(0x554d5353)
    PointOnSurfaceInfo = MTypeId(0x4e505349)
    PointOnSurfaceManip = MTypeId(0x554d5053)
    PoleVectorConstraint = MTypeId(0x44505643)
    PolyAppend = MTypeId(0x50415050)
    PolyAppendVertex = MTypeId(0x50415056)
    PolyAutoProj = MTypeId(0x50415550)
    PolyAverageVertex = MTypeId(0x50415656)
    PolyAxis = MTypeId(0x50435244)
    PolyBevel = MTypeId(0x5042564c)
    PolyBevel2 = MTypeId(0x50425632)
    PolyBevel3 = MTypeId(0x50425633)
    PolyBlindData = MTypeId(0x4d424454)
    PolyBoolOp = MTypeId(0x50424f50)
    PolyBridgeEdge = MTypeId(0x50425245)
    PolyCBoolOp = MTypeId(0x50435642)
    PolyChipOff = MTypeId(0x50434849)
    PolyCircularize = MTypeId(0x50435243)
    PolyClean = MTypeId(0x504c434c)
    PolyCloseBorder = MTypeId(0x50434c4f)
    PolyCollapseEdge = MTypeId(0x50434f45)
    PolyCollapseF = MTypeId(0x50434f46)
    PolyColorDel = MTypeId(0x5043444c)
    PolyColorMod = MTypeId(0x50434d4f)
    PolyColorPerVertex = MTypeId(0x50435056)
    PolyCone = MTypeId(0x50434f4e)
    PolyConnectComponents = MTypeId(0x50434353)
    PolyContourProj = MTypeId(0x50434e50)
    PolyCopyUV = MTypeId(0x50435556)
    PolyCrease = MTypeId(0x50435253)
    PolyCreaseEdge = MTypeId(0x50435345)
    PolyCreateFace = MTypeId(0x50435245)
    PolyCube = MTypeId(0x50435542)
    PolyCut = MTypeId(0x50504354)
    PolyCylProj = MTypeId(0x50435950)
    PolyCylinder = MTypeId(0x5043594c)
    PolyDelEdge = MTypeId(0x50444545)
    PolyDelFacet = MTypeId(0x50444546)
    PolyDelVertex = MTypeId(0x50444556)
    PolyDuplicateEdge = MTypeId(0x50445545)
    PolyEdgeToCurve = MTypeId(0x50544356)
    PolyEditEdgeFlow = MTypeId(0x50534546)
    PolyExtrudeEdge = MTypeId(0x50455845)
    PolyExtrudeFace = MTypeId(0x50455846)
    PolyExtrudeVertex = MTypeId(0x50455856)
    PolyFlipEdge = MTypeId(0x50464c45)
    PolyFlipUV = MTypeId(0x50465556)
    PolyHelix = MTypeId(0x48454c49)
    PolyHoleFace = MTypeId(0x50484645)
    PolyLayoutUV = MTypeId(0x504c5556)
    PolyMapCut = MTypeId(0x504d4143)
    PolyMapDel = MTypeId(0x504d4144)
    PolyMapSew = MTypeId(0x504d4153)
    PolyMapSewMove = MTypeId(0x5053454d)
    PolyMergeEdge = MTypeId(0x504d4545)
    PolyMergeFace = MTypeId(0x504d4546)
    PolyMergeUV = MTypeId(0x504d4755)
    PolyMergeVert = MTypeId(0x504d5645)
    PolyMirror = MTypeId(0x504d4952)
    PolyMoveEdge = MTypeId(0x504d4f45)
    PolyMoveFace = MTypeId(0x504d4f46)
    PolyMoveFacetUV = MTypeId(0x504d4655)
    PolyMoveUV = MTypeId(0x504d5556)
    PolyMoveVertex = MTypeId(0x504d4f56)
    PolyNormal = MTypeId(0x504e4f52)
    PolyNormalPerVertex = MTypeId(0x504e5056)
    PolyNormalizeUV = MTypeId(0x504e5556)
    PolyOptUvs = MTypeId(0x504f5556)
    PolyPassThru = MTypeId(0x50595054)
    PolyPinUV = MTypeId(0x50505556)
    PolyPipe = MTypeId(0x50504950)
    PolyPlanarProj = MTypeId(0x50504c50)
    PolyPlane = MTypeId(0x504d4553)
    PolyPlatonicSolid = MTypeId(0x534f4c49)
    PolyPoke = MTypeId(0x5050504b)
    PolyPrimitiveMisc = MTypeId(0x4d495343)
    PolyPrism = MTypeId(0x50505249)
    PolyProj = MTypeId(0x5050524f)
    PolyProjectCurve = MTypeId(0x50504356)
    PolyPyramid = MTypeId(0x50505952)
    PolyQuad = MTypeId(0x50515541)
    PolyReduce = MTypeId(0x50524544)
    PolyRemesh = MTypeId(0x50524d48)
    PolyRetopo = MTypeId(0x5052464d)
    PolySeparate = MTypeId(0x50534550)
    PolySewEdge = MTypeId(0x50535745)
    PolySmooth = MTypeId(0x50534d54)
    PolySmoothFace = MTypeId(0x50534d46)
    PolySmoothProxy = MTypeId(0x50534d50)
    PolySoftEdge = MTypeId(0x50534f45)
    PolySphProj = MTypeId(0x50535050)
    PolySphere = MTypeId(0x50535048)
    PolySpinEdge = MTypeId(0x50535051)
    PolySplit = MTypeId(0x5053504c)
    PolySplitEdge = MTypeId(0x50534544)
    PolySplitRing = MTypeId(0x50535052)
    PolySplitVert = MTypeId(0x50535645)
    PolyStraightenUVBorder = MTypeId(0x50535442)
    PolySubdEdge = MTypeId(0x50535545)
    PolySubdFace = MTypeId(0x50535546)
    PolyToSubdiv = MTypeId(0x50534453)
    PolyTorus = MTypeId(0x50544f52)
    PolyTransfer = MTypeId(0x50544652)
    PolyTriangulate = MTypeId(0x50545249)
    PolyTweak = MTypeId(0x5054574b)
    PolyTweakUV = MTypeId(0x50545556)
    PolyUVRectangle = MTypeId(0x50555652)
    PolyUnite = MTypeId(0x50554e49)
    PolyUnsmooth = MTypeId(0x50555344)
    PolyWedgeFace = MTypeId(0x50574643)
    PoseInterpolatorManager = MTypeId(0x5053444d)
    PositionMarker = MTypeId(0x504f534d)
    PostProcessList = MTypeId(0x50505354)
    Power = MTypeId(0x504f5744)
    PrimitiveFalloff = MTypeId(0x53464f46)
    ProjectCurve = MTypeId(0x4e504352)
    ProjectTangent = MTypeId(0x4e50544e)
    Projection = MTypeId(0x5250524a)
    ProjectionManip = MTypeId(0x554d4354)
    PropModManip = MTypeId(0x554d4354)
    PropMoveTriadManip = MTypeId(0x554d5054)
    ProximityFalloff = MTypeId(0x5058464f)
    ProximityPin = MTypeId(0x50525850)
    ProximityWrap = MTypeId(0x50575250)
    ProxyManager = MTypeId(0x50584d47)
    PsdFileTex = MTypeId(0x50534454)
    QuadPtOnLineManip = MTypeId(0x554d504c)
    QuadShadingSwitch = MTypeId(0x53574834)
    RadialField = MTypeId(0x59524144)
    Ramp = MTypeId(0x52545241)
    RampShader = MTypeId(0x52525053)
    RbfSrf = MTypeId(0x4e524246)
    RebuildCurve = MTypeId(0x4e524243)
    RebuildSurface = MTypeId(0x4e524253)
    Record = MTypeId(0x52454344)
    Reference = MTypeId(0x5245464e)
    RelOverride = MTypeId(0x5800037a)
    RelUniqueOverride = MTypeId(0x580003a1)
    RemapColor = MTypeId(0x524d434c)
    RemapHsv = MTypeId(0x524d4853)
    RemapValue = MTypeId(0x524d564c)
    RenderBox = MTypeId(0x524e4258)
    RenderCone = MTypeId(0x524e434f)
    RenderGlobals = MTypeId(0x52474c42)
    RenderGlobalsList = MTypeId(0x5244474c)
    RenderLayer = MTypeId(0x524e444c)
    RenderLayerManager = MTypeId(0x524e4c4d)
    RenderPass = MTypeId(0x524e5053)
    RenderPassSet = MTypeId(0x52505353)
    RenderQuality = MTypeId(0x52515541)
    RenderRect = MTypeId(0x52524354)
    RenderSettingsChildCollection = MTypeId(0x580003a3)
    RenderSettingsCollection = MTypeId(0x58000395)
    RenderSetup = MTypeId(0x58000371)
    RenderSetupLayer = MTypeId(0x58000372)
    RenderSphere = MTypeId(0x524e5350)
    RenderTarget = MTypeId(0x524e5447)
    RenderedImageSource = MTypeId(0x52434953)
    ReorderUVSet = MTypeId(0x524f5553)
    Resolution = MTypeId(0x524c544e)
    ResultCurveTimeToAngular = MTypeId(0x52435441)
    ResultCurveTimeToLinear = MTypeId(0x5243544c)
    ResultCurveTimeToTime = MTypeId(0x52435454)
    ResultCurveTimeToUnitless = MTypeId(0x52435455)
    Reverse = MTypeId(0x52525653)
    ReverseCurve = MTypeId(0x4e525643)
    ReverseSurface = MTypeId(0x4e525653)
    Revolve = MTypeId(0x4e52564c)
    RgbToHsv = MTypeId(0x52523248)
    RigidBody = MTypeId(0x59524744)
    RigidConstraint = MTypeId(0x59435354)
    RigidSolver = MTypeId(0x59534c56)
    Rock = MTypeId(0x5254524b)
    RotateLimitsManip = MTypeId(0x554d524c)
    RotateManip = MTypeId(0x554d5241)
    RotateUV2dManip = MTypeId(0x5532524f)
    RotateVector = MTypeId(0x524f5456)
    RotationFromMatrix = MTypeId(0x524f4d58)
    Round = MTypeId(0x524f554e)
    RoundConstantRadius = MTypeId(0x4e524352)
    RowFromMatrix = MTypeId(0x524d4154)
    Sampler = MTypeId(0x46534d50)
    SamplerInfo = MTypeId(0x5253494e)
    ScaleConstraint = MTypeId(0x44534343)
    ScaleFromMatrix = MTypeId(0x534d4154)
    ScaleLimitsManip = MTypeId(0x4c544d50)
    ScaleManip = MTypeId(0x554d4650)
    ScaleUV2dManip = MTypeId(0x55325343)
    ScreenAlignedCircleManip = MTypeId(0x5341434d)
    Script = MTypeId(0x53435250)
    ScriptManip = MTypeId(0x554d5343)
    Sculpt = MTypeId(0x46534350)
    SelectionListOperator = MTypeId(0x534c4f50)
    SequenceManager = MTypeId(0x53514d47)
    Sequencer = MTypeId(0x53514e43)
    SetRange = MTypeId(0x52524e47)
    ShaderGlow = MTypeId(0x5348474c)
    ShaderOverride = MTypeId(0x58000386)
    ShadingEngine = MTypeId(0x53484144)
    ShadingMap = MTypeId(0x53444d50)
    ShapeEditorManager = MTypeId(0x53444d4c)
    ShellTessellate = MTypeId(0x53544553)
    Shot = MTypeId(0x53484f54)
    ShrinkWrap = MTypeId(0x53575250)
    SimpleSelector = MTypeId(0x5800039e)
    SimpleTestNode = MTypeId(0x53544e44)
    SimpleVolumeShader = MTypeId(0x53565348)
    Sin = MTypeId(0x53494e45)
    SingleShadingSwitch = MTypeId(0x53574831)
    SketchPlane = MTypeId(0x534b504e)
    SkinBinding = MTypeId(0x534b4244)
    SkinCluster = MTypeId(0x4653434c)
    SmoothCurve = MTypeId(0x4e534d43)
    SmoothStep = MTypeId(0x534d5354)
    SmoothTangentSrf = MTypeId(0x4e53544e)
    SnapUV2dManip = MTypeId(0x5532534e)
    Snapshot = MTypeId(0x534e5054)
    SnapshotShape = MTypeId(0x53534841)
    Snow = MTypeId(0x5254534e)
    SoftMod = MTypeId(0x4653534c)
    SoftModHandle = MTypeId(0x46535348)
    SolidFractal = MTypeId(0x52544633)
    Solidify = MTypeId(0x534f4c59)
    SpBirailSrf = MTypeId(0x4e534253)
    SphericalProjManip = MTypeId(0x554d5350)
    SpotCylinderManip = MTypeId(0x53434d50)
    SpotLight = MTypeId(0x5350544c)
    SpotManip = MTypeId(0x554d4958)
    Spring = MTypeId(0x59535052)
    SquareSrf = MTypeId(0x4e535153)
    StandardSurface = MTypeId(0x53544453)
    Stencil = MTypeId(0x52545354)
    StereoRigCamera = MTypeId(0x53524341)
    StitchAsNurbsShell = MTypeId(0x4e535348)
    StitchSrf = MTypeId(0x4e535453)
    Stroke = MTypeId(0x5354524b)
    StrokeGlobals = MTypeId(0x53544b47)
    Stucco = MTypeId(0x52533630)
    StyleCurve = MTypeId(0x4e535443)
    SubCurve = MTypeId(0x4e534243)
    SubSurface = MTypeId(0x4e535352)
    SubdAddTopology = MTypeId(0x53415459)
    SubdAutoProj = MTypeId(0x53415550)
    SubdBlindData = MTypeId(0x53424454)
    SubdCleanTopology = MTypeId(0x53435459)
    SubdHierBlind = MTypeId(0x53485242)
    SubdLayoutUV = MTypeId(0x534c5556)
    SubdMapCut = MTypeId(0x534d4143)
    SubdMapSewMove = MTypeId(0x5353454d)
    SubdPlanarProj = MTypeId(0x53504c50)
    SubdTweak = MTypeId(0x5354574b)
    SubdTweakUV = MTypeId(0x53545556)
    Subdiv = MTypeId(0x53445353)
    SubdivCollapse = MTypeId(0x53434c50)
    SubdivComponentId = MTypeId(0x53534944)
    SubdivReverseFaces = MTypeId(0x53525646)
    SubdivSurfaceVarGroup = MTypeId(0x53535647)
    SubdivToNurbs = MTypeId(0x5344534e)
    SubdivToPoly = MTypeId(0x53445350)
    SubsetFalloff = MTypeId(0x5353464f)
    Subtract = MTypeId(0x53554253)
    Sum = MTypeId(0x53554d44)
    SurfaceInfo = MTypeId(0x4e53494e)
    SurfaceLuminance = MTypeId(0x52534c55)
    SurfaceShader = MTypeId(0x52535348)
    SurfaceVarGroup = MTypeId(0x4e535647)
    SymmetryConstraint = MTypeId(0x44534d43)
    Tan = MTypeId(0x54414e47)
    TangentConstraint = MTypeId(0x44544332)
    Tension = MTypeId(0x54454e53)
    TextButtonManip = MTypeId(0x554d5442)
    Texture3dManip = MTypeId(0x554d5458)
    TextureBakeSet = MTypeId(0x5442414b)
    TextureDeformer = MTypeId(0x54584446)
    TextureDeformerHandle = MTypeId(0x54444844)
    TextureToGeom = MTypeId(0x5454474f)
    Time = MTypeId(0x54494d45)
    TimeEditor = MTypeId(0x544d4544)
    TimeEditorAnimSource = MTypeId(0x54454153)
    TimeEditorClip = MTypeId(0x41434c43)
    TimeEditorClipBase = MTypeId(0x414c434c)
    TimeEditorClipEvaluator = MTypeId(0x4143524f)
    TimeEditorInterpolator = MTypeId(0x54454950)
    TimeEditorTracks = MTypeId(0x5445544b)
    TimeFunction = MTypeId(0x7466786e)
    TimeToUnitConversion = MTypeId(0x44544d55)
    TimeWarp = MTypeId(0x54495741)
    ToggleManip = MTypeId(0x554d5447)
    ToggleOnLineManip = MTypeId(0x55544f4c)
    ToolDrawManip = MTypeId(0x5454444d)
    ToolDrawManip2D = MTypeId(0x54444d32)
    ToonLineAttributes = MTypeId(0x544c4154)
    TrackInfoManager = MTypeId(0x54494d47)
    TransUV2dManip = MTypeId(0x55325452)
    TransferAttributes = MTypeId(0x54524154)
    TransferFalloff = MTypeId(0x50464f46)
    Transform = MTypeId(0x5846524d)
    TransformGeometry = MTypeId(0x5447454f)
    TranslateLimitsManip = MTypeId(0x434e4d50)
    TranslateManip = MTypeId(0x554d4650)
    TranslateUVManip = MTypeId(0x554d5556)
    TranslationFromMatrix = MTypeId(0x544d4154)
    Trim = MTypeId(0x4e54524d)
    TrimWithBoundaries = MTypeId(0x4e545742)
    TriplanarProjManip = MTypeId(0x554d5452)
    TripleShadingSwitch = MTypeId(0x53574833)
    TrsInsertManip = MTypeId(0x554d4354)
    TrsManip = MTypeId(0x5554544d)
    Truncate = MTypeId(0x5452554e)
    TurbulenceField = MTypeId(0x59545552)
    TurbulenceManip = MTypeId(0x554d4958)
    Tweak = MTypeId(0x464d5054)
    UfeProxyCameraShape = MTypeId(0x55465043)
    UfeProxyTransform = MTypeId(0x55465058)
    UniformFalloff = MTypeId(0x55574754)
    UniformField = MTypeId(0x59554e49)
    UnitConversion = MTypeId(0x44554e54)
    UnitToTimeConversion = MTypeId(0x4455544d)
    Unknown = MTypeId(0x554e4b4e)
    UnknownDag = MTypeId(0x554e4b44)
    UnknownTransform = MTypeId(0x554e4b54)
    Untrim = MTypeId(0x4e555452)
    UseBackground = MTypeId(0x55534247)
    Uv2dManip = MTypeId(0x5556324d)
    UvChooser = MTypeId(0x55564348)
    UvPin = MTypeId(0x55565256)
    VectorProduct = MTypeId(0x52564543)
    VertexBakeSet = MTypeId(0x5642414b)
    ViewColorManager = MTypeId(0x5657434d)
    VolumeAxisField = MTypeId(0x59565846)
    VolumeFog = MTypeId(0x52564647)
    VolumeLight = MTypeId(0x564f4c4c)
    VolumeNoise = MTypeId(0x52545633)
    VolumeShader = MTypeId(0x52565348)
    VortexField = MTypeId(0x59564f52)
    Water = MTypeId(0x52545741)
    WeightGeometryFilter = MTypeId(0x44574746)
    Wire = MTypeId(0x46574952)
    Wood = MTypeId(0x52545744)
    Wrap = MTypeId(0x46575250)
    WtAddMatrix = MTypeId(0x4457414d)


_COMMON_ATTR_PROPERTIES = {
    'hiddenInOutliner': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'overrideEnabled': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'overrideDisplayType': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kEnumAttribute},

    'translate': {'is_array': False, 'is_compound': True, 'is_element': False, 'attr_type': MFn.kAttribute3Double, 'children': ['translateX', 'translateY', 'translateZ']},
    'translateX': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleLinearAttribute},
    'translateY': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleLinearAttribute},
    'translateZ': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleLinearAttribute},

    'rotate': {'is_array': False, 'is_compound': True, 'is_element': False, 'attr_type': MFn.kAttribute3Double, 'children': ['rotateX', 'rotateY', 'rotateZ']},
    'rotateX': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleAngleAttribute},
    'rotateY': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleAngleAttribute},
    'rotateZ': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleAngleAttribute},

    'scale': {'is_array': False, 'is_compound': True, 'is_element': False, 'attr_type': MFn.kAttribute3Double, 'children': ['scaleX', 'scaleY', 'scaleZ']},
    'scaleX': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'scaleY': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'scaleZ': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},

    'visibility': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'template': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},

    'inheritsTransform': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},

    'matrix': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'inverseMatrix': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'worldMatrix': {'is_array': True, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'worldInverseMatrix': {'is_array': True, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'offsetParentMatrix': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kMatrixAttribute},
    'parentMatrix': {'is_array': True, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'parentInverseMatrix': {'is_array': True, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'dagLocalMatrix': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kMatrixAttribute},
    'dagLocalInverseMatrix': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kMatrixAttribute},

    'drawStyle': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kEnumAttribute},
    'radius': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'segmentScaleCompensate': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'rotateOrder': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kEnumAttribute},
    'preferredAngleX': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleAngleAttribute},
    'preferredAngleY': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleAngleAttribute},
    'preferredAngleZ': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kDoubleAngleAttribute},
    'side': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kEnumAttribute},
    'type': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kEnumAttribute},
    'otherType': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'drawLabel': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},

    'blender': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'color1': {'is_array': False, 'is_compound': True, 'is_element': False, 'attr_type': MFn.kAttribute3Float, 'children': ['color1R', 'color1G', 'color1B']},
    'color1R': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'color1G': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'color1B': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'color2': {'is_array': False, 'is_compound': True, 'is_element': False, 'attr_type': MFn.kAttribute3Float, 'children': ['color2R', 'color2G', 'color2B']},
    'color2R': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'color2G': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'color2B': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'outputR': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'outputG': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'outputB': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},

    'attributesBlender': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},
    'input': {'is_array': True, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kNumericAttribute},

    'inMesh': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'outMesh': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'worldMesh': {'is_array': True, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},

    'outputCurve': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},
    'create': {'is_array': False, 'is_compound': False, 'is_element': False, 'attr_type': MFn.kTypedAttribute},


}

_COMMON_ATTR_SHORT_NAMES_TO_FULL_NAME = {
    'hio': 'hiddenInOutliner',
    'ove': 'overrideEnabled',
    'ovdt': 'overrideDisplayType',

    't': 'translate',
    'tx': 'translateX',
    'ty': 'translateY',
    'tz': 'translateZ',
    'r': 'rotate',
    'rx': 'rotateX',
    'ry': 'rotateY',
    'rz': 'rotateZ',
    's': 'scale',
    'sx': 'scaleX',
    'sy': 'scaleY',
    'sz': 'scaleZ',
    'v': 'visibility',
    'tmp': 'template',
    'it': 'inheritsTransform',

    'm': 'matrix',
    'im': 'inverseMatrix',
    'wm': 'worldMatrix',
    'wim': 'worldInverseMatrix',
    'opm': 'offsetParentMatrix',
    'pm': 'parentMatrix',
    'pim': 'parentInverseMatrix',
    'dlm': 'dagLocalMatrix',
    'dlim': 'dagLocalInverseMatrix',

    'ds': 'drawStyle',
    'radi': 'radius',
    'ssc': 'segmentScaleCompensate',
    'ro': 'rotateOrder',
    'pax': 'preferredAngleX',
    'pay': 'preferredAngleY',
    'paz': 'preferredAngleZ',
    'sd': 'side',
    'typ': 'type',
    'otp': 'otherType',
    'dl': 'drawLabel',

    'b': 'blender',
    'c1': 'color1',
    'c1r': 'color1R',
    'c1g': 'color1G',
    'c1b': 'color1B',
    'c2': 'color2',
    'c2r': 'color2R',
    'c2g': 'color2G',
    'c2b': 'color2B',
    'opr': 'outputR',
    'opg': 'outputG',
    'opb': 'outputB',

    'ab': 'attributesBlender',

    'i': 'inMesh',
    'o': 'outMesh',
    'w': 'worldMesh',

    'oc': 'outputCurve',
    'cr': 'create',


}

_COMMON_ATTR_FULL_NAMES_TO_SHORT_NAME = {ln: sn for sn, ln in _COMMON_ATTR_SHORT_NAMES_TO_FULL_NAME.items()}

_TYPE_STR_TO_ID = {

   "AISEnvFacade": MTypeId(0x52454656),

   "aboutToSetValueTestNode": MTypeId(0x4153564e),

   "absOverride": MTypeId(0x58000378),

   "absUniqueOverride": MTypeId(0x580003a0),

   "absolute": MTypeId(0x41425344),

   "acos": MTypeId(0x41434f53),

   "addDoubleLinear": MTypeId(0x4441444c),

   "addMatrix": MTypeId(0x44414d58),

   "adskMaterial": MTypeId(0x4144534d),

   "aimConstraint": MTypeId(0x44414d43),

   "aimMatrix": MTypeId(0x414d4154),

   "airField": MTypeId(0x59414952),

   "indexManip": MTypeId(0x554d4958),

   "alignCurve": MTypeId(0x4e414c43),

   "alignManip": MTypeId(0x554d4144),

   "alignSurface": MTypeId(0x4e414c53),

   "ambientLight": MTypeId(0x414d424c),

   "and": MTypeId(0x414e4442),

   "angleBetween": MTypeId(0x4e414254),

   "angleDimension": MTypeId(0x4147444e),

   "animBlend": MTypeId(0x41424e44),

   "animBlendInOut": MTypeId(0x4142494f),

   "animBlendNodeAdditive": MTypeId(0x41424e41),

   "animBlendNodeAdditiveDA": MTypeId(0x41424141),

   "animBlendNodeAdditiveDL": MTypeId(0x4142414c),

   "animBlendNodeAdditiveF": MTypeId(0x41424146),

   "animBlendNodeAdditiveFA": MTypeId(0x41424641),

   "animBlendNodeAdditiveFL": MTypeId(0x4142464c),

   "animBlendNodeAdditiveI16": MTypeId(0x41424153),

   "animBlendNodeAdditiveI32": MTypeId(0x41424149),

   "animBlendNodeAdditiveRotation": MTypeId(0x41424e52),

   "animBlendNodeAdditiveScale": MTypeId(0x41424e53),

   "animBlendNodeBoolean": MTypeId(0x4142424f),

   "animBlendNodeEnum": MTypeId(0x41424e45),

   "animBlendNodeTime": MTypeId(0x41425449),

   "animClip": MTypeId(0x434c504e),

   "animCurveTA": MTypeId(0x50435441),

   "animCurveTL": MTypeId(0x5043544c),

   "animCurveTT": MTypeId(0x50435454),

   "animCurveTU": MTypeId(0x50435455),

   "animCurveUA": MTypeId(0x50435541),

   "animCurveUL": MTypeId(0x5043554c),

   "animCurveUT": MTypeId(0x50435554),

   "animCurveUU": MTypeId(0x50435555),

   "animLayer": MTypeId(0x414e4c52),

   "anisotropic": MTypeId(0x52414e49),

   "annotationShape": MTypeId(0x414e4e53),

   "aovChildCollection": MTypeId(0x5800039c),

   "aovCollection": MTypeId(0x5800039b),

   "applyAbs2FloatsOverride": MTypeId(0x58000397),

   "applyAbs3FloatsOverride": MTypeId(0x58000381),

   "applyAbsBoolOverride": MTypeId(0x5800038a),

   "applyAbsEnumOverride": MTypeId(0x5800038c),

   "applyAbsFloatOverride": MTypeId(0x5800037d),

   "applyAbsIntOverride": MTypeId(0x58000391),

   "applyAbsStringOverride": MTypeId(0x58000393),

   "applyConnectionOverride": MTypeId(0x58000384),

   "applyRel2FloatsOverride": MTypeId(0x58000399),

   "applyRel3FloatsOverride": MTypeId(0x58000383),

   "applyRelFloatOverride": MTypeId(0x5800037f),

   "applyRelIntOverride": MTypeId(0x58000392),

   "arcLengthDimension": MTypeId(0x41444d4e),

   "areaLight": MTypeId(0x41524c54),

   "arrayMapper": MTypeId(0x44414d50),

   "arrowManip": MTypeId(0x554d4152),

   "arubaTessellate": MTypeId(0x41544553),

   "asin": MTypeId(0x4153494e),

   "atan": MTypeId(0x4154414e),

   "atan2": MTypeId(0x41544132),

   "attachCurve": MTypeId(0x4e415443),

   "attachSurface": MTypeId(0x4e415453),

   "attrHierarchyTest": MTypeId(0x41544854),

   "audio": MTypeId(0x41554449),

   "average": MTypeId(0x41565244),

   "avgCurves": MTypeId(0x4e414352),

   "avgNurbsSurfacePoints": MTypeId(0x4e414e50),

   "avgSurfacePoints": MTypeId(0x4e415350),

   "axisFromMatrix": MTypeId(0x584d4154),

   "ballProjManip": MTypeId(0x554d4250),

   "lineManip": MTypeId(0x554d4c4e),

   "baseLattice": MTypeId(0x46424153),

   "basicSelector": MTypeId(0x58000375),

   "bevel": MTypeId(0x4e42564c),

   "bevelPlus": MTypeId(0x4e425356),

   "bezierCurve": MTypeId(0x42435256),

   "bezierCurveToNurbs": MTypeId(0x42544e52),

   "blendColorSets": MTypeId(0x50424353),

   "blendColors": MTypeId(0x52424c32),

   "blendDevice": MTypeId(0x424c4456),

   "blendFalloff": MTypeId(0x42464f46),

   "blendMatrix": MTypeId(0x424d4154),

   "blendShape": MTypeId(0x46424c53),

   "blendTwoAttr": MTypeId(0x41424c32),

   "blendWeighted": MTypeId(0x41424c57),

   "blindDataTemplate": MTypeId(0x424c4454),

   "blinn": MTypeId(0x52424c4e),

   "boneLattice": MTypeId(0x4642554c),

   "boolean": MTypeId(0x4e424f4c),

   "boundary": MTypeId(0x4e424e44),

   "brownian": MTypeId(0x5246424d),

   "brush": MTypeId(0x42525348),

   "bulge": MTypeId(0x52544255),

   "bump2d": MTypeId(0x5242554d),

   "bump3d": MTypeId(0x52425533),

   "freePointTriadManip": MTypeId(0x55465054),

   "cacheBlend": MTypeId(0x4354524b),

   "cacheFile": MTypeId(0x43434846),

   "camera": MTypeId(0x4443414d),

   "cameraPlaneManip": MTypeId(0x554d4350),

   "cameraSet": MTypeId(0x44525452),

   "cameraView": MTypeId(0x44434156),

   "ceil": MTypeId(0x43454944),

   "centerManip": MTypeId(0x434e4d50),

   "character": MTypeId(0x43484152),

   "characterMap": MTypeId(0x434d4150),

   "characterOffset": MTypeId(0x584f4646),

   "checker": MTypeId(0x52544348),

   "choice": MTypeId(0x43484345),

   "chooser": MTypeId(0x43484f4f),

   "circleManip": MTypeId(0x554d434c),

   "circleSweepManip": MTypeId(0x5543534d),

   "clamp": MTypeId(0x52434c33),

   "clampRange": MTypeId(0x434c414d),

   "clipGhostShape": MTypeId(0x43475348),

   "clipLibrary": MTypeId(0x434c4950),

   "clipScheduler": MTypeId(0x43534348),

   "clipToGhostData": MTypeId(0x43324744),

   "closeCurve": MTypeId(0x4e434355),

   "closeSurface": MTypeId(0x4e435355),

   "closestPointOnMesh": MTypeId(0x43504f4d),

   "closestPointOnSurface": MTypeId(0x4e435053),

   "cloth": MTypeId(0x5254434c),

   "cloud": MTypeId(0x52544344),

   "cluster": MTypeId(0x46434c53),

   "clusterFlexorShape": MTypeId(0x464a4346),

   "clusterHandle": MTypeId(0x46434c48),

   "collection": MTypeId(0x58000373),

   "collisionModel": MTypeId(0x59434f4c),

   "colorManagementGlobals": MTypeId(0x434d4742),

   "colorProfile": MTypeId(0x434f4c50),

   "columnFromMatrix": MTypeId(0x434d4154),

   "combinationShape": MTypeId(0x46434e53),

   "compactPlugArrayTest": MTypeId(0x43504154),

   "componentFalloff": MTypeId(0x47464f46),

   "translateManip": MTypeId(0x5554544d),

   "componentMatch": MTypeId(0x544f504d),

   "componentTagBase": MTypeId(0x43544253),

   "composeMatrix": MTypeId(0x58000301),

   "concentricProjManip": MTypeId(0x554d434f),

   "condition": MTypeId(0x52434e44),

   "connectionOverride": MTypeId(0x58000385),

   "connectionUniqueOverride": MTypeId(0x580003a2),

   "container": MTypeId(0x434f4e54),

   "containerBase": MTypeId(0x434f4241),

   "contrast": MTypeId(0x52434f4e),

   "controller": MTypeId(0x43475250),

   "copyColorSet": MTypeId(0x43504353),

   "copyUVSet": MTypeId(0x43505553),

   "cos": MTypeId(0x434f5349),

   "crater": MTypeId(0x52533430),

   "creaseSet": MTypeId(0x43524541),

   "createColorSet": MTypeId(0x43524353),

   "createUVSet": MTypeId(0x43525553),

   "crossProduct": MTypeId(0x43524f50),

   "cubicProjManip": MTypeId(0x554d4355),

   "curveFromMeshCoM": MTypeId(0x4e434d43),

   "curveFromMeshEdge": MTypeId(0x4e434d45),

   "curveFromSubdivEdge": MTypeId(0x53435345),

   "curveFromSubdivFace": MTypeId(0x53435346),

   "curveFromSurfaceBnd": MTypeId(0x4e435342),

   "curveFromSurfaceCoS": MTypeId(0x4e435343),

   "curveFromSurfaceIso": MTypeId(0x4e435349),

   "curveInfo": MTypeId(0x4e43494e),

   "curveIntersect": MTypeId(0x4e434349),

   "curveNormalizerAngle": MTypeId(0x434e5241),

   "curveNormalizerLinear": MTypeId(0x434e524c),

   "pointOnCurveManip": MTypeId(0x554d5043),

   "curveVarGroup": MTypeId(0x4e435647),

   "cylindricalProjManip": MTypeId(0x554d4359),

   "dagContainer": MTypeId(0x44414743),

   "dagPose": MTypeId(0x46504f53),

   "dataBlockTest": MTypeId(0x44425453),

   "decomposeMatrix": MTypeId(0x58000300),

   "defaultLightList": MTypeId(0x4445464c),

   "defaultRenderUtilityList": MTypeId(0x4452554c),

   "defaultRenderingList": MTypeId(0x44524e4c),

   "defaultShaderList": MTypeId(0x5244534c),

   "defaultTextureList": MTypeId(0x5244544c),

   "deformBend": MTypeId(0x46444244),

   "deformFlare": MTypeId(0x4644464c),

   "deformSine": MTypeId(0x4644534e),

   "deformSquash": MTypeId(0x46445351),

   "deformTwist": MTypeId(0x46445457),

   "deformWave": MTypeId(0x46445756),

   "deleteColorSet": MTypeId(0x444c4353),

   "deleteComponent": MTypeId(0x44454354),

   "deleteUVSet": MTypeId(0x444c4d53),

   "deltaMush": MTypeId(0x444c544d),

   "detachCurve": MTypeId(0x4e445443),

   "detachSurface": MTypeId(0x4e445453),

   "determinant": MTypeId(0x4445544d),

   "directedDisc": MTypeId(0x44445343),

   "directionalLight": MTypeId(0x4449524c),

   "discManip": MTypeId(0x5544534d),

   "diskCache": MTypeId(0x44534b43),

   "displacementShader": MTypeId(0x52445348),

   "displayLayer": MTypeId(0x4453504c),

   "displayLayerManager": MTypeId(0x44504c4d),

   "distanceBetween": MTypeId(0x44444254),

   "distanceDimShape": MTypeId(0x44444d4e),

   "distanceManip": MTypeId(0x554d444d),

   "divide": MTypeId(0x44495644),

   "dof": MTypeId(0x444f4644),

   "dotProduct": MTypeId(0x444f5450),

   "doubleShadingSwitch": MTypeId(0x53574832),

   "dpBirailSrf": MTypeId(0x4e444253),

   "dragField": MTypeId(0x59445247),

   "dropoffLocator": MTypeId(0x444c4354),

   "dynController": MTypeId(0x5943544c),

   "dynGlobals": MTypeId(0x5944474c),

   "dynHolder": MTypeId(0x59484c44),

   "dynamicConstraint": MTypeId(0x44434f4e),

   "editMetadata": MTypeId(0x454d5444),

   "editsManager": MTypeId(0x454d4752),

   "enableManip": MTypeId(0x454e4d50),

   "envBall": MTypeId(0x5245424c),

   "envChrome": MTypeId(0x52454348),

   "envCube": MTypeId(0x52454342),

   "envFacade": MTypeId(0x52454643),

   "envFog": MTypeId(0x52454647),

   "envSky": MTypeId(0x5245534b),

   "envSphere": MTypeId(0x52455350),

   "environmentFog": MTypeId(0x454e5646),

   "equal": MTypeId(0x4551554c),

   "explodeNurbsShell": MTypeId(0x4e455348),

   "expression": MTypeId(0x44455850),

   "extendCurve": MTypeId(0x4e455843),

   "extendSurface": MTypeId(0x4e455853),

   "extrude": MTypeId(0x4e455852),

   "facade": MTypeId(0x4446434e),

   "falloffEval": MTypeId(0x45464f46),

   "ffBlendSrf": MTypeId(0x4e424c54),

   "ffBlendSrfObsolete": MTypeId(0x4e424c53),

   "ffFilletSrf": MTypeId(0x4e464653),

   "ffd": MTypeId(0x46464644),

   "file": MTypeId(0x52544654),

   "filletCurve": MTypeId(0x4e464352),

   "fitBspline": MTypeId(0x4e465443),

   "flexorShape": MTypeId(0x464c5848),

   "floor": MTypeId(0x464c4f4f),

   "flow": MTypeId(0x464c4f57),

   "fluidEmitter": MTypeId(0x46454d49),

   "fluidShape": MTypeId(0x464c5549),

   "fluidSliceManip": MTypeId(0x46534c4d),

   "fluidTexture2D": MTypeId(0x464c5454),

   "fluidTexture3D": MTypeId(0x464c5458),

   "follicle": MTypeId(0x48435256),

   "forceUpdateManip": MTypeId(0x554d4655),

   "fosterParent": MTypeId(0x4650524e),

   "fourByFourMatrix": MTypeId(0x4642464d),

   "fractal": MTypeId(0x52543246),

   "frameCache": MTypeId(0x46434348),

   "freePointManip": MTypeId(0x554d4650),

   "gammaCorrect": MTypeId(0x5247414d),

   "geoConnectable": MTypeId(0x5947434f),

   "geoConnector": MTypeId(0x59474354),

   "geomBind": MTypeId(0x4742494e),

   "geometryConstraint": MTypeId(0x44474e43),

   "geometryFilter": MTypeId(0x44474649),

   "geometryOnLineManip": MTypeId(0x554d474c),

   "geometryVarGroup": MTypeId(0x4e475647),

   "globalCacheControl": MTypeId(0x4743434c),

   "globalStitch": MTypeId(0x4e475354),

   "granite": MTypeId(0x52544752),

   "gravityField": MTypeId(0x59475241),

   "greasePencilSequence": MTypeId(0x47505351),

   "greasePlane": MTypeId(0x4447504c),

   "greasePlaneRenderShape": MTypeId(0x47505253),

   "greaterThan": MTypeId(0x47525448),

   "grid": MTypeId(0x52544744),

   "group": MTypeId(0x580003a5),

   "groupId": MTypeId(0x47504944),

   "groupParts": MTypeId(0x47525050),

   "guide": MTypeId(0x46475549),

   "hairConstraint": MTypeId(0x4850494e),

   "hairSystem": MTypeId(0x48535953),

   "hairTubeShader": MTypeId(0x52485442),

   "hardenPoint": MTypeId(0x4e484450),

   "hardwareRenderGlobals": MTypeId(0x48575247),

   "hardwareRenderingGlobals": MTypeId(0x48525247),

   "heightField": MTypeId(0x4f435050),

   "hierarchyTestNode1": MTypeId(0x48544e31),

   "hierarchyTestNode2": MTypeId(0x48544e32),

   "hierarchyTestNode3": MTypeId(0x48544e33),

   "hikEffector": MTypeId(0x4446494b),

   "hikFKJoint": MTypeId(0x4a54494b),

   "hikFloorContactMarker": MTypeId(0x4846434d),

   "hikGroundPlane": MTypeId(0x48474e44),

   "hikHandle": MTypeId(0x4b484948),

   "hikIKEffector": MTypeId(0x494b4546),

   "hikSolver": MTypeId(0x4b48494b),

   "historySwitch": MTypeId(0x48495353),

   "holdMatrix": MTypeId(0x4450484d),

   "hsvToRgb": MTypeId(0x52483252),

   "hwReflectionMap": MTypeId(0x4857524d),

   "hwRenderGlobals": MTypeId(0x59485244),

   "hyperGraphInfo": MTypeId(0x48595052),

   "hyperLayout": MTypeId(0x4859504c),

   "hyperView": MTypeId(0x44485056),

   "ikEffector": MTypeId(0x4b454646),

   "ikHandle": MTypeId(0x4b48444c),

   "ikMCsolver": MTypeId(0x4b4d4353),

   "ikPASolver": MTypeId(0x4b504153),

   "ikRPsolver": MTypeId(0x4b525053),

   "ikSCsolver": MTypeId(0x4b534353),

   "ikSplineSolver": MTypeId(0x4b535053),

   "ikSystem": MTypeId(0x4b535953),

   "imagePlane": MTypeId(0x4449504c),

   "implicitBox": MTypeId(0x46494258),

   "implicitCone": MTypeId(0x4649434f),

   "implicitSphere": MTypeId(0x46495350),

   "insertKnotCurve": MTypeId(0x4e494b43),

   "insertKnotSurface": MTypeId(0x4e494b53),

   "instancer": MTypeId(0x594e5354),

   "intersectSurface": MTypeId(0x4e495346),

   "inverseLerp": MTypeId(0x494c5250),

   "jiggle": MTypeId(0x4a474446),

   "joint": MTypeId(0x4a4f494e),

   "jointCluster": MTypeId(0x464a434c),

   "jointFfd": MTypeId(0x46464442),

   "jointLattice": MTypeId(0x4642454c),

   "keyframeRegionManip": MTypeId(0x4b46524d),

   "keyingGroup": MTypeId(0x4b475250),

   "lambert": MTypeId(0x524c414d),

   "lattice": MTypeId(0x464c4154),

   "layeredShader": MTypeId(0x4c595253),

   "layeredTexture": MTypeId(0x4c595254),

   "leastSquaresModifier": MTypeId(0x4e4c534d),

   "leather": MTypeId(0x52544c45),

   "length": MTypeId(0x4c454e47),

   "lerp": MTypeId(0x4c455250),

   "lessThan": MTypeId(0x4c535448),

   "lightEditor": MTypeId(0x580003e3),

   "lightFog": MTypeId(0x52464f47),

   "lightGroup": MTypeId(0x580003e2),

   "lightInfo": MTypeId(0x524c494e),

   "lightItem": MTypeId(0x580003e1),

   "lightLinker": MTypeId(0x524c4c4b),

   "lightList": MTypeId(0x4c4c5354),

   "lightsChildCollection": MTypeId(0x5800039a),

   "lightsCollection": MTypeId(0x58000394),

   "lightsCollectionSelector": MTypeId(0x580003a4),

   "limitManip": MTypeId(0x4c544d50),

   "lineModifier": MTypeId(0x4c4d4f44),

   "locator": MTypeId(0x4c4f4354),

   "lodGroup": MTypeId(0x4c4f4447),

   "lodThresholds": MTypeId(0x4c4f4454),

   "loft": MTypeId(0x4e534b4e),

   "log": MTypeId(0x4c4f4744),

   "lookAt": MTypeId(0x444c4154),

   "luminance": MTypeId(0x524c554d),

   "makeGroup": MTypeId(0x504d4752),

   "makeIllustratorCurves": MTypeId(0x4e4d4943),

   "makeNurbCircle": MTypeId(0x4e435243),

   "makeNurbCone": MTypeId(0x4e434e45),

   "makeNurbCube": MTypeId(0x4e435542),

   "makeNurbCylinder": MTypeId(0x4e43594c),

   "makeNurbPlane": MTypeId(0x4e504c4e),

   "makeNurbSphere": MTypeId(0x4e535048),

   "makeNurbTorus": MTypeId(0x4e544f52),

   "makeNurbsSquare": MTypeId(0x4e535152),

   "makeTextCurves": MTypeId(0x4e545843),

   "makeThreePointCircularArc": MTypeId(0x4e334341),

   "makeTwoPointCircularArc": MTypeId(0x4e324341),

   "mandelbrot": MTypeId(0x52544d41),

   "mandelbrot3D": MTypeId(0x52544d33),

   "manip2DContainer": MTypeId(0x554d3243),

   "manipContainer": MTypeId(0x554d4343),

   "marble": MTypeId(0x52544d52),

   "markerManip": MTypeId(0x554d4d41),

   "materialFacade": MTypeId(0x524d4643),

   "materialInfo": MTypeId(0x444d5449),

   "materialOverride": MTypeId(0x58000387),

   "materialTemplate": MTypeId(0x4d544c41),

   "materialTemplateOverride": MTypeId(0x58000389),

   "max": MTypeId(0x4d415844),

   "membrane": MTypeId(0x4d454d42),

   "mesh": MTypeId(0x444d5348),

   "meshVarGroup": MTypeId(0x4e4d5647),

   "min": MTypeId(0x4d494e44),

   "modulo": MTypeId(0x4d4f4444),

   "morph": MTypeId(0x4d525048),

   "motionPath": MTypeId(0x4d505448),

   "motionTrail": MTypeId(0x4d4f5452),

   "motionTrailShape": MTypeId(0x4d4f5348),

   "mountain": MTypeId(0x52544d54),

   "movie": MTypeId(0x52544d56),

   "mpBirailSrf": MTypeId(0x4e4d4253),

   "multDoubleLinear": MTypeId(0x444d444c),

   "multMatrix": MTypeId(0x444d544d),

   "multilisterLight": MTypeId(0x4d554c4c),

   "multiply": MTypeId(0x4d554c54),

   "multiplyDivide": MTypeId(0x524d4449),

   "multiplyPointByMatrix": MTypeId(0x4d50424d),

   "multiplyVectorByMatrix": MTypeId(0x4d56424d),

   "mute": MTypeId(0x4d555445),

   "nCloth": MTypeId(0x4e434c4f),

   "nComponent": MTypeId(0x4e434d50),

   "nParticle": MTypeId(0x4e504152),

   "nRigid": MTypeId(0x4e524744),

   "nearestPointOnCurve": MTypeId(0x4e504f43),

   "negate": MTypeId(0x4e454754),

   "network": MTypeId(0x4e54574b),

   "newtonField": MTypeId(0x594e4557),

   "noise": MTypeId(0x52544e33),

   "nonLinear": MTypeId(0x464e4c44),

   "normalConstraint": MTypeId(0x444e4332),

   "normalize": MTypeId(0x4e4f524d),

   "not": MTypeId(0x4e4f5442),

   "nucleus": MTypeId(0x4e535953),

   "nurbsCurve": MTypeId(0x4e435256),

   "nurbsCurveToBezier": MTypeId(0x4e525442),

   "nurbsSurface": MTypeId(0x4e535246),

   "nurbsTessellate": MTypeId(0x4e544553),

   "nurbsToSubdiv": MTypeId(0x534e5453),

   "nurbsToSubdivProc": MTypeId(0x534e5450),

   "objectAttrFilter": MTypeId(0x4f464154),

   "objectBinFilter": MTypeId(0x4f4b464c),

   "objectFilter": MTypeId(0x4f464c54),

   "objectMultiFilter": MTypeId(0x4f4d464c),

   "objectNameFilter": MTypeId(0x4f4e464c),

   "objectRenderFilter": MTypeId(0x4f52464c),

   "objectScriptFilter": MTypeId(0x4f53464c),

   "objectSet": MTypeId(0x4f425354),

   "objectTypeFilter": MTypeId(0x4f54464c),

   "ocean": MTypeId(0x52544f43),

   "oceanShader": MTypeId(0x524f5053),

   "offsetCos": MTypeId(0x4e4f4353),

   "offsetCurve": MTypeId(0x4e4f4355),

   "offsetSurface": MTypeId(0x4e4f5355),

   "oldBlindDataBase": MTypeId(0x42444454),

   "oldGeometryConstraint": MTypeId(0x44474d43),

   "oldNormalConstraint": MTypeId(0x444e5243),

   "oldTangentConstraint": MTypeId(0x44544e43),

   "opticalFX": MTypeId(0x4f504658),

   "or": MTypeId(0x4f52424f),

   "orientConstraint": MTypeId(0x444f5243),

   "orientationMarker": MTypeId(0x4f52544d),

   "pairBlend": MTypeId(0x4150424c),

   "paramDimension": MTypeId(0x52444d4e),

   "parentConstraint": MTypeId(0x44504152),

   "parentMatrix": MTypeId(0x50524d54),

   "particle": MTypeId(0x59504152),

   "particleAgeMapper": MTypeId(0x50414d41),

   "particleCloud": MTypeId(0x50434c44),

   "particleColorMapper": MTypeId(0x50434d41),

   "particleIncandMapper": MTypeId(0x50494d41),

   "particleSamplerInfo": MTypeId(0x5053494e),

   "particleTranspMapper": MTypeId(0x50544d41),

   "partition": MTypeId(0x5052544e),

   "passContributionMap": MTypeId(0x5053434d),

   "passMatrix": MTypeId(0x4450534d),

   "pfxHair": MTypeId(0x50464841),

   "pfxToon": MTypeId(0x5046544f),

   "phong": MTypeId(0x5250484f),

   "phongE": MTypeId(0x52504845),

   "pi": MTypeId(0x50494b44),

   "pickMatrix": MTypeId(0x504d4154),

   "pivotAndOrientManip": MTypeId(0x50414f4d),

   "place2dTexture": MTypeId(0x52504c32),

   "place3dTexture": MTypeId(0x52504c44),

   "planarProjManip": MTypeId(0x554d5050),

   "planarTrimSurface": MTypeId(0x4e504c54),

   "plusMinusAverage": MTypeId(0x52504d41),

   "pointConstraint": MTypeId(0x44505443),

   "pointEmitter": MTypeId(0x59454d49),

   "pointLight": MTypeId(0x504f4954),

   "pointMatrixMult": MTypeId(0x44504d4d),

   "pointOnCurveInfo": MTypeId(0x4e504349),

   "pointOnLineManip": MTypeId(0x554d504c),

   "pointOnPolyConstraint": MTypeId(0x44505043),

   "pointOnSurfManip": MTypeId(0x554d5353),

   "pointOnSurfaceInfo": MTypeId(0x4e505349),

   "pointOnSurfaceManip": MTypeId(0x554d5053),

   "poleVectorConstraint": MTypeId(0x44505643),

   "polyAppend": MTypeId(0x50415050),

   "polyAppendVertex": MTypeId(0x50415056),

   "polyAutoProj": MTypeId(0x50415550),

   "polyAverageVertex": MTypeId(0x50415656),

   "polyAxis": MTypeId(0x50435244),

   "polyBevel": MTypeId(0x5042564c),

   "polyBevel2": MTypeId(0x50425632),

   "polyBevel3": MTypeId(0x50425633),

   "polyBlindData": MTypeId(0x4d424454),

   "polyBoolOp": MTypeId(0x50424f50),

   "polyBridgeEdge": MTypeId(0x50425245),

   "polyCBoolOp": MTypeId(0x50435642),

   "polyChipOff": MTypeId(0x50434849),

   "polyCircularize": MTypeId(0x50435243),

   "polyClean": MTypeId(0x504c434c),

   "polyCloseBorder": MTypeId(0x50434c4f),

   "polyCollapseEdge": MTypeId(0x50434f45),

   "polyCollapseF": MTypeId(0x50434f46),

   "polyColorDel": MTypeId(0x5043444c),

   "polyColorMod": MTypeId(0x50434d4f),

   "polyColorPerVertex": MTypeId(0x50435056),

   "polyCone": MTypeId(0x50434f4e),

   "polyConnectComponents": MTypeId(0x50434353),

   "polyContourProj": MTypeId(0x50434e50),

   "polyCopyUV": MTypeId(0x50435556),

   "polyCrease": MTypeId(0x50435253),

   "polyCreaseEdge": MTypeId(0x50435345),

   "polyCreateFace": MTypeId(0x50435245),

   "polyCube": MTypeId(0x50435542),

   "polyCut": MTypeId(0x50504354),

   "polyCylProj": MTypeId(0x50435950),

   "polyCylinder": MTypeId(0x5043594c),

   "polyDelEdge": MTypeId(0x50444545),

   "polyDelFacet": MTypeId(0x50444546),

   "polyDelVertex": MTypeId(0x50444556),

   "polyDuplicateEdge": MTypeId(0x50445545),

   "polyEdgeToCurve": MTypeId(0x50544356),

   "polyEditEdgeFlow": MTypeId(0x50534546),

   "polyExtrudeEdge": MTypeId(0x50455845),

   "polyExtrudeFace": MTypeId(0x50455846),

   "polyExtrudeVertex": MTypeId(0x50455856),

   "polyFlipEdge": MTypeId(0x50464c45),

   "polyFlipUV": MTypeId(0x50465556),

   "polyHelix": MTypeId(0x48454c49),

   "polyHoleFace": MTypeId(0x50484645),

   "polyLayoutUV": MTypeId(0x504c5556),

   "polyMapCut": MTypeId(0x504d4143),

   "polyMapDel": MTypeId(0x504d4144),

   "polyMapSew": MTypeId(0x504d4153),

   "polyMapSewMove": MTypeId(0x5053454d),

   "polyMergeEdge": MTypeId(0x504d4545),

   "polyMergeFace": MTypeId(0x504d4546),

   "polyMergeUV": MTypeId(0x504d4755),

   "polyMergeVert": MTypeId(0x504d5645),

   "polyMirror": MTypeId(0x504d4952),

   "polyMoveEdge": MTypeId(0x504d4f45),

   "polyMoveFace": MTypeId(0x504d4f46),

   "polyMoveFacetUV": MTypeId(0x504d4655),

   "polyMoveUV": MTypeId(0x504d5556),

   "polyMoveVertex": MTypeId(0x504d4f56),

   "polyNormal": MTypeId(0x504e4f52),

   "polyNormalPerVertex": MTypeId(0x504e5056),

   "polyNormalizeUV": MTypeId(0x504e5556),

   "polyOptUvs": MTypeId(0x504f5556),

   "polyPassThru": MTypeId(0x50595054),

   "polyPinUV": MTypeId(0x50505556),

   "polyPipe": MTypeId(0x50504950),

   "polyPlanarProj": MTypeId(0x50504c50),

   "polyPlane": MTypeId(0x504d4553),

   "polyPlatonicSolid": MTypeId(0x534f4c49),

   "polyPoke": MTypeId(0x5050504b),

   "polyPrimitiveMisc": MTypeId(0x4d495343),

   "polyPrism": MTypeId(0x50505249),

   "polyProj": MTypeId(0x5050524f),

   "polyProjectCurve": MTypeId(0x50504356),

   "polyPyramid": MTypeId(0x50505952),

   "polyQuad": MTypeId(0x50515541),

   "polyReduce": MTypeId(0x50524544),

   "polyRemesh": MTypeId(0x50524d48),

   "polyRetopo": MTypeId(0x5052464d),

   "polySeparate": MTypeId(0x50534550),

   "polySewEdge": MTypeId(0x50535745),

   "polySmooth": MTypeId(0x50534d54),

   "polySmoothFace": MTypeId(0x50534d46),

   "polySmoothProxy": MTypeId(0x50534d50),

   "polySoftEdge": MTypeId(0x50534f45),

   "polySphProj": MTypeId(0x50535050),

   "polySphere": MTypeId(0x50535048),

   "polySpinEdge": MTypeId(0x50535051),

   "polySplit": MTypeId(0x5053504c),

   "polySplitEdge": MTypeId(0x50534544),

   "polySplitRing": MTypeId(0x50535052),

   "polySplitVert": MTypeId(0x50535645),

   "polyStraightenUVBorder": MTypeId(0x50535442),

   "polySubdEdge": MTypeId(0x50535545),

   "polySubdFace": MTypeId(0x50535546),

   "polyToSubdiv": MTypeId(0x50534453),

   "polyTorus": MTypeId(0x50544f52),

   "polyTransfer": MTypeId(0x50544652),

   "polyTriangulate": MTypeId(0x50545249),

   "polyTweak": MTypeId(0x5054574b),

   "polyTweakUV": MTypeId(0x50545556),

   "polyUVRectangle": MTypeId(0x50555652),

   "polyUnite": MTypeId(0x50554e49),

   "polyUnsmooth": MTypeId(0x50555344),

   "polyWedgeFace": MTypeId(0x50574643),

   "poseInterpolatorManager": MTypeId(0x5053444d),

   "positionMarker": MTypeId(0x504f534d),

   "postProcessList": MTypeId(0x50505354),

   "power": MTypeId(0x504f5744),

   "primitiveFalloff": MTypeId(0x53464f46),

   "projectCurve": MTypeId(0x4e504352),

   "projectTangent": MTypeId(0x4e50544e),

   "projection": MTypeId(0x5250524a),

   "trsManip": MTypeId(0x554d4354),

   "propMoveTriadManip": MTypeId(0x554d5054),

   "proximityFalloff": MTypeId(0x5058464f),

   "proximityPin": MTypeId(0x50525850),

   "proximityWrap": MTypeId(0x50575250),

   "proxyManager": MTypeId(0x50584d47),

   "psdFileTex": MTypeId(0x50534454),

   "quadShadingSwitch": MTypeId(0x53574834),

   "radialField": MTypeId(0x59524144),

   "ramp": MTypeId(0x52545241),

   "rampShader": MTypeId(0x52525053),

   "rbfSrf": MTypeId(0x4e524246),

   "rebuildCurve": MTypeId(0x4e524243),

   "rebuildSurface": MTypeId(0x4e524253),

   "record": MTypeId(0x52454344),

   "reference": MTypeId(0x5245464e),

   "relOverride": MTypeId(0x5800037a),

   "relUniqueOverride": MTypeId(0x580003a1),

   "remapColor": MTypeId(0x524d434c),

   "remapHsv": MTypeId(0x524d4853),

   "remapValue": MTypeId(0x524d564c),

   "renderBox": MTypeId(0x524e4258),

   "renderCone": MTypeId(0x524e434f),

   "renderGlobals": MTypeId(0x52474c42),

   "renderGlobalsList": MTypeId(0x5244474c),

   "renderLayer": MTypeId(0x524e444c),

   "renderLayerManager": MTypeId(0x524e4c4d),

   "renderPass": MTypeId(0x524e5053),

   "renderPassSet": MTypeId(0x52505353),

   "renderQuality": MTypeId(0x52515541),

   "renderRect": MTypeId(0x52524354),

   "renderSettingsChildCollection": MTypeId(0x580003a3),

   "renderSettingsCollection": MTypeId(0x58000395),

   "renderSetup": MTypeId(0x58000371),

   "renderSetupLayer": MTypeId(0x58000372),

   "renderSphere": MTypeId(0x524e5350),

   "renderTarget": MTypeId(0x524e5447),

   "renderedImageSource": MTypeId(0x52434953),

   "reorderUVSet": MTypeId(0x524f5553),

   "resolution": MTypeId(0x524c544e),

   "resultCurveTimeToAngular": MTypeId(0x52435441),

   "resultCurveTimeToLinear": MTypeId(0x5243544c),

   "resultCurveTimeToTime": MTypeId(0x52435454),

   "resultCurveTimeToUnitless": MTypeId(0x52435455),

   "reverse": MTypeId(0x52525653),

   "reverseCurve": MTypeId(0x4e525643),

   "reverseSurface": MTypeId(0x4e525653),

   "revolve": MTypeId(0x4e52564c),

   "rgbToHsv": MTypeId(0x52523248),

   "rigidBody": MTypeId(0x59524744),

   "rigidConstraint": MTypeId(0x59435354),

   "rigidSolver": MTypeId(0x59534c56),

   "rock": MTypeId(0x5254524b),

   "rotateLimitsManip": MTypeId(0x554d524c),

   "rotateManip": MTypeId(0x554d5241),

   "rotateUV2dManip": MTypeId(0x5532524f),

   "rotateVector": MTypeId(0x524f5456),

   "rotationFromMatrix": MTypeId(0x524f4d58),

   "round": MTypeId(0x524f554e),

   "roundConstantRadius": MTypeId(0x4e524352),

   "rowFromMatrix": MTypeId(0x524d4154),

   "sampler": MTypeId(0x46534d50),

   "samplerInfo": MTypeId(0x5253494e),

   "scaleConstraint": MTypeId(0x44534343),

   "scaleFromMatrix": MTypeId(0x534d4154),

   "scaleUV2dManip": MTypeId(0x55325343),

   "screenAlignedCircleManip": MTypeId(0x5341434d),

   "script": MTypeId(0x53435250),

   "scriptManip": MTypeId(0x554d5343),

   "sculpt": MTypeId(0x46534350),

   "selectionListOperator": MTypeId(0x534c4f50),

   "sequenceManager": MTypeId(0x53514d47),

   "sequencer": MTypeId(0x53514e43),

   "setRange": MTypeId(0x52524e47),

   "shaderGlow": MTypeId(0x5348474c),

   "shaderOverride": MTypeId(0x58000386),

   "shadingEngine": MTypeId(0x53484144),

   "shadingMap": MTypeId(0x53444d50),

   "shapeEditorManager": MTypeId(0x53444d4c),

   "shellTessellate": MTypeId(0x53544553),

   "shot": MTypeId(0x53484f54),

   "shrinkWrap": MTypeId(0x53575250),

   "simpleSelector": MTypeId(0x5800039e),

   "simpleTestNode": MTypeId(0x53544e44),

   "simpleVolumeShader": MTypeId(0x53565348),

   "sin": MTypeId(0x53494e45),

   "singleShadingSwitch": MTypeId(0x53574831),

   "sketchPlane": MTypeId(0x534b504e),

   "skinBinding": MTypeId(0x534b4244),

   "skinCluster": MTypeId(0x4653434c),

   "smoothCurve": MTypeId(0x4e534d43),

   "smoothStep": MTypeId(0x534d5354),

   "smoothTangentSrf": MTypeId(0x4e53544e),

   "snapUV2dManip": MTypeId(0x5532534e),

   "snapshot": MTypeId(0x534e5054),

   "snapshotShape": MTypeId(0x53534841),

   "snow": MTypeId(0x5254534e),

   "softMod": MTypeId(0x4653534c),

   "softModHandle": MTypeId(0x46535348),

   "solidFractal": MTypeId(0x52544633),

   "solidify": MTypeId(0x534f4c59),

   "spBirailSrf": MTypeId(0x4e534253),

   "sphericalProjManip": MTypeId(0x554d5350),

   "spotCylinderManip": MTypeId(0x53434d50),

   "spotLight": MTypeId(0x5350544c),

   "spring": MTypeId(0x59535052),

   "squareSrf": MTypeId(0x4e535153),

   "standardSurface": MTypeId(0x53544453),

   "stencil": MTypeId(0x52545354),

   "stereoRigCamera": MTypeId(0x53524341),

   "stitchAsNurbsShell": MTypeId(0x4e535348),

   "stitchSrf": MTypeId(0x4e535453),

   "stroke": MTypeId(0x5354524b),

   "strokeGlobals": MTypeId(0x53544b47),

   "stucco": MTypeId(0x52533630),

   "styleCurve": MTypeId(0x4e535443),

   "subCurve": MTypeId(0x4e534243),

   "subSurface": MTypeId(0x4e535352),

   "subdAddTopology": MTypeId(0x53415459),

   "subdAutoProj": MTypeId(0x53415550),

   "subdBlindData": MTypeId(0x53424454),

   "subdCleanTopology": MTypeId(0x53435459),

   "subdHierBlind": MTypeId(0x53485242),

   "subdLayoutUV": MTypeId(0x534c5556),

   "subdMapCut": MTypeId(0x534d4143),

   "subdMapSewMove": MTypeId(0x5353454d),

   "subdPlanarProj": MTypeId(0x53504c50),

   "subdTweak": MTypeId(0x5354574b),

   "subdTweakUV": MTypeId(0x53545556),

   "subdiv": MTypeId(0x53445353),

   "subdivCollapse": MTypeId(0x53434c50),

   "subdivComponentId": MTypeId(0x53534944),

   "subdivReverseFaces": MTypeId(0x53525646),

   "subdivSurfaceVarGroup": MTypeId(0x53535647),

   "subdivToNurbs": MTypeId(0x5344534e),

   "subdivToPoly": MTypeId(0x53445350),

   "subsetFalloff": MTypeId(0x5353464f),

   "subtract": MTypeId(0x53554253),

   "sum": MTypeId(0x53554d44),

   "surfaceInfo": MTypeId(0x4e53494e),

   "surfaceLuminance": MTypeId(0x52534c55),

   "surfaceShader": MTypeId(0x52535348),

   "surfaceVarGroup": MTypeId(0x4e535647),

   "symmetryConstraint": MTypeId(0x44534d43),

   "tan": MTypeId(0x54414e47),

   "tangentConstraint": MTypeId(0x44544332),

   "tension": MTypeId(0x54454e53),

   "textButtonManip": MTypeId(0x554d5442),

   "texture3dManip": MTypeId(0x554d5458),

   "textureBakeSet": MTypeId(0x5442414b),

   "textureDeformer": MTypeId(0x54584446),

   "textureDeformerHandle": MTypeId(0x54444844),

   "textureToGeom": MTypeId(0x5454474f),

   "time": MTypeId(0x54494d45),

   "timeEditor": MTypeId(0x544d4544),

   "timeEditorAnimSource": MTypeId(0x54454153),

   "timeEditorClip": MTypeId(0x41434c43),

   "timeEditorClipBase": MTypeId(0x414c434c),

   "timeEditorClipEvaluator": MTypeId(0x4143524f),

   "timeEditorInterpolator": MTypeId(0x54454950),

   "timeEditorTracks": MTypeId(0x5445544b),

   "timeFunction": MTypeId(0x7466786e),

   "timeToUnitConversion": MTypeId(0x44544d55),

   "timeWarp": MTypeId(0x54495741),

   "toggleManip": MTypeId(0x554d5447),

   "toggleOnLineManip": MTypeId(0x55544f4c),

   "toolDrawManip": MTypeId(0x5454444d),

   "toolDrawManip2D": MTypeId(0x54444d32),

   "toonLineAttributes": MTypeId(0x544c4154),

   "trackInfoManager": MTypeId(0x54494d47),

   "transUV2dManip": MTypeId(0x55325452),

   "transferAttributes": MTypeId(0x54524154),

   "transferFalloff": MTypeId(0x50464f46),

   "transform": MTypeId(0x5846524d),

   "transformGeometry": MTypeId(0x5447454f),

   "translateUVManip": MTypeId(0x554d5556),

   "translationFromMatrix": MTypeId(0x544d4154),

   "trim": MTypeId(0x4e54524d),

   "trimWithBoundaries": MTypeId(0x4e545742),

   "triplanarProjManip": MTypeId(0x554d5452),

   "tripleShadingSwitch": MTypeId(0x53574833),

   "truncate": MTypeId(0x5452554e),

   "turbulenceField": MTypeId(0x59545552),

   "tweak": MTypeId(0x464d5054),

   "ufeProxyCameraShape": MTypeId(0x55465043),

   "ufeProxyTransform": MTypeId(0x55465058),

   "uniformFalloff": MTypeId(0x55574754),

   "uniformField": MTypeId(0x59554e49),

   "unitConversion": MTypeId(0x44554e54),

   "unitToTimeConversion": MTypeId(0x4455544d),

   "unknown": MTypeId(0x554e4b4e),

   "unknownDag": MTypeId(0x554e4b44),

   "unknownTransform": MTypeId(0x554e4b54),

   "untrim": MTypeId(0x4e555452),

   "useBackground": MTypeId(0x55534247),

   "uv2dManip": MTypeId(0x5556324d),

   "uvChooser": MTypeId(0x55564348),

   "uvPin": MTypeId(0x55565256),

   "vectorProduct": MTypeId(0x52564543),

   "vertexBakeSet": MTypeId(0x5642414b),

   "viewColorManager": MTypeId(0x5657434d),

   "volumeAxisField": MTypeId(0x59565846),

   "volumeFog": MTypeId(0x52564647),

   "volumeLight": MTypeId(0x564f4c4c),

   "volumeNoise": MTypeId(0x52545633),

   "volumeShader": MTypeId(0x52565348),

   "vortexField": MTypeId(0x59564f52),

   "water": MTypeId(0x52545741),

   "weightGeometryFilter": MTypeId(0x44574746),

   "wire": MTypeId(0x46574952),

   "wood": MTypeId(0x52545744),

   "wrap": MTypeId(0x46575250),

   "wtAddMatrix": MTypeId(0x4457414d),

}

_TYPE_INT_TO_STR = {

   1380271702: "AISEnvFacade",

   1095980622: "aboutToSetValueTestNode",

   1476395896: "absOverride",

   1476395936: "absUniqueOverride",

   1094865732: "absolute",

   1094930259: "acos",

   1145128012: "addDoubleLinear",

   1145130328: "addMatrix",

   1094996813: "adskMaterial",

   1145130307: "aimConstraint",

   1095582036: "aimMatrix",

   1497450834: "airField",

   1431128408: "indexManip",

   1312902211: "alignCurve",

   1431126340: "alignManip",

   1312902227: "alignSurface",

   1095582284: "ambientLight",

   1095648322: "and",

   1312899668: "angleBetween",

   1095189582: "angleDimension",

   1094864452: "animBlend",

   1094863183: "animBlendInOut",

   1094864449: "animBlendNodeAdditive",

   1094861121: "animBlendNodeAdditiveDA",

   1094861132: "animBlendNodeAdditiveDL",

   1094861126: "animBlendNodeAdditiveF",

   1094862401: "animBlendNodeAdditiveFA",

   1094862412: "animBlendNodeAdditiveFL",

   1094861139: "animBlendNodeAdditiveI16",

   1094861129: "animBlendNodeAdditiveI32",

   1094864466: "animBlendNodeAdditiveRotation",

   1094864467: "animBlendNodeAdditiveScale",

   1094861391: "animBlendNodeBoolean",

   1094864453: "animBlendNodeEnum",

   1094865993: "animBlendNodeTime",

   1129074766: "animClip",

   1346589761: "animCurveTA",

   1346589772: "animCurveTL",

   1346589780: "animCurveTT",

   1346589781: "animCurveTU",

   1346590017: "animCurveUA",

   1346590028: "animCurveUL",

   1346590036: "animCurveUT",

   1346590037: "animCurveUU",

   1095650386: "animLayer",

   1380011593: "anisotropic",

   1095650899: "annotationShape",

   1476395932: "aovChildCollection",

   1476395931: "aovCollection",

   1476395927: "applyAbs2FloatsOverride",

   1476395905: "applyAbs3FloatsOverride",

   1476395914: "applyAbsBoolOverride",

   1476395916: "applyAbsEnumOverride",

   1476395901: "applyAbsFloatOverride",

   1476395921: "applyAbsIntOverride",

   1476395923: "applyAbsStringOverride",

   1476395908: "applyConnectionOverride",

   1476395929: "applyRel2FloatsOverride",

   1476395907: "applyRel3FloatsOverride",

   1476395903: "applyRelFloatOverride",

   1476395922: "applyRelIntOverride",

   1094995278: "arcLengthDimension",

   1095912532: "areaLight",

   1145130320: "arrayMapper",

   1431126354: "arrowManip",

   1096041811: "arubaTessellate",

   1095977294: "asin",

   1096040782: "atan",

   1096040754: "atan2",

   1312904259: "attachCurve",

   1312904275: "attachSurface",

   1096042580: "attrHierarchyTest",

   1096107081: "audio",

   1096176196: "average",

   1312899922: "avgCurves",

   1312902736: "avgNurbsSurfacePoints",

   1312904016: "avgSurfacePoints",

   1481458004: "axisFromMatrix",

   1431126608: "ballProjManip",

   1431129166: "lineManip",

   1178747219: "baseLattice",

   1476395893: "basicSelector",

   1312970316: "bevel",

   1312969558: "bevelPlus",

   1111708246: "bezierCurve",

   1112821330: "bezierCurveToNurbs",

   1346519891: "blendColorSets",

   1380076594: "blendColors",

   1112294486: "blendDevice",

   1111904070: "blendFalloff",

   1112359252: "blendMatrix",

   1178750035: "blendShape",

   1094863922: "blendTwoAttr",

   1094863959: "blendWeighted",

   1112294484: "blindDataTemplate",

   1380076622: "blinn",

   1178752332: "boneLattice",

   1312968524: "boolean",

   1312968260: "boundary",

   1380336205: "brownian",

   1112691528: "brush",

   1381253717: "bulge",

   1380078925: "bump2d",

   1380078899: "bump3d",

   1430671444: "freePointTriadManip",

   1129599563: "cacheBlend",

   1128482886: "cacheFile",

   1145258317: "camera",

   1431126864: "cameraPlaneManip",

   1146246226: "cameraSet",

   1145258326: "cameraView",

   1128614212: "ceil",

   1129205072: "centerManip",

   1128808786: "character",

   1129136464: "characterMap",

   1481590342: "characterOffset",

   1381253960: "checker",

   1128809285: "choice",

   1128812367: "chooser",

   1431126860: "circleManip",

   1430475597: "circleSweepManip",

   1380142131: "clamp",

   1129070925: "clampRange",

   1128747848: "clipGhostShape",

   1129072976: "clipLibrary",

   1129530184: "clipScheduler",

   1127368516: "clipToGhostData",

   1313030997: "closeCurve",

   1313035093: "closeSurface",

   1129336653: "closestPointOnMesh",

   1313034323: "closestPointOnSurface",

   1381253964: "cloth",

   1381253956: "cloud",

   1178815571: "cluster",

   1179272006: "clusterFlexorShape",

   1178815560: "clusterHandle",

   1476395891: "collection",

   1497583436: "collisionModel",

   1129137986: "colorManagementGlobals",

   1129270352: "colorProfile",

   1129136468: "columnFromMatrix",

   1178816083: "combinationShape",

   1129333076: "compactPlugArrayTest",

   1195790150: "componentFalloff",

   1431589965: "translateManip",

   1414484045: "componentMatch",

   1129595475: "componentTagBase",

   1476395777: "composeMatrix",

   1431126863: "concentricProjManip",

   1380142660: "condition",

   1476395909: "connectionOverride",

   1476395938: "connectionUniqueOverride",

   1129270868: "container",

   1129267777: "containerBase",

   1380142926: "contrast",

   1128747600: "controller",

   1129333587: "copyColorSet",

   1129338195: "copyUVSet",

   1129272137: "cos",

   1381184560: "crater",

   1129465153: "creaseSet",

   1129464659: "createColorSet",

   1129469267: "createUVSet",

   1129467728: "crossProduct",

   1431126869: "cubicProjManip",

   1313033539: "curveFromMeshCoM",

   1313033541: "curveFromMeshEdge",

   1396921157: "curveFromSubdivEdge",

   1396921158: "curveFromSubdivFace",

   1313035074: "curveFromSurfaceBnd",

   1313035075: "curveFromSurfaceCoS",

   1313035081: "curveFromSurfaceIso",

   1313032526: "curveInfo",

   1313030985: "curveIntersect",

   1129206337: "curveNormalizerAngle",

   1129206348: "curveNormalizerLinear",

   1431130179: "pointOnCurveManip",

   1313035847: "curveVarGroup",

   1431126873: "cylindricalProjManip",

   1145128771: "dagContainer",

   1179668307: "dagPose",

   1145197651: "dataBlockTest",

   1476395776: "decomposeMatrix",

   1145390668: "defaultLightList",

   1146246476: "defaultRenderUtilityList",

   1146244684: "defaultRenderingList",

   1380209484: "defaultShaderList",

   1380209740: "defaultTextureList",

   1178878532: "deformBend",

   1178879564: "deformFlare",

   1178882894: "deformSine",

   1178882897: "deformSquash",

   1178883159: "deformTwist",

   1178883926: "deformWave",

   1145848659: "deleteColorSet",

   1145389908: "deleteComponent",

   1145851219: "deleteUVSet",

   1145853005: "deltaMush",

   1313100867: "detachCurve",

   1313100883: "detachSurface",

   1145394253: "determinant",

   1145328451: "directedDisc",

   1145655884: "directionalLight",

   1430541133: "discManip",

   1146309443: "diskCache",

   1380209480: "displacementShader",

   1146310732: "displayLayer",

   1146113101: "displayLayerManager",

   1145324116: "distanceBetween",

   1145326926: "distanceDimShape",

   1431127117: "distanceManip",

   1145656900: "divide",

   1146046020: "dof",

   1146049616: "dotProduct",

   1398229042: "doubleShadingSwitch",

   1313096275: "dpBirailSrf",

   1497649735: "dragField",

   1145848660: "dropoffLocator",

   1497584716: "dynController",

   1497646924: "dynGlobals",

   1497910340: "dynHolder",

   1145261902: "dynamicConstraint",

   1162695748: "editMetadata",

   1162692434: "editsManager",

   1162759504: "enableManip",

   1380270668: "envBall",

   1380270920: "envChrome",

   1380270914: "envCube",

   1380271683: "envFacade",

   1380271687: "envFog",

   1380275019: "envSky",

   1380275024: "envSphere",

   1162761798: "environmentFog",

   1162958156: "equal",

   1313166152: "explodeNurbsShell",

   1145395280: "expression",

   1313167427: "extendCurve",

   1313167443: "extendSurface",

   1313167442: "extrude",

   1145455438: "facade",

   1162235718: "falloffEval",

   1312967764: "ffBlendSrf",

   1312967763: "ffBlendSrfObsolete",

   1313228371: "ffFilletSrf",

   1179010628: "ffd",

   1381254740: "file",

   1313227602: "filletCurve",

   1313231939: "fitBspline",

   1179408456: "flexorShape",

   1179406159: "floor",

   1179406167: "flow",

   1178946889: "fluidEmitter",

   1179407689: "fluidShape",

   1179864141: "fluidSliceManip",

   1179407444: "fluidTexture2D",

   1179407448: "fluidTexture3D",

   1212371542: "follicle",

   1431127637: "forceUpdateManip",

   1179669070: "fosterParent",

   1178748493: "fourByFourMatrix",

   1381249606: "fractal",

   1178813256: "frameCache",

   1431127632: "freePointManip",

   1380401485: "gammaCorrect",

   1497842511: "geoConnectable",

   1497842516: "geoConnector",

   1195526478: "geomBind",

   1145523779: "geometryConstraint",

   1145521737: "geometryFilter",

   1431127884: "geometryOnLineManip",

   1313297991: "geometryVarGroup",

   1195590476: "globalCacheControl",

   1313297236: "globalStitch",

   1381254994: "granite",

   1497846337: "gravityField",

   1196446545: "greasePencilSequence",

   1145524300: "greasePlane",

   1196446291: "greasePlaneRenderShape",

   1196577864: "greaterThan",

   1381254980: "grid",

   1476395941: "group",

   1196443972: "groupId",

   1196576848: "groupParts",

   1179080009: "guide",

   1213221198: "hairConstraint",

   1213421907: "hairSystem",

   1380471874: "hairTubeShader",

   1313358928: "hardenPoint",

   1213682247: "hardwareRenderGlobals",

   1213354567: "hardwareRenderingGlobals",

   1329811536: "heightField",

   1213484593: "hierarchyTestNode1",

   1213484594: "hierarchyTestNode2",

   1213484595: "hierarchyTestNode3",

   1145456971: "hikEffector",

   1247037771: "hikFKJoint",

   1212564301: "hikFloorContactMarker",

   1212632644: "hikGroundPlane",

   1263028552: "hikHandle",

   1229669702: "hikIKEffector",

   1263028555: "hikSolver",

   1212765011: "historySwitch",

   1146112077: "holdMatrix",

   1380463186: "hsvToRgb",

   1213682253: "hwReflectionMap",

   1497911876: "hwRenderGlobals",

   1213812818: "hyperGraphInfo",

   1213812812: "hyperLayout",

   1145589846: "hyperView",

   1262831174: "ikEffector",

   1263027276: "ikHandle",

   1263354707: "ikMCsolver",

   1263550803: "ikPASolver",

   1263685715: "ikRPsolver",

   1263747923: "ikSCsolver",

   1263751251: "ikSplineSolver",

   1263753555: "ikSystem",

   1145655372: "imagePlane",

   1179206232: "implicitBox",

   1179206479: "implicitCone",

   1179210576: "implicitSphere",

   1313426243: "insertKnotCurve",

   1313426259: "insertKnotSurface",

   1498305364: "instancer",

   1313428294: "intersectSurface",

   1229738576: "inverseLerp",

   1246184518: "jiggle",

   1246710094: "joint",

   1179272012: "jointCluster",

   1179010114: "jointFfd",

   1178748236: "jointLattice",

   1262899789: "keyframeRegionManip",

   1262965328: "keyingGroup",

   1380729165: "lambert",

   1179402580: "lattice",

   1280922195: "layeredShader",

   1280922196: "layeredTexture",

   1313624909: "leastSquaresModifier",

   1381256261: "leather",

   1279610439: "length",

   1279611472: "lerp",

   1280529480: "lessThan",

   1476396003: "lightEditor",

   1380339527: "lightFog",

   1476396002: "lightGroup",

   1380731214: "lightInfo",

   1476396001: "lightItem",

   1380731979: "lightLinker",

   1280070484: "lightList",

   1476395930: "lightsChildCollection",

   1476395924: "lightsCollection",

   1476395940: "lightsCollectionSelector",

   1280593232: "limitManip",

   1280134980: "lineModifier",

   1280262996: "locator",

   1280263239: "lodGroup",

   1280263252: "lodThresholds",

   1314081614: "loft",

   1280264004: "log",

   1145848148: "lookAt",

   1380734285: "luminance",

   1347241810: "makeGroup",

   1313687875: "makeIllustratorCurves",

   1313034819: "makeNurbCircle",

   1313033797: "makeNurbCone",

   1313035586: "makeNurbCube",

   1313036620: "makeNurbCylinder",

   1313885262: "makeNurbPlane",

   1314082888: "makeNurbSphere",

   1314148178: "makeNurbTorus",

   1314083154: "makeNurbsSquare",

   1314150467: "makeTextCurves",

   1311982401: "makeThreePointCircularArc",

   1311916865: "makeTwoPointCircularArc",

   1381256513: "mandelbrot",

   1381256499: "mandelbrot3D",

   1431122499: "manip2DContainer",

   1431126851: "manipContainer",

   1381256530: "marble",

   1431129409: "markerManip",

   1380795971: "materialFacade",

   1145918537: "materialInfo",

   1476395911: "materialOverride",

   1297370177: "materialTemplate",

   1476395913: "materialTemplateOverride",

   1296128068: "max",

   1296387394: "membrane",

   1145918280: "mesh",

   1313691207: "meshVarGroup",

   1296649796: "min",

   1297040452: "modulo",

   1297240136: "morph",

   1297110088: "motionPath",

   1297044562: "motionTrail",

   1297044296: "motionTrailShape",

   1381256532: "mountain",

   1381256534: "movie",

   1313686099: "mpBirailSrf",

   1145914444: "multDoubleLinear",

   1145918541: "multMatrix",

   1297435724: "multilisterLight",

   1297435732: "multiply",

   1380795465: "multiplyDivide",

   1297105485: "multiplyPointByMatrix",

   1297498701: "multiplyVectorByMatrix",

   1297437765: "mute",

   1313033295: "nCloth",

   1313033552: "nComponent",

   1313882450: "nParticle",

   1314015044: "nRigid",

   1313886019: "nearestPointOnCurve",

   1313163092: "negate",

   1314150219: "network",

   1498301783: "newtonField",

   1381256755: "noise",

   1179536452: "nonLinear",

   1145979698: "normalConstraint",

   1313821261: "normalize",

   1313821762: "not",

   1314085203: "nucleus",

   1313034838: "nurbsCurve",

   1314018370: "nurbsCurveToBezier",

   1314083398: "nurbsSurface",

   1314145619: "nurbsTessellate",

   1397642323: "nurbsToSubdiv",

   1397642320: "nurbsToSubdivProc",

   1330004308: "objectAttrFilter",

   1330333260: "objectBinFilter",

   1330007124: "objectFilter",

   1330464332: "objectMultiFilter",

   1330529868: "objectNameFilter",

   1330792012: "objectRenderFilter",

   1330857548: "objectScriptFilter",

   1329746772: "objectSet",

   1330923084: "objectTypeFilter",

   1381257027: "ocean",

   1380929619: "oceanShader",

   1313817427: "offsetCos",

   1313817429: "offsetCurve",

   1313821525: "offsetSurface",

   1111770196: "oldBlindDataBase",

   1145523523: "oldGeometryConstraint",

   1145983555: "oldNormalConstraint",

   1146375747: "oldTangentConstraint",

   1330660952: "opticalFX",

   1330790991: "or",

   1146049091: "orientConstraint",

   1330795597: "orientationMarker",

   1095778892: "pairBlend",

   1380207950: "paramDimension",

   1146110290: "parentConstraint",

   1347571028: "parentMatrix",

   1498431826: "particle",

   1346456897: "particleAgeMapper",

   1346587716: "particleCloud",

   1346587969: "particleColorMapper",

   1346981185: "particleIncandMapper",

   1347635534: "particleSamplerInfo",

   1347702081: "particleTranspMapper",

   1347572814: "partition",

   1347633997: "passContributionMap",

   1146114893: "passMatrix",

   1346783297: "pfxHair",

   1346786383: "pfxToon",

   1380993103: "phong",

   1380993093: "phongE",

   1346980676: "pi",

   1347240276: "pickMatrix",

   1346457421: "pivotAndOrientManip",

   1380994098: "place2dTexture",

   1380994116: "place3dTexture",

   1431130192: "planarProjManip",

   1313885268: "planarTrimSurface",

   1380994369: "plusMinusAverage",

   1146115139: "pointConstraint",

   1497713993: "pointEmitter",

   1347373396: "pointLight",

   1146113357: "pointMatrixMult",

   1313882953: "pointOnCurveInfo",

   1431130188: "pointOnLineManip",

   1146114115: "pointOnPolyConstraint",

   1431130963: "pointOnSurfManip",

   1313887049: "pointOnSurfaceInfo",

   1431130195: "pointOnSurfaceManip",

   1146115651: "poleVectorConstraint",

   1346457680: "polyAppend",

   1346457686: "polyAppendVertex",

   1346458960: "polyAutoProj",

   1346459222: "polyAverageVertex",

   1346589252: "polyAxis",

   1346524748: "polyBevel",

   1346524722: "polyBevel2",

   1346524723: "polyBevel3",

   1296188500: "polyBlindData",

   1346522960: "polyBoolOp",

   1346523717: "polyBridgeEdge",

   1346590274: "polyCBoolOp",

   1346586697: "polyChipOff",

   1346589251: "polyCircularize",

   1347175244: "polyClean",

   1346587727: "polyCloseBorder",

   1346588485: "polyCollapseEdge",

   1346588486: "polyCollapseF",

   1346585676: "polyColorDel",

   1346587983: "polyColorMod",

   1346588758: "polyColorPerVertex",

   1346588494: "polyCone",

   1346585427: "polyConnectComponents",

   1346588240: "polyContourProj",

   1346590038: "polyCopyUV",

   1346589267: "polyCrease",

   1346589509: "polyCreaseEdge",

   1346589253: "polyCreateFace",

   1346590018: "polyCube",

   1347437396: "polyCut",

   1346591056: "polyCylProj",

   1346591052: "polyCylinder",

   1346651461: "polyDelEdge",

   1346651462: "polyDelFacet",

   1346651478: "polyDelVertex",

   1346655557: "polyDuplicateEdge",

   1347699542: "polyEdgeToCurve",

   1347634502: "polyEditEdgeFlow",

   1346721861: "polyExtrudeEdge",

   1346721862: "polyExtrudeFace",

   1346721878: "polyExtrudeVertex",

   1346784325: "polyFlipEdge",

   1346786646: "polyFlipUV",

   1212501065: "polyHelix",

   1346913861: "polyHoleFace",

   1347179862: "polyLayoutUV",

   1347240259: "polyMapCut",

   1347240260: "polyMapDel",

   1347240275: "polyMapSew",

   1347634509: "polyMapSewMove",

   1347241285: "polyMergeEdge",

   1347241286: "polyMergeFace",

   1347241813: "polyMergeUV",

   1347245637: "polyMergeVert",

   1347242322: "polyMirror",

   1347243845: "polyMoveEdge",

   1347243846: "polyMoveFace",

   1347241557: "polyMoveFacetUV",

   1347245398: "polyMoveUV",

   1347243862: "polyMoveVertex",

   1347309394: "polyNormal",

   1347309654: "polyNormalPerVertex",

   1347310934: "polyNormalizeUV",

   1347376470: "polyOptUvs",

   1348030548: "polyPassThru",

   1347442006: "polyPinUV",

   1347438928: "polyPipe",

   1347439696: "polyPlanarProj",

   1347241299: "polyPlane",

   1397705801: "polyPlatonicSolid",

   1347440715: "polyPoke",

   1296651075: "polyPrimitiveMisc",

   1347441225: "polyPrism",

   1347441231: "polyProj",

   1347437398: "polyProjectCurve",

   1347443026: "polyPyramid",

   1347507521: "polyQuad",

   1347568964: "polyReduce",

   1347571016: "polyRemesh",

   1347569229: "polyRetopo",

   1347634512: "polySeparate",

   1347639109: "polySewEdge",

   1347636564: "polySmooth",

   1347636550: "polySmoothFace",

   1347636560: "polySmoothProxy",

   1347637061: "polySoftEdge",

   1347637328: "polySphProj",

   1347637320: "polySphere",

   1347637329: "polySpinEdge",

   1347637324: "polySplit",

   1347634500: "polySplitEdge",

   1347637330: "polySplitRing",

   1347638853: "polySplitVert",

   1347638338: "polyStraightenUVBorder",

   1347638597: "polySubdEdge",

   1347638598: "polySubdFace",

   1347634259: "polyToSubdiv",

   1347702610: "polyTorus",

   1347700306: "polyTransfer",

   1347703369: "polyTriangulate",

   1347704651: "polyTweak",

   1347704150: "polyTweakUV",

   1347769938: "polyUVRectangle",

   1347767881: "polyUnite",

   1347769156: "polyUnsmooth",

   1347896899: "polyWedgeFace",

   1347634253: "poseInterpolatorManager",

   1347375949: "positionMarker",

   1347441492: "postProcessList",

   1347376964: "power",

   1397116742: "primitiveFalloff",

   1313882962: "projectCurve",

   1313887310: "projectTangent",

   1380995658: "projection",

   1431126868: "trsManip",

   1431130196: "propMoveTriadManip",

   1347962447: "proximityFalloff",

   1347573840: "proximityPin",

   1347899984: "proximityWrap",

   1347964231: "proxyManager",

   1347634260: "psdFileTex",

   1398229044: "quadShadingSwitch",

   1498562884: "radialField",

   1381257793: "ramp",

   1381126227: "rampShader",

   1314013766: "rbfSrf",

   1314013763: "rebuildCurve",

   1314013779: "rebuildSurface",

   1380270916: "record",

   1380271694: "reference",

   1476395898: "relOverride",

   1476395937: "relUniqueOverride",

   1380795212: "remapColor",

   1380796499: "remapHsv",

   1380800076: "remapValue",

   1380860504: "renderBox",

   1380860751: "renderCone",

   1380404290: "renderGlobals",

   1380206412: "renderGlobalsList",

   1380861004: "renderLayer",

   1380863053: "renderLayerManager",

   1380864083: "renderPass",

   1380995923: "renderPassSet",

   1381061953: "renderQuality",

   1381122900: "renderRect",

   1476395939: "renderSettingsChildCollection",

   1476395925: "renderSettingsCollection",

   1476395889: "renderSetup",

   1476395890: "renderSetupLayer",

   1380864848: "renderSphere",

   1380865095: "renderTarget",

   1380141395: "renderedImageSource",

   1380930899: "reorderUVSet",

   1380734030: "resolution",

   1380144193: "resultCurveTimeToAngular",

   1380144204: "resultCurveTimeToLinear",

   1380144212: "resultCurveTimeToTime",

   1380144213: "resultCurveTimeToUnitless",

   1381127763: "reverse",

   1314018883: "reverseCurve",

   1314018899: "reverseSurface",

   1314018892: "revolve",

   1381118536: "rgbToHsv",

   1498564420: "rigidBody",

   1497584468: "rigidConstraint",

   1498631254: "rigidSolver",

   1381257803: "rock",

   1431130700: "rotateLimitsManip",

   1431130689: "rotateManip",

   1429361231: "rotateUV2dManip",

   1380930646: "rotateVector",

   1380928856: "rotationFromMatrix",

   1380930894: "round",

   1314014034: "roundConstantRadius",

   1380794708: "rowFromMatrix",

   1179864400: "sampler",

   1381189966: "samplerInfo",

   1146307395: "scaleConstraint",

   1397571924: "scaleFromMatrix",

   1429361475: "scaleUV2dManip",

   1396785997: "screenAlignedCircleManip",

   1396920912: "script",

   1431130947: "scriptManip",

   1179861840: "sculpt",

   1397509968: "selectionListOperator",

   1397837127: "sequenceManager",

   1397837379: "sequencer",

   1381125703: "setRange",

   1397245772: "shaderGlow",

   1476395910: "shaderOverride",

   1397244228: "shadingEngine",

   1396985168: "shadingMap",

   1396985164: "shapeEditorManager",

   1398031699: "shellTessellate",

   1397247828: "shot",

   1398231632: "shrinkWrap",

   1476395934: "simpleSelector",

   1398033988: "simpleTestNode",

   1398166344: "simpleVolumeShader",

   1397313093: "sin",

   1398229041: "singleShadingSwitch",

   1397444686: "sketchPlane",

   1397441092: "skinBinding",

   1179861836: "skinCluster",

   1314082115: "smoothCurve",

   1397576532: "smoothStep",

   1314083918: "smoothTangentSrf",

   1429361486: "snapUV2dManip",

   1397641300: "snapshot",

   1397966913: "snapshotShape",

   1381258062: "snow",

   1179865932: "softMod",

   1179865928: "softModHandle",

   1381254707: "solidFractal",

   1397705817: "solidify",

   1314079315: "spBirailSrf",

   1431130960: "sphericalProjManip",

   1396919632: "spotCylinderManip",

   1397773388: "spotLight",

   1498632274: "spring",

   1314083155: "squareSrf",

   1398031443: "standardSurface",

   1381258068: "stencil",

   1397900097: "stereoRigCamera",

   1314083656: "stitchAsNurbsShell",

   1314083923: "stitchSrf",

   1398035019: "stroke",

   1398033223: "strokeGlobals",

   1381185072: "stucco",

   1314083907: "styleCurve",

   1314079299: "subCurve",

   1314083666: "subSurface",

   1396790361: "subdAddTopology",

   1396790608: "subdAutoProj",

   1396851796: "subdBlindData",

   1396921433: "subdCleanTopology",

   1397248578: "subdHierBlind",

   1397511510: "subdLayoutUV",

   1397571907: "subdMapCut",

   1397966157: "subdMapSewMove",

   1397771344: "subdPlanarProj",

   1398036299: "subdTweak",

   1398035798: "subdTweakUV",

   1396986707: "subdiv",

   1396919376: "subdivCollapse",

   1397967172: "subdivComponentId",

   1397904966: "subdivReverseFaces",

   1397970503: "subdivSurfaceVarGroup",

   1396986702: "subdivToNurbs",

   1396986704: "subdivToPoly",

   1397966415: "subsetFalloff",

   1398096467: "subtract",

   1398099268: "sum",

   1314081102: "surfaceInfo",

   1381190741: "surfaceLuminance",

   1381192520: "surfaceShader",

   1314084423: "surfaceVarGroup",

   1146309955: "symmetryConstraint",

   1413566023: "tan",

   1146372914: "tangentConstraint",

   1413828179: "tension",

   1431131202: "textButtonManip",

   1431131224: "texture3dManip",

   1413628235: "textureBakeSet",

   1415070790: "textureDeformer",

   1413761092: "textureDeformerHandle",

   1414809423: "textureToGeom",

   1414090053: "time",

   1414350148: "timeEditor",

   1413824851: "timeEditorAnimSource",

   1094929475: "timeEditorClip",

   1095517004: "timeEditorClipBase",

   1094931023: "timeEditorClipEvaluator",

   1413826896: "timeEditorInterpolator",

   1413829707: "timeEditorTracks",

   1952872558: "timeFunction",

   1146375509: "timeToUnitConversion",

   1414092609: "timeWarp",

   1431131207: "toggleManip",

   1431588684: "toggleOnLineManip",

   1414808653: "toolDrawManip",

   1413762354: "toolDrawManip2D",

   1414283604: "toonLineAttributes",

   1414090055: "trackInfoManager",

   1429361746: "transUV2dManip",

   1414676820: "transferAttributes",

   1346785094: "transferFalloff",

   1481003597: "transform",

   1413956943: "transformGeometry",

   1431131478: "translateUVManip",

   1414349140: "translationFromMatrix",

   1314148941: "trim",

   1314150210: "trimWithBoundaries",

   1431131218: "triplanarProjManip",

   1398229043: "tripleShadingSwitch",

   1414681934: "truncate",

   1498699090: "turbulenceField",

   1179471956: "tweak",

   1430671427: "ufeProxyCameraShape",

   1430671448: "ufeProxyTransform",

   1431783252: "uniformFalloff",

   1498762825: "uniformField",

   1146441300: "unitConversion",

   1146442829: "unitToTimeConversion",

   1431194446: "unknown",

   1431194436: "unknownDag",

   1431194452: "unknownTransform",

   1314214994: "untrim",

   1431519815: "useBackground",

   1431712333: "uv2dManip",

   1431716680: "uvChooser",

   1431720534: "uvPin",

   1381385539: "vectorProduct",

   1447182667: "vertexBakeSet",

   1448559437: "viewColorManager",

   1498830918: "volumeAxisField",

   1381385799: "volumeFog",

   1448037452: "volumeLight",

   1381258803: "volumeNoise",

   1381389128: "volumeShader",

   1498828626: "vortexField",

   1381259073: "water",

   1146570566: "weightGeometryFilter",

   1180125522: "wire",

   1381259076: "wood",

   1180127824: "wrap",

   1146569037: "wtAddMatrix",

}

_API_TYPES_INT_TO_STR = {
    0: "kInvalid",
    1: "kBase",
    2: "kNamedObject",
    3: "kModel",
    4: "kDependencyNode",
    5: "kAddDoubleLinear",
    6: "kAffect",
    7: "kAnimCurve",
    8: "kAnimCurveTimeToAngular",
    9: "kAnimCurveTimeToDistance",
    10: "kAnimCurveTimeToTime",
    11: "kAnimCurveTimeToUnitless",
    12: "kAnimCurveUnitlessToAngular",
    13: "kAnimCurveUnitlessToDistance",
    14: "kAnimCurveUnitlessToTime",
    15: "kAnimCurveUnitlessToUnitless",
    16: "kResultCurve",
    17: "kResultCurveTimeToAngular",
    18: "kResultCurveTimeToDistance",
    19: "kResultCurveTimeToTime",
    20: "kResultCurveTimeToUnitless",
    21: "kAngleBetween",
    22: "kAudio",
    23: "kBackground",
    24: "kColorBackground",
    25: "kFileBackground",
    26: "kRampBackground",
    27: "kBlend",
    28: "kBlendTwoAttr",
    29: "kBlendWeighted",
    30: "kBlendDevice",
    31: "kBlendColors",
    32: "kBump",
    33: "kBump3d",
    34: "kCameraView",
    35: "kChainToSpline",
    36: "kChoice",
    37: "kCondition",
    38: "kContrast",
    39: "kClampColor",
    40: "kCreate",
    41: "kAlignCurve",
    42: "kAlignSurface",
    43: "kAttachCurve",
    44: "kAttachSurface",
    45: "kAvgCurves",
    46: "kAvgSurfacePoints",
    47: "kAvgNurbsSurfacePoints",
    48: "kBevel",
    49: "kBirailSrf",
    50: "kDPbirailSrf",
    51: "kMPbirailSrf",
    52: "kSPbirailSrf",
    53: "kBoundary",
    54: "kCircle",
    55: "kCloseCurve",
    56: "kClosestPointOnSurface",
    57: "kCloseSurface",
    58: "kCurveFromSurface",
    59: "kCurveFromSurfaceBnd",
    60: "kCurveFromSurfaceCoS",
    61: "kCurveFromSurfaceIso",
    62: "kCurveInfo",
    63: "kDetachCurve",
    64: "kDetachSurface",
    65: "kExtendCurve",
    66: "kExtendSurface",
    67: "kExtrude",
    68: "kFFblendSrf",
    69: "kFFfilletSrf",
    70: "kFilletCurve",
    71: "kFitBspline",
    72: "kFlow",
    73: "kHardenPointCurve",
    74: "kIllustratorCurve",
    75: "kInsertKnotCrv",
    76: "kInsertKnotSrf",
    77: "kIntersectSurface",
    78: "kNurbsTesselate",
    79: "kNurbsPlane",
    80: "kNurbsCube",
    81: "kOffsetCos",
    82: "kOffsetCurve",
    83: "kPlanarTrimSrf",
    84: "kPointOnCurveInfo",
    85: "kPointOnSurfaceInfo",
    86: "kPrimitive",
    87: "kProjectCurve",
    88: "kProjectTangent",
    89: "kRBFsurface",
    90: "kRebuildCurve",
    91: "kRebuildSurface",
    92: "kReverseCurve",
    93: "kReverseSurface",
    94: "kRevolve",
    95: "kRevolvedPrimitive",
    96: "kCone",
    97: "kRenderCone",
    98: "kCylinder",
    99: "kSphere",
    100: "kSkin",
    101: "kStitchSrf",
    102: "kSubCurve",
    103: "kSurfaceInfo",
    104: "kTextCurves",
    105: "kTrim",
    106: "kUntrim",
    107: "kDagNode",
    108: "kProxy",
    109: "kUnderWorld",
    110: "kTransform",
    111: "kAimConstraint",
    112: "kLookAt",
    113: "kGeometryConstraint",
    114: "kGeometryVarGroup",
    115: "kAnyGeometryVarGroup",
    116: "kCurveVarGroup",
    117: "kMeshVarGroup",
    118: "kSurfaceVarGroup",
    119: "kIkEffector",
    120: "kIkHandle",
    121: "kJoint",
    122: "kManipulator3D",
    123: "kArrowManip",
    124: "kAxesActionManip",
    125: "kBallProjectionManip",
    126: "kCircleManip",
    127: "kScreenAlignedCircleManip",
    128: "kCircleSweepManip",
    129: "kConcentricProjectionManip",
    130: "kCubicProjectionManip",
    131: "kCylindricalProjectionManip",
    132: "kDiscManip",
    133: "kFreePointManip",
    134: "kCenterManip",
    135: "kLimitManip",
    136: "kEnableManip",
    137: "kFreePointTriadManip",
    138: "kPropMoveTriadManip",
    139: "kTowPointManip",
    140: "kPolyCreateToolManip",
    141: "kPolySplitToolManip",
    142: "kGeometryOnLineManip",
    143: "kCameraPlaneManip",
    144: "kToggleOnLineManip",
    145: "kStateManip",
    146: "kIsoparmManip",
    147: "kLineManip",
    148: "kManipContainer",
    149: "kAverageCurveManip",
    150: "kBarnDoorManip",
    151: "kBevelManip",
    152: "kBlendManip",
    153: "kButtonManip",
    154: "kCameraManip",
    155: "kCoiManip",
    156: "kCpManip",
    157: "kCreateCVManip",
    158: "kCreateEPManip",
    159: "kCurveEdManip",
    160: "kCurveSegmentManip",
    161: "kDirectionManip",
    162: "kDofManip",
    163: "kDropoffManip",
    164: "kExtendCurveDistanceManip",
    165: "kExtrudeManip",
    166: "kIkSplineManip",
    167: "kIkRPManip",
    168: "kJointClusterManip",
    169: "kLightManip",
    170: "kMotionPathManip",
    171: "kOffsetCosManip",
    172: "kOffsetCurveManip",
    173: "kProjectionManip",
    174: "kPolyProjectionManip",
    175: "kProjectionUVManip",
    176: "kProjectionMultiManip",
    177: "kProjectTangentManip",
    178: "kPropModManip",
    179: "kQuadPtOnLineManip",
    180: "kRbfSrfManip",
    181: "kReverseCurveManip",
    182: "kReverseCrvManip",
    183: "kReverseSurfaceManip",
    184: "kRevolveManip",
    185: "kRevolvedPrimitiveManip",
    186: "kSpotManip",
    187: "kSpotCylinderManip",
    188: "kTriplanarProjectionManip",
    189: "kTrsManip",
    190: "kDblTrsManip",
    191: "kPivotManip2D",
    192: "kManip2DContainer",
    193: "kPolyMoveUVManip",
    194: "kPolyMappingManip",
    195: "kPolyModifierManip",
    196: "kPolyMoveVertexManip",
    197: "kPolyVertexNormalManip",
    198: "kTexSmudgeUVManip",
    199: "kTexLatticeDeformManip",
    200: "kTexLattice",
    201: "kTexSmoothManip",
    202: "kTrsTransManip",
    203: "kTrsInsertManip",
    204: "kTrsXformManip",
    205: "kManipulator2D",
    206: "kTranslateManip2D",
    207: "kPlanarProjectionManip",
    208: "kPointOnCurveManip",
    209: "kTowPointOnCurveManip",
    210: "kMarkerManip",
    211: "kPointOnLineManip",
    212: "kPointOnSurfaceManip",
    213: "kTranslateUVManip",
    214: "kRotateBoxManip",
    215: "kRotateManip",
    216: "kHandleRotateManip",
    217: "kRotateLimitsManip",
    218: "kScaleLimitsManip",
    219: "kScaleManip",
    220: "kScalingBoxManip",
    221: "kScriptManip",
    222: "kSphericalProjectionManip",
    223: "kTextureManip3D",
    224: "kToggleManip",
    225: "kTranslateBoxManip",
    226: "kTranslateLimitsManip",
    227: "kTranslateManip",
    228: "kTrimManip",
    229: "kJointTranslateManip",
    230: "kManipulator",
    231: "kCirclePointManip",
    232: "kDimensionManip",
    233: "kFixedLineManip",
    234: "kLightProjectionGeometry",
    235: "kLineArrowManip",
    236: "kPointManip",
    237: "kTriadManip",
    238: "kNormalConstraint",
    239: "kOrientConstraint",
    240: "kPointConstraint",
    241: "kSymmetryConstraint",
    242: "kParentConstraint",
    243: "kPoleVectorConstraint",
    244: "kScaleConstraint",
    245: "kTangentConstraint",
    246: "kUnknownTransform",
    247: "kWorld",
    248: "kShape",
    249: "kBaseLattice",
    250: "kCamera",
    251: "kCluster",
    252: "kSoftMod",
    253: "kCollision",
    254: "kDummy",
    255: "kEmitter",
    256: "kField",
    257: "kAir",
    258: "kDrag",
    259: "kGravity",
    260: "kNewton",
    261: "kRadial",
    262: "kTurbulence",
    263: "kUniform",
    264: "kVortex",
    265: "kGeometric",
    266: "kCurve",
    267: "kNurbsCurve",
    268: "kNurbsCurveGeom",
    269: "kDimension",
    270: "kAngle",
    271: "kAnnotation",
    272: "kDistance",
    273: "kArcLength",
    274: "kRadius",
    275: "kParamDimension",
    276: "kDirectedDisc",
    277: "kRenderRect",
    278: "kEnvFogShape",
    279: "kLattice",
    280: "kLatticeGeom",
    281: "kLocator",
    282: "kDropoffLocator",
    283: "kMarker",
    284: "kOrientationMarker",
    285: "kPositionMarker",
    286: "kOrientationLocator",
    287: "kTrimLocator",
    288: "kPlane",
    289: "kSketchPlane",
    290: "kGroundPlane",
    291: "kOrthoGrid",
    292: "kSprite",
    293: "kSurface",
    294: "kNurbsSurface",
    295: "kNurbsSurfaceGeom",
    296: "kMesh",
    297: "kMeshGeom",
    298: "kRenderSphere",
    299: "kFlexor",
    300: "kClusterFlexor",
    301: "kGuideLine",
    302: "kLight",
    303: "kAmbientLight",
    304: "kNonAmbientLight",
    305: "kAreaLight",
    306: "kLinearLight",
    307: "kNonExtendedLight",
    308: "kDirectionalLight",
    309: "kPointLight",
    310: "kSpotLight",
    311: "kParticle",
    312: "kPolyToolFeedbackShape",
    313: "kRigidConstraint",
    314: "kRigid",
    315: "kSpring",
    316: "kUnknownDag",
    317: "kDefaultLightList",
    318: "kDeleteComponent",
    319: "kDispatchCompute",
    320: "kShadingEngine",
    321: "kDisplacementShader",
    322: "kDistanceBetween",
    323: "kDOF",
    324: "kDummyConnectable",
    325: "kDynamicsController",
    326: "kGeoConnectable",
    327: "kExpression",
    328: "kExtract",
    329: "kFilter",
    330: "kFilterClosestSample",
    331: "kFilterEuler",
    332: "kFilterSimplify",
    333: "kGammaCorrect",
    334: "kGeometryFilt",
    335: "kBendLattice",
    336: "kBlendShape",
    337: "kCombinationShape",
    338: "kBulgeLattice",
    339: "kFFD",
    340: "kFfdDualBase",
    341: "kRigidDeform",
    342: "kSculpt",
    343: "kTextureDeformer",
    344: "kTextureDeformerHandle",
    345: "kTweak",
    346: "kWeightGeometryFilt",
    347: "kClusterFilter",
    348: "kSoftModFilter",
    349: "kJointCluster",
    350: "kDeltaMush",
    351: "kTension",
    352: "kMorph",
    353: "kSolidify",
    354: "kProximityWrap",
    355: "kWire",
    356: "kGroupId",
    357: "kGroupParts",
    358: "kGuide",
    359: "kHsvToRgb",
    360: "kHyperGraphInfo",
    361: "kHyperLayout",
    362: "kHyperView",
    363: "kIkSolver",
    364: "kMCsolver",
    365: "kPASolver",
    366: "kSCsolver",
    367: "kRPsolver",
    368: "kSplineSolver",
    369: "kIkSystem",
    370: "kImagePlane",
    371: "kLambert",
    372: "kReflect",
    373: "kBlinn",
    374: "kPhong",
    375: "kPhongExplorer",
    376: "kLayeredShader",
    377: "kStandardSurface",
    378: "kLightInfo",
    379: "kLeastSquares",
    380: "kLightFogMaterial",
    381: "kEnvFogMaterial",
    382: "kLightList",
    383: "kLightSource",
    384: "kLuminance",
    385: "kMakeGroup",
    386: "kMaterial",
    387: "kDiffuseMaterial",
    388: "kLambertMaterial",
    389: "kBlinnMaterial",
    390: "kPhongMaterial",
    391: "kLightSourceMaterial",
    392: "kMaterialInfo",
    393: "kMaterialTemplate",
    394: "kMatrixAdd",
    395: "kMatrixHold",
    396: "kMatrixMult",
    397: "kMatrixPass",
    398: "kMatrixWtAdd",
    399: "kMidModifier",
    400: "kMidModifierWithMatrix",
    401: "kPolyBevel",
    402: "kPolyTweak",
    403: "kPolyAppend",
    404: "kPolyChipOff",
    405: "kPolyCloseBorder",
    406: "kPolyCollapseEdge",
    407: "kPolyCollapseF",
    408: "kPolyCylProj",
    409: "kPolyDelEdge",
    410: "kPolyDelFacet",
    411: "kPolyDelVertex",
    412: "kPolyExtrudeFacet",
    413: "kPolyMapCut",
    414: "kPolyMapDel",
    415: "kPolyMapSew",
    416: "kPolyMergeEdge",
    417: "kPolyMergeFacet",
    418: "kPolyMoveEdge",
    419: "kPolyMoveFacet",
    420: "kPolyMoveFacetUV",
    421: "kPolyMoveUV",
    422: "kPolyMoveVertex",
    423: "kPolyMoveVertexUV",
    424: "kPolyNormal",
    425: "kPolyPlanProj",
    426: "kPolyProj",
    427: "kPolyQuad",
    428: "kPolySmooth",
    429: "kPolySoftEdge",
    430: "kPolySphProj",
    431: "kPolySplit",
    432: "kPolySubdEdge",
    433: "kPolySubdFacet",
    434: "kPolyTriangulate",
    435: "kPolyCreator",
    436: "kPolyPrimitive",
    437: "kPolyCone",
    438: "kPolyCube",
    439: "kPolyCylinder",
    440: "kPolyMesh",
    441: "kPolySphere",
    442: "kPolyTorus",
    443: "kPolyCreateFacet",
    444: "kPolyUnite",
    445: "kMotionPath",
    446: "kPluginMotionPathNode",
    447: "kMultilisterLight",
    448: "kMultiplyDivide",
    449: "kOldGeometryConstraint",
    450: "kOpticalFX",
    451: "kParticleAgeMapper",
    452: "kParticleCloud",
    453: "kParticleColorMapper",
    454: "kParticleIncandecenceMapper",
    455: "kParticleTransparencyMapper",
    456: "kPartition",
    457: "kPlace2dTexture",
    458: "kPlace3dTexture",
    459: "kPluginDependNode",
    460: "kPluginLocatorNode",
    461: "kPlusMinusAverage",
    462: "kPointMatrixMult",
    463: "kPolySeparate",
    464: "kPostProcessList",
    465: "kProjection",
    466: "kRecord",
    467: "kRenderUtilityList",
    468: "kReverse",
    469: "kRgbToHsv",
    470: "kRigidSolver",
    471: "kSet",
    472: "kTextureBakeSet",
    473: "kVertexBakeSet",
    474: "kSetRange",
    475: "kShaderGlow",
    476: "kShaderList",
    477: "kShadingMap",
    478: "kSamplerInfo",
    479: "kShapeFragment",
    480: "kSimpleVolumeShader",
    481: "kSl60",
    482: "kSnapshot",
    483: "kStoryBoard",
    484: "kSummaryObject",
    485: "kSuper",
    486: "kControl",
    487: "kSurfaceLuminance",
    488: "kSurfaceShader",
    489: "kTextureList",
    490: "kTextureEnv",
    491: "kEnvBall",
    492: "kEnvCube",
    493: "kEnvChrome",
    494: "kEnvSky",
    495: "kEnvSphere",
    496: "kTexture2d",
    497: "kBulge",
    498: "kChecker",
    499: "kCloth",
    500: "kFileTexture",
    501: "kFractal",
    502: "kGrid",
    503: "kMountain",
    504: "kRamp",
    505: "kStencil",
    506: "kWater",
    507: "kTexture3d",
    508: "kBrownian",
    509: "kCloud",
    510: "kCrater",
    511: "kGranite",
    512: "kLeather",
    513: "kMarble",
    514: "kRock",
    515: "kSnow",
    516: "kSolidFractal",
    517: "kStucco",
    518: "kTxSl",
    519: "kWood",
    520: "kTime",
    521: "kTimeToUnitConversion",
    522: "kRenderSetup",
    523: "kRenderGlobals",
    524: "kRenderGlobalsList",
    525: "kRenderQuality",
    526: "kResolution",
    527: "kHardwareRenderGlobals",
    528: "kArrayMapper",
    529: "kUnitConversion",
    530: "kUnitToTimeConversion",
    531: "kUseBackground",
    532: "kUnknown",
    533: "kVectorProduct",
    534: "kVolumeShader",
    535: "kComponent",
    536: "kCurveCVComponent",
    537: "kCurveEPComponent",
    538: "kCurveKnotComponent",
    539: "kCurveParamComponent",
    540: "kIsoparmComponent",
    541: "kPivotComponent",
    542: "kSurfaceCVComponent",
    543: "kSurfaceEPComponent",
    544: "kSurfaceKnotComponent",
    545: "kEdgeComponent",
    546: "kLatticeComponent",
    547: "kSurfaceRangeComponent",
    548: "kDecayRegionCapComponent",
    549: "kDecayRegionComponent",
    550: "kMeshComponent",
    551: "kMeshEdgeComponent",
    552: "kMeshPolygonComponent",
    553: "kMeshFrEdgeComponent",
    554: "kMeshVertComponent",
    555: "kMeshFaceVertComponent",
    556: "kOrientationComponent",
    557: "kSubVertexComponent",
    558: "kMultiSubVertexComponent",
    559: "kSetGroupComponent",
    560: "kDynParticleSetComponent",
    561: "kSelectionItem",
    562: "kDagSelectionItem",
    563: "kNonDagSelectionItem",
    564: "kItemList",
    565: "kAttribute",
    566: "kNumericAttribute",
    567: "kDoubleAngleAttribute",
    568: "kFloatAngleAttribute",
    569: "kDoubleLinearAttribute",
    570: "kFloatLinearAttribute",
    571: "kTimeAttribute",
    572: "kEnumAttribute",
    573: "kUnitAttribute",
    574: "kTypedAttribute",
    575: "kCompoundAttribute",
    576: "kGenericAttribute",
    577: "kLightDataAttribute",
    578: "kMatrixAttribute",
    579: "kFloatMatrixAttribute",
    580: "kMessageAttribute",
    581: "kOpaqueAttribute",
    582: "kPlugin",
    583: "kData",
    584: "kComponentListData",
    585: "kDoubleArrayData",
    586: "kIntArrayData",
    587: "kUintArrayData",
    588: "kLatticeData",
    589: "kMatrixData",
    590: "kMeshData",
    591: "kNurbsSurfaceData",
    592: "kNurbsCurveData",
    593: "kNumericData",
    594: "kData2Double",
    595: "kData2Float",
    596: "kData2Int",
    597: "kData2Short",
    598: "kData3Double",
    599: "kData3Float",
    600: "kData3Int",
    601: "kData3Short",
    602: "kPluginData",
    603: "kPointArrayData",
    604: "kMatrixArrayData",
    605: "kSphereData",
    606: "kStringData",
    607: "kStringArrayData",
    608: "kVectorArrayData",
    609: "kSelectionList",
    610: "kTransformGeometry",
    611: "kCommEdgePtManip",
    612: "kCommEdgeOperManip",
    613: "kCommEdgeSegmentManip",
    614: "kCommCornerManip",
    615: "kCommCornerOperManip",
    616: "kPluginDeformerNode",
    617: "kTorus",
    618: "kPolyBoolOp",
    619: "kSingleShadingSwitch",
    620: "kDoubleShadingSwitch",
    621: "kTripleShadingSwitch",
    622: "kNurbsSquare",
    623: "kAnisotropy",
    624: "kNonLinear",
    625: "kDeformFunc",
    626: "kDeformBend",
    627: "kDeformTwist",
    628: "kDeformSquash",
    629: "kDeformFlare",
    630: "kDeformSine",
    631: "kDeformWave",
    632: "kDeformBendManip",
    633: "kDeformTwistManip",
    634: "kDeformSquashManip",
    635: "kDeformFlareManip",
    636: "kDeformSineManip",
    637: "kDeformWaveManip",
    638: "kSoftModManip",
    639: "kDistanceManip",
    640: "kScript",
    641: "kCurveFromMeshEdge",
    642: "kCurveCurveIntersect",
    643: "kNurbsCircular3PtArc",
    644: "kNurbsCircular2PtArc",
    645: "kOffsetSurface",
    646: "kRoundConstantRadius",
    647: "kRoundRadiusManip",
    648: "kRoundRadiusCrvManip",
    649: "kRoundConstantRadiusManip",
    650: "kThreePointArcManip",
    651: "kTwoPointArcManip",
    652: "kTextButtonManip",
    653: "kOffsetSurfaceManip",
    654: "kImageData",
    655: "kImageLoad",
    656: "kImageSave",
    657: "kImageNetSrc",
    658: "kImageNetDest",
    659: "kImageRender",
    660: "kImageAdd",
    661: "kImageDiff",
    662: "kImageMultiply",
    663: "kImageOver",
    664: "kImageUnder",
    665: "kImageColorCorrect",
    666: "kImageBlur",
    667: "kImageFilter",
    668: "kImageDepth",
    669: "kImageDisplay",
    670: "kImageView",
    671: "kImageMotionBlur",
    672: "kViewColorManager",
    673: "kMatrixFloatData",
    674: "kSkinShader",
    675: "kComponentManip",
    676: "kSelectionListData",
    677: "kObjectFilter",
    678: "kObjectMultiFilter",
    679: "kObjectNameFilter",
    680: "kObjectTypeFilter",
    681: "kObjectAttrFilter",
    682: "kObjectRenderFilter",
    683: "kObjectScriptFilter",
    684: "kSelectionListOperator",
    685: "kSubdiv",
    686: "kPolyToSubdiv",
    687: "kSkinClusterFilter",
    688: "kKeyingGroup",
    689: "kCharacter",
    690: "kCharacterOffset",
    691: "kDagPose",
    692: "kStitchAsNurbsShell",
    693: "kExplodeNurbsShell",
    694: "kNurbsBoolean",
    695: "kStitchSrfManip",
    696: "kForceUpdateManip",
    697: "kPluginManipContainer",
    698: "kPolySewEdge",
    699: "kPolyMergeVert",
    700: "kPolySmoothFacet",
    701: "kSmoothCurve",
    702: "kGlobalStitch",
    703: "kSubdivCVComponent",
    704: "kSubdivEdgeComponent",
    705: "kSubdivFaceComponent",
    706: "kUVManip2D",
    707: "kTranslateUVManip2D",
    708: "kRotateUVManip2D",
    709: "kScaleUVManip2D",
    710: "kPolyTweakUV",
    711: "kMoveUVShellManip2D",
    712: "kPluginShape",
    713: "kGeometryData",
    714: "kSingleIndexedComponent",
    715: "kDoubleIndexedComponent",
    716: "kTripleIndexedComponent",
    717: "kExtendSurfaceDistanceManip",
    718: "kSquareSrf",
    719: "kSquareSrfManip",
    720: "kSubdivToPoly",
    721: "kDynBase",
    722: "kDynEmitterManip",
    723: "kDynFieldsManip",
    724: "kDynBaseFieldManip",
    725: "kDynAirManip",
    726: "kDynNewtonManip",
    727: "kDynTurbulenceManip",
    728: "kDynSpreadManip",
    729: "kDynAttenuationManip",
    730: "kDynArrayAttrsData",
    731: "kPluginFieldNode",
    732: "kPluginEmitterNode",
    733: "kPluginSpringNode",
    734: "kDisplayLayer",
    735: "kDisplayLayerManager",
    736: "kPolyColorPerVertex",
    737: "kCreateColorSet",
    738: "kDeleteColorSet",
    739: "kCopyColorSet",
    740: "kBlendColorSet",
    741: "kPolyColorMod",
    742: "kPolyColorDel",
    743: "kCharacterMappingData",
    744: "kDynSweptGeometryData",
    745: "kWrapFilter",
    746: "kMeshVtxFaceComponent",
    747: "kBinaryData",
    748: "kAttribute2Double",
    749: "kAttribute2Float",
    750: "kAttribute2Short",
    751: "kAttribute2Int",
    752: "kAttribute3Double",
    753: "kAttribute3Float",
    754: "kAttribute3Short",
    755: "kAttribute3Int",
    756: "kReference",
    757: "kBlindData",
    758: "kBlindDataTemplate",
    759: "kPolyBlindData",
    760: "kPolyNormalPerVertex",
    761: "kNurbsToSubdiv",
    762: "kPluginIkSolver",
    763: "kInstancer",
    764: "kMoveVertexManip",
    765: "kStroke",
    766: "kBrush",
    767: "kStrokeGlobals",
    768: "kPluginGeometryData",
    769: "kLightLink",
    770: "kDynGlobals",
    771: "kPolyReduce",
    772: "kLodThresholds",
    773: "kChooser",
    774: "kLodGroup",
    775: "kMultDoubleLinear",
    776: "kFourByFourMatrix",
    777: "kTowPointOnSurfaceManip",
    778: "kSurfaceEdManip",
    779: "kSurfaceFaceComponent",
    780: "kClipScheduler",
    781: "kClipLibrary",
    782: "kSubSurface",
    783: "kSmoothTangentSrf",
    784: "kRenderPass",
    785: "kRenderPassSet",
    786: "kRenderLayer",
    787: "kRenderLayerManager",
    788: "kPassContributionMap",
    789: "kPrecompExport",
    790: "kRenderTarget",
    791: "kRenderedImageSource",
    792: "kImageSource",
    793: "kPolyFlipEdge",
    794: "kPolyExtrudeEdge",
    795: "kAnimBlend",
    796: "kAnimBlendInOut",
    797: "kPolyAppendVertex",
    798: "kUvChooser",
    799: "kSubdivCompId",
    800: "kVolumeAxis",
    801: "kDeleteUVSet",
    802: "kSubdHierBlind",
    803: "kSubdBlindData",
    804: "kCharacterMap",
    805: "kLayeredTexture",
    806: "kSubdivCollapse",
    807: "kParticleSamplerInfo",
    808: "kCopyUVSet",
    809: "kCreateUVSet",
    810: "kClip",
    811: "kPolySplitVert",
    812: "kSubdivData",
    813: "kSubdivGeom",
    814: "kUInt64ArrayData",
    815: "kInt64ArrayData",
    816: "kPolySplitEdge",
    817: "kSubdivReverseFaces",
    818: "kMeshMapComponent",
    819: "kSectionManip",
    820: "kXsectionSubdivEdit",
    821: "kSubdivToNurbs",
    822: "kEditCurve",
    823: "kEditCurveManip",
    824: "kCrossSectionManager",
    825: "kCreateSectionManip",
    826: "kCrossSectionEditManip",
    827: "kDropOffFunction",
    828: "kSubdBoolean",
    829: "kSubdModifyEdge",
    830: "kModifyEdgeCrvManip",
    831: "kModifyEdgeManip",
    832: "kScalePointManip",
    833: "kTransformBoxManip",
    834: "kSymmetryLocator",
    835: "kSymmetryMapVector",
    836: "kSymmetryMapCurve",
    837: "kCurveFromSubdivEdge",
    838: "kCreateBPManip",
    839: "kModifyEdgeBaseManip",
    840: "kSubdExtrudeFace",
    841: "kSubdivSurfaceVarGroup",
    842: "kSfRevolveManip",
    843: "kCurveFromSubdivFace",
    844: "kUnused1",
    845: "kUnused2",
    846: "kUnused3",
    847: "kUnused4",
    848: "kUnused5",
    849: "kUnused6",
    850: "kPolyTransfer",
    851: "kPolyAverageVertex",
    852: "kPolyAutoProj",
    853: "kPolyLayoutUV",
    854: "kPolyMapSewMove",
    855: "kSubdModifier",
    856: "kSubdMoveVertex",
    857: "kSubdMoveEdge",
    858: "kSubdMoveFace",
    859: "kSubdDelFace",
    860: "kSnapshotShape",
    861: "kSubdivMapComponent",
    862: "kJiggleDeformer",
    863: "kGlobalCacheControls",
    864: "kDiskCache",
    865: "kSubdCloseBorder",
    866: "kSubdMergeVert",
    867: "kBoxData",
    868: "kBox",
    869: "kRenderBox",
    870: "kSubdSplitFace",
    871: "kVolumeFog",
    872: "kSubdTweakUV",
    873: "kSubdMapCut",
    874: "kSubdLayoutUV",
    875: "kSubdMapSewMove",
    876: "kOcean",
    877: "kVolumeNoise",
    878: "kSubdAutoProj",
    879: "kSubdSubdivideFace",
    880: "kNoise",
    881: "kAttribute4Double",
    882: "kData4Double",
    883: "kSubdPlanProj",
    884: "kSubdTweak",
    885: "kSubdProjectionManip",
    886: "kSubdMappingManip",
    887: "kHardwareReflectionMap",
    888: "kPolyNormalizeUV",
    889: "kPolyFlipUV",
    890: "kHwShaderNode",
    891: "kPluginHardwareShader",
    892: "kPluginHwShaderNode",
    893: "kSubdAddTopology",
    894: "kSubdCleanTopology",
    895: "kImplicitCone",
    896: "kImplicitSphere",
    897: "kRampShader",
    898: "kVolumeLight",
    899: "kOceanShader",
    900: "kBevelPlus",
    901: "kStyleCurve",
    902: "kPolyCut",
    903: "kPolyPoke",
    904: "kPolyWedgeFace",
    905: "kPolyCutManipContainer",
    906: "kPolyCutManip",
    907: "kPolyMirrorManipContainer",
    908: "kPolyPokeManip",
    909: "kFluidTexture3D",
    910: "kFluidTexture2D",
    911: "kPolyMergeUV",
    912: "kPolyStraightenUVBorder",
    913: "kAlignManip",
    914: "kPluginTransformNode",
    915: "kFluid",
    916: "kFluidGeom",
    917: "kFluidData",
    918: "kSmear",
    919: "kStringShadingSwitch",
    920: "kStudioClearCoat",
    921: "kFluidEmitter",
    922: "kHeightField",
    923: "kGeoConnector",
    924: "kSnapshotPath",
    925: "kPluginObjectSet",
    926: "kQuadShadingSwitch",
    927: "kPolyExtrudeVertex",
    928: "kPairBlend",
    929: "kTextManip",
    930: "kViewManip",
    931: "kXformManip",
    932: "kMute",
    933: "kConstraint",
    934: "kTrimWithBoundaries",
    935: "kCurveFromMeshCoM",
    936: "kFollicle",
    937: "kHairSystem",
    938: "kRemapValue",
    939: "kRemapColor",
    940: "kRemapHsv",
    941: "kHairConstraint",
    942: "kTimeFunction",
    943: "kMentalRayTexture",
    944: "kObjectBinFilter",
    945: "kPolySmoothProxy",
    946: "kPfxGeometry",
    947: "kPfxHair",
    948: "kHairTubeShader",
    949: "kPsdFileTexture",
    950: "kKeyframeDelta",
    951: "kKeyframeDeltaMove",
    952: "kKeyframeDeltaScale",
    953: "kKeyframeDeltaAddRemove",
    954: "kKeyframeDeltaBlockAddRemove",
    955: "kKeyframeDeltaInfType",
    956: "kKeyframeDeltaTangent",
    957: "kKeyframeDeltaWeighted",
    958: "kKeyframeDeltaBreakdown",
    959: "kPolyMirror",
    960: "kPolyCreaseEdge",
    961: "kPolyPinUV",
    962: "kHikEffector",
    963: "kHikIKEffector",
    964: "kHikFKJoint",
    965: "kHikSolver",
    966: "kHikHandle",
    967: "kProxyManager",
    968: "kPolyAutoProjManip",
    969: "kPolyPrism",
    970: "kPolyPyramid",
    971: "kPolySplitRing",
    972: "kPfxToon",
    973: "kToonLineAttributes",
    974: "kPolyDuplicateEdge",
    975: "kFacade",
    976: "kMaterialFacade",
    977: "kEnvFacade",
    978: "kAISEnvFacade",
    979: "kLineModifier",
    980: "kPolyArrow",
    981: "kPolyPrimitiveMisc",
    982: "kPolyPlatonicSolid",
    983: "kPolyPipe",
    984: "kHikFloorContactMarker",
    985: "kHikGroundPlane",
    986: "kPolyComponentData",
    987: "kPolyHelix",
    988: "kCacheFile",
    989: "kHistorySwitch",
    990: "kClosestPointOnMesh",
    991: "kUVPin",
    992: "kProximityPin",
    993: "kTransferAttributes",
    994: "kDynamicConstraint",
    995: "kNComponent",
    996: "kPolyBridgeEdge",
    997: "kCacheableNode",
    998: "kNucleus",
    999: "kNBase",
    1000: "kCacheBase",
    1001: "kCacheBlend",
    1002: "kCacheTrack",
    1003: "kKeyframeRegionManip",
    1004: "kCurveNormalizerAngle",
    1005: "kCurveNormalizerLinear",
    1006: "kHyperLayoutDG",
    1007: "kPluginImagePlaneNode",
    1008: "kNCloth",
    1009: "kNParticle",
    1010: "kNRigid",
    1011: "kPluginParticleAttributeMapperNode",
    1012: "kCameraSet",
    1013: "kPluginCameraSet",
    1014: "kContainer",
    1015: "kFloatVectorArrayData",
    1016: "kNObjectData",
    1017: "kNObject",
    1018: "kPluginConstraintNode",
    1019: "kAsset",
    1020: "kPolyEdgeToCurve",
    1021: "kAnimLayer",
    1022: "kBlendNodeBase",
    1023: "kBlendNodeBoolean",
    1024: "kBlendNodeDouble",
    1025: "kBlendNodeDoubleAngle",
    1026: "kBlendNodeDoubleLinear",
    1027: "kBlendNodeEnum",
    1028: "kBlendNodeFloat",
    1029: "kBlendNodeFloatAngle",
    1030: "kBlendNodeFloatLinear",
    1031: "kBlendNodeInt16",
    1032: "kBlendNodeInt32",
    1033: "kBlendNodeAdditiveScale",
    1034: "kBlendNodeAdditiveRotation",
    1035: "kPluginManipulatorNode",
    1036: "kNIdData",
    1037: "kNId",
    1038: "kFloatArrayData",
    1039: "kMembrane",
    1040: "kMergeVertsToolManip",
    1041: "kUint64SingleIndexedComponent",
    1042: "kPolyToolFeedbackManip",
    1043: "kPolySelectEditFeedbackManip",
    1044: "kWriteToFrameBuffer",
    1045: "kWriteToColorBuffer",
    1046: "kWriteToVectorBuffer",
    1047: "kWriteToDepthBuffer",
    1048: "kWriteToLabelBuffer",
    1049: "kStereoCameraMaster",
    1050: "kSequenceManager",
    1051: "kSequencer",
    1052: "kShot",
    1053: "kBlendNodeTime",
    1054: "kCreateBezierManip",
    1055: "kBezierCurve",
    1056: "kBezierCurveData",
    1057: "kNurbsCurveToBezier",
    1058: "kBezierCurveToNurbs",
    1059: "kPolySpinEdge",
    1060: "kPolyHoleFace",
    1061: "kPointOnPolyConstraint",
    1062: "kPolyConnectComponents",
    1063: "kSkinBinding",
    1064: "kVolumeBindManip",
    1065: "kVertexWeightSet",
    1066: "kNearestPointOnCurve",
    1067: "kColorProfile",
    1068: "kAdskMaterial",
    1069: "kContainerBase",
    1070: "kDagContainer",
    1071: "kPolyUVRectangle",
    1072: "kHardwareRenderingGlobals",
    1073: "kPolyProjectCurve",
    1074: "kRenderingList",
    1075: "kPolyExtrudeManip",
    1076: "kPolyExtrudeManipContainer",
    1077: "kThreadedDevice",
    1078: "kClientDevice",
    1079: "kPluginClientDevice",
    1080: "kPluginThreadedDevice",
    1081: "kTimeWarp",
    1082: "kAssembly",
    1083: "kClipGhostShape",
    1084: "kClipToGhostData",
    1085: "kMandelbrot",
    1086: "kMandelbrot3D",
    1087: "kGreasePlane",
    1088: "kGreasePlaneRenderShape",
    1089: "kGreasePencilSequence",
    1090: "kEditMetadata",
    1091: "kCreaseSet",
    1092: "kPolyEditEdgeFlow",
    1093: "kFosterParent",
    1094: "kSnapUVManip2D",
    1095: "kToolContext",
    1096: "kNLE",
    1097: "kShrinkWrapFilter",
    1098: "kEditsManager",
    1099: "kPolyBevel2",
    1100: "kPolyCBoolOp",
    1101: "kGeomBind",
    1102: "kColorMgtGlobals",
    1103: "kPolyBevel3",
    1104: "kTimeEditorClipBase",
    1105: "kTimeEditorClipEvaluator",
    1106: "kTimeEditorClip",
    1107: "kTimeEditor",
    1108: "kTimeEditorTracks",
    1109: "kTimeEditorInterpolator",
    1110: "kTimeEditorAnimSource",
    1111: "kCaddyManipBase",
    1112: "kPolyCaddyManip",
    1113: "kPolyModifierManipContainer",
    1114: "kPolyRemesh",
    1115: "kPolyContourProj",
    1116: "kContourProjectionManip",
    1117: "kNodeGraphEditorInfo",
    1118: "kNodeGraphEditorBookmarks",
    1119: "kNodeGraphEditorBookmarkInfo",
    1120: "kPluginSkinCluster",
    1121: "kPluginGeometryFilter",
    1122: "kPluginBlendShape",
    1123: "kPolyPassThru",
    1124: "kTrackInfoManager",
    1125: "kPolyClean",
    1126: "kShapeEditorManager",
    1127: "kOceanDeformer",
    1128: "kPoseInterpolatorManager",
    1129: "kControllerTag",
    1130: "kReForm",
    1131: "kCustomEvaluatorClusterNode",
    1132: "kPolyCircularize",
    1133: "kArubaTesselate",
    1134: "kReorderUVSet",
    1135: "kUfeProxyTransform",
    1136: "kDecomposeMatrix",
    1137: "kComposeMatrix",
    1138: "kBlendMatrix",
    1139: "kPickMatrix",
    1140: "kAimMatrix",
    1141: "kPrimitiveFalloff",
    1142: "kBlendFalloff",
    1143: "kUniformFalloff",
    1144: "kTransferFalloff",
    1145: "kComponentFalloff",
    1146: "kProximityFalloff",
    1147: "kSubsetFalloff",
    1148: "kWeightFunctionData",
    1149: "kFalloffEval",
    1150: "kComponentMatch",
    1151: "kPolyUnsmooth",
    1152: "kPolyReFormManipContainer",
    1153: "kPolyReFormManip",
    1154: "kPolyAxis",
    1155: "kAngleToDoubleNode",
    1156: "kDoubleToAngleNode",
    1157: "kAbsolute",
    1158: "kACos",
    1159: "kAnd",
    1160: "kASin",
    1161: "kATan",
    1162: "kATan2",
    1163: "kAverage",
    1164: "kCeil",
    1165: "kClampRange",
    1166: "kCos",
    1167: "kDeterminant",
    1168: "kEqual",
    1169: "kFloor",
    1170: "kGreaterThan",
    1171: "kInverseLinearInterpolation",
    1172: "kLength",
    1173: "kLessThan",
    1174: "kLinearInterpolation",
    1175: "kLog",
    1176: "kMax",
    1177: "kMin",
    1178: "kModulo",
    1179: "kMultiply",
    1180: "kNegate",
    1181: "kNormalize",
    1182: "kNot",
    1183: "kOr",
    1184: "kPIConstant",
    1185: "kPower",
    1186: "kRotateVector",
    1187: "kRound",
    1188: "kSin",
    1189: "kSmoothStep",
    1190: "kSum",
    1191: "kTan",
    1192: "kTruncate",
    1193: "kDotProduct",
    1194: "kCrossProduct",
    1195: "kMultiplyPointByMatrix",
    1196: "kMultiplyVectorByMatrix",
    1197: "kAxisFromMatrix",
    1198: "kDivide",
    1199: "kSubtract",
    1200: "kTranslationFromMatrix",
    1201: "kRowFromMatrix",
    1202: "kColumnFromMatrix",
    1203: "kScaleFromMatrix",
    1204: "kRotationFromMatrix",
    1205: "kParentMatrix",
}


# Reuse world
WORLD = World()
