from typing import Dict, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Conditions import Conditions
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

    @classmethod
    def fromInitialCondition(cls, init):
        ris = cls()
        for (literal, value) in init.numericAssignments.items():
            ris.__intervals[literal.getAtom()] = MooreInterval(value, value)

        return ris

    def getAtom(self, atom: Atom) -> MooreInterval:
        return self.__intervals[atom]

    def __repr__(self):
        return repr(self.__intervals)

    def applySupporters(self, activeSupporters: Set[Supporter]):

        state = RelaxedIntervalState()
        state.__intervals = self.__intervals.copy()

        for supporter in activeSupporters:
            atom = supporter.effect.atom
            state.__intervals[atom] = state.__intervals[atom].getExtended(supporter.effect)

        return state

    def satisfies(self, c: Conditions) -> bool:
        satisfied = True
        for pre in c.conditions:
            if not self.satisfiesPredicate(pre):
                return False

        return satisfied

    def satisfiesPredicate(self, p: Predicate):

        if isinstance(p, Literal) or not isinstance(p, BinaryPredicate):
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
