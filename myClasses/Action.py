from typing import List

from libs.pyGrounder.myClasses.Operation import Operation
from libs.pyGrounder.myClasses.OperationType import OperationType


class Action(Operation):

    def __init__(self, node=None, name=None, planName=None, preconditions=None, effects=None):
        super().__init__(node, name, planName, preconditions, effects)

    @property
    def type(self):
        return OperationType.ACTION

    def ground(self, problem) -> List:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            groundOps.append(Action(name=op.name, planName=op.planName, preconditions=op.preconditions, effects=op.effects))
        return groundOps
