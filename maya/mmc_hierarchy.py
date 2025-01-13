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
    def __setitem__(cls, node: 'om.MObject'):
        cls._node_instances[hash(node._name)] = node

    @classmethod
    def __add__(cls, node: 'om.MObject'):
        cls._node_instances[hash(node._name)] = node

    @classmethod
    def add_object(cls, node: 'om.MObject'):
        cls.__add__(node)

    @classmethod
    def __getitem__(cls, node: 'om.MObject') -> 'om.MObject':
        return cls._node_instances[hash(node._name)]

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
        return cls.__contains__(node)

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
    """Registers a node from its MObject into the node pool and builds the hierarchy"""

    # Put inside pool
    NodePool.add_object(node)


def deregister(node: 'om.MObject'):
    """Removes a node from the registry and hierarchy"""
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

        if not as_node._parent:
            ...
        elif NodePool.from_name(name)._parent._name != parent_name:
            base_name = f'{parent_name or ""}|{base_name}'
            name = base_name

    while NodePool.hash_exists(hash(name)):
        name = f'{base_name}{idx}'
        idx += 1
    return name
