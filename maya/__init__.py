from . import mmc_selection
import os
import json

ACTIVE_SELECTION = mmc_selection.ActiveSelection()
ASSUME_NODES_EXIST = json.loads(os.getenv("ASSUME_NODES_EXIST", "true"))
IMPORT_MESH_DATA = json.loads(os.getenv("IMPORT_MESH_DATA", "true"))

stringTable = None
