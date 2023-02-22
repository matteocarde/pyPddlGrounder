from __future__ import annotations

from typing import Dict, cast

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Conditions import Conditions


class Effects(Conditions):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.EffectsContext) -> Effects:
        return cast(Effects, super().fromNode(node))

    def ground(self, sub: Dict[str, str]) -> Effects:
        e = Effects()
        e.conditions = [predicate.ground(sub) for predicate in self.conditions]
        return e
