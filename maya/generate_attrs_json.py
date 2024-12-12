import ast
import json
import pathlib
import pprint
import re

from maya import cmds as mc
from maya.api import OpenMaya as om

sel_ls = om.MSelectionList()
node_types = ('transform', 'joint', 'multDoubleLinear', 'condition', 'clamp', 'remapValue', 'remapColor', 'uvPin',
              'plusMinusAverage', 'blendTwoAttr', 'blendColors', 'decomposeMatrix', 'inverseMatrix', 'multMatrix',
              'blendMatrix',)


def get_attr_properties(nd):
    sel_ls.add(nd)
    mobject = sel_ls.getDependNode(0)
    dg = om.MFnDependencyNode(mobject)
    sel_ls.clear()

    all_attr_properties = {}
    all_short_name_to_long_name = {}

    for attr_name in mc.listAttr(nd):
        try:
            plug = dg.findPlug(attr_name, 0)
            attr = plug.attribute()

            attr_properties = {'short_name': plug.partialName(),
                               'long_name': plug.partialName(useLongNames=1),
                               'is_element': plug.isElement,
                               'is_array': plug.isArray,
                               'is_compound': plug.isCompound,
                               'type_str': attr.apiTypeStr}

            all_short_name_to_long_name[attr_properties['short_name']] = attr_properties['long_name']

            if plug.isArray:
                attr_properties['num_elements'] = plug.numElements()
            elif plug.isCompound:
                attr_properties['num_children'] = plug.numChildren()
                attr_properties['children'] = []
                for index in range(plug.numChildren()):
                    attr_properties['children'].append(plug.child(index).partialName(useLongNames=1))

            if attr.apiType == om.MFn.kNumericAttribute:
                numeric = om.MFnNumericAttribute(attr)
                attr_properties['numeric_type'] = numeric.numericType()
                attr_properties['default_value'] = numeric.default
            elif attr.apiType == om.MFn.kEnumAttribute:
                enum = om.MFnEnumAttribute(attr)
                fields = {}
                for value in range(enum.getMax()):
                    fields[value] = enum.fieldName(value)

            all_attr_properties[attr_properties['long_name']] = attr_properties
        except RuntimeError:
            continue

    return all_attr_properties, all_short_name_to_long_name


def convert_booleans_to_python_style(json_str):
    # Debug print to ensure JSON booleans are being captured
    print("Before regex replacement: ", json_str[:200])  # Print the first 200 chars to inspect
    json_str = re.sub(r'\btrue\b', 'True', json_str)
    json_str = re.sub(r'\bfalse\b', 'False', json_str)
    print("After regex replacement: ", json_str[:200])  # Print the first 200 chars after replacing booleans
    return json_str


def create_attrs_dict(output_file):
    attributes_properties = {}
    attributes_short_names_map = {}

    for node_type in node_types:
        mc.file(newFile=1, force=1)
        node_name = mc.createNode(node_type)
        attrs_dict, short_name_to_long_name = get_attr_properties(node_name)
        attributes_properties[node_type] = attrs_dict
        attributes_short_names_map.update(short_name_to_long_name)

    # Prepare the data to be written
    data = {
        "ATTRIBUTES_PROPERTIES": attributes_properties,
        "ATTRIBUTES_SHORT_NAMES_MAP": attributes_short_names_map
    }

    # Write to Python file
    with open(output_file, "w") as f:
        f.write("# Auto-generated Maya attributes file\n\n")

        for name, content in data.items():
            f.write(f"{name} = ")
            # Convert to JSON string with pretty formatting
            json_str = json.dumps(content, indent=4)
            print("Serialized JSON string: ", json_str[:200])  # Print part of the serialized JSON
            # Replace booleans with Python-style booleans
            formatted_str = convert_booleans_to_python_style(json_str)
            print("Formatted string to write: ", formatted_str[:200])  # Print part of the formatted string
            f.write(formatted_str + "\n\n")


if __name__ == '__main__':
    out_file = ''
    create_attrs_dict(out_file)
