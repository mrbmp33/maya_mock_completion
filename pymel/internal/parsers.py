from abc import ABCMeta
from abc import abstractmethod
from pymel.util.external.BeautifulSoup import NavigableString
from HTMLParser import HTMLParser
from pymel.util.external.BeautifulSoup import BeautifulSoup
from pymel.mayautils import getMayaLocation

if False:
    from typing import Dict, List, Tuple, Union, Optional


class NodeHierarchyDocParser(HTMLParser):
    def __init__(self, version='None'): pass

    def handle_data(self, data): pass

    def handle_starttag(self, tag, attrs): pass

    def parse(self): pass


class ApiDocParser(object):
    def __init__(self, apiModule, version='None', verbose='False', enumClass='"<type \'tuple\'>"', docLocation='None',
                 strict='False'): pass

    def __repr__(self): pass

    def formatMsg(self, *args): pass

    def fullMethodName(self): pass

    def getClassFilename(self): pass

    def getClassPath(self): pass

    def getMethodNameAndOutput(self): pass

    def getOperatorName(self, methodName): pass

    def getPymelMethodNames(self): pass

    def handleEnumDefaults(self, default, type): pass

    def handleEnums(self, type): pass

    def hasNoPython(self): pass

    def isBadEnum(self, type): pass

    def isGetMethod(self): pass

    def isSetMethod(self): pass

    def isStaticMethod(self): pass

    def parse(self, apiClassName): pass

    def parseArgTypes(self): pass

    def parseBody(self): pass

    def parseEnum(self, enumData): pass

    def parseMethod(self, rawMethod): pass

    def parseMethodArgs(self, returnType, names, types, typeQualifiers): pass

    def parseType(self, tokens): pass

    def parseValue(self, rawValue, valueType): pass

    def setClass(self, apiClassName): pass

    def xprint(self, *args): pass

    @staticmethod
    def __new__(cls, apiModule, version='None', *args, **kwargs): pass

    DEPRECATED_MSG = []

    MISSING_TYPES = []

    NOT_TYPES = []

    NO_PYTHON_MSG = []

    OTHER_TYPES = []

    PYMEL_ENUM_DEFAULTS = {}

    __abstractmethods__ = frozenset()

    __dict__ = None

    __weakref__ = None


class MLStripper(HTMLParser):
    """
    # Thanks to Eloff for this snippet: https://stackoverflow.com/a/925630/920545
    """

    def __init__(self): pass

    def get_data(self): pass

    def handle_data(self, d): pass


class CommandDocParser(HTMLParser):
    def __init__(self, command): pass

    def __repr__(self): pass

    def addFlagData(self, data): pass

    def endFlag(self): pass

    def handle_data(self, data): pass

    def handle_endtag(self, tag): pass

    def handle_entityref(self, name): pass

    def handle_starttag(self, tag, attrs): pass

    def startFlag(self, data): pass


class CommandModuleDocParser(HTMLParser):
    def __init__(self, category, version='None'): pass

    def handle_starttag(self, tag, attrs): pass

    def parse(self): pass


class XmlApiDocParser(ApiDocParser):
    def fullMethodName(self): pass

    def getClassPath(self): pass

    def getMethodNameAndOutput(self): pass

    def hasNoPython(self): pass

    def isDeprecated(self): pass

    def isStaticMethod(self): pass

    def parseArgTypes(self): pass

    def parseBody(self): pass

    def parseMethodArgs(self, returnType, names, types, typeQualifiers): pass

    def setClass(self, apiClassName): pass

    @classmethod
    def iterBackslashTags(cls, text, subTags="('li',)"):
        """
        Iterator that parses text with tags like: "\tag Some text for tag"
        
        Sometimes detail text does not parse parameters properly, and we end up with text like this,
        from 2019 MFnMesh.addPolygon 2nd overload (with 6 args):
        
        If we are adding to an existing polygonal mesh then parentOrOwner is
        ignored and the geometry is returned.
        
        \param[in] vertexArray Array of ordered vertices that make up the polygon.
        \param[in] loopCounts Array of vertex loop counts.
        \param[out] faceIndex Index of the newly added polygon.
        \param[in] mergeVertices If true then if a vertex falls within
                                                            pointTolerance of an existing vertex then the
                                                            existing vertex is reused.
        \param[in] pointTolerance Specifies how close verticies have to be to
                                                            before they are &lt;i&gt;merged&lt;/i&gt;.  This merging is
                                                            only done if &lt;i&gt;mergeVerticies&lt;/i&gt; is true.
        \param[in] parentOrOwner The DAG parent or kMeshData the new
                                                            surface will belong to.
        \param[out] ReturnStatus Status code.
        
        \return
        The transform if one is created, otherwise the geometry.
        
        This code will iterate through, finding lines that start with a "backslash tag", and issuing tuples like this:
        
        ("param[in]", "vertexArray Array of ordered vertices that make up the polygon.\n")
        ("param[in]", "loopCounts Array of vertex loop counts.\n")
        
        The text before we find the first tag will be ignored.
        """
        pass

    @classmethod
    def parseBackslashTags(cls, text): pass

    __abstractmethods__ = frozenset()


class HtmlApiDocParser(ApiDocParser):
    def getClassPath(self): pass

    def getDoxygenVersion(self, soup): pass

    def getMethodNameAndOutput(self): pass

    def hasNoPython(self): pass

    def isStaticMethod(self): pass

    def parseArgTypes(self): pass

    def parseBody(self): pass

    def parseMethodArgs(self, returnType, names, types, typeQualifiers): pass

    def setClass(self, apiClassName): pass

    DOXYGEN_VER_RE = None

    TYPEDEF_RE = None

    __abstractmethods__ = frozenset()


def mayaDocsLocation(version='None'): pass


def getFirstText(element, ignore="('ref', 'bold', 'emphasis')"):
    """
    Finds a non-empty text element, then stops once it hits not first non-filtered sub-element
    
    >>> getFirstText(ET.fromstring('<top>Some text. <sub>Blah</sub> tail.</top>'))
    'Some text.'
    >>> getFirstText(ET.fromstring('<top><sub>Blah blah</sub> More stuff</top>'))
    'Blah blah'
    >>> getFirstText(ET.fromstring('<top> <sub>Blah blah <ref>someRef</ref> More stuff</sub> The end</top>'))
    'Blah blah someRef More stuff'
    """
    pass


def _iskeyword(*args, **kwargs):
    """
    x.__contains__(y) <==> y in x.
    """
    pass


def standardizeWhitespace(text): pass


def xmlText(element, strip='True', allowNone='True'):
    """
    Given an xml Element object, returns it's full text (with children)
    
    If predicate is given, and it returns False for this element or any child,
    then text generation will be terminated at that point.
    """
    pass


def strip_tags(html): pass


def mayaIsRunning():
    """
    Returns True if maya.cmds have  False otherwise.
    
    Early in interactive startup it is possible for commands to exist but for Maya to not yet be initialized.
    
    Returns
    -------
    bool
    """
    pass


def printTree(tree, depth='0'): pass


def iterXmlTextAndElem(element):
    """
    Like Element.itertext, except returns a tuple of (text, element, isTail)
    """
    pass


_logger = None

FLAGMODES = ()
