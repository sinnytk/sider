"""Functional core of Sider, a redis-like data store"""

from dataclasses import dataclass, field
from typing import Dict

@dataclass(frozen=True)
class Sider:
    """Immutable structure containing the store"""
    store: Dict[str, str] = field(default_factory=dict) # key-value store
