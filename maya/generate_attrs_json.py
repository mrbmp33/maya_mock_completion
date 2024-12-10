from maya import cmds as mc
from maya.api import OpenMaya as om

sel_ls = om.MSelectionList()

node_types = ('transform',
              'joint',
              'multDoubleLinear',
              'condition',
              'clamp',
              'remapValue',
              'remapColor',
              'uvPin'
              'plusMinusAverage',
              'blendTwoAttr',
              'blendColor',
              'decomposeMatrix',
              'inverseMatrix',
              'multMatrix',
              'blendMatrix',
              )


def get_attr_properties(nd):
    sel_ls.add(nd)
    mobject = sel_ls.getDependNode(0)
    dg = om.MFnDependencyNode(mobject)
    sel_ls.clear()

    attr_properties = {}

    for attr_name in mc.listAttr(nd):
        try:
            plug = dg.findPlug(attr_name, 0)
            attr = plug.attribute()

            attr_properties['short_name'] = plug.partialName()
            attr_properties['long_name'] = plug.partialName(useLongNames=1)
            attr_properties['is_element'] = plug.isElement
            attr_properties['is_array'] = plug.isArray
            attr_properties['is_compound'] = plug.isCompound
            attr_properties['type_str'] = attr.apiTypeStr

            if plug.isArray:
                attr_properties['num_elements'] = plug.numElements()
            elif plug.isCompound:
                attr_properties['num_children'] = plug.numChildren()

            if attr.apiType == om.MFn.kNumericAttribute:
                numeric = om.MFnNumericAttribute(attr)
                attr_properties['numeric_type'] = numeric.numericType()
                attr_properties['default_value'] = numeric.default
            elif attr.apiType == om.MFn.kEnumAttribute:
                enum = om.MFnEnumAttribute(attr)
                fields = {}
                for value in range(enum.getMax()):
                    fields[value] = enum.fieldName(value)

        except RuntimeError:
            continue

    # print(f"'{short_name}': '{long_name}',")


def create_attrs_dict():
    attributes_properties = {}
    attributes_short_names_map = {}

    for node_type in node_types:
        mc.file(newFile=1, force=1)
        node_name = mc.createNode(node_type)
        get_attr_properties(node_name)
        # attrs_dict, name_map = get_attr_properties(node_name)
        # attributes_properties[node_type] = attrs_dict


if __name__ == '__main__':
    create_attrs_dict()
