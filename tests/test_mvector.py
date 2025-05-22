import pytest
import numpy as np
from maya.api.OpenMaya import MVector

def test_init_from_args():
    v = MVector(1, 2, 3)
    assert np.allclose(list(v), [1, 2, 3])

def test_init_from_list():
    v = MVector([4, 5, 6])
    assert np.allclose(list(v), [4, 5, 6])

def test_init_from_mvector():
    v1 = MVector(7, 8, 9)
    v2 = MVector(v1)
    assert np.allclose(list(v2), [7, 8, 9])

def test_addition():
    v1 = MVector(1, 2, 3)
    v2 = MVector(4, 5, 6)
    v3 = v1 + v2
    assert np.allclose(list(v3), [5, 7, 9])

def test_subtraction():
    v1 = MVector(5, 7, 9)
    v2 = MVector(1, 2, 3)
    v3 = v1 - v2
    assert np.allclose(list(v3), [4, 5, 6])

def test_scalar_multiplication():
    v = MVector(1, 2, 3)
    v2 = v * 2
    assert np.allclose(list(v2), [2, 4, 6])

def test_dot_product():
    v1 = MVector(1, 2, 3)
    v2 = MVector(4, 5, 6)
    dot = v1 * v2
    assert np.isclose(dot, 32)

def test_cross_product():
    v1 = MVector(1, 0, 0)
    v2 = MVector(0, 1, 0)
    v3 = v1 ^ v2
    assert np.allclose(list(v3), [0, 0, 1])

def test_length():
    v = MVector(3, 4)
    assert np.isclose(v.length(), 5)

def test_angle():
    v1 = MVector(1, 0)
    v2 = MVector(0, 1)
    angle = v1.angle(v2)
    assert np.isclose(angle, np.pi / 2)

def test_normalize():
    v = MVector(3, 0, 4)
    v.normalize()
    assert np.allclose(np.linalg.norm(list(v)), 1.0)

def test_normal():
    v = MVector(0, 0, 5)
    n = v.normal()
    assert np.allclose(list(n), [0, 0, 1])

def test_is_equivalent():
    v1 = MVector(1, 2, 3)
    v2 = MVector(1 + 1e-11, 2, 3)
    assert v1.isEquivalent(v2)

def test_is_parallel():
    v1 = MVector(1, 2, 3)
    v2 = MVector(2, 4, 6)
    assert v1.isParallel(v2)

def test_get_set_item():
    v = MVector(1, 2, 3)
    v[0] = 10
    assert v[0] == 10

def test_del_item():
    v = MVector(1, 2, 3)
    del v[1]
    assert v[1] == 0.0

def test_properties():
    v = MVector(1, 2, 3)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3
    v.x = 4
    v.y = 5
    v.z = 6
    assert np.allclose(list(v), [4, 5, 6])

def test_repr_and_str():
    v = MVector(1, 2, 3)
    assert "MVector" in repr(v)
    assert str(v).startswith("(")