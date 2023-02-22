from enum import Enum

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes.Constant import Constant
from libs.pyGrounder.classes.Literal import Literal
from libs.pyGrounder.classes.Predicate import Predicate


class BinaryPredicateType(Enum):
    MODIFICATION = "modification"
    OPERATION = "operation"
    COMPARATION = "comparation"


class BinaryPredicate(Predicate):

    def __init__(self, node: p.ModificationContext or p.ComparationContext or p.OperationContext):
        super().__init__()

        self.operator = node.getChild(1).getText()
        self.rhs = self.__assignClass(node.getChild(3))

        if isinstance(node, p.OperationContext):
            self.lhs = self.__assignClass(node.getChild(2))
        else:
            self.lhs = Literal(node.getChild(2))

        if isinstance(node, p.ModificationContext):
            self.type = BinaryPredicateType.MODIFICATION
        elif isinstance(node, p.ComparationContext):
            self.type = BinaryPredicateType.COMPARATION
        elif isinstance(node, p.OperationContext):
            self.type = BinaryPredicateType.OPERATION

    @staticmethod
    def __assignClass(node: p.OperationSideContext):
        child = node.getChild(0)
        if isinstance(child, p.OperationContext):
            return BinaryPredicate(child)
        elif isinstance(child, p.PositiveLiteralContext):
            return Literal(child)
        elif isinstance(child, p.ConstantContext):
            return Constant(child)
        elif isinstance(child, p.NumberContext):
            return Constant(child)
        else:
            raise NotImplemented()

    def __str__(self):
        return f"({self.operator} {self.lhs} {self.rhs})"

    def __repr__(self):
        return str(self)
