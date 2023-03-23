from __future__ import annotations

from enum import Enum
from typing import Dict, Set, List

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from Literal import Literal
from MooreInterval import MooreInterval
from Predicate import Predicate
from antlr4_directory.pddlParser import pddlParser as p


class ListPredicate(Predicate):
    operator: str
    list: List[Predicate]

    def __init__(self):
        super().__init__()
        self.__functions = None

    @classmethod
    def fromNode(cls, node: p.OrClauseContext or p.AndClauseContext) -> BinaryPredicate:
        if not isinstance(node, p.OrClauseContext) or not isinstance(node, p.AndClauseContext):
            raise Exception("Expected OR or AND")

        lp = cls()

        return bp

    @staticmethod
    def __assignClass(node: p.OperationSideContext):
        child = node.getChild(0)
        if isinstance(child, p.OperationContext):
            return BinaryPredicate.fromNode(child)
        elif isinstance(child, p.PositiveLiteralContext):
            return Literal.fromNode(child)
        elif isinstance(child, p.ConstantContext):
            return Constant.fromNode(child)
        elif isinstance(child, p.NumberContext):
            return Constant.fromNode(child)
        else:
            raise NotImplemented()

    def ground(self, subs: Dict[str, str]) -> BinaryPredicate:
        bp = BinaryPredicate()
        bp.operator = self.operator
        bp.lhs = self.lhs.ground(subs)
        bp.rhs = self.rhs.ground(subs)

        return bp

    def getAtom(self) -> Atom:
        if not isinstance(self.lhs, Literal):
            raise Exception("Cannot get atom from Binary Predicate")
        return self.lhs.atom

    def getPredicates(self) -> Set[Atom]:
        return set()

    def getFunctions(self) -> Set[Atom]:
        if not self.__functions:
            self.__functions = self.lhs.getFunctions() | self.rhs.getFunctions()
        return self.__functions

    def __str__(self):
        return f"({self.operator} {self.lhs} {self.rhs})"

    def __repr__(self):
        return str(self)

    @staticmethod
    def additiveEffectsTransformation(effect: BinaryPredicate):
        x = BinaryPredicate()
        x.lhs = effect.lhs
        x.operator = "increase"
        x.rhs = effect.rhs - effect.lhs
        return x
