"""Module for generating a dictionary of all shapes in Maya based on the type of node."""
import json
from pathlib import Path
import traceback
import maya.cmds as mc
import maya.api.OpenMaya as om
import time

GLOBAL_SL = om.MSelectionList()


node_types = [
    "polySphere",
    "polyCube",
    "polyCylinder",
    "polyCone",
    "polyTorus",
    "polyPlane",
    "polyPyramid",
    "polyDisc",
    "polyHelix",
    "polyPipe",
    "polyPlatonic",
    "polySuperShape",
    "polyGear",
    "mesh",
    
    "nurbsCurve",
    "nurbsSurface",
    "bezierCurve",

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


def yield_children():
    for ndt in node_types:
        # print(ndt)
        try:
            mobject = om.MFnDagNode().create(ndt)
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
                    yield ndt, shape.apiTypeStr, om.MFnDependencyNode(mobject).name()
        except Exception as e:
            traceback.print_exc()
            continue


def to_data_struct():
    data = {}
    for ndt, child_type, child_name in yield_children():
        data[ndt] = (child_type, child_name)
    return data


def to_cache_file(data, out_file):
    out_txt = 'NODE_TYPES_TO_SHAPES = {\n'
    for k, v in data.items():
        out_txt += f'    "{k}": {v},\n'
    out_txt += '}\n'
    with open(out_file, "w") as f:
        f.write(out_txt)
    

if __name__ == '__main__':
    route = r''
    out_file = Path()
    out_file.parent.mkdir(parents=True, exist_ok=True)
    mc.file(new=True, f=True)
    # to_data_struct()
    to_cache_file(to_data_struct(), str(out_file))