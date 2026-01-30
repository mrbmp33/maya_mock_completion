import ast
import json
import logging
import os
import pathlib
import pprint
import re
from typing import Optional

from maya import cmds as mc
import cmdx
from maya.api import OpenMaya as om

sel_ls = om.MSelectionList()
node_types = [
    "areaLight",
    "blendColors",
    "blendMatrix",
    "blendTwoAttr",
    "camera",
    "clamp",
    "condition",
    "decomposeMatrix",
    "equal",
    "file",
    "inverseMatrix",
    "joint",
    "lambert",
    "mesh",
    "multDoubleLinear",
    "multMatrix",
    "nurbsCurve",
    "nurbsSurface",
    "parentMatrix",
    "pickMatrix",
    "plusMinusAverage",
    "pointOnCurveInfo",
    "pointOnSurfaceInfo",
    "pointLight",
    "polyCube",
    "ramp",
    "remapColor",
    "remapValue",
    "spotLight",
    "transform",
    "uvPin",
]


def get_attr_properties(nd):
    as_node = cmdx.encode(nd)
    mobject = as_node.object()

    all_attr_properties = {}
    all_short_name_to_long_name = {}

    for attr_name in sorted(mc.listAttr(nd)):
        try:
            plug = as_node[attr_name]
            attr: om.MObject = plug.attribute()
            short_name = plug.name(long=False)
            long_name = plug.name(long=True)
            attr_properties = {
                "short_name": short_name,
                "long_name": long_name,
                "is_element": plug.isElement,
                "is_array": plug.isArray,
                "is_compound": plug.isCompound,
                "type_str": attr.apiTypeStr,
            }

            # Add the short name to long name mapping
            name_key_d = all_short_name_to_long_name.get(short_name, {}).get(
                as_node.typeName, {}
            )
            name_key_d[as_node.object().apiTypeStr] = long_name
            all_short_name_to_long_name[short_name] = name_key_d

            # See if it has a parent plug. Better ask forgiveness than permission
            try:
                parent_plug: cmdx.Plug = plug.parent()
                attr_properties["parent_plug"] = parent_plug.name(long=True)
            except TypeError:
                ...

            if plug.isArray:
                try:
                    attr_properties["num_elements"] = mc.getAttr(
                        f"{plug.plug().partialName(includeNodeName=True, useLongNames=True)}".replace(
                            "[-1]", "[0]"
                        ),
                        multiIndices=True,
                    ) or 0
                except ValueError:
                    continue

            elif plug.isCompound:
                attr_properties["num_children"] = plug.plug().numChildren()
                attr_properties["children"] = []
                for child_plug in plug:
                    attr_properties["children"].append(child_plug.name(long=True))

            if attr.apiType() in (
                om.MFn.kDoubleLinearAttribute,
                om.MFn.kFloatLinearAttribute,
                om.MFn.kDoubleAngleAttribute,
                om.MFn.kFloatAngleAttribute,
            ):
                unit = om.MFnUnitAttribute(attr)
                attr_properties["unit_type"] = unit.unitType()
                attr_properties["default_value"] = unit.default.value

            if attr.apiType() == om.MFn.kNumericAttribute:
                numeric = om.MFnNumericAttribute(attr)
                attr_properties["numeric_type"] = numeric.numericType()
                attr_properties["default_value"] = numeric.default
                if numeric.hasMin():
                    attr_properties["min_value"] = numeric.getMin()
                if numeric.hasMax():
                    attr_properties["max_value"] = numeric.getMax()

            elif attr.apiType() == om.MFn.kEnumAttribute:
                enum = om.MFnEnumAttribute(attr)
                fields = {}
                for value in range(enum.getMax()):
                    fields[value] = enum.fieldName(value)
                attr_properties["enum_fields"] = fields
                attr_properties["default_value"] = enum.default

            elif attr.apiType() == om.MFn.kTypedAttribute:
                typed = om.MFnTypedAttribute(attr)
                attr_properties["typed_type"] = typed.attrType()

            all_attr_properties[attr_properties["long_name"]] = attr_properties

        except RuntimeError as err:
            logging.debug(f"Could not complete attribute {attr_name}. {err}")

    return all_attr_properties, all_short_name_to_long_name


def convert_booleans_to_python_style(json_str):
    # Debug print to ensure JSON booleans are being captured
    # print("Before regex replacement: ", json_str[:200])  # Print the first 200 chars to inspect
    json_str = re.sub(r"\btrue\b", "True", json_str)
    json_str = re.sub(r"\bfalse\b", "False", json_str)
    # print("After regex replacement: ", json_str[:200])  # Print the first 200 chars after replacing booleans
    return json_str


def create_attrs_dict(
    output_properties_file, output_literals_file: Optional[str] = None
):
    attributes_properties = {}
    attributes_short_names_map = {}

    for node_type in node_types:
        mc.file(newFile=1, force=1)
        node_name = mc.createNode(node_type)
        api_type = mc.nodeType(node_name, api=True)
        print(f"Processing node type: {node_type}, node name: {node_name}")

        if isinstance(node_name, (tuple, list)):
            node_name, *_ = node_name
            mc.select(clear=True)

        attrs_dict, short_name_to_long_name = get_attr_properties(node_name)

        attributes_properties[api_type] = attrs_dict
        for key, nested_dict in short_name_to_long_name.items():
            short_name_dict = attributes_short_names_map.setdefault(key, nested_dict)
            short_name_dict.update(nested_dict)

    # Prepare the data to be written
    data = {
        "ATTRIBUTES_PROPERTIES": attributes_properties,
        "ATTRIBUTES_SHORT_NAMES_MAP": attributes_short_names_map,
    }

    # Write to Python file
    with open(output_properties_file, "w") as f:
        f.write("# Auto-generated Maya attributes file\n\n")

        for name, content in data.items():
            f.write(f"{name} = ")

            # Convert to JSON string with pretty formatting
            json_str = json.dumps(content, indent=4)

            # Replace booleans with Python-style booleans
            formatted_str = convert_booleans_to_python_style(json_str)
            f.write(formatted_str + "\n\n")

    # If passed a file create separate literals file with possible attribute keys
    if not output_literals_file:
        return

    with open(output_literals_file, "w") as f1:
        f1.write("# Auto-generated Maya attribute literals file\n\n")
        f1.write("from typing import Literal, TypeAlias\n\n")
        f1.write("ATTRIBUTE_KEYS: TypeAlias = Literal[\n")

        dicts_keys = []
        for nd in attributes_properties.values():
            dicts_keys.extend([x for x in nd.keys()])

        dicts_keys.extend(attributes_short_names_map.keys())

        for k in set(dicts_keys):
            f1.write(f'    "{k}",\n')

        f1.write("]")
        f1.write("\n\n")


if __name__ == "__main__":
    properties_file = os.getenv("GENERATE_ATTRIBUTES_PROPERTIES_OUTPUT")
    literals_file = os.getenv("GENERATE_ATTRIBUTES_LITERALS_OUTPUT")

    create_attrs_dict(
        properties_file,
        literals_file
    )
