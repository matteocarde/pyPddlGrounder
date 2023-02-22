from __future__ import annotations

from typing import Dict


class Predicate:

    def __init__(self):
        pass

    def ground(self, subs: Dict[str, str]) -> Predicate:
        raise NotImplemented("Implementation error")
