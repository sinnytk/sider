import pytest
from dataclasses import FrozenInstanceError
from core import Sider


def test_sider_is_a_store():
    assert Sider()._store == {}


def test_sider_store_is_immutable():
    sider = Sider()
    with pytest.raises(FrozenInstanceError):
        sider._store = {"2": "b", "o": "r", "2": "b"}


def test_sider_construction_with_dict():
    old_store = {"2": "b", "o": "r", "2": "b"}
    assert Sider.from_dict(old_store)._store == old_store  # value is same
    assert Sider.from_dict(old_store)._store is not old_store  # reference is different.


def test_sider_construction_with_existing_store():
    assert Sider.from_sider(
        Sider.from_dict({"2": "b", "o": "r", "2": "b"})
    ) == Sider.from_dict(
        {"2": "b", "o": "r", "2": "b"}
    )  # value is same
    assert Sider.from_sider(
        Sider.from_dict({"2": "b", "o": "r", "2": "b"})
    ) is not Sider.from_dict(
        {"2": "b", "o": "r", "2": "b"}
    )  # reference is different.


def test_sider_equivalence():
    old_store = {"2": "b", "o": "r", "2": "b"}
    assert Sider.from_dict(old_store) == Sider.from_dict(old_store)


def test_sider_get():
    old_store = {"2": "b", "o": "r", "2": "b"}
    Sider.from_dict(old_store).get("2") is "b"
    Sider.from_dict(old_store).get("o") is "r"
    Sider.from_dict(old_store).get("5") is None


def test_sider_set():
    # setting new value
    assert Sider().set("marco", "polo") == Sider.from_dict({"marco": "polo"})

    # updating existing value
    assert Sider.from_dict({"marco": "polo"}).set("marco", "polo2") == Sider.from_dict(
        {"marco": "polo2"}
    )

    # chaining works as it's functional
    assert Sider().set("marco", "polo").set("marco2", "polo2") == Sider.from_dict(
        {"marco": "polo", "marco2": "polo2"}
    )


def test_sider_unset():
    # unsetting all
    assert Sider.from_dict({"marco": "polo"}).unset("marco") == Sider()

    # unsetting one
    assert Sider.from_dict({"marco": "polo", "marco2": "polo2"}).unset(
        "marco"
    ) == Sider.from_dict({"marco2": "polo2"})

    # unsetting non-existing does nothing
    assert Sider.from_dict({"marco": "polo", "marco2": "polo2"}).unset(
        "marco3"
    ) == Sider.from_dict({"marco": "polo", "marco2": "polo2"})

    # unsetting on empty store
    assert Sider().unset("marco") == Sider()

    # chaining unsets work
    assert (
        Sider.from_dict({"marco": "polo", "marco2": "polo2"})
        .unset("marco")
        .unset("marco2")
        == Sider()
    )


def test_sider_value_count():
    assert Sider.from_dict({"a": "1", "b": "1"}).value_count("1") == 2
    assert Sider.from_dict({"a": "1", "b": "2"}).value_count("1") == 1
    assert Sider.from_dict({"a": "1", "b": "2"}).value_count("3") == 0
    assert Sider().value_count("3") == 0
