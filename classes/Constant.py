from __future__ import annotations

from typing import Dict

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Predicate import Predicate


class Constant(Predicate):
    value: float
    isDelta: bool

    def __init__(self):
        super().__init__()
        self.value = 0
        self.isDelta = False

    @classmethod
    def fromNode(cls, node: pddlParser.ConstantContext or pddlParser.NumberContext) -> Constant:

        constant = cls()
        constant.isDelta = False
        if isinstance(node, pddlParser.NumberContext):
            constant.value = float(node.getText())
            return constant

        child = node.getChild(0)
        if isinstance(child, pddlParser.NumberContext):
            constant.value = float(child.getText())
        elif isinstance(child, pddlParser.DeltaContext):
            constant.isDelta = True

        return constant

    def ground(self, subs: Dict[str, str]) -> Constant:
        constant = Constant()
        constant.value = self.value
        constant.isDelta = self.isDelta

        return constant

    def __str__(self):
        return "#t" if self.isDelta else str(self.value)

    def __repr__(self):
        return str(self)
