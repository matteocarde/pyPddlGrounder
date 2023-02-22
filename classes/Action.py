from __future__ import annotations
from typing import List, Dict, cast

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes.Operation import Operation
from libs.pyGrounder.classes.OperationType import OperationType
from libs.pyGrounder.classes.Type import Type


class Action(Operation):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.ActionContext):
        return super().fromNode(node)

    @property
    def type(self):
        return OperationType.ACTION

    def ground(self, problem) -> List[Action]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            action = Action()
            action.name = op.name
            action.preconditions = op.preconditions
            action.effects = op.effects
            action.planName = op.planName
            groundOps.append(action)
        return groundOps
