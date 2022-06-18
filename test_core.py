import pytest
from dataclasses import FrozenInstanceError
from core import Sider

def test_sider_is_a_store():
    sider = Sider()
    assert sider.store == {}

def test_sider_store_is_immutable():
    sider = Sider()
    assert sider.store == {}
    with pytest.raises(FrozenInstanceError):
        sider.store = {'2': 'b','o':'r', '2': 'b'}