"""
These classes are the UI builders for the options of import and Export
of a render setup.
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


class ExportUI(object):
    """
    Helper class to build the Options UI for the fileDialog2 command used when exporting all
    """

    @staticmethod
    def addOptions(parent, exportOption): pass

    @staticmethod
    def setLabelColorExport(value):
        """
        User can decide to export label colors to json
        """
        pass

    @staticmethod
    def setNotesText(data):
        """
        Preserve the notes because it's consumed after the UI is gone.
        Note: Trap the focus changed which is the only way to have the text for a scroll field.
        """
        pass

    @staticmethod
    def setRenderSettingsExport(value):
        """
        User can decide to export Render Settings and AOVs to json
        """
        pass

    __dict__ = None

    __weakref__ = None

    exportColorType = 1

    exportTextEditor = None

    notesText = None

    notesTextEditor = None


class ImportAOVsUI(object):
    """
    Helper class to build the Options UI for the fileDialog2 command used for importing AOVs
    """

    @staticmethod
    def addOptions(parent): pass

    @staticmethod
    def setMergeImportType(data):
        """
        Merge the content of the existing render setup with the imported content. 
        If an unexpected render setup object is found it will renamed using the 'importText'.
        """
        pass

    @staticmethod
    def setOverwriteImportType(data):
        """
        Completely overwrite the content of the existing render setup with the imported content.
        """
        pass

    __dict__ = None

    __weakref__ = None

    importType = 0


class ParentGuard(object):
    def __enter__(self): pass

    def __exit__(self, type, value, traceback): pass

    __dict__ = None

    __weakref__ = None


class ImportAllUI(object):
    """
    Helper class to build the Options UI for the fileDialog2 command used when importing all
    """

    @staticmethod
    def addOptions(parent): pass

    @staticmethod
    def setImportText(data):
        """
        Preserve the text because it's consumed after the UI is gone.
        """
        pass

    @staticmethod
    def setLabelColorImport(value):
        """
        User can decide to import label colors from json
        """
        pass

    @staticmethod
    def setMergeImportType(data):
        """
        Merge the content of the existing render setup with the imported content. 
        If an unexpected render setup object is found it will renamed using the 'importText'.
        """
        pass

    @staticmethod
    def setOverwriteImportType(data):
        """
        Completely overwrite the content of the existing render setup with the imported content.
        """
        pass

    @staticmethod
    def setRenameImportType(data):
        """
        Always rename the imported render setup content using the 'importText'.
        """
        pass

    @staticmethod
    def updateContent(parent, selectedFilename):
        """
        Update the displayed content following the file selection 
        Note: If the file is not a render setup file or is a directory, 
              the content (notes & preview) will be empty.
        """
        pass

    __dict__ = None

    __weakref__ = None

    importColorType = 1

    importText = 'Import_'

    importTextEditor = None

    importType = 0

    notesEditor = None

    previewEditor = None


kOverwriteExplanation = []

kRename = []

kLabelColorImportExplanation = []

kLabelColorOptions = []

kLabelColorExportExplanation = []

kUnknownFile = []

kPreview = []

kDefaultTextToPrepend = 'Import_'

kTextToPrepend = []

kMerge = []

kRenderSettingsOptions = []

kLabelColorExport = []

kOverwrite = []

kLabelColorImport = []

kGeneralOptions = []

DEFAULT_UI_INDENTATION = 12

kRenderSettingsExport = []

kMergeExplanation = []

kMergeAOVExplanation = []

kNotes = []

kRenameExplanation = []

kRenderSettingsExportExplanation = []
