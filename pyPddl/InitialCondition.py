from __future__ import annotations
from typing import List, Dict

from antlr4_directory.pddlParser import pddlParser
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from Literal import Literal
from Predicate import Predicate


class InitialCondition:
    assignment: List[Predicate]

    numericAssignments: Dict[Literal, float]

    def __init__(self):
        self.assignment = []
        self.numericAssignments = dict()

    @classmethod
    def fromNode(cls, node: pddlParser.InitContext) -> InitialCondition:
        ic = cls()
        ic.assignment = []
        for child in node.children:
            if isinstance(child, pddlParser.PositiveLiteralContext):
                ic.assignment.append(Literal.fromNode(child))
            if isinstance(child, pddlParser.AssignmentContext):
                assignment = BinaryPredicate.fromNode(child)
                ic.assignment.append(assignment)
                if not isinstance(assignment.rhs, Constant):
                    raise Exception(
                        "At the moment, this tool only support initial conditions with numeric constant assignments")
                ic.numericAssignments[assignment.lhs] = assignment.rhs.value

        return ic

    def getAssignment(self, literal: Literal) -> float:
        return self.numericAssignments[literal]
        pass
