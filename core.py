"""Functional core of Sider, a redis-like data store"""

from dataclasses import dataclass, field
from typing import Dict

@dataclass(frozen=True)
class Sider:
    """Immutable structure containing the store"""
    _store: Dict[str, str] = field(default_factory=dict) # underlying key-value store
