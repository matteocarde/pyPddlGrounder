from __future__ import annotations

from typing import Dict, cast

from Conditions import Conditions
from antlr4_directory.pddlParser import pddlParser


class Preconditions(Conditions):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.PreconditionsContext) -> Preconditions:
        return cast(Preconditions, super().fromNode(node))

    def ground(self, sub: Dict[str, str]) -> Preconditions:
        p = Preconditions()
        p.conditions = [predicate.ground(sub) for predicate in self.conditions]

        return p

