from pymel.util.utilitytypes import *
from pymel.util.arguments import *

from pymel.util.objectParser import isParserClass
from pymel.util.objectParser import currentfn
from pymel.util.objectParser import Token
from pymel.util.objectParser import Parser
from pymel.util.objectParser import verbose
from pymel.util.common import uncapitalize
from pymel.util.objectParser import NameParseError
from pymel.util.objectParser import process
from pymel.util.objectParser import Parsed
from pymel.util.objectParser import ProxyUni
from pymel.util.objectParser import autoparsed
from pymel.util.common import capitalize
from pymel.util.objectParser import TokenParser
from pymel.util.objectParser import ParsingWarning
from pymel.util.objectParser import EmptyParser
from pymel.util.objectParser import isParsedClass
from pymel.util.objectParser import EmptyTokenParser

if False:
    from typing import Dict, List, Tuple, Union, Optional


class UnderscoreParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class IndexParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class NameSepParser(Parser):
    """
    A Parser for the MayaName NameGroup separator : one or more underscores
    """

    def p_sep(self, p):
        """
        NameSep : Underscore
        """
        pass

    def p_sep_concat(self, p):
        """
        NameSep : NameSep Underscore
        """
        pass

    precedence = ()

    start = 'NameSep'

    t_Underscore = '_+'


class NumParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class PipeParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class DotParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class NameBaseParser(Parser):
    """
    Base for name parser with common tokens
    """

    start = None

    t_Alpha = '([a-z]+)|([A-Z]+[a-z]*)'

    t_Num = '[0-9]+'


