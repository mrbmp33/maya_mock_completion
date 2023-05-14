"""
Maya-related functions, which are useful to both `api` and `core`, including `mayaInit` which ensures
that maya is initialized in standalone mode.
"""

from pymel.util.shell import shellOutput
from pymel.versions import installName
from pymel.util.shell import refreshEnviron
from pymel.versions import shortName
from pymel.util.utilitytypes import universalmethod
from pymel.util.common import subpackages
from pymel.mayautils import getUserPrefsDir
from collections import namedtuple

if False:
    from typing import Dict, List, Tuple, Union, Optional

CacheFormat = namedtuple('CacheFormat', ('ext', 'reader', 'writer'))


class PymelCache(object):
    def fromRawData(self, rawData):
        """
        If a subclass needs to modify data as it is read from the cache
        on disk, do it here
        """
        pass

    def path(*args, **kwargs): pass

    def read(self, ext='None'): pass

    def toRawData(self, data):
        """
        If a subclass needs to modify data before it is written to the cache
        on disk, do it here
        """
        pass

    def write(self, data, ext='None'): pass

    @classmethod
    def allVersions(cls, allowEmpty='False'): pass

    DEFAULT_EXT = '.py'

    DESC = ''

    EXTENSIONS = {}

    FORMATS = []

    NAME = ''

    USE_VERSION = True

    __dict__ = None

    __weakref__ = None


class SubItemCache(PymelCache):
    """
    Used to store various maya information
    
    ie, api / cmd data parsed from docs
    
    To implement, create a subclass, which overrides at least the NAME, DESC,
    and _CACHE_NAMES attributes, and implements the rebuild method.
    
    Then to access data, you should initialize an instance, then call build;
    build will load the data from the cache file if possible, or call rebuild
    to build the data from scratch if not.  If the data had to be rebuilt,
    a new file cache will be saved.
    
    The data may then be accessed through attributes on the instance, with
    the names given in _CACHE_NAMES.
    
    >>> class NodeCache(SubItemCache):
    ...     NAME = 'mayaNodes'
    ...     DESC = 'the maya nodes cache'
    ...     _CACHE_NAMES = ['nodeTypes']
    ...     AUTO_SAVE = False
    ...     def rebuild(self):
    ...         import maya.cmds
    ...         self.nodeTypes = maya.cmds.allNodeTypes(includeAbstract=True)
    >>> cacheInst = NodeCache()
    >>> cacheInst.build()
    >>> 'polyCube' in cacheInst.nodeTypes
    True
    """

    def __init__(self): pass

    def build(self):
        """
        Used to rebuild cache, either by loading from a cache file, or rebuilding from scratch.
        """
        pass

    def contents(self):
        """
        # was called 'caches'
        """
        pass

    def initVal(self, name): pass

    def load(self):
        """
        Attempts to load the data from the cache on file.
        
        If it succeeds, it will update itself, and return the loaded items;
        if it fails, it will return None
        """
        pass

    def rebuild(self):
        """
        Rebuild cache from scratch
        
        Unlike 'build', this does not attempt to load a cache file, but always
        rebuilds it by parsing the docs, etc.
        """
        pass

    def save(self, obj='None', ext='None'):
        """
        Saves the cache
        
        Will optionally update the caches from the given object (which may be
        a dictionary, or an object with the caches stored in attributes on it)
        before saving
        """
        pass

    def update(self, obj, cacheNames='None'):
        """
        Update all the various data from the given object, which should
        either be a dictionary, a list or tuple with the right number of items,
        or an object with the caches stored in attributes on it.
        """
        pass

    @classmethod
    def cacheNames(cls): pass

    @classmethod
    def itemIndex(cls, name): pass

    @classmethod
    def itemType(cls, name): pass

    AUTO_SAVE = True

    DEFAULT_TYPE = None

    ITEM_TYPES = {}


def setupFormatting(): pass


def fixMayapy2011SegFault():
    """
    # Have all the checks inside here, in case people want to insert this in their
    # userSetup... it's currently not always on
    """
    pass


def _getpycbytes(source): pass


def _pickledump(data, filename, protocol='-1'): pass


def initAE(): pass


def getConfigFile(): pass


def _moduleJoin(*args):
    """
    Joins with the base pymel directory.
    :rtype: string
    """
    pass


def _pyzipload(filename): pass


def finalize(): pass


def mayaInit(forversion='None'): pass


def _pycodeload(code): pass


def _pickleload(filename): pass


def _mayaInit(forversion='None'):
    """
    Try to init Maya standalone module, use when running pymel from an external Python inerpreter,
    it is possible to pass the desired Maya version number to define which Maya to initialize
    
    
    Part of the complexity of initializing maya in standalone mode is that maya does not populate os.environ when
    parsing Maya.env.  If we initialize normally, the env's are available via maya (via the shell), but not in python
    via os.environ.
    
    Note: the following example assumes that MAYA_SCRIPT_PATH is not set in your shell environment prior to launching
    python or mayapy.
    
    >>> import maya.standalone            #doctest: +SKIP
    >>> maya.standalone.initialize()      #doctest: +SKIP
    >>> import maya.mel as mm             #doctest: +SKIP
    >>> print mm.eval("getenv MAYA_SCRIPT_PATH")    #doctest: +SKIP
    /Network/Servers/sv-user.luma-pictures.com/luma .....
    >>> import os                         #doctest: +SKIP
    >>> 'MAYA_SCRIPT_PATH' in os.environ  #doctest: +SKIP
    False
    
    The solution lies in `refreshEnviron`, which copies the environment from the shell to os.environ after maya.standalone
    initializes.
    
    Returns
    -------
    bool
        returns True if maya.cmds required initializing ( in other words, we are in a standalone python interpreter )
    """
    pass


def _pydump(data, filename): pass


def mayaStartupHasRun():
    """
    Returns True if maya.app.startup has already finished, False otherwise.
    """
    pass


def getImportableObject(importableName): pass


def _pyload(filename): pass


def fixMayapySegFault(): pass


def parsePymelConfig(): pass


def encodeFix(): pass


def _pyformatdump(data): pass


def mayaStartupHasStarted():
    """
    Returns True if maya.app.startup has begun running, False otherwise.
    
    It's possible that maya.app.startup is in the process of running (ie,
    in maya.app.startup.basic, calling executeUserSetup) - unlike mayaStartup,
    this will attempt to detect if this is the case.
    """
    pass


def getImportableName(obj): pass


def _pyzipdump(data, filename): pass


def initMEL(): pass


def _pyczipdump(data, filename, pyc='True'): pass


_finalizeCalled = True

_mayaExitCallbackId = None

PY_CACHE_FORMAT_VERSION = ()

_logger = None

_atExitCallbackInstalled = False

pymel_options = {}
