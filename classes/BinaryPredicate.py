from __future__ import annotations

from enum import Enum
from typing import Dict

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes.Constant import Constant
from libs.pyGrounder.classes.Literal import Literal
from libs.pyGrounder.classes.Predicate import Predicate


class BinaryPredicateType(Enum):
    MODIFICATION = "modification"
    OPERATION = "operation"
    COMPARATION = "comparation"


class BinaryPredicate(Predicate):
    operator: str
    lhs: BinaryPredicate or Literal or Constant
    rhs: BinaryPredicate or Literal or Constant

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.ModificationContext or p.ComparationContext or p.OperationContext) -> BinaryPredicate:
        bp = cls()

        bp.operator = node.getChild(1).getText()
        bp.rhs = bp.__assignClass(node.getChild(3))
        lhsNode = node.getChild(2)

        bp.lhs = bp.__assignClass(lhsNode) if isinstance(node, p.OperationContext) else Literal.fromNode(lhsNode)

        if isinstance(node, p.ModificationContext):
            bp.type = BinaryPredicateType.MODIFICATION
        elif isinstance(node, p.ComparationContext):
            bp.type = BinaryPredicateType.COMPARATION
        elif isinstance(node, p.OperationContext):
            bp.type = BinaryPredicateType.OPERATION

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

    def __str__(self):
        return f"({self.operator} {self.lhs} {self.rhs})"

    def __repr__(self):
        return str(self)
