from __future__ import annotations

from itertools import chain
from typing import Dict

from BinaryPredicate import BinaryPredicate
from Literal import Literal
from Predicate import Predicate
from antlr4_directory.pddlParser import pddlParser as p


class Conditions:
    conditions: [Predicate]

    def __init__(self):
        self.conditions = list()

    @classmethod
    def fromNode(cls, node: p.PreconditionsContext or p.EffectContext) -> Conditions:
        conditions = cls()
        nodes: [p.PreconditionContext] = []
        if isinstance(node.getChild(0), p.AndPreconditionContext) or isinstance(node.getChild(0), p.AndEffectContext):
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        elif isinstance(node.getChild(0), p.EmptyPreconditionContext):
            return conditions
        else:
            nodes.append(node.getChild(0))

        for node in nodes:
            if isinstance(node, p.BooleanLiteralContext):
                conditions.conditions.append(Literal.fromNode(node.getChild(0)))
            else:
                conditions.conditions.append(BinaryPredicate.fromNode(node))

        return conditions

    def ground(self, subs: Dict[str, str]):
        raise NotImplemented()

    def getFunctions(self):
        return set(chain.from_iterable([c.getFunctions() for c in self.conditions if isinstance(c, BinaryPredicate)]))

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.conditions]))

    def __iter__(self):
        return iter(self.conditions)

    def __str__(self):
        return str(self.conditions)

    def __repr__(self):
        return str(self.conditions)

    def __add__(self, other):
        c = Conditions()
        c.conditions = self.conditions + other
        return c

