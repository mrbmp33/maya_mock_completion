import logging
import traceback
import unittest
import sys
import pathlib
from maya.api import OpenMaya as om
from maya import cmds as mc

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
        if self.host == 'python':
            self.assertEqual(len(self.dagmod._queue), 1)

        self.dagmod.createNode("joint")
        self.dagmod.createNode("transform")
        self.dagmod.doIt()
        if self.host == 'python':
            self.assertEqual(len(self.dagmod._queue), 2)

        self.dagmod.doIt()

        if self.host == 'python':
            self.assertEqual(self.dagmod._executed, 0)

    def test_create_node_by_string(self):
        transform = self.dagmod.createNode("transform")
        
        self.dagmod.doIt()
        
        self.assertTrue(transform.isNull() == False)
        
        mesh = self.dagmod.createNode("mesh")
        
        self.dagmod.doIt()
        
        self.assertTrue(mesh.isNull() == False)

    def test_create_node_by_typeid(self):
        transform_id = om.MTypeId(0x5846524d)
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
            self.assertIn(
                dst_plug,
                src_plug.connectedTo(0, 1)._plugs
            )
        
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


class TestCmds(unittest.TestCase):

    def setUp(self):
        mc.file(new=True, force=True)
    
    def test_create_node(self):
        transform = mc.createNode("transform")
        self.assertTrue(mc.objExists(transform))
        
        mesh = mc.createNode("mesh")
        self.assertTrue(mc.objExists(mesh))

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
        self.assertIn('child', mc.ls(selection=True))
        
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


if __name__ == '__main__':
    try:
        from maya import cmds as mc
        from maya import mel

        reporter = mel.eval('string $tmp = $gCommandReporter;')
        mc.cmdScrollFieldReporter(reporter, e=True, clear=True)
        
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        for case_class in [TestMayaMockCompletion, TestCmds]:
            suite.addTests(loader.loadTestsFromTestCase(case_class))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    except Exception as e:
        logging.critical(traceback.format_exc(), e)