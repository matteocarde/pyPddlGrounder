from __future__ import annotations

from typing import Dict

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes import Predicate
from libs.pyGrounder.classes.BinaryPredicate import BinaryPredicate
from libs.pyGrounder.classes.Literal import Literal


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

    def __iter__(self):
        return iter(self.conditions)
