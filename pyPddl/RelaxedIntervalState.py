from typing import Dict, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Formula import Formula
from Constant import Constant
from Literal import Literal
from MooreInterval import MooreInterval
from Predicate import Predicate
from Supporter import Supporter
from Utilities import Utilities


class RelaxedIntervalState:
    __intervals: Dict[Atom, MooreInterval]

    def __init__(self):
        self.__intervals = dict()

    def __repr__(self):
        return repr(self.__intervals)

    def __iter__(self):
        return iter(self.__intervals)

    @property
    def intervals(self) -> Dict[Atom, MooreInterval]:
        return self.__intervals

    @classmethod
    def fromInitialCondition(cls, init):
        ris = cls()
        for (atom, value) in init.numericAssignments.items():
            ris.__intervals[atom] = MooreInterval(value, value)

        return ris

    def getAtom(self, atom: Atom) -> MooreInterval:
        # if not atom in self.__intervals:
        #     print(f"WARNING: The fluent {atom} was not initialized. Setting it to 0")
        #     return MooreInterval(0, 0)
        return self.__intervals[atom]

    def applySupporters(self, activeSupporters: Set[Supporter]):

        state = RelaxedIntervalState()
        state.__intervals = self.__intervals.copy()

        for supporter in activeSupporters:
            atom = supporter.effect.atom
            state.__intervals[atom] = state.__intervals[atom].getExtended(supporter.effect)

        return state

    def __satisfiesAnd(self, formula: Formula):
        satisfied = True
        for c in formula.conditions:
            if isinstance(c, Predicate) and not self.satisfiesPredicate(c):
                return False
            if isinstance(c, Formula) and c.type == "AND" and not self.__satisfiesAnd(c):
                return False
            if isinstance(c, Formula) and c.type == "OR" and not self.__satisfiesOr(c):
                return False

        return satisfied

    def __satisfiesOr(self, formula: Formula):
        satisfied = False
        for c in formula.conditions:
            if isinstance(c, Predicate) and self.satisfiesPredicate(c):
                return True
            if isinstance(c, Formula) and c.type == "AND" and self.__satisfiesAnd(c):
                return True
            if isinstance(c, Formula) and c.type == "OR" and self.__satisfiesOr(c):
                return True

        return satisfied

    def satisfies(self, c: Formula) -> bool:
        return self.__satisfiesAnd(c) if c.type == "AND" else self.__satisfiesOr(c)

    def satisfiesPredicate(self, p: Predicate):

        if isinstance(p, Literal) or not isinstance(p, BinaryPredicate):
            return True

        if p.operator == "!=":
            return True

        if p.operator not in {">=", ">", "<=", "<", "="}:
            raise Exception(f"Cannot check satisfaction for precondition with operator '{p.operator}'")

        function: BinaryPredicate = p.lhs - p.rhs
        interval: MooreInterval = self.substituteInto(function)

        return interval.exists(p.operator, 0)

    def substituteInto(self, p: Predicate) -> MooreInterval:
        if isinstance(p, Constant):
            return MooreInterval(p.value, p.value)
        if isinstance(p, Literal):
            return self.getAtom(p.getAtom())
        if isinstance(p, BinaryPredicate):
            lhs = self.substituteInto(p.lhs)
            rhs = self.substituteInto(p.rhs)
            return Utilities.op(p.operator, lhs, rhs)
