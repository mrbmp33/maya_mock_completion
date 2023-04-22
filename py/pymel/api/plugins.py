import exceptions

"""
A quick example::

    from pymel.api.plugins import Command
    class testCmd(Command):
        @classmethod
        def createSyntax(cls):
            syntax = om.MSyntax()
            # the node type name
            syntax.addArg(om.MSyntax.kString)
            return syntax

        def doIt(self, args):
            argParser =  om.MArgParser(self.syntax(), args)
            arg = argParser.commandArgumentString(0)
            print "doing it: {}".format(arg)

    testCmd.register()
    cmds.testCmd()
    testCmd.deregister()

An example of a plugin which creates a node::

    import math

    import pymel.api.plugins as plugins
    import maya.OpenMaya as om

    class PymelSineNode(plugins.DependNode):
        '''Example node adapted from maya's example sine node plugin

        Shows how much easier it is to create a plugin node using pymel.api.plugins
        '''
        # For quick testing, if _typeId is not defined, pymel will create one by
        # hashing the node name. For longer-term uses, you should explicitly set
        # own typeId like this
        #
        # (NOTE - if using the automatic typeId generation, the hashlib python
        # builtin library must be functional / working from within maya... due
        # to dynamic library linking issues (ie, libssl, libcrypto), this
        # may not always be the case out-of-the-box on some linux distros
        _typeId = om.MTypeId(0x900FF)

        # by default, the name of the node will be the name of the class - to
        # override and set your own maya node name, do this:
        #_name = 'PymelSineNode'

        @classmethod
        def initialize(cls):
            # input
            nAttr = om.MFnNumericAttribute()
            cls.input = nAttr.create( "input", "in", om.MFnNumericData.kFloat, 0.0 )
            nAttr.setStorable(1)
            cls.addAttribute( cls.input )

            # output
            cls.output = nAttr.create( "output", "out", om.MFnNumericData.kFloat, 0.0 )
            nAttr.setStorable(1)
            nAttr.setWritable(1)
            cls.addAttribute( cls.output )

            # set attributeAffects relationships
            cls.attributeAffects( cls.input, cls.output )

        def compute(self, plug, dataBlock):
            if ( plug == self.output ):
                dataHandle = dataBlock.inputValue( self.input )
                inputFloat = dataHandle.asFloat()
                result = math.sin( inputFloat )
                outputHandle = dataBlock.outputValue( self.output )
                outputHandle.setFloat( result )
                dataBlock.setClean( plug )
                return om.MStatus.kSuccess
            return om.MStatus.kUnknownParameter

    ## initialize the script plug-in
    def initializePlugin(mobject):
        PymelSineNode.register(mobject)

    # uninitialize the script plug-in
    def uninitializePlugin(mobject):
        PymelSineNode.deregister(mobject)
"""

from maya.OpenMayaMPx import MPxTransform as _mpx
from maya.OpenMayaMPx import MPxLocatorNode as _mpxCls

if False:
    from typing import Dict, List, Tuple, Union, Optional


class BasePluginMixin(object):
    @classmethod
    def create(cls): pass

    @classmethod
    def deregister(cls, plugin='None'):
        """
        If using from within a plugin module's ``initializePlugin`` or
        ``uninitializePlugin`` callback, pass along the MObject given to these
        functions.
        """
        pass

    @classmethod
    def getTypeId(cls, nodeName='None'):
        """
        # Defined here just so it can be shared between MPxTransformationMatrix
        # and DependNode
        """
        pass

    @classmethod
    def isRegistered(cls): pass

    @classmethod
    def mayaName(cls): pass

    @classmethod
    def register(cls, plugin='None'):
        """
        Used to register this MPx object wrapper with the maya plugin.
        
        By default the command will be registered to a dummy plugin provided by pymel.
        
        If using from within a plugin module's ``initializePlugin`` or
        ``uninitializePlugin`` callback, pass along the MObject given to these
        functions.
        
        When implementing the derived MPx wrappers, do not override this -
        instead, override _registerOverride
        """
        pass

    __dict__ = None

    __weakref__ = None


class _DummyPluginNodesMaker(object):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    def __init__(self, dummyClasses='None', alreadyCreated='None'): pass

    __dict__ = None

    __weakref__ = None


class PluginError(exceptions.Exception):
    __weakref__ = None


class PyNodeMethod(object):
    """
    Used as a decorator, placed on methods on a plugin node class, to signal
    that these methods should be placed on to PyNode objects constructed for
    the resulting depend nodes.
    
    >>> class FriendlyNode(DependNode):
    ...     _typeId = om.MTypeId(654748)
    ...     @PyNodeMethod
    ...     def introduce(self):
    ...         print "Hi, I'm an instance of a MyNode PyNode - my name is %s!" % self.name()
    >>> FriendlyNode.register()
    >>> import pymel.core as pm
    >>> frank = pm.createNode('FriendlyNode', name='Frank')
    >>> frank.introduce()
    Hi, I'm an instance of a MyNode PyNode - my name is Frank!
    """

    def __init__(self, func, name='None'): pass

    __dict__ = None

    __weakref__ = None


import maya.OpenMayaMPx as mpx


class DependNode(BasePluginMixin, mpx.MPxNode):
    @classmethod
    def getMpxType(cls): pass

    @classmethod
    def getTypeEnum(cls): pass

    @classmethod
    def initialize(cls): pass

    @classmethod
    def isAbstractClass(cls): pass