class NameParsed(Parsed):
    def isAttributeName(self):
        """
        True if this object is specified including one or more dag parents
        """
        pass

    def isComponentName(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
        pass

    def isNodeName(self):
        """
        True if this dag path name is absolute (starts with '|')
        """
        pass


class NamespaceSepParser(Parser):
    """
    A Parser for the Namespace separator
    """

    def p_nspace_sep(self, p):
        """
        NamespaceSep : Colon
        """
        pass

    precedence = ()

    start = 'NamespaceSep'

    t_Colon = ':'


class AlphaParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class Dot(Token):
    """
    Token stub class
    """

    pass


class ColonParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class Underscore(Token):
    """
    Token stub class
    """

    pass


class RangeIndexParser(TokenParser):
    """
    Token Parser stub class
    """

    pass


class Colon(Token):
    """
    Token stub class
    """

    pass


class Pipe(Token):
    """
    Token stub class
    """

    pass


class Index(Token):
    """
    Token stub class
    """

    pass


class NameIndexParser(Parser):
    """
    A Parser for attribute or component name indexes, in the form [<int number>]
    """

    def p_index(self, p):
        """
        NameIndex : Index
        """
        pass

    precedence = ()

    start = 'NameIndex'

    t_Index = r'\[(?:[0-9]+|-1)\]'


class Num(Token):
    """
    Token stub class
    """

    pass


class AttrSepParser(Parser):
    """
    A Parser for the MayaAttributePath separator
    """

    def p_attr_sep(self, p):
        """
        AttrSep : Dot
        """
        pass

    precedence = ()

    start = 'AttrSep'

    t_Dot = r'\.'


class DagPathSepParser(Parser):
    """
    A Parser for the DagPathSep separator
    """

    def p_dpath_sep(self, p):
        """
        DagPathSep : Pipe
        """
        pass

    precedence = ()

    start = 'DagPathSep'

    t_Pipe = r'\|'


class RangeIndex(Token):
    """
    Token stub class
    """

    pass


class NameRangeIndexParser(Parser):
    """
    A Parser for an index specification for an attribute or a component index,
    in the form [<optional int number>:<optional int number>]
    Rule : NameIndex = r'\[[0-9]*:[0-9]*\]'
    """

    def p_rindex(self, p):
        """
        NameRangeIndex : RangeIndex
        """
        pass

    precedence = ()

    start = 'NameRangeIndex'

    t_RangeIndex = r'\[[0-9]*:[0-9]*\]'


class Alpha(Token):
    """
    Token stub class
    """

    pass


class MayaNodePath(NameParsed):
    """
    A node name in Maya, one or more MayaShortName separated by DagPathSep, with an optional leading DagPathSep
    
        Rule : MayaNodePath = `DagPathSep` ? `MayaShortName` (`DagPathSep` `MayaShortName`) *
    
        Composed Of: `DagPathSep`, `MayaShortName`
    
        Component Of: `Component`, `NodeAttribute`
    
    Example
        >>> import pymel.util.nameparse as nameparse
        >>> obj = nameparse.parse( 'group1|pCube1|pCubeShape1' )
        >>> obj.setNamespace( 'foo:' )
        >>> print obj
        foo:group1|foo:pCube1|foo:pCubeShape1
        >>> print obj.parent
        foo:group1|foo:pCube1
        >>> print obj.node
        foo:pCubeShape1
        >>> print obj.node.basename
        pCubeShape1
        >>> print obj.node.namespace
        foo:
    """

    def addNamespace(self, namespace):
        """
        Append the namespace for all nodes in this path.
        """
        pass

    def addNode(self, node):
        """
        Add a node to the end of the path
        """
        pass

    def addPrefix(self, prefix):
        """
        Add a prefix to all nodes in the path. This must produce a valid maya name (no separators allowed).
        """
        pass

    def addSuffix(self, suffix):
        """
        Add a suffix to all nodes in the path. This must produce a valid maya name (no separators allowed).
        """
        pass

    def isAbsolute(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
        pass

    def isDagName(self):
        """
        True if this object is specified including one or more dag parents
        """
        pass

    def isLongName(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
        pass

    def isShortName(self):
        """
        True if this object node is specified as a short name (without a path)
        """
        pass

    def popNamespace(self, index='0'):
        """
        Remove an individual namespace (no separator) from all nodes in this path. An index of 0 (default) is the shallowest (leftmost) in the list.
        Returns a tuple containing the namespace popped from each node in the path or None if the node had no namespaces.
        """
        pass

    def popNode(self, index='-1'):
        """
        Remove a node from the end of the path
        """
        pass

    def setNamespace(self, namespace):
        """
        Set the namespace for all nodes in this path. The provided namespace may be nested and should including a trailing colon unless it is empty.
        """
        pass

    def shortName(self):
        """
        The last short name of the path
        """
        pass

    @property
    def first(self):
        """
        First node name of that dag path name (root of the path)
        """
        pass

    @property
    def last(self):
        """
        Last node name of that dag path name (leaf of the path, equivalent to self.node)
        """
        pass

    @property
    def node(self):
        """
        The last short name of the path
        """
        pass

    @property
    def nodePaths(self):
        """
        All the long names in the dag path including the last
        """
        pass

    @property
    def nodes(self):
        """
        All the short names in the dag path including the last, without separators
        """
        pass

    @property
    def parent(self):
        """
        Parent of the last node in the dag hierarchy
        """
        pass

    @property
    def parents(self):
        """
        All the dags in the dag hierarchy above the last node, starting from last up
        """
        pass

    @property
    def parts(self):
        """
        All parts of that node name, including separators
        """
        pass

    @property
    def root(self):
        """
        First node name of that dag path name (root of the path)
        """
        pass

    @property
    def separator(self): pass


class AttrSep(NameParsed):
    """
    The Maya attribute separator : the dot '.'
    
        Rule : AttrSep = r'\.'
    
        Component Of: `Component`, `AttributePath`, `NodeAttribute`
    """

    @classmethod
    def default(cls): pass


class NamePart(NameParsed):
    """
    A name part of either the NameAlphaPart or NameNumPart kind
    
        Rule : NamePart = `NameAlphaPart` | `NameNumPart`
    
        Composed Of: `NameAlphaPart`, `NameNumPart`
    
        Component Of: `NameNumGroup`
    """

    def isAlpha(self): pass

    def isNum(self): pass


class DagPathSep(NameParsed):
    """
    The Maya long names separator : the pipe '|'
    
        Rule : DagPathSep = r'\|'
    
        Component Of: `MayaNodePath`
    """

    @classmethod
    def default(cls): pass


class MayaShortName(NameParsed):
    """
    A short node name in Maya, a Maya name, possibly preceded by a Namespace
    
        Rule : MayaShortName = `Namespace` ? `MayaName`
    
        Composed Of: `Namespace`, `MayaName`
    
        Component Of: `MayaNodePath`
    """

    def addPrefix(self, prefix):
        """
        Add a prefix to the node name. This must produce a valid maya name (no separators allowed).
        """
        pass

    def addSuffix(self, suffix):
        """
        Add a suffix to the node name. This must produce a valid maya name (no separators allowed).
        """
        pass

    def getBaseName(self):
        """
        Get the short node name of the object
        """
        pass

    def getBaseNamespace(self):
        """
        Get the namespace for the current node
        """
        pass

    def isAbsoluteNamespace(self):
        """
        True if this object is specified in an absolute namespace
        """
        pass

    def setBaseName(self, name):
        """
        Set the name of the object.  Should not include namespace
        """
        pass

    def setNamespace(self, namespace):
        """
        Set the namespace. The provided namespace may be nested and should including a trailing colon unless it is empty.
        """
        pass

    @property
    def basename(self):
        """
        The short node name without any namespace of the Maya short object name
        """
        pass

    @property
    def first(self):
        """
        All parts of that name group
        """
        pass

    @property
    def last(self):
        """
        All parts of that name group
        """
        pass

    @property
    def namespace(self):
        """
        The namespace name (full) of the Maya short object name
        """
        pass

    @property
    def parts(self):
        """
        All parts of that namespace, including separators
        """
        pass


class NameGroup(NameParsed):
    """
    A name group of either the NameAlphaGroup or NameNumGroup kind
    
        Rule : NameGroup = `NameAlphaGroup` | `NameNumGroup`
    
        Composed Of: `NameAlphaGroup`, `NameNumGroup`
    
        Component Of: `MayaName`
    """

    def isAlpha(self): pass

    def isNum(self): pass

    def nextName(self): pass

    def prevName(self): pass

    @property
    def first(self):
        """
        First part of that name group
        """
        pass

    @property
    def last(self):
        """
        Last part of that name group
        """
        pass

    @property
    def parts(self):
        """
        All parts of that name group
        """
        pass

    @property
    def tail(self):
        """
        The tail (trailing numbers if any) of that name group
        """
        pass


class NameAlphaPartParser(NameBaseParser):
    """
    Parser for a name part starting with a letter
    """

    def p_apart(self, p):
        """
        NameAlphaPart : Alpha
        """
        pass

    start = 'NameAlphaPart'


class Namespace(NameParsed):
    """
    A Maya namespace name, one or more MayaName separated by ':'
    
        Rule : Namespace = `NamespaceSep` ? (`MayaName` `NamespaceSep`) +
    
        Composed Of: `NamespaceSep`, `MayaName`
    
        Component Of: `MayaShortName`
    """

    def append(self, namespace):
        """
        Append a namespace. Can include separator and multiple namespaces. The new namespace will be the shallowest (leftmost) namespace.
        """
        pass

    def isAbsolute(self):
        """
        True if this namespace is an absolute namespace path (starts with ':')
        """
        pass

    def pop(self, index='0'):
        """
        Remove an individual namespace (no separator). An index of 0 (default) is the shallowest (leftmost) in the list
        """
        pass

    def setSpace(self, index, space):
        """
        Set the namespace at the given index
        """
        pass

    @classmethod
    def default(cls): pass

    @property
    def first(self):
        """
        First individual namespace of that namespace
        """
        pass

    @property
    def last(self):
        """
        Last individual namespace in that namespace
        """
        pass

    @property
    def parent(self):
        """
        All the individual namespaces in the namespace but the last, starting from last up, without separators
        """
        pass

    @property
    def parents(self):
        """
        All the nested namespaces names (full) in the namespace but the last, starting from last up
        """
        pass

    @property
    def parts(self):
        """
        All parts of that namespace, including separators
        """
        pass

    @property
    def path(self):
        """
        All nested namespaces in that Maya namespace
        """
        pass

    @property
    def separator(self): pass

    @property
    def space(self):
        """
        Last namespace of the individual namespaces
        """
        pass

    @property
    def spaces(self):
        """
        All different individual namespaces in that Maya namespace, skipping separators
        """
        pass


class NameIndex(NameParsed):
    """
    An index specification for an attribute or a component index, in the form [<int number>]
    
        Rule : NameIndex = r'\[[0-9]+\]'
    
        Component Of: `Attribute`
    """

    @staticmethod
    def __new__(cls, *args, **kwargs):
        """
        # to allow initialization from a single int
        """
        pass

    @property
    def value(self):
        """
        Index of that node attribute name
        """
        pass


class Attribute(NameParsed):
    """
    The name of a Maya attribute on a Maya node, a MayaName with an optional NameIndex
    
        Rule : Attribute = `MayaName` `NameIndex` ?
    
        Composed Of: `MayaName`, `NameIndex`
    
        Component Of: `AttributePath`
    """

    def isCompound(self): pass

    @property
    def bracketedIndex(self):
        """
        Index of that node attribute name
        """
        pass

    @property
    def index(self):
        """
        Int value of the index of that node attribute name
        """
        pass

    @property
    def name(self):
        """
        name(without index) of that node attribute name
        """
        pass

    @property
    def parts(self):
        """
        All groups of that name, including separators
        """
        pass


class Empty(NameParsed):
    @classmethod
    def default(cls): pass


class NameSep(NameParsed):
    """
    the MayaName NameGroup separator : one or more underscores
    
        Rule : NameSep = r'_+'
    
        Component Of: `MayaName`
    """

    def reduced(self):
        """
        Reduce multiple underscores to one
        """
        pass

    @classmethod
    def default(cls): pass


class NameNumPartParser(NameBaseParser):
    """
    Parser for a name part starting with a number
    """

    def p_npart(self, p):
        """
        NameNumPart : Num
        """
        pass

    start = 'NameNumPart'


class Component(NameParsed):
    """
    A Maya component name of any of the single, double or triple indexed kind
    
        Rule : Component = SingleComponentName | DoubleComponentName | TripleComponentName
    
        Component Of: `MayaObjectName`
    """

    pass


class NodeAttribute(NameParsed):
    """
    The name of a Maya node and attribute (plug): a MayaNodePath followed by a AttrSep and a AttributePath
    
        Rule : NodeAttribute = `MayaNodePath` `AttrSep` `AttributePath`
    
        Composed Of: `MayaNodePath`, `AttrSep`, `AttributePath`
    
        Component Of: `MayaObjectName`
    
    
        >>> nodeAttr = NodeAttribute( 'persp|perspShape.focalLength' )
        >>> nodeAttr.attributes
        (Attribute('focalLength', 17),)
        >>> nodeAttr.nodePath
        MayaNodePath('persp|perspShape', 0)
        >>> nodeAttr.shortName()
        NodeAttribute('perspShape.focalLength', 0)
        >>>
        >>> nodeAttr2 = NodeAttribute( 'persp.translate.tx' )
        >>> nodeAttr2.attributes
        (Attribute('translate', 6), Attribute('tx', 16))
    """

    def popNode(self):
        """
        Remove a node from the end of the path, preserving any attributes (Ex. pCube1|pCubeShape1.width --> pCube1.width).
        """
        pass

    def shortName(self):
        """
        Just the node and attribute without the full dag path. Returns a copy.
        """
        pass

    @property
    def attribute(self):
        """
        The attribute part of the plug
        """
        pass

    @property
    def attributes(self):
        """
        All the node attribute names in that node attribute path, including the last, without separators
        """
        pass

    @property
    def nodePath(self):
        """
        The node part of the plug
        """
        pass

    @property
    def parts(self):
        """
        All parts of that attribute name, including separators
        """
        pass

    @property
    def separator(self): pass


class AttributePath(NameParsed):
    """
    The full path of a Maya attribute on a Maya node, as one or more AttrSep ('.') separated Attribute
    
        Rule : AttributePath = ( `Attribute` `AttrSep` ) * `Attribute`
    
        Composed Of: `Attribute`, `AttrSep`
    
        Component Of: `NodeAttribute`
    """

    def isCompound(self): pass

    @property
    def attributes(self):
        """
        All the node attribute names in that node attribute path, including the last, without separators
        """
        pass

    @property
    def first(self):
        """
        First node attribute name of that node attribute path (root of the path)
        """
        pass

    @property
    def last(self):
        """
        Last node attribute name of that node attribute path (leaf of the path, equivalent to self.attribute)
        """
        pass

    @property
    def parent(self):
        """
        Parent of the last node attribute name in the path
        """
        pass

    @property
    def parents(self):
        """
        All the node attributes names (full) in the attribute path above the last node attribute name, starting from last up
        """
        pass

    @property
    def parts(self):
        """
        All parts of that node attribute path name, including separators
        """
        pass

    @property
    def path(self):
        """
        All nested namespaces in that Maya namespace
        """
        pass

    @property
    def separator(self): pass


class NamespaceSep(NameParsed):
    """
    The Maya Namespace separator : the colon ':'
    
        Rule : NamespaceSep = r':'
    
        Component Of: `Namespace`
    """

    @classmethod
    def default(cls): pass


class MayaName(NameParsed):
    """
    The most basic Maya Name : several name groups separated by one or more underscores,
    starting with a NameHead or one or more underscore, followed by zero or more NameGroup
    
        Rule : MayaName = (`NameSep` * `NameAlphaGroup`) | (`NameSep` + `NameNumGroup`)  ( `NameSep` `NameGroup` ) * `NameSep` *
    
        Composed Of: `NameSep`, `NameAlphaGroup`, `NameNumGroup`, `NameGroup`
    
        Component Of: `Namespace`, `MayaShortName`, `Attribute`
    """

    def extractNum(self):
        """
        Return the trailing numbers of the node name. If no trailing numbers are found
        an error will be raised.
        """
        pass

    def nextName(self):
        """
        Increment the trailing number of the object by 1
        """
        pass

    def nextUniqueName(self):
        """
        Increment the trailing number of the object until a unique name is found
        """
        pass

    def prevName(self):
        """
        Decrement the trailing number of the object by 1
        """
        pass

    def reduced(self):
        """
        Reduces all separators in thet Maya Name to one underscore, eliminates head and tail separators if not needed
        """
        pass

    @property
    def first(self):
        """
        First group of that Maya name
        """
        pass

    @property
    def groups(self):
        """
        All groups of that Maya name, skipping separators
        """
        pass

    @property
    def last(self):
        """
        Last group of that Maya name
        """
        pass

    @property
    def parts(self):
        """
        All groups of that name, including separators
        """
        pass

    @property
    def tail(self):
        """
        The tail (trailing numbers if any) of that Maya Name
        """
        pass


class NameRangeIndex(NameParsed):
    """
    An index specification for an attribute or a component index, in the form::
        [<optional int number>:<optional int number>]
    
        Rule : NameIndex = r'\[[0-9]*:[0-9]*\]'
    """

    @classmethod
    def default(cls): pass

    @staticmethod
    def __new__(cls, *args, **kwargs): pass

    @property
    def bounds(self):
        """
        start and end bounds (inclusive) of that component index range
        """
        pass

    @property
    def end(self):
        """
        end (inclusive) of that component index range
        """
        pass

    @property
    def range(self):
        """
        Python styled range (start and exclusive end) of that component index range
        """
        pass

    @property
    def start(self):
        """
        start of that component index range
        """
        pass


class MayaObjectName(NameParsed):
    """
    An object name in Maya, can be a dag object name, a node name,
    an plug name, a component name or a ui name
    
        Rule : MayaObjectName = `MayaNodePath` | `NodeAttribute` | `Component`
    
        Composed Of: `MayaNodePath`, `NodeAttribute`, `Component`
    """

    def isAttributeName(self):
        """
        True if this object is specified including one or more dag parents
        """
        pass

    def isComponentName(self):
        """
        True if this object is specified as an absolute dag path (starting with '|')
        """
        pass

    def isNodeName(self):
        """
        True if this dag path name is absolute (starts with '|')
        """
        pass

    @property
    def attribute(self):
        """
        The attribute (full) name for a NodeAttribute (node.attribute) name
        """
        pass

    @property
    def attributes(self):
        """
        All the node attribute names in that node attribute path, including the last, without separators
        """
        pass

    @property
    def component(self):
        """
        The component name for a Component (node.component) name
        """
        pass

    @property
    def node(self):
        """
        The full path of the node
        """
        pass

    @property
    def nodes(self):
        """
        All the short names in the dag path including the last, without separators
        """
        pass

    @property
    def object(self):
        """
        The actual Maya object name (node, attribute or component) it encapsulate
        """
        pass

    @property
    def parts(self):
        """
        All parts of that object name, including separators
        """
        pass

    @property
    def type(self):
        """
        What kind of Maya object is it, a node, an attribute or a component
        """
        pass


class NameAlphaGroupParser(NameAlphaPartParser, NameNumPartParser):
    """
    A Parser for suitable groups for a name head : one or more name parts, the first part starting with a letter
    NameAlphaGroup = NameAlphaPart NamePart *
    """

    def p_agroup(self, p):
        """
        NameAlphaGroup : NameAlphaPart
        """
        pass

    def p_agroup_concat(self, p):
        """
        NameAlphaGroup : NameAlphaGroup NameAlphaPart
        |  NameAlphaGroup NameNumPart
        """
        pass

    start = 'NameAlphaGroup'


class NameAlphaGroup(NameGroup):
    """
    A name group starting with an alphabetic part
    
        Rule : NameAlphaGroup  = `NameAlphaPart` `NamePart` *
    
        Composed Of: `NameAlphaPart`, `NamePart`
    
        Component Of: `NameNumGroup`
    """

    def isAlpha(self): pass

    def isNum(self): pass


class NameNumPart(NamePart):
    """
    A name part made of numbers
    
        Rule : NameNumPart = r'[0-9]+'
    """

    def isAlpha(self): pass

    def isNum(self): pass

    @staticmethod
    def __new__(cls, *args, **kwargs):
        """
        # to allow initialization from a single int
        """
        pass

    @property
    def value(self): pass


class NameNumGroupParser(NameAlphaPartParser, NameNumPartParser):
    """
    A Parser for suitable groups for a name body : one or more name parts, the first part starting with a number
    NameNumGroup = NameNumPart NamePart *
    """

    def p_ngroup(self, p):
        """
        NameNumGroup : NameNumPart
        """
        pass

    def p_ngroup_concat(self, p):
        """
        NameNumGroup : NameNumGroup NameAlphaPart
        | NameNumGroup NameNumPart
        """
        pass

    start = 'NameNumGroup'


class NameAlphaPart(NamePart):
    """
    A name part made of alphabetic letters
    
        Rule : NameAlphaPart = r'([a-z]+)|([A-Z]+[a-z]*)'
    
        Component Of: `NameNumGroup`, `NameAlphaGroup`
    """

    def isAlpha(self): pass

    def isNum(self): pass


class NameNumGroup(NameGroup):
    """
    A name group starting with an alphabetic part
    
        Rule : NameAlphaGroup  = `NameAlphaPart` `NamePart` *
    
        Composed Of: `NameAlphaPart`, `NamePart`
    
        Component Of: `MayaName`
    """

    def isAlpha(self): pass

    def isNum(self): pass


class NamePartParser(NameAlphaPartParser, NameNumPartParser):
    """
    Parser for a name part of either the NameAlphaPart or NameNumPart kind
    """

    def p_part(self, p):
        """
        NamePart : NameAlphaPart
        | NameNumPart
        """
        pass

    start = 'NamePart'


class NameGroupParser(NameAlphaGroupParser, NameNumGroupParser):
    """
    A Parser for a name group of either the NameAlphaGroup or NameNumGroup kind
    """

    def p_group(self, p):
        """
        NameGroup : NameAlphaGroup
        | NameNumGroup
        """
        pass

    start = 'NameGroup'


class MayaNameParser(NameSepParser, NameGroupParser):
    """
    A Parser for the most basic Maya Name : several name groups separated by one or more underscores,
    starting with an alphabetic part or one or more underscore, followed by zero or more NameGroup(s)
    separated by underscores
    """

    def p_name(self, p):
        """
        MayaName : NameSep NameGroup
        | NameAlphaGroup
        """
        pass

    def p_name_concat(self, p):
        """
        MayaName : MayaName NameSep NameGroup
        | MayaName NameSep
        """
        pass

    def p_name_error(self, p):
        """
        MayaName : error
        """
        pass

    start = 'MayaName'


class SingleComponentNameParser(NameRangeIndexParser, NameIndexParser, MayaNameParser):
    """
    A NameParsed for the reserved single indexed components names:
    vtx,
    Rule : NameIndex = r'\[[0-9]*:[0-9]*\]'
    """

    pass


class NamespaceParser(NamespaceSepParser, MayaNameParser, EmptyParser):
    """
    A Parser for Namespace, Maya namespaces names
    """

    def p_nspace(self, p):
        """
        Namespace : MayaName NamespaceSep
        | NamespaceSep
        | Empty
        """
        pass

    def p_nspace_concat(self, p):
        """
        Namespace : Namespace MayaName NamespaceSep
        """
        pass

    start = 'Namespace'


class DoubleComponentNameParser(NameRangeIndexParser, NameIndexParser, MayaNameParser):
    pass


class TripleComponentNameParser(NameRangeIndexParser, NameIndexParser, MayaNameParser):
    pass


class NodeAttributeNameParser(NameIndexParser, MayaNameParser):
    """
    Parser for a Attribute, the name of a Maya attribute on a Maya node, a MayaName with an optional NameIndex
    """

    def p_nodeattr(self, p):
        """
        Attribute : MayaName NameIndex
        | MayaName
        """
        pass

    def p_nodeattr_error(self, p):
        """
        Attribute : error
        """
        pass

    start = 'Attribute'


class MayaShortNameParser(NamespaceParser, MayaNameParser):
    """
    A parser for MayaShortName, a short object name (without preceding path) with a possible preceding namespace
    """

    def p_sname(self, p):
        """
        MayaShortName : Namespace MayaName
        | MayaName
        """
        pass

    start = 'MayaShortName'


class NodeAttributePathParser(AttrSepParser, NodeAttributeNameParser):
    """
    Parser for a full path of a Maya attribute on a Maya node, as one or more AttrSep ('.') separated Attribute
    """

    def p_nodeattrpath(self, p):
        """
        AttributePath : Attribute
        """
        pass

    def p_nodeattrpath_concat(self, p):
        """
        AttributePath : AttributePath AttrSep Attribute
        """
        pass

    start = 'AttributePath'


class ComponentNameParser(SingleComponentNameParser, DoubleComponentNameParser, TripleComponentNameParser):
    pass


class MayaNodePathParser(DagPathSepParser, MayaShortNameParser):
    """
    a Parser for Maya node name, an optional leading DagPathSep followed by one or more
    MayaShortName separated by DagPathSep
    """

    def p_node(self, p):
        """
        MayaNodePath : DagPathSep MayaShortName
        | MayaShortName
        """
        pass

    def p_node_concat(self, p):
        """
        MayaNodePath : MayaNodePath DagPathSep MayaShortName
        """
        pass

    start = 'MayaNodePath'


class AttributeNameParser(NodeAttributePathParser, MayaNodePathParser):
    """
    Parser for the name of a Maya attribute, a MayaNodePath followed by a AttrSep and a AttributePath
    """

    def p_attribute(self, p):
        """
        NodeAttribute : MayaNodePath AttrSep AttributePath
        """
        pass

    start = 'NodeAttribute'


class MayaObjectNameParser(AttributeNameParser):
    """
    A Parser for an unspecified object name in Maya, can be a dag object name, a node name,
    an plug name, or a component name.
    """

    def p_mobject(self, p):
        """
        MayaObjectName : MayaNodePath
        | NodeAttribute
        """
        pass

    start = 'MayaObjectName'


def _decomposeObjectName(name, ident='0'): pass


def _decomposeName(name, ident='0'): pass


def _itest():
    """
    Inerractive name parsing test, enter a name and see result decomposition
    """
    pass


def _decomposeShortName(name, ident='0'): pass


def _decomposeNodeAttributeName(name, ident='0'): pass


def _decomposeAttributeName(name, ident='0'): pass


def _decomposeGroup(name, ident='0'): pass


def _decomposeNodeAttributePathName(name, ident='0'): pass


def getBasicPartList(name):
    """
    convenience function for breaking apart a maya object to the appropriate level for pymel name parsing
    
        >>> getBasicPartList('thing|foo:bar.attr[0].child')
        [MayaNodePath('thing|foo:bar', 0), MayaName('attr', 14), NameIndex('[0]', 18), MayaName('child', 22)]
    """
    pass


def _test(expr):
    """
    Tests the name parsing of the string argument expr and displays results
    """
    pass


def _decomposeNamespace(name, ident='0'): pass


def _decomposeNodeName(name, ident='0'): pass


def parse(name):
    """
    main entry point for parsing a maya node name
    """
    pass
