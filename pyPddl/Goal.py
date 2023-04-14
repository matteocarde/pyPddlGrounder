from __future__ import annotations

from typing import cast

from antlr4_directory.pddlParser import pddlParser
from Preconditions import Preconditions
from pylatex import Document


class Goal(Preconditions):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.GoalContext) -> Goal:
        return cast(Goal, super().fromNode(node.getChild(2)))

