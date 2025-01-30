# Auto-generated Maya attributes file

ATTRIBUTES_PROPERTIES = {
    "transform": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
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
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "dagLocalInverseMatrix": {
            "short_name": "dlim",
            "long_name": "dagLocalInverseMatrix",
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
        "geometry": {
            "short_name": "g",
            "long_name": "geometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kGenericAttribute"
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
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.878000020980835
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
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
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
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 9
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.5
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
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
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
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 1
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
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 4,
            "default_value": 0
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
        "instObjGroups": {
            "short_name": "iog",
            "long_name": "instObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
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
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 2,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 1,
            "default_value": True
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
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
        "maxRotXLimit": {
            "short_name": "xrxl",
            "long_name": "maxRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotLimit",
            "unit_type": 1,
            "default_value": 0.7853981633974483
        },
        "maxRotXLimitEnable": {
            "short_name": "xrxe",
            "long_name": "maxRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotYLimit": {
            "short_name": "xryl",
            "long_name": "maxRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotLimit",
            "unit_type": 1,
            "default_value": 0.7853981633974483
        },
        "maxRotYLimitEnable": {
            "short_name": "xrye",
            "long_name": "maxRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotZLimit": {
            "short_name": "xrzl",
            "long_name": "maxRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotLimit",
            "unit_type": 1,
            "default_value": 0.7853981633974483
        },
        "maxRotZLimitEnable": {
            "short_name": "xrze",
            "long_name": "maxRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "maxScaleXLimit": {
            "short_name": "xsxl",
            "long_name": "maxScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimit",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleXLimitEnable": {
            "short_name": "xsxe",
            "long_name": "maxScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleYLimit": {
            "short_name": "xsyl",
            "long_name": "maxScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimit",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleYLimitEnable": {
            "short_name": "xsye",
            "long_name": "maxScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleZLimit": {
            "short_name": "xszl",
            "long_name": "maxScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimit",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleZLimitEnable": {
            "short_name": "xsze",
            "long_name": "maxScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "maxTransXLimit": {
            "short_name": "xtxl",
            "long_name": "maxTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "maxTransLimit",
            "unit_type": 2,
            "default_value": 1.0
        },
        "maxTransXLimitEnable": {
            "short_name": "xtxe",
            "long_name": "maxTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransYLimit": {
            "short_name": "xtyl",
            "long_name": "maxTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "maxTransLimit",
            "unit_type": 2,
            "default_value": 1.0
        },
        "maxTransYLimitEnable": {
            "short_name": "xtye",
            "long_name": "maxTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransZLimit": {
            "short_name": "xtzl",
            "long_name": "maxTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "maxTransLimit",
            "unit_type": 2,
            "default_value": 1.0
        },
        "maxTransZLimitEnable": {
            "short_name": "xtze",
            "long_name": "maxTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "minRotXLimit": {
            "short_name": "mrxl",
            "long_name": "minRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotLimit",
            "unit_type": 1,
            "default_value": -0.7853981633974483
        },
        "minRotXLimitEnable": {
            "short_name": "mrxe",
            "long_name": "minRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotYLimit": {
            "short_name": "mryl",
            "long_name": "minRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotLimit",
            "unit_type": 1,
            "default_value": -0.7853981633974483
        },
        "minRotYLimitEnable": {
            "short_name": "mrye",
            "long_name": "minRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotZLimit": {
            "short_name": "mrzl",
            "long_name": "minRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotLimit",
            "unit_type": 1,
            "default_value": -0.7853981633974483
        },
        "minRotZLimitEnable": {
            "short_name": "mrze",
            "long_name": "minRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minRotLimitEnable",
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
        "minScaleXLimit": {
            "short_name": "msxl",
            "long_name": "minScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimit",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleXLimitEnable": {
            "short_name": "msxe",
            "long_name": "minScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleYLimit": {
            "short_name": "msyl",
            "long_name": "minScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimit",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleYLimitEnable": {
            "short_name": "msye",
            "long_name": "minScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleZLimit": {
            "short_name": "mszl",
            "long_name": "minScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimit",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleZLimitEnable": {
            "short_name": "msze",
            "long_name": "minScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "minTransXLimit": {
            "short_name": "mtxl",
            "long_name": "minTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "minTransLimit",
            "unit_type": 2,
            "default_value": -1.0
        },
        "minTransXLimitEnable": {
            "short_name": "mtxe",
            "long_name": "minTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransYLimit": {
            "short_name": "mtyl",
            "long_name": "minTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "minTransLimit",
            "unit_type": 2,
            "default_value": -1.0
        },
        "minTransYLimitEnable": {
            "short_name": "mtye",
            "long_name": "minTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransZLimit": {
            "short_name": "mtzl",
            "long_name": "minTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "minTransLimit",
            "unit_type": 2,
            "default_value": -1.0
        },
        "minTransZLimitEnable": {
            "short_name": "mtze",
            "long_name": "minTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
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
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
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
        "offsetParentMatrix": {
            "short_name": "opm",
            "long_name": "offsetParentMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
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
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
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
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
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
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "parent_plug": "drawOverride",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
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
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
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
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
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
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateAxisY": {
            "short_name": "ray",
            "long_name": "rotateAxisY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateAxisZ": {
            "short_name": "raz",
            "long_name": "rotateAxisZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateOrder": {
            "short_name": "ro",
            "long_name": "rotateOrder",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotTranslateY": {
            "short_name": "rpty",
            "long_name": "rotatePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotTranslateZ": {
            "short_name": "rptz",
            "long_name": "rotatePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotX": {
            "short_name": "rpx",
            "long_name": "rotatePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotY": {
            "short_name": "rpy",
            "long_name": "rotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotZ": {
            "short_name": "rpz",
            "long_name": "rotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivot",
            "unit_type": 2,
            "default_value": 0.0
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
        "rotateQuaternionW": {
            "short_name": "rqw",
            "long_name": "rotateQuaternionW",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "rotateQuaternion",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionX": {
            "short_name": "rqx",
            "long_name": "rotateQuaternionX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "rotateQuaternion",
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
            "parent_plug": "rotateQuaternion",
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
            "parent_plug": "rotateQuaternion",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateX": {
            "short_name": "rx",
            "long_name": "rotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateY": {
            "short_name": "ry",
            "long_name": "rotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateZ": {
            "short_name": "rz",
            "long_name": "rotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotate",
            "unit_type": 1,
            "default_value": 0.0
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotTranslateY": {
            "short_name": "spty",
            "long_name": "scalePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotTranslateZ": {
            "short_name": "sptz",
            "long_name": "scalePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotX": {
            "short_name": "spx",
            "long_name": "scalePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotY": {
            "short_name": "spy",
            "long_name": "scalePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotZ": {
            "short_name": "spz",
            "long_name": "scalePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scaleX": {
            "short_name": "sx",
            "long_name": "scaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "scale",
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
            "parent_plug": "scale",
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
            "parent_plug": "scale",
            "numeric_type": 14,
            "default_value": 1.0
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "selectHandle",
            "unit_type": 2,
            "default_value": 0.0
        },
        "selectHandleY": {
            "short_name": "hdly",
            "long_name": "selectHandleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "selectHandle",
            "unit_type": 2,
            "default_value": 0.0
        },
        "selectHandleZ": {
            "short_name": "hdlz",
            "long_name": "selectHandleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "selectHandle",
            "unit_type": 2,
            "default_value": 0.0
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
            "parent_plug": "shear",
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
            "parent_plug": "shear",
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
            "parent_plug": "shear",
            "numeric_type": 14,
            "default_value": 0.0
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
            "type_str": "kTypedAttribute",
            "typed_type": 24
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
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "transMinusRotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "transMinusRotatePivotY": {
            "short_name": "tmry",
            "long_name": "transMinusRotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "transMinusRotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "transMinusRotatePivotZ": {
            "short_name": "tmrz",
            "long_name": "transMinusRotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "transMinusRotatePivot",
            "unit_type": 2,
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "translate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "translateY": {
            "short_name": "ty",
            "long_name": "translateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "translate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "translateZ": {
            "short_name": "tz",
            "long_name": "translateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "translate",
            "unit_type": 2,
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
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
            "parent_plug": "wireColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "xformMatrix": {
            "short_name": "xm",
            "long_name": "xformMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
        }
    },
    "joint": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
            "parent_plug": "bindInverseScale",
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
            "parent_plug": "bindInverseScale",
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
            "parent_plug": "bindInverseScale",
            "numeric_type": 14,
            "default_value": 1.0
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindJointOrient",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindJointOrientY": {
            "short_name": "bjy",
            "long_name": "bindJointOrientY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindJointOrient",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindJointOrientZ": {
            "short_name": "bjz",
            "long_name": "bindJointOrientZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindJointOrient",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindPose": {
            "short_name": "bps",
            "long_name": "bindPose",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindRotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindRotateAxisY": {
            "short_name": "bray",
            "long_name": "bindRotateAxisY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindRotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindRotateAxisZ": {
            "short_name": "braz",
            "long_name": "bindRotateAxisZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindRotateAxis",
            "unit_type": 1,
            "default_value": 0.0
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindRotation",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindRotationY": {
            "short_name": "bry",
            "long_name": "bindRotationY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindRotation",
            "unit_type": 1,
            "default_value": 0.0
        },
        "bindRotationZ": {
            "short_name": "brz",
            "long_name": "bindRotationZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindRotation",
            "unit_type": 1,
            "default_value": 0.0
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindScale",
            "unit_type": 1,
            "default_value": 1.0
        },
        "bindScaleY": {
            "short_name": "bsy",
            "long_name": "bindScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindScale",
            "unit_type": 1,
            "default_value": 1.0
        },
        "bindScaleZ": {
            "short_name": "bsz",
            "long_name": "bindScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "bindScale",
            "unit_type": 1,
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
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
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
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "dagLocalInverseMatrix": {
            "short_name": "dlim",
            "long_name": "dagLocalInverseMatrix",
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
        "drawStyle": {
            "short_name": "ds",
            "long_name": "drawStyle",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "fkRotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "fkRotateY": {
            "short_name": "fry",
            "long_name": "fkRotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "fkRotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "fkRotateZ": {
            "short_name": "frz",
            "long_name": "fkRotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "fkRotate",
            "unit_type": 1,
            "default_value": 0.0
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
        "geometry": {
            "short_name": "g",
            "long_name": "geometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kGenericAttribute"
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
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.878000020980835
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
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
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
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 9
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.5
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
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
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
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 1
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
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "hikFkJoint": {
            "short_name": "hfk",
            "long_name": "hikFkJoint",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 4,
            "default_value": 0
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "ikRotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "ikRotateY": {
            "short_name": "iry",
            "long_name": "ikRotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "ikRotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "ikRotateZ": {
            "short_name": "irz",
            "long_name": "ikRotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "ikRotate",
            "unit_type": 1,
            "default_value": 0.0
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
        "instObjGroups": {
            "short_name": "iog",
            "long_name": "instObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
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
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
            "parent_plug": "inverseScale",
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
            "parent_plug": "inverseScale",
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
            "parent_plug": "inverseScale",
            "numeric_type": 14,
            "default_value": 1.0
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
        "jointOrientType": {
            "short_name": "jot",
            "long_name": "jointOrientType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "jointOrientX": {
            "short_name": "jox",
            "long_name": "jointOrientX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "jointOrient",
            "unit_type": 1,
            "default_value": 0.0
        },
        "jointOrientY": {
            "short_name": "joy",
            "long_name": "jointOrientY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "jointOrient",
            "unit_type": 1,
            "default_value": 0.0
        },
        "jointOrientZ": {
            "short_name": "joz",
            "long_name": "jointOrientZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "jointOrient",
            "unit_type": 1,
            "default_value": 0.0
        },
        "jointType": {
            "short_name": "jt",
            "long_name": "jointType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 2,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 1,
            "default_value": True
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
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
        "maxRotXLimit": {
            "short_name": "xrxl",
            "long_name": "maxRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotLimit",
            "unit_type": 1,
            "default_value": 0.7853981633974483
        },
        "maxRotXLimitEnable": {
            "short_name": "xrxe",
            "long_name": "maxRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotYLimit": {
            "short_name": "xryl",
            "long_name": "maxRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotLimit",
            "unit_type": 1,
            "default_value": 0.7853981633974483
        },
        "maxRotYLimitEnable": {
            "short_name": "xrye",
            "long_name": "maxRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxRotZLimit": {
            "short_name": "xrzl",
            "long_name": "maxRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotLimit",
            "unit_type": 1,
            "default_value": 0.7853981633974483
        },
        "maxRotZLimitEnable": {
            "short_name": "xrze",
            "long_name": "maxRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotateDampRange",
            "unit_type": 1,
            "default_value": 0.0
        },
        "maxRotateDampRangeY": {
            "short_name": "xdy",
            "long_name": "maxRotateDampRangeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotateDampRange",
            "unit_type": 1,
            "default_value": 0.0
        },
        "maxRotateDampRangeZ": {
            "short_name": "xdz",
            "long_name": "maxRotateDampRangeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "maxRotateDampRange",
            "unit_type": 1,
            "default_value": 0.0
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
            "parent_plug": "maxRotateDampStrength",
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
            "parent_plug": "maxRotateDampStrength",
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
            "parent_plug": "maxRotateDampStrength",
            "numeric_type": 14,
            "default_value": 0.0
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
        "maxScaleXLimit": {
            "short_name": "xsxl",
            "long_name": "maxScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimit",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleXLimitEnable": {
            "short_name": "xsxe",
            "long_name": "maxScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleYLimit": {
            "short_name": "xsyl",
            "long_name": "maxScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimit",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleYLimitEnable": {
            "short_name": "xsye",
            "long_name": "maxScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxScaleZLimit": {
            "short_name": "xszl",
            "long_name": "maxScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimit",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "maxScaleZLimitEnable": {
            "short_name": "xsze",
            "long_name": "maxScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "maxTransXLimit": {
            "short_name": "xtxl",
            "long_name": "maxTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "maxTransLimit",
            "unit_type": 2,
            "default_value": 1.0
        },
        "maxTransXLimitEnable": {
            "short_name": "xtxe",
            "long_name": "maxTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransYLimit": {
            "short_name": "xtyl",
            "long_name": "maxTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "maxTransLimit",
            "unit_type": 2,
            "default_value": 1.0
        },
        "maxTransYLimitEnable": {
            "short_name": "xtye",
            "long_name": "maxTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "maxTransZLimit": {
            "short_name": "xtzl",
            "long_name": "maxTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "maxTransLimit",
            "unit_type": 2,
            "default_value": 1.0
        },
        "maxTransZLimitEnable": {
            "short_name": "xtze",
            "long_name": "maxTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "maxTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "minRotXLimit": {
            "short_name": "mrxl",
            "long_name": "minRotXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotLimit",
            "unit_type": 1,
            "default_value": -0.7853981633974483
        },
        "minRotXLimitEnable": {
            "short_name": "mrxe",
            "long_name": "minRotXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotYLimit": {
            "short_name": "mryl",
            "long_name": "minRotYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotLimit",
            "unit_type": 1,
            "default_value": -0.7853981633974483
        },
        "minRotYLimitEnable": {
            "short_name": "mrye",
            "long_name": "minRotYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minRotZLimit": {
            "short_name": "mrzl",
            "long_name": "minRotZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotLimit",
            "unit_type": 1,
            "default_value": -0.7853981633974483
        },
        "minRotZLimitEnable": {
            "short_name": "mrze",
            "long_name": "minRotZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minRotLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotateDampRange",
            "unit_type": 1,
            "default_value": 0.0
        },
        "minRotateDampRangeY": {
            "short_name": "ndy",
            "long_name": "minRotateDampRangeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotateDampRange",
            "unit_type": 1,
            "default_value": 0.0
        },
        "minRotateDampRangeZ": {
            "short_name": "ndz",
            "long_name": "minRotateDampRangeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "minRotateDampRange",
            "unit_type": 1,
            "default_value": 0.0
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
            "parent_plug": "minRotateDampStrength",
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
            "parent_plug": "minRotateDampStrength",
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
            "parent_plug": "minRotateDampStrength",
            "numeric_type": 14,
            "default_value": 0.0
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
        "minScaleXLimit": {
            "short_name": "msxl",
            "long_name": "minScaleXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimit",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleXLimitEnable": {
            "short_name": "msxe",
            "long_name": "minScaleXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleYLimit": {
            "short_name": "msyl",
            "long_name": "minScaleYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimit",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleYLimitEnable": {
            "short_name": "msye",
            "long_name": "minScaleYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minScaleZLimit": {
            "short_name": "mszl",
            "long_name": "minScaleZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimit",
            "numeric_type": 14,
            "default_value": -1.0
        },
        "minScaleZLimitEnable": {
            "short_name": "msze",
            "long_name": "minScaleZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minScaleLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "minTransXLimit": {
            "short_name": "mtxl",
            "long_name": "minTransXLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "minTransLimit",
            "unit_type": 2,
            "default_value": -1.0
        },
        "minTransXLimitEnable": {
            "short_name": "mtxe",
            "long_name": "minTransXLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransYLimit": {
            "short_name": "mtyl",
            "long_name": "minTransYLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "minTransLimit",
            "unit_type": 2,
            "default_value": -1.0
        },
        "minTransYLimitEnable": {
            "short_name": "mtye",
            "long_name": "minTransYLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
        },
        "minTransZLimit": {
            "short_name": "mtzl",
            "long_name": "minTransZLimit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "minTransLimit",
            "unit_type": 2,
            "default_value": -1.0
        },
        "minTransZLimitEnable": {
            "short_name": "mtze",
            "long_name": "minTransZLimitEnable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minTransLimitEnable",
            "numeric_type": 1,
            "default_value": False
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
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
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
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
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
        "offsetParentMatrix": {
            "short_name": "opm",
            "long_name": "offsetParentMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "otherType": {
            "short_name": "otp",
            "long_name": "otherType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
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
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
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
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "parent_plug": "drawOverride",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
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
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "preferredAngle",
            "unit_type": 1,
            "default_value": 0.0
        },
        "preferredAngleY": {
            "short_name": "pay",
            "long_name": "preferredAngleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "preferredAngle",
            "unit_type": 1,
            "default_value": 0.0
        },
        "preferredAngleZ": {
            "short_name": "paz",
            "long_name": "preferredAngleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "preferredAngle",
            "unit_type": 1,
            "default_value": 0.0
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
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
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
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateAxisY": {
            "short_name": "ray",
            "long_name": "rotateAxisY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateAxisZ": {
            "short_name": "raz",
            "long_name": "rotateAxisZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotateAxis",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateOrder": {
            "short_name": "ro",
            "long_name": "rotateOrder",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotTranslateY": {
            "short_name": "rpty",
            "long_name": "rotatePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotTranslateZ": {
            "short_name": "rptz",
            "long_name": "rotatePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotX": {
            "short_name": "rpx",
            "long_name": "rotatePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotY": {
            "short_name": "rpy",
            "long_name": "rotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "rotatePivotZ": {
            "short_name": "rpz",
            "long_name": "rotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "rotatePivot",
            "unit_type": 2,
            "default_value": 0.0
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
        "rotateQuaternionW": {
            "short_name": "rqw",
            "long_name": "rotateQuaternionW",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "rotateQuaternion",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateQuaternionX": {
            "short_name": "rqx",
            "long_name": "rotateQuaternionX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "rotateQuaternion",
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
            "parent_plug": "rotateQuaternion",
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
            "parent_plug": "rotateQuaternion",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "rotateX": {
            "short_name": "rx",
            "long_name": "rotateX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateY": {
            "short_name": "ry",
            "long_name": "rotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "rotateZ": {
            "short_name": "rz",
            "long_name": "rotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "rotate",
            "unit_type": 1,
            "default_value": 0.0
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotTranslateY": {
            "short_name": "spty",
            "long_name": "scalePivotTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotTranslateZ": {
            "short_name": "sptz",
            "long_name": "scalePivotTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivotTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotX": {
            "short_name": "spx",
            "long_name": "scalePivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotY": {
            "short_name": "spy",
            "long_name": "scalePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scalePivotZ": {
            "short_name": "spz",
            "long_name": "scalePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "scalePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "scaleX": {
            "short_name": "sx",
            "long_name": "scaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "scale",
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
            "parent_plug": "scale",
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
            "parent_plug": "scale",
            "numeric_type": 14,
            "default_value": 1.0
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "selectHandle",
            "unit_type": 2,
            "default_value": 0.0
        },
        "selectHandleY": {
            "short_name": "hdly",
            "long_name": "selectHandleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "selectHandle",
            "unit_type": 2,
            "default_value": 0.0
        },
        "selectHandleZ": {
            "short_name": "hdlz",
            "long_name": "selectHandleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "selectHandle",
            "unit_type": 2,
            "default_value": 0.0
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
            "parent_plug": "shear",
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
            "parent_plug": "shear",
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
            "parent_plug": "shear",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "showManipDefault": {
            "short_name": "smd",
            "long_name": "showManipDefault",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "side": {
            "short_name": "sd",
            "long_name": "side",
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
            "type_str": "kTypedAttribute",
            "typed_type": 24
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
            "parent_plug": "stiffness",
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
            "parent_plug": "stiffness",
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
            "parent_plug": "stiffness",
            "numeric_type": 14,
            "default_value": 0.0
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
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "transMinusRotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "transMinusRotatePivotY": {
            "short_name": "tmry",
            "long_name": "transMinusRotatePivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "transMinusRotatePivot",
            "unit_type": 2,
            "default_value": 0.0
        },
        "transMinusRotatePivotZ": {
            "short_name": "tmrz",
            "long_name": "transMinusRotatePivotZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "transMinusRotatePivot",
            "unit_type": 2,
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "translate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "translateY": {
            "short_name": "ty",
            "long_name": "translateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "translate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "translateZ": {
            "short_name": "tz",
            "long_name": "translateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "translate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "type": {
            "short_name": "typ",
            "long_name": "type",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "useObjectColor": {
            "short_name": "uoc",
            "long_name": "useObjectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
            "parent_plug": "wireColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "xformMatrix": {
            "short_name": "xm",
            "long_name": "xformMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
        }
    },
    "multDoubleLinear": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "input1": {
            "short_name": "i1",
            "long_name": "input1",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "unit_type": 2,
            "default_value": 0.0
        },
        "input2": {
            "short_name": "i2",
            "long_name": "input2",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "unit_type": 2,
            "default_value": 0.0
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "output": {
            "short_name": "o",
            "long_name": "output",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "unit_type": 2,
            "default_value": 0.0
        }
    },
    "condition": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "colorIfFalseB": {
            "short_name": "cfb",
            "long_name": "colorIfFalseB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "colorIfFalse",
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
            "parent_plug": "colorIfFalse",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "colorIfFalseR": {
            "short_name": "cfr",
            "long_name": "colorIfFalseR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "colorIfFalse",
            "numeric_type": 11,
            "default_value": 1.0
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
        "colorIfTrueB": {
            "short_name": "ctb",
            "long_name": "colorIfTrueB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "colorIfTrue",
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
            "parent_plug": "colorIfTrue",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "colorIfTrueR": {
            "short_name": "ctr",
            "long_name": "colorIfTrueR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "colorIfTrue",
            "numeric_type": 11,
            "default_value": 0.0
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "operation": {
            "short_name": "op",
            "long_name": "operation",
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
        "outColorB": {
            "short_name": "ocb",
            "long_name": "outColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outColor",
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
            "parent_plug": "outColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorR": {
            "short_name": "ocr",
            "long_name": "outColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outColor",
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
        }
    },
    "clamp": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "inputB": {
            "short_name": "ipb",
            "long_name": "inputB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "input",
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
            "parent_plug": "input",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "inputR": {
            "short_name": "ipr",
            "long_name": "inputR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "input",
            "numeric_type": 11,
            "default_value": 0.0
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
        "maxB": {
            "short_name": "mxb",
            "long_name": "maxB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "max",
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
            "parent_plug": "max",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "maxR": {
            "short_name": "mxr",
            "long_name": "maxR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "max",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "minB": {
            "short_name": "mnb",
            "long_name": "minB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "min",
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
            "parent_plug": "min",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "minR": {
            "short_name": "mnr",
            "long_name": "minR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "min",
            "numeric_type": 11,
            "default_value": 0.0
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
        "outputB": {
            "short_name": "opb",
            "long_name": "outputB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "output",
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
            "parent_plug": "output",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputR": {
            "short_name": "opr",
            "long_name": "outputR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "output",
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
        }
    },
    "remapValue": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "color": {
            "short_name": "cl",
            "long_name": "color",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "outColorB": {
            "short_name": "ocb",
            "long_name": "outColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outColor",
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
            "parent_plug": "outColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorR": {
            "short_name": "ocr",
            "long_name": "outColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outColor",
            "numeric_type": 11,
            "default_value": 0.0
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
        "value": {
            "short_name": "vl",
            "long_name": "value",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        }
    },
    "remapColor": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "colorB": {
            "short_name": "cb",
            "long_name": "colorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color",
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
            "parent_plug": "color",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "colorR": {
            "short_name": "cr",
            "long_name": "colorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color",
            "numeric_type": 11,
            "default_value": 0.5
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
        "green": {
            "short_name": "g",
            "long_name": "green",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "outColorB": {
            "short_name": "ocb",
            "long_name": "outColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outColor",
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
            "parent_plug": "outColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outColorR": {
            "short_name": "ocr",
            "long_name": "outColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outColor",
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
        "red": {
            "short_name": "r",
            "long_name": "red",
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
        }
    },
    "uvPin": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "cacheSetup": {
            "short_name": "csp",
            "long_name": "cacheSetup",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kOpaqueAttribute"
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
        "coordinate": {
            "short_name": "coord",
            "long_name": "coordinate",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_elements": 0
        },
        "deformedGeometry": {
            "short_name": "curgeom",
            "long_name": "deformedGeometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "normalAxis": {
            "short_name": "nrm",
            "long_name": "normalAxis",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "normalOverride": {
            "short_name": "novr",
            "long_name": "normalOverride",
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
        "originalGeometry": {
            "short_name": "orggeom",
            "long_name": "originalGeometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
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
        "outputTranslate": {
            "short_name": "ot",
            "long_name": "outputTranslate",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "railCurve": {
            "short_name": "rlcrv",
            "long_name": "railCurve",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
        },
        "relativeSpaceMatrix": {
            "short_name": "rsmat",
            "long_name": "relativeSpaceMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "relativeSpaceMode": {
            "short_name": "rsmd",
            "long_name": "relativeSpaceMode",
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
        "uvSetName": {
            "short_name": "msn",
            "long_name": "uvSetName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        }
    },
    "plusMinusAverage": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "operation": {
            "short_name": "op",
            "long_name": "operation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
            "parent_plug": "output2D",
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
            "parent_plug": "output2D",
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
            "parent_plug": "output3D",
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
            "parent_plug": "output3D",
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
            "parent_plug": "output3D",
            "numeric_type": 11,
            "default_value": 0.0
        }
    },
    "blendTwoAttr": {
        "attributesBlender": {
            "short_name": "ab",
            "long_name": "attributesBlender",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        }
    },
    "blendColors": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "color1B": {
            "short_name": "c1b",
            "long_name": "color1B",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color1",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color1G": {
            "short_name": "c1g",
            "long_name": "color1G",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color1",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color1R": {
            "short_name": "c1r",
            "long_name": "color1R",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color1",
            "numeric_type": 11,
            "default_value": 1.0
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
        "color2B": {
            "short_name": "c2b",
            "long_name": "color2B",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color2",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "color2G": {
            "short_name": "c2g",
            "long_name": "color2G",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color2",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "color2R": {
            "short_name": "c2r",
            "long_name": "color2R",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "color2",
            "numeric_type": 11,
            "default_value": 0.0
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "outputB": {
            "short_name": "opb",
            "long_name": "outputB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "output",
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
            "parent_plug": "output",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outputR": {
            "short_name": "opr",
            "long_name": "outputR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "output",
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
        }
    },
    "decomposeMatrix": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "outputQuatW": {
            "short_name": "oqw",
            "long_name": "outputQuatW",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outputQuat",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "outputQuatX": {
            "short_name": "oqx",
            "long_name": "outputQuatX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outputQuat",
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
            "parent_plug": "outputQuat",
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
            "parent_plug": "outputQuat",
            "numeric_type": 14,
            "default_value": 0.0
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
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "outputRotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "outputRotateY": {
            "short_name": "ory",
            "long_name": "outputRotateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "outputRotate",
            "unit_type": 1,
            "default_value": 0.0
        },
        "outputRotateZ": {
            "short_name": "orz",
            "long_name": "outputRotateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "parent_plug": "outputRotate",
            "unit_type": 1,
            "default_value": 0.0
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
            "parent_plug": "outputScale",
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
            "parent_plug": "outputScale",
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
            "parent_plug": "outputScale",
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
            "parent_plug": "outputShear",
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
            "parent_plug": "outputShear",
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
            "parent_plug": "outputShear",
            "numeric_type": 14,
            "default_value": 0.0
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "outputTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "outputTranslateY": {
            "short_name": "oty",
            "long_name": "outputTranslateY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "outputTranslate",
            "unit_type": 2,
            "default_value": 0.0
        },
        "outputTranslateZ": {
            "short_name": "otz",
            "long_name": "outputTranslateZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "outputTranslate",
            "unit_type": 2,
            "default_value": 0.0
        }
    },
    "inverseMatrix": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "inputMatrix": {
            "short_name": "imat",
            "long_name": "inputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
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
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        }
    },
    "blendMatrix": {
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "inputMatrix": {
            "short_name": "imat",
            "long_name": "inputMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
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
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "outputMatrix": {
            "short_name": "omat",
            "long_name": "outputMatrix",
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
        "preSpaceMatrix": {
            "short_name": "premat",
            "long_name": "preSpaceMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMatrixAttribute"
        },
        "target": {
            "short_name": "tgt",
            "long_name": "target",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        }
    },
    "nurbsCurve": {
        "alwaysDrawOnTop": {
            "short_name": "adot",
            "long_name": "alwaysDrawOnTop",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "antialiasingLevel": {
            "short_name": "gal",
            "long_name": "antialiasingLevel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "asBackground": {
            "short_name": "asbg",
            "long_name": "asBackground",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "blindDataNodes": {
            "short_name": "bn",
            "long_name": "blindDataNodes",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
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
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "cached": {
            "short_name": "cc",
            "long_name": "cached",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 16
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
        "castsShadows": {
            "short_name": "csh",
            "long_name": "castsShadows",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "colorSet": {
            "short_name": "clst",
            "long_name": "colorSet",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "compInstObjGroups": {
            "short_name": "ciog",
            "long_name": "compInstObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "componentTags": {
            "short_name": "gtag",
            "long_name": "componentTags",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "controlPoints": {
            "short_name": "cp",
            "long_name": "controlPoints",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "create": {
            "short_name": "cr",
            "long_name": "create",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 16
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "currentColorSet": {
            "short_name": "ccls",
            "long_name": "currentColorSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "currentUVSet": {
            "short_name": "cuvs",
            "long_name": "currentUVSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "degree": {
            "short_name": "d",
            "long_name": "degree",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "depthJitter": {
            "short_name": "dej",
            "long_name": "depthJitter",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispCV": {
            "short_name": "dcv",
            "long_name": "dispCV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispCurveEndPoints": {
            "short_name": "dce",
            "long_name": "dispCurveEndPoints",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispEP": {
            "short_name": "dep",
            "long_name": "dispEP",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispGeometry": {
            "short_name": "dg",
            "long_name": "dispGeometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "dispHull": {
            "short_name": "dh",
            "long_name": "dispHull",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayColorChannel": {
            "short_name": "dcc",
            "long_name": "displayColorChannel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "displayColors": {
            "short_name": "dcol",
            "long_name": "displayColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayImmediate": {
            "short_name": "di",
            "long_name": "displayImmediate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
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
        "editPoints": {
            "short_name": "eps",
            "long_name": "editPoints",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "form": {
            "short_name": "f",
            "long_name": "form",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "geometryAntialiasingOverride": {
            "short_name": "gao",
            "long_name": "geometryAntialiasingOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
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
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.878000020980835
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
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
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
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 9
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.5
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
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
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
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 1
        },
        "hardwareFogMultiplier": {
            "short_name": "hfm",
            "long_name": "hardwareFogMultiplier",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "header": {
            "short_name": "hd",
            "long_name": "header",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
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
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 4,
            "default_value": 0
        },
        "ignoreSelfShadowing": {
            "short_name": "iss",
            "long_name": "ignoreSelfShadowing",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "inPlace": {
            "short_name": "ipo",
            "long_name": "inPlace",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "instMaterialAssign": {
            "short_name": "imtla",
            "long_name": "instMaterialAssign",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
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
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 2,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 1,
            "default_value": True
        },
        "lineWidth": {
            "short_name": "ls",
            "long_name": "lineWidth",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": -1.0
        },
        "local": {
            "short_name": "l",
            "long_name": "local",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 16
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
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
        },
        "maxShadingSamples": {
            "short_name": "msa",
            "long_name": "maxShadingSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "maxValue": {
            "short_name": "max",
            "long_name": "maxValue",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minMaxValue",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "maxVisibilitySamples": {
            "short_name": "mvs",
            "long_name": "maxVisibilitySamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "maxVisibilitySamplesOverride": {
            "short_name": "vbo",
            "long_name": "maxVisibilitySamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "minMaxValue": {
            "short_name": "mmv",
            "long_name": "minMaxValue",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_children": 2,
            "children": [
                "minValue",
                "maxValue"
            ]
        },
        "minValue": {
            "short_name": "min",
            "long_name": "minValue",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minMaxValue",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "motionBlur": {
            "short_name": "mb",
            "long_name": "motionBlur",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
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
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
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
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
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
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
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
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "parent_plug": "drawOverride",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
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
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "pickTexture": {
            "short_name": "pte",
            "long_name": "pickTexture",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "primaryVisibility": {
            "short_name": "vis",
            "long_name": "primaryVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "receiveShadows": {
            "short_name": "rcsh",
            "long_name": "receiveShadows",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "referenceObject": {
            "short_name": "rob",
            "long_name": "referenceObject",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "relativeTweak": {
            "short_name": "rtw",
            "long_name": "relativeTweak",
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
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "renderType": {
            "short_name": "rt",
            "long_name": "renderType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "renderVolume": {
            "short_name": "rv",
            "long_name": "renderVolume",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "rmbCommand": {
            "short_name": "rmc",
            "long_name": "rmbCommand",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "shadingSamples": {
            "short_name": "ssa",
            "long_name": "shadingSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "shadingSamplesOverride": {
            "short_name": "sso",
            "long_name": "shadingSamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "spans": {
            "short_name": "s",
            "long_name": "spans",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
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
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "tweak": {
            "short_name": "tw",
            "long_name": "tweak",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "tweakLocation": {
            "short_name": "twl",
            "long_name": "tweakLocation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 24
        },
        "tweakSize": {
            "short_name": "ts",
            "long_name": "tweakSize",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": -1
        },
        "useObjectColor": {
            "short_name": "uoc",
            "long_name": "useObjectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "uvPivot": {
            "short_name": "pv",
            "long_name": "uvPivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_children": 2,
            "children": [
                "uvPivotX",
                "uvPivotY"
            ]
        },
        "uvPivotX": {
            "short_name": "pvx",
            "long_name": "uvPivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "uvPivot",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "uvPivotY": {
            "short_name": "pvy",
            "long_name": "uvPivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "uvPivot",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "uvSet": {
            "short_name": "uvst",
            "long_name": "uvSet",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "visibleFraction": {
            "short_name": "vf",
            "long_name": "visibleFraction",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "visibleInReflections": {
            "short_name": "vir",
            "long_name": "visibleInReflections",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "visibleInRefractions": {
            "short_name": "vif",
            "long_name": "visibleInRefractions",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "volumeSamples": {
            "short_name": "vss",
            "long_name": "volumeSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "volumeSamplesOverride": {
            "short_name": "vso",
            "long_name": "volumeSamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "weights": {
            "short_name": "wt",
            "long_name": "weights",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 14,
            "default_value": 1.0
        },
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
            "parent_plug": "wireColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldNormal": {
            "short_name": "wn",
            "long_name": "worldNormal",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "worldSpace": {
            "short_name": "ws",
            "long_name": "worldSpace",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 16
        }
    },
    "nurbsSurface": {
        "antialiasingLevel": {
            "short_name": "gal",
            "long_name": "antialiasingLevel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "asBackground": {
            "short_name": "asbg",
            "long_name": "asBackground",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "basicTessellationType": {
            "short_name": "btt",
            "long_name": "basicTessellationType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "blindDataNodes": {
            "short_name": "bn",
            "long_name": "blindDataNodes",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
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
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxScale": {
            "short_name": "bbs",
            "long_name": "boundingBoxScale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "boundingBoxScaleX",
                "boundingBoxScaleY",
                "boundingBoxScaleZ"
            ]
        },
        "boundingBoxScaleX": {
            "short_name": "bscx",
            "long_name": "boundingBoxScaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "boundingBoxScale",
            "numeric_type": 11,
            "default_value": 1.5
        },
        "boundingBoxScaleY": {
            "short_name": "bscy",
            "long_name": "boundingBoxScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "boundingBoxScale",
            "numeric_type": 11,
            "default_value": 1.5
        },
        "boundingBoxScaleZ": {
            "short_name": "bscz",
            "long_name": "boundingBoxScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "boundingBoxScale",
            "numeric_type": 11,
            "default_value": 1.5
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "cached": {
            "short_name": "cc",
            "long_name": "cached",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 17
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
        "castsShadows": {
            "short_name": "csh",
            "long_name": "castsShadows",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "chordHeight": {
            "short_name": "ch",
            "long_name": "chordHeight",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.1
        },
        "chordHeightRatio": {
            "short_name": "chr",
            "long_name": "chordHeightRatio",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.983
        },
        "collisionDepthVelocityIncrement": {
            "short_name": "cdvi",
            "long_name": "collisionDepthVelocityIncrement",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "collisionDepthVelocityMultiplier": {
            "short_name": "cdvm",
            "long_name": "collisionDepthVelocityMultiplier",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 1
        },
        "collisionOffsetVelocityIncrement": {
            "short_name": "covi",
            "long_name": "collisionOffsetVelocityIncrement",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "collisionOffsetVelocityMultiplier": {
            "short_name": "covm",
            "long_name": "collisionOffsetVelocityMultiplier",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 1
        },
        "colorSet": {
            "short_name": "clst",
            "long_name": "colorSet",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "compInstObjGroups": {
            "short_name": "ciog",
            "long_name": "compInstObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "componentTags": {
            "short_name": "gtag",
            "long_name": "componentTags",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "controlPoints": {
            "short_name": "cp",
            "long_name": "controlPoints",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "create": {
            "short_name": "cr",
            "long_name": "create",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 17
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "currentColorSet": {
            "short_name": "ccls",
            "long_name": "currentColorSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "currentUVSet": {
            "short_name": "cuvs",
            "long_name": "currentUVSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "curvatureTolerance": {
            "short_name": "cvto",
            "long_name": "curvatureTolerance",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "curvePrecision": {
            "short_name": "cpr",
            "long_name": "curvePrecision",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 4
        },
        "curvePrecisionShaded": {
            "short_name": "cps",
            "long_name": "curvePrecisionShaded",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 1
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "degreeU": {
            "short_name": "du",
            "long_name": "degreeU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "degreeUV",
            "numeric_type": 4,
            "default_value": 0
        },
        "degreeUV": {
            "short_name": "d",
            "long_name": "degreeUV",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Short",
            "num_children": 2,
            "children": [
                "degreeU",
                "degreeV"
            ]
        },
        "degreeV": {
            "short_name": "dv",
            "long_name": "degreeV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "degreeUV",
            "numeric_type": 4,
            "default_value": 0
        },
        "depthJitter": {
            "short_name": "dej",
            "long_name": "depthJitter",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispCV": {
            "short_name": "dcv",
            "long_name": "dispCV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispEP": {
            "short_name": "dep",
            "long_name": "dispEP",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispGeometry": {
            "short_name": "dg",
            "long_name": "dispGeometry",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "dispHull": {
            "short_name": "dh",
            "long_name": "dispHull",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispOrigin": {
            "short_name": "dor",
            "long_name": "dispOrigin",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispSF": {
            "short_name": "dsf",
            "long_name": "dispSF",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayColorChannel": {
            "short_name": "dcc",
            "long_name": "displayColorChannel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "displayColors": {
            "short_name": "dcol",
            "long_name": "displayColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayHWEnvironment": {
            "short_name": "dhe",
            "long_name": "displayHWEnvironment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayImmediate": {
            "short_name": "di",
            "long_name": "displayImmediate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayRenderTessellation": {
            "short_name": "drt",
            "long_name": "displayRenderTessellation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "divisionsU": {
            "short_name": "dvu",
            "long_name": "divisionsU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "divisionsV": {
            "short_name": "dvv",
            "long_name": "divisionsV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "doubleSided": {
            "short_name": "ds",
            "long_name": "doubleSided",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "edgeSwap": {
            "short_name": "es",
            "long_name": "edgeSwap",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "explicitTessellationAttributes": {
            "short_name": "eta",
            "long_name": "explicitTessellationAttributes",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "extraSampleRate": {
            "short_name": "xsr",
            "long_name": "extraSampleRate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 5
        },
        "featureDisplacement": {
            "short_name": "fbda",
            "long_name": "featureDisplacement",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "fixTextureWarp": {
            "short_name": "ftwp",
            "long_name": "fixTextureWarp",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "formU": {
            "short_name": "fu",
            "long_name": "formU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "formV": {
            "short_name": "fv",
            "long_name": "formV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "geometryAntialiasingOverride": {
            "short_name": "gao",
            "long_name": "geometryAntialiasingOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
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
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.878000020980835
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
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
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
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 9
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.5
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
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
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
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 1
        },
        "gridDivisionPerSpanU": {
            "short_name": "gdsu",
            "long_name": "gridDivisionPerSpanU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 4
        },
        "gridDivisionPerSpanV": {
            "short_name": "gdsv",
            "long_name": "gridDivisionPerSpanV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 4
        },
        "hardwareFogMultiplier": {
            "short_name": "hfm",
            "long_name": "hardwareFogMultiplier",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "header": {
            "short_name": "hd",
            "long_name": "header",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
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
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "holdOut": {
            "short_name": "hot",
            "long_name": "holdOut",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 4,
            "default_value": 0
        },
        "ignoreHwShader": {
            "short_name": "ih",
            "long_name": "ignoreHwShader",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "ignoreSelfShadowing": {
            "short_name": "iss",
            "long_name": "ignoreSelfShadowing",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "inPlace": {
            "short_name": "ipo",
            "long_name": "inPlace",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "initialSampleRate": {
            "short_name": "dsr",
            "long_name": "initialSampleRate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 6
        },
        "instMaterialAssign": {
            "short_name": "imtla",
            "long_name": "instMaterialAssign",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
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
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 2,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 1,
            "default_value": True
        },
        "local": {
            "short_name": "l",
            "long_name": "local",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 17
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
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
        },
        "maxShadingSamples": {
            "short_name": "msa",
            "long_name": "maxShadingSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "maxValueU": {
            "short_name": "mxu",
            "long_name": "maxValueU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minMaxRangeU",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "maxValueV": {
            "short_name": "mxv",
            "long_name": "maxValueV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minMaxRangeV",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "maxVisibilitySamples": {
            "short_name": "mvs",
            "long_name": "maxVisibilitySamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "maxVisibilitySamplesOverride": {
            "short_name": "vbo",
            "long_name": "maxVisibilitySamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "minMaxRangeU": {
            "short_name": "mmu",
            "long_name": "minMaxRangeU",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_children": 2,
            "children": [
                "minValueU",
                "maxValueU"
            ]
        },
        "minMaxRangeV": {
            "short_name": "mmv",
            "long_name": "minMaxRangeV",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_children": 2,
            "children": [
                "minValueV",
                "maxValueV"
            ]
        },
        "minScreen": {
            "short_name": "mns",
            "long_name": "minScreen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 14.0
        },
        "minValueU": {
            "short_name": "mnu",
            "long_name": "minValueU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minMaxRangeU",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "minValueV": {
            "short_name": "mnv",
            "long_name": "minValueV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "minMaxRangeV",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "motionBlur": {
            "short_name": "mb",
            "long_name": "motionBlur",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "normalThreshold": {
            "short_name": "nat",
            "long_name": "normalThreshold",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 30.0
        },
        "normalsDisplayScale": {
            "short_name": "ndf",
            "long_name": "normalsDisplayScale",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.0
        },
        "numberU": {
            "short_name": "nu",
            "long_name": "numberU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 3
        },
        "numberV": {
            "short_name": "nv",
            "long_name": "numberV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 3
        },
        "objSpaceChordHeight": {
            "short_name": "uco",
            "long_name": "objSpaceChordHeight",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
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
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
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
        "opposite": {
            "short_name": "op",
            "long_name": "opposite",
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
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
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
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
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
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "parent_plug": "drawOverride",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
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
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "patchUVIds": {
            "short_name": "pu",
            "long_name": "patchUVIds",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 0
        },
        "pickTexture": {
            "short_name": "pte",
            "long_name": "pickTexture",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "primaryVisibility": {
            "short_name": "vis",
            "long_name": "primaryVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "receiveShadows": {
            "short_name": "rcsh",
            "long_name": "receiveShadows",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "referenceObject": {
            "short_name": "rob",
            "long_name": "referenceObject",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "relativeTweak": {
            "short_name": "rtw",
            "long_name": "relativeTweak",
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
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "renderTriangleCount": {
            "short_name": "tcn",
            "long_name": "renderTriangleCount",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "renderType": {
            "short_name": "rt",
            "long_name": "renderType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "renderVolume": {
            "short_name": "rv",
            "long_name": "renderVolume",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "rmbCommand": {
            "short_name": "rmc",
            "long_name": "rmbCommand",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "selCVDisp": {
            "short_name": "scvd",
            "long_name": "selCVDisp",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
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
        "shadingSamples": {
            "short_name": "ssa",
            "long_name": "shadingSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "shadingSamplesOverride": {
            "short_name": "sso",
            "long_name": "shadingSamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "simplifyMode": {
            "short_name": "sm",
            "long_name": "simplifyMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 0
        },
        "simplifyU": {
            "short_name": "smu",
            "long_name": "simplifyU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 1
        },
        "simplifyV": {
            "short_name": "smv",
            "long_name": "simplifyV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 2,
            "default_value": 1
        },
        "smoothEdge": {
            "short_name": "ues",
            "long_name": "smoothEdge",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "smoothEdgeRatio": {
            "short_name": "esr",
            "long_name": "smoothEdgeRatio",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.99
        },
        "smoothShading": {
            "short_name": "smo",
            "long_name": "smoothShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "spansU": {
            "short_name": "su",
            "long_name": "spansU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "spansUV",
            "numeric_type": 7,
            "default_value": 0
        },
        "spansUV": {
            "short_name": "sp",
            "long_name": "spansUV",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Long",
            "num_children": 2,
            "children": [
                "spansU",
                "spansV"
            ]
        },
        "spansV": {
            "short_name": "sv",
            "long_name": "spansV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "spansUV",
            "numeric_type": 7,
            "default_value": 0
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
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "textureThreshold": {
            "short_name": "fth",
            "long_name": "textureThreshold",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "trimFace": {
            "short_name": "tf",
            "long_name": "trimFace",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 0
        },
        "tweak": {
            "short_name": "tw",
            "long_name": "tweak",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "tweakLocation": {
            "short_name": "twl",
            "long_name": "tweakLocation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 24
        },
        "tweakSizeU": {
            "short_name": "tsu",
            "long_name": "tweakSizeU",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": -1
        },
        "tweakSizeV": {
            "short_name": "tsv",
            "long_name": "tweakSizeV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": -1
        },
        "uDivisionsFactor": {
            "short_name": "nufa",
            "long_name": "uDivisionsFactor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.5
        },
        "useChordHeight": {
            "short_name": "uch",
            "long_name": "useChordHeight",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useChordHeightRatio": {
            "short_name": "ucr",
            "long_name": "useChordHeightRatio",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "useMinScreen": {
            "short_name": "uns",
            "long_name": "useMinScreen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useObjectColor": {
            "short_name": "uoc",
            "long_name": "useObjectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "uvPivot": {
            "short_name": "pv",
            "long_name": "uvPivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_children": 2,
            "children": [
                "uvPivotX",
                "uvPivotY"
            ]
        },
        "uvPivotX": {
            "short_name": "pvx",
            "long_name": "uvPivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "uvPivot",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "uvPivotY": {
            "short_name": "pvy",
            "long_name": "uvPivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "uvPivot",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "uvSet": {
            "short_name": "uvst",
            "long_name": "uvSet",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "vDivisionsFactor": {
            "short_name": "nvfa",
            "long_name": "vDivisionsFactor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 1.5
        },
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "visibleFraction": {
            "short_name": "vf",
            "long_name": "visibleFraction",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "visibleInReflections": {
            "short_name": "vir",
            "long_name": "visibleInReflections",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "visibleInRefractions": {
            "short_name": "vif",
            "long_name": "visibleInRefractions",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "volumeSamples": {
            "short_name": "vss",
            "long_name": "volumeSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "volumeSamplesOverride": {
            "short_name": "vso",
            "long_name": "volumeSamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "weights": {
            "short_name": "wt",
            "long_name": "weights",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 14,
            "default_value": 1.0
        },
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
            "parent_plug": "wireColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldSpace": {
            "short_name": "ws",
            "long_name": "worldSpace",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 17
        }
    },
    "mesh": {
        "allowTopologyMod": {
            "short_name": "atm",
            "long_name": "allowTopologyMod",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "alwaysDrawOnTop": {
            "short_name": "adot",
            "long_name": "alwaysDrawOnTop",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "antialiasingLevel": {
            "short_name": "gal",
            "long_name": "antialiasingLevel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "asBackground": {
            "short_name": "asbg",
            "long_name": "asBackground",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "backfaceCulling": {
            "short_name": "bck",
            "long_name": "backfaceCulling",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "binMembership": {
            "short_name": "bnm",
            "long_name": "binMembership",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "blindDataNodes": {
            "short_name": "bn",
            "long_name": "blindDataNodes",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
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
        "borderWidth": {
            "short_name": "bw",
            "long_name": "borderWidth",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 2.0
        },
        "boundaryRule": {
            "short_name": "bnr",
            "long_name": "boundaryRule",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "boundingBoxCenterX": {
            "short_name": "bcx",
            "long_name": "boundingBoxCenterX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterY": {
            "short_name": "bcy",
            "long_name": "boundingBoxCenterY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxCenterZ": {
            "short_name": "bcz",
            "long_name": "boundingBoxCenterZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "center",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMax": {
            "short_name": "bbmx",
            "long_name": "boundingBoxMax",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxY": {
            "short_name": "bbxy",
            "long_name": "boundingBoxMaxY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMaxZ": {
            "short_name": "bbxz",
            "long_name": "boundingBoxMaxZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMax",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMin": {
            "short_name": "bbmn",
            "long_name": "boundingBoxMin",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinY": {
            "short_name": "bbny",
            "long_name": "boundingBoxMinY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxMinZ": {
            "short_name": "bbnz",
            "long_name": "boundingBoxMinZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxMin",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxScale": {
            "short_name": "bbs",
            "long_name": "boundingBoxScale",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "boundingBoxScaleX",
                "boundingBoxScaleY",
                "boundingBoxScaleZ"
            ]
        },
        "boundingBoxScaleX": {
            "short_name": "bscx",
            "long_name": "boundingBoxScaleX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "boundingBoxScale",
            "numeric_type": 11,
            "default_value": 1.5
        },
        "boundingBoxScaleY": {
            "short_name": "bscy",
            "long_name": "boundingBoxScaleY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "boundingBoxScale",
            "numeric_type": 11,
            "default_value": 1.5
        },
        "boundingBoxScaleZ": {
            "short_name": "bscz",
            "long_name": "boundingBoxScaleZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "boundingBoxScale",
            "numeric_type": 11,
            "default_value": 1.5
        },
        "boundingBoxSize": {
            "short_name": "bbsi",
            "long_name": "boundingBoxSize",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "parent_plug": "boundingBox",
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
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeY": {
            "short_name": "bbsy",
            "long_name": "boundingBoxSizeY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "boundingBoxSizeZ": {
            "short_name": "bbsz",
            "long_name": "boundingBoxSizeZ",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleLinearAttribute",
            "parent_plug": "boundingBoxSize",
            "unit_type": 2,
            "default_value": 0.0
        },
        "cachedInMesh": {
            "short_name": "ci",
            "long_name": "cachedInMesh",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 14
        },
        "cachedSmoothMesh": {
            "short_name": "cs",
            "long_name": "cachedSmoothMesh",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 14
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
        "castsShadows": {
            "short_name": "csh",
            "long_name": "castsShadows",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "collisionDepthVelocityIncrement": {
            "short_name": "cdvi",
            "long_name": "collisionDepthVelocityIncrement",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "collisionDepthVelocityMultiplier": {
            "short_name": "cdvm",
            "long_name": "collisionDepthVelocityMultiplier",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 1
        },
        "collisionOffsetVelocityIncrement": {
            "short_name": "covi",
            "long_name": "collisionOffsetVelocityIncrement",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "collisionOffsetVelocityMultiplier": {
            "short_name": "covm",
            "long_name": "collisionOffsetVelocityMultiplier",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 1
        },
        "colorPerVertex": {
            "short_name": "cpvx",
            "long_name": "colorPerVertex",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 1,
            "children": [
                "vertexColor"
            ]
        },
        "colorSet": {
            "short_name": "clst",
            "long_name": "colorSet",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "colors": {
            "short_name": "clr",
            "long_name": "colors",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "compInstObjGroups": {
            "short_name": "ciog",
            "long_name": "compInstObjGroups",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "componentTags": {
            "short_name": "gtag",
            "long_name": "componentTags",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "computeFromSculptCache": {
            "short_name": "cfsc",
            "long_name": "computeFromSculptCache",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "containerType": {
            "short_name": "ctyp",
            "long_name": "containerType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "continuity": {
            "short_name": "co",
            "long_name": "continuity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "controlPoints": {
            "short_name": "cp",
            "long_name": "controlPoints",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Double",
            "num_elements": 0
        },
        "creaseData": {
            "short_name": "cd",
            "long_name": "creaseData",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
        },
        "creaseVertexData": {
            "short_name": "cvd",
            "long_name": "creaseVertexData",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
        },
        "creationDate": {
            "short_name": "cdat",
            "long_name": "creationDate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "creator": {
            "short_name": "ctor",
            "long_name": "creator",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "currentColorSet": {
            "short_name": "ccls",
            "long_name": "currentColorSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "currentUVSet": {
            "short_name": "cuvs",
            "long_name": "currentUVSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "customTreatment": {
            "short_name": "ctrt",
            "long_name": "customTreatment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "depthJitter": {
            "short_name": "dej",
            "long_name": "depthJitter",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "dispResolution": {
            "short_name": "dr",
            "long_name": "dispResolution",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "displacementType": {
            "short_name": "dist",
            "long_name": "displacementType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "displayAlphaAsGreyScale": {
            "short_name": "dags",
            "long_name": "displayAlphaAsGreyScale",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayBlueColorChannel": {
            "short_name": "dblu",
            "long_name": "displayBlueColorChannel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "displayBorders": {
            "short_name": "db",
            "long_name": "displayBorders",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayCenter": {
            "short_name": "dc",
            "long_name": "displayCenter",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayColorAsGreyScale": {
            "short_name": "dcgs",
            "long_name": "displayColorAsGreyScale",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayColorChannel": {
            "short_name": "dcc",
            "long_name": "displayColorChannel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "displayColors": {
            "short_name": "dcol",
            "long_name": "displayColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayEdges": {
            "short_name": "de",
            "long_name": "displayEdges",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "displayFacesWithGroupId": {
            "short_name": "dfgi",
            "long_name": "displayFacesWithGroupId",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": -2
        },
        "displayGreenColorChannel": {
            "short_name": "dgrn",
            "long_name": "displayGreenColorChannel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "displayHWEnvironment": {
            "short_name": "dhe",
            "long_name": "displayHWEnvironment",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayImmediate": {
            "short_name": "di",
            "long_name": "displayImmediate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayInvisibleFaces": {
            "short_name": "difs",
            "long_name": "displayInvisibleFaces",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayItemNumbers": {
            "short_name": "din",
            "long_name": "displayItemNumbers",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "displayMapBorders": {
            "short_name": "dmb",
            "long_name": "displayMapBorders",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayNonPlanar": {
            "short_name": "dnp",
            "long_name": "displayNonPlanar",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayNormal": {
            "short_name": "dn",
            "long_name": "displayNormal",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayRedColorChannel": {
            "short_name": "dred",
            "long_name": "displayRedColorChannel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "displaySmoothMesh": {
            "short_name": "dsm",
            "long_name": "displaySmoothMesh",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "displaySubdComps": {
            "short_name": "dsc",
            "long_name": "displaySubdComps",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayTangent": {
            "short_name": "dtn",
            "long_name": "displayTangent",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayTriangles": {
            "short_name": "dt",
            "long_name": "displayTriangles",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayUVs": {
            "short_name": "duv",
            "long_name": "displayUVs",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "displayVertices": {
            "short_name": "dv",
            "long_name": "displayVertices",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "doubleSided": {
            "short_name": "ds",
            "long_name": "doubleSided",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "edge": {
            "short_name": "ed",
            "long_name": "edge",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Long",
            "num_elements": 0
        },
        "edgeIdMap": {
            "short_name": "emap",
            "long_name": "edgeIdMap",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "enableOpenCL": {
            "short_name": "eocl",
            "long_name": "enableOpenCL",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "extraSampleRate": {
            "short_name": "xsr",
            "long_name": "extraSampleRate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 5
        },
        "face": {
            "short_name": "fc",
            "long_name": "face",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 0
        },
        "faceColorIndices": {
            "short_name": "fcid",
            "long_name": "faceColorIndices",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 9
        },
        "faceIdMap": {
            "short_name": "fmap",
            "long_name": "faceIdMap",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "featureDisplacement": {
            "short_name": "fbda",
            "long_name": "featureDisplacement",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "freeze": {
            "short_name": "frze",
            "long_name": "freeze",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 11,
            "default_value": 0.0
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
        "geometryAntialiasingOverride": {
            "short_name": "gao",
            "long_name": "geometryAntialiasingOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
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
        "ghostColorPostB": {
            "short_name": "gab",
            "long_name": "ghostColorPostB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6629999876022339
        },
        "ghostColorPostG": {
            "short_name": "gag",
            "long_name": "ghostColorPostG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.6779999732971191
        },
        "ghostColorPostR": {
            "short_name": "gar",
            "long_name": "ghostColorPostR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPost",
            "numeric_type": 11,
            "default_value": 0.878000020980835
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
        "ghostColorPreB": {
            "short_name": "gpb",
            "long_name": "ghostColorPreB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreG": {
            "short_name": "gpg",
            "long_name": "ghostColorPreG",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "ghostColorPreR": {
            "short_name": "grr",
            "long_name": "ghostColorPreR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostColorPre",
            "numeric_type": 11,
            "default_value": 0.44699999690055847
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
        "ghostDriver": {
            "short_name": "gdr",
            "long_name": "ghostDriver",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "ghostFarOpacity": {
            "short_name": "gfro",
            "long_name": "ghostFarOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.15000000596046448
        },
        "ghostFrames": {
            "short_name": "gf",
            "long_name": "ghostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 9
        },
        "ghostNearOpacity": {
            "short_name": "gnro",
            "long_name": "ghostNearOpacity",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostOpacityRange",
            "numeric_type": 11,
            "default_value": 0.5
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
        "ghostPostFrames": {
            "short_name": "gpof",
            "long_name": "ghostPostFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
        },
        "ghostPreFrames": {
            "short_name": "gprf",
            "long_name": "ghostPreFrames",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 3
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
        "ghostsStep": {
            "short_name": "gstp",
            "long_name": "ghostsStep",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "ghostCustomSteps",
            "numeric_type": 7,
            "default_value": 1
        },
        "hardwareFogMultiplier": {
            "short_name": "hfm",
            "long_name": "hardwareFogMultiplier",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
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
        "hideOnPlayback": {
            "short_name": "hpb",
            "long_name": "hideOnPlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "holdOut": {
            "short_name": "hot",
            "long_name": "holdOut",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "holeFaceData": {
            "short_name": "hfd",
            "long_name": "holeFaceData",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 0
        },
        "hyperLayout": {
            "short_name": "hl",
            "long_name": "hyperLayout",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "iconName": {
            "short_name": "icn",
            "long_name": "iconName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "identification": {
            "short_name": "rlid",
            "long_name": "identification",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 4,
            "default_value": 0
        },
        "ignoreHwShader": {
            "short_name": "ih",
            "long_name": "ignoreHwShader",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "ignoreSelfShadowing": {
            "short_name": "iss",
            "long_name": "ignoreSelfShadowing",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "inForceNodeUVUpdate": {
            "short_name": "ifuv",
            "long_name": "inForceNodeUVUpdate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "inMesh": {
            "short_name": "i",
            "long_name": "inMesh",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 14
        },
        "initialSampleRate": {
            "short_name": "dsr",
            "long_name": "initialSampleRate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 6
        },
        "instMaterialAssign": {
            "short_name": "imtla",
            "long_name": "instMaterialAssign",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kMessageAttribute",
            "num_elements": 0
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
        "inverseMatrix": {
            "short_name": "im",
            "long_name": "inverseMatrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
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
        "keepBorder": {
            "short_name": "kb",
            "long_name": "keepBorder",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "keepHardEdge": {
            "short_name": "khe",
            "long_name": "keepHardEdge",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "keepMapBorders": {
            "short_name": "kmb",
            "long_name": "keepMapBorders",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "layerOverrideColor": {
            "short_name": "lovc",
            "long_name": "layerOverrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 2,
            "default_value": 0
        },
        "layerRenderable": {
            "short_name": "rndr",
            "long_name": "layerRenderable",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "renderInfo",
            "numeric_type": 1,
            "default_value": True
        },
        "loadTiledTextures": {
            "short_name": "ltt",
            "long_name": "loadTiledTextures",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
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
        "materialBlend": {
            "short_name": "matb",
            "long_name": "materialBlend",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "matrix": {
            "short_name": "m",
            "long_name": "matrix",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 5
        },
        "maxEdgeLength": {
            "short_name": "mxe",
            "long_name": "maxEdgeLength",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.10000000149011612
        },
        "maxShadingSamples": {
            "short_name": "msa",
            "long_name": "maxShadingSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "maxSubd": {
            "short_name": "mxs",
            "long_name": "maxSubd",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 5
        },
        "maxTriangles": {
            "short_name": "tsl",
            "long_name": "maxTriangles",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 60000
        },
        "maxUv": {
            "short_name": "xuv",
            "long_name": "maxUv",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.5
        },
        "maxVisibilitySamples": {
            "short_name": "mvs",
            "long_name": "maxVisibilitySamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "maxVisibilitySamplesOverride": {
            "short_name": "vbo",
            "long_name": "maxVisibilitySamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "message": {
            "short_name": "msg",
            "long_name": "message",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "mikktspaceTangentGen": {
            "short_name": "mttg",
            "long_name": "mikktspaceTangentGen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "minEdgeLength": {
            "short_name": "mne",
            "long_name": "minEdgeLength",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 0.009999999776482582
        },
        "minScreen": {
            "short_name": "mns",
            "long_name": "minScreen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 14.0
        },
        "motionBlur": {
            "short_name": "mb",
            "long_name": "motionBlur",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "motionVectorColorSet": {
            "short_name": "mvcs",
            "long_name": "motionVectorColorSet",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "normalPerVertex": {
            "short_name": "npvx",
            "long_name": "normalPerVertex",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_children": 1,
            "children": [
                "vertexNormal"
            ]
        },
        "normalSize": {
            "short_name": "ns",
            "long_name": "normalSize",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 0.4
        },
        "normalThreshold": {
            "short_name": "nat",
            "long_name": "normalThreshold",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 30.0
        },
        "normals": {
            "short_name": "n",
            "long_name": "normals",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_elements": 0
        },
        "numTriangles": {
            "short_name": "nt",
            "long_name": "numTriangles",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 100
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
        "objectColorB": {
            "short_name": "obcb",
            "long_name": "objectColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
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
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "objectColorR": {
            "short_name": "obcr",
            "long_name": "objectColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "objectColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
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
        "opposite": {
            "short_name": "op",
            "long_name": "opposite",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "osdCreaseMethod": {
            "short_name": "ocr",
            "long_name": "osdCreaseMethod",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "osdFvarBoundary": {
            "short_name": "ofb",
            "long_name": "osdFvarBoundary",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "osdFvarPropagateCorners": {
            "short_name": "ofc",
            "long_name": "osdFvarPropagateCorners",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "osdIndependentUVChannels": {
            "short_name": "iuv",
            "long_name": "osdIndependentUVChannels",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "osdSmoothTriangles": {
            "short_name": "ost",
            "long_name": "osdSmoothTriangles",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "outForceNodeUVUpdate": {
            "short_name": "ofuv",
            "long_name": "outForceNodeUVUpdate",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "outGeometryClean": {
            "short_name": "ogc",
            "long_name": "outGeometryClean",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "outMesh": {
            "short_name": "o",
            "long_name": "outMesh",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 14
        },
        "outSmoothMesh": {
            "short_name": "os",
            "long_name": "outSmoothMesh",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 14
        },
        "outSmoothMeshSubdError": {
            "short_name": "osde",
            "long_name": "outSmoothMeshSubdError",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
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
        "outlinerColorB": {
            "short_name": "oclrb",
            "long_name": "outlinerColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
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
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "outlinerColorR": {
            "short_name": "oclrr",
            "long_name": "outlinerColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "outlinerColor",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColor": {
            "short_name": "ovc",
            "long_name": "overrideColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 2,
            "default_value": 0
        },
        "overrideColorA": {
            "short_name": "ovca",
            "long_name": "overrideColorA",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "overrideColorB": {
            "short_name": "ovcb",
            "long_name": "overrideColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
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
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorR": {
            "short_name": "ovcr",
            "long_name": "overrideColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "overrideColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "overrideColorRGB": {
            "short_name": "ovrgb",
            "long_name": "overrideColorRGB",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "parent_plug": "drawOverride",
            "num_children": 3,
            "children": [
                "overrideColorR",
                "overrideColorG",
                "overrideColorB"
            ]
        },
        "overrideDisplayType": {
            "short_name": "ovdt",
            "long_name": "overrideDisplayType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overrideEnabled": {
            "short_name": "ove",
            "long_name": "overrideEnabled",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideLevelOfDetail": {
            "short_name": "ovlod",
            "long_name": "overrideLevelOfDetail",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute",
            "parent_plug": "drawOverride"
        },
        "overridePlayback": {
            "short_name": "ovp",
            "long_name": "overridePlayback",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideRGBColors": {
            "short_name": "ovrgbf",
            "long_name": "overrideRGBColors",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": False
        },
        "overrideShading": {
            "short_name": "ovs",
            "long_name": "overrideShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
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
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "overrideVisibility": {
            "short_name": "ovv",
            "long_name": "overrideVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "drawOverride",
            "numeric_type": 1,
            "default_value": True
        },
        "parentInverseMatrix": {
            "short_name": "pim",
            "long_name": "parentInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "parentMatrix": {
            "short_name": "pm",
            "long_name": "parentMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "perInstanceIndex": {
            "short_name": "pii",
            "long_name": "perInstanceIndex",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 7,
            "default_value": -1
        },
        "perInstanceTag": {
            "short_name": "pit",
            "long_name": "perInstanceTag",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 7,
            "default_value": -1
        },
        "pickTexture": {
            "short_name": "pte",
            "long_name": "pickTexture",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "pinData": {
            "short_name": "pd",
            "long_name": "pinData",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 0
        },
        "pnts": {
            "short_name": "pt",
            "long_name": "pnts",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_elements": 0
        },
        "primaryVisibility": {
            "short_name": "vis",
            "long_name": "primaryVisibility",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "propagateEdgeHardness": {
            "short_name": "peh",
            "long_name": "propagateEdgeHardness",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
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
        "quadSplit": {
            "short_name": "qsp",
            "long_name": "quadSplit",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "receiveShadows": {
            "short_name": "rcsh",
            "long_name": "receiveShadows",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "referenceObject": {
            "short_name": "rob",
            "long_name": "referenceObject",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kMessageAttribute"
        },
        "relativeTweak": {
            "short_name": "rtw",
            "long_name": "relativeTweak",
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
        "renderLayerInfo": {
            "short_name": "rlio",
            "long_name": "renderLayerInfo",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 0
        },
        "renderSmoothLevel": {
            "short_name": "rsl",
            "long_name": "renderSmoothLevel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 2
        },
        "renderType": {
            "short_name": "rt",
            "long_name": "renderType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 0
        },
        "renderVolume": {
            "short_name": "rv",
            "long_name": "renderVolume",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "reuseTriangles": {
            "short_name": "rtri",
            "long_name": "reuseTriangles",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "rmbCommand": {
            "short_name": "rmc",
            "long_name": "rmbCommand",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "shadingSamples": {
            "short_name": "ssa",
            "long_name": "shadingSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "shadingSamplesOverride": {
            "short_name": "sso",
            "long_name": "shadingSamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "showDisplacements": {
            "short_name": "sdis",
            "long_name": "showDisplacements",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "smoothLevel": {
            "short_name": "lev",
            "long_name": "smoothLevel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 2
        },
        "smoothMeshSelectionMode": {
            "short_name": "ssm",
            "long_name": "smoothMeshSelectionMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "smoothOffset": {
            "short_name": "so",
            "long_name": "smoothOffset",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_children": 3,
            "children": [
                "sofx",
                "sofy",
                "sofz"
            ]
        },
        "smoothOsdColorizePatches": {
            "short_name": "socp",
            "long_name": "smoothOsdColorizePatches",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "smoothShading": {
            "short_name": "smo",
            "long_name": "smoothShading",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "smoothTessLevel": {
            "short_name": "stlv",
            "long_name": "smoothTessLevel",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 4,
            "default_value": 7
        },
        "smoothUVs": {
            "short_name": "suv",
            "long_name": "smoothUVs",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "smoothWarn": {
            "short_name": "sw",
            "long_name": "smoothWarn",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "sofx": {
            "short_name": "sx",
            "long_name": "sofx",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "smoothOffset",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "sofy": {
            "short_name": "sy",
            "long_name": "sofy",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "smoothOffset",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "sofz": {
            "short_name": "sz",
            "long_name": "sofz",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "smoothOffset",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "tangentNormalThreshold": {
            "short_name": "tnt",
            "long_name": "tangentNormalThreshold",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "unit_type": 1,
            "default_value": 0.0
        },
        "tangentSmoothingAngle": {
            "short_name": "tsa",
            "long_name": "tangentSmoothingAngle",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kDoubleAngleAttribute",
            "unit_type": 1,
            "default_value": 0.0
        },
        "tangentSpace": {
            "short_name": "tgsp",
            "long_name": "tangentSpace",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
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
        "templateName": {
            "short_name": "tna",
            "long_name": "templateName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "templatePath": {
            "short_name": "tpt",
            "long_name": "templatePath",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "textureThreshold": {
            "short_name": "fth",
            "long_name": "textureThreshold",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 0
        },
        "tweak": {
            "short_name": "tw",
            "long_name": "tweak",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "tweakLocation": {
            "short_name": "twl",
            "long_name": "tweakLocation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 24
        },
        "useGlobalSmoothDrawType": {
            "short_name": "ugsdt",
            "long_name": "useGlobalSmoothDrawType",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "useMaxEdgeLength": {
            "short_name": "uxe",
            "long_name": "useMaxEdgeLength",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useMaxSubdivisions": {
            "short_name": "uxs",
            "long_name": "useMaxSubdivisions",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useMaxUV": {
            "short_name": "uxu",
            "long_name": "useMaxUV",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useMeshSculptCache": {
            "short_name": "umsc",
            "long_name": "useMeshSculptCache",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useMeshTexSculptCache": {
            "short_name": "umtsc",
            "long_name": "useMeshTexSculptCache",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useMinEdgeLength": {
            "short_name": "uie",
            "long_name": "useMinEdgeLength",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useMinScreen": {
            "short_name": "uns",
            "long_name": "useMinScreen",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "useNumTriangles": {
            "short_name": "unp",
            "long_name": "useNumTriangles",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "useObjectColor": {
            "short_name": "uoc",
            "long_name": "useObjectColor",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "useOsdBoundaryMethods": {
            "short_name": "uob",
            "long_name": "useOsdBoundaryMethods",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
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
        "useSmoothPreviewForRender": {
            "short_name": "uspr",
            "long_name": "useSmoothPreviewForRender",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "userTrg": {
            "short_name": "utrg",
            "long_name": "userTrg",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
        },
        "uvPivot": {
            "short_name": "pv",
            "long_name": "uvPivot",
            "is_element": False,
            "is_array": False,
            "is_compound": True,
            "type_str": "kAttribute2Double",
            "num_children": 2,
            "children": [
                "uvPivotX",
                "uvPivotY"
            ]
        },
        "uvPivotX": {
            "short_name": "pvx",
            "long_name": "uvPivotX",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "uvPivot",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "uvPivotY": {
            "short_name": "pvy",
            "long_name": "uvPivotY",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "uvPivot",
            "numeric_type": 14,
            "default_value": 0.0
        },
        "uvSet": {
            "short_name": "uvst",
            "long_name": "uvSet",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "num_elements": 1
        },
        "uvSize": {
            "short_name": "usz",
            "long_name": "uvSize",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 4.0
        },
        "uvTweakLocation": {
            "short_name": "uvtl",
            "long_name": "uvTweakLocation",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 24
        },
        "uvpt": {
            "short_name": "uv",
            "long_name": "uvpt",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute2Float",
            "num_elements": 0
        },
        "vertexBackfaceCulling": {
            "short_name": "vbc",
            "long_name": "vertexBackfaceCulling",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": True
        },
        "vertexColor": {
            "short_name": "vclr",
            "long_name": "vertexColor",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "parent_plug": "colorPerVertex",
            "num_elements": 0
        },
        "vertexColorSource": {
            "short_name": "vcs",
            "long_name": "vertexColorSource",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "vertexIdMap": {
            "short_name": "vmap",
            "long_name": "vertexIdMap",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "vertexNormal": {
            "short_name": "vn",
            "long_name": "vertexNormal",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kCompoundAttribute",
            "parent_plug": "normalPerVertex",
            "num_elements": 0
        },
        "vertexNormalMethod": {
            "short_name": "vnm",
            "long_name": "vertexNormalMethod",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "vertexSize": {
            "short_name": "vs",
            "long_name": "vertexSize",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 14,
            "default_value": 3.0
        },
        "viewMode": {
            "short_name": "vwm",
            "long_name": "viewMode",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kEnumAttribute"
        },
        "viewName": {
            "short_name": "vwn",
            "long_name": "viewName",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "typed_type": 4
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
        "visibleFraction": {
            "short_name": "vf",
            "long_name": "visibleFraction",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 11,
            "default_value": 1.0
        },
        "visibleInReflections": {
            "short_name": "vir",
            "long_name": "visibleInReflections",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "visibleInRefractions": {
            "short_name": "vif",
            "long_name": "visibleInRefractions",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "volumeSamples": {
            "short_name": "vss",
            "long_name": "volumeSamples",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 7,
            "default_value": 1
        },
        "volumeSamplesOverride": {
            "short_name": "vso",
            "long_name": "volumeSamplesOverride",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "numeric_type": 1,
            "default_value": False
        },
        "vrts": {
            "short_name": "vt",
            "long_name": "vrts",
            "is_element": False,
            "is_array": True,
            "is_compound": True,
            "type_str": "kAttribute3Float",
            "num_elements": 0
        },
        "weights": {
            "short_name": "wt",
            "long_name": "weights",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "num_elements": 0,
            "numeric_type": 14,
            "default_value": 1.0
        },
        "wireColorB": {
            "short_name": "wfcb",
            "long_name": "wireColorB",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
            "parent_plug": "wireColorRGB",
            "numeric_type": 11,
            "default_value": 0.0
        },
        "wireColorR": {
            "short_name": "wfcr",
            "long_name": "wireColorR",
            "is_element": False,
            "is_array": False,
            "is_compound": False,
            "type_str": "kNumericAttribute",
            "parent_plug": "wireColorRGB",
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
        "worldInverseMatrix": {
            "short_name": "wim",
            "long_name": "worldInverseMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldMatrix": {
            "short_name": "wm",
            "long_name": "worldMatrix",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 5
        },
        "worldMesh": {
            "short_name": "w",
            "long_name": "worldMesh",
            "is_element": False,
            "is_array": True,
            "is_compound": False,
            "type_str": "kTypedAttribute",
            "num_elements": 0,
            "typed_type": 14
        }
    }
}

ATTRIBUTES_SHORT_NAMES_MAP = {
    "bnm": "binMembership",
    "bbx": "blackBox",
    "boc": "borderConnections",
    "bb": "boundingBox",
    "bcx": "boundingBoxCenterX",
    "bcy": "boundingBoxCenterY",
    "bcz": "boundingBoxCenterZ",
    "bbmx": "boundingBoxMax",
    "bbxx": "boundingBoxMaxX",
    "bbxy": "boundingBoxMaxY",
    "bbxz": "boundingBoxMaxZ",
    "bbmn": "boundingBoxMin",
    "bbnx": "boundingBoxMinX",
    "bbny": "boundingBoxMinY",
    "bbnz": "boundingBoxMinZ",
    "bbsi": "boundingBoxSize",
    "bbsx": "boundingBoxSizeX",
    "bbsy": "boundingBoxSizeY",
    "bbsz": "boundingBoxSizeZ",
    "cch": "caching",
    "c": "center",
    "ctyp": "containerType",
    "cdat": "creationDate",
    "ctor": "creator",
    "ctrt": "customTreatment",
    "dlim": "dagLocalInverseMatrix",
    "dlm": "dagLocalMatrix",
    "dh": "dispHull",
    "dla": "displayLocalAxis",
    "drp": "displayRotatePivot",
    "dsp": "displayScalePivot",
    "do": "drawOverride",
    "dyn": "dynamics",
    "fzn": "frozen",
    "g": "green",
    "gac": "ghostColorPost",
    "gab": "ghostColorPostB",
    "gag": "ghostColorPostG",
    "gar": "ghostColorPostR",
    "gcp": "ghostColorPre",
    "gpb": "ghostColorPreB",
    "gpg": "ghostColorPreG",
    "grr": "ghostColorPreR",
    "gcs": "ghostCustomSteps",
    "gdr": "ghostDriver",
    "gfro": "ghostFarOpacity",
    "gf": "ghostFrames",
    "gnro": "ghostNearOpacity",
    "golr": "ghostOpacityRange",
    "gpof": "ghostPostFrames",
    "gprf": "ghostPreFrames",
    "gud": "ghostUseDriver",
    "gh": "ghosting",
    "gm": "ghostingMode",
    "gstp": "ghostsStep",
    "hio": "hiddenInOutliner",
    "hpb": "hideOnPlayback",
    "hl": "hyperLayout",
    "icn": "iconName",
    "rlid": "identification",
    "it": "inheritsTransform",
    "iog": "instObjGroups",
    "io": "intermediateObject",
    "im": "inverseMatrix",
    "isc": "isCollapsed",
    "ish": "isHierarchicalConnection",
    "ihi": "isHistoricallyInteresting",
    "lovc": "layerOverrideColor",
    "rndr": "layerRenderable",
    "lodv": "lodVisibility",
    "m": "matrix",
    "mxrl": "maxRotLimit",
    "xrle": "maxRotLimitEnable",
    "xrxl": "maxRotXLimit",
    "xrxe": "maxRotXLimitEnable",
    "xryl": "maxRotYLimit",
    "xrye": "maxRotYLimitEnable",
    "xrzl": "maxRotZLimit",
    "xrze": "maxRotZLimitEnable",
    "mxsl": "maxScaleLimit",
    "xsle": "maxScaleLimitEnable",
    "xsxl": "maxScaleXLimit",
    "xsxe": "maxScaleXLimitEnable",
    "xsyl": "maxScaleYLimit",
    "xsye": "maxScaleYLimitEnable",
    "xszl": "maxScaleZLimit",
    "xsze": "maxScaleZLimitEnable",
    "mxtl": "maxTransLimit",
    "xtle": "maxTransLimitEnable",
    "xtxl": "maxTransXLimit",
    "xtxe": "maxTransXLimitEnable",
    "xtyl": "maxTransYLimit",
    "xtye": "maxTransYLimitEnable",
    "xtzl": "maxTransZLimit",
    "xtze": "maxTransZLimitEnable",
    "msg": "message",
    "mnrl": "minRotLimit",
    "mrle": "minRotLimitEnable",
    "mrxl": "minRotXLimit",
    "mrxe": "minRotXLimitEnable",
    "mryl": "minRotYLimit",
    "mrye": "minRotYLimitEnable",
    "mrzl": "minRotZLimit",
    "mrze": "minRotZLimitEnable",
    "mnsl": "minScaleLimit",
    "msle": "minScaleLimitEnable",
    "msxl": "minScaleXLimit",
    "msxe": "minScaleXLimitEnable",
    "msyl": "minScaleYLimit",
    "msye": "minScaleYLimitEnable",
    "mszl": "minScaleZLimit",
    "msze": "minScaleZLimitEnable",
    "mntl": "minTransLimit",
    "mtle": "minTransLimitEnable",
    "mtxl": "minTransXLimit",
    "mtxe": "minTransXLimitEnable",
    "mtyl": "minTransYLimit",
    "mtye": "minTransYLimitEnable",
    "mtzl": "minTransZLimit",
    "mtze": "minTransZLimitEnable",
    "nds": "nodeState",
    "oc": "objectColor",
    "obcb": "objectColorB",
    "obcg": "objectColorG",
    "obcr": "objectColorR",
    "obcc": "objectColorRGB",
    "opm": "offsetParentMatrix",
    "oclr": "outlinerColor",
    "oclrb": "outlinerColorB",
    "oclrg": "outlinerColorG",
    "oclrr": "outlinerColorR",
    "ovc": "overrideColor",
    "ovca": "overrideColorA",
    "ovcb": "overrideColorB",
    "ovcg": "overrideColorG",
    "ovcr": "overrideColorR",
    "ovrgb": "overrideColorRGB",
    "ovdt": "overrideDisplayType",
    "ove": "overrideEnabled",
    "ovlod": "overrideLevelOfDetail",
    "ovp": "overridePlayback",
    "ovrgbf": "overrideRGBColors",
    "ovs": "overrideShading",
    "ovt": "overrideTexturing",
    "ovv": "overrideVisibility",
    "pim": "parentInverseMatrix",
    "pm": "parentMatrix",
    "pni": "publishedNodeInfo",
    "ri": "renderInfo",
    "rlio": "renderLayerInfo",
    "rmc": "rmbCommand",
    "r": "red",
    "ra": "rotateAxis",
    "rax": "rotateAxisX",
    "ray": "rotateAxisY",
    "raz": "rotateAxisZ",
    "ro": "inputRotateOrder",
    "rp": "rotatePivot",
    "rpt": "rotatePivotTranslate",
    "rptx": "rotatePivotTranslateX",
    "rpty": "rotatePivotTranslateY",
    "rptz": "rotatePivotTranslateZ",
    "rpx": "rotatePivotX",
    "rpy": "rotatePivotY",
    "rpz": "rotatePivotZ",
    "rq": "rotateQuaternion",
    "rqw": "rotateQuaternionW",
    "rqx": "rotateQuaternionX",
    "rqy": "rotateQuaternionY",
    "rqz": "rotateQuaternionZ",
    "rx": "rotateX",
    "ry": "rotateY",
    "rz": "rotateZ",
    "roi": "rotationInterpolation",
    "s": "spans",
    "sp": "spansUV",
    "spt": "scalePivotTranslate",
    "sptx": "scalePivotTranslateX",
    "spty": "scalePivotTranslateY",
    "sptz": "scalePivotTranslateZ",
    "spx": "scalePivotX",
    "spy": "scalePivotY",
    "spz": "scalePivotZ",
    "sx": "sofx",
    "sy": "sofy",
    "sz": "sofz",
    "hdl": "selectHandle",
    "hdlx": "selectHandleX",
    "hdly": "selectHandleY",
    "hdlz": "selectHandleZ",
    "sech": "selectionChildHighlighting",
    "sh": "shear",
    "shxy": "shearXY",
    "shxz": "shearXZ",
    "shyz": "shearYZ",
    "smd": "showManipDefault",
    "sml": "specifiedManipLocation",
    "tmp": "template",
    "tna": "templateName",
    "tpt": "templatePath",
    "tpv": "templateVersion",
    "tmrp": "transMinusRotatePivot",
    "tmrx": "transMinusRotatePivotX",
    "tmry": "transMinusRotatePivotY",
    "tmrz": "transMinusRotatePivotZ",
    "t": "translate",
    "tx": "translateX",
    "ty": "translateY",
    "tz": "translateZ",
    "uit": "uiTreatment",
    "uoc": "useObjectColor",
    "uocol": "useOutlinerColor",
    "vwm": "viewMode",
    "vwn": "viewName",
    "v": "visibility",
    "wfcb": "wireColorB",
    "wfcg": "wireColorG",
    "wfcr": "wireColorR",
    "wfcc": "wireColorRGB",
    "wim": "worldInverseMatrix",
    "wm": "worldMatrix",
    "xm": "xformMatrix",
    "bis": "bindInverseScale",
    "bix": "bindInverseScaleX",
    "biy": "bindInverseScaleY",
    "biz": "bindInverseScaleZ",
    "bjo": "bindJointOrient",
    "bjx": "bindJointOrientX",
    "bjy": "bindJointOrientY",
    "bjz": "bindJointOrientZ",
    "bps": "bindPose",
    "bra": "bindRotateAxis",
    "brax": "bindRotateAxisX",
    "bray": "bindRotateAxisY",
    "braz": "bindRotateAxisZ",
    "br": "bindRotation",
    "brx": "bindRotationX",
    "bry": "bindRotationY",
    "brz": "bindRotationZ",
    "bs": "bindScale",
    "bsx": "bindScaleX",
    "bsy": "bindScaleY",
    "bsz": "bindScaleZ",
    "bsc": "bindSegmentScaleCompensate",
    "dm": "dofMask",
    "dl": "drawLabel",
    "ds": "doubleSided",
    "fkr": "fkRotate",
    "frx": "fkRotateX",
    "fry": "fkRotateY",
    "frz": "fkRotateZ",
    "hfk": "hikFkJoint",
    "hni": "hikNodeID",
    "ikr": "ikRotate",
    "irx": "ikRotateX",
    "iry": "ikRotateY",
    "irz": "ikRotateZ",
    "isf": "inIKSolveFlag",
    "is": "inverseScale",
    "isx": "inverseScaleX",
    "isy": "inverseScaleY",
    "isz": "inverseScaleZ",
    "idf": "isIKDirtyFlag",
    "jo": "jointOrient",
    "jot": "jointOrientType",
    "jox": "jointOrientX",
    "joy": "jointOrientY",
    "joz": "jointOrientZ",
    "jt": "jointType",
    "jtx": "jointTypeX",
    "jty": "jointTypeY",
    "jtz": "jointTypeZ",
    "xdr": "maxRotateDampRange",
    "xdx": "maxRotateDampRangeX",
    "xdy": "maxRotateDampRangeY",
    "xdz": "maxRotateDampRangeZ",
    "xst": "maxRotateDampStrength",
    "xstx": "maxRotateDampStrengthX",
    "xsty": "maxRotateDampStrengthY",
    "xstz": "maxRotateDampStrengthZ",
    "ndr": "minRotateDampRange",
    "ndx": "minRotateDampRangeX",
    "ndy": "minRotateDampRangeY",
    "ndz": "minRotateDampRangeZ",
    "nst": "minRotateDampStrength",
    "nstx": "minRotateDampStrengthX",
    "nsty": "minRotateDampStrengthY",
    "nstz": "minRotateDampStrengthZ",
    "otp": "otherType",
    "pa": "preferredAngle",
    "pax": "preferredAngleX",
    "pay": "preferredAngleY",
    "paz": "preferredAngleZ",
    "radi": "radius",
    "ssc": "segmentScaleCompensate",
    "sd": "side",
    "st": "secondTerm",
    "stx": "stiffnessX",
    "sty": "stiffnessY",
    "stz": "stiffnessZ",
    "typ": "type",
    "i1": "input1D",
    "i2": "input2D",
    "o": "outMesh",
    "cf": "colorIfFalse",
    "cfb": "colorIfFalseB",
    "cfg": "colorIfFalseG",
    "cfr": "colorIfFalseR",
    "ct": "colorIfTrue",
    "ctb": "colorIfTrueB",
    "ctg": "colorIfTrueG",
    "ctr": "colorIfTrueR",
    "ft": "firstTerm",
    "op": "opposite",
    "ocb": "outColorB",
    "ocg": "outColorG",
    "ocr": "osdCreaseMethod",
    "ip": "input",
    "ipb": "inputB",
    "ipg": "inputG",
    "ipr": "inputR",
    "mx": "max",
    "mxb": "maxB",
    "mxg": "maxG",
    "mxr": "maxR",
    "mn": "min",
    "mnb": "minB",
    "mng": "minG",
    "mnr": "minR",
    "opb": "outputB",
    "opg": "outputG",
    "opr": "outputR",
    "arp": "renderPassMode",
    "cl": "color",
    "imx": "inputMax",
    "imn": "inputMin",
    "i": "inMesh",
    "ov": "outValue",
    "omx": "outputMax",
    "omn": "outputMin",
    "vl": "value",
    "b": "blender",
    "cb": "colorB",
    "cg": "colorG",
    "cr": "create",
    "csp": "cacheSetup",
    "coord": "coordinate",
    "curgeom": "deformedGeometry",
    "nrm": "normalAxis",
    "novr": "normalOverride",
    "nrmip": "normalizedIsoParms",
    "orggeom": "originalGeometry",
    "omat": "outputMatrix",
    "ot": "outputTranslate",
    "rlcrv": "railCurve",
    "rsmat": "relativeSpaceMatrix",
    "rsmd": "relativeSpaceMode",
    "tng": "tangentAxis",
    "msn": "uvSetName",
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
    "c1b": "color1B",
    "c1g": "color1G",
    "c1r": "color1R",
    "c2": "color2",
    "c2b": "color2B",
    "c2g": "color2G",
    "c2r": "color2R",
    "imat": "inputMatrix",
    "oq": "outputQuat",
    "oqw": "outputQuatW",
    "oqx": "outputQuatX",
    "oqy": "outputQuatY",
    "oqz": "outputQuatZ",
    "or": "outputRotate",
    "orx": "outputRotateX",
    "ory": "outputRotateY",
    "orz": "outputRotateZ",
    "os": "outSmoothMesh",
    "osx": "outputScaleX",
    "osy": "outputScaleY",
    "osz": "outputScaleZ",
    "osh": "outputShear",
    "oshx": "outputShearX",
    "oshy": "outputShearY",
    "oshz": "outputShearZ",
    "otx": "outputTranslateX",
    "oty": "outputTranslateY",
    "otz": "outputTranslateZ",
    "enb": "enable",
    "env": "envelope",
    "pstmat": "postSpaceMatrix",
    "premat": "preSpaceMatrix",
    "tgt": "target",
    "adot": "alwaysDrawOnTop",
    "gal": "antialiasingLevel",
    "asbg": "asBackground",
    "bn": "blindDataNodes",
    "cc": "cached",
    "csh": "castsShadows",
    "clst": "colorSet",
    "ciog": "compInstObjGroups",
    "gtag": "componentTags",
    "cp": "controlPoints",
    "ccls": "currentColorSet",
    "cuvs": "currentUVSet",
    "d": "degreeUV",
    "dej": "depthJitter",
    "dcv": "dispCV",
    "dce": "dispCurveEndPoints",
    "dep": "dispEP",
    "dg": "dispGeometry",
    "dcc": "displayColorChannel",
    "dcol": "displayColors",
    "di": "displayImmediate",
    "eps": "editPoints",
    "f": "form",
    "gao": "geometryAntialiasingOverride",
    "hfm": "hardwareFogMultiplier",
    "hd": "header",
    "iss": "ignoreSelfShadowing",
    "ipo": "inPlace",
    "imtla": "instMaterialAssign",
    "ls": "lineWidth",
    "l": "local",
    "msa": "maxShadingSamples",
    "max": "maxValue",
    "mvs": "maxVisibilitySamples",
    "vbo": "maxVisibilitySamplesOverride",
    "mmv": "minMaxRangeV",
    "min": "minValue",
    "mb": "motionBlur",
    "pte": "pickTexture",
    "vis": "primaryVisibility",
    "rcsh": "receiveShadows",
    "rob": "referenceObject",
    "rtw": "relativeTweak",
    "rt": "renderType",
    "rv": "renderVolume",
    "ssa": "shadingSamples",
    "sso": "shadingSamplesOverride",
    "tw": "tweak",
    "twl": "tweakLocation",
    "ts": "tweakSize",
    "pv": "uvPivot",
    "pvx": "uvPivotX",
    "pvy": "uvPivotY",
    "uvst": "uvSet",
    "vf": "visibleFraction",
    "vir": "visibleInReflections",
    "vif": "visibleInRefractions",
    "vss": "volumeSamples",
    "vso": "volumeSamplesOverride",
    "wt": "weights",
    "wn": "worldNormal",
    "ws": "worldSpace",
    "btt": "basicTessellationType",
    "bbs": "boundingBoxScale",
    "bscx": "boundingBoxScaleX",
    "bscy": "boundingBoxScaleY",
    "bscz": "boundingBoxScaleZ",
    "ch": "chordHeight",
    "chr": "chordHeightRatio",
    "cdvi": "collisionDepthVelocityIncrement",
    "cdvm": "collisionDepthVelocityMultiplier",
    "covi": "collisionOffsetVelocityIncrement",
    "covm": "collisionOffsetVelocityMultiplier",
    "cvto": "curvatureTolerance",
    "cpr": "curvePrecision",
    "cps": "curvePrecisionShaded",
    "du": "degreeU",
    "dv": "displayVertices",
    "dor": "dispOrigin",
    "dsf": "dispSF",
    "dhe": "displayHWEnvironment",
    "drt": "displayRenderTessellation",
    "dvu": "divisionsU",
    "dvv": "divisionsV",
    "es": "edgeSwap",
    "eta": "explicitTessellationAttributes",
    "xsr": "extraSampleRate",
    "fbda": "featureDisplacement",
    "ftwp": "fixTextureWarp",
    "fu": "formU",
    "fv": "formV",
    "gdsu": "gridDivisionPerSpanU",
    "gdsv": "gridDivisionPerSpanV",
    "hot": "holdOut",
    "ih": "ignoreHwShader",
    "dsr": "initialSampleRate",
    "mxu": "maxValueU",
    "mxv": "maxValueV",
    "mmu": "minMaxRangeU",
    "mns": "minScreen",
    "mnu": "minValueU",
    "mnv": "minValueV",
    "mu": "modeU",
    "mv": "modeV",
    "nat": "normalThreshold",
    "ndf": "normalsDisplayScale",
    "nu": "numberU",
    "nv": "numberV",
    "uco": "objSpaceChordHeight",
    "pu": "patchUVIds",
    "tcn": "renderTriangleCount",
    "scvd": "selCVDisp",
    "sm": "simplifyMode",
    "smu": "simplifyU",
    "smv": "simplifyV",
    "ues": "smoothEdge",
    "esr": "smoothEdgeRatio",
    "smo": "smoothShading",
    "su": "spansU",
    "sv": "spansV",
    "fth": "textureThreshold",
    "tf": "trimFace",
    "tsu": "tweakSizeU",
    "tsv": "tweakSizeV",
    "nufa": "uDivisionsFactor",
    "uch": "useChordHeight",
    "ucr": "useChordHeightRatio",
    "uns": "useMinScreen",
    "nvfa": "vDivisionsFactor",
    "atm": "allowTopologyMod",
    "bck": "backfaceCulling",
    "bw": "borderWidth",
    "bnr": "boundaryRule",
    "ci": "cachedInMesh",
    "cs": "cachedSmoothMesh",
    "cpvx": "colorPerVertex",
    "clr": "colors",
    "cfsc": "computeFromSculptCache",
    "co": "continuity",
    "cd": "creaseData",
    "cvd": "creaseVertexData",
    "dr": "dispResolution",
    "dist": "displacementType",
    "dags": "displayAlphaAsGreyScale",
    "dblu": "displayBlueColorChannel",
    "db": "displayBorders",
    "dc": "displayCenter",
    "dcgs": "displayColorAsGreyScale",
    "de": "displayEdges",
    "dfgi": "displayFacesWithGroupId",
    "dgrn": "displayGreenColorChannel",
    "difs": "displayInvisibleFaces",
    "din": "displayItemNumbers",
    "dmb": "displayMapBorders",
    "dnp": "displayNonPlanar",
    "dn": "displayNormal",
    "dred": "displayRedColorChannel",
    "dsm": "displaySmoothMesh",
    "dsc": "displaySubdComps",
    "dtn": "displayTangent",
    "dt": "displayTriangles",
    "duv": "displayUVs",
    "ed": "edge",
    "emap": "edgeIdMap",
    "eocl": "enableOpenCL",
    "fc": "face",
    "fcid": "faceColorIndices",
    "fmap": "faceIdMap",
    "frze": "freeze",
    "hfd": "holeFaceData",
    "ifuv": "inForceNodeUVUpdate",
    "kb": "keepBorder",
    "khe": "keepHardEdge",
    "kmb": "keepMapBorders",
    "ltt": "loadTiledTextures",
    "matb": "materialBlend",
    "mxe": "maxEdgeLength",
    "mxs": "maxSubd",
    "tsl": "maxTriangles",
    "xuv": "maxUv",
    "mttg": "mikktspaceTangentGen",
    "mne": "minEdgeLength",
    "mvcs": "motionVectorColorSet",
    "npvx": "normalPerVertex",
    "ns": "normalSize",
    "ndt": "normalType",
    "n": "normals",
    "nt": "numTriangles",
    "ofb": "osdFvarBoundary",
    "ofc": "osdFvarPropagateCorners",
    "iuv": "osdIndependentUVChannels",
    "ost": "osdSmoothTriangles",
    "ovb": "osdVertBoundary",
    "ofuv": "outForceNodeUVUpdate",
    "ogc": "outGeometryClean",
    "osde": "outSmoothMeshSubdError",
    "pii": "perInstanceIndex",
    "pit": "perInstanceTag",
    "pd": "pinData",
    "pt": "pnts",
    "peh": "propagateEdgeHardness",
    "qsp": "quadSplit",
    "rsl": "renderSmoothLevel",
    "rtri": "reuseTriangles",
    "sdis": "showDisplacements",
    "sdt": "smoothDrawType",
    "lev": "smoothLevel",
    "ssm": "smoothMeshSelectionMode",
    "so": "smoothOffset",
    "socp": "smoothOsdColorizePatches",
    "stlv": "smoothTessLevel",
    "suv": "smoothUVs",
    "sw": "smoothWarn",
    "tnt": "tangentNormalThreshold",
    "tsa": "tangentSmoothingAngle",
    "tgsp": "tangentSpace",
    "ugsdt": "useGlobalSmoothDrawType",
    "uxe": "useMaxEdgeLength",
    "uxs": "useMaxSubdivisions",
    "uxu": "useMaxUV",
    "umsc": "useMeshSculptCache",
    "umtsc": "useMeshTexSculptCache",
    "uie": "useMinEdgeLength",
    "unp": "useNumTriangles",
    "uob": "useOsdBoundaryMethods",
    "uspr": "useSmoothPreviewForRender",
    "utrg": "userTrg",
    "usz": "uvSize",
    "uvtl": "uvTweakLocation",
    "uv": "uvpt",
    "vbc": "vertexBackfaceCulling",
    "vclr": "vertexColor",
    "vcs": "vertexColorSource",
    "vmap": "vertexIdMap",
    "vn": "vertexNormal",
    "vnm": "vertexNormalMethod",
    "vs": "vertexSize",
    "vt": "vrts",
    "w": "worldMesh"
}

