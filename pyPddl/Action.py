# Ciao

from __future__ import annotations
from typing import List, Dict, cast, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from MooreInterval import MooreInterval
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

        simpleIntervals: Dict[Atom, MooreInterval] = dict()
        for c in self.preconditions:
            if not isinstance(c, BinaryPredicate) or len(c.getFunctions()) > 1:
                continue
            atom = c.getFunctions().pop()
            interval = c.getIntervalFromSimpleCondition()
            if not interval:
                continue
            if atom in simpleIntervals:
                other = simpleIntervals[atom]
                simpleIntervals[atom] = other.intersecate(interval)
            else:
                simpleIntervals[atom] = interval

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

            atom = effect.getAtom()
            interval = MooreInterval()

            if atom in simpleIntervals and len(effect.rhs.getFunctions()) == 0:
                interval = simpleIntervals[atom]
                if effect.operator == "increase":
                    interval.ub = float(interval.ub + effect.rhs.toExpression())
                if effect.operator == "decrease":
                    interval.lb = float(interval.lb - effect.rhs.toExpression())

            dir_plus = interval.ub if effect.operator == "increase" else interval.lb
            dir_minus = interval.lb if effect.operator == "increase" else interval.ub

            pre_plus = self.preconditions + [effect.rhs > 0]
            pre_minus = self.preconditions + [effect.rhs < 0]

            e_plus = Supporter(self, pre_plus, SupporterEffect(atom, dir_plus))
            e_minus = Supporter(self, pre_minus, SupporterEffect(atom, dir_minus))
            supporters |= {e_plus, e_minus}

        return supporters

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        action = Action()
        action.name = self.name
        action.preconditions = self.preconditions.substitute(sub, default)
        action.effects = self.effects.substitute(sub, default)
        action.planName = self.planName
        return action
