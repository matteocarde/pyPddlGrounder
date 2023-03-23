from typing import Dict, Set

from Action import Action
from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Formula import Formula
from Constant import Constant
from InitialCondition import InitialCondition
from Literal import Literal
from MooreInterval import MooreInterval
from Predicate import Predicate
from Supporter import Supporter
from Utilities import Utilities


class State:
    __assignments: Dict[Atom, bool or float]

    def __init__(self):
        self.__assignments = dict()

    @classmethod
    def fromInitialCondition(cls, init: InitialCondition):
        state = cls()

        assignment: Predicate
        for assignment in init.assignment:
            atom = assignment.getAtom()
            state.__assignments[atom] = state.getRealization(assignment)

        return state

    def getAtom(self, atom: Atom) -> MooreInterval:
        return self.__assignments[atom]

    def __repr__(self):
        return repr(self.__assignments)

    def applyAction(self, action: Action):

        state = State()
        state.__assignments = self.__assignments.copy()

        effect: Predicate
        for effect in action.effects:
            state.__assignments[effect.getAtom()] = self.getRealization(effect)

        return state

    def satisfies(self, c: Formula) -> bool:
        satisfied = True
        for pre in c.conditions:
            if not self.satisfiesPredicate(pre):
                return False

        return satisfied

    def satisfiesPredicate(self, p: Predicate):
        if isinstance(p, Literal):
            return p.sign == "+" and p.getAtom() in self.__assignments and self.__assignments[p.getAtom()] is True

        if not isinstance(p, BinaryPredicate):
            raise "Precondition can only be BinaryPredicate or Literal"

        if p.operator not in {">=", ">", "<=", "<", "="}:
            raise Exception(f"Cannot check satisfaction for precondition with operator '{p.operator}'")

        function: BinaryPredicate = p.lhs - p.rhs
        result = self.substituteInto(function)

        return Utilities.compare(p.operator, result, 0)

    def getRealization(self, p: Predicate):
        if isinstance(p, Literal):
            return True if p.sign == "+" else False
        if isinstance(p, BinaryPredicate):
            if p.operator not in {"=", "assign", "increase", "decrease"}:
                raise Exception(f"Operator {p.operator} not allowed in effects")

            lhs = self.substituteInto(p.rhs)
            if p.operator == "assign" or p.operator == "=":
                return lhs
            if p.operator == "increase":
                return self.__assignments[p.getAtom()] + lhs
            if p.operator == "decrease":
                return self.__assignments[p.getAtom()] - lhs

    def substituteInto(self, p: Predicate) -> bool or float:
        if isinstance(p, Constant):
            return p.value
        if isinstance(p, Literal):
            return self.__assignments[p.getAtom()]
        if isinstance(p, BinaryPredicate):
            lhs = self.substituteInto(p.lhs)
            rhs = self.substituteInto(p.rhs)
            return Utilities.op(p.operator, lhs, rhs)
