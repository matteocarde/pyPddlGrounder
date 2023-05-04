# Ciao

from __future__ import annotations

from typing import List, Dict, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from MooreInterval import MooreInterval
from Operation import Operation
from OperationType import OperationType
from Supporter import Supporter, SupporterEffect
from Utilities import Utilities
from antlr4_directory.pddlParser import pddlParser as p


class Action(Operation):

    def __init__(self):
        self.isFake = False
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.ActionContext):
        return super().fromNode(node)

    @classmethod
    def fromProperties(cls, name, preconditions, effects, planName):
        return super().fromProperties(name, preconditions, effects, planName)

    @classmethod
    def fromString(cls, string: str) -> Action:
        return cls.fromNode(Utilities.getParseTree(string).action())

    @property
    def type(self):
        return OperationType.ACTION

    def ground(self, problem) -> List[Action]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            name = op.name
            preconditions = op.preconditions
            effects = op.effects
            planName = op.planName
            action = Action.fromProperties(name, preconditions, effects, planName)
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
            if effect.operator == "assign":
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

            if not isinstance(effect.rhs, Constant) or effect.rhs.value > 0:
                pre_plus = self.preconditions + [effect.rhs > 0]
                e_plus = Supporter(self, pre_plus, SupporterEffect(atom, dir_plus))
                supporters.add(e_plus)

            if not isinstance(effect.rhs, Constant) or effect.rhs.value < 0:
                pre_minus = self.preconditions + [effect.rhs < 0]
                e_minus = Supporter(self, pre_minus, SupporterEffect(atom, dir_minus))
                supporters.add(e_minus)

        return supporters

    def substitute(self, sub: Dict[Atom, float], default=None) -> Action:
        name = self.name
        preconditions = self.preconditions.substitute(sub, default)
        effects = self.effects.substitute(sub, default)
        planName = self.planName
        action = Action.fromProperties(name, preconditions, effects, planName)
        return action
