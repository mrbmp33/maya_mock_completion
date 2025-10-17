from __future__ import annotations
import sys
from qtpy import QtWidgets
from typing import Optional, TypedDict, cast
from qtpy.QtWidgets import QApplication, QMainWindow, QTreeView
from qtpy.QtCore import QAbstractItemModel, Qt, QModelIndex, QObject

from maya.mmc_hierarchy import NodePool


class TreeItemData(TypedDict):
    """TypedDict for the data stored in each tree item."""

    name: str
    uuid: str
    children: list[TreeItemData]


class TreeItem:
    """Object representing a node in the tree model.

    It stores the data in columns and keeps track of its children and parent.
    """

    def __init__(self, data: list, parent: "TreeItem" = None):
        self.item_data = data
        self.parent_item = parent
        self.children: list[TreeItem] = []
        self.extra_data: dict[str, str] = {}

    def child(self, number: int) -> "TreeItem":
        """Returns the child at the given index."""
        if number < 0 or number >= len(self.children):
            return None
        return self.children[number]

    def last_child(self) -> Optional["TreeItem"]:
        """Returns the last child of the item."""
        return self.children[-1] if self.children else None

    def child_count(self) -> int:
        """Returns the number of children."""
        return len(self.children)

    def child_number(self) -> int:
        """Returns the index of the item in its parent's children."""
        if self.parent_item:
            return self.parent_item.children.index(self)
        return 0

    def column_count(self) -> int:
        """Returns the number of columns in which the data of this object is organized."""
        return len(self.item_data)

    def data(self, column: int):
        """Returns the data stored at a given column, not ALL data"""
        if column < 0 or column >= len(self.item_data):
            return None
        return self.item_data[column]

    def insert_children(self, position: int, count: int, columns: int) -> bool:
        """Inserts *n* children at the given position.

        Parameters:
            position (int): The position at which to insert the children.
            count (int): The number of children to insert.
            columns (int): The number of columns in which the data of the children is organized.

        Returns:
            bool: True if the children were inserted successfully, False otherwise.
        """
        if position < 0 or position > len(self.children):
            return False

        for row in range(count):
            data = [None] * columns
            item = TreeItem(data.copy(), self)
            self.children.insert(position, item)

        return True

    def insert_columns(self, position: int, columns: int) -> bool:
        """Inserts *n* columns at the given position.

        Returns:
            bool: True if the columns were inserted successfully, False otherwise.
        """
        if position < 0 or position > len(self.item_data):
            return False

        for column in range(columns):
            self.item_data.insert(position, None)

        for child in self.children:
            child.insert_columns(position, columns)

        return True

    def parent(self) -> Optional["TreeItem"]:
        return self.parent_item

    def remove_children(self, position: int, count: int) -> bool:
        """Removes *n* children at the given position.

        Returns:
            bool: True if the children were removed successfully, False otherwise.
        """

        if position < 0 or position + count > len(self.children):
            return False

        for _ in range(count):
            self.children.pop(position)

        return True

    def remove_columns(self, position: int, columns: int) -> bool:
        """Removes *n* columns at the given position."""
        if position < 0 or position + columns > len(self.item_data):
            return False

        for _ in range(columns):
            self.item_data.pop(position)

        for child in self.children:
            child.remove_columns(position, columns)

        return True

    def set_data(self, column: int, value):
        """Sets the data at the given column."""

        if column < 0 or column >= len(self.item_data):
            return False

        self.item_data[column] = value
        return True

    def __repr__(self) -> str:
        result = f"<treeitem.TreeItem at 0x{id(self):x}"
        for d in self.item_data:
            result += f' "{d}"' if d else " <None>"
        result += f", {len(self.children)} children>"
        return result
    

