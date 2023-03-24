from __future__ import annotations

from typing import Dict

from sympy import Symbol, Expr

from antlr4_directory.pddlParser import pddlParser as p


class Atom:
    name: str
    attributes: list[str]

    def __init__(self):
        self.attributes = []
        pass

    @classmethod
    def fromNode(cls, node: p.AtomContext) -> Atom:
        atom = cls()
        atom.name = node.getChild(0).getText()
        node: p.GroundAtomParameterContext or p.LiftedAtomParameterContext
        for attr in node.children[1:]:
            atom.attributes.append(attr.getText())
        return atom

    def ground(self, subs: Dict[str, str]) -> Atom:
        atom = Atom()
        atom.name = self.name
        atom.attributes = [subs[attr] for attr in self.attributes]
        return atom

    def __str__(self):
        parts = [self.name] + [a for a in self.attributes]
        return " ".join(parts)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: Atom):
        if not isinstance(other, Atom):
            return False
        return str(self) == str(other)

    def toFunctionName(self):
        parameters = ','.join([a for a in self.attributes])
        parenthesis = f"({parameters})" if self.attributes else ""
        return f"{self.name}{parenthesis}"

    def toAlphaFunctionName(self):
        parameters = ','.join([a for a in self.attributes])
        parenthesis = f"({parameters})" if self.attributes else ""
        return f"\\alpha_{{{self.name}}}{parenthesis}"

    def toExpression(self) -> Expr:
        return Symbol(self.toFunctionName())
