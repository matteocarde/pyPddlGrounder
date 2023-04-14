from __future__ import annotations

from itertools import chain
from typing import Dict, List

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Literal import Literal
from antlr4_directory.pddlParser import pddlParser
from antlr4_directory.pddlParser import pddlParser as p


class Effects:
    assignments: List[Literal or BinaryPredicate]

    def __init__(self):
        self.assignments = []
        pass

    @classmethod
    def fromNode(cls, node: pddlParser.EffectsContext) -> Effects:

        effects = cls()
        nodes: [p.EffectContext] = []

        if isinstance(node.getChild(0), p.AndEffectContext):
            nodes.extend([n.getChild(0) for n in node.getChild(0).children[2:-1]])
        else:
            nodes.append(node.getChild(0))

        for node in nodes:
            if isinstance(node, p.BooleanLiteralContext):
                effects.assignments.append(Literal.fromNode(node.getChild(0)))
            else:
                effects.assignments.append(BinaryPredicate.fromNode(node))

        return effects

    def ground(self, sub: Dict[str, str]) -> Effects:
        e = Effects()
        e.assignments = [predicate.ground(sub) for predicate in self.assignments]
        return e

    def getFunctions(self):
        return set(chain.from_iterable([c.getFunctions() for c in self.assignments if isinstance(c, BinaryPredicate)]))

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.assignments]))

    def substitute(self, sub: Dict[Atom, float], default=None):
        e = Effects()
        e.assignments = [predicate.substitute(sub, default) for predicate in self.assignments]
        return e

    def __iter__(self):
        return iter(self.assignments)

    def __str__(self):
        return str(self.assignments)

    def __repr__(self):
        return str(self.assignments)

    def __len__(self):
        return len(self.assignments)

    def toLatex(self):
        return ",".join([a.toLatex() for a in self.assignments])
        pass
