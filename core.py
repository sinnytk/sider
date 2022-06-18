"""Functional core of Sider, a redis-like data store"""

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict

@dataclass(frozen=True)
class Sider:
    """Immutable structure containing the store"""
    _store: Dict[str, str] = field(default_factory=dict) # underlying key-value store

    @classmethod
    def from_dict(cls, old_store: dict) -> "Sider":
        """Factory method to create a Sider from existing dict.

        Main purpose to separate it from a constructor is to
        abstract out the protected `_store`

        Also to side-effects like ensuring old store is always _deep copied_
        """
        return cls(_store=deepcopy(old_store))
    
