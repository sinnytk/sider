"""Functional core of Sider, a redis-like data store"""

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass(frozen=True)
class Sider:
    """Immutable structure containing the store"""

    _store: Dict[str, str] = field(default_factory=dict)  # underlying key-value store

    def get(self, key: str) -> Optional[str]:
        """Returns the value of given key if it exists, null otherwise.

        Args:
            key (str): Key to query the store against

        Returns:
            Optional[str]: Value of key, null if not found
        """
        return self._store.get(key)

    def set(self, key: str, value: str) -> "Sider":
        """Returns a new `Sider` with added/updated value.

        Args:
            key (str): Key to map against
            value (str): Value to be mapped against key

        Returns:
            Sider: Instance of Sider with key-value added
        """
        return Sider.from_dict(dict(self._store, **{key: value}))

    def unset(self, key: str) -> "Sider":
        """Returns a new `Sider` with key<>value pair removed

        Args:
            key (str): Key to remove

        Returns:
            Sider: Instance of Sider with key-value removed

        NOTE: I could've used `del` to remove the value but
        that's against "functional" programming.
        Compromise? Time complextiy becomes O(n) compared to O(1) of `del`

        """
        if key in self._store:
            return Sider.from_dict({k: v for k, v in self._store.items() if k != key})
        else:
            return self

    def value_count(self, value: str) -> int:
        """Returns the number of entries mapped to `value`.

        Args:
            value (str): Value to search occurrences of

        Returns:
            int: Number of occurrences, 0 if none found
        """

        return len([k for k, v in self._store.items() if v == value])

    @classmethod
    def from_dict(cls, old_store: dict) -> "Sider":
        """Factory method to create a Sider from existing dict.

        Main purpose to separate it from a constructor is to
        abstract out the protected `_store`

        Also to side-effects like ensuring old store is always _deep copied_
        """
        assert isinstance(old_store, dict)

        return cls(_store=deepcopy(old_store))

    @classmethod
    def from_sider(cls, old_sider: "Sider") -> "Sider":
        """Factory method to create a Sider from existing instance"""
        return cls.from_dict(old_sider._store)