class TreeModel(QAbstractItemModel):

    def __init__(self, headers: list, data: list[TreeItemData], parent=None):
        super().__init__(parent)

        # UUIDs are mandatory to map the items to their indexes
        if "uuid" not in headers:
            raise ValueError("UUIDs are mandatory to map the items to their indexes")

        self.headers = headers
        self.root_item = TreeItem(self.headers.copy())
        self.uuid_to_index_map: dict[str, QModelIndex] = {}

        self.setup_model_data(data, self.root_item)

    # ==== GET ITEMS AND INDEXES =========================================================

    def build_index_map(self):
        """Builds a map of UUIDs to QModelIndex(es) by traversing the whole 

        For this to be useful, the model must be populated with data first.
        """

        def recurse(item: TreeItem):
            for row, child in enumerate(item.children):
                index = self.createIndex(row, 0, child)
                self.uuid_to_index_map[self._item_uuid(child)] = index
                recurse(child)

        self.uuid_to_index_map[self._item_uuid(self.root_item)] = (
            QModelIndex()
        )  # root maps to invalid index
        recurse(self.root_item)

    def _item_uuid(self, item: TreeItem) -> str:
        """Returns the UUID of the item."""
        return item.item_data[self.headers.index("uuid")]

    def index(
        self, row: int, column: int, parent: QModelIndex = QModelIndex()
    ) -> QModelIndex:
        """Build an index for the item at the given row and column, relative to the parent
        or root."""
        if parent.isValid() and parent.column() != 0:
            return QModelIndex()

        parent_item: TreeItem = self.item_from_index(parent)
        if not parent_item:
            return QModelIndex()

        child_item: TreeItem = parent_item.child(row)
        if child_item:
            idx = self.createIndex(row, column, child_item)
            self.uuid_to_index_map[self._item_uuid(child_item)] = idx
            return idx
        return QModelIndex()

    def item_from_index(self, index: QModelIndex = QModelIndex()) -> TreeItem:
        """Returns the item at the given index."""
        if index.isValid():
            item: TreeItem = index.internalPointer()
            if item:
                return item

        return self.root_item

    def index_for_item(self, item: TreeItem) -> QModelIndex:
        """Returns the index for the given item."""
        return self.uuid_to_index_map.get(self._item_uuid(item), QModelIndex())

    # === MODEL INTERFACE ==================================================================

    def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
        return self.root_item.column_count()

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid() and parent.column() > 0:
            return 0

        parent_item: TreeItem = self.item_from_index(parent)
        if not parent_item:
            return 0
        return parent_item.child_count()

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        return Qt.ItemFlag.ItemIsEditable | QAbstractItemModel.flags(self, index)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        """Returns the header data for the given section and orientation."""
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            try:
                return self.root_item.data(section)
            except AttributeError:
                # If the section is out of range, return None
                return None

        return None

    def setHeaderData(
        self, section: int, orientation: Qt.Orientation, value, role: int = None
    ) -> bool:
        if role != Qt.ItemDataRole.EditRole or orientation != Qt.Orientation.Horizontal:
            return False

        result: bool = self.root_item.set_data(section, value)

        if result:
            self.headerDataChanged.emit(orientation, section, section)

        return result

    def __repr__(self) -> str:
        return self._repr_recursion(self.root_item)

    # === INSERT AND REMOVE ITEMS ======================================================

    def insertColumns(
        self, position: int, columns: int, parent: QModelIndex = QModelIndex()
    ) -> bool:
        self.beginInsertColumns(parent, position, position + columns - 1)
        success: bool = self.root_item.insert_columns(position, columns)
        self.endInsertColumns()

        return success

    def insertRows(
        self, position: int, rows: int, parent: QModelIndex = QModelIndex()
    ) -> bool:
        parent_item: TreeItem = self.item_from_index(parent)
        if not parent_item:
            return False

        self.beginInsertRows(parent, position, position + rows - 1)
        column_count = self.root_item.column_count()
        success: bool = parent_item.insert_children(position, rows, column_count)
        self.endInsertRows()

        return success

    def parent(self, index: QModelIndex = QModelIndex()) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()

        child_item: TreeItem = self.item_from_index(index)
        if child_item:
            parent_item: TreeItem = child_item.parent()
        else:
            parent_item = None

        if parent_item == self.root_item or not parent_item:
            return QModelIndex()

        return self.createIndex(parent_item.child_number(), 0, parent_item)

    def removeColumns(
        self, position: int, columns: int, parent: QModelIndex = QModelIndex()
    ) -> bool:
        self.beginRemoveColumns(parent, position, position + columns - 1)
        success: bool = self.root_item.remove_columns(position, columns)
        self.endRemoveColumns()

        if self.root_item.column_count() == 0:
            self.removeRows(0, self.rowCount())

        return success

    def removeRows(
        self, position: int, rows: int, parent: QModelIndex = QModelIndex()
    ) -> bool:
        parent_item: TreeItem = self.item_from_index(parent)
        if not parent_item:
            return False

        self.beginRemoveRows(parent, position, position + rows - 1)
        success: bool = parent_item.remove_children(position, rows)
        self.endRemoveRows()

        return success
    
    def data(self, index: QModelIndex, role: Qt.ItemDataRole = None):
        if not index.isValid():
            return None

        # Accept both int and Qt.ItemDataRole
        if role is None:
            role = Qt.ItemDataRole.DisplayRole

        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            item: TreeItem = index.internalPointer()
            return item.data(index.column())

        # Optionally, handle other roles if needed
        return None


    def setData(self, index: QModelIndex, value, role: int) -> bool:
        if role != Qt.ItemDataRole.EditRole:
            return False

        item: TreeItem = self.item_from_index(index)
        result: bool = item.set_data(index.column(), value)

        if result:
            self.dataChanged.emit(
                index, index, [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole]
            )

        return result

    # ==== POPULATE MODEL ========================================================================

    def setup_model_data(self, data: list[TreeItemData], parent: TreeItem):
        """Converts input data in dict format into a Tree Structure.

        Data should be formatted as a list of dictionaries, where each dictionary represents a node in the 
        The keys of the dictionary should be the column names and the values should be the data for that column.
        """
        parents = [parent]

        for d in data:
            if not isinstance(d, dict):
                RuntimeWarning(f"Item {d} is not a dictionary. Skipping.")
                continue

            # For each dictionary, create a new TreeItem and add it to the parent
            parent = parents[-1]
            self._node_dict_to_tree_item(d, parent)

        self.build_index_map()

    def _node_dict_to_tree_item(
        self, node_dict: TreeItemData, parent: TreeItem
    ) -> TreeItem:
        """Converts a dictionary to a TreeItem."""

        # Create a new TreeItem under the parent
        parent.insert_children(parent.child_count(), 1, len(self.headers))
        new_item = parent.last_child()

        # Override the data of the last child with the new data
        for key, value in node_dict.items():

            # If the key is "children", recursively create child items
            if key == "children":
                value = cast(list[TreeItemData], value)
                for child in value:
                    self._node_dict_to_tree_item(child, new_item)
                    continue

            # Only set the data if the key is in list of headers (self.root_data)
            column = self.headers.index(key) if key in self.headers else None
            if column is None:
                continue

            if column < self.root_item.column_count():
                parent.last_child().set_data(column, value)

    def _repr_recursion(self, item: TreeItem, indent: int = 0) -> str:
        result = " " * indent + repr(item) + "\n"
        for child in item.children:
            result += self._repr_recursion(child, indent + 2)
        return result

    # ==== EXPORT DATA ===========================================================================

    def export_data(self) -> list[TreeItemData]:
        """Exports the data the same format as the input data."""
        data = []

        for child in self.root_item.children:
            data.append(self._export_node_data(child))

        return data

    def _export_node_data(self, node: TreeItem) -> TreeItemData:
        """Export the data of a node. Hierarchies are traversed recursively."""
        node_data = {
            "name": node.data(self.headers.index("name")),
            "uuid": node.data(self.headers.index("uuid")),
        }
        children = []
        for child in node.children:
            children.append(self._export_node_data(child))
        node_data["children"] = children
        return node_data


