from __future__ import annotations

from typing import Dict, Set

from Atom import Atom
from MooreInterval import MooreInterval
from Utilities import Utilities


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

    def __operation(self, other, operator: str):
        from BinaryPredicate import BinaryPredicate, BinaryPredicateType
        from Constant import Constant
        op = BinaryPredicate()
        op.lhs = self
        op.rhs = Constant.fromValue(other) if isinstance(other, float) or isinstance(other, int) else other
        op.operator = operator
        if operator in {"+", "-", "*", "/"}:
            op.type = BinaryPredicateType.OPERATION
        if operator in {">", ">=", "<=", "<", "="}:
            op.type = BinaryPredicateType.COMPARATION
        return op

    def __sub__(self, other):
        return self.__operation(other, "-")

    def __gt__(self, other):
        return self.__operation(other, ">")

    def __lt__(self, other):
        return self.__operation(other, "<")

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        raise NotImplemented()

    def getLinearIncrement(self) -> float:
        raise NotImplemented