class FileTranslator(BasePluginMixin, mpx.MPxFileTranslator):
    def defaultExtension(self): pass

    def filter(self): pass

    def identifyFile(self, mfile, buffer, size): pass


class PluginRegistryError(PluginError):
    pass


class Command(BasePluginMixin, mpx.MPxCommand):
    """
    create a subclass of this with a doIt method
    """

    @classmethod
    def createSyntax(cls): pass


class TransformationMatrix(BasePluginMixin, mpx.MPxTransformationMatrix):
    @classmethod
    def deregister(cls, plugin='None'): pass

    @classmethod
    def register(cls, plugin='None'): pass


class EmitterNode(DependNode, mpx.MPxEmitterNode):
    pass


class BlendShape(DependNode, mpx.MPxBlendShape):
    pass


class SurfaceShape(DependNode, mpx.MPxSurfaceShape):
    pass


class ImagePlane(DependNode, mpx.MPxImagePlane):
    pass


class SpringNode(DependNode, mpx.MPxSpringNode):
    pass


class ManipulatorNode(DependNode, mpx.MPxManipulatorNode):
    pass


class Transform(DependNode, _mpx):
    pass


class ParticleAttributeMapperNode(DependNode, mpx.MPxParticleAttributeMapperNode):
    pass


class IkSolverNode(DependNode, mpx.MPxIkSolverNode):
    pass


class LocatorNode(DependNode, _mpxCls):
    pass


class GeometryFilter(DependNode, mpx.MPxGeometryFilter):
    pass


class AlreadyRegisteredError(PluginRegistryError):
    pass


class DeformerNode(DependNode, mpx.MPxDeformerNode):
    pass


class CameraSet(DependNode, mpx.MPxCameraSet):
    pass


class NotRegisteredError(PluginRegistryError):
    pass


class MotionPathNode(DependNode, mpx.MPxMotionPathNode):
    pass


class SkinCluster(DependNode, mpx.MPxSkinCluster):
    pass


class ObjectSet(DependNode, mpx.MPxObjectSet):
    pass


class Constraint(DependNode, mpx.MPxConstraint):
    pass


class ManipContainer(DependNode, mpx.MPxManipContainer):
    pass


class FieldNode(DependNode, mpx.MPxFieldNode):
    pass


class HwShaderNode(DependNode, mpx.MPxHwShaderNode):
    pass


class HardwareShader(DependNode, mpx.MPxHardwareShader):
    pass


class Assembly(DependNode, mpx.MPxAssembly):
    pass


class PolyTrg(DependNode, mpx.MPxPolyTrg):
    pass


class FluidEmitterNode(EmitterNode, mpx.MPxFluidEmitterNode):
    pass


class ComponentShape(SurfaceShape, mpx.MPxComponentShape):
    pass


def unloadAllPlugins(skipErrors='False', exclude="('DirectConnect',)"): pass


def enumToStr():
    """
    Returns a dictionary mapping from an MPxNode node type enum to it's
    string name.
    Useful for debugging purposes.
    """
    pass


def _pluginName(): pass


def _buildMpxNamesToMayaNodes(hierarchy='None'): pass


def _pluginModule(): pass


def _buildMpxNamesToApiEnumNames(dummyClasses='None', dummyNodes='None'): pass


def _unloadPlugin(): pass


def allMPx():
    """
    Returns a list of all MPx classes
    """
    pass


def pluginCommands(pluginName, reportedOnly='False'):
    """
    Returns the list of all commands that the plugin provides, to the best
    of our knowledge.
    
    Note that depending on your version of maya, this may not actually be the
    list of all commands provided.
    """
    pass


def _guessEnumStrFromMpxClass(className): pass


def _createDummyPluginNodeClasses():
    """
    Registers with the dummy pymel plugin a dummy node type for each MPxNode
    subclass
    
    returns a dictionary mapping from MPx class to a pymel dummy class of that
    type
    """
    pass


def uninitializePlugin(mobject):
    """
    do not call directly
    """
    pass


def _pluginFile(): pass


def _buildPluginHierarchy(dummyClasses='None'):
    """
    Dynamically query the mel node hierarchy for all plugin node types
    
    This command must be run from within a running maya session - ie, where
    maya.cmds, etc are accessible.
    """
    pass


def initializePlugin(mobject):
    """
    do not call directly
    """
    pass


def _suggestNewMPxValues(classes='None'): pass


def _getPlugin(object='None'): pass


def mayaPlugins():
    """
    all maya plugins in the maya install directory
    """
    pass


def _buildAll(): pass


def loadAllMayaPlugins():
    """
    will load all maya-installed plugins
    
    WARNING: tthe act of loading all the plugins may crash maya, especially if
    done from a non-GUI session
    """
    pass


def _loadPlugin(): pass


NON_CREATABLE = set()

registered = set()

_new = []

UNREPORTED_COMMANDS = {}

mpxNamesToMayaNodes = {}

_enumToStr = None

mpxClassesToMpxEnums = {}

pyNodeMethods = {}

mpxNamesToEnumNames = {}

mpxNamesToApiEnumNames = {}

missingMPx = []

_allMPx = []

pluginMayaTypes = set()
