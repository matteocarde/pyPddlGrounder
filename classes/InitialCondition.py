from typing import List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.BinaryPredicate import BinaryPredicate
from libs.pyGrounder.classes.Literal import Literal
from libs.pyGrounder.classes.Predicate import Predicate


class InitialCondition:
    assignment: List[Predicate]

    def __init__(self):
        self.assignment = []

    @classmethod
    def fromNode(cls, node: pddlParser.InitContext):
        ic = cls()
        ic.assignment = []
        for child in node.children:
            if isinstance(child, pddlParser.PositiveLiteralContext):
                ic.assignment.append(Literal.fromNode(child))
            if isinstance(child, pddlParser.AssignmentContext):
                ic.assignment.append(BinaryPredicate.fromNode(child))
