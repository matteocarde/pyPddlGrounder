from typing import List

from libs.pyGrounder.myClasses.Operation import Operation
from libs.pyGrounder.myClasses.OperationType import OperationType


class Event(Operation):
    '''
    The class Event represents one event of the pddl file. It is composed by name, parameters, preconditions and effect.
    
    Parameters
    ----------
    node : antlr4 tree
        The tree containing the nodes with the event.
    
    OR
    
    name : str
        The name of the action. For example endMoving
    preconditions : list
        The list containing the objects Preconditions
    effects : list
        The list containing the ojects Effects
    '''

    def __init__(self, node=None, name=None, planName=None, preconditions=None, effects=None):
        super().__init__(node, name, planName, preconditions, effects)

    @property
    def type(self):
        return OperationType.EVENT

    def ground(self, problem) -> List:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            groundOps.append(
                Event(name=op.name, planName=op.planName, preconditions=op.preconditions, effects=op.effects))
        return groundOps
