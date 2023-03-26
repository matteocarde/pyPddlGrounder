from __future__ import annotations
from typing import List, Dict

from Atom import Atom
from Utilities import Utilities
from antlr4_directory.pddlParser import pddlParser
from BinaryPredicate import BinaryPredicate
from Constant import Constant
from Literal import Literal
from Predicate import Predicate


class InitialCondition:
    assignments: List[Predicate]

    numericAssignments: Dict[Atom, float]

    def __init__(self):
        self.assignments = []
        self.numericAssignments = dict()

    def __str__(self):
        return str(self.assignments)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.assignments)

    @classmethod
    def fromNode(cls, node: pddlParser.InitContext) -> InitialCondition:
        ic = cls()
        ic.assignments = []
        for child in node.children:
            if isinstance(child, pddlParser.PositiveLiteralContext):
                ic.assignments.append(Literal.fromNode(child))
            if isinstance(child, pddlParser.AssignmentContext):
                assignment = BinaryPredicate.fromNode(child)
                ic.assignments.append(assignment)
                if not isinstance(assignment.rhs, Constant):
                    raise Exception(
                        "At the moment, this tool only support initial conditions with numeric constant assignments")
                ic.numericAssignments[assignment.getAtom()] = assignment.rhs.value

        return ic

    def getAssignment(self, atom: Atom) -> float:
        return self.numericAssignments[atom]
        pass

    @classmethod
    def fromString(cls, string: str):
        return InitialCondition.fromNode(Utilities.getParseTree(string).init())
