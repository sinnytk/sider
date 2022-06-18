from core import Sider

def test_sider_is_a_store():
    sider = Sider()
    assert sider.store == {}
