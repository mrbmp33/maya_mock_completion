import os
import pathlib
from maya.api import OpenMaya as om
from maya import cmds as mc
import cmdx


def generate_type_str_to_id_map() -> tuple[dict[str, int], dict[str, om.MTypeId]]:
    TYPE_STR_TO_ID = {}
    to_cached_types = {}
    blacklist = (
        # Causes crash (Maya 2018)
        "caddyManipBase",
        # Causes TypeError
        "applyAbsOverride",
        "applyOverride",
        "applyRelOverride",
        "childNode",
        "lightItemBase",
        "listItem",
        "override",
        "selector",
        "valueOverride",
    )

    def generate_key(node_type: str) -> str:
        try:
            mobj = dg.create(node_type)
            # print(mobj.apiType())
            fn = om.MFnDependencyNode
            try:
                # If `name` is a shape, then the transform
                # is returned. We need the shape.
                mobj = om.MFnDagNode(mobj).child(0)
            except RuntimeError:
                pass

            TYPE_STR_TO_ID.setdefault(mobj.apiTypeStr, fn(mobj).typeId)
            key = node_type[1:] if node_type.startswith("k") else node_type
            to_cached_types[key[0].upper() + key[1:]] = fn(mobj).typeId
            try:
                nd = mc.createNode(f"{node_type}DL")
                if not nd.startswith("unknown"):
                    node = cmdx.encode(nd)
                    mobj: om.MObject = node.object()
                    key = node_type[1:] if node_type.startswith("k") else node_type
                    to_cached_types[key[0].upper() + key[1:]] = fn(mobj).typeId
            except RuntimeError:
                pass
        except (RuntimeError, TypeError):
            mc.file(new=True, force=True)

    dg = om.MFnDependencyNode()
    for node_type in mc.allNodeTypes(includeAbstract=False):
        
        if node_type in blacklist:
            continue

        generate_key(node_type)

    return TYPE_STR_TO_ID, to_cached_types


def print_type_str_to_id_map():
    print("_TYPE_STR_TO_ID = {")
    type_str_to_id_map = generate_type_str_to_id_map()
    for type_str, type_id in type_str_to_id_map.items():
        print(f'  "{type_str}": {type_id},')
    print("}")


def print_int_to_str_map():
    print("_TYPE_INT_TO_STR = {")
    type_str_to_id_map = generate_type_str_to_id_map()
    for type_str, type_id in type_str_to_id_map.items():
        print(f'  {type_id}: "{type_str}",')
    print("}")


def map_fn_id_to_key():
    return sorted(
        {v: k for k, v in om.MFn.__dict__.items() if isinstance(v, int)}.items()
    )


def to_file(file_path: str):
    with open(file_path, "w") as f:
        f.write("_API_TYPES_INT_TO_FN_TYPE_STR = {\n")
        for type_id, fn_type_str in map_fn_id_to_key():
            f.write(f'  {type_id}: "{fn_type_str}",\n')
        f.write("}\n\n")

        f.write("_TYPE_STR_TO_ID = {\n")
        type_str_to_id_map, to_cached_types = generate_type_str_to_id_map()
        for type_str, type_id in type_str_to_id_map.items():
            f.write(f'  "{type_str}": {type_id},\n')
        f.write("}\n\n")

        f.write("_TYPE_INT_TO_STR = {\n")
        for type_str, type_id in type_str_to_id_map.items():
            f.write(f'  {type_id}: "{type_str}",\n')
        f.write("}\n")

    cached_mtypeids_file = pathlib.Path(file_path).with_name(f"mtypeids_cache.py")
    content = '''
import enum
from typing import Literal
from maya.api import OpenMaya as om


class NodeTypes(om.MTypeId, enum.Enum):
    """Object that allows for Enum-like syntax for Maya node types.

    It implements hashability for using specific node types as dictionary keys or literal values.
    """

    def __hash__(self):
        """Return the hash value of the node type. By default they are not hashable but they *are*
        unique due to their ID nature.
        """
        value: om.MTypeId = self.value
        return hash(value.id())

    def id(self) -> int:
        """Return the ID of the type."""
        value: om.MTypeId = self.value
        return value.id()

'''
    with open(str(cached_mtypeids_file), "w") as f:
        f.write(content)

        for key, type_id in to_cached_types.items():
            f.write(f'    {key} = om.MTypeId({hex(type_id.id())})\n')


if __name__ == "__main__":
    print("Generating type maps...")
    to_file(os.getenv("NODE_TYPE_IDS_OUTPUT"))
