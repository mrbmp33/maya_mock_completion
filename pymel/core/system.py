"""
In particular, the system module contains the functionality of maya.cmds.file. The file command should not be imported into
the default namespace because it conflicts with python's builtin file class. Since the file command has so many flags,
we decided to kill two birds with one stone: by breaking the file command down into multiple functions -- one for each
primary flag -- the resulting functions are more readable and allow the file command's functionality to be used directly
within the pymel namespace.

for example, instead of this:

    >>> res = cmds.file( 'test.ma', exportAll=1, preserveReferences=1, type='mayaAscii', force=1 ) # doctest: +SKIP

you can do this:

    >>> expFile = exportAll( 'test.ma', preserveReferences=1, force=1)

some of the new commands were changed slightly from their flag name to avoid name clashes and to add to readability:

    >>> importFile( expFile )  # flag was called import, but that's a python keyword
    >>> ref = createReference( expFile )
    >>> ref # doctest: +ELLIPSIS
    FileReference(u'...test.ma', refnode=u'testRN')

Notice that the 'type' flag is set automatically for you when your path includes a '.mb' or '.ma' extension.

Paths returned by these commands are either a `Path` or a `FileReference`, so you can use object-oriented path methods with
the results::

    >>> expFile.exists()
    True
    >>> expFile.remove() # doctest: +ELLIPSIS
    Path('...test.ma')
"""

from pymel.internal.pmcmds import showHelp
from pymel.internal.pmcmds import selLoadSettings
from pymel.internal.pmcmds import unassignInputDevice
from pymel.internal.pmcmds import dgeval
from pymel.internal.pmcmds import redo
from pymel.internal.pmcmds import filePathEditor
from pymel.internal.pmcmds import getFileList
from pymel.internal.pmcmds import moduleInfo
from pymel.internal.pmcmds import dbmessage
from pymel.internal.pmcmds import dbcount
from pymel.internal.pmcmds import autoSave
from pymel.internal.pmcmds import dagObjectCompare
from pymel.internal.pmcmds import imfPlugins
from pymel.internal.pmcmds import unknownNode
from pymel.internal.pmcmds import hardware
from pymel.internal.pmcmds import dirmap
from pymel.internal.pmcmds import launchImageEditor
from pymel.internal.pmcmds import translator
from pymel.internal.pmcmds import dgValidateCurve
from pymel.internal.pmcmds import hitTest
from pymel.internal.pmcmds import deviceEditor
from pymel.internal.pmcmds import loadModule
from pymel.internal.pmcmds import listInputDeviceButtons
from pymel.internal.pmcmds import getInputDeviceRange
from pymel.internal.pmcmds import convertUnit
from pymel.internal.pmcmds import requires
from pymel.internal.pmcmds import profilerTool
from pymel.internal.pmcmds import recordAttr
from pymel.internal.pmcmds import clearCache
from pymel.internal.pmcmds import whatsNewHighlight
from pymel.internal.pmcmds import scriptNode
from pymel.internal.pmcmds import xpmPicker
from pymel.internal.pmcmds import openGLExtension
from pymel.internal.pmcmds import timerX
from pymel.internal.pmcmds import warning
from pymel.internal.pmcmds import dbfootprint
from pymel.internal.pmcmds import mouse
from pymel.internal.pmcmds import aaf2fcp
from pymel.internal.pmcmds import cacheFileMerge
from pymel.internal.pmcmds import date
from pymel.internal.pmcmds import dgInfo
from pymel.internal.pmcmds import cacheFile
from pymel.internal.pmcmds import detachDeviceAttr
from pymel.internal.pmcmds import audioTrack
from pymel.internal.pmcmds import sceneUIReplacement
from pymel.internal.pmcmds import dbpeek
from pymel.internal.pmcmds import crashInfo
from pymel.internal.pmcmds import getModulePath
from pymel.internal.pmcmds import listDeviceAttachments
from pymel.internal.pmcmds import assignInputDevice
from pymel.internal.pmcmds import findType
from pymel.internal.pmcmds import openMayaPref
from pymel.internal.pmcmds import error
from pymel.internal.pmcmds import setAttrMapping
from pymel.internal.pmcmds import attrCompatibility
from pymel.internal.pmcmds import dgtimer
from pymel.internal.pmcmds import profiler
from pymel.internal.pmcmds import launch
from pymel.internal.pmcmds import dgfilter
from pymel.internal.pmcmds import melInfo
from pymel.internal.pmcmds import internalVar
from pymel.internal.pmcmds import displayString
from pymel.internal.pmcmds import listInputDeviceAxes
from pymel.internal.pmcmds import pluginDisplayFilter
from pymel.internal.pmcmds import fileDialog
from pymel.internal.pmcmds import dbtrace
from pymel.internal.pmcmds import timer
from pymel.internal.pmcmds import flushUndo
from pymel.internal.pmcmds import shotTrack
from pymel.internal.pmcmds import reloadImage
from pymel.internal.pmcmds import diskCache
from pymel.internal.pmcmds import rehash
from pymel.internal.pmcmds import dynamicLoad
from pymel.internal.pmcmds import listInputDevices
from pymel.internal.pmcmds import allNodeTypes
from pymel.util.scanf import fscanf
from pymel.internal.pmcmds import memory
from pymel.internal.pmcmds import setInputDeviceMapping
from pymel.internal.pmcmds import dgdirty
from pymel.internal.pmcmds import namespace
from pymel.internal.pmcmds import cmdFileOutput
from pymel.internal.pmcmds import ogs
from pymel.internal.pmcmds import attachDeviceAttr
from pymel.internal.pmcmds import undo
from pymel.internal.pmcmds import sysFile
from pymel.internal.pmcmds import cacheFileCombine
from pymel.internal.pmcmds import dgmodified
from pymel.internal.pmcmds import undoInfo
from pymel.internal.pmcmds import cacheFileTrack
from pymel.internal.pmcmds import getModifiers
from pymel.util.path import path as pathClass
from pymel.util.decoration import decorator
from pymel.internal.pmcmds import unknownPlugin
from pymel.internal.pmcmds import fcheck

if False:
    from typing import Dict, List, Tuple, Union, Optional


class ReferenceEdit(str):
    """
    Parses a reference edit command string into various components based on the edit type.
    This is the class returned by pymel's version of the 'referenceQuery' command.
    """

    def remove(self, force='False'):
        """
        Remove the reference edit. if 'force=True' then the reference will be unloaded from the scene (if it is not already unloaded)
        """
        pass

    @staticmethod
    def __new__(cls, editStr, fileReference='None', successful='None'): pass

    @property
    def editData(self): pass

    @property
    def fullNamespace(self): pass

    @property
    def namespace(self): pass

    @property
    def rawEditData(self): pass

    __dict__ = None


class _Container(object):
    def __contains__(self, x): pass

    @classmethod
    def __subclasshook__(cls, C): pass

    __abstractmethods__ = frozenset()

    __dict__ = None

    __weakref__ = None


class WorkspaceEntryDict(object):
    def __contains__(self, key): pass

    def __getitem__(self, item): pass

    def __init__(self, entryType): pass

    def __iter__(self): pass

    def __repr__(self): pass

    def __setitem__(self, item, value): pass

    def get(self, item, default='None'): pass

    def has_key(self, key): pass

    def items(self): pass

    def keys(self): pass

    def values(self): pass

    __dict__ = None

    __weakref__ = None


