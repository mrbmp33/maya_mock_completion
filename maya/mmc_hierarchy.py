"""Mapping of all nodes inside MMC."""
import typing
import uuid

# FKS modules
if typing.TYPE_CHECKING:
    import maya.api.OpenMaya as om


# noinspection PyProtectedMember
class NodePoolMeta(type):
    """Store all instances of node mobjects in a dictionary UUID : MObject."""

    _node_instances: typing.MutableMapping[uuid.UUID, 'om.MObject'] = {}

    @classmethod
    def __setitem__(cls, node: 'om.MObject'):
        cls._node_instances[node._uuid._uuid] = node

    @classmethod
    def __add__(cls, node: 'om.MObject'):
        cls._node_instances[node._uuid._uuid] = node

    @classmethod
    def add_object(cls, node: 'om.MObject'):
        cls.__add__(node)

    @classmethod
    def __getitem__(cls, node: 'om.MObject') -> 'om.MObject':
        return cls._node_instances[node._uuid._uuid]

    @classmethod
    def get_node(cls, node: 'om.MObject') -> 'om.MObject':
        return cls.__getitem__(node)

    @classmethod
    def __delitem__(cls, node: 'om.MObject'):
        del cls._node_instances[node._uuid._uuid]

    @classmethod
    def remove_object(cls, node: 'om.MObject'):
        cls._node_instances.pop(node._uuid._uuid, None)

    @classmethod
    def __contains__(cls, node):
        return node._uuid._uuid in cls._node_instances

    @classmethod
    def object_exists(cls, node: 'om.MObject') -> bool:
        return cls.__contains__(node)

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
