"""Mapping of all nodes inside MMC."""
import typing
import re

# FKS modules
if typing.TYPE_CHECKING:
    import maya.api.OpenMaya as om


# noinspection PyProtectedMember
class NodePoolMeta(type):
    """Store all instances of node mobjects in a dictionary UUID : MObject."""

    _node_instances: typing.MutableMapping[int, 'om.MObject'] = {}

    @classmethod
    def __setitem__(cls, node: 'om.MObject', use_path: bool = False):
        if use_path:
            cls._node_instances[hash(node._path_str())] = node
        cls._node_instances[hash(node._name)] = node

    @classmethod
    def __add__(cls, node: 'om.MObject', use_path: bool = False):
        if use_path:
            cls._node_instances[hash(node._path_str())] = node
        cls._node_instances[hash(node._name)] = node

    @classmethod
    def add_object(cls, node: 'om.MObject', use_path: bool = False):
        cls.__add__(node, use_path=use_path)

    @classmethod
    def __getitem__(cls, node: 'om.MObject') -> 'om.MObject':
        return cls._node_instances.get(
            hash(node._name),
            cls._node_instances.get(hash(node._path_str()))
        )

    @classmethod
    def get_node(cls, node: 'om.MObject') -> 'om.MObject':
        return cls.__getitem__(node)

    @classmethod
    def __delitem__(cls, node: 'om.MObject'):
        del cls._node_instances[hash(node._name)]

    @classmethod
    def remove_object(cls, node: 'om.MObject'):
        cls._node_instances.pop(hash(node._name), None)

    @classmethod
    def __contains__(cls, node):
        return hash(node._name) in cls._node_instances

    @classmethod
    def object_exists(cls, node: 'om.MObject') -> bool:
        # if not hasattr(node, '_name'):
        #     print(f"Node {node} has no attribute '_name'")
        #     print(cls.all_nodes())
        #     print(node)
        #     raise AttributeError

        nd = cls._node_instances.get(
            hash(node._name),
            cls._node_instances.get(hash(node._path_str()))
        )
        if nd is None:
            return False
        return True

    @classmethod
    def hash_exists(cls, hash_num: int) -> bool:
        return hash_num in cls._node_instances

    @classmethod
    def from_name(cls, name: str) -> 'om.MObject':
        return cls._node_instances.get(hash(name))

    @classmethod
    def reset(cls):
        """Empties the pool of all current instances."""
        cls._node_instances = {}

    @classmethod
    def all_nodes(cls):
        return cls._node_instances.values()


class NodePool(metaclass=NodePoolMeta):
    ...


# noinspection PyProtectedMember
def register(node: 'om.MObject'):
    """Registers a node from its MObject into the node pool and builds the hierarchy.
    
    Looks first for possible matches in the pool. If a match is found, it will compare the paths
    of the nodes. If paths are different, it will use full path as key.
    """

    # If not in the pool, add it normally. Fast return
    if not NodePool.object_exists(node):
        NodePool.add_object(node)
        return

    old_node = NodePool.get_node(node)
    old_path = old_node._path_str()
    new_path = node._path_str()

    # Check if the paths are the same
    if old_path == new_path:
        if old_node._uuid == node._uuid:  # same node
            return
        else:  # same path, different node
            raise ValueError(f"Node with same path already exists in the pool: {old_node._name}")

    # If the paths are different, use the full path as key
    else:
        # Remove the old node from the pool and add both using the full path as key
        NodePool.remove_object(old_node)
        NodePool.add_object(node, use_path=True)
        NodePool.add_object(old_node, use_path=True)


def deregister(node: 'om.MObject'):
    """Removes a node from the registry and hierarchy"""
    if NodePool.object_exists(node):
        NodePool.remove_object(node)
    else:
        # Try to get the node by its path
        if NodePool.hash_exists(hash(node._path_str())):
            NodePool.remove_object(node)


def find_first_available_name(name: str, parent_name: str = None) -> str:
    # Check if the name ends with a number
    match = re.match(r"^(.*?)(\d+)$", name)
    if match:
        # Extract the base name and starting number
        base_name = match.group(1)
        idx = int(match.group(2))
    else:
        # No number at the end of the name
        base_name = name
        idx = 1

    if NodePool.hash_exists(hash(name)):

        as_node = NodePool.from_name(name)

        if as_node._parent is None:
            ...
        elif as_node._parent.apiTypeStr == 'kWorld':
            ...
        elif NodePool.from_name(name)._parent._name != parent_name:
            base_name = f'{parent_name or ""}|{base_name}'
            name = base_name

    while NodePool.hash_exists(hash(name)):
        name = f'{base_name}{idx}'
        idx += 1
    return name
