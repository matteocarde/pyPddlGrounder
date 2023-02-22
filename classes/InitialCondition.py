from typing import List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.BinaryPredicate import BinaryPredicate
from libs.pyGrounder.classes.Literal import Literal
from libs.pyGrounder.classes.Predicate import Predicate


class InitialCondition:
    assignment: List[Predicate]

    def __init__(self, node: pddlParser.InitContext):

        self.assignment = []
        for child in node.children:
            if isinstance(child, pddlParser.PositiveLiteralContext):
                self.assignment.append(Literal(child))
            if isinstance(child, pddlParser.AssignmentContext):
                self.assignment.append(BinaryPredicate(child))
