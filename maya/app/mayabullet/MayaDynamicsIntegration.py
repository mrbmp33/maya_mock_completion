"""
MayaDynamicsIntegration - integration with the user interface for Maya's 
                          built-in Dynamics such as supporting Maya's fields
"""

from collections import defaultdict

if False:
    from typing import Dict, List, Tuple, Union, Optional


def collectBulletObjects(objects):
    """
    Take the list of objects and find all Bullet shapes associated with them.
    
    In this case we are interested in shapes that can be affected by fields.
    """
    pass


def solverForShape(shape):
    """
    Get the solver for the given bullet shape
    """
    pass


def deleteConnections(bullet_shapes, fields):
    """
    Delete all of the connections between the given fields and bullet shapes
    """
    pass


def addDynamicConnectHook(): pass


def removeDynamicConnectHook(): pass


def disconnectFieldFromShape(field, shape):
    """
    Disconnect the given field from the given bullet shape
    """
    pass


def makeConnections(bullet_shapes, fields):
    """
    Make all of the required connections
    """
    pass


def connectDynamicCB(fields, emitters, collisionObjects, objects, delete):
    """
    This is the callback that gets called when the 'connectDynamic' command
    is called. This callback looks for bullet shapes in the objects and 
    takes over if it finds some.
    """
    pass


def connectFieldToShape(field, shape):
    """
    Connect the given field to the given bullet shape
    """
    pass


def findExisitingConnections(objects):
    """
    In the case where we connect a field to a solver, we need to check if that
    field is already connected to any objects being handled by that solver. So, if
    we need to break those direct connections to prevent the field from affecting
    the same object twice. So, here we iterate over any solver objects and 
    build up a list of the objects they are solving and the fields that they are
    connected to.
    
    This function returns a tuple of:
    - solvers->fields->shapes the fields are connected to
    - solvers->connected fields
    
    We build these lists because, for large operations, it is more efficient
    """
    pass


strVersion = []

aVersion = []

kBulletSoftBodyShapeType = 'bulletSoftBodyShape'

kBulletSolverShapeType = 'bulletSolverShape'

connectDynamicCB_ID = None

gMayaVersion = 2019.0

kBulletRigidBodyShapeType = 'bulletRigidBodyShape'
