from enum import Enum

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.myClasses.new.NConstant import NConstant
from libs.pyGrounder.myClasses.new.NLiteral import NLiteral
from libs.pyGrounder.myClasses.new.NPredicate import NPredicate


class BinaryPredicateType(Enum):
    MODIFICATION = "modification"
    OPERATION = "operation"
    COMPARATION = "comparation"


class NBinaryPredicate(NPredicate):

    def __init__(self, node: p.ModificationContext or p.ComparationContext or p.NOperationContext):
        super().__init__()

        self.operator = node.getChild(1).getText()
        self.rhs = self.__assignClass(node.getChild(3))

        if isinstance(node, p.OperationContext):
            self.lhs = self.__assignClass(node.getChild(2))
        else:
            self.lhs = NLiteral(node.getChild(2))

        if isinstance(node, p.ModificationContext):
            self.type = BinaryPredicateType.MODIFICATION
        elif isinstance(node, p.ComparationContext):
            self.type = BinaryPredicateType.COMPARATION
        elif isinstance(node, p.NOperationContext):
            self.type = BinaryPredicateType.OPERATION

    @staticmethod
    def __assignClass(node: p.OperationSideContext):
        child = node.getChild(0)
        if isinstance(child, p.NOperationContext):
            return NBinaryPredicate(child)
        elif isinstance(child, p.PositiveLiteralContext):
            return NLiteral(child)
        elif isinstance(child, p.ConstantContext):
            return NConstant(child)
        else:
            raise NotImplemented()

    def __str__(self):
        return f"({self.operator} {self.lhs} {self.rhs})"

    def __repr__(self):
        return str(self)