def visualize_mmc():
    from maya.mmc_hierarchy import NodePool
    from maya.api import OpenMaya as om
    app = QtWidgets.QApplication([sys.argv[0]]) if not QtWidgets.QApplication.instance() else QtWidgets.QApplication.instance()

    lw = QtWidgets.QListWidget()
    for nd in NodePool.all_nodes():
        lw.addItem(f"{nd._name} | {nd._alive}")

    view = QtWidgets.QTreeView()
    def build_tree(node: om.MObject) -> TreeItemData:
        """Recursively build a TreeItemData dict from an MObject hierarchy."""
        return {
            "name": node._name,   # assuming `node.name` exists
            "uuid": node._uuid,   # assuming `node.uuid` exists
            "children": [build_tree(child) for child in node._children],
        }
    data = build_tree(om.WORLD)
    model = TreeModel(headers=["name", "uuid"], data=[data])
    view.setModel(model)
    view.expandAll()
    view.resizeColumnToContents(0)
    
    wid = QtWidgets.QWidget()
    layout = QtWidgets.QHBoxLayout(wid)

    # Embed the QListWidget and QTreeView in a layout
    layout.addWidget(view)
    layout.addWidget(lw)
    wid.resize(800, 600)
    wid.setWindowTitle("MObject Hierarchy")

    wid.show()
    if app:
        app.exec_()
