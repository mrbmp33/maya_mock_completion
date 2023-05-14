import exceptions

from maya.app.renderSetup.common.devtools import *
from maya.app.renderSetup.model.selector import *
from maya.app.renderSetup.model.issue import *

if False:
    from typing import Dict, List, Tuple, Union, Optional


class Issue2016R2Collection(Issue):
    def __init__(self, resolveCallback='None'): pass


class ConversionFailed(exceptions.Exception):
    __weakref__ = None


class ConvertDialog:
    def __init__(self): pass

    def onHelp(self, *args): pass

    def onNo(self, *args): pass

    def onYes(self, *args): pass

    def prompt(self): pass


class Observer2016R2(object):
    def __init__(self): pass

    def activate(self): pass

    def assistedResolve(self): pass

    def autoResolve(self): pass

    def deactivate(self): pass

    def resolve(self): pass

    @staticmethod
    def instance(): pass

    __dict__ = None

    __weakref__ = None


def sceneHasBasicSelector(): pass


def removeAutoConvertFlag(): pass


def hasAutoConvertFlag(): pass


def _findCollections(encodedData):
    """
    yields all the collection dictionary in the encodedData
    """
    pass


def _splitOverrides(ovrs): pass


def setAutoConvertFlag(value): pass


def _createSubCollection(name, filterType, customs, children): pass


def convert2016R2(encodedData):
    """
    This is the function to call to convert any encodedData (partial or not).
    It will find all the collections in encodedData and convert them to use simpleSelector if they do not already.
    See convertCollection() for more details.
    """
    pass


def convertCollection(collection):
    """
    Convert the encoded data of a collection of 2016 R2 (using a BasicSelector) into 
    a collection with a collection using a SimpleSelector.
    Creates subcollections to simulate the old "include hierarchy".
    Creates subcollections for shader overrides since they now apply to shading engines.
    """
    pass


def getAutoConvertFlag(): pass


kConvertYes = []

kConversionCompletedOk = []

kConvertNo = []

kConvertHelp = []

kIssueShortDescription = []

kConvertBatchError = []

kConversionFailedForMessage = 'Conversion failed for collections: %s.'

kOptionVarAutoConvert = 'renderSetup_autoConvert2016R2Collections'

kConversionCompletedTitle = []

DECODE_AND_MERGE = 1

kConversionCompletedMessage = []

kConversionFailedTitle = []

kRelativeHelpLink = 'RENDER_SETUP_COMPATIBLE'

kConvertTitle = []

kConversionCompletedForMessage = 'Conversion successfully completed for collections: %s.'

kConvertMessage = []

kConversionCompletedWithErrorsMessage = []
