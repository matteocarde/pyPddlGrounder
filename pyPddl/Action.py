# Ciao

from __future__ import annotations
from typing import List, Dict, cast, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from Supporter import Supporter, SupporterEffect
from antlr4_directory.pddlParser import pddlParser as p
from Operation import Operation
from OperationType import OperationType
from Type import Type


class Action(Operation):

    def __init__(self):
        self.isFake = False
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.ActionContext):
        return super().fromNode(node)

    @property
    def type(self):
        return OperationType.ACTION

    def ground(self, problem) -> List[Action]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            action = Action()
            action.name = op.name
            action.preconditions = op.preconditions
            action.effects = op.effects
            action.planName = op.planName
            groundOps.append(action)
        return groundOps

    def getSupporters(self) -> Set[Supporter]:
        supporters: Set[Supporter] = set()

        for effect in self.effects:
            if not isinstance(effect, BinaryPredicate):
                continue
            if effect.operator == "assign" and isinstance(effect.rhs, Constant):
                s = Supporter(self, self.preconditions, SupporterEffect(effect.lhs.getAtom(), effect.rhs.value))
                supporters.add(s)
                continue

            # Additive Effects Transformation
            if effect.operator == "assign" and isinstance(effect.rhs, BinaryPredicate):
                effect = BinaryPredicate.additiveEffectsTransformation(effect)

            dir_plus = float("+inf") if effect.operator == "increase" else float("-inf")
            dir_minus = float("-inf") if effect.operator == "increase" else float("+inf")

            pre_plus = self.preconditions + [effect.rhs > 0]
            pre_minus = self.preconditions + [effect.rhs < 0]

            e_plus = Supporter(self, pre_plus, SupporterEffect(effect.lhs.getAtom(), dir_plus))
            e_minus = Supporter(self, pre_minus, SupporterEffect(effect.lhs.getAtom(), dir_minus))
            supporters |= {e_plus, e_minus}

        return supporters

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        action = Action()
        action.name = self.name
        action.preconditions = self.preconditions.substitute(sub, default)
        action.effects = self.effects.substitute(sub, default)
        action.planName = self.planName
        return action
