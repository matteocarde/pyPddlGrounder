from typing import Dict, Set

from Atom import Atom
from MooreInterval import MooreInterval
from Supporter import Supporter


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
        state.__intervals = self.__intervals

        for supporter in activeSupporters:
            atom = supporter.effect.atom
            state.__intervals[atom] = state.__intervals[atom].getExtended(supporter.effect)

        return state
