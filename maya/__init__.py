from pkgutil import extend_path
from . import mmc_selection
import os

ACTIVE_SELECTION = mmc_selection.ActiveSelection()
_ASSUME_NODES_EXIST = os.getenv("ASSUME_NODES_EXIST", "1") == "1"

stringTable = None
