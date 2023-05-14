"""
This module is always imported during Maya's startup.  It is imported from
both the maya.app.startup.batch and maya.app.startup.gui scripts
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


def setupScriptPaths():
    """
    Add Maya-specific directories to sys.path
    """
    pass


def executeUserSetupOnly():
    """
    Look for userSetup.py in the search path and execute it in the "__main__"
    namespace
    """
    pass


def executeUserSetup(): pass


def executeSiteSetup():
    """
    Look for userSetup.py in the search path and execute it in the "__main__"
    namespace
    """
    pass


old_code = None

new_consts = ()

_runOverriddenModule_already_executed = set()

new_code = None
