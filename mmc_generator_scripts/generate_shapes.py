"""Module for generating a dictionary of all shapes in Maya based on the type of node."""
import json
import os
from pathlib import Path
import traceback
import maya.cmds as mc
import maya.api.OpenMaya as om
import time

GLOBAL_SL = om.MSelectionList()


node_types = [
    ("polySphere", mc.polySphere),
    ("polyCube", mc.polyCube),
    ("polyCylinder", mc.polyCylinder),
    ("polyCone", mc.polyCone),
    ("polyTorus", mc.polyTorus),
    ("polyPlane", mc.polyPlane),
    ("polyPyramid", mc.polyPyramid),
    ("polyDisc", mc.polyDisc),
    "polyHelix",
    "polyPipe",
    "polyPlatonic",
    "polySuperShape",
    "polyGear",
    "mesh",
    
    "nurbsCurve",
    "nurbsSurface",
    "bezierCurve",
    ("circle", mc.circle),

    "pointLight",
    "directionalLight",
    "spotLight",
    "areaLight",
    "volumeLight",
    "ambientLight",

    "camera",

    "volumeLight",

    "lattice",
    "imagePlane",
    "locator",

    "joint",
    "cluster",
    "ikHandle",
    "wire",
    "sculpt",
    "wrap"
]

def find_builder_object(shape_mobject: om.MObject) -> om.MObject | None:
    """Find the builder object for a given shape MObject."""
    
    shape_fn = om.MFnDependencyNode(shape_mobject)
    try:
        creator_connection_plug = shape_fn.findPlug("inMesh", False)
    except RuntimeError as e:
        try:
            creator_connection_plug = shape_fn.findPlug("create", False)
        except RuntimeError as e:
            return None

    src = creator_connection_plug.source()
    if src:
        if src.node().isNull():
            return None
        elif om.MFnDependencyNode(src.node()).name() == "nullptr":
            return None
        else:
            return src.node()


def yield_children():
    for ndt in node_types:
        if isinstance(ndt, tuple):
            s, shape_name = ndt[1]()
            ndt = ndt[0]
            mobject = om.MSelectionList().add(s).getDependNode(0)
            as_fn = om.MFnDependencyNode(mobject)
            mc.select(clear=True)
        else:
            try:
                mobject = om.MFnDagNode().create(ndt)
                as_fn = om.MFnDagNode(mobject)
            except Exception:
                try:
                    mobject = om.MFnDependencyNode().create(ndt)
                except RuntimeError:
                    print(f'Failed to create {ndt}'.upper())
                    continue
        try:
            if mobject.hasFn(om.MFn.kTransform):
                dag_path = om.MDagPath.getAPathTo(mobject)
                if dag_path.numberOfShapesDirectlyBelow():
                    dag_path.extendToShape()
                    shape = dag_path.node()
                    shape_fn = om.MFnDagNode(shape)
                    builder_mobj = find_builder_object(shape)
                    builder_d = None
                    if builder_mobj:
                        buidler_fn = om.MFnDependencyNode(builder_mobj)
                        builder_d = {
                            'name': buidler_fn.name(),
                            'type': builder_mobj.apiTypeStr
                        }
                    yield ndt, shape.apiTypeStr, shape_fn.name(), as_fn.name(), builder_d
        except Exception as e:
            traceback.print_exc()
            continue


def to_data_struct():
    data = {}
    for ndt, child_type, child_name, parent_name, builder_d in yield_children():
        ndt_dict = {}
        ndt_dict['child_type'] = child_type
        ndt_dict['child_name'] = child_name
        ndt_dict['parent_name'] = parent_name
        if builder_d:
            ndt_dict['builder'] = builder_d

        data[ndt] = ndt_dict
    return data


def to_cache_file(data, out_file):
    out_txt = 'NODE_TYPES_TO_SHAPES = {\n'
    for k, v in data.items():
        out_txt += f'    "{k}": {v},\n'
    out_txt += '}\n'
    with open(out_file, "w") as f:
        f.write(out_txt)
    

if __name__ == '__main__':
    route = os.environ["GENERATE_SHAPES_OUTPUT"]
    out_file = Path(route)
    mc.file(new=True, f=True)
    to_cache_file(to_data_struct(), str(out_file))