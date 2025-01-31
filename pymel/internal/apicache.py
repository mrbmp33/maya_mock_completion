

if False:
    from typing import Dict, List, Tuple, Union, Optional


class InvalidNodeTypeError(Exception):
    __weakref__ = None


class _GhostObjMaker(object):
    """
    Context used to get an mobject which we can query within this context.
    
    Automatically does any steps need to create and destroy the mobj within
    the context
    
    (Note - None may be returned in the place of any mobj)
    """

    def __enter__(self): pass

    def __exit__(self, exc_type, exc_value, traceback): pass

    def __init__(self, mayaTypes, dagMod='None', dgMod='None', manipError='True', multi='False'): pass

    __dict__ = None

    __weakref__ = None


class ApiEnum(tuple):
    def __repr__(self): pass

    def __str__(self): pass

    def pymelName(self): pass

    __dict__ = None


class GhostObjsOkHere(object):
    def __enter__(self): pass

    def __exit__(self, exc_type, exc_value, traceback): pass

    @classmethod
    def OK(cls): pass

    __dict__ = None

    __weakref__ = None


from . import startup


class BaseApiClassInfoCache(startup.SubItemCache):
    def fromRawData(self, data): pass

    def toRawData(self, data): pass

    CLASSINFO_SUBCACHE_NAME = None


class ApiCache(BaseApiClassInfoCache):
    def __init__(self, docLocation='None'): pass

    def addMayaType(self, mayaType, apiType='None', updateObj='None'):
        """
        Add a type to the MayaTypes lists. Fill as many dictionary caches as we have info for.
        
            - mayaTypesToApiTypes
            - mayaTypesToApiEnums
        
        if updateObj is given, this instance will first be updated from it,
        before the mayaType is added.
        """
        pass

    def extraDicts(self): pass

    def fromRawData(self, data): pass

    def melBridgeContents(self): pass

    def rebuild(self):
        """
        Rebuild the api cache from scratch
        
        Unlike 'build', this does not attempt to load a cache file, but always
        rebuilds it by parsing the docs, etc.
        """
        pass

    def removeMayaType(self, mayaType, updateObj='None'):
        """
        Remove a type from the MayaTypes lists.
        
            - mayaTypesToApiTypes
            - mayaTypesToApiEnums
        
        if updateObj is given, this instance will first be updated from it,
        before the mayaType is added.
        """
        pass

    def toRawData(self, data): pass

    @classmethod
    def allVersions(cls, allowEmpty='False'): pass

    API_TO_MFN_OVERRIDES = {}

    CLASSINFO_SUBCACHE_NAME = 'apiClassInfo'

    CRASH_TYPES = {}

    DEFAULT_API_TYPE = 'kDependencyNode'

    DESC = 'the API cache'

    EXTRA_GLOBAL_NAMES = ()

    MAYA_TO_API_OVERRIDES = {}

    MFN_TO_API_OVERRIDES = {}

    NAME = 'mayaApi'

    USE_VERSION = True


class ManipNodeTypeError(InvalidNodeTypeError):
    pass


class ApiMelBridgeCache(BaseApiClassInfoCache):
    def rebuild(self): pass

    def write(self, data, ext='None'):
        """
        # override write to preserve comments
        """
        pass

    @classmethod
    def applyComments(cls, origText, origTextNoComments, newPath): pass

    @classmethod
    def stripComments(cls, sourcelines):
        """
        Returns the text of the input python source lines with no comments,
        or None if the source did not have any comments
        
        sourcelines should have trailing newlines, ie, as returned by readlines
        """
        pass

    CLASSINFO_SUBCACHE_NAME = 'apiClassOverrides'

    DESC = 'the API-MEL bridge'

    NAME = 'mayaApiMelBridge'

    USE_VERSION = False


def _getRealMayaTypes(**kwargs): pass


def isPluginNode(nodeName):
    """
    # if we have MNodeClass, this is easy...
    """
    pass


def _getMayaTypes(real='True', abstract='True', basePluginTypes='True', addAncestors='True', noManips='True',
                  noPlugins='False', returnRealAbstract='False'):
    """
    Returns a list of maya types
    
    Parameters
    ----------
    real : bool
        Include the set of real/createable nodes
    abstract : bool
        Include the set of abstract nodes (as defined by allNodeTypes(includeAbstract=True)
    basePluginTypes : bool
        Include the set of "base" plugin maya types (these are not returned by
        allNodeTypes(includeAbstract=True), and so, even though these types are
        abstract, this set shares no members with those added by the abstract
        flag
    addAncestors : bool
        If true, add to the list of nodes returned all of their ancestors as
        well
    noManips : Union[bool, str]
        If true, filter out any manipulator node types; if the special value
        'fast', then it will filter out manipulator node types, but will do so
        using a faster method that may potentially be less thorough
    noPlugins : bool
        If true, filter out any nodes defined in plugins (note - if
        basePluginTypes is True, and noPlugins is False, the basePluginTypes
        will still be returned, as these types are not themselves defined in
        the plugin)
    returnRealAbstract : bool
        if True, will return two sets, realNodes and abstractNodes; otherwise,
        returns a single set of all the desired nodes (more precisely, realNodes
        is defined as the set of directly createdable nodes matching the
        criteria, and abstract are all non-createable nodes matching the
        criteria)
    """
    pass


def getInheritance(mayaType, checkManip3D='True', checkCache='True', updateCache='True'):
    """
    Get parents as a list, starting from the node after dependNode, and
    ending with the mayaType itself.
    
    Raises a ManipNodeTypeError if the node type fed in was a manipulator
    """
    pass


def _defaultdictdict(cls, val='None'): pass


def _makeDgModGhostObject(mayaType, dagMod, dgMod): pass


def _getAbstractMayaTypes(**kwargs): pass


def nodeToApiName(nodeName): pass


def getLowerCaseMapping(names): pass


def _getAllMayaTypes(**kwargs): pass


_ASSET_PREFIX = 'adskAssetInstanceNode_'

API_NAME_MODIFIERS = []

_ABSTRACT_SUFFIX = ' (abstract)'

_logger = None

_fixedLineages = {}

_cachedInheritances = {}

apiSuffixes = []

replace = 'vertice'

find = 'vert(?!(ex|ice))'

mpxNamesToApiEnumNames = {}