class Path(pathClass):
    """
    A basic Maya file class. it gets most of its power from the path class written by Jason Orendorff.
    see path.py for more documentation.
    """

    def __repr__(self): pass

    def getTypeName(self, **kwargs):
        """
        Set the type of this file.  By default this can be any one of: mayaAscii, mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R) Illustrator(R), imageplug-ins may define their own types as well.Return a string array of file types that match this file.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def setSubType(self, **kwargs): pass


class Workspace(object):
    """
    This class is designed to lend more readability to the often confusing workspace command.
    The four types of workspace entries (objectType, fileRule, renderType, and variable) each
    have a corresponding dictiony for setting and accessing these mappings.
    
        >>> from pymel.all import *
        >>> workspace.fileRules['mayaAscii']
        u'scenes'
        >>> workspace.fileRules.keys() # doctest: +ELLIPSIS
        [...u'mayaAscii', u'mayaBinary',...]
        >>> 'mayaBinary' in workspace.fileRules
        True
        >>> workspace.fileRules['super'] = 'data'
        >>> workspace.fileRules.get( 'foo', 'some_default' )
        'some_default'
    
    the workspace dir can be confusing because it works by maintaining a current working directory that is persistent
    between calls to the command.  In other words, it works much like the unix 'cd' command, or python's 'os.chdir'.
    In order to clarify this distinction, the names of these flags have been changed in their class method counterparts
    to resemble similar commands from the os module.
    
    old way (still exists for backward compatibility)
        >>> proj = workspace(query=1, dir=1)
        >>> proj  # doctest: +ELLIPSIS
        u'...'
        >>> workspace(create='mydir')
        >>> workspace(dir='mydir') # move into new dir
        >>> workspace(dir=proj) # change back to original dir
    
    new way
        >>> proj = workspace.getcwd()
        >>> proj  # doctest: +ELLIPSIS
        Path('...')
        >>> workspace.mkdir('mydir')
        >>> workspace.chdir('mydir')
        >>> workspace.chdir(proj)
    
    All paths are returned as an pymel.core.system.Path class, which makes it easy to alter or join them on the fly.
        >>> workspace.path / workspace.fileRules['mayaAscii']  # doctest: +ELLIPSIS
        Path('...')
    """

    def __call__(self, *args, **kwargs):
        """
        provides backward compatibility with cmds.workspace by allowing an instance
        of this class to be called as if it were a function
        """
        pass

    def expandName(self, path): pass

    @classmethod
    def chdir(self, newdir): pass

    @classmethod
    def getName(self): pass

    @classmethod
    def getPath(self): pass

    @classmethod
    def getcwd(self): pass

    @classmethod
    def mkdir(self, newdir): pass

    @classmethod
    def new(self, workspace): pass

    @classmethod
    def open(self, workspace): pass

    @classmethod
    def save(self): pass

    @classmethod
    def update(self): pass

    @staticmethod
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
        pass

    @property
    def name(self): pass

    @property
    def path(self): pass

    __dict__ = None

    __weakref__ = None

    fileRules = {}

    objectTypes = {}

    renderTypes = {}

    variables = {}


class Translator(object):
    """
    Provides information about a Maya translator, which is used for reading
    and/or writing file formats.
    
    >>> ascii = Translator('mayaAscii')
    >>> ascii.ext
    u'ma'
    >>> bin = Translator.fromExtension( 'mb' )
    >>> bin
    Translator(u'mayaBinary')
    >>> bin.name
    u'mayaBinary'
    >>> bin.hasReadSupport()
    True
    """

    def __init__(self, name): pass

    def __repr__(self): pass

    def __str__(self): pass

    def extension(self): pass

    def filter(self): pass

    def getDefaultOptions(self): pass

    def getFileCompression(self): pass

    def hasReadSupport(self): pass

    def hasWriteSupport(self): pass

    def optionsScript(self): pass

    def setDefaultOptions(self, options): pass

    def setFileCompression(self, compression): pass

    @staticmethod
    def fromExtension(ext, mode='None', caseSensitive='False'):
        """
        Parameters
        ----------
        ext : str
        mode : str
            {'read', 'write'}
        caseSensitive : bool
        
        Returns
        -------
        Optional[Translator]
        """
        pass

    @staticmethod
    def listRegistered(): pass

    @property
    def ext(self): pass

    @property
    def name(self): pass

    __dict__ = None

    __weakref__ = None


class FileReference(object):
    """
    A class for manipulating references which inherits Path and path.  you can create an
    instance by supplying the path to a reference file, its namespace, or its reference node to the
    appropriate keyword. The namespace and reference node of the reference can be retreived via
    the namespace and refNode properties. The namespace property can also be used to change the namespace
    of the reference.
    
    Use listReferences command to return a list of references as instances of the FileReference class.
    
    It is important to note that instances of this class will have their copy number stripped off
    and stored in an internal variable upon creation.  This is to maintain compatibility with the numerous methods
    inherited from the path class which requires a real file path. When calling built-in methods of FileReference,
    the path will automatically be suffixed with the copy number before being passed to maya commands, thus ensuring
    the proper results in maya as well.
    """

    def __eq__(self, other): pass

    def __ge__(self, other): pass

    def __gt__(self, other): pass

    def __hash__(self): pass

    def __init__(self, pathOrRefNode='None', namespace='None', refnode='None'): pass

    def __le__(self, other): pass

    def __lt__(self, other): pass

    def __melobject__(self): pass

    def __ne__(self, other): pass

    def __repr__(self): pass

    def __str__(self): pass

    def clean(self, **kwargs):
        """
        Remove edits from the passed in reference node. The reference must be in an unloaded state. To remove a particular type of edit, use the editCommand flag. If no flag is specified, all edits will be removed.                  
        
        - cleanReference : ec            (unicode)       [create]
            For use with cleanReference. Remove only this type of edit. Supported edits are:
            setAttr addAttr deleteAttr connectAttr disconnectAttr and parent
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def copyNumberList(self):
        """
        When queried, this flag returns a string array containing a number that uniquely identifies each instance the file is used.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def exportAnim(self, exportPath, **kwargs):
        """
        Export the main scene animation nodes and animation helper nodes from all referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                  
        
        - exportAnimFromReference : f    (bool)          [create]
            Force an action to take place. (new, open, save, remove reference, unload
            reference) Used with removeReference to force remove reference namespace even if
            it has contents. Cannot be used with removeReference if the reference resides in
            the root namespace. Used with unloadReference to force unload reference even if
            the reference node is locked, without prompting a dialog that warns user about
            the lost of edits.
        
        - exportAnimFromReference : rfn  (unicode)       [query]
            This flag is only used during queries. In MEL, if it appears before -query then
            it must be followed by the name of one of the scene's reference nodes. That will
            determine the reference to be queried by whatever flags appear after -query. If
            the named reference node does not exist within the scene the command will fail
            with an error. In Python the equivalent behavior is obtained by passing the name
            of the reference node as the flag's value. In MEL, if this flag appears after
            -query then it takes no argument and will cause the command to return the name
            of the reference node associated with the file given as the command's argument.
            If the file is not a reference or for some reason does not have a reference node
            (e.g., the user deleted it) then an empty string will be returned. If the file
            is not part of the current scene then the command will fail with an error. In
            Python the equivalent behavior is obtained by passing True as the flag's value.
            In query mode, this flag can accept a value.
        
        - exportAnimFromReference : typ  (unicode)       [create,query]
            Set the type of this file.  By default this can be any one of: mayaAscii,
            mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
            Illustrator(R), imageplug-ins may define their own types as well.Return a string
            array of file types that match this file.
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def exportSelectedAnim(self, exportPath, **kwargs):
        """
        Export the main scene animation nodes and animation helper nodes from the selected referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the selected nodes of a specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                  
        
        - exportSelectedAnimFromReference : f (bool)          [create]
            Force an action to take place. (new, open, save, remove reference, unload
            reference) Used with removeReference to force remove reference namespace even if
            it has contents. Cannot be used with removeReference if the reference resides in
            the root namespace. Used with unloadReference to force unload reference even if
            the reference node is locked, without prompting a dialog that warns user about
            the lost of edits.
        
        - exportSelectedAnimFromReference : rfn (unicode)       [query]
            This flag is only used during queries. In MEL, if it appears before -query then
            it must be followed by the name of one of the scene's reference nodes. That will
            determine the reference to be queried by whatever flags appear after -query. If
            the named reference node does not exist within the scene the command will fail
            with an error. In Python the equivalent behavior is obtained by passing the name
            of the reference node as the flag's value. In MEL, if this flag appears after
            -query then it takes no argument and will cause the command to return the name
            of the reference node associated with the file given as the command's argument.
            If the file is not a reference or for some reason does not have a reference node
            (e.g., the user deleted it) then an empty string will be returned. If the file
            is not part of the current scene then the command will fail with an error. In
            Python the equivalent behavior is obtained by passing True as the flag's value.
            In query mode, this flag can accept a value.
        
        - exportSelectedAnimFromReference : typ (unicode)       [create,query]
            Set the type of this file.  By default this can be any one of: mayaAscii,
            mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
            Illustrator(R), imageplug-ins may define their own types as well.Return a string
            array of file types that match this file.
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def getReferenceEdits(self, **kwargs):
        """
        Get a list of ReferenceEdit objects for this node
        
        Adapted from:
        referenceQuery -editString -onReferenceNode <self.refNode>
        
        Notes
        -----
        By default, removes all edits. If neither of successfulEdits or
        failedEdits is given, they both default to True. If only one is given,
        the other defaults to the opposite value.
        """
        pass

    def importContents(self, removeNamespace='False'):
        """
        Remove the encapsulation of the reference around the data within the specified file.    This makes the contents of the specified file part of the current scene and all references to the original file are lost. Returns the name of the reference that was imported.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def isDeferred(self):
        """
        When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is deferred.C: The default is false.Q: When queried, this flag returns true if the reference is deferred, or false if the reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def isLoaded(self):
        """
        When used in conjunction with the -reference flag, this flag determines if the reference is loaded, or if loading is deferred.C: The default is false.Q: When queried, this flag returns true if the reference is deferred, or false if the reference is not deferred. If this is used with -rfn/referenceNode, the -rfn flag must come before -q.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def isUsingNamespaces(self):
        """
        Returns boolean. Queries whether the specified reference file uses namespaces or renaming prefixes.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def load(self, newFile='None', **kwargs):
        """
        This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.If a file is not given, the command will load (or reload) the last used reference file. 
        
        - loadReference : lnr            (bool)          [create]
            This flag is obsolete and has been replaced witht the loadReferenceDepth flag.
            When used with the -open flag, no references will be loaded. When used with
            -i/import, -r/reference or -lr/loadReference flags, will load the top-most
            reference only.
        
        - loadReference : lrd            (unicode)       [create]
            Used to specify which references should be loaded. Valid types are all, noneand
            topOnly, which will load all references, no references and top-level references
            only, respectively. May only be used with the -o/open, -i/import, -r/reference
            or -lr/loadReference flags. When noneis used with -lr/loadReference, only path
            validation is performed. This can be used to replace a reference without
            triggering reload. Not using loadReferenceDepth will load references in the same
            loaded or unloaded state that they were in when the file was saved.
            Additionally, the -lr/loadReference flag supports a fourth type, asPrefs. This
            will force any nested references to be loaded according to the state (if any)
            stored in the current scene file, rather than according to the state saved in
            the reference file itself.
        
        - loadReference : rnn            (bool)          [create]
            Used to control the return value in open, import, loadReference, and reference
            operations. It will force the file command to return a list of new nodes added
            to the current scene.
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def lock(self):
        """
        Locks attributes and nodes from the referenced file.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def namespaceExists(self):
        """
        Returns true if the specified namespace exists, false if not.                  
        
        
        Derived from mel command `maya.cmds.namespace`
        """
        pass

    def nodes(self, recursive='False'):
        """
        Returns string array. A main flag used to query the contents of the target reference.                              
        
        
        Derived from mel command `maya.cmds.referenceQuery`
        """
        pass

    def parent(self):
        """
        Returns the parent FileReference object, or None
        
        Returns
        -------
        Optional[FileReference]
        """
        pass

    def remove(self, **kwargs):
        """
        Remove the given file reference from its parent. This will also Remove everything this file references. Returns the name of the file removed. If the reference is alone in its namespace, remove the namespace. If there are objects remaining in the namespace after the file reference is removed, by default, keep the remaining objects in the namespace. To merge the objects remaining in the namespace to the parent or root namespace, use flags mergeNamespaceWithParent or mergeNamespaceWithRoot. The empty file reference namespace is then removed. To forcibly delete all objects, use flag force. The empty file reference namespace is then removed.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def removeReferenceEdits(self, editCommand='None', force='False', **kwargs):
        """
        Remove edits from the reference.
        
        Parameters
        ----------
        editCommand : str
            If specified, remove only edits of a particular type: addAttr,
            setAttr, connectAttr, disconnectAttr or parent
        force : bool
            Unload the reference if it is not unloaded already
        successfulEdits : bool
            Whether to remove successful edits
        failedEdits : bool
            Whether to remove failed edits
        
        Notes
        -----
        By default, removes all edits. If neither of successfulEdits or
        failedEdits is given, they both default to True. If only one is given,
        the other defaults to the opposite value. This will only succeed on
        unapplied edits (ie, on unloaded nodes, or failed edits)... However,
        like maya.cmds.file/maya.cmds.referenceEdit, no error will be raised
        if there are no unapplied edits to work on. This may change in the
        future, however...
        """
        pass

    def replaceWith(self, newFile, **kwargs):
        """
        This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.If a file is not given, the command will load (or reload) the last used reference file. 
        
        - loadReference : lnr            (bool)          [create]
            This flag is obsolete and has been replaced witht the loadReferenceDepth flag.
            When used with the -open flag, no references will be loaded. When used with
            -i/import, -r/reference or -lr/loadReference flags, will load the top-most
            reference only.
        
        - loadReference : lrd            (unicode)       [create]
            Used to specify which references should be loaded. Valid types are all, noneand
            topOnly, which will load all references, no references and top-level references
            only, respectively. May only be used with the -o/open, -i/import, -r/reference
            or -lr/loadReference flags. When noneis used with -lr/loadReference, only path
            validation is performed. This can be used to replace a reference without
            triggering reload. Not using loadReferenceDepth will load references in the same
            loaded or unloaded state that they were in when the file was saved.
            Additionally, the -lr/loadReference flag supports a fourth type, asPrefs. This
            will force any nested references to be loaded according to the state (if any)
            stored in the current scene file, rather than according to the state saved in
            the reference file itself.
        
        - loadReference : rnn            (bool)          [create]
            Used to control the return value in open, import, loadReference, and reference
            operations. It will force the file command to return a list of new nodes added
            to the current scene.
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def selectAll(self):
        """
        Select all the components of this file as well as its child files.  Note that the file specified must be one that is already opened in this Maya session. The default behavior is to replace the existing selection. Use with the addflag to keep the active selection list.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def subReferences(self):
        """
        Returns
        -------
        Dict[unicode, FileReference]
        """
        pass

    def unload(self):
        """
        This flag will unload the reference file associated with the passed reference node.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def unlock(self):
        """
        Locks attributes and nodes from the referenced file.                  
        
        
        Derived from mel command `maya.cmds.file`
        """
        pass

    def unresolvedPath(self):
        """
        Returns
        -------
        Path
        """
        pass

    def withCopyNumber(self):
        """
        return the path with the copy number at the end
        
        Returns
        -------
        unicode
        """
        pass

    @property
    def fullNamespace(self):
        """
        Returns
        -------
        unicode
        """
        pass

    @property
    def namespace(self): pass

    @property
    def path(self):
        """
        Returns
        -------
        Path
        """
        pass

    @property
    def refNode(self): pass

    __dict__ = None

    __weakref__ = None


class UndoChunk(object):
    """
    Context manager for encapsulating code in a single undo.
    
    Use in a with statement
    Wrapper for cmds.undoInfo(openChunk=1)/cmds.undoInfo(closeChunk=1)
    
    >>> import pymel.core as pm
    >>> pm.ls("MyNode*", type='transform')
    []
    >>> with pm.UndoChunk():
    ...     res = pm.createNode('transform', name="MyNode1")
    ...     res = pm.createNode('transform', name="MyNode2")
    ...     res = pm.createNode('transform', name="MyNode3")
    >>> pm.ls("MyNode*", type='transform')
    [nt.Transform(u'MyNode1'), nt.Transform(u'MyNode2'), nt.Transform(u'MyNode3')]
    >>> pm.undo() # Due to the undo chunk, all three are undone at once
    >>> pm.ls("MyNode*", type='transform')
    []
    """

    def __enter__(self): pass

    def __exit__(*args, **kwargs): pass

    def __init__(self, name='None'): pass

    __dict__ = None

    __weakref__ = None


class _Sized(object):
    def __len__(self): pass

    @classmethod
    def __subclasshook__(cls, C): pass

    __abstractmethods__ = frozenset()

    __dict__ = None

    __weakref__ = None


class Namespace(str):
    """
    # ==============================================================================
    # Namespace
    # ==============================================================================
    """

    def __add__(self, other): pass

    def __cmp__(self, other): pass

    def __eq__(self, other): pass

    def __ge__(self, other): pass

    def __gt__(self, other): pass

    def __le__(self, other): pass

    def __lt__(self, other): pass

    def __ne__(self, other): pass

    def __repr__(self): pass

    def clean(self, haltOnError='True', reparentOtherChildren='True'):
        """
        Deletes all nodes in this namespace
        
        Parameters
        ----------
        haltOnError : bool
            If true, and reparentOtherChildren is set, and there is an error in
            reparenting, then raise an Exception (no rollback is performed);
            otherwise, ignore the failed reparent, and continue
        reparentOtherChildren : bool
            If True, then if any transforms in this namespace have children NOT
            in this namespace, then will attempt to reparent these children
            under world (errors during these reparenting attempts is controlled
            by haltOnError)
        """
        pass

    def getNode(self, nodeName, verify='True'):
        """
        Returns
        -------
        general.PyNode
        """
        pass

    def getParent(self):
        """
        Returns
        -------
        Namespace
        """
        pass

    def listNamespaces(self, recursive='False', internal='False'):
        """
        List the namespaces contained within this namespace.
        
        Parameters
        ----------
        recursive : bool
            Set to True to enable recursive search of sub (and sub-sub, etc)
            namespaces
        internal : bool
            By default, this command filters out certain automatically created
            maya namespaces (ie, :UI, :shared); set to True to show these
            internal namespaces as well
        
        Returns
        -------
        List[Namespace]
        """
        pass

    def listNodes(self, recursive='False', internal='False'):
        """
        List the nodes contained within this namespace.
        
        Parameters
        ----------
        recursive : bool
            Set to True to enable recursive search of sub (and sub-sub, etc)
            namespaces
        internal : bool
            By default, this command filters out nodes in certain automatically
            created maya namespaces (ie, :UI, :shared); set to True to show
            these internal namespaces as well
        
        Returns
        -------
        List[general.PyNode]
        """
        pass

    def ls(self, pattern="'*'", **kwargs):
        """
        Returns
        -------
        List[general.PyNode]
        """
        pass

    def move(self, other, force='False'): pass

    def remove(self, haltOnError='True', reparentOtherChildren='True'):
        """
        Removes this namespace
        
        Recursively deletes any nodes and sub-namespaces
        
        Parameters
        ----------
        haltOnError : bool
            If true, and reparentOtherChildren is set, and there is an error in
            reparenting, then raise an Exception (no rollback is performed);
            otherwise, ignore the failed reparent, and continue
        reparentOtherChildren : bool
            If True, then if any transforms in this namespace have children NOT
            in this namespace, then will attempt to reparent these children
            under world (errors during these reparenting attempts is controlled
            by haltOnError)
        """
        pass

    def setCurrent(self): pass

    def shortName(self):
        """
        Returns
        -------
        unicode
        """
        pass

    def splitAll(self):
        """
        Returns
        -------
        List[unicode]
        """
        pass

    @classmethod
    def create(cls, name):
        """
        Returns
        -------
        Namespace
        """
        pass

    @classmethod
    def getCurrent(cls):
        """
        Returns
        -------
        Namespace
        """
        pass

    @staticmethod
    def __new__(cls, namespace, create='False'): pass

    __dict__ = None

    __weakref__ = None


class _Iterable(object):
    def __iter__(self): pass

    @classmethod
    def __subclasshook__(cls, C): pass

    __abstractmethods__ = frozenset()

    __dict__ = None

    __weakref__ = None


class _Mapping(_Sized, _Iterable, _Container):
    """
    A Mapping is a generic container for associating key/value
    pairs.
    
    This class provides concrete generic implementations of all
    methods except for __getitem__, __iter__, and __len__.
    """

    def __contains__(self, key): pass

    def __eq__(self, other): pass

    def __getitem__(self, key): pass

    def __ne__(self, other): pass

    def get(self, key, default='None'):
        """
        D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
        """
        pass

    def items(self):
        """
        D.items() -> list of D's (key, value) pairs, as 2-tuples
        """
        pass

    def iteritems(self):
        """
        D.iteritems() -> an iterator over the (key, value) items of D
        """
        pass

    def iterkeys(self):
        """
        D.iterkeys() -> an iterator over the keys of D
        """
        pass

    def itervalues(self):
        """
        D.itervalues() -> an iterator over the values of D
        """
        pass

    def keys(self):
        """
        D.keys() -> list of D's keys
        """
        pass

    def values(self):
        """
        D.values() -> list of D's values
        """
        pass

    __abstractmethods__ = frozenset()

    __hash__ = None


class _MutableMapping(_Mapping):
    """
    A MutableMapping is a generic container for associating
    key/value pairs.
    
    This class provides concrete generic implementations of all
    methods except for __getitem__, __setitem__, __delitem__,
    __iter__, and __len__.
    """

    def __delitem__(self, key): pass

    def __setitem__(self, key, value): pass

    def clear(self):
        """
        D.clear() -> None.  Remove all items from D.
        """
        pass

    def pop(self, key, default="'<object object>'"):
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised.
        """
        pass

    def popitem(self):
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair
        as a 2-tuple; but raise KeyError if D is empty.
        """
        pass

    def setdefault(self, key, default='None'):
        """
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
        """
        pass

    def update(*args, **kwds):
        """
        D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
        If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
        If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
        In either case, this is followed by: for k, v in F.items(): D[k] = v
        """
        pass

    __abstractmethods__ = frozenset()


class FileInfo(_MutableMapping):
    """
    store and get custom data specific to this file:
    
        >>> from pymel.all import *
        >>> fileInfo['lastUser'] = env.user()
    
    if the python structures have valid __repr__ functions, you can
    store them and reuse them later:
    
        >>> fileInfo['cameras'] = str( ls( cameras=1) )
        >>> camList = eval(fileInfo['cameras'])
        >>> camList[0]
        nt.Camera(u'frontShape')
    
    for backward compatibility it retains it's original syntax as well:
    
        >>> fileInfo( 'myKey', 'myData' )
    
    Updated to have a fully functional dictiony interface.
    """

    def __call__(self, *args, **kwargs): pass

    def __delitem__(self, item): pass

    def __getitem__(self, item): pass

    def __iter__(self): pass

    def __len__(self): pass

    def __setitem__(self, item, value): pass

    def has_key(self, key): pass

    def items(self): pass

    def keys(self): pass

    @staticmethod
    def __new__(cls, *p, **k):
        """
        # redefine __new__
        """
        pass

    __abstractmethods__ = frozenset()


def isModified(): pass


def _safePyNode(n): pass


def displayWarning(*args, **kwargs): pass


def exportAll(exportPath, **kwargs):
    """
    Export everything into a single file. Returns the name of the exported file.                  
    
    - exportAll : f                  (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - exportAll : pr                 (bool)          [create]
        Modifies the various import/export flags such that references are
        imported/exported as actual references rather than copies of those references.
    
    - exportAll : typ                (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def createReference(filepath, **kwargs):
    """
    Create a reference to the specified file. Returns the name of the file referenced.Query all file references from the specified file.                  
    
    - reference : lnr                (bool)          [create]
        This flag is obsolete and has been replaced witht the loadReferenceDepth flag.
        When used with the -open flag, no references will be loaded. When used with
        -i/import, -r/reference or -lr/loadReference flags, will load the top-most
        reference only.
    
    - reference : lrd                (unicode)       [create]
        Used to specify which references should be loaded. Valid types are all, noneand
        topOnly, which will load all references, no references and top-level references
        only, respectively. May only be used with the -o/open, -i/import, -r/reference
        or -lr/loadReference flags. When noneis used with -lr/loadReference, only path
        validation is performed. This can be used to replace a reference without
        triggering reload. Not using loadReferenceDepth will load references in the same
        loaded or unloaded state that they were in when the file was saved.
        Additionally, the -lr/loadReference flag supports a fourth type, asPrefs. This
        will force any nested references to be loaded according to the state (if any)
        stored in the current scene file, rather than according to the state saved in
        the reference file itself.
    
    - reference : dns                (bool)          [create]
        Use the default name space for import and referencing.  This is an advanced
        option.  If set, then on import or reference, Maya will attempt to place all
        nodes from the imported or referenced file directly into the root (default) name
        space, without invoking any name clash resolution algorithms.  If the names of
        any of the new objects    already exist in the root namespace, then errors will
        result. The user of this flag is responsible for creating a name clash
        resolution mechanism outside of Maya to avoid such errors. Note:This flag    is
        intended only for use with custom file translators written through    the API.
        Use at your own risk.
    
    - reference : dr                 (bool)          [create,query]
        When used in conjunction with the -reference flag, this flag determines if the
        reference is loaded, or if loading is deferred.C: The default is false.Q: When
        queried, this flag returns true if the reference is deferred, or false if the
        reference is not deferred. If this is used with -rfn/referenceNode, the -rfn
        flag must come before -q.
    
    - reference : gr                 (bool)          [create]
        Used only with the -r or the -i flag. Used to group all the imported/referenced
        items under a single transform.
    
    - reference : gl                 (bool)          [create]
        Used only with the -r and the -gr flag. Used to group the output of
        groupReference under a locator
    
    - reference : gn                 (unicode)       [create]
        Used only with the -gr flag. Optionally used to set the name of the transform
        node that the imported/referenced items will be grouped under.
    
    - reference : ns                 (unicode)       [edit]
        The namespace name to use that will group all objects during importing and
        referencing. Change the namespace used to group all the objects from the
        specified referenced file. The reference must have been created with the Using
        Namespacesoption, and must be loaded. Non-referenced nodes contained in the
        existing namespace will also be moved to the new namespace. The new namespace
        will be created by this command and can not already exist. The old namespace
        will be removed.
    
    - reference : rfn                (unicode)       [query]
        This flag is only used during queries. In MEL, if it appears before -query then
        it must be followed by the name of one of the scene's reference nodes. That will
        determine the reference to be queried by whatever flags appear after -query. If
        the named reference node does not exist within the scene the command will fail
        with an error. In Python the equivalent behavior is obtained by passing the name
        of the reference node as the flag's value. In MEL, if this flag appears after
        -query then it takes no argument and will cause the command to return the name
        of the reference node associated with the file given as the command's argument.
        If the file is not a reference or for some reason does not have a reference node
        (e.g., the user deleted it) then an empty string will be returned. If the file
        is not part of the current scene then the command will fail with an error. In
        Python the equivalent behavior is obtained by passing True as the flag's value.
        In query mode, this flag can accept a value.
    
    - reference : rpr                (unicode)       [create,query]
        The string to use as a prefix for all objects from this file. This flag has been
        replaced by -ns/namespace.
    
    - reference : sns                (unicode, unicode) [create]
        Can only be used in conjunction with the -r/reference or -i/import flags. This
        flag will replace any occurrences of a given namespace to an alternate specified
        namespace. This namespace swapwill occur as the file is referenced in. It takes
        in two string arguments. The first argument specifies the namespace to replace.
        The second argument specifies the replacement namespace. Use of this flag,
        implicitly enables the use of namespaces and cannot be used with deferReference.
    
    - reference : srf                (bool)          [create]
        Can only be used in conjunction with the -r/reference flag and the -ns/namespace
        flag (there is no prefix support). This flag modifies the '-r/reference' flag to
        indicate that all nodes within that reference should be treated as shared nodes.
        New copies    of those nodes will not be created if a copy already exists.
        Instead, the shared node will be merged with the existing node. The specifics of
        what happens when two nodes are merged depends on the node type. This flag
        cannot be used in conjunction with -shd/sharedNodes.
    
    - reference : shd                (unicode)       [create]
        This flag modifies the '-r/reference' flag to indicate that certain    types of
        nodes within that reference should be treated as shared nodes. All shared nodes
        will be placed in the default namespace. New copies of those nodes will not be
        created if a copy already exists in the default namespace, instead the shared
        node will be merged with the    existing node. The specifics of what happens
        when two nodes are merged depends on the node type. In general attribute values
        will not be merged, meaning the values set on any existing shared nodes will be
        retained, and the values of the nodes being merged in will be ignored. The valid
        options are displayLayers, shadingNetworks, renderLayersByName, and
        renderLayersById. This flag is multi-use; it may be specified multiple times to
        for example, share both display layers and shading networks. Two shading
        networks will only be merged if    they are identical: the network    of nodes
        feeding into the shading group must be arranged identically with equivalent
        nodes have the same name and node type. Additionally if a network is animated or
        contains a DAG object or expression it will not be mergeable. This flag cannot
        be used in conjunction with -srf/sharedReferenceFile.
    
    - reference : rnn                (bool)          [create]
        Used to control the return value in open, import, loadReference, and reference
        operations. It will force the file command to return a list of new nodes added
        to the current scene.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def openFile(*args, **kwargs):
    """
    Open the specified file. Returns the name of the opened file.                  
    
    - open : lad                     (bool)          [create]
        This flag is obsolete, and has been replaced by the loadReferenceDepth flag.
        When used with the -open flag, determines if the -deferReference flag is
        respected when reading in the file. If true is passed, all of the references are
        loaded. If false is passed, the -deferReference flag is respected.
    
    - open : lnr                     (bool)          [create]
        This flag is obsolete and has been replaced witht the loadReferenceDepth flag.
        When used with the -open flag, no references will be loaded. When used with
        -i/import, -r/reference or -lr/loadReference flags, will load the top-most
        reference only.
    
    - open : lrd                     (unicode)       [create]
        Used to specify which references should be loaded. Valid types are all, noneand
        topOnly, which will load all references, no references and top-level references
        only, respectively. May only be used with the -o/open, -i/import, -r/reference
        or -lr/loadReference flags. When noneis used with -lr/loadReference, only path
        validation is performed. This can be used to replace a reference without
        triggering reload. Not using loadReferenceDepth will load references in the same
        loaded or unloaded state that they were in when the file was saved.
        Additionally, the -lr/loadReference flag supports a fourth type, asPrefs. This
        will force any nested references to be loaded according to the state (if any)
        stored in the current scene file, rather than according to the state saved in
        the reference file itself.
    
    - open : f                       (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - open : rnn                     (bool)          [create]
        Used to control the return value in open, import, loadReference, and reference
        operations. It will force the file command to return a list of new nodes added
        to the current scene.
    
    - open : typ                     (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def listNamespaces(root='None', recursive='False', internal='False'):
    """
    Returns a list of the namespaces in the scene
    
    Returns
    -------
    List[Namespace]
    """
    pass


def pluginInfo(*args, **kwargs):
    """
    This command provides access to the plug-in registry of the application. It is
    used mainly to query the characteristics of registered plug-ins. Plugins
    automatically become registered the first time that they are loaded. The
    argument is either the internal name of the plug-in or the path to access it.
    
    Flags:
    - activeFile : af                (bool)          [query]
        Restricts the command to the active file only, not the entire scene. This only
        affects the dependNode/dnand pluginsInUse/puflags. For use during export
        selected.
    
    - animCurveInterp : aci          (unicode)       [query]
        Returns a string array containing the names of all of the animation curve
        interpolators registered by this plug-in.
    
    - apiVersion : av                (bool)          [query]
        Returns a string containing the version of the API that this plug-in was
        compiled with.  See the comments in MTypes.h for the details on how to interpret
        this value.
    
    - autoload : a                   (bool)          [create,query,edit]
        Sets whether or not this plug-in should be loaded every time the application
        starts up. Returns a boolean in query mode.
    
    - cacheFormat : cf               (bool)          [query]
        Returns a string array containing the names of all of the registered geometry
        cache formats
    
    - changedCommand : cc            (script)        [create]
        Adds a callback that will get executed every time the plug-in registry changes.
        Any other previously registered callbacks will also get called.
    
    - command : c                    (unicode)       [query]
        Returns a string array containing the names of all of the normal commands
        registered by this plug-in. Constraint, control, context and model editor
        commands are not included.
    
    - constraintCommand : cnc        (bool)          [query]
        Returns a string array containing the names of all of the constraint commands
        registered by this plug-in.
    
    - controlCommand : ctc           (bool)          [query]
        Returns a string array containing the names of all of the control commands
        registered by this plug-in.
    
    - data : d                       (unicode, unicode) [query]
        Returns a string array containing the names of all of the data types registered
        by this plug-in.
    
    - dependNode : dn                (bool)          [query]
        Returns a string array containing the names of all of the custom nodes types
        registered by this plug-in.
    
    - dependNodeByType : dnt         (unicode)       [query]
        Returns a string array of all registered node types within a specified class of
        nodes.  Each custom node type registered by a plug-in belongs to a more general
        class of node types as specified by its MPxNode::Type. The flag's argument is an
        MPxNode::Type as a string.  For example, if you want to list all registered
        Locator nodes, you should specify kLocatorNode as a argument to this flag.
    
    - dependNodeId : dni             (unicode)       [query]
        Returns an integer array containing the ids of all of the custom node types
        registered by this plug-in.
    
    - device : dv                    (bool)          [query]
        Returns a string array containing the names of all of the devices registered by
        this plug-in.
    
    - dragAndDropBehavior : ddb      (bool)          [query]
        Returns a string array containing the names of all of the drag and drop
        behaviors registered by this plug-in.
    
    - iksolver : ik                  (bool)          [query]
        Returns a string array containing the names of all of the ik solvers registered
        by this plug-in.
    
    - listPlugins : ls               (bool)          [query]
        Returns a string array containing all the plug-ins that are currently loaded.
    
    - listPluginsPath : lsp          (bool)          [query]
        Returns a string array containing the full paths of all the plug-ins that are
        currently loaded.
    
    - loadPluginPrefs : lpp          (bool)          [create]
        Loads the plug-in preferences (ie. autoload) from pluginPrefs.mel into Maya.
    
    - loaded : l                     (bool)          [query]
        Returns a boolean specifying whether or not the plug-in is loaded.
    
    - modelEditorCommand : mec       (bool)          [query]
        Returns a string array containing the names of all of the model editor commands
        registered by this plug-in.
    
    - name : n                       (unicode)       [query]
        Returns a string containing the internal name by which the plug-in is
        registered.
    
    - path : p                       (unicode)       [query]
        Returns a string containing the absolute path name to the plug-in.
    
    - pluginsInUse : pu              (bool)          [query]
        Returns a string array containing all the plug-ins that are currently being used
        in the scene.
    
    - referenceTranslators : rtr     (bool)          [query]
        If this flag is used in conjunction with the pluginsInUse/puflag then it will
        modify the output. When true it will only show plug-ins currently in use
        containing translators that are used to load referenced files. When false it
        will only show plug-ins not containing such translators.
    
    - registered : r                 (bool)          [query]
        Returns a boolean specifying whether or not plug-in is currently registered with
        the system.
    
    - remove : rm                    (bool)          [edit]
        Removes the given plug-in's record from the registry. There is no return value.
    
    - renderer : rdr                 (bool)          [query]
        Returns a string array containing the names of all of the renderers registered
        by this plug-in.
    
    - savePluginPrefs : spp          (bool)          [create]
        Saves the plug-in preferences (ie. autoload) out to pluginPrefs.mel
    
    - serviceDescriptions : sd       (bool)          [query]
        If there are services in use, then this flag will return a string array
        containing short descriptions saying what those services are.
    
    - settings : set                 (bool)          [query]
        Returns an array of values with the loaded, autoload, registered flags
    
    - tool : t                       (unicode)       [query]
        Returns a string array containing the names of all of the tool contexts
        registered by this plug-in.
    
    - translator : tr                (bool)          [query]
        Returns a string array containing the names of all of the file translators
        registered by this plug-in.
    
    - unloadOk : uo                  (bool)          [query]
        Returns a boolean that specifies whether or not the plug-in can be safely
        unloaded.  It will return false if the plug-in is currently in use.  For
        example, if the plug-in adds a new dependency node type, and an instance of that
        node type is present in the scene, then this query will return false.
    
    - userNamed : u                  (bool)          [query]
        Returns a boolean specifying whether or not the plug-in has been assigned a name
        by the user.
    
    - vendor : vd                    (unicode)       [query]
        Returns a string containing the vendor of the plug-in.
    
    - version : v                    (bool)          [query]
        Returns a string containing the version the plug-in.
    
    - writeRequires : wr             (bool)          [create,query,edit]
        Sets whether or not this plug-in should write requirescommand into the saved
        file. requirescommand could autoload the plug-in when you open or import that
        saved file. This way, Maya will load the plug-in when a file is being loaded for
        some specified reason, such as to create a customized UI or to load some plug-in
        data that is not saved in any node or attributes. For example, stereoCamerais
        using this flag for its customized UI.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.pluginInfo`
    """
    pass


def displayError(*args, **kwargs): pass


def newFile(*args, **kwargs):
    """
    Initialize the scene. Returns untitled scene with default location.                  
    
    - newFile : f                    (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - newFile : typ                  (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def _referenceQuery(*args, **kwargs):
    """
    Modifications:
    - When queried for 'es/editStrings', returned a list of ReferenceEdit objects
    - By default, returns all edits. If neither of successfulEdits or
      failedEdits is given, they both default to True. If only one is given,
      the other defaults to the opposite value.
    """
    pass


def iterReferences(parentReference='None', recursive='False', namespaces='False', refNodes='False', references='True',
                   recurseType="'depth'", loaded='None', unloaded='None'):
    """
    returns references in the scene as a list of value tuples.
    
    The values in the tuples can be namespaces, refNodes (as PyNodes), and/or
    references (as FileReferences), and are controlled by their respective
    keywords (and are returned in that order).  If only one of the three options
    is True, the result will not be a list of value tuples, but will simply be a
    list of values.
    
    Parameters
    ----------
    parentReference : Union[str, Path, FileReference]
        a reference to get sub-references from. If None (default), the current
        scene is used.
    recursive : bool
        recursively determine all references and sub-references
    namespaces : bool
        controls whether namespaces are returned
    refNodes : bool
        controls whether reference PyNodes are returned
    references : bool
        controls whether FileReferences returned
    recurseType : str
        if recursing, whether to do a 'breadth' or 'depth' first search;
        defaults to a 'depth' first
    loaded : Optional[bool]
        whether to return loaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    unloaded : Optional[bool]
        whether to return unloaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    
    Returns
    -------
    Iterator[Union[FileReference, Tuple[unicode, FileReference], Tuple[unicode, FileReference, nt.Reference]]]
    """
    pass


def untitledFileName():
    """
    Obtain the base filename used for untitled scenes. In localized environments, this string will contain a translated value.
    """
    pass


def getReferences(parentReference='None', recursive='False'):
    """
    Returns
    -------
    Dict[unicode, FileReference]
    """
    pass


def exportAnimFromReference(exportPath, **kwargs):
    """
    Export the main scene animation nodes and animation helper nodes from all referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                  
    
    - exportAnimFromReference : f    (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - exportAnimFromReference : rfn  (unicode)       [query]
        This flag is only used during queries. In MEL, if it appears before -query then
        it must be followed by the name of one of the scene's reference nodes. That will
        determine the reference to be queried by whatever flags appear after -query. If
        the named reference node does not exist within the scene the command will fail
        with an error. In Python the equivalent behavior is obtained by passing the name
        of the reference node as the flag's value. In MEL, if this flag appears after
        -query then it takes no argument and will cause the command to return the name
        of the reference node associated with the file given as the command's argument.
        If the file is not a reference or for some reason does not have a reference node
        (e.g., the user deleted it) then an empty string will be returned. If the file
        is not part of the current scene then the command will fail with an error. In
        Python the equivalent behavior is obtained by passing True as the flag's value.
        In query mode, this flag can accept a value.
    
    - exportAnimFromReference : typ  (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def loadReference(filepath, **kwargs):
    """
    This flag loads a file and associates it with the passed reference node. If the reference node does not exist, the command will fail. If the file is already loaded, then this flag will reload the same file.If a file is not given, the command will load (or reload) the last used reference file. 
    
    - loadReference : lnr            (bool)          [create]
        This flag is obsolete and has been replaced witht the loadReferenceDepth flag.
        When used with the -open flag, no references will be loaded. When used with
        -i/import, -r/reference or -lr/loadReference flags, will load the top-most
        reference only.
    
    - loadReference : lrd            (unicode)       [create]
        Used to specify which references should be loaded. Valid types are all, noneand
        topOnly, which will load all references, no references and top-level references
        only, respectively. May only be used with the -o/open, -i/import, -r/reference
        or -lr/loadReference flags. When noneis used with -lr/loadReference, only path
        validation is performed. This can be used to replace a reference without
        triggering reload. Not using loadReferenceDepth will load references in the same
        loaded or unloaded state that they were in when the file was saved.
        Additionally, the -lr/loadReference flag supports a fourth type, asPrefs. This
        will force any nested references to be loaded according to the state (if any)
        stored in the current scene file, rather than according to the state saved in
        the reference file itself.
    
    - loadReference : rnn            (bool)          [create]
        Used to control the return value in open, import, loadReference, and reference
        operations. It will force the file command to return a list of new nodes added
        to the current scene.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def referenceQuery(*args, **kwargs):
    """
    Use this command to find out information about references and referenced nodes.
    A valid target is either a reference node, a reference file, or a referenced
    node. Some flags don't require a target, see flag descriptions for more
    information on what effect this has. When a scene contains multiple levels of
    file references, those edits which affect a nested reference may be stored on
    several different reference nodes. For example: A.ma has a reference to B.ma
    which has a reference to C.ma which contains a poly sphere (pSphere1). If you
    were to open B.ma and translate the sphere, an edit would be stored on CRN which
    refers to a node named C:pSphere1. If you were then to open A.ma and parent the
    sphere, an edit would be stored on BRN which refers to a node named
    B:C:pSphere1. It is important to note that when querying edits which affect a
    nested reference, the edits will be returned in the same format that they were
    applied. In the above example, opening A.ma and querying all edits which affect
    C.ma, would return two edits a parent edit affecting B:C:pSphere1, and a setAttr
    edit affecting C:pSphere1. Since there is currently no node named C:pSphere1
    (only B:C:pSphere1) care will have to be taken when interpreting the returned
    information. The same care should be taken when referenced DAG nodes have been
    parented or instanced. Continuing with the previous example, let's say that you
    were to open A.ma and, instead of simply parenting pSphere1, you were to
    instance it. While A.ma is open, B:C:pSphere1may now be an amibiguous name,
    replaced by |B:C:pSphere1and group1|B:C:pSphere1. However querying the edits
    which affect C.ma would still return a setAttr edit affecting C:pSphere1since it
    was applied prior to B:C:pSphere1 being instanced. Some tips: 1. Use the
    '-topReference' flag to query only those edits which were applied    from the
    currently open file. 2. Use the '-onReferenceNode' flag to limit the results to
    those edits where    are stored on a given reference node. You can then use
    various string    manipulation techniques to extrapolate the current name of any
    affected    nodes.
    
    Flags:
    - child : ch                     (bool)          [create]
        This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to
        indicate the the children of the target reference will be returned. Returns a
        string array.
    
    - dagPath : dp                   (bool)          [create]
        This flag modifies the '-n/-nodes' flag to indicate that the names of any dag
        objects returned will include as much of the dag path as is necessary to make
        the names unique. If this flag is not present, the names returned will not
        include any dag paths.
    
    - editAttrs : ea                 (bool)          [create]
        Returns string array. A main flag used to query the edits that have been applied
        to the target. Only the names of the attributes involved in the reference edit
        will be returned. If an edit involves multiple attributes (e.g.
        connectAttredits) the nodes will be returned as separate, consecutive entries in
        the string array. A valid target is either a reference node, a reference file,
        or a referenced node. If a referenced node is specified, only those edits which
        affect that node will be returned. If a reference file or reference node is
        specified any edit which affects a node in that reference will be returned. If
        no target is specified all edits are returned. This command can be used on both
        loaded and unloaded references. By default it will return all the edits,
        formatted as MEL commands, which apply to the target. This flag can be used in
        combination with the '-ea/-editAttrs' flag to indicate that the names of both
        the involved nodes and attributes will be returned in the format
        'node.attribute'.
    
    - editCommand : ec               (unicode)       [create,query]
        This is a secondary flag used to indicate which type of reference edits should
        be considered by the command. If this flag is not specified all edit types will
        be included. This flag requires a string parameter. Valid values are: addAttr,
        connectAttr, deleteAttr, disconnectAttr, parent, setAttr, lockand unlock. In
        some contexts, this flag may be specified more than once to specify multiple
        edit types to consider.
    
    - editNodes : en                 (bool)          [create]
        Returns string array. A main flag used to query the edits that have been applied
        to the target. Only the names of the nodes involved in the reference edit will
        be returned. If an edit involves multiple nodes (e.g. connectAttredits) the
        nodes will be returned as separate, consecutive entries in the string array. A
        valid target is either a reference node, a reference file, or a referenced node.
        If a referenced node is specified, only those edits which affect that node will
        be returned. If a reference file or reference node is specified any edit which
        affects a node in that reference will be returned. If no target is specified all
        edits are returned. This command can be used on both loaded and unloaded
        references. By default it will return all the edits, formatted as MEL commands,
        which apply to the target. This flag can be used in combination with the
        '-ea/-editAttrs' flag to indicate that the names of both the involved nodes and
        attributes will be returned in the format 'node.attribute'.
    
    - editStrings : es               (bool)          [create]
        Returns string array. A main flag used to query the edits that have been applied
        to the target. The edit will be returned as a valid MEL command. A valid target
        is either a reference node, a reference file, or a referenced node. If a
        referenced node is specified, only those edits which affect that node will be
        returned. If a reference file or reference node is specified any edit which
        affects a node in that reference will be returned. If no target is specified all
        edits are returned. This command can be used on both loaded and unloaded
        references. By default it will return all the edits, formatted as MEL commands,
        which apply to the target. This flag cannot be used with either the
        '-en/-editNodes' or '-ea/-editAttrs' flags.
    
    - failedEdits : fld              (bool)          [create]
        This is a secondary flag used to indicate whether or not failed edits should be
        acted on (e.g. queried, removed, etc...). A failed edit is an edit which could
        not be successfully applied the last time its reference was loaded. An edit can
        fail for a variety of reasons (e.g. the referenced node to which it applies was
        removed from the referenced file). By default failed edits will not be acted on.
    
    - filename : f                   (bool)          [create]
        Returns string. A main flag used to query the filename associated with the
        target reference.
    
    - isExportEdits : iee            (bool)          [create]
        Returns a boolean indicating whether the specified reference node or file name
        is an edits file (created with the Export Edits feature)
    
    - isLoaded : il                  (bool)          [create]
        Returns a boolean indicating whether the specified reference node or file name
        refers to a loaded or unloaded reference.
    
    - isNodeReferenced : inr         (bool)          [create]
        Returns boolean. A main flag used to determine whether or not the target node
        comes from a referenced file. true if the target node comes from a referenced
        file, false if not.
    
    - isPreviewOnly : ipo            (bool)          [create]
        Returns boolean. This flag is used to determine whether or not the target
        reference node is only a preview reference node.
    
    - liveEdits : le                 (bool)          [create]
        Specifies that the edits should be returned based on the live edits database.
        Only valid when used in conjunction with the editStrings flag.
    
    - namespace : ns                 (bool)          [create]
        Returns string. This flag returns the full namespace path of the target
        reference, starting from the root namespace :. It can be combined with the
        shortName flag to return just the base name of the namespace.
    
    - nodes : n                      (bool)          [create]
        Returns string array. A main flag used to query the contents of the target
        reference.
    
    - onReferenceNode : orn          (unicode)       [create,query]
        This is a secondary flag used to indicate that only those edits which are stored
        on the indicated reference node should be considered. This flag only supports
        multiple uses when specified with the exportEditscommand.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - parent : p                     (bool)          [create]
        This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags to
        indicate the the parent of the target reference will be returned.
    
    - parentNamespace : pns          (bool)          [create]
        A main flag used to query and return the parent namespace of the target
        reference.
    
    - referenceNode : rfn            (bool)          [create]
        Returns string. A main flag used to query the reference node associated with the
        target reference.
    
    - shortName : shn                (bool)          [create]
        This flag modifies the '-f/-filename' and '-ns/-namespace' flags. Used with the
        '-f/-filename' flag indicates that the file name returned will be the short name
        (i.e. just a file name without any directory paths). If this flag is not
        present, the full name and directory path will be returned. Used with the
        '-ns/-namespace' flag indicates that the namespace returned will be the base
        name of the namespace. (i.e. the base name of the full namespace path
        :AAA:BBB:CCCis CCC
    
    - showDagPath : sdp              (bool)          [create]
        Shows/hides the full dag path for edits. If false only displays the node-name of
        reference edits. Must be used with the -editNodes, -editStrings or -editAttrs
        flag.
    
    - showNamespace : sns            (bool)          [create]
        Shows/hides the namespaces on nodes in the reference edits. Must be used with
        the -editNodes, -editStrings or -editAttrs flag
    
    - successfulEdits : scs          (bool)          [create]
        This is a secondary flag used to indicate whether or not successful edits should
        be acted on (e.g. queried, removed, etc...). A successful edit is any edit which
        was successfully applied the last time its reference was loaded. By default
        successful edits will be acted on.
    
    - topReference : tr              (bool)          [create]
        This flag modifies the '-rfn/-referenceNode' flag to indicate the top level
        ancestral reference of the target reference will be returned.
    
    - unresolvedName : un            (bool)          [create]
        This flag modifies the '-f/-filename' flag to indicate that the file name
        returned will be unresolved (i.e. it will be the path originally specified when
        the file was loaded into Maya; this path may contain environment variables and
        may not exist on disk). If this flag is not present, the resolved name will
        be returned.
    
    - withoutCopyNumber : wcn        (bool)          [create]
        This flag modifies the '-f/-filename' flag to indicate that the file name
        returned will not have a copy number (e.g. '{1}') appended to the end. If this
        flag is not present, the file name returned may have a copy number appended to
        the end.
    
    
    Derived from mel command `maya.cmds.referenceQuery`
    """
    pass


def feof(fileid):
    """
    Reproduces the behavior of the mel command of the same name. if writing pymel scripts from scratch,
    you should use a more pythonic construct for looping through files:
    
    >>> f = open('myfile.txt') # doctest: +SKIP
    ... for line in f:
    ...     print line
    
    This command is provided for python scripts generated by mel2py
    """
    pass


def saveImage(*args, **kwargs):
    """
    This command creates a static image for non-xpm files. Any image file format
    supported by the file texture node is supported by this command. This command
    creates a static image control for non-xpm files used to display a thumbnail
    image of the scene file.
    
    Flags:
    - annotation : ann               (unicode)       [create,query,edit]
        Annotate the control with an extra string value.
    
    - backgroundColor : bgc          (float, float, float) [create,query,edit]
        The background color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0. When
        setting backgroundColor, the background is automatically enabled, unless
        enableBackground is also specified with a false value.
    
    - currentView : cv               (bool)          [edit]
        Generate the image from the current view.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Add a documentation flag to the control.  The documentation flag has a directory
        structure. (e.g., -dt render/multiLister/createNode/material)
    
    - dragCallback : dgc             (script)        [create,edit]
        Adds a callback that is called when the middle mouse button is pressed.  The MEL
        version of the callback is of the form: global proc string[] callbackName(string
        $dragControl, int $x, int $y, int $mods) The proc returns a string array that is
        transferred to the drop site. By convention the first string in the array
        describes the user settable message type.  Controls that are application defined
        drag sources may ignore the callback. $mods allows testing for the key modifiers
        CTRL and SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL, 3
        == CTRL + SHIFT. In Python, it is similar, but there are two ways to specify the
        callback.  The recommended way is to pass a Python function object as the
        argument.  In that case, the Python callback should have the form: def
        callbackName( dragControl, x, y, modifiers ): The values of these arguments are
        the same as those for the MEL version above. The other way to specify the
        callback in Python is to specify a string to be executed.  In that case, the
        string will have the values substituted into it via the standard Python format
        operator.  The format values are passed in a dictionary with the keys
        dragControl, x, y, modifiers.  The dragControlvalue is a string and the other
        values are integers (eg the callback string could be print '%(dragControl)s
        %(x)d %(y)d %(modifiers)d'
    
    - dropCallback : dpc             (script)        [create,edit]
        Adds a callback that is called when a drag and drop operation is released above
        the drop site.  The MEL version of the callback is of the form: global proc
        callbackName(string $dragControl, string $dropControl, string $msgs[], int $x,
        int $y, int $type) The proc receives a string array that is transferred from the
        drag source. The first string in the msgs array describes the user defined
        message type. Controls that are application defined drop sites may ignore the
        callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link. In Python,
        it is similar, but there are two ways to specify the callback.  The recommended
        way is to pass a Python function object as the argument.  In that case, the
        Python callback should have the form: def pythonDropTest( dragControl,
        dropControl, messages, x, y, dragType ): The values of these arguments are the
        same as those for the MEL version above. The other way to specify the callback
        in Python is to specify a string to be executed.  In that case, the string will
        have the values substituted into it via the standard Python format operator.
        The format values are passed in a dictionary with the keys dragControl,
        dropControl, messages, x, y, type.  The dragControlvalue is a string and the
        other values are integers (eg the callback string could be print
        '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'
    
    - enable : en                    (bool)          [create,query,edit]
        The enable state of the control.  By default, this flag is set to true and the
        control is enabled.  Specify false and the control will appear dimmed or greyed-
        out indicating it is disabled.
    
    - enableBackground : ebg         (bool)          [create,query,edit]
        Enables the background color of the control.
    
    - enableKeyboardFocus : ekf      (bool)          [create,query,edit]
        If enabled, the user can navigate to the control with the tab key and select
        values with the keyboard. If not, the user can only use the mouse. This flag
        would typically be used to turn off keyboard focus support from controls that
        get it by default, like Edit and List controls
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - fullPathName : fpn             (bool)          [query]
        Return the full path name of the widget, which includes all the parents.
    
    - height : h                     (int)           [create,query,edit]
        The height of the control.  The control will attempt to be this size if it is
        not overruled by parent layout conditions.
    
    - highlightColor : hlc           (float, float, float) [create,query,edit]
        The highlight color of the control. The arguments correspond to the red, green,
        and blue color components. Each component ranges in value from 0.0 to 1.0.
    
    - image : i                      (unicode)       [create,query,edit]
        Sets the image given the file name.
    
    - isObscured : io                (bool)          [query]
        Return whether the control can actually be seen by the user. The control will be
        obscured if its state is invisible, if it is blocked (entirely or partially) by
        some other control, if it or a parent layout is unmanaged, or if the control's
        window is invisible or iconified.
    
    - manage : m                     (bool)          [create,query,edit]
        Manage state of the control.  An unmanaged control is not visible, nor does it
        take up any screen real estate.  All controls are created managed by default.
    
    - noBackground : nbg             (bool)          [create,edit]
        Clear/reset the control's background. Passing true means the background should
        not be drawn at all, false means the background should be drawn.  The state of
        this flag is inherited by children of this control.
    
    - numberOfPopupMenus : npm       (bool)          [query]
        Return the number of popup menus attached to this control.
    
    - objectThumbnail : ot           (unicode)       [edit]
        Use an image of the named object, if possible.
    
    - parent : p                     (unicode)       [create,query]
        The parent layout for this control.
    
    - popupMenuArray : pma           (bool)          [query]
        Return the names of all the popup menus attached to this control.
    
    - preventOverride : po           (bool)          [create,query,edit]
        If true, this flag prevents overriding the control's attribute via the control's
        right mouse button menu.
    
    - sceneFile : sf                 (unicode)       [edit]
        The name of the file that the icon is to be associated with.
    
    - statusBarMessage : sbm         (unicode)       [create,edit]
        Extra string to display in the status bar when the mouse is over the control.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - visible : vis                  (bool)          [create,query,edit]
        The visible state of the control.  A control is created visible by default.
        Note that a control's actual appearance is also dependent on the visible state
        of its parent layout(s).
    
    - visibleChangeCommand : vcc     (script)        [create,query,edit]
        Command that gets executed when visible state of the control changes.
    
    - width : w                      (int)           [create,query,edit]
        The width of the control.  The control will attempt to be this size if it is not
        overruled by parent layout conditions.                  Flag can have multiple
        arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.saveImage`
    """
    pass


def fileDialog2(*args, **kwargs):
    """
    This command provides a dialog that allows users to select files or directories.
    
    Flags:
    - buttonBoxOrientation : bbo     (int)           [create]
        1 Vertical button box layout. Cancel button is below the accept button. 2
        Horizontal button box layout. Cancel button is to the right of the accept
        button.
    
    - cancelCaption : cc             (unicode)       [create]
        If the dialogStyle flag is set to 2 then this provides a caption for the Cancel
        button within the dialog.
    
    - caption : cap                  (unicode)       [create]
        Provide a title for the dialog.
    
    - dialogStyle : ds               (int)           [create]
        1 On Windows or Mac OS X will use a native style file dialog.2 Use a custom file
        dialog with a style that is consistent across platforms.
    
    - fileFilter : ff                (unicode)       [create]
        Provide a list of file type filters to the dialog.  Multiple filters should be
        separated by double semi-colons.  See the examples section.
    
    - fileMode : fm                  (int)           [create]
        Indicate what the dialog is to return. 0 Any file, whether it exists or not.1 A
        single existing file.2 The name of a directory.  Both directories and files are
        displayed in the dialog.3 The name of a directory.  Only directories are
        displayed in the dialog.4 Then names of one or more existing files.
    
    - fileTypeChanged : ftc          (script)        [create]
        MEL only.  The string is interpreted as a MEL callback, to be called when the
        user-selected file type changes.  The callback is of the form: global proc
        MyCustomFileTypeChanged(string $parent, string $newType) The parent argument is
        the parent layout into which controls have been added using the optionsUICreate
        flag.  The newType argument is the new file type.
    
    - hideFileExtensions : hfe       (bool)          []
    
    - hideNameEdit : hne             (bool)          [create]
        Hide name editing input field.
    
    - okCaption : okc                (unicode)       [create]
        If the dialogStyle flag is set to 2 then this provides a caption for the OK, or
        Accept, button within the dialog.
    
    - optionsUICancel : oca          (script)        [create]
        MEL only.  The string is interpreted as a MEL callback, to be called when the
        dialog is cancelled (with Cancel button or close button to close window). The
        callback is of the form: global proc MyCustomOptionsUICancel()
    
    - optionsUICommit : ocm          (script)        [create]
        MEL only.  The string is interpreted as a MEL callback, to be called when the
        dialog is successfully dismissed.  It will not be called if the user cancels the
        dialog, or closes the window using window title bar controls or other window
        system means.  The callback is of the form: global proc
        MyCustomOptionsUICommit(string $parent) The parent argument is the parent layout
        into which controls have been added using the optionsUICreate flag.
    
    - optionsUICommit2 : oc2         (script)        [create]
        MEL only.  As optionsUICommit, the given string is interpreted as a MEL
        callback, to be called when the dialog is successfully dismissed. The difference
        is that this callback takes one additional argument which is the file name
        selected by the user before the dialog validation. It will not be called if the
        user cancels the dialog, or closes the window using window title bar controls or
        other window system means.  The callback is of the form: global proc
        MyCustomOptionsUICommit(string $parent, string $selectedFile) The parent
        argument is the parent layout into which controls have been added using the
        optionsUICreate flag.
    
    - optionsUICreate : ocr          (script)        [create]
        MEL only.  The string is interpreted as a MEL callback, to be called on creation
        of the file dialog.  The callback is of the form: global proc
        MyCustomOptionsUISetup(string $parent) The parent argument is the parent layout
        into which controls can be added.  This parent is the right-hand pane of the
        file dialog.
    
    - optionsUIInit : oin            (script)        [create]
        MEL only.  The string is interpreted as a MEL callback, to be called just after
        file dialog creation, to initialize controls.  The callback is of the form:
        global proc MyCustomOptionsUIInitValues(string $parent, string $filterType) The
        parent argument is the parent layout into which controls have been added using
        the optionsUICreate flag.  The filterType argument is the initial file filter.
    
    - returnFilter : rf              (bool)          [create]
        If true, the selected filter will be returned as the last item in the string
        array along with the selected files.
    
    - selectFileFilter : sff         (unicode)       [create]
        Specify the initial file filter to select.  Specify just the begining text and
        not the full wildcard spec.
    
    - selectionChanged : sc          (script)        [create]
        MEL only.  The string is interpreted as a MEL callback, to be called when the
        user changes the file selection in the file dialog.  The callback is of the
        form: global proc MyCustomSelectionChanged(string $parent, string $selection)
        The parent argument is the parent layout into which controls have been added
        using the optionsUICreate flag.  The selection argument is the full path to the
        newly-selected file.
    
    - setProjectBtnEnabled : spe     (bool)          [create]
        Define whether the project button should be enabled
    
    - startingDirectory : dir        (unicode)       [create]
        Provide the starting directory for the dialog.                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.fileDialog2`
    """
    pass


def _correctPath(path): pass


def saveAs(newname, **kwargs):
    """
    Returns
    -------
    Path
    """
    pass


def reference(*args, **kwargs):
    """
    Flags:
    - connectionsBroken : cb         (bool)          []
    
    - connectionsMade : cm           (bool)          []
    
    - dagPath : dp                   (bool)          []
    
    - editCommand : ec               (unicode)       []
    
    - filename : f                   (unicode)       []
    
    - isNodeReferenced : inr         (bool)          []
    
    - longName : ln                  (bool)          []
    
    - node : n                       (unicode)       []
    
    - referenceNode : rfn            (unicode)       []
    
    - shortName : sn                 (bool)          []
    
    
    Derived from mel command `maya.cmds.reference`
    """
    pass


def devicePanel(*args, **kwargs):
    """
    This command is now obsolete. It is included only for the purpose of file
    compatibility. It creates a blank panel.
    
    Flags:
    - control : ctl                  (bool)          [query]
        Returns the top level control for this panel. Usually used for getting a parent
        to attach popup menus. CAUTION: panels may not have controls at times.  This
        flag can return if no control is present.
    
    - copy : cp                      (unicode)       [edit]
        Makes this panel a copy of the specified panel.  Both panels must be of the same
        type.
    
    - createString : cs              (bool)          [edit]
        Command string used to create a panel
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the Maya panel.
    
    - editString : es                (bool)          [edit]
        Command string used to edit a panel
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - init : init                    (bool)          [create,edit]
        Initializes the panel's default state.  This is usually done automatically on
        file -new and file -open.
    
    - isUnique : iu                  (bool)          [query]
        Returns true if only one instance of this panel type is allowed.
    
    - label : l                      (unicode)       [query,edit]
        Specifies the user readable label for the panel.
    
    - menuBarRepeatLast : mrl        (bool)          [create,query,edit]
        Controls whether clicking on the menu header with the middle mouse button would
        repeat the last selected menu item.
    
    - menuBarVisible : mbv           (bool)          [create,query,edit]
        Controls whether the menu bar for the panel is displayed.
    
    - needsInit : ni                 (bool)          [query,edit]
        (Internal) On Edit will mark the panel as requiring initialization. Query will
        return whether the panel is marked for initialization.  Used during file -new
        and file -open.
    
    - parent : p                     (unicode)       [create]
        Specifies the parent layout for this panel.
    
    - popupMenuProcedure : pmp       (script)        [query,edit]
        Specifies the procedure called for building the panel's popup menu(s). The
        default value is buildPanelPopupMenu.  The procedure should take one string
        argument which is the panel's name.
    
    - replacePanel : rp              (unicode)       [edit]
        Will replace the specified panel with this panel.  If the target panel is within
        the same layout it will perform a swap.
    
    - tearOff : to                   (bool)          [query,edit]
        Will tear off this panel into a separate window with a paneLayout as the parent
        of the panel. When queried this flag will return if the panel has been torn off
        into its own window.
    
    - tearOffCopy : toc              (unicode)       [create]
        Will create this panel as a torn of copy of the specified source panel.
    
    - tearOffRestore : tor           (bool)          [create,edit]
        Restores panel if it is torn off and focus is given to it. If docked, becomes
        the active panel in the docked window. This should be the default flag that is
        added to all panels instead of -to/-tearOffflag which should only be used to
        tear off the panel.
    
    - unParent : up                  (bool)          [edit]
        Specifies that the panel should be removed from its layout. This (obviously)
        cannot be used with query.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.devicePanel`
    """
    pass


def unloadPlugin(*args, **kwargs):
    """
    Unload plug-ins from Maya. After the successful execution of this command, plug-
    in services will no longer be available.
    
    Flags:
    - addCallback : ac               (script)        [create]
        Add a procedure to be called just before a plugin is unloaded. The procedure
        should have one string argument, which will be the plugin's name.
    
    - force : f                      (bool)          [create]
        Unload the plugin even if it is providing services.  This is not recommended.
        If you unload a plug-in that implements a node or data type in the scene, those
        instances will be converted to unknown nodes or data and the scene will no
        longer behave properly. Maya may become unstable or even crash. If you use this
        flag you are advised to save your scene in MayaAscii format and restart Maya as
        soon as possible.
    
    - removeCallback : rc            (script)        [create]
        Remove a procedure which was previously added with -addCallback.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.unloadPlugin`
    """
    pass


def exportSelectedAnimFromReference(exportPath, **kwargs):
    """
    Export the main scene animation nodes and animation helper nodes from the selected referenced objects. This flag, when used in conjunction with the -rfn/referenceNode flag, can be constrained to only export animation nodes from the selected nodes of a specified reference file. See -ean/exportAnim flag description for details on usage of animation files.                  
    
    - exportSelectedAnimFromReference : f (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - exportSelectedAnimFromReference : rfn (unicode)       [query]
        This flag is only used during queries. In MEL, if it appears before -query then
        it must be followed by the name of one of the scene's reference nodes. That will
        determine the reference to be queried by whatever flags appear after -query. If
        the named reference node does not exist within the scene the command will fail
        with an error. In Python the equivalent behavior is obtained by passing the name
        of the reference node as the flag's value. In MEL, if this flag appears after
        -query then it takes no argument and will cause the command to return the name
        of the reference node associated with the file given as the command's argument.
        If the file is not a reference or for some reason does not have a reference node
        (e.g., the user deleted it) then an empty string will be returned. If the file
        is not part of the current scene then the command will fail with an error. In
        Python the equivalent behavior is obtained by passing True as the flag's value.
        In query mode, this flag can accept a value.
    
    - exportSelectedAnimFromReference : typ (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def saveFile(**kwargs):
    """
    Save the specified file. Returns the name of the saved file.                  
    
    - save : f                       (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - save : prs                     (unicode)       [create]
        When used with the save flag, the specified script will be executed before the
        file is saved.
    
    - save : pos                     (unicode)       [create]
        When used with the save flag, the specified script will be executed after the
        file is saved.
    
    - save : typ                     (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def listReferences(parentReference='None', recursive='False', namespaces='False', refNodes='False', references='True',
                   loaded='None', unloaded='None'):
    """
    Like iterReferences, except returns a list instead of an iterator.
    
    Parameters
    ----------
    parentReference : Union[str, Path, FileReference]
        a reference to get sub-references from. If None (default), the current
        scene is used.
    recursive : bool
        recursively determine all references and sub-references
    namespaces : bool
        controls whether namespaces are returned
    refNodes : bool
        controls whether reference PyNodes are returned
    references : bool
        controls whether FileReferences returned
    loaded : Optional[bool]
        whether to return loaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    unloaded : Optional[bool]
        whether to return unloaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    
    Returns
    -------
    List[Union[FileReference, Tuple[unicode, FileReference], Tuple[unicode, FileReference, nt.Reference]]]
    
    returns references in the scene as a list of value tuples.
    
    The values in the tuples can be namespaces, refNodes (as PyNodes), and/or
    references (as FileReferences), and are controlled by their respective
    keywords (and are returned in that order).  If only one of the three options
    is True, the result will not be a list of value tuples, but will simply be a
    list of values.
    
    Parameters
    ----------
    parentReference : Union[str, Path, FileReference]
        a reference to get sub-references from. If None (default), the current
        scene is used.
    recursive : bool
        recursively determine all references and sub-references
    namespaces : bool
        controls whether namespaces are returned
    refNodes : bool
        controls whether reference PyNodes are returned
    references : bool
        controls whether FileReferences returned
    recurseType : str
        if recursing, whether to do a 'breadth' or 'depth' first search;
        defaults to a 'depth' first
    loaded : Optional[bool]
        whether to return loaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    unloaded : Optional[bool]
        whether to return unloaded references in the return result; if both of
        loaded/unloaded are not given (or None), then both are assumed True;
        if only one is given, the other is assumed to have the opposite boolean
        value
    
    Returns
    -------
    Iterator[Union[FileReference, Tuple[unicode, FileReference], Tuple[unicode, FileReference, nt.Reference]]]
    """
    pass


def preloadRefEd(*args, **kwargs):
    """
    This creates an editor for managing which references will be read in (loaded)
    and which deferred (unloaded) upon opening a file.
    
    Flags:
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - filter : f                     (unicode)       [create,query,edit]
        Specifies the name of an itemFilter object to be used with this editor. This
        filters the information coming onto the main list of the editor.
    
    - forceMainConnection : fmc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object. This is a variant of the -mainListConnection flag in
        that it will force a change even when the connection is locked. This flag is
        used to reduce the overhead when using the -unlockMainConnection ,
        -mainListConnection, -lockMainConnection flags in immediate succession.
    
    - highlightConnection : hlc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its highlight list. Not all editors have a highlight list. For
        those that do, it is a secondary selection list.
    
    - lockMainConnection : lck       (bool)          [create,edit]
        Locks the current list of objects within the mainConnection, so that only those
        objects are displayed within the editor. Further changes to the original
        mainConnection are ignored.
    
    - mainListConnection : mlc       (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - selectCommand : sc             (script)        [create,query,edit]
        A script to be executed when an item is selected.
    
    - selectFileNode : sf            (bool)          [query]
        Query the currently selected load setting. Returns the id of the currently
        selected load setting. This id can be used as an argument to the selLoadSettings
        command.
    
    - selectionConnection : slc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its own selection list. As the user selects things in this
        editor, they will be selected in the selectionConnection object. If the object
        undergoes changes, the editor updates to show the changes.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - unParent : up                  (bool)          [create,edit]
        Specifies that the editor should be removed from its layout. This cannot be used
        in query mode.
    
    - unlockMainConnection : ulk     (bool)          [create,edit]
        Unlocks the mainConnection, effectively restoring the original mainConnection
        (if it is still available), and dynamic updates.
    
    - updateMainConnection : upd     (bool)          [create,edit]
        Causes a locked mainConnection to be updated from the orginal mainConnection,
        but preserves the lock state.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.preloadRefEd`
    """
    pass


def exportSelected(exportPath, **kwargs):
    """
    Export the selected items into the specified file. Returns the name of the exported file.                  
    
    - exportSelected : f             (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - exportSelected : ch            (bool)          [create,query]
        For use with exportSelected to specify whether attached construction history
        should be included in the export.
    
    - exportSelected : chn           (bool)          [create,query]
        For use with exportSelected to specify whether attached channels should be
        included in the export.
    
    - exportSelected : con           (bool)          [create,query]
        For use with exportSelected to specify whether attached constraints should be
        included in the export.
    
    - exportSelected : exp           (bool)          [create,query]
        For use with exportSelected to specify whether attached expressions should be
        included in the export.
    
    - exportSelected : sh            (bool)          [create,query]
        For use with exportSelected to specify whether attached shaders should be
        included in the export.
    
    - exportSelected : pr            (bool)          [create]
        Modifies the various import/export flags such that references are
        imported/exported as actual references rather than copies of those references.
    
    - exportSelected : typ           (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def referenceEdit(*args, **kwargs):
    """
    Use this command to remove and change the modifications which have been applied
    to references. A valid commandTarget is either a reference node, a reference
    file, a node in a reference, or a plug from a reference. Only modifications that
    have been made from the currently open scene can be changed or removed. The
    'referenceQuery -topReference' command can be used to determine what
    modifications have been made to a given commandTarget. Additionally only
    unapplied edits will be affected. Edits are unapplied when the node(s) which
    they affect are unloaded, or when they could not be successfully applied. By
    default this command only works on failed edits (this can be adjusted using the
    -failedEditsand -successfulEditsflags). Specifying a reference node as the
    command target is equivalent to specifying every node in the target reference
    file as a target. In this situation the results may differ depending on whether
    the target reference is loaded or unloaded. When it is unloaded, edits that
    affect both a node in the target reference and a node in one of its descendant
    references may be missed (e.g. those edits may not be removed). This is because
    when a reference is unloaded Maya no longer retains detailed information about
    which nodes belong to it. However, edits that only affect nodes in the target
    reference or in one of its ancestral references should be removed as expected.
    When the flags -removeEdits and -editCommand are used together, by default all
    connectAttr edits are removed from the specified source object. To remove only
    edits that connect to a specific target object, the target object can be passed
    as an additional argument to the command. This narrows the match criteria, so
    that only edits that connect the source object to the provided target in this
    additional argument are removed. See the example below. NOTE: When specifying a
    plug it is important to use the appropriate long attribute name.
    
    Flags:
    - applyFailedEdits : afe         (bool)          [create]
        Attempts to apply any unapplied edits. This flag is useful if previously failing
        edits have been fixed using the -changeEditTarget flag. This flag can only be
        used on loaded references. If the command target is a referenced node, the
        associated reference is used instead.
    
    - changeEditTarget : cet         (unicode, unicode) [create]
        Used to change a target of the specified edits. This flag takes two parameters:
        the old target of the edits, and the new target to change it to. The target can
        either be a node name (node), a node and attribute name (node.attr), or just an
        attribute name (.attr). If an edit currently affects the old target, it will be
        changed to affect the new target. Flag 'referenceQuery' should be used to
        determine the format of the edit targets. As an example most edits store the
        long name of the attribute (e.g. translateX), so when specifying the old target,
        a long name must also be used. If the short name is specified (e.g. tx), chances
        are the edit won't be retargeted.
    
    - editCommand : ec               (unicode)       [create,query]
        This is a secondary flag used to indicate which type of reference edits should
        be considered by the command. If this flag is not specified all edit types will
        be included. This flag requires a string parameter. Valid values are: addAttr,
        connectAttr, deleteAttr, disconnectAttr, parent, setAttr, lockand unlock. In
        some contexts, this flag may be specified more than once to specify multiple
        edit types to consider.
    
    - failedEdits : fld              (bool)          [create]
        This is a secondary flag used to indicate whether or not failed edits should be
        acted on (e.g. queried, removed, etc...). A failed edit is an edit which could
        not be successfully applied the last time its reference was loaded. An edit can
        fail for a variety of reasons (e.g. the referenced node to which it applies was
        removed from the referenced file). By default failed edits will be acted on.
    
    - onReferenceNode : orn          (unicode)       [create,query]
        This is a secondary flag used to indicate that only those edits which are stored
        on the indicated reference node should be considered. This flag only supports
        multiple uses when specified with the exportEditscommand.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - removeEdits : r                (bool)          [create]
        Remove edits which affect the specified unloaded commandTarget.
    
    - successfulEdits : scs          (bool)          [create]
        This is a secondary flag used to indicate whether or not successful edits should
        be acted on (e.g. queried, removed, etc...). A successful edit is any edit which
        was successfully applied the last time its reference was loaded. This flag will
        have no affect if the commandTarget is loaded. By default successful edits will
        not be acted on.
    
    
    Derived from mel command `maya.cmds.referenceEdit`
    """
    pass


def _translateEditFlags(kwargs, addKwargs='True'):
    """
    Given the pymel values for successfulEdits/failedEdits (which may be
    True, False, or None), returns the corresponding maya.cmds values to use
    """
    pass


def exportEdits(*args, **kwargs):
    """
    Use this command to export edits made in the scene to a file. The exported file
    can be subsequently imported to another scene. Edits may include: nodes,
    connections and reference edits such as value changes. The nodes that are
    included in the exported file will be based on the options used. At least one
    option flag that describes the set of target nodes to include in the exported
    file must be specified (e.g. 'selected', 'onReferenceNode'). Use the inclusion
    flags ('includeAnimation', 'includeShaders', 'includeNetwork') to specify which
    additional related nodes will be added to the export list. In export mode, when
    the command completes successfully, the name of the exported file will be
    returned. In query mode, this command will return information about the contents
    of the exported file. The query mode will return the list of nodes that will be
    considered for inclusion in the exported file based on the specified flags.
    
    Flags:
    - editCommand : ec               (unicode)       [create,query]
        This is a secondary flag used to indicate which type of reference edits should
        be considered by the command. If this flag is not specified all edit types will
        be included. This flag requires a string parameter. Valid values are: addAttr,
        connectAttr, deleteAttr, disconnectAttr, parent, setAttr, lockand unlock. In
        some contexts, this flag may be specified more than once to specify multiple
        edit types to consider.
    
    - excludeHierarchy : ehr         (bool)          [create,query]
        By default, all DAG parents and DAG history are written to the export file. To
        prevent any DAG relations not otherwise connected to the target nodes to be
        included, specify the -excludeHierarchy flag.
    
    - excludeNode : en               (unicode)       [create,query]
        Prevent the node from being included in the list of nodes being exported. This
        flag is useful to exclude specific scene nodes that might otherwise be exported.
        In the case where more than one Maya node has the same name, the DAG path can be
        specified to uniquely identify the node.
    
    - exportSelected : exs           (bool)          [create,query]
        The selected nodes and their connections to each other will be exported.
        Additionally, any dangling connections to non-exported nodes will be exported.
        Default nodes are ignored and never exported. Note that when using the
        exportSelected flag, only selected nodes are exported, and -include/-exclude
        flags such as -includeHierarchy are ignored.
    
    - force : f                      (bool)          [create,query]
        Force the export action to take place. This flag is required to overwrite an
        existing file.
    
    - includeAnimation : ian         (bool)          [create,query]
        Additionally include animation nodes and animation helper nodes associated with
        the target nodes being exported.
    
    - includeConstraints : ic        (bool)          [create,query]
        Additionally include constraint-related nodes associated with the target nodes
        being exported.
    
    - includeDeformers : idf         (bool)          [create,query]
        Additionally include deformer networks associated with the target nodes being
        exported.
    
    - includeNetwork : inw           (bool)          [create,query]
        Additionally include the network of nodes connected to the target nodes being
        exported.
    
    - includeNode : includeNode      (unicode)       [create,query]
        Additionally include the named node in the list of nodes being exported. In the
        case where more than one Maya node has the same name, the DAG path can be
        specified to uniquely identify the node.
    
    - includeSetAttrs : isa          (bool)          [create,query]
        When using the -selected/-sel flag, if any of the selected nodes are referenced,
        also include/exclude any setAttr edits on those nodes. If used with the
        -onReferenceNode/-orn flag, include/exclude any setAttr edits on the reference.
    
    - includeSetDrivenKeys : sdk     (bool)          [create,query]
        Additionally include setDrivenKey-related nodes associated with the target nodes
        being exported.
    
    - includeShaders : ish           (bool)          [create,query]
        Additionally include shaders associated with the target nodes being exported.
    
    - onReferenceNode : orn          (unicode)       [create,query]
        This is a secondary flag used to indicate that only those edits which are stored
        on the indicated reference node should be considered. This flag only supports
        multiple uses when specified with the exportEditscommand.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    - selected : sel                 (bool)          [create,query]
        Export will operate on the list of nodes currently selected. This flag differs
        from the exportSelected flag in that the selected nodes are not exported, only
        the edits on them, and any nodes found via the include flags that are used (such
        as includeAnimation, includeNetwork and so on).
    
    - type : typ                     (unicode)       [create,query]
        Set the type of the exported file. Valid values are editMAor editMB. Note that
        this command respects the global defaultExtensionssetting for file naming that
        is controlled with the file command defaultExtensions option.  See the file
        command for more information.
    
    
    Derived from mel command `maya.cmds.exportEdits`
    """
    pass


def namespaceInfo(*args, **kwargs):
    """
    This command displays information about a namespace. The target namespace can
    optionally be specified on the command line. If no namespace is specified, the
    command will display information about the current namespace. A namespace is a
    simple grouping of objects under a given name. Each item in a namespace can then
    be identified by its own name, along with what namespace it belongs to.
    Namespaces can contain other namespaces like sets, with the restriction that all
    namespaces are disjoint. Namespaces are primarily used to resolve name-clash
    issues in Maya, where a new object has the same name as an existing object (from
    importing a file, for example). Using namespaces, you can have two objects with
    the same name, as long as they are contained in different namespaces. Note that
    namespaces are a simple grouping of names, so they do not effect selection, the
    DAG, the Dependency Graph, or any other aspect of Maya.  All namespace names are
    colon-separated. The namespace format flags are: baseName(shortName), fullName
    and absoluteName. The flags are used in conjunction with the main query flags to
    specify the desired namespace format of the returned result. They can also be
    used to return the different formats of a specified namespace. By default, when
    no format is specified, the result will be returned as a full name.
    
    Modifications:
        - returns an empty list when the result is None
        - returns wrapped classes for listOnlyDependencyNodes
    
    Flags:
    - absoluteName : an              (bool)          [create]
        This is a general flag which can be used to specify the desired format for the
        namespace(s) returned by the command. The absolute name of the namespace is a
        full namespace path, starting from the root namespace :and including all parent
        namespaces.  For example :ns:ballis an absolute namespace name while ns:ballis
        not. The absolute namespace name is invariant and is not affected by the current
        namespace or relative namespace modes. See also other format modifiers
        'baseName', 'fullName', etc
    
    - baseName : bn                  (bool)          [create]
        This is a general flag which can be used to specify the desired format for the
        namespace(s) returned by the command. The base name of the namespace contains
        only the leaf level name and does not contain its parent namespace(s). For
        example the base name of an object named ns:ballis ball. This mode will always
        return the base name in the same manner, and is not affected by the current
        namespace or relative namespace mode. See also other format modifiers
        'absoluteName', 'fullName', etc The flag 'shortName' is a synonym for
        'baseName'.
    
    - currentNamespace : cur         (bool)          [create]
        Display the name of the current namespace.
    
    - dagPath : dp                   (bool)          [create]
        This flag modifies the 'listNamespace' and 'listOnlyDependencyNodes' flags to
        indicate that the names of any dag objects returned will include as much of the
        dag path as is necessary to make the names unique. If this flag is not present,
        the names returned will not include any dag paths.
    
    - fullName : fn                  (bool)          [create]
        This is a general flag which can be used to specify the desired format for the
        namespace(s) returned by the command. The full name of the namespace contains
        both the namespace path and the base name, but without the leading colon
        representing the root namespace. For example ns:ballis a full name, whereas
        :ns:ballis an absolute name. This mode is affected by the current namespace and
        relative namespace modes. See also other format modifiers 'baseName',
        'absoluteName', etc.
    
    - internal : int                 (bool)          [create]
        This flag is used together with the 'listOnlyDependencyNodes' flag. When this
        flag is set, the returned list will include internal nodes (for example
        itemFilters) that are not listed by default.
    
    - isRootNamespace : ir           (bool)          [create]
        Returns true if the namespace is root(:), false if not.
    
    - listNamespace : ls             (bool)          [create]
        List the contents of the namespace.
    
    - listOnlyDependencyNodes : lod  (bool)          [create]
        List all dependency nodes in the namespace.
    
    - listOnlyNamespaces : lon       (bool)          [create]
        List all namespaces in the namespace.
    
    - parent : p                     (bool)          [create]
        Display the parent of the namespace. By default, the list returned will not
        include internal nodes (such as itemFilters). To include the internal nodes, use
        the 'internal' flag.
    
    - recurse : r                    (bool)          [create]
        Can be specified with 'listNamespace', 'listOnlyNamespaces' or
        'listOnlyDependencyNode' to cause the listing to recursively include any child
        namespaces of the namespaces;
    
    - shortName : sn                 (bool)          [create]
        This flag is deprecated and may be removed in future releases of Maya. It is a
        synonym for the baseName flag. Please use the baseName flag instead.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.namespaceInfo`
    """
    pass


def _safeEval(s): pass


def listNamespaces_old():
    """
    Deprecated
    Returns a list of the namespaces of referenced files.
    REMOVE In Favor of listReferences('dict') ?
    """
    pass


def fileBrowserDialog(*args, **kwargs):
    """
    The fileBrowserDialog and fileDialog commands have now been deprecated. Both
    commands are still callable, but it is recommended that the fileDialog2 command
    be used instead.  To maintain some backwards compatibility, both
    fileBrowserDialog and fileDialog will convert the flags/values passed to them
    into the appropriate flags/values that the fileDialog2 command uses and will
    call that command internally.  It is not guaranteed that this compatibility will
    be able to be maintained in future versions so any new scripts that are written
    should use fileDialog2. See below for an example of how to change a script to
    use fileDialog2.
    
    Flags:
    - actionName : an                (unicode)       [create]
        Script to be called when the file is validated.
    
    - dialogStyle : ds               (int)           [create]
        0 for old style dialog1 for Windows 2000 style Explorer style2 for Explorer
        style with Shortcuttip at bottom
    
    - fileCommand : fc               (script)        [create]
        The script to run on command action
    
    - fileType : ft                  (unicode)       [create]
        Set the type of file to filter.  By default this can be any one of: mayaAscii,
        mayaBinary, mel, OBJ, directory, plug-in, audio, move, EPS, Illustrator, image.
        plug-ins may define their own types as well.
    
    - filterList : fl                (unicode)       [create]
        Specify file filters. Used with dialog style 1 and 2. Each string should be a
        description followed by a comma followed by a semi-colon separated list of file
        extensions with wildcard.
    
    - includeName : includeName      (unicode)       [create]
        Include the given string after the actionName in parentheses. If the name is too
        long, it will be shortened to fit on the dialog (for example,
        /usr/alias/commands/scripts/fileBrowser.mel might be shortened to
        /usr/...pts/fileBrowser.mel)
    
    - mode : m                       (int)           [create]
        Defines the mode in which to run the file brower: 0 for read1 for write2 for
        write without paths (segmented files)4 for directories have meaning when used
        with the action+100 for returning short names
    
    - operationMode : om             (unicode)       [create]
        Enables the option dialog. Valid strings are:
        ImportReferenceSaveAsExportAllExportActive
    
    - tipMessage : tm                (unicode)       [create]
        Message to be displayed at the bottom of the style 2 dialog box.
    
    - windowTitle : wt               (unicode)       [create]
        Set the window title of a style 1 or 2 dialog box                  Flag can have
        multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.fileBrowserDialog`
    """
    pass


def _setTypeKwargFromExtension(path, kwargs, mode="'write'"): pass


def exportAnim(exportPath, **kwargs):
    """
    Export all animation nodes and animation helper nodes from all objects in the scene. The resulting animation export file will contain connections to objects that are not included in the animation file. As a result, importing/referencing this file back in will require objects of the same name to be present, else errors will occur. The -sns/swapNamespace flag is available for swapping the namespaces of given objects to another namespace. This use of namespaces can be used to re-purpose the animation file to multiple targets using a consistent naming scheme.  The exportAnim flag will not export animation layers. For generalized file export of animLayers and other types of nodes, refer to the exportEdits command. Or use the Export Layers functionality.                  
    
    - exportAnim : f                 (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - exportAnim : typ               (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def loadPlugin(*args, **kwargs):
    """
    Load plug-ins into Maya. The parameter(s) to this command are either the names
    or pathnames of plug-in files.  The convention for naming plug-ins is to use a
    .so extension on Linux, a .mll extension on Windows and .bundle extension on Mac
    OS X. If no extension is provided then the default extension for the platform
    will be used. To load a Python plugin you must explicitly supply the '.py'
    extension. If the plugin was specified with a pathname then that is where the
    plugin will be searched for. If no pathname was provided then the current
    working directory (i.e. the one returned by Maya's 'pwd' command) will be
    searched, followed by the directories in the MAYA_PLUG_IN_PATH environment
    variable. When the plug-in is loaded, the name used in Maya's internal plug-in
    registry for the plug-in information will be the file name with the extension
    removed.  For example, if you load the plug-in newNode.mllthe name used in the
    Maya's registry will be newNode.  This value as well as that value with either a
    .so, .mllor .bundleextension can be used as valid arguments to either the
    unloadPlugin or pluginInfo commands.
    
    Flags:
    - addCallback : ac               (script)        [create]
        Add a MEL or Python callback script to be called after a plug-in is loaded.  For
        MEL, the procedure should have the following signature: global proc
        procedureName(string $pluginName).  For Python, you may specify either a script
        as a string, or a Python callable object such as a function.  If you specify a
        string, then put the formatting specifier %swhere you want the name of the plug-
        in to be inserted.  If you specify a callable such as a function, then the name
        of the plug-in will be passed as an argument.
    
    - allPlugins : a                 (bool)          [create]
        Cause all plug-ins in the search path specified in MAYA_PLUG_IN_PATH to be
        loaded.
    
    - name : n                       (unicode)       [create]
        Set a user defined name for the plug-ins that are loaded.  If the name is
        already taken, then a number will be added to the end of the name to make it
        unique.
    
    - qObsolete : q                  (bool)          []
    
    - quiet : qt                     (bool)          [create]
        Don't print a warning if you attempt to load a plug-in that is already loaded.
    
    - removeCallback : rc            (script)        [create]
        Removes a procedure which was previously added with -addCallback.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.loadPlugin`
    """
    pass


def sceneEditor(*args, **kwargs):
    """
    This creates an editor for managing the files in a scene.
    
    Flags:
    - control : ctl                  (bool)          [query]
        Query only. Returns the top level control for this editor. Usually used for
        getting a parent to attach popup menus. Caution: It is possible for an editor to
        exist without a control. The query will return NONEif no control is present.
    
    - defineTemplate : dt            (unicode)       [create]
        Puts the command in a mode where any other flags and arguments are parsed and
        added to the command template specified in the argument. They will be used as
        default arguments in any subsequent invocations of the command when templateName
        is set as the current template.
    
    - docTag : dtg                   (unicode)       [create,query,edit]
        Attaches a tag to the editor.
    
    - exists : ex                    (bool)          [create]
        Returns whether the specified object exists or not. Other flags are ignored.
    
    - filter : f                     (unicode)       [create,query,edit]
        Specifies the name of an itemFilter object to be used with this editor. This
        filters the information coming onto the main list of the editor.
    
    - forceMainConnection : fmc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object. This is a variant of the -mainListConnection flag in
        that it will force a change even when the connection is locked. This flag is
        used to reduce the overhead when using the -unlockMainConnection ,
        -mainListConnection, -lockMainConnection flags in immediate succession.
    
    - highlightConnection : hlc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its highlight list. Not all editors have a highlight list. For
        those that do, it is a secondary selection list.
    
    - lockMainConnection : lck       (bool)          [create,edit]
        Locks the current list of objects within the mainConnection, so that only those
        objects are displayed within the editor. Further changes to the original
        mainConnection are ignored.
    
    - mainListConnection : mlc       (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will use as
        its source of content. The editor will only display items contained in the
        selectionConnection object.
    
    - onlyParents : op               (bool)          [query]
        When used with the 'selectItem' or 'selectReference' queries it indicates that,
        if both a parent and a child file or reference are selected, only the parent
        will be returned.
    
    - panel : pnl                    (unicode)       [create,query]
        Specifies the panel for this editor. By default if an editor is created in the
        create callback of a scripted panel it will belong to that panel. If an editor
        does not belong to a panel it will be deleted when the window that it is in is
        deleted.
    
    - parent : p                     (unicode)       [create,query,edit]
        Specifies the parent layout for this editor. This flag will only have an effect
        if the editor is currently un-parented.
    
    - refreshReferences : rr         (bool)          [edit]
        Force refresh of references
    
    - selectCommand : sc             (script)        [create,query,edit]
        A script to be executed when an item is selected.
    
    - selectItem : si                (int)           [query,edit]
        Query or change the currently selected item. When queried, the currently
        selected file name will be return.
    
    - selectReference : sr           (unicode)       [query]
        Query the currently selected reference. Returns the name of the currently
        selected reference node.
    
    - selectionConnection : slc      (unicode)       [create,query,edit]
        Specifies the name of a selectionConnection object that the editor will
        synchronize with its own selection list. As the user selects things in this
        editor, they will be selected in the selectionConnection object. If the object
        undergoes changes, the editor updates to show the changes.
    
    - shortName : shn                (bool)          [query]
        When used with the 'selectItem' query it indicates that the file name returned
        will be the short name (i.e. just a file name without any directory paths). If
        this flag is not present, the full name and directory path will be returned.
    
    - stateString : sts              (bool)          [query]
        Query only flag. Returns the MEL command that will create an editor to match the
        current editor state. The returned command string uses the string variable
        $editorName in place of a specific name.
    
    - unParent : up                  (bool)          [create,edit]
        Specifies that the editor should be removed from its layout. This cannot be used
        in query mode.
    
    - unlockMainConnection : ulk     (bool)          [create,edit]
        Unlocks the mainConnection, effectively restoring the original mainConnection
        (if it is still available), and dynamic updates.
    
    - unresolvedName : un            (bool)          [query]
        When used with the 'selectItem' query it indicates that the file name returned
        will be unresolved (i.e. it will be the path originally specified when the file
        was loaded into Maya; this path may contain environment variables and may not
        exist on disk). If this flag is not present, the resolved name will    be
        returned.
    
    - updateMainConnection : upd     (bool)          [create,edit]
        Causes a locked mainConnection to be updated from the orginal mainConnection,
        but preserves the lock state.
    
    - useTemplate : ut               (unicode)       [create]
        Forces the command to use a command template other than the current one.
    
    - withoutCopyNumber : wcn        (bool)          [query]
        When used with the 'selectItem' query it indicates that the file name returned
        will not have a copy number appended to the end. If this flag is not present,
        the file name returned may have a copy number appended to the end.
        Flag can have multiple arguments, passed either as a tuple or a list.
    
    
    Derived from mel command `maya.cmds.sceneEditor`
    """
    pass


def _getTypeFromExtension(path, mode="'write'"):
    """
    Parameters
    ----------
    path : str
        path from with to pull the extension from - note that it may NOT be
        ONLY the extension - ie, "obj" and ".obj", will not work, but
        "foo.obj" will
    mode : str
        {'write', 'read'}
        the type is basically a string name of a file translator, which can
        have different ones registered for reading or writing; this specifies
        whether you're looking for the read or write translator
    """
    pass


def importFile(filepath, **kwargs):
    """
    Import the specified file. Returns the name of the imported file.                  
    
    - i : lnr                        (bool)          [create]
        This flag is obsolete and has been replaced witht the loadReferenceDepth flag.
        When used with the -open flag, no references will be loaded. When used with
        -i/import, -r/reference or -lr/loadReference flags, will load the top-most
        reference only.
    
    - i : lrd                        (unicode)       [create]
        Used to specify which references should be loaded. Valid types are all, noneand
        topOnly, which will load all references, no references and top-level references
        only, respectively. May only be used with the -o/open, -i/import, -r/reference
        or -lr/loadReference flags. When noneis used with -lr/loadReference, only path
        validation is performed. This can be used to replace a reference without
        triggering reload. Not using loadReferenceDepth will load references in the same
        loaded or unloaded state that they were in when the file was saved.
        Additionally, the -lr/loadReference flag supports a fourth type, asPrefs. This
        will force any nested references to be loaded according to the state (if any)
        stored in the current scene file, rather than according to the state saved in
        the reference file itself.
    
    - i : dns                        (bool)          [create]
        Use the default name space for import and referencing.  This is an advanced
        option.  If set, then on import or reference, Maya will attempt to place all
        nodes from the imported or referenced file directly into the root (default) name
        space, without invoking any name clash resolution algorithms.  If the names of
        any of the new objects    already exist in the root namespace, then errors will
        result. The user of this flag is responsible for creating a name clash
        resolution mechanism outside of Maya to avoid such errors. Note:This flag    is
        intended only for use with custom file translators written through    the API.
        Use at your own risk.
    
    - i : dr                         (bool)          [create,query]
        When used in conjunction with the -reference flag, this flag determines if the
        reference is loaded, or if loading is deferred.C: The default is false.Q: When
        queried, this flag returns true if the reference is deferred, or false if the
        reference is not deferred. If this is used with -rfn/referenceNode, the -rfn
        flag must come before -q.
    
    - i : gr                         (bool)          [create]
        Used only with the -r or the -i flag. Used to group all the imported/referenced
        items under a single transform.
    
    - i : gn                         (unicode)       [create]
        Used only with the -gr flag. Optionally used to set the name of the transform
        node that the imported/referenced items will be grouped under.
    
    - i : ra                         (bool)          [create]
        If true, rename all newly-created nodes, not just those whose names clash with
        existing nodes. Only available with -i/import.
    
    - i : rpr                        (unicode)       [create,query]
        The string to use as a prefix for all objects from this file. This flag has been
        replaced by -ns/namespace.
    
    - i : sns                        (unicode, unicode) [create]
        Can only be used in conjunction with the -r/reference or -i/import flags. This
        flag will replace any occurrences of a given namespace to an alternate specified
        namespace. This namespace swapwill occur as the file is referenced in. It takes
        in two string arguments. The first argument specifies the namespace to replace.
        The second argument specifies the replacement namespace. Use of this flag,
        implicitly enables the use of namespaces and cannot be used with deferReference.
    
    - i : rnn                        (bool)          [create]
        Used to control the return value in open, import, loadReference, and reference
        operations. It will force the file command to return a list of new nodes added
        to the current scene.
    
    - i : pr                         (bool)          [create]
        Modifies the various import/export flags such that references are
        imported/exported as actual references rather than copies of those references.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def displayInfo(*args, **kwargs): pass


def renameFile(newname, *args, **kwargs):
    """
    Rename the scene. Used mostly during save to set the saveAs name. Returns the new name of the scene.                  
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def sceneName():
    """
    return the name of the current scene.                  
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def exportSelectedAnim(exportPath, **kwargs):
    """
    Export all animation nodes and animation helper nodes from the selected objects in the scene. See -ean/exportAnim flag description for details on usage of animation files.                  
    
    - exportSelectedAnim : f         (bool)          [create]
        Force an action to take place. (new, open, save, remove reference, unload
        reference) Used with removeReference to force remove reference namespace even if
        it has contents. Cannot be used with removeReference if the reference resides in
        the root namespace. Used with unloadReference to force unload reference even if
        the reference node is locked, without prompting a dialog that warns user about
        the lost of edits.
    
    - exportSelectedAnim : typ       (unicode)       [create,query]
        Set the type of this file.  By default this can be any one of: mayaAscii,
        mayaBinary, mel,  OBJ, directory, plug-in, audio, move, EPS, Adobe(R)
        Illustrator(R), imageplug-ins may define their own types as well.Return a string
        array of file types that match this file.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


def exportAsReference(exportPath, **kwargs):
    """
    Export the selected objects into a reference file with the given name. The file is saved on disk during the process. Returns the name of the reference created.                  
    
    - exportAsReference : ns         (unicode)       [edit]
        The namespace name to use that will group all objects during importing and
        referencing. Change the namespace used to group all the objects from the
        specified referenced file. The reference must have been created with the Using
        Namespacesoption, and must be loaded. Non-referenced nodes contained in the
        existing namespace will also be moved to the new namespace. The new namespace
        will be created by this command and can not already exist. The old namespace
        will be removed.
    
    - exportAsReference : rpr        (unicode)       [create,query]
        The string to use as a prefix for all objects from this file. This flag has been
        replaced by -ns/namespace.
    
    
    Derived from mel command `maya.cmds.file`
    """
    pass


_pymel_options = {}

workspace = Workspace()

fileInfo = FileInfo()

_logger = None
