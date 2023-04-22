if False:
    from typing import Dict, List, Tuple, Union, Optional


class DocstringBuilder(object):
    def __init__(self, cmdName, indentation="'    '"): pass

    def addFlag(self, flag, typ, shortname, descr, modes):
        """
        Generate docs for a single flag
        """
        pass

    def addFooter(self): pass

    def build(self, docstring):
        """
        Add the generated docstrings to the existing docstring
        
        Parameters
        ----------
        docstring : str
            original docstring
        
        Returns
        -------
        str
        """
        pass

    def getTypeIdentifier(self, typ): pass

    def indent(self, lines): pass

    def startFlagSection(self): pass

    DOC_WIDTH = 120

    __dict__ = None

    __weakref__ = None


class PyDocstringBuilder(DocstringBuilder):
    """
    Docstring builder that generates human-readable docstrings for use with
    the python help() function.
    """

    def addFlag(self, flag, typ, shortname, descr, modes): pass

    def startFlagSection(self): pass

    @staticmethod
    def section(title): pass

    DOC_WIDTH = 80


class RstDocstringBuilder(DocstringBuilder):
    """
    Docstring builder that outputs reStructuredText for building HTML docs
    """

    def addFlag(self, flag, typ, shortname, descr, modes): pass

    def addFooter(self): pass

    def startFlagSection(self): pass

    @staticmethod
    def makerow(items, widths): pass

    @staticmethod
    def section(title): pass

    altwidths = []

    headersep = '+==+===================================================================================================+===============================+===============================+\n'

    rowsep = '+--+---------------------------------------------------------------------------------------------------+-------------------------------+-------------------------------+\n'

    w = 32

    widths = []


class NumpyDocstringBuilder(DocstringBuilder):
    def addFlag(self, flag, typ, shortname, descr, modes): pass

    def getTypeIdentifier(self, typ): pass

    def startFlagSection(self): pass

    @staticmethod
    def section(title): pass

    DOC_WIDTH = 80


def indent(s, margin): pass
