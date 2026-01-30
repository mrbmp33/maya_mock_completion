from maya.api import OpenMaya as om
from maya import cmds as mc
import cmdx

def generate_type_str_to_id_map() -> dict[str, int]:
    TYPE_STR_TO_ID = {}
    for node_type in mc.allNodeTypes(includeAbstract=False):
        try:
            nd = cmdx.Node(om.MFnDependencyNode().create(node_type))
            if isinstance(nd, cmdx.DagNode):
                nd = nd.shape() or nd
            TYPE_STR_TO_ID[nd.object().apiTypeStr] = om.MNodeClass(node_type).typeId.id()
        except RuntimeError:
            mc.file(new=True, force=True)
            continue
    return TYPE_STR_TO_ID


def print_type_str_to_id_map():
    print("_TYPE_STR_TO_ID = {")
    type_str_to_id_map = generate_type_str_to_id_map()
    for type_str, type_id in type_str_to_id_map.items():
        print(f'  "{type_str}": MTypeId({type_id}),')
    print("}")


def print_int_to_str_map():
    print("_TYPE_INT_TO_STR = {")
    type_str_to_id_map = generate_type_str_to_id_map()
    for type_str, type_id in type_str_to_id_map.items():
        print(f'  {type_id}: "{type_str}",')
    print("}")


if __name__ == "__main__":
    # mc.file(new=True, force=True)
    print_type_str_to_id_map()
    # print_int_to_str_map()
    # mc.file(new=True, force=True)
