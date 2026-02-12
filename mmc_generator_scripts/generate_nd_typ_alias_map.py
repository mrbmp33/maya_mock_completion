import maya.cmds as mc
import cmdx
from maya.api import OpenMaya as om

# Fn constant num to Fn k string map
api_type_to_typ_str = {num: key for key, num in om.MFn.__dict__.items() if key.startswith("k")}
type_alias_to_api_constant = {}

for node_type in mc.allNodeTypes(includeAbstract=False):
    try:
        nd = cmdx.Node(om.MFnDependencyNode().create(node_type))
        if isinstance(nd, cmdx.DagNode):
            nd = nd.shape() or nd
        api_type = mc.nodeType(nd.name(), api=True)
        # print(f'"{node_type}": {api_type},')
    except RuntimeError:
        # mc.file(new=True, force=True)
        continue

    type_alias_to_api_constant[node_type] = api_type

import pathlib
import os
output_path = os.getenv("NODE_TYPE_ALIAS_MAP_OUTPUT")
output_file = pathlib.Path(output_path)

direct_map = {k: v for k, v in type_alias_to_api_constant.items()}
reversed_map = {v: k for k, v in type_alias_to_api_constant.items()}
reversed_map['kTransform'] = "transform"  # only transform node has a different api type and node type name, so we need to add it manually

with open(output_file, "w") as f:
    f.write("NODE_TYPES_ALIAS_MAP = {\n")
    for alias, api_constant_key in sorted(direct_map.items()):
        f.write(f'  "{alias}": "{api_constant_key}",\n')

    f.write("}\n\n")
    f.write("REVERSE_NODE_TYPES_ALIAS_MAP = {\n")
    for api_constant_key, alias in sorted(reversed_map.items()):
        f.write(f' "{api_constant_key}": "{alias}",\n')
    f.write("}\n\n")
