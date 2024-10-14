

if False:
    from typing import Dict, List, Tuple, Union, Optional


class MPxAttributePatternFactory(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def createPatternsFromFile(self, *args): pass

    def createPatternsFromString(self, *args): pass

    def name(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class uIntPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxMaterialInformation(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def computeMaterial(self, *args): pass

    def connectAsTexture(self, *args): pass

    def materialInfoIsDirty(self, *args): pass

    def textureDisconnected(self, *args): pass

    def useMaterialAsTexture(self, *args): pass

    @property
    def fInstance(self): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kOverrideDraw = 2

    kSimpleMaterial = 0

    kTexture = 1


class MPxCacheFormat(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def beginReadChunk(self, *args): pass

    def beginWriteChunk(self, *args): pass

    def close(self, *args): pass

    def endReadChunk(self, *args): pass

    def endWriteChunk(self, *args): pass

    def extension(self, *args): pass

    def findChannelName(self, *args): pass

    def findTime(self, *args): pass

    def handlesDescription(self, *args): pass

    def isValid(self, *args): pass

    def open(self, *args): pass

    def readArraySize(self, *args): pass

    def readChannelName(self, *args): pass

    def readDescription(self, *args): pass

    def readDoubleArray(self, *args): pass

    def readDoubleVectorArray(self, *args): pass

    def readFloatArray(self, *args): pass

    def readFloatVectorArray(self, *args): pass

    def readHeader(self, *args): pass

    def readInt32(self, *args): pass

    def readIntArray(self, *args): pass

    def readNextTime(self, *args): pass

    def readTime(self, *args): pass

    def rewind(self, *args): pass

    def writeChannelName(self, *args): pass

    def writeDescription(self, *args): pass

    def writeDoubleArray(self, *args): pass

    def writeDoubleVectorArray(self, *args): pass

    def writeFloatArray(self, *args): pass

    def writeFloatVectorArray(self, *args): pass

    def writeHeader(self, *args): pass

    def writeInt32(self, *args): pass

    def writeIntArray(self, *args): pass

    def writeTime(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kRead = 0

    kReadWrite = 2

    kWrite = 1


class MPxRenderPassImpl(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def frameBufferSemantic(self, *args): pass

    def getDefaultType(self, *args): pass

    def getNumChannels(self, *args): pass

    def isCompatible(self, *args): pass

    def perLightPassContributionSupported(self, *args): pass

    def typesSupported(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kBit = 2048

    kColorSemantic = 1

    kDepthSemantic = 4

    kDirectionVectorSemantic = 3

    kFloat16 = 256

    kFloat32 = 512

    kFloat64 = 1024

    kInt16 = 32

    kInt32 = 64

    kInt64 = 128

    kInt8 = 16

    kInvalidSemantic = 0

    kLabelSemantic = 5

    kMaskSemantic = 6

    kOther = 4096

    kOtherSemantic = 7

    kUInt16 = 2

    kUInt32 = 4

    kUInt64 = 8

    kUInt8 = 1

    kVectorSemantic = 2


class charPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxModelEditorCommand(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def appendSyntax(self, *args): pass

    def doEditFlags(self, *args): pass

    def doQueryFlags(self, *args): pass

    def editorCommandName(self, *args): pass

    def editorMenuScriptName(self, *args): pass

    def makeModelView(self, *args): pass

    def modelView(self, *args): pass

    def setResult(self, *args): pass

    def skipFlagForCreate(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxGlBuffer(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def beginBufferNotify(self, *args): pass

    def bindFbo(self, *args): pass

    def closeFbo(self, *args): pass

    def endBufferNotify(self, *args): pass

    def openFbo(self, *args): pass

    def unbindFbo(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxCommand(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def commandString(self, *args): pass

    def doIt(self, *args): pass

    def hasSyntax(self, *args): pass

    def isHistoryOn(self, *args): pass

    def isUndoable(self, *args): pass

    def redoIt(self, *args): pass

    def setCommandString(self, *args): pass

    def setHistoryOn(self, *args): pass

    def setUndoable(self, *args): pass

    def syntax(self, *args): pass

    def undoIt(self, *args): pass

    @staticmethod
    def appendToResult(*args, **kwargs): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def clearResult(*args, **kwargs): pass

    @staticmethod
    def currentDoubleResult(*args, **kwargs): pass

    @staticmethod
    def currentIntResult(*args, **kwargs): pass

    @staticmethod
    def currentResultType(*args, **kwargs): pass

    @staticmethod
    def currentStringResult(*args, **kwargs): pass

    @staticmethod
    def displayError(*args, **kwargs): pass

    @staticmethod
    def displayInfo(*args, **kwargs): pass

    @staticmethod
    def displayWarning(*args, **kwargs): pass

    @staticmethod
    def getCurrentResult(*args, **kwargs): pass

    @staticmethod
    def isCurrentResultArray(*args, **kwargs): pass

    @staticmethod
    def setResult(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kDouble = 1

    kLong = 0

    kNoArg = 3

    kString = 2


class boolPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxTransformationMatrix(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __eq__(self, *args): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __ne__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def asInterpolationMatrix(self, *args): pass

    def asMatrix(self, *args): pass

    def asMatrixInverse(self, *args): pass

    def asRotateMatrix(self, *args): pass

    def asRotateMatrixInverse(self, *args): pass

    def asScaleMatrix(self, *args): pass

    def asScaleMatrixInverse(self, *args): pass

    def asTransformationMatrix(self, *args): pass

    def assign(self, *args): pass

    def copyValues(self, *args): pass

    def decomposeMatrix(self, *args): pass

    def eulerRotateOrientation(self, *args): pass

    def eulerRotation(self, *args): pass

    def isEquivalent(self, *args): pass

    def reverse(self, *args): pass

    def rotateBy(self, *args): pass

    def rotateOrientation(self, *args): pass

    def rotatePivot(self, *args): pass

    def rotatePivotTranslation(self, *args): pass

    def rotateTo(self, *args): pass

    def rotation(self, *args): pass

    def rotationOrder(self, *args): pass

    def scale(self, *args): pass

    def scaleBy(self, *args): pass

    def scalePivot(self, *args): pass

    def scalePivotTranslation(self, *args): pass

    def scaleTo(self, *args): pass

    def setRotateOrientation(self, *args): pass

    def setRotatePivot(self, *args): pass

    def setRotatePivotTranslation(self, *args): pass

    def setRotationOrder(self, *args): pass

    def setScalePivot(self, *args): pass

    def setScalePivotTranslation(self, *args): pass

    def shear(self, *args): pass

    def shearBy(self, *args): pass

    def shearTo(self, *args): pass

    def transformBy(self, *args): pass

    def translateBy(self, *args): pass

    def translateTo(self, *args): pass

    def translation(self, *args): pass

    def typeId(self, *args): pass

    def unSquishIt(self, *args): pass

    def unSquishMatrix(self, *args): pass

    @staticmethod
    def convertEulerRotationOrder(*args, **kwargs): pass

    @staticmethod
    def convertTransformationRotationOrder(*args, **kwargs): pass

    @staticmethod
    def creator(*args, **kwargs): pass

    @property
    def baseTransformationMatrixId(self): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    identity = None


class MPxGeometryIterator(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def component(self, *args): pass

    def currentPoint(self, *args): pass

    def geometry(self, *args): pass

    def hasNormals(self, *args): pass

    def hasPoints(self, *args): pass

    def index(self, *args): pass

    def indexUnsimplified(self, *args): pass

    def isDone(self, *args): pass

    def iteratorCount(self, *args): pass

    def maxPoints(self, *args): pass

    def next(self, *args): pass

    def point(self, *args): pass

    def reset(self, *args): pass

    def setCurrentPoint(self, *args): pass

    def setMaxPoints(self, *args): pass

    def setObject(self, *args): pass

    def setPoint(self, *args): pass

    def setPointGetNext(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxUIControl(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxMayaAsciiFilterOutput(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __lshift__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxFileResolver(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def performAfterSaveURI(self, *args): pass

    def resolveURI(self, *args): pass

    def resolveURIWithContext(self, *args): pass

    def resolverName(self, *args): pass

    def uriScheme(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def findURIResolverByName(*args, **kwargs): pass

    @staticmethod
    def findURIResolverByScheme(*args, **kwargs): pass

    @staticmethod
    def getURIResolversByName(*args, **kwargs): pass

    @staticmethod
    def getURIResolversByScheme(*args, **kwargs): pass

    @staticmethod
    def numURIResolvers(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kInput = 2

    kNone = 1


class MPxContextCommand(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def appendSyntax(self, *args): pass

    def doEditFlags(self, *args): pass

    def doQueryFlags(self, *args): pass

    def makeObj(self, *args): pass

    def setResult(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class uCharPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MaterialInputData(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    @property
    def ambient(self): pass

    @property
    def diffuse(self): pass

    @property
    def emission(self): pass

    @property
    def hasTransparency(self): pass

    @property
    def shininess(self): pass

    @property
    def specular(self): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxDragAndDropBehavior(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def connectAttrToAttr(self, *args): pass

    def connectAttrToNode(self, *args): pass

    def connectNodeToAttr(self, *args): pass

    def connectNodeToNode(self, *args): pass

    def shouldBeUsedFor(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class doublePtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


from . import OpenMaya


class MFnPlugin(OpenMaya.MFnBase):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addMenuItem(self, *args): pass

    def apiVersion(self, *args): pass

    def deregisterAnimCurveInterpolator(self, *args): pass

    def deregisterAttributePatternFactory(self, *args): pass

    def deregisterCacheFormat(self, *args): pass

    def deregisterCommand(self, *args): pass

    def deregisterConstraintCommand(self, *args): pass

    def deregisterContextCommand(self, *args): pass

    def deregisterControlCommand(self, *args): pass

    def deregisterData(self, *args): pass

    def deregisterDevice(self, *args): pass

    def deregisterDisplayFilter(self, *args): pass

    def deregisterDragAndDropBehavior(self, *args): pass

    def deregisterEvaluator(self, *args): pass

    def deregisterFileTranslator(self, *args): pass

    def deregisterIkSolver(self, *args): pass

    def deregisterImageFile(self, *args): pass

    def deregisterModelEditorCommand(self, *args): pass

    def deregisterNode(self, *args): pass

    def deregisterRenderPassImpl(self, *args): pass

    def deregisterRenderer(self, *args): pass

    def deregisterTopologyEvaluator(self, *args): pass

    def deregisterURIFileResolver(self, *args): pass

    def loadPath(self, *args): pass

    def matrixTypeIdFromXformId(self, *args): pass

    def name(self, *args): pass

    def registerAnimCurveInterpolator(self, *args): pass

    def registerAttributePatternFactory(self, *args): pass

    def registerBakeEngine(self, *args): pass

    def registerCacheFormat(self, *args): pass

    def registerCommand(self, *args): pass

    def registerConstraintCommand(self, *args): pass

    def registerContextCommand(self, *args): pass

    def registerControlCommand(self, *args): pass

    def registerData(self, *args): pass

    def registerDevice(self, *args): pass

    def registerDisplayFilter(self, *args): pass

    def registerDragAndDropBehavior(self, *args): pass

    def registerEvaluator(self, *args): pass

    def registerFileTranslator(self, *args): pass

    def registerIkSolver(self, *args): pass

    def registerImageFile(self, *args): pass

    def registerMaterialInfo(self, *args): pass

    def registerModelEditorCommand(self, *args): pass

    def registerNode(self, *args): pass

    def registerRenderPassImpl(self, *args): pass

    def registerRenderer(self, *args): pass

    def registerShape(self, *args): pass

    def registerTopologyEvaluator(self, *args): pass

    def registerTransform(self, *args): pass

    def registerUI(self, *args): pass

    def registerUIStrings(self, *args): pass

    def registerURIFileResolver(self, *args): pass

    def removeMenuItem(self, *args): pass

    def setName(self, *args): pass

    def setVersion(self, *args): pass

    def type(self, *args): pass

    def unregisterBakeEngine(self, *args): pass

    def unregisterMaterialInfo(self, *args): pass

    def vendor(self, *args): pass

    def version(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def findPlugin(*args, **kwargs): pass

    @staticmethod
    def isNodeRegistered(*args, **kwargs): pass

    @staticmethod
    def registeringCallableScript(*args, **kwargs): pass

    @staticmethod
    def setRegisteringCallableScript(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kDefaultDataLocation = None


class MPxCacheConfigRuleFilter(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def isMatch(self, *args): pass

    def postRulesExecution(self, *args): pass

    def preRulesExecution(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxAnimCurveInterpolator(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def evaluate(self, *args): pass

    def initialize(self, *args): pass

    def typeId(self, *args): pass

    def typeName(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kEvaluateAtKey = 1

    kLockType = 2


class MPxRepresentation(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def activate(self, *args): pass

    def canApplyEdits(self, *args): pass

    def getExternalContent(self, *args): pass

    def getName(self, *args): pass

    def getType(self, *args): pass

    def inactivate(self, *args): pass

    def setExternalContent(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxControlCommand(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def appendSyntax(self, *args): pass

    def clearResult(self, *args): pass

    def doEditFlags(self, *args): pass

    def doQueryFlags(self, *args): pass

    def makeControl(self, *args): pass

    def setResult(self, *args): pass

    def skipFlagForCreate(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxEditData(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def isEqual(self, *args): pass

    def isLessThan(self, *args): pass

    def performIsEqual(self, *args): pass

    def performIsLessThan(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxNode(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addExternalContentForFileAttr(self, *args): pass

    def compute(self, *args): pass

    def connectionBroken(self, *args): pass

    def connectionMade(self, *args): pass

    def copyInternalData(self, *args): pass

    def dependsOn(self, *args): pass

    def existWithoutInConnections(self, *args): pass

    def existWithoutOutConnections(self, *args): pass

    def getExternalContent(self, *args): pass

    def getFilesToArchive(self, *args): pass

    def getInternalValue(self, *args): pass

    def getInternalValueInContext(self, *args): pass

    def internalArrayCount(self, *args): pass

    def isAbstractClass(self, *args): pass

    def isPassiveOutput(self, *args): pass

    def isTrackingTopology(self, *args): pass

    def legalConnection(self, *args): pass

    def legalDisconnection(self, *args): pass

    def name(self, *args): pass

    def passThroughToMany(self, *args): pass

    def passThroughToOne(self, *args): pass

    def postConstructor(self, *args): pass

    def postEvaluation(self, *args): pass

    def preEvaluation(self, *args): pass

    def schedulingType(self, *args): pass

    def setDependentsDirty(self, *args): pass

    def setExistWithoutInConnections(self, *args): pass

    def setExistWithoutOutConnections(self, *args): pass

    def setExternalContent(self, *args): pass

    def setExternalContentForFileAttr(self, *args): pass

    def setInternalValue(self, *args): pass

    def setInternalValueInContext(self, *args): pass

    def shouldSave(self, *args): pass

    def thisMObject(self, *args): pass

    def type(self, *args): pass

    def typeId(self, *args): pass

    def typeName(self, *args): pass

    @staticmethod
    def addAttribute(*args, **kwargs): pass

    @staticmethod
    def attributeAffects(*args, **kwargs): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def inheritAttributesFrom(*args, **kwargs): pass

    @property
    def caching(self): pass

    @property
    def frozen(self): pass

    @property
    def isHistoricallyInteresting(self): pass

    @property
    def message(self): pass

    @property
    def state(self): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kAssembly = 22

    kBlendShape = 25

    kCameraSetNode = 16

    kClientDeviceNode = 20

    kConstraintNode = 17

    kDefaultScheduling = 1

    kDeformerNode = 2

    kDependNode = 0

    kEmitterNode = 6

    kEvaluatedDirectly = 1

    kEvaluatedIndirectly = 0

    kFieldNode = 5

    kFluidEmitterNode = 13

    kGeometryFilter = 24

    kGloballySerial = 2

    kGloballySerialize = 2

    kHardwareShader = 9

    kHwShaderNode = 10

    kIkSolverNode = 8

    kImagePlaneNode = 14

    kLast = 26

    kLeaveDirty = 2

    kLocatorNode = 1

    kManipContainer = 3

    kManipulatorNode = 18

    kMotionPathNode = 19

    kObjectSet = 12

    kParallel = 0

    kParticleAttributeMapperNode = 15

    kPostEvaluationTypeLast = 3

    kSchedulingTypeLast = 4

    kSerial = 1

    kSerialize = 1

    kSkinCluster = 23

    kSpringNode = 7

    kSurfaceShape = 4

    kThreadedDeviceNode = 21

    kTransformNode = 11

    kUntrusted = 3


class MPxImageFile(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def close(self, *args): pass

    def glLoad(self, *args): pass

    def load(self, *args): pass

    def open(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class floatPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxSurfaceShapeUI(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def canDrawUV(self, *args): pass

    def draw(self, *args): pass

    def drawUV(self, *args): pass

    def getDrawData(self, *args): pass

    def getDrawRequests(self, *args): pass

    def material(self, *args): pass

    def materials(self, *args): pass

    def select(self, *args): pass

    def selectUV(self, *args): pass

    def snap(self, *args): pass

    def surfaceShape(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def surfaceShapeUI(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kSelectMeshEdges = 3

    kSelectMeshFaces = 2

    kSelectMeshUVs = 0

    kSelectMeshVerts = 1


class MPxData(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def copy(self, *args): pass

    def name(self, *args): pass

    def readASCII(self, *args): pass

    def readBinary(self, *args): pass

    def typeId(self, *args): pass

    def writeASCII(self, *args): pass

    def writeBinary(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kData = 0

    kGeometryData = 1

    kLast = 2


class MPxMidiInputDevice(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def closeDevice(self, *args): pass

    def deviceState(self, *args): pass

    def doButtonEvents(self, *args): pass

    def doMovementEvents(self, *args): pass

    def getMessage(self, *args): pass

    def nameAxes(self, *args): pass

    def nameButtons(self, *args): pass

    def openDevice(self, *args): pass

    def sendMessage(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxFileTranslator(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def allowMultipleFileOptimization(self, *args): pass

    def canBeOpened(self, *args): pass

    def defaultExtension(self, *args): pass

    def filter(self, *args): pass

    def haveNamespaceSupport(self, *args): pass

    def haveReadMethod(self, *args): pass

    def haveReferenceMethod(self, *args): pass

    def haveWriteMethod(self, *args): pass

    def identifyFile(self, *args): pass

    def reader(self, *args): pass

    def writer(self, *args): pass

    @staticmethod
    def fileAccessMode(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kCouldBeMyFileType = 1

    kExportAccessMode = 5

    kExportActiveAccessMode = 6

    kImportAccessMode = 3

    kIsMyFileType = 0

    kNotMyFileType = 2

    kOpenAccessMode = 1

    kReferenceAccessMode = 2

    kSaveAccessMode = 4

    kUnknownAccessMode = 0


class MPx3dModelView(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def backgroundColor(self, *args): pass

    def backgroundColorBottom(self, *args): pass

    def backgroundColorTop(self, *args): pass

    def beginGL(self, *args): pass

    def beginXorDrawing(self, *args): pass

    def colorAtIndex(self, *args): pass

    def customDraw(self, *args): pass

    def customDrawEnabled(self, *args): pass

    def destroyOnPanelDestruction(self, *args): pass

    def displayAxisAtOriginOn(self, *args): pass

    def displayAxisOn(self, *args): pass

    def displayCameraAnnotationOn(self, *args): pass

    def displayHUD(self, *args): pass

    def displayStyle(self, *args): pass

    def doUpdateOnMove(self, *args): pass

    def drawAdornments(self, *args): pass

    def drawAdornmentsNow(self, *args): pass

    def drawHUDNow(self, *args): pass

    def drawInterrupt(self, *args): pass

    def drawOnePass(self, *args): pass

    def drawText(self, *args): pass

    def endGL(self, *args): pass

    def endXorDrawing(self, *args): pass

    def filteredObjectList(self, *args): pass

    def fogColor(self, *args): pass

    def fogDensity(self, *args): pass

    def fogEnd(self, *args): pass

    def fogMode(self, *args): pass

    def fogSource(self, *args): pass

    def fogStart(self, *args): pass

    def getAsM3dView(self, *args): pass

    def getCamera(self, *args): pass

    def getCameraHUDName(self, *args): pass

    def getCameraSet(self, *args): pass

    def getColorIndexAndTable(self, *args): pass

    def getCurrentCameraSetCamera(self, *args): pass

    def getObjectsToView(self, *args): pass

    def handleDraw(self, *args): pass

    def hasStereoBufferSupport(self, *args): pass

    def includeInvisible(self, *args): pass

    def isBackfaceCulling(self, *args): pass

    def isBackgroundFogEnabled(self, *args): pass

    def isBackgroundGradient(self, *args): pass

    def isFogEnabled(self, *args): pass

    def isShadeActiveOnly(self, *args): pass

    def isTextureDisplayEnabled(self, *args): pass

    def isTwoSidedLighting(self, *args): pass

    def isVisible(self, *args): pass

    def isWireframeOnShaded(self, *args): pass

    def isXrayEnabled(self, *args): pass

    def lightingMode(self, *args): pass

    def multipleDrawEnabled(self, *args): pass

    def multipleDrawPassCount(self, *args): pass

    def name(self, *args): pass

    def numActiveColors(self, *args): pass

    def numDormantColors(self, *args): pass

    def numUserDefinedColors(self, *args): pass

    def objectDisplay(self, *args): pass

    def okForMultipleDraw(self, *args): pass

    def portHeight(self, *args): pass

    def portWidth(self, *args): pass

    def postMultipleDraw(self, *args): pass

    def postMultipleDrawPass(self, *args): pass

    def preMultipleDraw(self, *args): pass

    def preMultipleDrawPass(self, *args): pass

    def processDraw(self, *args): pass

    def refresh(self, *args): pass

    def removingCamera(self, *args): pass

    def requestOkForDraw(self, *args): pass

    def setBackfaceCulling(self, *args): pass

    def setBackgroundFogEnabled(self, *args): pass

    def setCamera(self, *args): pass

    def setCameraInDraw(self, *args): pass

    def setCameraSet(self, *args): pass

    def setCurrentCameraSetCamera(self, *args): pass

    def setCustomDrawEnable(self, *args): pass

    def setDestroyOnPanelDestruction(self, *args): pass

    def setDisplayAxis(self, *args): pass

    def setDisplayAxisAtOrigin(self, *args): pass

    def setDisplayCameraAnnotation(self, *args): pass

    def setDisplayHUD(self, *args): pass

    def setDisplayStyle(self, *args): pass

    def setDoUpdateOnMove(self, *args): pass

    def setDrawAdornments(self, *args): pass

    def setDrawCameraOverride(self, *args): pass

    def setDrawColor(self, *args): pass

    def setDrawInterrupt(self, *args): pass

    def setFogColor(self, *args): pass

    def setFogDensity(self, *args): pass

    def setFogEnabled(self, *args): pass

    def setFogEnd(self, *args): pass

    def setFogMode(self, *args): pass

    def setFogSource(self, *args): pass

    def setFogStart(self, *args): pass

    def setInStereoDrawMode(self, *args): pass

    def setIncludeInvisible(self, *args): pass

    def setLightingMode(self, *args): pass

    def setMultipleDrawEnable(self, *args): pass

    def setObjectDisplay(self, *args): pass

    def setObjectsToView(self, *args): pass

    def setTextureDisplayEnabled(self, *args): pass

    def setTwoSidedLighting(self, *args): pass

    def setUserDefinedColor(self, *args): pass

    def setViewSelected(self, *args): pass

    def setViewSelectedPrefix(self, *args): pass

    def setViewSelectedSet(self, *args): pass

    def setWireframeOnShaded(self, *args): pass

    def setXrayEnabled(self, *args): pass

    def templateColor(self, *args): pass

    def updateViewingParameters(self, *args): pass

    def userDefinedColorIndex(self, *args): pass

    def viewIsFiltered(self, *args): pass

    def viewSelected(self, *args): pass

    def viewSelectedPrefix(self, *args): pass

    def viewSelectedSet(self, *args): pass

    def viewToObjectSpace(self, *args): pass

    def viewToWorld(self, *args): pass

    def viewType(self, *args): pass

    def wantStereoGLBuffer(self, *args): pass

    def worldToView(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def getModelView(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kFogCoordinate = 1

    kFogExponential = 1

    kFogExponentialSquared = 2

    kFogFragment = 0

    kFogLinear = 0

    kLightActive = 2

    kLightAll = 0

    kLightDefault = 3

    kLightNone = 4

    kLightQuality = 5

    kLightSelected = 1


class intPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MExternalContentLocationTable(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addEntry(self, *args): pass

    def getEntryByIndex(self, *args): pass

    def getLocationByKey(self, *args): pass

    def length(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MExternalContentInfoTable(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addResolvedEntry(self, *args): pass

    def addUnresolvedEntry(self, *args): pass

    def getEntryByIndex(self, *args): pass

    def getInfoByKey(self, *args): pass

    def length(self, *args): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxContext(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def abortAction(self, *args): pass

    def addManipulator(self, *args): pass

    def argTypeNumericalInput(self, *args): pass

    def completeAction(self, *args): pass

    def deleteAction(self, *args): pass

    def deleteManipulators(self, *args): pass

    def doDrag(self, *args): pass

    def doEnterRegion(self, *args): pass

    def doHold(self, *args): pass

    def doPress(self, *args): pass

    def doPtrMoved(self, *args): pass

    def doRelease(self, *args): pass

    def feedbackNumericalInput(self, *args): pass

    def helpStateHasChanged(self, *args): pass

    def image(self, *args): pass

    def newToolCommand(self, *args): pass

    def processNumericalInput(self, *args): pass

    def setImage(self, *args): pass

    def stringClassName(self, *args): pass

    def toolOffCleanup(self, *args): pass

    def toolOnSetup(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None

    kImage1 = 0

    kImage2 = 1

    kImage3 = 2


class shortPtr(object):
    def __del__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def assign(self, *args): pass

    def cast(self, *args): pass

    def value(self, *args): pass

    @staticmethod
    def frompointer(*args, **kwargs): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxBakeEngine(object):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def bake(self, *args): pass

    def getUVRange(self, *args): pass

    def setNeedTransparency(self, *args): pass

    @property
    def fInstance(self): pass

    __dict__ = None

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    __weakref__ = None


class MPxGeometryFilter(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def accessoryAttribute(self, *args): pass

    def accessoryNodeSetup(self, *args): pass

    def deform(self, *args): pass

    def getDeformationDetails(self, *args): pass

    def setDeformationDetails(self, *args): pass

    def setModifiedCallback(self, *args): pass

    def setUseExistingConnectionWhenSetEditing(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def envelope(self): pass

    @property
    def groupId(self): pass

    @property
    def input(self): pass

    @property
    def inputGeom(self): pass

    @property
    def outputGeom(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kDeformsAll = 6

    kDeformsColors = 4

    kDeformsUVs = 2


class MPxHwShaderNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def bind(self, *args): pass

    def colorsPerVertex(self, *args): pass

    def currentPath(self, *args): pass

    def currentShadingEngine(self, *args): pass

    def dirtyMask(self, *args): pass

    def geometry(self, *args): pass

    def glBind(self, *args): pass

    def glGeometry(self, *args): pass

    def glUnbind(self, *args): pass

    def hasTransparency(self, *args): pass

    def invertTexCoords(self, *args): pass

    def normalsPerVertex(self, *args): pass

    def provideFaceIDs(self, *args): pass

    def provideLocalUVCoord(self, *args): pass

    def provideVertexIDs(self, *args): pass

    def renderSwatchImage(self, *args): pass

    def supportsBatching(self, *args): pass

    def texCoordsPerVertex(self, *args): pass

    def transparencyOptions(self, *args): pass

    def type(self, *args): pass

    def unbind(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def getHwShaderNodePtr(*args, **kwargs): pass

    @property
    def outColor(self): pass

    @property
    def outColorB(self): pass

    @property
    def outColorG(self): pass

    @property
    def outColorR(self): pass

    @property
    def outGlowColor(self): pass

    @property
    def outGlowColorB(self): pass

    @property
    def outGlowColorG(self): pass

    @property
    def outGlowColorR(self): pass

    @property
    def outMatteOpacity(self): pass

    @property
    def outMatteOpacityB(self): pass

    @property
    def outMatteOpacityG(self): pass

    @property
    def outMatteOpacityR(self): pass

    @property
    def outTransparency(self): pass

    @property
    def outTransparencyB(self): pass

    @property
    def outTransparencyG(self): pass

    @property
    def outTransparencyR(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kDirtyAll = 15

    kDirtyColorArrays = 4

    kDirtyNone = 0

    kDirtyNormalArray = 2

    kDirtyTexCoordArrays = 8

    kDirtyVertexArray = 1

    kIsTransparent = 1

    kNoTransparencyFrontBackCull = 2

    kNoTransparencyPolygonSort = 4

    kWriteAll = 15

    kWriteColorArrays = 4

    kWriteNone = 0

    kWriteNormalArray = 2

    kWriteTexCoordArrays = 8

    kWriteVertexArray = 1


class MPxMayaAsciiFilter(MPxFileTranslator):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def haveReadMethod(self, *args): pass

    def haveWriteMethod(self, *args): pass

    def processReadOptions(self, *args): pass

    def processWriteOptions(self, *args): pass

    def reader(self, *args): pass

    def writePostConnectAttrsBlock(self, *args): pass

    def writePostCreateNodesBlock(self, *args): pass

    def writePostHeader(self, *args): pass

    def writePostRequires(self, *args): pass

    def writePreConnectAttrsBlock(self, *args): pass

    def writePreCreateNodesBlock(self, *args): pass

    def writePreTrailer(self, *args): pass

    def writer(self, *args): pass

    def writesConnectAttr(self, *args): pass

    def writesCreateNode(self, *args): pass

    def writesDisconnectAttr(self, *args): pass

    def writesFileReference(self, *args): pass

    def writesMetadata(self, *args): pass

    def writesParentNode(self, *args): pass

    def writesRequirements(self, *args): pass

    def writesSelectNode(self, *args): pass

    def writesSetAttr(self, *args): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxEmitterNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def compute(self, *args): pass

    def draw(self, *args): pass

    def evalEmission2dTexture(self, *args): pass

    def getCurrentTime(self, *args): pass

    def getDeltaTime(self, *args): pass

    def getEmitterType(self, *args): pass

    def getMaxDistance(self, *args): pass

    def getMinDistance(self, *args): pass

    def getOwnerShape(self, *args): pass

    def getRandomSeed(self, *args): pass

    def getRandomState(self, *args): pass

    def getRate(self, *args): pass

    def getStartTime(self, *args): pass

    def getWorldMatrix(self, *args): pass

    def getWorldPosition(self, *args): pass

    def hasValidEmission2dTexture(self, *args): pass

    def randgen(self, *args): pass

    def resetRandomState(self, *args): pass

    def setRandomState(self, *args): pass

    def type(self, *args): pass

    def volumePrimitiveBoundingBox(self, *args): pass

    def volumePrimitiveDistanceFromAxis(self, *args): pass

    def volumePrimitivePointInside(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def mCurrentTime(self): pass

    @property
    def mDeltaTime(self): pass

    @property
    def mDirection(self): pass

    @property
    def mDirectionX(self): pass

    @property
    def mDirectionY(self): pass

    @property
    def mDirectionZ(self): pass

    @property
    def mEmitterType(self): pass

    @property
    def mInheritFactor(self): pass

    @property
    def mIsFull(self): pass

    @property
    def mMaxDistance(self): pass

    @property
    def mMinDistance(self): pass

    @property
    def mOutput(self): pass

    @property
    def mOwnerCentroid(self): pass

    @property
    def mOwnerCentroidX(self): pass

    @property
    def mOwnerCentroidY(self): pass

    @property
    def mOwnerCentroidZ(self): pass

    @property
    def mOwnerPosData(self): pass

    @property
    def mOwnerVelData(self): pass

    @property
    def mRandState(self): pass

    @property
    def mRandStateX(self): pass

    @property
    def mRandStateY(self): pass

    @property
    def mRandStateZ(self): pass

    @property
    def mRate(self): pass

    @property
    def mSeed(self): pass

    @property
    def mSpeed(self): pass

    @property
    def mStartTime(self): pass

    @property
    def mSweptGeometry(self): pass

    @property
    def mWorldMatrix(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kCurve = 3

    kDirectional = 0

    kOmni = 1

    kSurface = 2

    kVolume = 4


class MPxMotionPathNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def banking(self, *args): pass

    def evaluatePath(self, *args): pass

    def fractionalToParametric(self, *args): pass

    def getVectors(self, *args): pass

    def matrix(self, *args): pass

    def parametricToFractional(self, *args): pass

    def position(self, *args): pass

    def type(self, *args): pass

    def wraparoundFractionalValue(self, *args): pass

    @property
    def allCoordinates(self): pass

    @property
    def bank(self): pass

    @property
    def bankScale(self): pass

    @property
    def bankThreshold(self): pass

    @property
    def flowNode(self): pass

    @property
    def follow(self): pass

    @property
    def fractionMode(self): pass

    @property
    def frontAxis(self): pass

    @property
    def frontTwist(self): pass

    @property
    def inverseFront(self): pass

    @property
    def inverseUp(self): pass

    @property
    def normal(self): pass

    @property
    def orientMatrix(self): pass

    @property
    def orientationMarkerTime(self): pass

    @property
    def pathGeometry(self): pass

    @property
    def positionMarkerTime(self): pass

    @property
    def rotate(self): pass

    @property
    def rotateOrder(self): pass

    @property
    def rotateX(self): pass

    @property
    def rotateY(self): pass

    @property
    def rotateZ(self): pass

    @property
    def sideTwist(self): pass

    @property
    def uValue(self): pass

    @property
    def upAxis(self): pass

    @property
    def upTwist(self): pass

    @property
    def updateOrientationMarkers(self): pass

    @property
    def worldUpMatrix(self): pass

    @property
    def worldUpType(self): pass

    @property
    def worldUpVector(self): pass

    @property
    def worldUpVectorX(self): pass

    @property
    def worldUpVectorY(self): pass

    @property
    def worldUpVectorZ(self): pass

    @property
    def xCoordinate(self): pass

    @property
    def yCoordinate(self): pass

    @property
    def zCoordinate(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kUpNormal = 4

    kUpObject = 1

    kUpObjectRotation = 2

    kUpScene = 0

    kUpVector = 3


class MPxUITableControl(MPxUIControl):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addToSelection(self, *args): pass

    def allowEdit(self, *args): pass

    def allowSelection(self, *args): pass

    def cellString(self, *args): pass

    def clearSelection(self, *args): pass

    def collapseOrExpandRow(self, *args): pass

    def getCellColor(self, *args): pass

    def isSelected(self, *args): pass

    def labelString(self, *args): pass

    def numberOfColumns(self, *args): pass

    def numberOfRows(self, *args): pass

    def redrawCells(self, *args): pass

    def redrawLabels(self, *args): pass

    def removeFromSelection(self, *args): pass

    def setNumberOfColumns(self, *args): pass

    def setNumberOfRows(self, *args): pass

    def setSelection(self, *args): pass

    def suspendUpdates(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kAllLabels = 3

    kColumnLabel = 2

    kNoLabel = 0

    kRowLabel = 1


class MPxConstraintCommand(MPxCommand):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def aimVectorAttribute(self, *args): pass

    def appendSyntax(self, *args): pass

    def connectObjectAndConstraint(self, *args): pass

    def connectTarget(self, *args): pass

    def constraintEnableRestAttribute(self, *args): pass

    def constraintInstancedAttribute(self, *args): pass

    def constraintNode(self, *args): pass

    def constraintOutputAttribute(self, *args): pass

    def constraintRestAttribute(self, *args): pass

    def constraintTargetAttribute(self, *args): pass

    def constraintTargetInstancedAttribute(self, *args): pass

    def constraintTargetWeightAttribute(self, *args): pass

    def constraintTypeId(self, *args): pass

    def createdConstraint(self, *args): pass

    def doCreate(self, *args): pass

    def doEdit(self, *args): pass

    def doIt(self, *args): pass

    def doQuery(self, *args): pass

    def getObjectAttributesArray(self, *args): pass

    def handleNewTargets(self, *args): pass

    def hasVectorFlags(self, *args): pass

    def objectAttribute(self, *args): pass

    def offsetAttribute(self, *args): pass

    def parseArgs(self, *args): pass

    def redoIt(self, *args): pass

    def setRestPosition(self, *args): pass

    def supportsOffset(self, *args): pass

    def targetType(self, *args): pass

    def undoIt(self, *args): pass

    def upVectorAttribute(self, *args): pass

    def worldUpMatrixAttribute(self, *args): pass

    def worldUpTypeAttribute(self, *args): pass

    def worldUpVectorAttribute(self, *args): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kGeometryShape = 1

    kLast = 2

    kTransform = 0


class MPxManipulatorNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addDependentPlug(self, *args): pass

    def addDoubleValue(self, *args): pass

    def addPointValue(self, *args): pass

    def addVectorValue(self, *args): pass

    def colorAndName(self, *args): pass

    def connectPlugToValue(self, *args): pass

    def connectToDependNode(self, *args): pass

    def dependentPlugsReset(self, *args): pass

    def deregisterForMouseMove(self, *args): pass

    def dimmedColor(self, *args): pass

    def doDrag(self, *args): pass

    def doMove(self, *args): pass

    def doPress(self, *args): pass

    def doRelease(self, *args): pass

    def draw(self, *args): pass

    def finishAddingManips(self, *args): pass

    def getDoubleValue(self, *args): pass

    def getInstancePtr(self, *args): pass

    def getPointValue(self, *args): pass

    def getVectorValue(self, *args): pass

    def glActiveName(self, *args): pass

    def glFirstHandle(self, *args): pass

    def labelBackgroundColor(self, *args): pass

    def labelColor(self, *args): pass

    def lineColor(self, *args): pass

    def mainColor(self, *args): pass

    def mouseDown(self, *args): pass

    def mousePosition(self, *args): pass

    def mouseRay(self, *args): pass

    def mouseRayWorld(self, *args): pass

    def mouseUp(self, *args): pass

    def prevColor(self, *args): pass

    def registerForMouseMove(self, *args): pass

    def selectedColor(self, *args): pass

    def setDoubleValue(self, *args): pass

    def setHandleColor(self, *args): pass

    def setInstancePtr(self, *args): pass

    def setPointValue(self, *args): pass

    def setVectorValue(self, *args): pass

    def shouldDrawHandleAsSelected(self, *args): pass

    def xColor(self, *args): pass

    def yColor(self, *args): pass

    def zColor(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def newManipulator(*args, **kwargs): pass

    @property
    def connectedNodes(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxGeometryData(MPxData):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def copy(self, *args): pass

    def deleteComponent(self, *args): pass

    def deleteComponentsFromGroups(self, *args): pass

    def iterator(self, *args): pass

    def matrix(self, *args): pass

    def name(self, *args): pass

    def setMatrix(self, *args): pass

    def smartCopy(self, *args): pass

    def typeId(self, *args): pass

    def updateCompleteVertexGroup(self, *args): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxSurfaceShape(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def acceptsGeometryIterator(self, *args): pass

    def activeComponents(self, *args): pass

    def boundingBox(self, *args): pass

    def cachedShapeAttr(self, *args): pass

    def canMakeLive(self, *args): pass

    def childChanged(self, *args): pass

    def closestPoint(self, *args): pass

    def componentToPlugs(self, *args): pass

    def convertToTweakNodePlug(self, *args): pass

    def createFullRenderGroup(self, *args): pass

    def createFullVertexGroup(self, *args): pass

    def deleteComponents(self, *args): pass

    def evalNodeAffectsDrawDb(self, *args): pass

    def excludeAsPluginShape(self, *args): pass

    def geometryData(self, *args): pass

    def geometryIteratorSetup(self, *args): pass

    def getComponentSelectionMask(self, *args): pass

    def getShapeSelectionMask(self, *args): pass

    def getWorldMatrix(self, *args): pass

    def hasActiveComponents(self, *args): pass

    def isBounded(self, *args): pass

    def isRenderable(self, *args): pass

    def localShapeInAttr(self, *args): pass

    def localShapeOutAttr(self, *args): pass

    def match(self, *args): pass

    def matchComponent(self, *args): pass

    def newControlPointComponent(self, *args): pass

    def pointAtParm(self, *args): pass

    def renderGroupComponentType(self, *args): pass

    def setRenderable(self, *args): pass

    def transformUsing(self, *args): pass

    def tweakUsing(self, *args): pass

    def type(self, *args): pass

    def undeleteComponents(self, *args): pass

    def vertexOffsetDirection(self, *args): pass

    def weightedTransformUsing(self, *args): pass

    def weightedTweakUsing(self, *args): pass

    def worldShapeOutAttr(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def boundingBoxCenterX(self): pass

    @property
    def boundingBoxCenterY(self): pass

    @property
    def boundingBoxCenterZ(self): pass

    @property
    def center(self): pass

    @property
    def instObjGroups(self): pass

    @property
    def intermediateObject(self): pass

    @property
    def inverseMatrix(self): pass

    @property
    def isTemplated(self): pass

    @property
    def mControlPoints(self): pass

    @property
    def mControlValueX(self): pass

    @property
    def mControlValueY(self): pass

    @property
    def mControlValueZ(self): pass

    @property
    def mHasHistoryOnCreate(self): pass

    @property
    def matrix(self): pass

    @property
    def nodeBoundingBox(self): pass

    @property
    def nodeBoundingBoxMax(self): pass

    @property
    def nodeBoundingBoxMaxX(self): pass

    @property
    def nodeBoundingBoxMaxY(self): pass

    @property
    def nodeBoundingBoxMaxZ(self): pass

    @property
    def nodeBoundingBoxMin(self): pass

    @property
    def nodeBoundingBoxMinX(self): pass

    @property
    def nodeBoundingBoxMinY(self): pass

    @property
    def nodeBoundingBoxMinZ(self): pass

    @property
    def nodeBoundingBoxSize(self): pass

    @property
    def nodeBoundingBoxSizeX(self): pass

    @property
    def nodeBoundingBoxSizeY(self): pass

    @property
    def nodeBoundingBoxSizeZ(self): pass

    @property
    def objectColor(self): pass

    @property
    def objectGroupColor(self): pass

    @property
    def objectGroupId(self): pass

    @property
    def objectGroups(self): pass

    @property
    def objectGrpCompList(self): pass

    @property
    def parentInverseMatrix(self): pass

    @property
    def parentMatrix(self): pass

    @property
    def useObjectColor(self): pass

    @property
    def visibility(self): pass

    @property
    def worldInverseMatrix(self): pass

    @property
    def worldMatrix(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kBoundingBoxChanged = 1

    kMatchInvalidAttribute = 4

    kMatchInvalidAttributeDim = 7

    kMatchInvalidAttributeIndex = 5

    kMatchInvalidAttributeRange = 6

    kMatchInvalidName = 3

    kMatchNone = 1

    kMatchOk = 0

    kMatchTooMany = 2

    kNoPointCaching = 0

    kNormal = 0

    kObjectChanged = 0

    kRestorePoints = 2

    kSavePoints = 1

    kTransformOriginalPoints = 4

    kUTangent = 1

    kUVNTriad = 3

    kUpdatePoints = 3

    kVTangent = 2


class MPxSelectionContext(MPxContext):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def abortAction(self, *args): pass

    def addManipulator(self, *args): pass

    def argTypeNumericalInput(self, *args): pass

    def deleteManipulators(self, *args): pass

    def doDrag(self, *args): pass

    def doHold(self, *args): pass

    def doPress(self, *args): pass

    def doRelease(self, *args): pass

    def feedbackNumericalInput(self, *args): pass

    def helpStateHasChanged(self, *args): pass

    def image(self, *args): pass

    def newToolCommand(self, *args): pass

    def processNumericalInput(self, *args): pass

    def setAllowDoubleClickAction(self, *args): pass

    def setAllowPreSelectHilight(self, *args): pass

    def setAllowSoftSelect(self, *args): pass

    def setAllowSymmetry(self, *args): pass

    def setImage(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxPolyTrg(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def compute(self, *args): pass

    def isAbstractClass(self, *args): pass

    def postConstructor(self, *args): pass

    def registerTrgFunction(self, *args): pass

    def unregisterTrgFunction(self, *args): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxSpringNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def applySpringLaw(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def mDeltaTime(self): pass

    @property
    def mEnd1Weight(self): pass

    @property
    def mEnd2Weight(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxLocatorNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def boundingBox(self, *args): pass

    def closestPoint(self, *args): pass

    def color(self, *args): pass

    def colorRGB(self, *args): pass

    def draw(self, *args): pass

    def drawLast(self, *args): pass

    def excludeAsLocator(self, *args): pass

    def getShapeSelectionMask(self, *args): pass

    def isBounded(self, *args): pass

    def isTransparent(self, *args): pass

    def type(self, *args): pass

    def useClosestPointForSelection(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def boundingBoxCenterX(self): pass

    @property
    def boundingBoxCenterY(self): pass

    @property
    def boundingBoxCenterZ(self): pass

    @property
    def center(self): pass

    @property
    def instObjGroups(self): pass

    @property
    def intermediateObject(self): pass

    @property
    def inverseMatrix(self): pass

    @property
    def isTemplated(self): pass

    @property
    def localPosition(self): pass

    @property
    def localPositionX(self): pass

    @property
    def localPositionY(self): pass

    @property
    def localPositionZ(self): pass

    @property
    def localScale(self): pass

    @property
    def localScaleX(self): pass

    @property
    def localScaleY(self): pass

    @property
    def localScaleZ(self): pass

    @property
    def matrix(self): pass

    @property
    def nodeBoundingBox(self): pass

    @property
    def nodeBoundingBoxMax(self): pass

    @property
    def nodeBoundingBoxMaxX(self): pass

    @property
    def nodeBoundingBoxMaxY(self): pass

    @property
    def nodeBoundingBoxMaxZ(self): pass

    @property
    def nodeBoundingBoxMin(self): pass

    @property
    def nodeBoundingBoxMinX(self): pass

    @property
    def nodeBoundingBoxMinY(self): pass

    @property
    def nodeBoundingBoxMinZ(self): pass

    @property
    def nodeBoundingBoxSize(self): pass

    @property
    def nodeBoundingBoxSizeX(self): pass

    @property
    def nodeBoundingBoxSizeY(self): pass

    @property
    def nodeBoundingBoxSizeZ(self): pass

    @property
    def objectColor(self): pass

    @property
    def objectGroupColor(self): pass

    @property
    def objectGroupId(self): pass

    @property
    def objectGroups(self): pass

    @property
    def objectGrpCompList(self): pass

    @property
    def parentInverseMatrix(self): pass

    @property
    def parentMatrix(self): pass

    @property
    def underWorldObject(self): pass

    @property
    def useObjectColor(self): pass

    @property
    def visibility(self): pass

    @property
    def worldInverseMatrix(self): pass

    @property
    def worldMatrix(self): pass

    @property
    def worldPosition(self): pass

    @property
    def worldPositionX(self): pass

    @property
    def worldPositionY(self): pass

    @property
    def worldPositionZ(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxIkSolverNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def create(self, *args): pass

    def doSolve(self, *args): pass

    def funcValueTolerance(self, *args): pass

    def groupHandlesByTopology(self, *args): pass

    def handleGroup(self, *args): pass

    def hasJointLimitSupport(self, *args): pass

    def hasUniqueSolution(self, *args): pass

    def isAttributeCreatedBySolver(self, *args): pass

    def isPositionOnly(self, *args): pass

    def isSingleChainOnly(self, *args): pass

    def maxIterations(self, *args): pass

    def positionOnly(self, *args): pass

    def postSolve(self, *args): pass

    def preSolve(self, *args): pass

    def rotatePlane(self, *args): pass

    def setFuncValueTolerance(self, *args): pass

    def setHandleGroup(self, *args): pass

    def setMaxIterations(self, *args): pass

    def setPositionOnly(self, *args): pass

    def setRotatePlane(self, *args): pass

    def setSingleChainOnly(self, *args): pass

    def setSupportJointLimits(self, *args): pass

    def setUniqueSolution(self, *args): pass

    def singleChainOnly(self, *args): pass

    def snapHandle(self, *args): pass

    def solverTypeName(self, *args): pass

    def supportJointLimits(self, *args): pass

    def toSolverSpace(self, *args): pass

    def toWorldSpace(self, *args): pass

    def type(self, *args): pass

    def uniqueSolution(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxMultiPolyTweakUVCommand(MPxCommand):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def getTweakedUVs(self, *args): pass

    def parseSyntax(self, *args): pass

    def preProcessUVs(self, *args): pass

    @staticmethod
    def newSyntax(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxObjectSet(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def canBeDeleted(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def DNSetMembers(self): pass

    @property
    def annotation(self): pass

    @property
    def dagSetMembers(self): pass

    @property
    def edgesOnlySet(self): pass

    @property
    def editPointsOnlySet(self): pass

    @property
    def facetsOnlySet(self): pass

    @property
    def groupNodes(self): pass

    @property
    def isLayer(self): pass

    @property
    def memberWireframeColor(self): pass

    @property
    def partition(self): pass

    @property
    def renderableOnlySet(self): pass

    @property
    def usedByNodes(self): pass

    @property
    def verticesOnlySet(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxCameraSet(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def active(self): pass

    @property
    def camera(self): pass

    @property
    def cameraLayer(self): pass

    @property
    def order(self): pass

    @property
    def sceneData(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxParticleAttributeMapperNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def compute(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def computeNode(self): pass

    @property
    def computeNodeColor(self): pass

    @property
    def computeNodeColorB(self): pass

    @property
    def computeNodeColorG(self): pass

    @property
    def computeNodeColorR(self): pass

    @property
    def outColorPP(self): pass

    @property
    def outMaxValue(self): pass

    @property
    def outMinValue(self): pass

    @property
    def outValuePP(self): pass

    @property
    def time(self): pass

    @property
    def uCoordPP(self): pass

    @property
    def vCoordPP(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxManipContainer(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def addCircleSweepManip(self, *args): pass

    def addCurveSegmentManip(self, *args): pass

    def addDirectionManip(self, *args): pass

    def addDiscManip(self, *args): pass

    def addDistanceManip(self, *args): pass

    def addFreePointTriadManip(self, *args): pass

    def addMPxManipulatorNode(self, *args): pass

    def addManipToPlugConversion(self, *args): pass

    def addPlugToInViewEditor(self, *args): pass

    def addPlugToManipConversion(self, *args): pass

    def addPointOnCurveManip(self, *args): pass

    def addPointOnSurfaceManip(self, *args): pass

    def addRotateManip(self, *args): pass

    def addScaleManip(self, *args): pass

    def addStateManip(self, *args): pass

    def addToggleManip(self, *args): pass

    def connectToDependNode(self, *args): pass

    def createChildren(self, *args): pass

    def doDrag(self, *args): pass

    def doPress(self, *args): pass

    def doRelease(self, *args): pass

    def draw(self, *args): pass

    def finishAddingManips(self, *args): pass

    def getConverterManipValue(self, *args): pass

    def getConverterPlugValue(self, *args): pass

    def isManipActive(self, *args): pass

    def manipToPlugConversion(self, *args): pass

    def plugToManipConversion(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def addToManipConnectTable(*args, **kwargs): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def initialize(*args, **kwargs): pass

    @staticmethod
    def newManipulator(*args, **kwargs): pass

    @staticmethod
    def removeFromManipConnectTable(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kCircleSweepManip = 6

    kCurveSegmentManip = 9

    kCustomManip = 10

    kDirectionManip = 1

    kDiscManip = 5

    kDistanceManip = 2

    kFreePointTriadManip = 0

    kPointOnCurveManip = 3

    kPointOnSurfaceManip = 4

    kStateManip = 8

    kToggleManip = 7


class MPxConstraint(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def constraintRotateOrderAttribute(self, *args): pass

    def getOutputAttributes(self, *args): pass

    def passiveOutputAttribute(self, *args): pass

    def targetAttribute(self, *args): pass

    def weightAttribute(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def enableRestPosition(self): pass

    @property
    def lockOutput(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kLast = 4

    kObject = 1

    kObjectRotation = 2

    kScene = 0

    kVector = 3


class MPxAssembly(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def activate(self, *args): pass

    def activateRep(self, *args): pass

    def activating(self, *args): pass

    def addAddAttrEdit(self, *args): pass

    def addConnectAttrEdit(self, *args): pass

    def addDeleteAttrEdit(self, *args): pass

    def addDisconnectAttrEdit(self, *args): pass

    def addEdits(self, *args): pass

    def addParentEdit(self, *args): pass

    def addSetAttrEdit(self, *args): pass

    def beforeSave(self, *args): pass

    def canRepApplyEdits(self, *args): pass

    def createRepresentation(self, *args): pass

    def deleteAllRepresentations(self, *args): pass

    def deleteRepresentation(self, *args): pass

    def existWithoutInConnections(self, *args): pass

    def existWithoutOutConnections(self, *args): pass

    def getActive(self, *args): pass

    def getInitialRep(self, *args): pass

    def getInstancePtr(self, *args): pass

    def getRepLabel(self, *args): pass

    def getRepNamespace(self, *args): pass

    def getRepType(self, *args): pass

    def getRepresentations(self, *args): pass

    def handlesAddEdits(self, *args): pass

    def inactivateRep(self, *args): pass

    def isActive(self, *args): pass

    def memberAdded(self, *args): pass

    def memberRemoved(self, *args): pass

    def name(self, *args): pass

    def performActivate(self, *args): pass

    def performInactivate(self, *args): pass

    def postActivateRep(self, *args): pass

    def postApplyEdits(self, *args): pass

    def postLoad(self, *args): pass

    def postUnapplyEdits(self, *args): pass

    def preApplyEdits(self, *args): pass

    def preUnapplyEdits(self, *args): pass

    def repTypes(self, *args): pass

    def setExistWithoutInConnections(self, *args): pass

    def setExistWithoutOutConnections(self, *args): pass

    def setInstancePtr(self, *args): pass

    def setRepLabel(self, *args): pass

    def setRepName(self, *args): pass

    def supportsEdits(self, *args): pass

    def supportsMemberChanges(self, *args): pass

    def thisMObject(self, *args): pass

    def type(self, *args): pass

    def typeId(self, *args): pass

    def typeName(self, *args): pass

    def updateRepNamespace(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxTexContext(MPxContext):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def newToolCommand(self, *args): pass

    def portSize(self, *args): pass

    def portToView(self, *args): pass

    def viewRect(self, *args): pass

    def viewToPort(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def getMarqueeSelection(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxHardwareShader(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def profile(self, *args): pass

    def render(self, *args): pass

    def renderSwatchImage(self, *args): pass

    def setUniformParameters(self, *args): pass

    def setVaryingParameters(self, *args): pass

    def transparencyOptions(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def findResource(*args, **kwargs): pass

    @staticmethod
    def getHardwareShaderPtr(*args, **kwargs): pass

    @property
    def outColor(self): pass

    @property
    def outColorB(self): pass

    @property
    def outColorG(self): pass

    @property
    def outColorR(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}

    kIsTransparent = 1

    kNoTransparencyFrontBackCull = 2

    kNoTransparencyPolygonSort = 4


class MPxImagePlane(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def exactImageFile(self, *args): pass

    def loadImageMap(self, *args): pass

    def refreshImage(self, *args): pass

    def setImageDirty(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def alphaGain(self): pass

    @property
    def alreadyPremult(self): pass

    @property
    def center(self): pass

    @property
    def centerX(self): pass

    @property
    def centerY(self): pass

    @property
    def centerZ(self): pass

    @property
    def colorGain(self): pass

    @property
    def colorGainB(self): pass

    @property
    def colorGainG(self): pass

    @property
    def colorGainR(self): pass

    @property
    def colorOffset(self): pass

    @property
    def colorOffsetB(self): pass

    @property
    def colorOffsetG(self): pass

    @property
    def colorOffsetR(self): pass

    @property
    def composite(self): pass

    @property
    def coverage(self): pass

    @property
    def coverageOrigin(self): pass

    @property
    def coverageOriginX(self): pass

    @property
    def coverageOriginY(self): pass

    @property
    def coverageX(self): pass

    @property
    def coverageY(self): pass

    @property
    def depth(self): pass

    @property
    def depthBias(self): pass

    @property
    def depthFile(self): pass

    @property
    def depthOversample(self): pass

    @property
    def depthScale(self): pass

    @property
    def displayMode(self): pass

    @property
    def displayOnlyIfCurrent(self): pass

    @property
    def fit(self): pass

    @property
    def frameExtension(self): pass

    @property
    def frameOffset(self): pass

    @property
    def height(self): pass

    @property
    def imageName(self): pass

    @property
    def imageType(self): pass

    @property
    def lockedToCamera(self): pass

    @property
    def maxShadingSamples(self): pass

    @property
    def offset(self): pass

    @property
    def offsetX(self): pass

    @property
    def offsetY(self): pass

    @property
    def rotate(self): pass

    @property
    def separateDepth(self): pass

    @property
    def shadingSamples(self): pass

    @property
    def shadingSamplesOverride(self): pass

    @property
    def size(self): pass

    @property
    def sizeX(self): pass

    @property
    def sizeY(self): pass

    @property
    def sourceTexture(self): pass

    @property
    def squeezeCorrection(self): pass

    @property
    def useDepthMap(self): pass

    @property
    def useFrameExtension(self): pass

    @property
    def visibleInReflections(self): pass

    @property
    def visibleInRefractions(self): pass

    @property
    def width(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxFieldNode(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def compute(self, *args): pass

    def draw(self, *args): pass

    def falloffCurve(self, *args): pass

    def getForceAtPoint(self, *args): pass

    def iconBitmap(self, *args): pass

    def iconSizeAndOrigin(self, *args): pass

    def isFalloffCurveConstantOne(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def mApplyPerVertex(self): pass

    @property
    def mAttenuation(self): pass

    @property
    def mDeltaTime(self): pass

    @property
    def mInputData(self): pass

    @property
    def mInputForce(self): pass

    @property
    def mInputMass(self): pass

    @property
    def mInputPPData(self): pass

    @property
    def mInputPositions(self): pass

    @property
    def mInputVelocities(self): pass

    @property
    def mMagnitude(self): pass

    @property
    def mMaxDistance(self): pass

    @property
    def mOutputForce(self): pass

    @property
    def mOwnerCentroid(self): pass

    @property
    def mOwnerCentroidX(self): pass

    @property
    def mOwnerCentroidY(self): pass

    @property
    def mOwnerCentroidZ(self): pass

    @property
    def mOwnerPPData(self): pass

    @property
    def mOwnerPosData(self): pass

    @property
    def mOwnerVelData(self): pass

    @property
    def mUseMaxDistance(self): pass

    @property
    def mWorldMatrix(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxTransform(MPxNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def applyRotateOrientationLocks(self, *args): pass

    def applyRotatePivotLocks(self, *args): pass

    def applyRotatePivotLocksTranslate(self, *args): pass

    def applyRotationLimits(self, *args): pass

    def applyRotationLocks(self, *args): pass

    def applyScaleLimits(self, *args): pass

    def applyScaleLocks(self, *args): pass

    def applyScaleLocksPivot(self, *args): pass

    def applyScaleLocksPivotTranslate(self, *args): pass

    def applyShearLocks(self, *args): pass

    def applyTranslationLimits(self, *args): pass

    def applyTranslationLocks(self, *args): pass

    def assign(self, *args): pass

    def boundingBox(self, *args): pass

    def checkAndSetRotateOrientation(self, *args): pass

    def checkAndSetRotatePivot(self, *args): pass

    def checkAndSetRotatePivotTranslation(self, *args): pass

    def checkAndSetRotation(self, *args): pass

    def checkAndSetScale(self, *args): pass

    def checkAndSetScalePivot(self, *args): pass

    def checkAndSetScalePivotTranslation(self, *args): pass

    def checkAndSetShear(self, *args): pass

    def checkAndSetTranslation(self, *args): pass

    def clearLimits(self, *args): pass

    def compute(self, *args): pass

    def computeLocalTransformation(self, *args): pass

    def copyInternalData(self, *args): pass

    def createTransformationMatrix(self, *args): pass

    def enableLimit(self, *args): pass

    def getEulerRotation(self, *args): pass

    def getMatrix(self, *args): pass

    def getMatrixInverse(self, *args): pass

    def getRotateOrientation(self, *args): pass

    def getRotatePivot(self, *args): pass

    def getRotatePivotTranslation(self, *args): pass

    def getRotation(self, *args): pass

    def getRotationOrder(self, *args): pass

    def getScale(self, *args): pass

    def getScalePivot(self, *args): pass

    def getScalePivotTranslation(self, *args): pass

    def getShear(self, *args): pass

    def getTranslation(self, *args): pass

    def isBounded(self, *args): pass

    def isLimited(self, *args): pass

    def limitValue(self, *args): pass

    def postConstructor(self, *args): pass

    def resetTransformation(self, *args): pass

    def rotateBy(self, *args): pass

    def rotateTo(self, *args): pass

    def scaleBy(self, *args): pass

    def scaleTo(self, *args): pass

    def setLimit(self, *args): pass

    def setRotateOrientation(self, *args): pass

    def setRotatePivot(self, *args): pass

    def setRotatePivotTranslation(self, *args): pass

    def setRotationOrder(self, *args): pass

    def setScalePivot(self, *args): pass

    def setScalePivotTranslation(self, *args): pass

    def shearBy(self, *args): pass

    def shearTo(self, *args): pass

    def transformationMatrix(self, *args): pass

    def transformationMatrixPtr(self, *args): pass

    def translateBy(self, *args): pass

    def translateTo(self, *args): pass

    def treatAsTransform(self, *args): pass

    def type(self, *args): pass

    def updateMatrixAttrs(self, *args): pass

    def validateAndSetValue(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @staticmethod
    def isNonAffineMatricesEnabled(*args, **kwargs): pass

    @staticmethod
    def mustCallValidateAndSet(*args, **kwargs): pass

    @staticmethod
    def setNonAffineMatricesEnabled(*args, **kwargs): pass

    @property
    def boundingBoxCenterX(self): pass

    @property
    def boundingBoxCenterY(self): pass

    @property
    def boundingBoxCenterZ(self): pass

    @property
    def center(self): pass

    @property
    def displayHandle(self): pass

    @property
    def displayLocalAxis(self): pass

    @property
    def displayRotatePivot(self): pass

    @property
    def displayScalePivot(self): pass

    @property
    def drawOverride(self): pass

    @property
    def dynamics(self): pass

    @property
    def geometry(self): pass

    @property
    def ghosting(self): pass

    @property
    def identification(self): pass

    @property
    def inheritsTransform(self): pass

    @property
    def instObjGroups(self): pass

    @property
    def intermediateObject(self): pass

    @property
    def inverseMatrix(self): pass

    @property
    def isTemplated(self): pass

    @property
    def layerOverrideColor(self): pass

    @property
    def layerRenderable(self): pass

    @property
    def lodVisibility(self): pass

    @property
    def matrix(self): pass

    @property
    def maxRotLimit(self): pass

    @property
    def maxRotLimitEnable(self): pass

    @property
    def maxRotXLimit(self): pass

    @property
    def maxRotXLimitEnable(self): pass

    @property
    def maxRotYLimit(self): pass

    @property
    def maxRotYLimitEnable(self): pass

    @property
    def maxRotZLimit(self): pass

    @property
    def maxRotZLimitEnable(self): pass

    @property
    def maxScaleLimit(self): pass

    @property
    def maxScaleLimitEnable(self): pass

    @property
    def maxScaleXLimit(self): pass

    @property
    def maxScaleXLimitEnable(self): pass

    @property
    def maxScaleYLimit(self): pass

    @property
    def maxScaleYLimitEnable(self): pass

    @property
    def maxScaleZLimit(self): pass

    @property
    def maxScaleZLimitEnable(self): pass

    @property
    def maxTransLimit(self): pass

    @property
    def maxTransLimitEnable(self): pass

    @property
    def maxTransXLimit(self): pass

    @property
    def maxTransXLimitEnable(self): pass

    @property
    def maxTransYLimit(self): pass

    @property
    def maxTransYLimitEnable(self): pass

    @property
    def maxTransZLimit(self): pass

    @property
    def maxTransZLimitEnable(self): pass

    @property
    def minRotLimit(self): pass

    @property
    def minRotLimitEnable(self): pass

    @property
    def minRotXLimit(self): pass

    @property
    def minRotXLimitEnable(self): pass

    @property
    def minRotYLimit(self): pass

    @property
    def minRotYLimitEnable(self): pass

    @property
    def minRotZLimit(self): pass

    @property
    def minRotZLimitEnable(self): pass

    @property
    def minScaleLimit(self): pass

    @property
    def minScaleLimitEnable(self): pass

    @property
    def minScaleXLimit(self): pass

    @property
    def minScaleXLimitEnable(self): pass

    @property
    def minScaleYLimit(self): pass

    @property
    def minScaleYLimitEnable(self): pass

    @property
    def minScaleZLimit(self): pass

    @property
    def minScaleZLimitEnable(self): pass

    @property
    def minTransLimit(self): pass

    @property
    def minTransLimitEnable(self): pass

    @property
    def minTransXLimit(self): pass

    @property
    def minTransXLimitEnable(self): pass

    @property
    def minTransYLimit(self): pass

    @property
    def minTransYLimitEnable(self): pass

    @property
    def minTransZLimit(self): pass

    @property
    def minTransZLimitEnable(self): pass

    @property
    def nodeBoundingBox(self): pass

    @property
    def nodeBoundingBoxMax(self): pass

    @property
    def nodeBoundingBoxMaxX(self): pass

    @property
    def nodeBoundingBoxMaxY(self): pass

    @property
    def nodeBoundingBoxMaxZ(self): pass

    @property
    def nodeBoundingBoxMin(self): pass

    @property
    def nodeBoundingBoxMinX(self): pass

    @property
    def nodeBoundingBoxMinY(self): pass

    @property
    def nodeBoundingBoxMinZ(self): pass

    @property
    def nodeBoundingBoxSize(self): pass

    @property
    def nodeBoundingBoxSizeX(self): pass

    @property
    def nodeBoundingBoxSizeY(self): pass

    @property
    def nodeBoundingBoxSizeZ(self): pass

    @property
    def objectColor(self): pass

    @property
    def objectGroupColor(self): pass

    @property
    def objectGroupId(self): pass

    @property
    def objectGroups(self): pass

    @property
    def objectGrpCompList(self): pass

    @property
    def overrideColor(self): pass

    @property
    def overrideDisplayType(self): pass

    @property
    def overrideEnabled(self): pass

    @property
    def overrideLevelOfDetail(self): pass

    @property
    def overridePlayback(self): pass

    @property
    def overrideShading(self): pass

    @property
    def overrideTexturing(self): pass

    @property
    def overrideVisibility(self): pass

    @property
    def parentInverseMatrix(self): pass

    @property
    def parentMatrix(self): pass

    @property
    def renderInfo(self): pass

    @property
    def renderLayerColor(self): pass

    @property
    def renderLayerId(self): pass

    @property
    def renderLayerInfo(self): pass

    @property
    def renderLayerRenderable(self): pass

    @property
    def rotate(self): pass

    @property
    def rotateAxis(self): pass

    @property
    def rotateAxisX(self): pass

    @property
    def rotateAxisY(self): pass

    @property
    def rotateAxisZ(self): pass

    @property
    def rotateOrder(self): pass

    @property
    def rotatePivot(self): pass

    @property
    def rotatePivotTranslate(self): pass

    @property
    def rotatePivotTranslateX(self): pass

    @property
    def rotatePivotTranslateY(self): pass

    @property
    def rotatePivotTranslateZ(self): pass

    @property
    def rotatePivotX(self): pass

    @property
    def rotatePivotY(self): pass

    @property
    def rotatePivotZ(self): pass

    @property
    def rotateQuaternion(self): pass

    @property
    def rotateQuaternionW(self): pass

    @property
    def rotateQuaternionX(self): pass

    @property
    def rotateQuaternionY(self): pass

    @property
    def rotateQuaternionZ(self): pass

    @property
    def rotateX(self): pass

    @property
    def rotateY(self): pass

    @property
    def rotateZ(self): pass

    @property
    def rotationInterpolation(self): pass

    @property
    def scale(self): pass

    @property
    def scalePivot(self): pass

    @property
    def scalePivotTranslate(self): pass

    @property
    def scalePivotTranslateX(self): pass

    @property
    def scalePivotTranslateY(self): pass

    @property
    def scalePivotTranslateZ(self): pass

    @property
    def scalePivotX(self): pass

    @property
    def scalePivotY(self): pass

    @property
    def scalePivotZ(self): pass

    @property
    def scaleX(self): pass

    @property
    def scaleY(self): pass

    @property
    def scaleZ(self): pass

    @property
    def selectHandle(self): pass

    @property
    def selectHandleX(self): pass

    @property
    def selectHandleY(self): pass

    @property
    def selectHandleZ(self): pass

    @property
    def shear(self): pass

    @property
    def shearXY(self): pass

    @property
    def shearXZ(self): pass

    @property
    def shearYZ(self): pass

    @property
    def showManipDefault(self): pass

    @property
    def specifiedManipLocation(self): pass

    @property
    def transMinusRotatePivot(self): pass

    @property
    def transMinusRotatePivotX(self): pass

    @property
    def transMinusRotatePivotY(self): pass

    @property
    def transMinusRotatePivotZ(self): pass

    @property
    def translate(self): pass

    @property
    def translateX(self): pass

    @property
    def translateY(self): pass

    @property
    def translateZ(self): pass

    @property
    def useObjectColor(self): pass

    @property
    def visibility(self): pass

    @property
    def worldInverseMatrix(self): pass

    @property
    def worldMatrix(self): pass

    @property
    def xformMatrix(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxPolyTweakUVCommand(MPxCommand):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def getTweakedUVs(self, *args): pass

    def parseSyntax(self, *args): pass

    @staticmethod
    def newSyntax(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxToolCommand(MPxCommand):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def cancel(self, *args): pass

    def doIt(self, *args): pass

    def finalize(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxComponentShape(MPxSurfaceShape):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def componentToPlugs(self, *args): pass

    def createFullVertexGroup(self, *args): pass

    def getControlPoints(self, *args): pass

    def localShapeInAttr(self, *args): pass

    def match(self, *args): pass

    def setControlPoints(self, *args): pass

    def transformUsing(self, *args): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxSkinCluster(MPxGeometryFilter):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def type(self, *args): pass

    def weightValue(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def bindPreMatrix(self): pass

    @property
    def matrix(self): pass

    @property
    def weightList(self): pass

    @property
    def weights(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxDeformerNode(MPxGeometryFilter):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def getDeformationDetails(self, *args): pass

    def setDeformationDetails(self, *args): pass

    def setUseExistingConnectionWhenSetEditing(self, *args): pass

    def type(self, *args): pass

    def weightValue(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def weightList(self): pass

    @property
    def weights(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxFluidEmitterNode(MPxEmitterNode):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def compute(self, *args): pass

    def fluidColor(self, *args): pass

    def fluidDensityEmission(self, *args): pass

    def fluidDropoff(self, *args): pass

    def fluidEmitColor(self, *args): pass

    def fluidEmitter(self, *args): pass

    def fluidFuelEmission(self, *args): pass

    def fluidHeatEmission(self, *args): pass

    def fluidJitter(self, *args): pass

    def turbulence(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def mEmissionFunction(self): pass

    @property
    def mEmitFluidColor(self): pass

    @property
    def mFluidColor(self): pass

    @property
    def mFluidColorB(self): pass

    @property
    def mFluidColorG(self): pass

    @property
    def mFluidColorR(self): pass

    @property
    def mFluidDensityEmission(self): pass

    @property
    def mFluidDropoff(self): pass

    @property
    def mFluidFuelEmission(self): pass

    @property
    def mFluidHeatEmission(self): pass

    @property
    def mFluidJitter(self): pass

    @property
    def mTurbulence(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxBlendShape(MPxGeometryFilter):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def deformData(self, *args): pass

    def type(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    @property
    def inputComponentsTarget(self): pass

    @property
    def inputGeomTarget(self): pass

    @property
    def inputPointsTarget(self): pass

    @property
    def inputTarget(self): pass

    @property
    def inputTargetGroup(self): pass

    @property
    def inputTargetItem(self): pass

    @property
    def targetWeights(self): pass

    @property
    def weight(self): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


class MPxPolyTweakUVInteractiveCommand(MPxToolCommand):
    def __del__(self): pass

    def __disown__(self): pass

    def __getattr__(self, name): pass

    def __init__(self, *args): pass

    def __repr__(self): pass

    def __setattr__(self, name, value): pass

    def cancel(self, *args): pass

    def doIt(self, *args): pass

    def finalize(self, *args): pass

    def isUndoable(self, *args): pass

    def setUVs(self, *args): pass

    @staticmethod
    def className(*args, **kwargs): pass

    __swig_destroy__ = None

    __swig_getmethods__ = {}

    __swig_setmethods__ = {}


def MPxNode_inheritAttributesFrom(*args, **kwargs): pass


def MPx3dModelView_getModelView(*args, **kwargs): pass


def MPxCommand_getCurrentResult(*args, **kwargs): pass


def MPxAnimCurveInterpolator_swigregister(*args, **kwargs): pass


def intPtr_frompointer(*args, **kwargs): pass


def MPxManipulatorNode_swigregister(*args, **kwargs): pass


def MPxSpringNode_swigregister(*args, **kwargs): pass


def doublePtr_frompointer(*args, **kwargs): pass


def weakref_proxy(*args, **kwargs):
    """
    proxy(object[, callback]) -- create a proxy object that weakly
    references 'object'.  'callback', if given, is called with a
    reference to the proxy when 'object' is about to be finalized.
    """
    pass


def MPxPolyTweakUVInteractiveCommand_swigregister(*args, **kwargs): pass


def MPxControlCommand_swigregister(*args, **kwargs): pass


def MPxManipContainer_initialize(*args, **kwargs): pass


def MPxGeometryIterator_className(*args, **kwargs): pass


def MPx3dModelView_swigregister(*args, **kwargs): pass


def MPxTransform_className(*args, **kwargs): pass


def MPxModelEditorCommand_className(*args, **kwargs): pass


def shortPtr_swigregister(*args, **kwargs): pass


def MPxToolCommand_className(*args, **kwargs): pass


def MPxFileResolver_findURIResolverByName(*args, **kwargs): pass


def MPxBlendShape_swigregister(*args, **kwargs): pass


def MFnPlugin_isNodeRegistered(*args, **kwargs): pass


def MFnPlugin_registeringCallableScript(*args, **kwargs): pass


def MPxData_swigregister(*args, **kwargs): pass


def MPxGeometryData_swigregister(*args, **kwargs): pass


def MPxTransform_mustCallValidateAndSet(*args, **kwargs): pass


def _swig_repr(self): pass


def MPxGlBuffer_className(*args, **kwargs): pass


def MPxRenderPassImpl_swigregister(*args, **kwargs): pass


def MPxNode_addAttribute(*args, **kwargs): pass


def MPxAssembly_swigregister(*args, **kwargs): pass


def MFnPlugin_swigregister(*args, **kwargs): pass


def MPxEmitterNode_swigregister(*args, **kwargs): pass


def MPxParticleAttributeMapperNode_swigregister(*args, **kwargs): pass


def MPxContext__ignoreEntry(*args, **kwargs): pass


def MPxFileTranslator_fileAccessMode(*args, **kwargs): pass


def MPxCommand_displayInfo(*args, **kwargs): pass


def MPxSurfaceShapeUI_swigregister(*args, **kwargs): pass


def MPxContext_className(*args, **kwargs): pass


def MPxCommand_setResult(*args, **kwargs): pass


def MPxPolyTweakUVCommand_swigregister(*args, **kwargs): pass


def MPxDeformerNode_className(*args, **kwargs): pass


def MPxCommand_className(*args, **kwargs): pass


def MPxHwShaderNode_className(*args, **kwargs): pass


def MPxConstraintCommand_swigregister(*args, **kwargs): pass


def MPxEditData_swigregister(*args, **kwargs): pass


def MPxMultiPolyTweakUVCommand_newSyntax(*args, **kwargs): pass


def MPxIkSolverNode_swigregister(*args, **kwargs): pass


def uCharPtr_frompointer(*args, **kwargs): pass


def MPxSelectionContext_className(*args, **kwargs): pass


def MPxImagePlane_className(*args, **kwargs): pass


def MPxFileResolver_swigregister(*args, **kwargs): pass


def MPxMultiPolyTweakUVCommand_swigregister(*args, **kwargs): pass


def MPxDeformerNode_swigregister(*args, **kwargs): pass


def MPxFluidEmitterNode_className(*args, **kwargs): pass


def MPxSpringNode_className(*args, **kwargs): pass


def MExternalContentInfoTable_swigregister(*args, **kwargs): pass


def MPxHardwareShader_className(*args, **kwargs): pass


def MPxCacheConfigRuleFilter_swigregister(*args, **kwargs): pass


def MPxObjectSet_className(*args, **kwargs): pass


def MPxBakeEngine_swigregister(*args, **kwargs): pass


def MPxTransformationMatrix_convertEulerRotationOrder(*args, **kwargs): pass


def shortPtr_frompointer(*args, **kwargs): pass


def MPxFieldNode_swigregister(*args, **kwargs): pass


def MPxFileResolver_findURIResolverByScheme(*args, **kwargs): pass


def MPxManipContainer_newManipulator(*args, **kwargs): pass


def MPxTexContext_className(*args, **kwargs): pass


def MFnPlugin_findPlugin(*args, **kwargs): pass


def MPxFileResolver_numURIResolvers(*args, **kwargs): pass


def MPxContext_swigregister(*args, **kwargs): pass


def MPxGeometryFilter_className(*args, **kwargs): pass


def MPxCacheFormat_className(*args, **kwargs): pass


def MFnPlugin_className(*args, **kwargs): pass


def uIntPtr_frompointer(*args, **kwargs): pass


def getLockCaptureCount(*args, **kwargs): pass


def MPxManipContainer_addToManipConnectTable(*args, **kwargs): pass


def MPxCameraSet_className(*args, **kwargs): pass


def _swig_setattr_nondynamic(self, class_type, name, value, static='1'): pass


def MPxSurfaceShape_swigregister(*args, **kwargs): pass


def MPxCommand_clearResult(*args, **kwargs): pass


def MPxManipContainer_removeFromManipConnectTable(*args, **kwargs): pass


def MPxCommand_currentResultType(*args, **kwargs): pass


def MPxManipContainer_className(*args, **kwargs): pass


def MPxCommand_isCurrentResultArray(*args, **kwargs): pass


def MPxCommand_currentStringResult(*args, **kwargs): pass


def MPxTransformationMatrix_swigregister(*args, **kwargs): pass


def MPxCommand_swigregister(*args, **kwargs): pass


def MPxManipulatorNode_className(*args, **kwargs): pass


def MPxTransform_swigregister(*args, **kwargs): pass


def MPxAttributePatternFactory_className(*args, **kwargs): pass


def asHashable(mpxObj): pass


def MPxAttributePatternFactory_swigregister(*args, **kwargs): pass


def MPxMidiInputDevice_swigregister(*args, **kwargs): pass


def MPxNode_className(*args, **kwargs): pass


def charPtr_frompointer(*args, **kwargs): pass


def MPxControlCommand_className(*args, **kwargs): pass


def MExternalContentLocationTable_swigregister(*args, **kwargs): pass


def MPx3dModelView_className(*args, **kwargs): pass


def MPxImagePlane_swigregister(*args, **kwargs): pass


def MPxMotionPathNode_swigregister(*args, **kwargs): pass


def MPxGeometryIterator_swigregister(*args, **kwargs): pass


def MPxToolCommand_swigregister(*args, **kwargs): pass


def MPxUIControl_className(*args, **kwargs): pass


def MPxBlendShape_className(*args, **kwargs): pass


def MPxModelEditorCommand_swigregister(*args, **kwargs): pass


def MPxDragAndDropBehavior_swigregister(*args, **kwargs): pass


def MPxUITableControl_swigregister(*args, **kwargs): pass


def MPxFileResolver_getURIResolversByName(*args, **kwargs): pass


def MPxImageFile_swigregister(*args, **kwargs): pass


def MPxEmitterNode_className(*args, **kwargs): pass


def MPxTransform_isNonAffineMatricesEnabled(*args, **kwargs): pass


def MPxDragAndDropBehavior_className(*args, **kwargs): pass


def MPxPolyTrg_swigregister(*args, **kwargs): pass


def boolPtr_swigregister(*args, **kwargs): pass


def uCharPtr_swigregister(*args, **kwargs): pass


def MPxPolyTweakUVInteractiveCommand_className(*args, **kwargs): pass


def uIntPtr_swigregister(*args, **kwargs): pass


def MPxContextCommand_className(*args, **kwargs): pass


def MPxHardwareShader_findResource(*args, **kwargs): pass


def MPxSurfaceShapeUI_className(*args, **kwargs): pass


def MPxParticleAttributeMapperNode_className(*args, **kwargs): pass


def MPxTexContext_swigregister(*args, **kwargs): pass


def MPxMayaAsciiFilter_swigregister(*args, **kwargs): pass


def MPxObjectSet_swigregister(*args, **kwargs): pass


def MPxLocatorNode_swigregister(*args, **kwargs): pass


def _swig_getattr(self, class_type, name): pass


def MPxPolyTweakUVCommand_newSyntax(*args, **kwargs): pass


def MPxFileTranslator_swigregister(*args, **kwargs): pass


def charPtr_swigregister(*args, **kwargs): pass


def MaterialInputData_swigregister(*args, **kwargs): pass


def MPxCommand_displayError(*args, **kwargs): pass


def MPxManipulatorNode_newManipulator(*args, **kwargs): pass


def MPxMidiInputDevice_className(*args, **kwargs): pass


def MPxCommand_appendToResult(*args, **kwargs): pass


def asMPxPtr(mpxObj): pass


def MPxEditData_className(*args, **kwargs): pass


def MPxAssembly_className(*args, **kwargs): pass


def MPxUITableControl_className(*args, **kwargs): pass


def MPxCommand_currentDoubleResult(*args, **kwargs): pass


def boolPtr_frompointer(*args, **kwargs): pass


def MPxSurfaceShape_className(*args, **kwargs): pass


def floatPtr_swigregister(*args, **kwargs): pass


def MPxNode_attributeAffects(*args, **kwargs): pass


def MPxSkinCluster_swigregister(*args, **kwargs): pass


def MPxSkinCluster_className(*args, **kwargs): pass


def MPxHardwareShader_getHardwareShaderPtr(*args, **kwargs): pass


def MPxHwShaderNode_swigregister(*args, **kwargs): pass


def MPxGlBuffer_swigregister(*args, **kwargs): pass


def _swig_setattr(self, class_type, name, value): pass


def doublePtr_swigregister(*args, **kwargs): pass


def MPxTexContext_getMarqueeSelection(*args, **kwargs): pass


def MPxTransformationMatrix_convertTransformationRotationOrder(*args, **kwargs): pass


def MPxTransformationMatrix_creator(*args, **kwargs): pass


def MPxFluidEmitterNode_swigregister(*args, **kwargs): pass


def MPxFieldNode_className(*args, **kwargs): pass


def MPxHardwareShader_swigregister(*args, **kwargs): pass


def MPxConstraint_className(*args, **kwargs): pass


def MPxComponentShape_swigregister(*args, **kwargs): pass


def MPxRepresentation_swigregister(*args, **kwargs): pass


def MPxConstraint_swigregister(*args, **kwargs): pass


def MPxFileResolver_getURIResolversByScheme(*args, **kwargs): pass


def MPxNode_swigregister(*args, **kwargs): pass


def floatPtr_frompointer(*args, **kwargs): pass


def MPxMaterialInformation_swigregister(*args, **kwargs): pass


def MPxCacheFormat_swigregister(*args, **kwargs): pass


def MPxMayaAsciiFilterOutput_swigregister(*args, **kwargs): pass


def MPxSurfaceShapeUI_surfaceShapeUI(*args, **kwargs): pass


def MFnPlugin_setRegisteringCallableScript(*args, **kwargs): pass


def MPxContextCommand_swigregister(*args, **kwargs): pass


def MPxUIControl_swigregister(*args, **kwargs): pass


def MPxFileResolver_className(*args, **kwargs): pass


def MPxLocatorNode_className(*args, **kwargs): pass


def MPxTransform_setNonAffineMatricesEnabled(*args, **kwargs): pass


def MPxHwShaderNode_getHwShaderNodePtr(*args, **kwargs): pass


def MPxCameraSet_swigregister(*args, **kwargs): pass


def MPxCommand_displayWarning(*args, **kwargs): pass


def MPxSelectionContext_swigregister(*args, **kwargs): pass


def intPtr_swigregister(*args, **kwargs): pass


def MPxCommand_currentIntResult(*args, **kwargs): pass


def MPxManipContainer_swigregister(*args, **kwargs): pass


def MPxGeometryFilter_swigregister(*args, **kwargs): pass


def MPxIkSolverNode_className(*args, **kwargs): pass


_newclass = 1

cvar = None

PLUGIN_COMPANY = 'Autodesk'
