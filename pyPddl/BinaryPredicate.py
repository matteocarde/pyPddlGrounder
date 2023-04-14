from __future__ import annotations

from enum import Enum
from typing import Dict, Set

from sympy import Expr, diff

from Atom import Atom
from Constant import Constant
from Literal import Literal
from MooreInterval import MooreInterval
from Predicate import Predicate
from Utilities import Utilities
from antlr4_directory.pddlParser import pddlParser as p


class BinaryPredicateType(Enum):
    MODIFICATION = "modification"
    OPERATION = "operation"
    COMPARATION = "comparation"


class BinaryPredicate(Predicate):
    operator: str
    lhs: BinaryPredicate or Literal or Constant
    rhs: BinaryPredicate or Literal or Constant
    type: BinaryPredicateType

    def __init__(self):
        super().__init__()
        self.__functions = None

    @classmethod
    def fromNode(cls, node: p.ModificationContext or p.ComparationContext or p.OperationContext) -> BinaryPredicate:
        bp = cls()

        if isinstance(node, p.NegatedComparationContext):
            bp = BinaryPredicate.fromNode(node.getChild(2))
            bp.operator = Utilities.inverted(bp.operator)
            return bp

        if type(node) not in {p.ModificationContext, p.ComparationContext, p.OperationContext, p.AssignmentContext}:
            raise Exception("Incorrect Binary Predicate Type: ", type(node))

        bp.operator = node.getChild(1).getText()
        bp.rhs = bp.__assignClass(node.getChild(3))
        lhsNode = node.getChild(2)

        bp.lhs = bp.__assignClass(lhsNode) if type(node) in {p.ComparationContext,
                                                             p.OperationContext} else Literal.fromNode(lhsNode)

        if type(node) in {p.ModificationContext, p.AssignmentContext}:
            bp.type = BinaryPredicateType.MODIFICATION
        elif isinstance(node, p.ComparationContext):
            bp.type = BinaryPredicateType.COMPARATION
        elif isinstance(node, p.OperationContext):
            bp.type = BinaryPredicateType.OPERATION
        else:
            raise Exception("I don't know what this is")

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
        bp.type = self.type

        return bp

    def getAtom(self) -> Atom:
        if not isinstance(self.lhs, Literal):
            raise Exception("Cannot get atom from Binary Predicate", self)
        return self.lhs.atom

    def getPredicates(self) -> Set[Atom]:
        return set()

    def getFunctions(self) -> Set[Atom]:
        if not self.__functions:
            self.__functions = self.lhs.getFunctions() | self.rhs.getFunctions()
        return self.__functions

    def getFunctionsOverwrite(self) -> Set[Atom]:
        self.__functions = self.lhs.getFunctions() | self.rhs.getFunctions()
        return self.__functions

    def __str__(self):
        return f"({self.operator} {self.lhs} {self.rhs})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, BinaryPredicate):
            return False
        return str(self) == str(other)

    def toLatex(self) -> str:
        if self.operator == "/":
            return r"\frac{" + self.lhs.toLatex() + "}{" + self.rhs.toLatex + "}"
        return f"({self.lhs.toLatex()} {Utilities.latexOp(self.operator)} {self.rhs.toLatex()})"

    @staticmethod
    def additiveEffectsTransformation(effect: BinaryPredicate):
        x = BinaryPredicate()
        x.lhs = effect.lhs
        x.operator = "increase"
        x.rhs = effect.rhs - effect.lhs
        x.type = effect.type
        return x

    def substitute(self, subs: Dict[Atom, float], default=None) -> Predicate:
        x = BinaryPredicate()
        x.lhs = self.lhs.substitute(subs, default)
        x.operator = self.operator
        x.rhs = self.rhs.substitute(subs, default)
        x.type = self.type
        x.__functions = x.getFunctionsOverwrite()

        return x

    def getLinearIncrement(self) -> float:
        if self.type != BinaryPredicateType.OPERATION:
            raise Exception("Cannot get linear increment since Binary Predicate is not an operation")

        if len(self.lhs.getFunctions()) > 0 and len(self.rhs.getFunctions()) > 0 and self.operator in {"*", "/"}:
            raise Exception("Cannot get linear increment in a non linear function ", self)

        return Utilities.op(self.operator, self.lhs.getLinearIncrement(), self.rhs.getLinearIncrement())

    def simplify(self):
        if self.type == BinaryPredicateType.MODIFICATION:
            raise Exception("Cannot simplify a modification of the form", self)
        if self.type == BinaryPredicateType.COMPARATION:
            bp = BinaryPredicate()
            bp.type = self.type
            bp.lhs = (self.lhs - self.rhs).simplify()
            bp.rhs = Constant(0)
            bp.operator = self.operator
            return bp
        if self.type == BinaryPredicateType.OPERATION:
            raise NotImplemented("TODO")

    def toExpression(self) -> Expr:
        if self.type != BinaryPredicateType.OPERATION:
            raise Exception("Cannot transform to expression ", self.type)
        return Utilities.op(self.operator, self.lhs.toExpression(), self.rhs.toExpression())

    def getIntervalFromSimpleCondition(self) -> MooreInterval or None:
        if len(self.getFunctions()) > 1:
            return None

        var = self.getFunctions().pop().toExpression()
        func = self.lhs - self.rhs

        # f = mx + q
        f: Expr = func.toExpression()

        m = diff(f, var)  # m = df/dx
        q = f.subs(var, 0)  # q = f | 0

        lb = float(-q / m) if self.operator in {">=", ">", "=", "!="} else float("-inf")
        ub = float(-q / m) if self.operator in {"<=", "<", "=", "!="} else float("+inf")

        return MooreInterval(lb, ub)

    @classmethod
    def fromOperationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).operation())

    @classmethod
    def fromModificationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).modification())

    @classmethod
    def fromAssignmentString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).assignment())

    @classmethod
    def fromComparationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).comparation())

    @classmethod
    def fromNegatedComparationString(cls, string: str):
        return cls.fromNode(Utilities.getParseTree(string).negatedComparation())
