from __future__ import annotations
from typing import List, Dict, cast

from antlr4_directory.pddlParser import pddlParser as p
from Operation import Operation
from OperationType import OperationType

class Event(Operation):

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: p.EventContext):
        return super().fromNode(node)

    @property
    def type(self):
        return OperationType.EVENT

    def ground(self, problem) -> List[Event]:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            event = Event()
            event.name = op.name
            event.preconditions = op.preconditions
            event.effects = op.effects
            event.planName = op.planName
            groundOps.append(event)
        return groundOps
