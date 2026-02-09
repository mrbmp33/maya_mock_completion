NODE_TYPES_TO_SHAPES = {
    # "polySphere": {
    #     "child_type": "kMesh",
    #     "child_name": "pSphereShape1",
    #     "parent_name": "pSphere1",
    #     "builder": {"name": "polySphere1", "type": "kPolySphere"},
    # },
    # "polyCube": {
    #     "child_type": "kMesh",
    #     "child_name": "pCubeShape1",
    #     "parent_name": "pCube1",
    #     "builder": {"name": "polyCube1", "type": "kPolyCube"},
    # },
    # "polyCylinder": {
    #     "child_type": "kMesh",
    #     "child_name": "pCylinderShape1",
    #     "parent_name": "pCylinder1",
    #     "builder": {"name": "polyCylinder1", "type": "kPolyCylinder"},
    # },
    # "polyCone": {
    #     "child_type": "kMesh",
    #     "child_name": "pConeShape1",
    #     "parent_name": "pCone1",
    #     "builder": {"name": "polyCone1", "type": "kPolyCone"},
    # },
    # "polyTorus": {
    #     "child_type": "kMesh",
    #     "child_name": "pTorusShape1",
    #     "parent_name": "pTorus1",
    #     "builder": {"name": "polyTorus1", "type": "kPolyTorus"},
    # },
    # "polyPlane": {
    #     "child_type": "kMesh",
    #     "child_name": "pPlaneShape1",
    #     "parent_name": "pPlane1",
    #     "builder": {"name": "polyPlane1", "type": "kPolyMesh"},
    # },
    # "polyPyramid": {
    #     "child_type": "kMesh",
    #     "child_name": "pPyramidShape1",
    #     "parent_name": "pPyramid1",
    #     "builder": {"name": "polyPyramid1", "type": "kPolyPyramid"},
    # },
    # "polyDisc": {
    #     "child_type": "kMesh",
    #     "child_name": "pDiscShape1",
    #     "parent_name": "pDisc1",
    #     "builder": {"name": "polyDisc1", "type": "kPluginDependNode"},
    # },
    "kMesh": {
        "child_type": "kMesh",
        "child_name": "polySurfaceShape1",
        "parent_name": "polySurface1",
    },
    "kNurbsCurve": {
        "child_type": "kNurbsCurve",
        "child_name": "curveShape1",
        "parent_name": "curve1",
    },
    "kNurbsSurface": {
        "child_type": "kNurbsSurface",
        "child_name": "surfaceShape1",
        "parent_name": "surface1",
    },
    "kBezierCurve": {
        "child_type": "kNurbsCurve",
        "child_name": "bezierShape1",
        "parent_name": "bezier1",
    },
    "kCircle": {
        "child_type": "kNurbsCurve",
        "child_name": "nurbsCircleShape1",
        "parent_name": "nurbsCircle1",
        "builder": {"name": "makeNurbCircle1", "type": "kCircle"},
    },
    "kPointLight": {
        "child_type": "kPointLight",
        "child_name": "pointLightShape1",
        "parent_name": "pointLight1",
    },
    "kDirectionalLight": {
        "child_type": "kDirectionalLight",
        "child_name": "directionalLightShape1",
        "parent_name": "directionalLight1",
    },
    "kSpotLight": {
        "child_type": "kSpotLight",
        "child_name": "spotLightShape1",
        "parent_name": "spotLight1",
    },
    "kAreaLight": {
        "child_type": "kAreaLight",
        "child_name": "areaLightShape1",
        "parent_name": "areaLight1",
    },
    "kVolumeLight": {
        "child_type": "kVolumeLight",
        "child_name": "volumeLightShape2",
        "parent_name": "volumeLight2",
    },
    "kAmbientLight": {
        "child_type": "kAmbientLight",
        "child_name": "ambientLightShape1",
        "parent_name": "ambientLight1",
    },
    "kCamera": {
        "child_type": "kCamera",
        "child_name": "cameraShape1",
        "parent_name": "camera1",
    },
    "kLattice": {
        "child_type": "kLattice",
        "child_name": "latticeShape1",
        "parent_name": "lattice1",
    },
    "kImagePlane": {
        "child_type": "kImagePlane",
        "child_name": "imagePlaneShape1",
        "parent_name": "imagePlane1",
    },
    "kLocator": {
        "child_type": "kLocator",
        "child_name": "locatorShape1",
        "parent_name": "locator1",
    },
}
