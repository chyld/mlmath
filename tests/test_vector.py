# python -m pytest -v --cov

from mlmath.vector import Vector

import pytest


@pytest.fixture
def vector():
    return Vector(1, 3)


def test_create_instance():
    v = Vector()
    assert isinstance(v, Vector)


def test_constructor():
    v = Vector(3, 4)
    assert v.elements == (3, 4)


def test_scale(vector):
    v2 = vector.scale(3)
    assert v2.elements == (3, 9)


def test_norm(vector):
    assert vector.norm() == pytest.approx(3.16, rel=1e-2)


def test_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert v3.elements == (4, 6)
