from typing import List, Dict

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Operation import Operation
from libs.pyGrounder.classes.OperationType import OperationType
from libs.pyGrounder.classes.Type import Type


class Process(Operation):

    def __init__(self, node: pddlParser.ProcessContext, types: Dict[str, Type]):
        super().__init__(node, types)

    @property
    def type(self):
        return OperationType.PROCESS

    def ground(self, problem) -> List:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            groundOps.append(
                Process(name=op.name, planName=op.planName, preconditions=op.preconditions, effects=op.effects))
        return groundOps
