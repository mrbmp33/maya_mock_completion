# Auto-generated Maya attributes file

from typing import Literal, TypeAlias

ATTRIBUTES_PROPERTIES = {
    "transform": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "isCollapsed": {
            "short_name": "isc",
            "long_name": "isCollapsed",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "blackBox": {
            "short_name": "bbx",
            "long_name": "blackBox",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "borderConnections": {
            "short_name": "boc",
            "long_name": "borderConnections",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
        },
        "isHierarchicalConnection": {
            "short_name": "ish",
            "long_name": "isHierarchicalConnection",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 1,
            "default_value": False
        },
        "publishedNodeInfo": {
            "short_name": "pni",
            "long_name": "publishedNodeInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "rmbCommand": {
            "short_name": "rmc",
            "long_name": "rmbCommand",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "templateVersion": {
            "short_name": "tpv",
            "long_name": "templateVersion",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "boundingBox": {
            "short_name": "bb",
            "long_name": "boundingBox",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "boundingBoxMin",
                "boundingBoxMax",
                "boundingBoxSize"
            ]
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxMinX",
                "boundingBoxMinY",
                "boundingBoxMinZ"
            ]
        },
        "boundingBoxMinX": {
            "short_name": "bbnx",
            "long_name": "boundingBoxMinX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxMaxX",
                "boundingBoxMaxY",
                "boundingBoxMaxZ"
            ]
        },
        "boundingBoxMaxX": {
            "short_name": "bbxx",
            "long_name": "boundingBoxMaxX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxSizeX",
                "boundingBoxSizeY",
                "boundingBoxSizeZ"
            ]
        },
        "boundingBoxSizeX": {
            "short_name": "bbsx",
            "long_name": "boundingBoxSizeX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "center": {
            "short_name": "c",
            "long_name": "center",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxCenterX",
                "boundingBoxCenterY",
                "boundingBoxCenterZ"
            ]
        },
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "visibility": {
            "short_name": "v",
            "long_name": "visibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "intermediateObject": {
            "short_name": "io",
            "long_name": "intermediateObject",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "template": {
            "short_name": "tmp",
            "long_name": "template",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "instObjGroups": {
            "short_name": "iog",
            "long_name": "instObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "objectColorRGB": {
            "short_name": "obcc",
            "long_name": "objectColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "objectColorR",
                "objectColorG",
                "objectColorB"
            ]
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorG": {
            "short_name": "obcg",
            "long_name": "objectColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorRGB": {
            "short_name": "wfcc",
            "long_name": "wireColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "wireColorR",
                "wireColorG",
                "wireColorB"
            ]
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorG": {
            "short_name": "wfcg",
            "long_name": "wireColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "useObjectColor": {
            "short_name": "uoc",
            "long_name": "useObjectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "objectColor": {
            "short_name": "oc",
            "long_name": "objectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "drawOverride": {
            "short_name": "do",
            "long_name": "drawOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 12,
            "children": [
                "overrideDisplayType",
                "overrideLevelOfDetail",
                "overrideShading",
                "overrideTexturing",
                "overridePlayback",
                "overrideEnabled",
                "overrideVisibility",
                "hideOnPlayback",
                "overrideRGBColors",
                "overrideColor",
                "overrideColorRGB",
                "overrideColorA"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideTexturing": {
            "short_name": "ovt",
            "long_name": "overrideTexturing",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorG": {
            "short_name": "ovcg",
            "long_name": "overrideColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "lodVisibility": {
            "short_name": "lodv",
            "long_name": "lodVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "selectionChildHighlighting": {
            "short_name": "sech",
            "long_name": "selectionChildHighlighting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "renderInfo": {
            "short_name": "ri",
            "long_name": "renderInfo",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "identification",
                "layerRenderable",
                "layerOverrideColor"
            ]
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "ghosting": {
            "short_name": "gh",
            "long_name": "ghosting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "ghostingMode": {
            "short_name": "gm",
            "long_name": "ghostingMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "ghostCustomSteps": {
            "short_name": "gcs",
            "long_name": "ghostCustomSteps",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "ghostPreFrames",
                "ghostPostFrames",
                "ghostsStep"
            ]
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "ghostOpacityRange": {
            "short_name": "golr",
            "long_name": "ghostOpacityRange",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Float",
            "num_children": 2,
            "children": [
                "ghostFarOpacity",
                "ghostNearOpacity"
            ]
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "ghostColorPre": {
            "short_name": "gcp",
            "long_name": "ghostColorPre",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "ghostColorPreR",
                "ghostColorPreG",
                "ghostColorPreB"
            ]
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPost": {
            "short_name": "gac",
            "long_name": "ghostColorPost",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "ghostColorPostR",
                "ghostColorPostG",
                "ghostColorPostB"
            ]
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.878000020980835
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostUseDriver": {
            "short_name": "gud",
            "long_name": "ghostUseDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "hiddenInOutliner": {
            "short_name": "hio",
            "long_name": "hiddenInOutliner",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useOutlinerColor": {
            "short_name": "uocol",
            "long_name": "useOutlinerColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "outlinerColor": {
            "short_name": "oclr",
            "long_name": "outlinerColor",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outlinerColorR",
                "outlinerColorG",
                "outlinerColorB"
            ]
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorG": {
            "short_name": "oclrg",
            "long_name": "outlinerColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "translate": {
            "short_name": "t",
            "long_name": "translate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "translateX",
                "translateY",
                "translateZ"
            ]
        },
        "translateX": {
            "short_name": "tx",
            "long_name": "translateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "translateY": {
            "short_name": "ty",
            "long_name": "translateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "translateZ": {
            "short_name": "tz",
            "long_name": "translateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotate": {
            "short_name": "r",
            "long_name": "rotate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotateX",
                "rotateY",
                "rotateZ"
            ]
        },
        "rotateX": {
            "short_name": "rx",
            "long_name": "rotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateY": {
            "short_name": "ry",
            "long_name": "rotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateZ": {
            "short_name": "rz",
            "long_name": "rotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateOrder": {
            "short_name": "ro",
            "long_name": "rotateOrder",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "scale": {
            "short_name": "s",
            "long_name": "scale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "scaleX",
                "scaleY",
                "scaleZ"
            ]
        },
        "scaleX": {
            "short_name": "sx",
            "long_name": "scaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "scaleY": {
            "short_name": "sy",
            "long_name": "scaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "scaleZ": {
            "short_name": "sz",
            "long_name": "scaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "shear": {
            "short_name": "sh",
            "long_name": "shear",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "shearXY",
                "shearXZ",
                "shearYZ"
            ]
        },
        "shearXY": {
            "short_name": "shxy",
            "long_name": "shearXY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "shearXZ": {
            "short_name": "shxz",
            "long_name": "shearXZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "shearYZ": {
            "short_name": "shyz",
            "long_name": "shearYZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotatePivot": {
            "short_name": "rp",
            "long_name": "rotatePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotatePivotX",
                "rotatePivotY",
                "rotatePivotZ"
            ]
        },
        "rotatePivotX": {
            "short_name": "rpx",
            "long_name": "rotatePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotY": {
            "short_name": "rpy",
            "long_name": "rotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotZ": {
            "short_name": "rpz",
            "long_name": "rotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotTranslate": {
            "short_name": "rpt",
            "long_name": "rotatePivotTranslate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotatePivotTranslateX",
                "rotatePivotTranslateY",
                "rotatePivotTranslateZ"
            ]
        },
        "rotatePivotTranslateX": {
            "short_name": "rptx",
            "long_name": "rotatePivotTranslateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotTranslateY": {
            "short_name": "rpty",
            "long_name": "rotatePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotTranslateZ": {
            "short_name": "rptz",
            "long_name": "rotatePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivot": {
            "short_name": "sp",
            "long_name": "scalePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "scalePivotX",
                "scalePivotY",
                "scalePivotZ"
            ]
        },
        "scalePivotX": {
            "short_name": "spx",
            "long_name": "scalePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotY": {
            "short_name": "spy",
            "long_name": "scalePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotZ": {
            "short_name": "spz",
            "long_name": "scalePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotTranslate": {
            "short_name": "spt",
            "long_name": "scalePivotTranslate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "scalePivotTranslateX",
                "scalePivotTranslateY",
                "scalePivotTranslateZ"
            ]
        },
        "scalePivotTranslateX": {
            "short_name": "sptx",
            "long_name": "scalePivotTranslateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotTranslateY": {
            "short_name": "spty",
            "long_name": "scalePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotTranslateZ": {
            "short_name": "sptz",
            "long_name": "scalePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotateAxis": {
            "short_name": "ra",
            "long_name": "rotateAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotateAxisX",
                "rotateAxisY",
                "rotateAxisZ"
            ]
        },
        "rotateAxisX": {
            "short_name": "rax",
            "long_name": "rotateAxisX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateAxisY": {
            "short_name": "ray",
            "long_name": "rotateAxisY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateAxisZ": {
            "short_name": "raz",
            "long_name": "rotateAxisZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "transMinusRotatePivot": {
            "short_name": "tmrp",
            "long_name": "transMinusRotatePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "transMinusRotatePivotX",
                "transMinusRotatePivotY",
                "transMinusRotatePivotZ"
            ]
        },
        "transMinusRotatePivotX": {
            "short_name": "tmrx",
            "long_name": "transMinusRotatePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "transMinusRotatePivotY": {
            "short_name": "tmry",
            "long_name": "transMinusRotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "transMinusRotatePivotZ": {
            "short_name": "tmrz",
            "long_name": "transMinusRotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransLimit": {
            "short_name": "mntl",
            "long_name": "minTransLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minTransXLimit",
                "minTransYLimit",
                "minTransZLimit"
            ]
        },
        "minTransXLimit": {
            "short_name": "mtxl",
            "long_name": "minTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransYLimit": {
            "short_name": "mtyl",
            "long_name": "minTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransZLimit": {
            "short_name": "mtzl",
            "long_name": "minTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "maxTransLimit": {
            "short_name": "mxtl",
            "long_name": "maxTransLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxTransXLimit",
                "maxTransYLimit",
                "maxTransZLimit"
            ]
        },
        "maxTransXLimit": {
            "short_name": "xtxl",
            "long_name": "maxTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "maxTransYLimit": {
            "short_name": "xtyl",
            "long_name": "maxTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "maxTransZLimit": {
            "short_name": "xtzl",
            "long_name": "maxTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransLimitEnable": {
            "short_name": "mtle",
            "long_name": "minTransLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "minTransXLimitEnable",
                "minTransYLimitEnable",
                "minTransZLimitEnable"
            ]
        },
        "minTransXLimitEnable": {
            "short_name": "mtxe",
            "long_name": "minTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransYLimitEnable": {
            "short_name": "mtye",
            "long_name": "minTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransZLimitEnable": {
            "short_name": "mtze",
            "long_name": "minTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransLimitEnable": {
            "short_name": "xtle",
            "long_name": "maxTransLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "maxTransXLimitEnable",
                "maxTransYLimitEnable",
                "maxTransZLimitEnable"
            ]
        },
        "maxTransXLimitEnable": {
            "short_name": "xtxe",
            "long_name": "maxTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransYLimitEnable": {
            "short_name": "xtye",
            "long_name": "maxTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransZLimitEnable": {
            "short_name": "xtze",
            "long_name": "maxTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotLimit": {
            "short_name": "mnrl",
            "long_name": "minRotLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minRotXLimit",
                "minRotYLimit",
                "minRotZLimit"
            ]
        },
        "minRotXLimit": {
            "short_name": "mrxl",
            "long_name": "minRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotYLimit": {
            "short_name": "mryl",
            "long_name": "minRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotZLimit": {
            "short_name": "mrzl",
            "long_name": "minRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotLimit": {
            "short_name": "mxrl",
            "long_name": "maxRotLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxRotXLimit",
                "maxRotYLimit",
                "maxRotZLimit"
            ]
        },
        "maxRotXLimit": {
            "short_name": "xrxl",
            "long_name": "maxRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotYLimit": {
            "short_name": "xryl",
            "long_name": "maxRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotZLimit": {
            "short_name": "xrzl",
            "long_name": "maxRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotLimitEnable": {
            "short_name": "mrle",
            "long_name": "minRotLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "minRotXLimitEnable",
                "minRotYLimitEnable",
                "minRotZLimitEnable"
            ]
        },
        "minRotXLimitEnable": {
            "short_name": "mrxe",
            "long_name": "minRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotYLimitEnable": {
            "short_name": "mrye",
            "long_name": "minRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotZLimitEnable": {
            "short_name": "mrze",
            "long_name": "minRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotLimitEnable": {
            "short_name": "xrle",
            "long_name": "maxRotLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "maxRotXLimitEnable",
                "maxRotYLimitEnable",
                "maxRotZLimitEnable"
            ]
        },
        "maxRotXLimitEnable": {
            "short_name": "xrxe",
            "long_name": "maxRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotYLimitEnable": {
            "short_name": "xrye",
            "long_name": "maxRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotZLimitEnable": {
            "short_name": "xrze",
            "long_name": "maxRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleLimit": {
            "short_name": "mnsl",
            "long_name": "minScaleLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minScaleXLimit",
                "minScaleYLimit",
                "minScaleZLimit"
            ]
        },
        "minScaleXLimit": {
            "short_name": "msxl",
            "long_name": "minScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleYLimit": {
            "short_name": "msyl",
            "long_name": "minScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleZLimit": {
            "short_name": "mszl",
            "long_name": "minScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "maxScaleLimit": {
            "short_name": "mxsl",
            "long_name": "maxScaleLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxScaleXLimit",
                "maxScaleYLimit",
                "maxScaleZLimit"
            ]
        },
        "maxScaleXLimit": {
            "short_name": "xsxl",
            "long_name": "maxScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleYLimit": {
            "short_name": "xsyl",
            "long_name": "maxScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleZLimit": {
            "short_name": "xszl",
            "long_name": "maxScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "minScaleLimitEnable": {
            "short_name": "msle",
            "long_name": "minScaleLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "minScaleXLimitEnable",
                "minScaleYLimitEnable",
                "minScaleZLimitEnable"
            ]
        },
        "minScaleXLimitEnable": {
            "short_name": "msxe",
            "long_name": "minScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleYLimitEnable": {
            "short_name": "msye",
            "long_name": "minScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleZLimitEnable": {
            "short_name": "msze",
            "long_name": "minScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleLimitEnable": {
            "short_name": "xsle",
            "long_name": "maxScaleLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "maxScaleXLimitEnable",
                "maxScaleYLimitEnable",
                "maxScaleZLimitEnable"
            ]
        },
        "maxScaleXLimitEnable": {
            "short_name": "xsxe",
            "long_name": "maxScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleYLimitEnable": {
            "short_name": "xsye",
            "long_name": "maxScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleZLimitEnable": {
            "short_name": "xsze",
            "long_name": "maxScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "offsetParentMatrix": {
            "short_name": "opm",
            "long_name": "offsetParentMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "dagLocalMatrix": {
            "short_name": "dlm",
            "long_name": "dagLocalMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "dagLocalInverseMatrix": {
            "short_name": "dlim",
            "long_name": "dagLocalInverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "geometry": {
            "short_name": "g",
            "long_name": "geometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kGenericAttribute"
        },
        "xformMatrix": {
            "short_name": "xm",
            "long_name": "xformMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "selectHandle": {
            "short_name": "hdl",
            "long_name": "selectHandle",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "selectHandleX",
                "selectHandleY",
                "selectHandleZ"
            ]
        },
        "selectHandleX": {
            "short_name": "hdlx",
            "long_name": "selectHandleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "selectHandleY": {
            "short_name": "hdly",
            "long_name": "selectHandleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "selectHandleZ": {
            "short_name": "hdlz",
            "long_name": "selectHandleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "inheritsTransform": {
            "short_name": "it",
            "long_name": "inheritsTransform",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "displayHandle": {
            "short_name": "dh",
            "long_name": "displayHandle",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayScalePivot": {
            "short_name": "dsp",
            "long_name": "displayScalePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayRotatePivot": {
            "short_name": "drp",
            "long_name": "displayRotatePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayLocalAxis": {
            "short_name": "dla",
            "long_name": "displayLocalAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dynamics": {
            "short_name": "dyn",
            "long_name": "dynamics",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "showManipDefault": {
            "short_name": "smd",
            "long_name": "showManipDefault",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "specifiedManipLocation": {
            "short_name": "sml",
            "long_name": "specifiedManipLocation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "rotateQuaternion": {
            "short_name": "rq",
            "long_name": "rotateQuaternion",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute4Double",
            "num_children": 4,
            "children": [
                "rotateQuaternionX",
                "rotateQuaternionY",
                "rotateQuaternionZ",
                "rotateQuaternionW"
            ]
        },
        "rotateQuaternionX": {
            "short_name": "rqx",
            "long_name": "rotateQuaternionX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionY": {
            "short_name": "rqy",
            "long_name": "rotateQuaternionY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionZ": {
            "short_name": "rqz",
            "long_name": "rotateQuaternionZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionW": {
            "short_name": "rqw",
            "long_name": "rotateQuaternionW",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        }
    },
    "joint": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "isCollapsed": {
            "short_name": "isc",
            "long_name": "isCollapsed",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "blackBox": {
            "short_name": "bbx",
            "long_name": "blackBox",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "borderConnections": {
            "short_name": "boc",
            "long_name": "borderConnections",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
        },
        "isHierarchicalConnection": {
            "short_name": "ish",
            "long_name": "isHierarchicalConnection",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 1,
            "default_value": False
        },
        "publishedNodeInfo": {
            "short_name": "pni",
            "long_name": "publishedNodeInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "rmbCommand": {
            "short_name": "rmc",
            "long_name": "rmbCommand",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "templateVersion": {
            "short_name": "tpv",
            "long_name": "templateVersion",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "boundingBox": {
            "short_name": "bb",
            "long_name": "boundingBox",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "boundingBoxMin",
                "boundingBoxMax",
                "boundingBoxSize"
            ]
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxMinX",
                "boundingBoxMinY",
                "boundingBoxMinZ"
            ]
        },
        "boundingBoxMinX": {
            "short_name": "bbnx",
            "long_name": "boundingBoxMinX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxMaxX",
                "boundingBoxMaxY",
                "boundingBoxMaxZ"
            ]
        },
        "boundingBoxMaxX": {
            "short_name": "bbxx",
            "long_name": "boundingBoxMaxX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxSizeX",
                "boundingBoxSizeY",
                "boundingBoxSizeZ"
            ]
        },
        "boundingBoxSizeX": {
            "short_name": "bbsx",
            "long_name": "boundingBoxSizeX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "center": {
            "short_name": "c",
            "long_name": "center",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "boundingBoxCenterX",
                "boundingBoxCenterY",
                "boundingBoxCenterZ"
            ]
        },
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0
        },
        "visibility": {
            "short_name": "v",
            "long_name": "visibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "intermediateObject": {
            "short_name": "io",
            "long_name": "intermediateObject",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "template": {
            "short_name": "tmp",
            "long_name": "template",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "instObjGroups": {
            "short_name": "iog",
            "long_name": "instObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "objectColorRGB": {
            "short_name": "obcc",
            "long_name": "objectColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "objectColorR",
                "objectColorG",
                "objectColorB"
            ]
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorG": {
            "short_name": "obcg",
            "long_name": "objectColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorRGB": {
            "short_name": "wfcc",
            "long_name": "wireColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "wireColorR",
                "wireColorG",
                "wireColorB"
            ]
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorG": {
            "short_name": "wfcg",
            "long_name": "wireColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "useObjectColor": {
            "short_name": "uoc",
            "long_name": "useObjectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "objectColor": {
            "short_name": "oc",
            "long_name": "objectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "drawOverride": {
            "short_name": "do",
            "long_name": "drawOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 12,
            "children": [
                "overrideDisplayType",
                "overrideLevelOfDetail",
                "overrideShading",
                "overrideTexturing",
                "overridePlayback",
                "overrideEnabled",
                "overrideVisibility",
                "hideOnPlayback",
                "overrideRGBColors",
                "overrideColor",
                "overrideColorRGB",
                "overrideColorA"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideTexturing": {
            "short_name": "ovt",
            "long_name": "overrideTexturing",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorG": {
            "short_name": "ovcg",
            "long_name": "overrideColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "lodVisibility": {
            "short_name": "lodv",
            "long_name": "lodVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "selectionChildHighlighting": {
            "short_name": "sech",
            "long_name": "selectionChildHighlighting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "renderInfo": {
            "short_name": "ri",
            "long_name": "renderInfo",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "identification",
                "layerRenderable",
                "layerOverrideColor"
            ]
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "ghosting": {
            "short_name": "gh",
            "long_name": "ghosting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "ghostingMode": {
            "short_name": "gm",
            "long_name": "ghostingMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "ghostCustomSteps": {
            "short_name": "gcs",
            "long_name": "ghostCustomSteps",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "ghostPreFrames",
                "ghostPostFrames",
                "ghostsStep"
            ]
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "ghostOpacityRange": {
            "short_name": "golr",
            "long_name": "ghostOpacityRange",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Float",
            "num_children": 2,
            "children": [
                "ghostFarOpacity",
                "ghostNearOpacity"
            ]
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "ghostColorPre": {
            "short_name": "gcp",
            "long_name": "ghostColorPre",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "ghostColorPreR",
                "ghostColorPreG",
                "ghostColorPreB"
            ]
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPost": {
            "short_name": "gac",
            "long_name": "ghostColorPost",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "ghostColorPostR",
                "ghostColorPostG",
                "ghostColorPostB"
            ]
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.878000020980835
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostUseDriver": {
            "short_name": "gud",
            "long_name": "ghostUseDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "hiddenInOutliner": {
            "short_name": "hio",
            "long_name": "hiddenInOutliner",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useOutlinerColor": {
            "short_name": "uocol",
            "long_name": "useOutlinerColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "outlinerColor": {
            "short_name": "oclr",
            "long_name": "outlinerColor",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outlinerColorR",
                "outlinerColorG",
                "outlinerColorB"
            ]
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorG": {
            "short_name": "oclrg",
            "long_name": "outlinerColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "translate": {
            "short_name": "t",
            "long_name": "translate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "translateX",
                "translateY",
                "translateZ"
            ]
        },
        "translateX": {
            "short_name": "tx",
            "long_name": "translateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "translateY": {
            "short_name": "ty",
            "long_name": "translateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "translateZ": {
            "short_name": "tz",
            "long_name": "translateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotate": {
            "short_name": "r",
            "long_name": "rotate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotateX",
                "rotateY",
                "rotateZ"
            ]
        },
        "rotateX": {
            "short_name": "rx",
            "long_name": "rotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateY": {
            "short_name": "ry",
            "long_name": "rotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateZ": {
            "short_name": "rz",
            "long_name": "rotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateOrder": {
            "short_name": "ro",
            "long_name": "rotateOrder",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "scale": {
            "short_name": "s",
            "long_name": "scale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "scaleX",
                "scaleY",
                "scaleZ"
            ]
        },
        "scaleX": {
            "short_name": "sx",
            "long_name": "scaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "scaleY": {
            "short_name": "sy",
            "long_name": "scaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "scaleZ": {
            "short_name": "sz",
            "long_name": "scaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "shear": {
            "short_name": "sh",
            "long_name": "shear",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "shearXY",
                "shearXZ",
                "shearYZ"
            ]
        },
        "shearXY": {
            "short_name": "shxy",
            "long_name": "shearXY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "shearXZ": {
            "short_name": "shxz",
            "long_name": "shearXZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "shearYZ": {
            "short_name": "shyz",
            "long_name": "shearYZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotatePivot": {
            "short_name": "rp",
            "long_name": "rotatePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotatePivotX",
                "rotatePivotY",
                "rotatePivotZ"
            ]
        },
        "rotatePivotX": {
            "short_name": "rpx",
            "long_name": "rotatePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotY": {
            "short_name": "rpy",
            "long_name": "rotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotZ": {
            "short_name": "rpz",
            "long_name": "rotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotTranslate": {
            "short_name": "rpt",
            "long_name": "rotatePivotTranslate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotatePivotTranslateX",
                "rotatePivotTranslateY",
                "rotatePivotTranslateZ"
            ]
        },
        "rotatePivotTranslateX": {
            "short_name": "rptx",
            "long_name": "rotatePivotTranslateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotTranslateY": {
            "short_name": "rpty",
            "long_name": "rotatePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotatePivotTranslateZ": {
            "short_name": "rptz",
            "long_name": "rotatePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivot": {
            "short_name": "sp",
            "long_name": "scalePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "scalePivotX",
                "scalePivotY",
                "scalePivotZ"
            ]
        },
        "scalePivotX": {
            "short_name": "spx",
            "long_name": "scalePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotY": {
            "short_name": "spy",
            "long_name": "scalePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotZ": {
            "short_name": "spz",
            "long_name": "scalePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotTranslate": {
            "short_name": "spt",
            "long_name": "scalePivotTranslate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "scalePivotTranslateX",
                "scalePivotTranslateY",
                "scalePivotTranslateZ"
            ]
        },
        "scalePivotTranslateX": {
            "short_name": "sptx",
            "long_name": "scalePivotTranslateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotTranslateY": {
            "short_name": "spty",
            "long_name": "scalePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "scalePivotTranslateZ": {
            "short_name": "sptz",
            "long_name": "scalePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "rotateAxis": {
            "short_name": "ra",
            "long_name": "rotateAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "rotateAxisX",
                "rotateAxisY",
                "rotateAxisZ"
            ]
        },
        "rotateAxisX": {
            "short_name": "rax",
            "long_name": "rotateAxisX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateAxisY": {
            "short_name": "ray",
            "long_name": "rotateAxisY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "rotateAxisZ": {
            "short_name": "raz",
            "long_name": "rotateAxisZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "transMinusRotatePivot": {
            "short_name": "tmrp",
            "long_name": "transMinusRotatePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "transMinusRotatePivotX",
                "transMinusRotatePivotY",
                "transMinusRotatePivotZ"
            ]
        },
        "transMinusRotatePivotX": {
            "short_name": "tmrx",
            "long_name": "transMinusRotatePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "transMinusRotatePivotY": {
            "short_name": "tmry",
            "long_name": "transMinusRotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "transMinusRotatePivotZ": {
            "short_name": "tmrz",
            "long_name": "transMinusRotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransLimit": {
            "short_name": "mntl",
            "long_name": "minTransLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minTransXLimit",
                "minTransYLimit",
                "minTransZLimit"
            ]
        },
        "minTransXLimit": {
            "short_name": "mtxl",
            "long_name": "minTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransYLimit": {
            "short_name": "mtyl",
            "long_name": "minTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransZLimit": {
            "short_name": "mtzl",
            "long_name": "minTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "maxTransLimit": {
            "short_name": "mxtl",
            "long_name": "maxTransLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxTransXLimit",
                "maxTransYLimit",
                "maxTransZLimit"
            ]
        },
        "maxTransXLimit": {
            "short_name": "xtxl",
            "long_name": "maxTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "maxTransYLimit": {
            "short_name": "xtyl",
            "long_name": "maxTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "maxTransZLimit": {
            "short_name": "xtzl",
            "long_name": "maxTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "minTransLimitEnable": {
            "short_name": "mtle",
            "long_name": "minTransLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "minTransXLimitEnable",
                "minTransYLimitEnable",
                "minTransZLimitEnable"
            ]
        },
        "minTransXLimitEnable": {
            "short_name": "mtxe",
            "long_name": "minTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransYLimitEnable": {
            "short_name": "mtye",
            "long_name": "minTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransZLimitEnable": {
            "short_name": "mtze",
            "long_name": "minTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransLimitEnable": {
            "short_name": "xtle",
            "long_name": "maxTransLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "maxTransXLimitEnable",
                "maxTransYLimitEnable",
                "maxTransZLimitEnable"
            ]
        },
        "maxTransXLimitEnable": {
            "short_name": "xtxe",
            "long_name": "maxTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransYLimitEnable": {
            "short_name": "xtye",
            "long_name": "maxTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransZLimitEnable": {
            "short_name": "xtze",
            "long_name": "maxTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotLimit": {
            "short_name": "mnrl",
            "long_name": "minRotLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minRotXLimit",
                "minRotYLimit",
                "minRotZLimit"
            ]
        },
        "minRotXLimit": {
            "short_name": "mrxl",
            "long_name": "minRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotYLimit": {
            "short_name": "mryl",
            "long_name": "minRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotZLimit": {
            "short_name": "mrzl",
            "long_name": "minRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotLimit": {
            "short_name": "mxrl",
            "long_name": "maxRotLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxRotXLimit",
                "maxRotYLimit",
                "maxRotZLimit"
            ]
        },
        "maxRotXLimit": {
            "short_name": "xrxl",
            "long_name": "maxRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotYLimit": {
            "short_name": "xryl",
            "long_name": "maxRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotZLimit": {
            "short_name": "xrzl",
            "long_name": "maxRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotLimitEnable": {
            "short_name": "mrle",
            "long_name": "minRotLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "minRotXLimitEnable",
                "minRotYLimitEnable",
                "minRotZLimitEnable"
            ]
        },
        "minRotXLimitEnable": {
            "short_name": "mrxe",
            "long_name": "minRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotYLimitEnable": {
            "short_name": "mrye",
            "long_name": "minRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotZLimitEnable": {
            "short_name": "mrze",
            "long_name": "minRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotLimitEnable": {
            "short_name": "xrle",
            "long_name": "maxRotLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "maxRotXLimitEnable",
                "maxRotYLimitEnable",
                "maxRotZLimitEnable"
            ]
        },
        "maxRotXLimitEnable": {
            "short_name": "xrxe",
            "long_name": "maxRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotYLimitEnable": {
            "short_name": "xrye",
            "long_name": "maxRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotZLimitEnable": {
            "short_name": "xrze",
            "long_name": "maxRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleLimit": {
            "short_name": "mnsl",
            "long_name": "minScaleLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minScaleXLimit",
                "minScaleYLimit",
                "minScaleZLimit"
            ]
        },
        "minScaleXLimit": {
            "short_name": "msxl",
            "long_name": "minScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleYLimit": {
            "short_name": "msyl",
            "long_name": "minScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleZLimit": {
            "short_name": "mszl",
            "long_name": "minScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "maxScaleLimit": {
            "short_name": "mxsl",
            "long_name": "maxScaleLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxScaleXLimit",
                "maxScaleYLimit",
                "maxScaleZLimit"
            ]
        },
        "maxScaleXLimit": {
            "short_name": "xsxl",
            "long_name": "maxScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleYLimit": {
            "short_name": "xsyl",
            "long_name": "maxScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleZLimit": {
            "short_name": "xszl",
            "long_name": "maxScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "minScaleLimitEnable": {
            "short_name": "msle",
            "long_name": "minScaleLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "minScaleXLimitEnable",
                "minScaleYLimitEnable",
                "minScaleZLimitEnable"
            ]
        },
        "minScaleXLimitEnable": {
            "short_name": "msxe",
            "long_name": "minScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleYLimitEnable": {
            "short_name": "msye",
            "long_name": "minScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleZLimitEnable": {
            "short_name": "msze",
            "long_name": "minScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleLimitEnable": {
            "short_name": "xsle",
            "long_name": "maxScaleLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 3,
            "children": [
                "maxScaleXLimitEnable",
                "maxScaleYLimitEnable",
                "maxScaleZLimitEnable"
            ]
        },
        "maxScaleXLimitEnable": {
            "short_name": "xsxe",
            "long_name": "maxScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleYLimitEnable": {
            "short_name": "xsye",
            "long_name": "maxScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleZLimitEnable": {
            "short_name": "xsze",
            "long_name": "maxScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "offsetParentMatrix": {
            "short_name": "opm",
            "long_name": "offsetParentMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "dagLocalMatrix": {
            "short_name": "dlm",
            "long_name": "dagLocalMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "dagLocalInverseMatrix": {
            "short_name": "dlim",
            "long_name": "dagLocalInverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "geometry": {
            "short_name": "g",
            "long_name": "geometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kGenericAttribute"
        },
        "xformMatrix": {
            "short_name": "xm",
            "long_name": "xformMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "selectHandle": {
            "short_name": "hdl",
            "long_name": "selectHandle",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "selectHandleX",
                "selectHandleY",
                "selectHandleZ"
            ]
        },
        "selectHandleX": {
            "short_name": "hdlx",
            "long_name": "selectHandleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "selectHandleY": {
            "short_name": "hdly",
            "long_name": "selectHandleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "selectHandleZ": {
            "short_name": "hdlz",
            "long_name": "selectHandleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "inheritsTransform": {
            "short_name": "it",
            "long_name": "inheritsTransform",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "displayHandle": {
            "short_name": "dh",
            "long_name": "displayHandle",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayScalePivot": {
            "short_name": "dsp",
            "long_name": "displayScalePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayRotatePivot": {
            "short_name": "drp",
            "long_name": "displayRotatePivot",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayLocalAxis": {
            "short_name": "dla",
            "long_name": "displayLocalAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dynamics": {
            "short_name": "dyn",
            "long_name": "dynamics",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "showManipDefault": {
            "short_name": "smd",
            "long_name": "showManipDefault",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "specifiedManipLocation": {
            "short_name": "sml",
            "long_name": "specifiedManipLocation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "rotateQuaternion": {
            "short_name": "rq",
            "long_name": "rotateQuaternion",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute4Double",
            "num_children": 4,
            "children": [
                "rotateQuaternionX",
                "rotateQuaternionY",
                "rotateQuaternionZ",
                "rotateQuaternionW"
            ]
        },
        "rotateQuaternionX": {
            "short_name": "rqx",
            "long_name": "rotateQuaternionX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionY": {
            "short_name": "rqy",
            "long_name": "rotateQuaternionY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionZ": {
            "short_name": "rqz",
            "long_name": "rotateQuaternionZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionW": {
            "short_name": "rqw",
            "long_name": "rotateQuaternionW",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "jointOrientType": {
            "short_name": "jot",
            "long_name": "jointOrientType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "jointType": {
            "short_name": "jt",
            "long_name": "jointType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "jointTypeX": {
            "short_name": "jtx",
            "long_name": "jointTypeX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "jointTypeY": {
            "short_name": "jty",
            "long_name": "jointTypeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "jointTypeZ": {
            "short_name": "jtz",
            "long_name": "jointTypeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "dofMask": {
            "short_name": "dm",
            "long_name": "dofMask",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 2021227011
        },
        "jointOrient": {
            "short_name": "jo",
            "long_name": "jointOrient",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "jointOrientX",
                "jointOrientY",
                "jointOrientZ"
            ]
        },
        "jointOrientX": {
            "short_name": "jox",
            "long_name": "jointOrientX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "jointOrientY": {
            "short_name": "joy",
            "long_name": "jointOrientY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "jointOrientZ": {
            "short_name": "joz",
            "long_name": "jointOrientZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "segmentScaleCompensate": {
            "short_name": "ssc",
            "long_name": "segmentScaleCompensate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "inverseScale": {
            "short_name": "is",
            "long_name": "inverseScale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "inverseScaleX",
                "inverseScaleY",
                "inverseScaleZ"
            ]
        },
        "inverseScaleX": {
            "short_name": "isx",
            "long_name": "inverseScaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "inverseScaleY": {
            "short_name": "isy",
            "long_name": "inverseScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "inverseScaleZ": {
            "short_name": "isz",
            "long_name": "inverseScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "stiffness": {
            "short_name": "st",
            "long_name": "stiffness",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "stiffnessX",
                "stiffnessY",
                "stiffnessZ"
            ]
        },
        "stiffnessX": {
            "short_name": "stx",
            "long_name": "stiffnessX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "stiffnessY": {
            "short_name": "sty",
            "long_name": "stiffnessY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "stiffnessZ": {
            "short_name": "stz",
            "long_name": "stiffnessZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "preferredAngle": {
            "short_name": "pa",
            "long_name": "preferredAngle",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "preferredAngleX",
                "preferredAngleY",
                "preferredAngleZ"
            ]
        },
        "preferredAngleX": {
            "short_name": "pax",
            "long_name": "preferredAngleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "preferredAngleY": {
            "short_name": "pay",
            "long_name": "preferredAngleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "preferredAngleZ": {
            "short_name": "paz",
            "long_name": "preferredAngleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotateDampRange": {
            "short_name": "ndr",
            "long_name": "minRotateDampRange",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minRotateDampRangeX",
                "minRotateDampRangeY",
                "minRotateDampRangeZ"
            ]
        },
        "minRotateDampRangeX": {
            "short_name": "ndx",
            "long_name": "minRotateDampRangeX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotateDampRangeY": {
            "short_name": "ndy",
            "long_name": "minRotateDampRangeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotateDampRangeZ": {
            "short_name": "ndz",
            "long_name": "minRotateDampRangeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "minRotateDampStrength": {
            "short_name": "nst",
            "long_name": "minRotateDampStrength",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "minRotateDampStrengthX",
                "minRotateDampStrengthY",
                "minRotateDampStrengthZ"
            ]
        },
        "minRotateDampStrengthX": {
            "short_name": "nstx",
            "long_name": "minRotateDampStrengthX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "minRotateDampStrengthY": {
            "short_name": "nsty",
            "long_name": "minRotateDampStrengthY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "minRotateDampStrengthZ": {
            "short_name": "nstz",
            "long_name": "minRotateDampStrengthZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "maxRotateDampRange": {
            "short_name": "xdr",
            "long_name": "maxRotateDampRange",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxRotateDampRangeX",
                "maxRotateDampRangeY",
                "maxRotateDampRangeZ"
            ]
        },
        "maxRotateDampRangeX": {
            "short_name": "xdx",
            "long_name": "maxRotateDampRangeX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotateDampRangeY": {
            "short_name": "xdy",
            "long_name": "maxRotateDampRangeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotateDampRangeZ": {
            "short_name": "xdz",
            "long_name": "maxRotateDampRangeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "maxRotateDampStrength": {
            "short_name": "xst",
            "long_name": "maxRotateDampStrength",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "maxRotateDampStrengthX",
                "maxRotateDampStrengthY",
                "maxRotateDampStrengthZ"
            ]
        },
        "maxRotateDampStrengthX": {
            "short_name": "xstx",
            "long_name": "maxRotateDampStrengthX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "maxRotateDampStrengthY": {
            "short_name": "xsty",
            "long_name": "maxRotateDampStrengthY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "maxRotateDampStrengthZ": {
            "short_name": "xstz",
            "long_name": "maxRotateDampStrengthZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "bindPose": {
            "short_name": "bps",
            "long_name": "bindPose",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "bindRotation": {
            "short_name": "br",
            "long_name": "bindRotation",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "bindRotationX",
                "bindRotationY",
                "bindRotationZ"
            ]
        },
        "bindRotationX": {
            "short_name": "brx",
            "long_name": "bindRotationX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindRotationY": {
            "short_name": "bry",
            "long_name": "bindRotationY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindRotationZ": {
            "short_name": "brz",
            "long_name": "bindRotationZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindJointOrient": {
            "short_name": "bjo",
            "long_name": "bindJointOrient",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "bindJointOrientX",
                "bindJointOrientY",
                "bindJointOrientZ"
            ]
        },
        "bindJointOrientX": {
            "short_name": "bjx",
            "long_name": "bindJointOrientX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindJointOrientY": {
            "short_name": "bjy",
            "long_name": "bindJointOrientY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindJointOrientZ": {
            "short_name": "bjz",
            "long_name": "bindJointOrientZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindRotateAxis": {
            "short_name": "bra",
            "long_name": "bindRotateAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "bindRotateAxisX",
                "bindRotateAxisY",
                "bindRotateAxisZ"
            ]
        },
        "bindRotateAxisX": {
            "short_name": "brax",
            "long_name": "bindRotateAxisX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindRotateAxisY": {
            "short_name": "bray",
            "long_name": "bindRotateAxisY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindRotateAxisZ": {
            "short_name": "braz",
            "long_name": "bindRotateAxisZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindScale": {
            "short_name": "bs",
            "long_name": "bindScale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "bindScaleX",
                "bindScaleY",
                "bindScaleZ"
            ]
        },
        "bindScaleX": {
            "short_name": "bsx",
            "long_name": "bindScaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindScaleY": {
            "short_name": "bsy",
            "long_name": "bindScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindScaleZ": {
            "short_name": "bsz",
            "long_name": "bindScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "bindInverseScale": {
            "short_name": "bis",
            "long_name": "bindInverseScale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "bindInverseScaleX",
                "bindInverseScaleY",
                "bindInverseScaleZ"
            ]
        },
        "bindInverseScaleX": {
            "short_name": "bix",
            "long_name": "bindInverseScaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "bindInverseScaleY": {
            "short_name": "biy",
            "long_name": "bindInverseScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "bindInverseScaleZ": {
            "short_name": "biz",
            "long_name": "bindInverseScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "bindSegmentScaleCompensate": {
            "short_name": "bsc",
            "long_name": "bindSegmentScaleCompensate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "isIKDirtyFlag": {
            "short_name": "idf",
            "long_name": "isIKDirtyFlag",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "inIKSolveFlag": {
            "short_name": "isf",
            "long_name": "inIKSolveFlag",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "drawStyle": {
            "short_name": "ds",
            "long_name": "drawStyle",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "drawLabel": {
            "short_name": "dl",
            "long_name": "drawLabel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "side": {
            "short_name": "sd",
            "long_name": "side",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "type": {
            "short_name": "typ",
            "long_name": "type",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "otherType": {
            "short_name": "otp",
            "long_name": "otherType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "ikRotate": {
            "short_name": "ikr",
            "long_name": "ikRotate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "ikRotateX",
                "ikRotateY",
                "ikRotateZ"
            ]
        },
        "ikRotateX": {
            "short_name": "irx",
            "long_name": "ikRotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "ikRotateY": {
            "short_name": "iry",
            "long_name": "ikRotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "ikRotateZ": {
            "short_name": "irz",
            "long_name": "ikRotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "fkRotate": {
            "short_name": "fkr",
            "long_name": "fkRotate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "fkRotateX",
                "fkRotateY",
                "fkRotateZ"
            ]
        },
        "fkRotateX": {
            "short_name": "frx",
            "long_name": "fkRotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "fkRotateY": {
            "short_name": "fry",
            "long_name": "fkRotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "fkRotateZ": {
            "short_name": "frz",
            "long_name": "fkRotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "radius": {
            "short_name": "radi",
            "long_name": "radius",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "hikNodeID": {
            "short_name": "hni",
            "long_name": "hikNodeID",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": -1
        },
        "hikFkJoint": {
            "short_name": "hfk",
            "long_name": "hikFkJoint",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        }
    },
    "multDoubleLinear": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "input1": {
            "short_name": "i1",
            "long_name": "input1",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "input2": {
            "short_name": "i2",
            "long_name": "input2",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "output": {
            "short_name": "o",
            "long_name": "output",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        }
    },
    "condition": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "operation": {
            "short_name": "op",
            "long_name": "operation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "firstTerm": {
            "short_name": "ft",
            "long_name": "firstTerm",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "secondTerm": {
            "short_name": "st",
            "long_name": "secondTerm",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "colorIfTrue": {
            "short_name": "ct",
            "long_name": "colorIfTrue",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "colorIfTrueR",
                "colorIfTrueG",
                "colorIfTrueB"
            ]
        },
        "colorIfTrueR": {
            "short_name": "ctr",
            "long_name": "colorIfTrueR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "colorIfTrueG": {
            "short_name": "ctg",
            "long_name": "colorIfTrueG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "colorIfTrueB": {
            "short_name": "ctb",
            "long_name": "colorIfTrueB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "colorIfFalse": {
            "short_name": "cf",
            "long_name": "colorIfFalse",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "colorIfFalseR",
                "colorIfFalseG",
                "colorIfFalseB"
            ]
        },
        "colorIfFalseR": {
            "short_name": "cfr",
            "long_name": "colorIfFalseR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "colorIfFalseG": {
            "short_name": "cfg",
            "long_name": "colorIfFalseG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "colorIfFalseB": {
            "short_name": "cfb",
            "long_name": "colorIfFalseB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "outColor": {
            "short_name": "oc",
            "long_name": "outColor",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outColorR",
                "outColorG",
                "outColorB"
            ]
        },
        "outColorR": {
            "short_name": "ocr",
            "long_name": "outColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorG": {
            "short_name": "ocg",
            "long_name": "outColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorB": {
            "short_name": "ocb",
            "long_name": "outColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "clamp": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "min": {
            "short_name": "mn",
            "long_name": "min",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "minR",
                "minG",
                "minB"
            ]
        },
        "minR": {
            "short_name": "mnr",
            "long_name": "minR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "minG": {
            "short_name": "mng",
            "long_name": "minG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "minB": {
            "short_name": "mnb",
            "long_name": "minB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "max": {
            "short_name": "mx",
            "long_name": "max",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "maxR",
                "maxG",
                "maxB"
            ]
        },
        "maxR": {
            "short_name": "mxr",
            "long_name": "maxR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "maxG": {
            "short_name": "mxg",
            "long_name": "maxG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "maxB": {
            "short_name": "mxb",
            "long_name": "maxB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "input": {
            "short_name": "ip",
            "long_name": "input",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "inputR",
                "inputG",
                "inputB"
            ]
        },
        "inputR": {
            "short_name": "ipr",
            "long_name": "inputR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "inputG": {
            "short_name": "ipg",
            "long_name": "inputG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "inputB": {
            "short_name": "ipb",
            "long_name": "inputB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "renderPassMode": {
            "short_name": "arp",
            "long_name": "renderPassMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "output": {
            "short_name": "op",
            "long_name": "output",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outputR",
                "outputG",
                "outputB"
            ]
        },
        "outputR": {
            "short_name": "opr",
            "long_name": "outputR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputG": {
            "short_name": "opg",
            "long_name": "outputG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputB": {
            "short_name": "opb",
            "long_name": "outputB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "remapValue": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "inputValue": {
            "short_name": "i",
            "long_name": "inputValue",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "inputMin": {
            "short_name": "imn",
            "long_name": "inputMin",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "inputMax": {
            "short_name": "imx",
            "long_name": "inputMax",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "outputMin": {
            "short_name": "omn",
            "long_name": "outputMin",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputMax": {
            "short_name": "omx",
            "long_name": "outputMax",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "value": {
            "short_name": "vl",
            "long_name": "value",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "color": {
            "short_name": "cl",
            "long_name": "color",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "outValue": {
            "short_name": "ov",
            "long_name": "outValue",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColor": {
            "short_name": "oc",
            "long_name": "outColor",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outColorR",
                "outColorG",
                "outColorB"
            ]
        },
        "outColorR": {
            "short_name": "ocr",
            "long_name": "outColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorG": {
            "short_name": "ocg",
            "long_name": "outColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorB": {
            "short_name": "ocb",
            "long_name": "outColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "remapColor": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "color": {
            "short_name": "cl",
            "long_name": "color",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "colorR",
                "colorG",
                "colorB"
            ]
        },
        "colorR": {
            "short_name": "cr",
            "long_name": "colorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "colorG": {
            "short_name": "cg",
            "long_name": "colorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "colorB": {
            "short_name": "cb",
            "long_name": "colorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "inputMin": {
            "short_name": "imn",
            "long_name": "inputMin",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "inputMax": {
            "short_name": "imx",
            "long_name": "inputMax",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "outputMin": {
            "short_name": "omn",
            "long_name": "outputMin",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputMax": {
            "short_name": "omx",
            "long_name": "outputMax",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "red": {
            "short_name": "r",
            "long_name": "red",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "green": {
            "short_name": "g",
            "long_name": "green",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "blue": {
            "short_name": "b",
            "long_name": "blue",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "renderPassMode": {
            "short_name": "arp",
            "long_name": "renderPassMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "outColor": {
            "short_name": "oc",
            "long_name": "outColor",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outColorR",
                "outColorG",
                "outColorB"
            ]
        },
        "outColorR": {
            "short_name": "ocr",
            "long_name": "outColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorG": {
            "short_name": "ocg",
            "long_name": "outColorG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorB": {
            "short_name": "ocb",
            "long_name": "outColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "uvPin": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "deformedGeometry": {
            "short_name": "curgeom",
            "long_name": "deformedGeometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "originalGeometry": {
            "short_name": "orggeom",
            "long_name": "originalGeometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "normalOverride": {
            "short_name": "novr",
            "long_name": "normalOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "railCurve": {
            "short_name": "rlcrv",
            "long_name": "railCurve",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "coordinate": {
            "short_name": "coord",
            "long_name": "coordinate",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_elements": 0
        },
        "uvSetName": {
            "short_name": "msn",
            "long_name": "uvSetName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "normalAxis": {
            "short_name": "nrm",
            "long_name": "normalAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "tangentAxis": {
            "short_name": "tng",
            "long_name": "tangentAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "normalizedIsoParms": {
            "short_name": "nrmip",
            "long_name": "normalizedIsoParms",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "relativeSpaceMode": {
            "short_name": "rsmd",
            "long_name": "relativeSpaceMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "relativeSpaceMatrix": {
            "short_name": "rsmat",
            "long_name": "relativeSpaceMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "outputTranslate": {
            "short_name": "ot",
            "long_name": "outputTranslate",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "outputMatrix": {
            "short_name": "omat",
            "long_name": "outputMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMatrixAttribute",
            "num_elements": 0
        },
        "cacheSetup": {
            "short_name": "csp",
            "long_name": "cacheSetup",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kOpaqueAttribute"
        }
    },
    "plusMinusAverage": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "operation": {
            "short_name": "op",
            "long_name": "operation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "input1D": {
            "short_name": "i1",
            "long_name": "input1D",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 11,
            "default_value": 0.0
        },
        "input2D": {
            "short_name": "i2",
            "long_name": "input2D",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute2Float",
            "num_elements": 0
        },
        "input3D": {
            "short_name": "i3",
            "long_name": "input3D",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_elements": 0
        },
        "output1D": {
            "short_name": "o1",
            "long_name": "output1D",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "output2D": {
            "short_name": "o2",
            "long_name": "output2D",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Float",
            "num_children": 2,
            "children": [
                "output2Dx",
                "output2Dy"
            ]
        },
        "output2Dx": {
            "short_name": "o2x",
            "long_name": "output2Dx",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "output2Dy": {
            "short_name": "o2y",
            "long_name": "output2Dy",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "output3D": {
            "short_name": "o3",
            "long_name": "output3D",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "output3Dx",
                "output3Dy",
                "output3Dz"
            ]
        },
        "output3Dx": {
            "short_name": "o3x",
            "long_name": "output3Dx",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "output3Dy": {
            "short_name": "o3y",
            "long_name": "output3Dy",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "output3Dz": {
            "short_name": "o3z",
            "long_name": "output3Dz",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "blendTwoAttr": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "input": {
            "short_name": "i",
            "long_name": "input",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 14,
            "default_value": 0.0
        },
        "output": {
            "short_name": "o",
            "long_name": "output",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "current": {
            "short_name": "c",
            "long_name": "current",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "attributesBlender": {
            "short_name": "ab",
            "long_name": "attributesBlender",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "blendColors": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "blender": {
            "short_name": "b",
            "long_name": "blender",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "color1": {
            "short_name": "c1",
            "long_name": "color1",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "color1R",
                "color1G",
                "color1B"
            ]
        },
        "color1R": {
            "short_name": "c1r",
            "long_name": "color1R",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "color1G": {
            "short_name": "c1g",
            "long_name": "color1G",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color1B": {
            "short_name": "c1b",
            "long_name": "color1B",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color2": {
            "short_name": "c2",
            "long_name": "color2",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "color2R",
                "color2G",
                "color2B"
            ]
        },
        "color2R": {
            "short_name": "c2r",
            "long_name": "color2R",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color2G": {
            "short_name": "c2g",
            "long_name": "color2G",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color2B": {
            "short_name": "c2b",
            "long_name": "color2B",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "renderPassMode": {
            "short_name": "arp",
            "long_name": "renderPassMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "output": {
            "short_name": "op",
            "long_name": "output",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "outputR",
                "outputG",
                "outputB"
            ]
        },
        "outputR": {
            "short_name": "opr",
            "long_name": "outputR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputG": {
            "short_name": "opg",
            "long_name": "outputG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputB": {
            "short_name": "opb",
            "long_name": "outputB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "decomposeMatrix": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "inputMatrix": {
            "short_name": "imat",
            "long_name": "inputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "inputRotateOrder": {
            "short_name": "ro",
            "long_name": "inputRotateOrder",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "outputTranslate": {
            "short_name": "ot",
            "long_name": "outputTranslate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "outputTranslateX",
                "outputTranslateY",
                "outputTranslateZ"
            ]
        },
        "outputTranslateX": {
            "short_name": "otx",
            "long_name": "outputTranslateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "outputTranslateY": {
            "short_name": "oty",
            "long_name": "outputTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "outputTranslateZ": {
            "short_name": "otz",
            "long_name": "outputTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute"
        },
        "outputRotate": {
            "short_name": "or",
            "long_name": "outputRotate",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "outputRotateX",
                "outputRotateY",
                "outputRotateZ"
            ]
        },
        "outputRotateX": {
            "short_name": "orx",
            "long_name": "outputRotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "outputRotateY": {
            "short_name": "ory",
            "long_name": "outputRotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "outputRotateZ": {
            "short_name": "orz",
            "long_name": "outputRotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute"
        },
        "outputScale": {
            "short_name": "os",
            "long_name": "outputScale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "outputScaleX",
                "outputScaleY",
                "outputScaleZ"
            ]
        },
        "outputScaleX": {
            "short_name": "osx",
            "long_name": "outputScaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputScaleY": {
            "short_name": "osy",
            "long_name": "outputScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputScaleZ": {
            "short_name": "osz",
            "long_name": "outputScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputShear": {
            "short_name": "osh",
            "long_name": "outputShear",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_children": 3,
            "children": [
                "outputShearX",
                "outputShearY",
                "outputShearZ"
            ]
        },
        "outputShearX": {
            "short_name": "oshx",
            "long_name": "outputShearX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputShearY": {
            "short_name": "oshy",
            "long_name": "outputShearY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputShearZ": {
            "short_name": "oshz",
            "long_name": "outputShearZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputQuat": {
            "short_name": "oq",
            "long_name": "outputQuat",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute4Double",
            "num_children": 4,
            "children": [
                "outputQuatX",
                "outputQuatY",
                "outputQuatZ",
                "outputQuatW"
            ]
        },
        "outputQuatX": {
            "short_name": "oqx",
            "long_name": "outputQuatX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputQuatY": {
            "short_name": "oqy",
            "long_name": "outputQuatY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputQuatZ": {
            "short_name": "oqz",
            "long_name": "outputQuatZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputQuatW": {
            "short_name": "oqw",
            "long_name": "outputQuatW",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.0
        }
    },
    "inverseMatrix": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "inputMatrix": {
            "short_name": "imat",
            "long_name": "inputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "outputMatrix": {
            "short_name": "omat",
            "long_name": "outputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        }
    },
    "multMatrix": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "matrixIn": {
            "short_name": "i",
            "long_name": "matrixIn",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMatrixAttribute",
            "num_elements": 0
        },
        "matrixSum": {
            "short_name": "o",
            "long_name": "matrixSum",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        }
    },
    "blendMatrix": {
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "caching": {
            "short_name": "cch",
            "long_name": "caching",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "frozen": {
            "short_name": "fzn",
            "long_name": "frozen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "isHistoricallyInteresting": {
            "short_name": "ihi",
            "long_name": "isHistoricallyInteresting",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 2
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute"
        },
        "enable": {
            "short_name": "enb",
            "long_name": "enable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "envelope": {
            "short_name": "env",
            "long_name": "envelope",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "target": {
            "short_name": "tgt",
            "long_name": "target",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "preSpaceMatrix": {
            "short_name": "premat",
            "long_name": "preSpaceMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "postSpaceMatrix": {
            "short_name": "pstmat",
            "long_name": "postSpaceMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "inputMatrix": {
            "short_name": "imat",
            "long_name": "inputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "outputMatrix": {
            "short_name": "omat",
            "long_name": "outputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        }
    }
}

ATTRIBUTES_SHORT_NAMES_MAP = {
    "msg": "message",
    "cch": "caching",
    "fzn": "frozen",
    "ihi": "isHistoricallyInteresting",
    "nds": "nodeState",
    "bnm": "binMembership",
    "hl": "hyperLayout",
    "isc": "isCollapsed",
    "bbx": "blackBox",
    "boc": "borderConnections",
    "ish": "isHierarchicalConnection",
    "pni": "publishedNodeInfo",
    "rmc": "rmbCommand",
    "tna": "templateName",
    "tpt": "templatePath",
    "vwn": "viewName",
    "icn": "iconName",
    "vwm": "viewMode",
    "tpv": "templateVersion",
    "uit": "uiTreatment",
    "ctrt": "customTreatment",
    "ctor": "creator",
    "cdat": "creationDate",
    "ctyp": "containerType",
    "bb": "boundingBox",
    "bbmn": "boundingBoxMin",
    "bbnx": "boundingBoxMinX",
    "bbny": "boundingBoxMinY",
    "bbnz": "boundingBoxMinZ",
    "bbmx": "boundingBoxMax",
    "bbxx": "boundingBoxMaxX",
    "bbxy": "boundingBoxMaxY",
    "bbxz": "boundingBoxMaxZ",
    "bbsi": "boundingBoxSize",
    "bbsx": "boundingBoxSizeX",
    "bbsy": "boundingBoxSizeY",
    "bbsz": "boundingBoxSizeZ",
    "c": "current",
    "bcx": "boundingBoxCenterX",
    "bcy": "boundingBoxCenterY",
    "bcz": "boundingBoxCenterZ",
    "m": "matrix",
    "im": "inverseMatrix",
    "wm": "worldMatrix",
    "wim": "worldInverseMatrix",
    "pm": "parentMatrix",
    "pim": "parentInverseMatrix",
    "v": "visibility",
    "io": "intermediateObject",
    "tmp": "template",
    "iog": "instObjGroups",
    "obcc": "objectColorRGB",
    "obcr": "objectColorR",
    "obcg": "objectColorG",
    "obcb": "objectColorB",
    "wfcc": "wireColorRGB",
    "wfcr": "wireColorR",
    "wfcg": "wireColorG",
    "wfcb": "wireColorB",
    "uoc": "useObjectColor",
    "oc": "outColor",
    "do": "drawOverride",
    "ovdt": "overrideDisplayType",
    "ovlod": "overrideLevelOfDetail",
    "ovs": "overrideShading",
    "ovt": "overrideTexturing",
    "ovp": "overridePlayback",
    "ove": "overrideEnabled",
    "ovv": "overrideVisibility",
    "hpb": "hideOnPlayback",
    "ovrgbf": "overrideRGBColors",
    "ovc": "overrideColor",
    "ovrgb": "overrideColorRGB",
    "ovcr": "overrideColorR",
    "ovcg": "overrideColorG",
    "ovcb": "overrideColorB",
    "ovca": "overrideColorA",
    "lodv": "lodVisibility",
    "sech": "selectionChildHighlighting",
    "ri": "renderInfo",
    "rlid": "identification",
    "rndr": "layerRenderable",
    "lovc": "layerOverrideColor",
    "rlio": "renderLayerInfo",
    "gh": "ghosting",
    "gm": "ghostingMode",
    "gcs": "ghostCustomSteps",
    "gprf": "ghostPreFrames",
    "gpof": "ghostPostFrames",
    "gstp": "ghostsStep",
    "gf": "ghostFrames",
    "golr": "ghostOpacityRange",
    "gfro": "ghostFarOpacity",
    "gnro": "ghostNearOpacity",
    "gcp": "ghostColorPre",
    "grr": "ghostColorPreR",
    "gpg": "ghostColorPreG",
    "gpb": "ghostColorPreB",
    "gac": "ghostColorPost",
    "gar": "ghostColorPostR",
    "gag": "ghostColorPostG",
    "gab": "ghostColorPostB",
    "gdr": "ghostDriver",
    "gud": "ghostUseDriver",
    "hio": "hiddenInOutliner",
    "uocol": "useOutlinerColor",
    "oclr": "outlinerColor",
    "oclrr": "outlinerColorR",
    "oclrg": "outlinerColorG",
    "oclrb": "outlinerColorB",
    "t": "translate",
    "tx": "translateX",
    "ty": "translateY",
    "tz": "translateZ",
    "r": "red",
    "rx": "rotateX",
    "ry": "rotateY",
    "rz": "rotateZ",
    "ro": "inputRotateOrder",
    "s": "scale",
    "sx": "scaleX",
    "sy": "scaleY",
    "sz": "scaleZ",
    "sh": "shear",
    "shxy": "shearXY",
    "shxz": "shearXZ",
    "shyz": "shearYZ",
    "rp": "rotatePivot",
    "rpx": "rotatePivotX",
    "rpy": "rotatePivotY",
    "rpz": "rotatePivotZ",
    "rpt": "rotatePivotTranslate",
    "rptx": "rotatePivotTranslateX",
    "rpty": "rotatePivotTranslateY",
    "rptz": "rotatePivotTranslateZ",
    "sp": "scalePivot",
    "spx": "scalePivotX",
    "spy": "scalePivotY",
    "spz": "scalePivotZ",
    "spt": "scalePivotTranslate",
    "sptx": "scalePivotTranslateX",
    "spty": "scalePivotTranslateY",
    "sptz": "scalePivotTranslateZ",
    "ra": "rotateAxis",
    "rax": "rotateAxisX",
    "ray": "rotateAxisY",
    "raz": "rotateAxisZ",
    "tmrp": "transMinusRotatePivot",
    "tmrx": "transMinusRotatePivotX",
    "tmry": "transMinusRotatePivotY",
    "tmrz": "transMinusRotatePivotZ",
    "mntl": "minTransLimit",
    "mtxl": "minTransXLimit",
    "mtyl": "minTransYLimit",
    "mtzl": "minTransZLimit",
    "mxtl": "maxTransLimit",
    "xtxl": "maxTransXLimit",
    "xtyl": "maxTransYLimit",
    "xtzl": "maxTransZLimit",
    "mtle": "minTransLimitEnable",
    "mtxe": "minTransXLimitEnable",
    "mtye": "minTransYLimitEnable",
    "mtze": "minTransZLimitEnable",
    "xtle": "maxTransLimitEnable",
    "xtxe": "maxTransXLimitEnable",
    "xtye": "maxTransYLimitEnable",
    "xtze": "maxTransZLimitEnable",
    "mnrl": "minRotLimit",
    "mrxl": "minRotXLimit",
    "mryl": "minRotYLimit",
    "mrzl": "minRotZLimit",
    "mxrl": "maxRotLimit",
    "xrxl": "maxRotXLimit",
    "xryl": "maxRotYLimit",
    "xrzl": "maxRotZLimit",
    "mrle": "minRotLimitEnable",
    "mrxe": "minRotXLimitEnable",
    "mrye": "minRotYLimitEnable",
    "mrze": "minRotZLimitEnable",
    "xrle": "maxRotLimitEnable",
    "xrxe": "maxRotXLimitEnable",
    "xrye": "maxRotYLimitEnable",
    "xrze": "maxRotZLimitEnable",
    "mnsl": "minScaleLimit",
    "msxl": "minScaleXLimit",
    "msyl": "minScaleYLimit",
    "mszl": "minScaleZLimit",
    "mxsl": "maxScaleLimit",
    "xsxl": "maxScaleXLimit",
    "xsyl": "maxScaleYLimit",
    "xszl": "maxScaleZLimit",
    "msle": "minScaleLimitEnable",
    "msxe": "minScaleXLimitEnable",
    "msye": "minScaleYLimitEnable",
    "msze": "minScaleZLimitEnable",
    "xsle": "maxScaleLimitEnable",
    "xsxe": "maxScaleXLimitEnable",
    "xsye": "maxScaleYLimitEnable",
    "xsze": "maxScaleZLimitEnable",
    "opm": "offsetParentMatrix",
    "dlm": "dagLocalMatrix",
    "dlim": "dagLocalInverseMatrix",
    "g": "green",
    "xm": "xformMatrix",
    "hdl": "selectHandle",
    "hdlx": "selectHandleX",
    "hdly": "selectHandleY",
    "hdlz": "selectHandleZ",
    "it": "inheritsTransform",
    "dh": "displayHandle",
    "dsp": "displayScalePivot",
    "drp": "displayRotatePivot",
    "dla": "displayLocalAxis",
    "dyn": "dynamics",
    "smd": "showManipDefault",
    "sml": "specifiedManipLocation",
    "rq": "rotateQuaternion",
    "rqx": "rotateQuaternionX",
    "rqy": "rotateQuaternionY",
    "rqz": "rotateQuaternionZ",
    "rqw": "rotateQuaternionW",
    "roi": "rotationInterpolation",
    "jot": "jointOrientType",
    "jt": "jointType",
    "jtx": "jointTypeX",
    "jty": "jointTypeY",
    "jtz": "jointTypeZ",
    "dm": "dofMask",
    "jo": "jointOrient",
    "jox": "jointOrientX",
    "joy": "jointOrientY",
    "joz": "jointOrientZ",
    "ssc": "segmentScaleCompensate",
    "is": "inverseScale",
    "isx": "inverseScaleX",
    "isy": "inverseScaleY",
    "isz": "inverseScaleZ",
    "st": "secondTerm",
    "stx": "stiffnessX",
    "sty": "stiffnessY",
    "stz": "stiffnessZ",
    "pa": "preferredAngle",
    "pax": "preferredAngleX",
    "pay": "preferredAngleY",
    "paz": "preferredAngleZ",
    "ndr": "minRotateDampRange",
    "ndx": "minRotateDampRangeX",
    "ndy": "minRotateDampRangeY",
    "ndz": "minRotateDampRangeZ",
    "nst": "minRotateDampStrength",
    "nstx": "minRotateDampStrengthX",
    "nsty": "minRotateDampStrengthY",
    "nstz": "minRotateDampStrengthZ",
    "xdr": "maxRotateDampRange",
    "xdx": "maxRotateDampRangeX",
    "xdy": "maxRotateDampRangeY",
    "xdz": "maxRotateDampRangeZ",
    "xst": "maxRotateDampStrength",
    "xstx": "maxRotateDampStrengthX",
    "xsty": "maxRotateDampStrengthY",
    "xstz": "maxRotateDampStrengthZ",
    "bps": "bindPose",
    "br": "bindRotation",
    "brx": "bindRotationX",
    "bry": "bindRotationY",
    "brz": "bindRotationZ",
    "bjo": "bindJointOrient",
    "bjx": "bindJointOrientX",
    "bjy": "bindJointOrientY",
    "bjz": "bindJointOrientZ",
    "bra": "bindRotateAxis",
    "brax": "bindRotateAxisX",
    "bray": "bindRotateAxisY",
    "braz": "bindRotateAxisZ",
    "bs": "bindScale",
    "bsx": "bindScaleX",
    "bsy": "bindScaleY",
    "bsz": "bindScaleZ",
    "bis": "bindInverseScale",
    "bix": "bindInverseScaleX",
    "biy": "bindInverseScaleY",
    "biz": "bindInverseScaleZ",
    "bsc": "bindSegmentScaleCompensate",
    "idf": "isIKDirtyFlag",
    "isf": "inIKSolveFlag",
    "ds": "drawStyle",
    "dl": "drawLabel",
    "sd": "side",
    "typ": "type",
    "otp": "otherType",
    "ikr": "ikRotate",
    "irx": "ikRotateX",
    "iry": "ikRotateY",
    "irz": "ikRotateZ",
    "fkr": "fkRotate",
    "frx": "fkRotateX",
    "fry": "fkRotateY",
    "frz": "fkRotateZ",
    "radi": "radius",
    "hni": "hikNodeID",
    "hfk": "hikFkJoint",
    "i1": "input1D",
    "i2": "input2D",
    "o": "matrixSum",
    "op": "output",
    "ft": "firstTerm",
    "ct": "colorIfTrue",
    "ctr": "colorIfTrueR",
    "ctg": "colorIfTrueG",
    "ctb": "colorIfTrueB",
    "cf": "colorIfFalse",
    "cfr": "colorIfFalseR",
    "cfg": "colorIfFalseG",
    "cfb": "colorIfFalseB",
    "ocr": "outColorR",
    "ocg": "outColorG",
    "ocb": "outColorB",
    "mn": "min",
    "mnr": "minR",
    "mng": "minG",
    "mnb": "minB",
    "mx": "max",
    "mxr": "maxR",
    "mxg": "maxG",
    "mxb": "maxB",
    "ip": "input",
    "ipr": "inputR",
    "ipg": "inputG",
    "ipb": "inputB",
    "arp": "renderPassMode",
    "opr": "outputR",
    "opg": "outputG",
    "opb": "outputB",
    "i": "matrixIn",
    "imn": "inputMin",
    "imx": "inputMax",
    "omn": "outputMin",
    "omx": "outputMax",
    "vl": "value",
    "cl": "color",
    "ov": "outValue",
    "cr": "colorR",
    "cg": "colorG",
    "cb": "colorB",
    "b": "blender",
    "curgeom": "deformedGeometry",
    "orggeom": "originalGeometry",
    "novr": "normalOverride",
    "rlcrv": "railCurve",
    "coord": "coordinate",
    "msn": "uvSetName",
    "nrm": "normalAxis",
    "tng": "tangentAxis",
    "nrmip": "normalizedIsoParms",
    "rsmd": "relativeSpaceMode",
    "rsmat": "relativeSpaceMatrix",
    "ot": "outputTranslate",
    "omat": "outputMatrix",
    "csp": "cacheSetup",
    "i3": "input3D",
    "o1": "output1D",
    "o2": "output2D",
    "o2x": "output2Dx",
    "o2y": "output2Dy",
    "o3": "output3D",
    "o3x": "output3Dx",
    "o3y": "output3Dy",
    "o3z": "output3Dz",
    "ab": "attributesBlender",
    "c1": "color1",
    "c1r": "color1R",
    "c1g": "color1G",
    "c1b": "color1B",
    "c2": "color2",
    "c2r": "color2R",
    "c2g": "color2G",
    "c2b": "color2B",
    "imat": "inputMatrix",
    "otx": "outputTranslateX",
    "oty": "outputTranslateY",
    "otz": "outputTranslateZ",
    "or": "outputRotate",
    "orx": "outputRotateX",
    "ory": "outputRotateY",
    "orz": "outputRotateZ",
    "os": "outputScale",
    "osx": "outputScaleX",
    "osy": "outputScaleY",
    "osz": "outputScaleZ",
    "osh": "outputShear",
    "oshx": "outputShearX",
    "oshy": "outputShearY",
    "oshz": "outputShearZ",
    "oq": "outputQuat",
    "oqx": "outputQuatX",
    "oqy": "outputQuatY",
    "oqz": "outputQuatZ",
    "oqw": "outputQuatW",
    "enb": "enable",
    "env": "envelope",
    "tgt": "target",
    "premat": "preSpaceMatrix",
    "pstmat": "postSpaceMatrix"
}

ATTRIBUTE_KEYS: TypeAlias = Literal[
   "minRotateDampRangeZ",
   "rotatePivotZ",
   "bindScaleY",
   "mxsl",
   "wim",
   "tz",
   "sech",
   "rotateAxisY",
   "templatePath",
   "railCurve",
   "boundingBoxSizeZ",
   "ovdt",
   "o2y",
   "s",
   "ory",
   "rptz",
   "sz",
   "lodVisibility",
   "rsmd",
   "opb",
   "hideOnPlayback",
   "overrideColorR",
   "jointTypeZ",
   "overrideColorG",
   "transMinusRotatePivotY",
   "overrideShading",
   "displayHandle",
   "minRotXLimit",
   "omn",
   "fkRotateX",
   "pay",
   "c2b",
   "tx",
   "ro",
   "output3D",
   "stz",
   "jot",
   "input3D",
   "displayScalePivot",
   "ikRotateZ",
   "cfb",
   "mn",
   "nst",
   "maxRotYLimit",
   "bindInverseScaleY",
   "grr",
   "rlcrv",
   "intermediateObject",
   "color",
   "bbxz",
   "inputMin",
   "xtyl",
   "jointOrientY",
   "gar",
   "jox",
   "frx",
   "maxRotLimitEnable",
   "jtz",
   "xstx",
   "isy",
   "rotateAxisZ",
   "colorIfFalseG",
   "tmp",
   "hni",
   "ssc",
   "ot",
   "xm",
   "joy",
   "ctrt",
   "ft",
   "lodv",
   "ghostColorPostB",
   "objectColor",
   "scale",
   "pm",
   "gcp",
   "bjo",
   "xtye",
   "cfg",
   "outputQuatX",
   "outputScaleY",
   "frz",
   "customTreatment",
   "bindJointOrientZ",
   "preferredAngle",
   "viewMode",
   "cch",
   "op",
   "osh",
   "minRotateDampRange",
   "cfr",
   "ghostColorPostR",
   "maxRotateDampRangeX",
   "inverseScaleX",
   "bindRotationX",
   "bindRotateAxisZ",
   "ghosting",
   "mxrl",
   "maxScaleZLimit",
   "o3x",
   "vwn",
   "frozen",
   "shearXY",
   "boundingBoxMinZ",
   "hfk",
   "minRotateDampRangeY",
   "spz",
   "nsty",
   "maxTransZLimitEnable",
   "rpx",
   "overrideRGBColors",
   "inputMatrix",
   "boundingBoxMaxZ",
   "bjy",
   "selectHandleZ",
   "mtyl",
   "colorIfTrueB",
   "outputB",
   "hpb",
   "o1",
   "min",
   "inheritsTransform",
   "target",
   "maxRotZLimitEnable",
   "rotatePivotY",
   "otx",
   "ghostColorPostG",
   "pstmat",
   "displayLocalAxis",
   "outColorB",
   "sp",
   "ndx",
   "gm",
   "joz",
   "orx",
   "outlinerColor",
   "cr",
   "jt",
   "stiffness",
   "irz",
   "xrze",
   "xrye",
   "br",
   "drawStyle",
   "tpv",
   "templateName",
   "jointTypeX",
   "cdat",
   "xdz",
   "ghostFrames",
   "gnro",
   "dm",
   "nrm",
   "mtle",
   "osy",
   "mryl",
   "gdr",
   "rmc",
   "t",
   "ovp",
   "xdx",
   "gag",
   "otz",
   "orggeom",
   "xsyl",
   "bbxx",
   "specifiedManipLocation",
   "selectionChildHighlighting",
   "type",
   "mtzl",
   "gf",
   "i",
   "objectColorRGB",
   "mx",
   "ghostCustomSteps",
   "tmry",
   "hdl",
   "dsp",
   "minB",
   "io",
   "overrideVisibility",
   "wireColorB",
   "b",
   "secondTerm",
   "minTransXLimit",
   "offsetParentMatrix",
   "dynamics",
   "overrideColorA",
   "o3",
   "maxRotateDampRange",
   "preferredAngleX",
   "inverseScaleY",
   "rotateX",
   "shear",
   "ghostColorPost",
   "bjz",
   "idf",
   "minTransLimitEnable",
   "uit",
   "mszl",
   "cg",
   "boundingBoxMinY",
   "ovlod",
   "hikFkJoint",
   "overrideColorB",
   "color2G",
   "colorB",
   "identification",
   "msxe",
   "minTransYLimitEnable",
   "bindJointOrientX",
   "oclrr",
   "oty",
   "ov",
   "colorIfFalse",
   "env",
   "minRotateDampStrengthY",
   "minRotYLimit",
   "center",
   "ipb",
   "translate",
   "wm",
   "wfcg",
   "tmrx",
   "minTransZLimitEnable",
   "rpz",
   "hikNodeID",
   "bindInverseScale",
   "ghostColorPreB",
   "minScaleYLimit",
   "minRotYLimitEnable",
   "inputValue",
   "biz",
   "xformMatrix",
   "isf",
   "hio",
   "ghostColorPreG",
   "maxRotateDampStrength",
   "outputShearX",
   "rotatePivotTranslateY",
   "bbsi",
   "wfcc",
   "stiffnessY",
   "isz",
   "o2",
   "input1",
   "xryl",
   "bindRotationY",
   "color2",
   "c2r",
   "msyl",
   "rotateQuaternionY",
   "sd",
   "ndr",
   "coord",
   "uoc",
   "outputRotate",
   "scaleX",
   "bs",
   "value",
   "rq",
   "xstz",
   "rotateQuaternionX",
   "wireColorG",
   "oqx",
   "hyperLayout",
   "r",
   "red",
   "o",
   "showManipDefault",
   "stiffnessZ",
   "minScaleLimitEnable",
   "hiddenInOutliner",
   "bbnz",
   "preferredAngleY",
   "scalePivotZ",
   "rlio",
   "jo",
   "ctor",
   "outputShearY",
   "rotateAxisX",
   "minRotZLimitEnable",
   "output3Dy",
   "pax",
   "outColor",
   "otp",
   "bindRotateAxis",
   "overrideEnabled",
   "useOutlinerColor",
   "translateX",
   "rotateY",
   "bbx",
   "mxb",
   "ra",
   "ovcr",
   "minScaleZLimit",
   "cb",
   "maxTransLimit",
   "maxRotYLimitEnable",
   "rotate",
   "overrideColor",
   "outlinerColorB",
   "publishedNodeInfo",
   "minScaleXLimit",
   "colorIfFalseR",
   "maxRotateDampStrengthX",
   "oclrb",
   "outputMin",
   "rqy",
   "sptx",
   "segmentScaleCompensate",
   "c1r",
   "fkRotateY",
   "minRotXLimitEnable",
   "typ",
   "scaleZ",
   "radius",
   "inverseScaleZ",
   "output2D",
   "ndz",
   "it",
   "creator",
   "ghostPostFrames",
   "rz",
   "mntl",
   "jtx",
   "outputQuatW",
   "uvSetName",
   "rqx",
   "im",
   "ovc",
   "ikRotate",
   "normalAxis",
   "biy",
   "attributesBlender",
   "ghostColorPre",
   "fzn",
   "xdy",
   "rqw",
   "outputRotateY",
   "shearXZ",
   "spt",
   "output3Dz",
   "matrixIn",
   "ctg",
   "iry",
   "minTransZLimit",
   "tangentAxis",
   "jty",
   "ry",
   "bsx",
   "ghostColorPreR",
   "minTransLimit",
   "blackBox",
   "postSpaceMatrix",
   "translateZ",
   "maxRotateDampStrengthY",
   "boundingBoxCenterX",
   "caching",
   "ocb",
   "nrmip",
   "gpof",
   "cl",
   "isHistoricallyInteresting",
   "imn",
   "boundingBoxCenterY",
   "ghostOpacityRange",
   "bry",
   "scaleY",
   "input2",
   "maxTransYLimit",
   "outputRotateZ",
   "geometry",
   "maxRotZLimit",
   "xrzl",
   "scalePivotTranslate",
   "bindRotateAxisX",
   "xsty",
   "gpg",
   "colorIfTrueR",
   "xtzl",
   "pni",
   "msze",
   "minRotateDampRangeX",
   "gud",
   "colorR",
   "scalePivotX",
   "maxScaleLimit",
   "ri",
   "opg",
   "osz",
   "xszl",
   "jointOrient",
   "instObjGroups",
   "uocol",
   "msg",
   "xrle",
   "minScaleZLimitEnable",
   "colorIfTrue",
   "wfcr",
   "scalePivotTranslateZ",
   "color2B",
   "maxG",
   "ab",
   "ghostDriver",
   "coordinate",
   "omx",
   "jointOrientX",
   "outputQuatZ",
   "bcz",
   "raz",
   "normalOverride",
   "selectHandleY",
   "nstx",
   "maxScaleYLimit",
   "bcy",
   "ctb",
   "output2Dx",
   "outlinerColorR",
   "ipg",
   "isHierarchicalConnection",
   "bindRotationZ",
   "preferredAngleZ",
   "outputTranslateY",
   "color2R",
   "outColorG",
   "tpt",
   "spty",
   "outputShearZ",
   "maxRotateDampStrengthZ",
   "rmbCommand",
   "rotatePivotTranslateX",
   "maxRotXLimit",
   "ghostNearOpacity",
   "oshx",
   "curgeom",
   "outputQuatY",
   "bcx",
   "outputTranslate",
   "boundingBoxSizeX",
   "bps",
   "drawLabel",
   "jointOrientType",
   "maxScaleYLimitEnable",
   "rax",
   "mtye",
   "blender",
   "bsz",
   "ikRotateY",
   "o3z",
   "transMinusRotatePivot",
   "inIKSolveFlag",
   "opr",
   "outColorR",
   "bindPose",
   "pim",
   "worldMatrix",
   "mtxl",
   "rotateQuaternionZ",
   "nds",
   "ghostPreFrames",
   "color1B",
   "oclrg",
   "obcb",
   "msxl",
   "jointTypeY",
   "ocr",
   "vl",
   "overridePlayback",
   "bindRotation",
   "i1",
   "ovca",
   "maxScaleZLimitEnable",
   "parentMatrix",
   "g",
   "boc",
   "bra",
   "outputRotateX",
   "outputScale",
   "outputTranslateX",
   "spy",
   "rotatePivotX",
   "imat",
   "rotateZ",
   "matrix",
   "current",
   "bbxy",
   "minRotLimitEnable",
   "iog",
   "fkRotateZ",
   "template",
   "otherType",
   "stx",
   "osx",
   "mrzl",
   "outputScaleZ",
   "rndr",
   "rx",
   "bbmx",
   "scalePivotTranslateY",
   "o3y",
   "displayRotatePivot",
   "inputG",
   "bbsx",
   "rpt",
   "orz",
   "shxz",
   "v",
   "outValue",
   "tgt",
   "ovs",
   "ndy",
   "visibility",
   "rlid",
   "selectHandle",
   "bjx",
   "dlim",
   "ghostFarOpacity",
   "sh",
   "output1D",
   "creationDate",
   "dofMask",
   "fkRotate",
   "input",
   "tna",
   "msle",
   "sml",
   "minRotateDampStrengthX",
   "output",
   "minG",
   "shearYZ",
   "minRotZLimit",
   "oqz",
   "paz",
   "maxTransZLimit",
   "outputR",
   "maxB",
   "maxTransXLimit",
   "premat",
   "rotateQuaternionW",
   "bbnx",
   "enable",
   "ove",
   "relativeSpaceMatrix",
   "pa",
   "hl",
   "maxRotLimit",
   "ovt",
   "shxy",
   "outputQuat",
   "bis",
   "maxRotateDampRangeZ",
   "isIKDirtyFlag",
   "msn",
   "rotatePivotTranslateZ",
   "oc",
   "mrle",
   "i2",
   "mtze",
   "worldInverseMatrix",
   "bindJointOrientY",
   "mnr",
   "maxTransLimitEnable",
   "envelope",
   "xtle",
   "mrxl",
   "dlm",
   "msye",
   "bsy",
   "rp",
   "boundingBoxMaxX",
   "isCollapsed",
   "bindScaleX",
   "boundingBoxMax",
   "outputScaleX",
   "rptx",
   "wireColorRGB",
   "csp",
   "useObjectColor",
   "inputMax",
   "xrxl",
   "deformedGeometry",
   "overrideColorRGB",
   "sx",
   "ikr",
   "roi",
   "hdly",
   "irx",
   "objectColorG",
   "obcr",
   "wfcb",
   "output3Dx",
   "scalePivotY",
   "c2",
   "braz",
   "rotateAxis",
   "mnrl",
   "minRotateDampStrengthZ",
   "mrze",
   "bray",
   "ghostUseDriver",
   "oclr",
   "mtxe",
   "templateVersion",
   "ihi",
   "oqw",
   "hdlz",
   "max",
   "bbmn",
   "hdlx",
   "xst",
   "borderConnections",
   "obcc",
   "maxScaleLimitEnable",
   "dagLocalMatrix",
   "selectHandleX",
   "originalGeometry",
   "gpb",
   "tmrp",
   "maxR",
   "ipr",
   "radi",
   "minRotLimit",
   "gfro",
   "bnm",
   "dyn",
   "rpty",
   "renderLayerInfo",
   "rotatePivot",
   "matrixSum",
   "scalePivotTranslateX",
   "boundingBoxMin",
   "operation",
   "spx",
   "xrxe",
   "objectColorB",
   "ovrgb",
   "cf",
   "bbsz",
   "translateY",
   "i3",
   "rotateOrder",
   "rsmat",
   "xsxl",
   "color1",
   "oshz",
   "mnb",
   "layerRenderable",
   "ghostsStep",
   "minScaleLimit",
   "scalePivot",
   "inverseScale",
   "bindSegmentScaleCompensate",
   "ovv",
   "sptz",
   "minScaleYLimitEnable",
   "maxRotateDampRangeY",
   "bbsy",
   "ray",
   "ip",
   "output2Dy",
   "lovc",
   "brax",
   "green",
   "normalizedIsoParms",
   "tmrz",
   "binMembership",
   "boundingBoxSize",
   "ty",
   "minR",
   "color1G",
   "bix",
   "gprf",
   "m",
   "ocg",
   "firstTerm",
   "shyz",
   "stiffnessX",
   "or",
   "input2D",
   "oshy",
   "xtxe",
   "minTransXLimitEnable",
   "side",
   "bindJointOrient",
   "bindScaleZ",
   "minRotateDampStrength",
   "color1R",
   "obcg",
   "outputTranslateZ",
   "brz",
   "iconName",
   "ghostingMode",
   "ovrgbf",
   "st",
   "arp",
   "wireColorR",
   "cacheSetup",
   "outputG",
   "mng",
   "bsc",
   "ctyp",
   "bb",
   "overrideDisplayType",
   "maxScaleXLimit",
   "overrideLevelOfDetail",
   "dagLocalInverseMatrix",
   "inputB",
   "nstz",
   "enb",
   "xsxe",
   "overrideTexturing",
   "transMinusRotatePivotX",
   "minTransYLimit",
   "tng",
   "jointType",
   "outputMax",
   "mxr",
   "maxScaleXLimitEnable",
   "dh",
   "ish",
   "containerType",
   "outlinerColorG",
   "ds",
   "imx",
   "os",
   "rpy",
   "mxg",
   "message",
   "minScaleXLimitEnable",
   "objectColorR",
   "mrye",
   "xtxl",
   "ikRotateX",
   "outputMatrix",
   "jointOrientZ",
   "oq",
   "renderPassMode",
   "boundingBox",
   "relativeSpaceMode",
   "gstp",
   "novr",
   "ovcg",
   "colorIfFalseB",
   "drawOverride",
   "xdr",
   "maxTransXLimitEnable",
   "mnsl",
   "transMinusRotatePivotZ",
   "bindRotateAxisY",
   "renderInfo",
   "is",
   "bindInverseScaleX",
   "do",
   "rotatePivotTranslate",
   "gac",
   "dla",
   "parentInverseMatrix",
   "isc",
   "preSpaceMatrix",
   "c1g",
   "input1D",
   "gh",
   "drp",
   "maxRotXLimitEnable",
   "colorIfTrueG",
   "vwm",
   "mxtl",
   "ct",
   "isx",
   "mrxe",
   "xtze",
   "c1b",
   "boundingBoxMinX",
   "bbny",
   "o2x",
   "opm",
   "smd",
   "brx",
   "blue",
   "inputR",
   "sty",
   "icn",
   "xsye",
   "bindScale",
   "maxTransYLimitEnable",
   "rqz",
   "c2g",
   "inputRotateOrder",
   "fry",
   "bindInverseScaleZ",
   "boundingBoxMaxY",
   "viewName",
   "c",
   "gcs",
   "sy",
   "xsle",
   "c1",
   "omat",
   "colorG",
   "boundingBoxCenterZ",
   "xsze",
   "inverseMatrix",
   "layerOverrideColor",
   "rotateQuaternion",
   "outputShear",
   "fkr",
   "dl",
   "oqy",
   "boundingBoxSizeY",
   "ctr",
   "golr",
   "gab",
   "ovcb",

]

