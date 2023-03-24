from __future__ import annotations

from typing import Dict, Set

from antlr4 import InputStream, CommonTokenStream
from sympy import Expr, Symbol

from Constant import Constant
from antlr4_directory.pddlLexer import pddlLexer
from antlr4_directory.pddlParser import pddlParser as p, pddlParser
from Atom import Atom
from Predicate import Predicate


class Literal(Predicate):
    sign: str
    atom: Atom
    funct: str

    def __init__(self):
        super().__init__()

    @classmethod
    def fromAtom(cls, atom: Atom, sign: str):
        lit = cls()
        lit.atom = atom
        lit.sign = sign
        return lit

    @classmethod
    def fromNode(cls, node: p.PositiveLiteralContext or p.NegativeLiteralContext) -> Literal:
        literal = cls()

        literal.sign = "+" if isinstance(node, p.PositiveLiteralContext) else "-"
        positiveLiteralNode = node.getChild(2) if literal.sign == "-" else node
        atomNode = positiveLiteralNode.getChild(1)

        literal.atom = Atom.fromNode(atomNode)
        literal.string = f"({literal.atom})"
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    def getPredicates(self) -> Set[Atom]:
        return {self.atom}

    def getFunctions(self) -> Set[Atom]:
        return {self.atom}

    def getAtom(self) -> Atom:
        return self.atom

    def ground(self, subs: Dict[str, str]) -> Literal:

        literal = Literal()
        literal.sign = self.sign

        literal.atom = self.atom.ground(subs)
        literal.funct = literal.atom.toFunctionName()
        literal.alphaFunct = literal.atom.toAlphaFunctionName()

        return literal

    def __str__(self):
        if self.sign == "+":
            return f"({self.atom})"
        else:
            return f"(not ({self.atom}))"

    def __repr__(self):
        return str(self)

    @classmethod
    def fromString(cls, string: str) -> Literal:
        lexer = pddlLexer(InputStream(string))
        token_stream = CommonTokenStream(lexer)
        node = pddlParser(token_stream).positiveLiteral()
        return cls.fromNode(node)

    def __hash__(self):
        return hash(self.sign + str(self.atom))

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        if self.atom not in subs and default is None:
            return self
        if self.atom not in subs and default is not None:
            c = Constant()
            c.value = default
            return c
        if self.atom in subs:
            c = Constant()
            c.value = subs[self.atom]
            return c

    def getLinearIncrement(self) -> float:
        return 0

    def toExpression(self) -> Expr:
        return self.atom.toExpression()
