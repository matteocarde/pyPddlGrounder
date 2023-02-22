from __future__ import annotations

from typing import Dict

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p


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
        return f"{self.name} {' '.join([a for a in self.attributes])}"

    def __repr__(self):
        return str(self)

    def toFunctionName(self):
        return f"{self.name}({''.join([a for a in self.attributes])})"

    def toAlphaFunctionName(self):
        return f"\\alpha_{{{self.name}}}({''.join([a for a in self.attributes])})"
