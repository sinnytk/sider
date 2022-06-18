import pytest
from dataclasses import FrozenInstanceError
from core import Sider


def test_sider_is_a_store():
    assert Sider()._store == {}


def test_sider_store_is_immutable():
    sider = Sider()
    with pytest.raises(FrozenInstanceError):
        sider._store = {"2": "b", "o": "r", "2": "b"}


def test_sider_construction_with_existing_store():
    old_store = {"2": "b", "o": "r", "2": "b"}
    assert Sider.from_dict(old_store)._store == old_store  # value is same
    assert Sider.from_dict(old_store)._store is not old_store  # reference is different.


def test_sider_equivalence():
    old_store = {"2": "b", "o": "r", "2": "b"}
    assert Sider.from_dict(old_store) == Sider.from_dict(old_store)


def test_sider_get():
    old_store = {"2": "b", "o": "r", "2": "b"}
    Sider.from_dict(old_store).get("2") is "b"
    Sider.from_dict(old_store).get("o") is "r"
    Sider.from_dict(old_store).get("5") is None
