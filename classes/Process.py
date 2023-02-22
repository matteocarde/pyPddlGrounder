from __future__ import annotations
from typing import List, Dict, cast

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser as p
from libs.pyGrounder.classes.Operation import Operation
from libs.pyGrounder.classes.OperationType import OperationType


class Process(Operation):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.ProcessContext):
        return super().fromNode(node)

    @property
    def type(self):
        return OperationType.PROCESS

    def ground(self, problem) -> List[Process]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            event = Process()
            event.name = op.name
            event.preconditions = op.preconditions
            event.effects = op.effects
            event.planName = op.planName
            groundOps.append(event)
        return groundOps
