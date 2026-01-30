from functools import partial
import logging
from pprint import pprint
import traceback
import unittest
import sys
import pathlib
from maya.api import OpenMaya as om
from maya import cmds as mc
import numpy as np
from scipy.spatial.transform import Rotation as R

try:
    from maya import mmc_hierarchy as hierarchy
    from maya import ACTIVE_SELECTION
except ImportError:
    ...


def HOST():
    exe = pathlib.Path(sys.executable).stem
    if exe.endswith("maya"):
        return "maya"
    else:
        return "python"


class TestMayaMockCompletion(unittest.TestCase):

    def setUp(self):
        self.host = HOST()
        mc.file(new=True, force=True)
        # Reset state before each test
        self.dagmod = om.MDagModifier()

    def test_modifier_undo(self):
        transform = self.dagmod.createNode("transform")

        self.dagmod.doIt()

        self.assertTrue(transform.isNull() is False)
        if self.host == "python":
            self.assertTrue(hierarchy.NodePool.object_exists(transform))

        self.dagmod.undoIt()

        self.assertTrue(transform.isNull() is False)
        if self.host == "python":
            self.assertFalse(hierarchy.NodePool.object_exists(transform))

    def test_modifier_do_it_multiple(self):
        transform = self.dagmod.createNode("transform")
        self.assertTrue(transform.isNull() is False)
        self.dagmod.doIt()
        self.assertTrue(transform.isNull() is False)
        if self.host == "python":
            self.assertEqual(len(self.dagmod._queue), 1)

        self.dagmod.createNode("joint")
        self.dagmod.createNode("transform")
        self.dagmod.doIt()
        if self.host == "python":
            self.assertEqual(len(self.dagmod._queue), 2)

        self.dagmod.doIt()

        if self.host == "python":
            self.assertEqual(self.dagmod._executed, 0)

    def test_create_node_by_string(self):
        transform = self.dagmod.createNode("transform")

        self.dagmod.doIt()

        self.assertTrue(transform.isNull() == False)

        mesh = self.dagmod.createNode("mesh")

        self.dagmod.doIt()

        self.assertTrue(mesh.isNull() == False)

    def test_create_node_by_typeid(self):
        transform_id = om._TYPE_STR_TO_ID["kTransform"]
        transform = self.dagmod.createNode(transform_id)
        self.dagmod.doIt()
        self.assertTrue(transform.isNull() == False)

    def test_node_registration(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        fn_dep = om.MFnDependencyNode(transform)

        if HOST() == "python":
            print(HOST())
            from maya import mmc_hierarchy as hierarchy

            self.assertTrue(hierarchy.NodePool.object_exists(transform))

    def test_hierarchy_parent_child(self):
        dag_mod = om.MDagModifier()
        parent = dag_mod.createNode("transform")
        child = dag_mod.createNode("transform")
        dag_mod.doIt()

        dag_mod = om.MDagModifier()
        dag_mod.reparentNode(child, parent)
        dag_mod.doIt()

        sel = om.MSelectionList().add(om.MFnDependencyNode(parent).name())
        dag_path = sel.getDagPath(0)

        om.MDagPath().getAPathTo(parent)
        self.assertEqual(dag_path.childCount(), 1)

    def test_hierarchy_siblings(self):
        dag_mod = om.MDagModifier()
        parent = dag_mod.createNode("transform")
        child1 = dag_mod.createNode("transform")
        child2 = dag_mod.createNode("transform")
        dag_mod.doIt()

        dag_mod.reparentNode(child1, parent)
        dag_mod.reparentNode(child2, parent)
        dag_mod.doIt()

        dag_path = om.MDagPath.getAPathTo(parent)
        self.assertEqual(dag_path.childCount(), 2)

    def test_node_registration_unique_path(self):
        parent1 = self.dagmod.createNode("transform")
        self.dagmod.renameNode(parent1, "parent1")
        child1 = self.dagmod.createNode("transform", parent=parent1)
        self.dagmod.renameNode(child1, "child")

        parent2 = self.dagmod.createNode("transform")
        self.dagmod.renameNode(parent2, "parent2")
        child2_1 = self.dagmod.createNode("transform", parent=parent2)
        self.dagmod.renameNode(child2_1, "child")
        child2_2 = self.dagmod.createNode("transform", parent=parent2)
        self.dagmod.renameNode(child2_2, "child")

        transform1 = self.dagmod.createNode("transform")
        child3 = self.dagmod.createNode("transform", parent=transform1)
        self.dagmod.renameNode(child3, "child")

        self.dagmod.doIt()

        self.assertEqual(om.MFnDependencyNode(transform1).name(), "transform1")
        self.assertEqual(om.MFnDependencyNode(parent1).name(), "parent1")
        self.assertEqual(om.MFnDependencyNode(child1).name(), "child")
        self.assertEqual(om.MFnDependencyNode(parent2).name(), "parent2")
        self.assertEqual(om.MFnDependencyNode(child2_1).name(), "child")
        self.assertEqual(om.MFnDependencyNode(child2_2).name(), "child1")
        self.assertEqual(om.MFnDependencyNode(child3).name(), "child")

        if HOST() == "python":
            from maya import mmc_hierarchy as hierarchy

            self.assertTrue(hierarchy.NodePool.object_exists(child1))
            self.assertTrue(hierarchy.NodePool.object_exists(child2_1))

            self.assertTrue(hierarchy.NodePool.hash_exists(hash(child1._path_str())))
            self.assertTrue(hierarchy.NodePool.hash_exists(hash(child2_1._path_str())))

    def test_find_plug(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()

        fn_dep = om.MFnDependencyNode(transform)
        translatex_plug = fn_dep.findPlug("translateX", False)
        tx_plug = fn_dep.findPlug("tx", False)
        self.assertIsInstance(translatex_plug, om.MPlug)
        self.assertIsInstance(tx_plug, om.MPlug)

    def test_plug_values(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        fn_dep = om.MFnDependencyNode(transform)

        # Test float value
        tx_plug = fn_dep.findPlug("translateX", False)
        tx_plug.setFloat(5.0)
        self.assertEqual(tx_plug.asFloat(), 5.0)

        # Test bool value
        vis_plug = fn_dep.findPlug("visibility", False)
        vis_plug.setBool(False)
        self.assertEqual(vis_plug.asBool(), False)

    def test_create_attributes(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()

        # Create numeric attribute
        nAttr = om.MFnNumericAttribute()
        testAttr = nAttr.create("testFloat", "tf", om.MFnNumericData.kFloat, 0.0)
        self.dagmod.addAttribute(transform, testAttr)
        self.dagmod.doIt()

        # Create enum attribute
        eAttr = om.MFnEnumAttribute()
        enumAttr = eAttr.create("testEnum", "te")
        eAttr.addField("OptionA", 0)
        eAttr.addField("OptionB", 1)
        self.dagmod.addAttribute(transform, enumAttr)
        self.dagmod.doIt()

    def test_plug_connections(self):
        src_node = self.dagmod.createNode("transform")
        dst_node = self.dagmod.createNode("transform")
        self.dagmod.doIt()

        fn_src = om.MFnDependencyNode(src_node)
        fn_dst = om.MFnDependencyNode(dst_node)

        src_plug = fn_src.findPlug("translateX", False)
        dst_plug = fn_dst.findPlug("translateX", False)

        # Connect plugs
        self.dagmod.connect(src_plug, dst_plug)
        self.dagmod.doIt()
        self.assertTrue(src_plug.isConnected)
        self.assertTrue(dst_plug.isConnected)
        if self.host == "python":
            self.assertIn(dst_plug, src_plug.connectedTo(0, 1)._plugs)

        # Disconnect plugs
        self.dagmod.disconnect(src_plug, dst_plug)
        self.dagmod.doIt()
        self.assertFalse(src_plug.isConnected)
        self.assertFalse(dst_plug.isConnected)

    def test_delete_node_and_undo(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        self.assertTrue(transform.isNull() == False)

        self.dagmod.deleteNode(transform)
        self.dagmod.doIt()
        self.assertTrue(transform.isNull() == False)

        self.dagmod.undoIt()
        self.assertTrue(transform.isNull() == False)
        if self.host == "python":
            self.assertTrue(hierarchy.NodePool.object_exists(transform))

    def test_create_node_with_shape_manual(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        cam = self.dagmod.createNode("camera", parent=transform)
        self.dagmod.doIt()

        self.assertTrue(cam.isNull() == False)

        cam_fn = om.MFnDagNode(cam)
        transform_fn = om.MFnDagNode(transform)
        self.assertEqual(transform_fn.childCount(), 1)
        self.assertEqual(
            om.MFnDagNode(cam_fn.parent(0)).fullPathName(), transform_fn.fullPathName()
        )

    def test_create_node_with_shape_auto(self):
        # returns the transform node bc no parent is provided
        trn_obj = om.MFnDagNode().create("mesh", name="some_mesh")
        trn = om.MFnDagNode(trn_obj)

        self.assertTrue(trn_obj.isNull() == False)
        self.assertEqual(trn_obj.apiType(), om.MFn.kTransform)
        self.assertEqual(trn.childCount(), 1)

        shape = om.MFnDagNode(trn.child(0))
        self.assertEqual(shape.object().apiType(), om.MFn.kMesh)
        self.assertEqual(shape.name(), "some_mesh")

        crv_trn_o = om.MFnDagNode().create("nurbsCurve")
        crv_trn = om.MFnDagNode(crv_trn_o)
        crv_shape = om.MFnDagNode(crv_trn.child(0))
        self.assertEqual(crv_trn_o.apiType(), om.MFn.kTransform)
        self.assertEqual(crv_trn.childCount(), 1)
        self.assertEqual(crv_trn.name(), "curve1")
        self.assertEqual(crv_shape.name(), "curveShape1")
        self.assertEqual(crv_shape.object().apiType(), om.MFn.kNurbsCurve)

    def test_delete_node_hierarchy(self):
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        cam = self.dagmod.createNode("camera", parent=transform)
        self.dagmod.doIt()

        self.dagmod.deleteNode(transform)
        self.dagmod.doIt()

        self.assertTrue(transform.isNull() == False)
        self.assertTrue(cam.isNull() == False)

        if self.host == "python":
            self.assertFalse(mc.objExists(transform._name))
            self.assertFalse(mc.objExists(cam._name))

    def test_dap_path(self):
        grandparent = self.dagmod.createNode("transform")
        self.dagmod.renameNode(grandparent, "grandparent")
        parent = self.dagmod.createNode("transform", parent=grandparent)
        self.dagmod.renameNode(parent, "parent")
        child = self.dagmod.createNode("transform", parent=parent)
        self.dagmod.renameNode(child, "child")
        self.dagmod.doIt()

        dag_path = om.MDagPath.getAPathTo(parent)
        self.assertEqual(dag_path.length(), 2)
        self.assertEqual(dag_path.node().apiTypeStr, "kTransform")
        self.assertEqual(dag_path.fullPathName(), "|grandparent|parent")
        self.assertEqual(dag_path.partialPathName(), "parent")
        self.assertEqual(dag_path.child(0), child)
        self.assertEqual(dag_path.node(), parent)
        dag_path.pop()
        self.assertEqual(dag_path.node(), grandparent)
        self.assertEqual(dag_path.fullPathName(), "|grandparent")

        dag_path = om.MFnDagNode(parent).getPath()
        self.assertEqual(dag_path.length(), 2)
        self.assertEqual(dag_path.node().apiTypeStr, "kTransform")
        self.assertEqual(dag_path.fullPathName(), "|grandparent|parent")
        self.assertEqual(dag_path.partialPathName(), "parent")
        self.assertEqual(dag_path.child(0), child)
        self.assertEqual(dag_path.node(), parent)
        dag_path.pop()
        self.assertEqual(dag_path.node(), grandparent)
        self.assertEqual(dag_path.fullPathName(), "|grandparent")

    def test_MItDag(self):
        mc.file(new=True, force=True)
        dagmod = om.MDagModifier()
        grandparent = dagmod.createNode("transform")
        dagmod.renameNode(grandparent, "grandparent")
        parent = dagmod.createNode("transform", parent=grandparent)
        dagmod.renameNode(parent, "parent")
        child = dagmod.createNode("transform", parent=parent)
        dagmod.renameNode(child, "child")
        dagmod.doIt()

        ls = [grandparent, parent, child]
        ls_copy = ls.copy()

        it_dag = om.MItDag(om.MItDag.kDepthFirst)
        while not it_dag.isDone():
            if it_dag.currentItem() in ls_copy:
                ls.pop()
            it_dag.next()

        self.assertEqual(len(ls), 0)

        # Test MItDag with filter
        great_grandchild = dagmod.createNode("joint", parent=child)
        dagmod.renameNode(great_grandchild, "great_grandchild")
        dagmod.doIt()
        it_dag = om.MItDag(om.MItDag.kDepthFirst)
        it_dag.reset(grandparent, filterType=om.MFn.kJoint)
        ls = [grandparent, parent, child, great_grandchild]
        while not it_dag.isDone():
            mobj = it_dag.currentItem()
            if mobj in ls:
                ls.remove(mobj)
            it_dag.next()
        self.assertEqual(len(ls), 3)
        self.assertEqual(mobj, great_grandchild)

    def test_duplicate_dag(self):
        dagmod = om.MDagModifier()
        grandparent = dagmod.createNode("transform")
        dagmod.renameNode(grandparent, "grandparent")
        parent = dagmod.createNode("transform", parent=grandparent)
        dagmod.renameNode(parent, "parent")
        child = dagmod.createNode("transform", parent=parent)
        dagmod.renameNode(child, "child")
        dagmod.doIt()

        gp = om.MFnDagNode(grandparent)
        gp_dup = om.MFnDagNode(gp.duplicate())
        self.assertEqual(gp_dup.name(), "grandparent1")
        itertator = om.MItDag(om.MItDag.kDepthFirst)
        itertator.reset(gp_dup.object())
        predicted_names = {"grandparent1", "parent1", "child1"}
        uuids = {
            om.MFnDagNode(grandparent).uuid().asString(),
            om.MFnDagNode(parent).uuid().asString(),
            om.MFnDagNode(child).uuid().asString(),
        }
        while not itertator.isDone():
            as_nd = om.MFnDagNode(itertator.currentItem())
            self.assertIn(as_nd.name(), predicted_names)
            self.assertNotIn(as_nd.uuid().asString(), uuids)
            itertator.next()

    def test_local_and_world_matrices(self):
        # Create a transform node and set translation, rotation, scale
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        fn_dep = om.MFnDependencyNode(transform)
        fn_tr = om.MFnTransform(transform)

        # Set translation, rotation, scale
        fn_tr.setTranslation(om.MVector(1.0, 2.0, 3.0), om.MSpace.kTransform)
        fn_tr.setRotation(om.MEulerRotation([0.1, 0.2, 0.3]), om.MTransformationMatrix.kXYZ)
        fn_tr.setScale([2.0, 3.0, 4.0])

        # Get local matrix
        local_matrix = fn_tr.transformation().asMatrix()
        # Get world matrix (should be same as local since no parent)
        world_matrix = fn_tr.transformation().asMatrix()

        # Check that local and world matrices are equal for root node
        self.assertTrue(all(
            abs(local_matrix[i][j] - world_matrix[i][j]) < 1e-6
            for i in range(4) for j in range(4)
        ))

        # Create a parent node and parent the transform under it
        parent = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        parent_fn = om.MFnTransform(parent)
        parent_fn.setTranslation(om.MVector(10.0, 0.0, 0.0), om.MSpace.kTransform)
        # Parent the transform node
        dag_mod = om.MDagModifier()
        dag_mod.reparentNode(transform, parent)
        dag_mod.doIt()

        # Get updated world matrix for child
        fn_tr = om.MFnTransform(transform)
        dag_path = om.MDagPath.getAPathTo(transform)
        world_matrix = dag_path.inclusiveMatrix()
        local_matrix = fn_tr.transformation().asMatrix()

    def test_rotations(self):
        # Create a transform node and set rotation
        transform = self.dagmod.createNode("transform")
        self.dagmod.doIt()
        fn_tr = om.MFnTransform(transform)

        # Set rotation using Euler angles
        euler_rotation = om.MEulerRotation(0.1, 0.2, 0.3)
        fn_tr.setRotation(euler_rotation)

        # Get the rotation as Euler angles
        rotation = fn_tr.rotation(om.MSpace.kTransform)
        self.assertAlmostEqual(rotation.x, euler_rotation.x)
        self.assertAlmostEqual(rotation.y, euler_rotation.y)
        self.assertAlmostEqual(rotation.z, euler_rotation.z)

        # Get transformation matrix and check rotation
        transformation_matrix = fn_tr.transformation()
        self.assertAlmostEqual(transformation_matrix.rotation().x, euler_rotation.x)
        self.assertAlmostEqual(transformation_matrix.rotation().y, euler_rotation.y)
        self.assertAlmostEqual(transformation_matrix.rotation().z, euler_rotation.z)

    def test_decompose_matrix(self):
        def decompose_matrix(matrix: np.ndarray) -> tuple:
            # Extract translation
            translation = matrix[:3, 3]

            # Extract 3x3 upper-left matrix
            M = matrix[:3, :3]

            # Extract scale (length of column vectors)
            scale = np.linalg.norm(M, axis=0)

            # Normalize the matrix to extract pure rotation
            norm_matrix = M / scale

            # Create a scipy Rotation object
            rotation = R.from_matrix(norm_matrix)
            rotation = rotation.as_euler('xyz', degrees=False)

            return translation, rotation, scale
        
        # Create a transform node
        dagmod = om.MDagModifier()
        parent = dagmod.createNode("transform")
        dagmod.renameNode(parent, "parent")
        child = dagmod.createNode("transform")
        dagmod.renameNode(child, "child")
        dagmod.doIt()

        ctrn = om.MFnTransform(child)
        ptrn = om.MFnTransform(parent)

        ptrn.setTranslation(om.MVector(1, 2, 3), om.MSpace.kTransform)
        ptrn.setRotation(om.MEulerRotation(0.2, 0.3, 0.4), om.MSpace.kTransform)

        # Set a rotation using Euler angles
        euler_angles = om.MEulerRotation(1,2,3)  # in radians
        ctrn.setRotation(euler_angles, om.MSpace.kTransform)

        cmx = om.MMatrix(ctrn.transformationMatrix())
        # print(f"Transformation Matrix:\n{np.array(cmx).reshape(4, 4)}")
        t, r, s = decompose_matrix(np.array(cmx).reshape(4, 4))
        print(ptrn.translation(om.MSpace.kTransform))


class TestCmds(unittest.TestCase):

    def setUp(self):
        mc.file(new=True, force=True)

    def test_new_scene_cleaning(self):
        mc.createNode("transform", name="transform")
        mc.createNode("transform", name="transform1")
        mc.createNode("transform", name="transform2")
        mc.createNode("mesh", name="mesh")  # will create a transform node as well

        if HOST() == "python":
            from maya import mmc_hierarchy as hierarchy

            self.assertEqual(len(hierarchy.NodePool._node_instances), 5)

        mc.file(new=True, force=True)

        if HOST() == "python":
            from maya import mmc_hierarchy as hierarchy

            self.assertEqual(mc.ls(type="transform"), [])
            self.assertEqual(mc.ls(type="mesh"), [])
        else:
            self.assertEqual(
                set(mc.ls(type="transform")), set(["front", "persp", "side", "top"])
            )
            self.assertEqual(mc.ls(type="mesh"), [])

    def test_create_node(self):
        transform = mc.createNode("transform")
        self.assertTrue(mc.objExists(transform))

        mesh = mc.createNode("mesh")
        self.assertTrue(mc.objExists("polySurfaceShape1"))
        mc.objectType(mesh, isType="mesh")
        mc.objectType(transform, isType="transform")

    def test_create_node_with_name(self):
        transform = mc.createNode("transform", name="testTransform")
        self.assertTrue(mc.objExists(transform))
        self.assertEqual(mc.ls("testTransform")[0], transform)

    def test_ls_all_transforms(self):
        mc.createNode("transform", name="transform1")
        mc.createNode("transform", name="transform2")
        mc.createNode("mesh", name="mesh1")

        transforms = mc.ls(type="transform")
        self.assertIn("transform1", transforms)
        self.assertIn("transform2", transforms)
        self.assertNotIn("mesh1", transforms)

    def test_ls_with_pattern(self):
        mc.createNode("transform", name="testTransform1")
        mc.createNode("transform", name="testTransform2")
        mc.createNode("mesh", name="testMesh")

        test_nodes = mc.ls("test*")
        self.assertIn("testTransform1", test_nodes)
        self.assertIn("testTransform2", test_nodes)
        self.assertIn("testMesh", test_nodes)

    def test_ls_with_long_names(self):
        mc.createNode("transform", name="parent")
        mc.createNode("transform", name="child", parent="parent")

        long_names = mc.ls(long=True)
        self.assertIn("|parent", long_names)
        self.assertIn("|parent|child", long_names)

    def test_ls_with_dag_objects(self):
        mc.createNode("transform", name="parent")
        mc.createNode("transform", name="child", parent="parent")

        dag_objects = mc.ls(dag=True)
        self.assertIn("parent", dag_objects)
        self.assertIn("child", dag_objects)

    def test_ls_with_selection(self):
        mc.createNode("transform", name="parent")
        mc.createNode("transform", name="child", parent="parent")
        self.assertIn("child", mc.ls(selection=True))

        mc.select("parent")
        selection = mc.ls(selection=True)
        self.assertIn("parent", selection)
        self.assertNotIn("child", selection)

    def test_mselectionlist_from_cmds_created(self):
        mc.createNode("transform", name="mmc")

        sel = om.MGlobal.getActiveSelectionList()
        self.assertEqual(sel.length(), 1)

        dep = om.MFnDependencyNode(sel.getDependNode(0))
        self.assertEqual(dep.name(), "mmc")

    def test_about(self):
        about = mc.about(version=True)
        self.assertIsInstance(about, str)


class TestCallbacks(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.callback_ids = []
        self.logger = logging.getLogger("test_callbacks")

    def tearDown(self):

        if HOST() == "python":
            self.assertEqual(
                len(self.callback_ids),
                len(list(om._CALLBACKS_REGISTRY.keys())),
            )

        for callback_id in self.callback_ids:
            om.MMessage.removeCallback(callback_id)

        if HOST() == "python":
            self.assertEqual(
                len(list(om._CALLBACKS_REGISTRY.keys())),
                0,
                "Callbacks were not removed properly",
            )

    def test_node_deleted_cb(self):
        mc.file(new=True, force=True)

        transform = om.MFnTransform(om.MFnTransform().create())
        self.assertTrue(mc.objExists(transform.name()))

        def do_smth_noticeble(*args, **kwargs):
            jnt = mc.createNode("joint", name="created_in_cb")
            self.logger.debug("Node deleted. Creating a different one: {}".format(jnt))
            self.logger.debug(f"Receiving args: {args}, kwargs: {kwargs}")

        self.callback_ids.append(
            om.MDGMessage.addNodeRemovedCallback(
                partial(do_smth_noticeble, "arg1", "arg2", kwarg1="kwarg1"),
                "dependNode",  # Filter for dependency nodes, which is to say all nodes
            )
        )

        mc.delete(transform.name())

        self.assertFalse(mc.objExists(transform.name()))
        self.assertTrue(mc.objExists("created_in_cb"))

    def test_node_created_cb(self):
        mc.file(new=True, force=True)

        # Create a node without any callback
        pma = mc.createNode("multDL", name="mdl")
        self.assertTrue(mc.objExists(pma))

        if HOST() == "python":
            from maya import mmc_hierarchy as hierarchy

            self.assertTrue(hierarchy.NodePool.from_name(pma))

        def do_smth_noticeble(*args, **kwargs):
            sl = om.MSelectionList().add(args[0])
            as_dep = om.MFnDependencyNode(sl.getDependNode(0))
            tx = as_dep.findPlug("input1", False)
            tx.setDouble(10.5)
            print(f"Node created. Receiving args: {args}, kwargs: {kwargs}")

        self.callback_ids.append(
            om.MDGMessage.addNodeAddedCallback(
                partial(do_smth_noticeble, "mdl", "arg2", kwarg1="kwarg1"),
                "dependNode",  # Filter for dependency nodes, which is to say all nodes
            )
        )

        # Create a node with the callback
        mc.createNode("transform", name="berni")

        sl = om.MSelectionList().add("mdl")
        as_dep = om.MFnDependencyNode(sl.getDependNode(0))
        tx = as_dep.findPlug("input1", False)
        self.assertEqual(tx.asDouble(), 10.5)


class TestScene(unittest.TestCase):

    def setUp(self):
        mc.file(new=True, force=True)

    def test_scene_save(self):
        x = mc.createNode("transform", name="transform")
        print(x)

    def test_scene_open(self):
        mc.createNode("transform", name="transform")


class TestNamespaces(unittest.TestCase):

    def setUp(self):
        mc.file(new=True, force=True)

    def test_create_namespace(self):
        mc.namespace(add="testNS")
        namespaces = mc.namespaceInfo(listOnlyNamespaces=True)
        self.assertIn("testNS", namespaces)
        om.MNamespace.namespaceExists(":testNS")

        om.MNamespace.addNamespace("testNS2:bob")
        namespaces = mc.namespaceInfo(listOnlyNamespaces=True)
        self.assertIn("testNS2", namespaces)

    def test_create_node_in_namespace(self):
        mc.namespace(add="testNS")
        om.MNamespace.namespaceExists(":testNS")
        mc.namespace(set="testNS")
        transform = mc.createNode("transform", name="nsTransform")
        self.assertTrue(mc.objExists("testNS:nsTransform"))

        om.MNamespace.addNamespace("testNS2:bob")
        om.MNamespace.namespaceExists(":testNS2:bob")
        mc.namespace(set=":testNS:testNS2:bob")
        transform2 = mc.createNode("transform", name="nsTransform2")
        self.assertTrue(mc.objExists("testNS:testNS2:bob:nsTransform2"))
        mc.namespace(set=":")


if __name__ == "__main__":

    def old_test_runner():
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        for case_class in [TestMayaMockCompletion, TestCmds, TestCallbacks]:
            suite.addTests(loader.loadTestsFromTestCase(case_class))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    try:
        from maya import cmds as mc
        from maya import mel

        reporter = mel.eval("string $tmp = $gCommandReporter;")
        mc.cmdScrollFieldReporter(reporter, e=True, clear=True)
        old_test_runner()

    except Exception as e:
        logging.critical(traceback.format_exc(), e)
