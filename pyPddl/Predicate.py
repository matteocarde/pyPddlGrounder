from __future__ import annotations

from typing import Dict, Set

from Atom import Atom


class Predicate:

    def __init__(self):
        pass

    def ground(self, subs: Dict[str, str]) -> Predicate:
        raise NotImplemented()

    def getAtom(self) -> Atom:
        raise NotImplemented()

    def getPredicates(self) -> Set[Atom]:
        raise NotImplemented()

    def getFunctions(self) -> Set[Atom]:
        raise NotImplemented()

    def __eq__(self, other):
        if not isinstance(other, Predicate):
            return False
        return str(other) == str(self)

    def __hash__(self):
        return hash(str(self))
