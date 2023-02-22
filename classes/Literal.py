from __future__ import annotations
from typing import Dict

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes.Atom import Atom
from libs.pyGrounder.classes.Predicate import Predicate


class Literal(Predicate):
    sign: str
    atom: Atom
    var: str

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.PositiveLiteralContext or p.NegativeLiteralContext) -> Literal:
        literal = cls()

        literal.sign = "+" if isinstance(node, p.PositiveLiteralContext) else "-"
        positiveLiteralNode = node.getChild(2) if literal.sign == "-" else node
        atomNode = positiveLiteralNode.getChild(1)

        literal.atom = Atom.fromNode(atomNode)
        literal.var = literal.atom.toFunctionName()

        return literal

    def ground(self, subs: Dict[str, str]) -> Literal:

        literal = Literal()
        literal.sign = self.sign

        literal.atom = self.atom.ground(subs)
        literal.var = literal.atom.toFunctionName()

        return literal

    def __str__(self):
        if self.sign == "+":
            return f"({self.atom})"
        else:
            return f"(not ({self.atom}))"

    def __repr__(self):
        return str(self)
