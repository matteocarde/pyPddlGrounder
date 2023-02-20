from typing import List

from libs.pyGrounder.myClasses.Operation import Operation


class Process(Operation):
    '''
    The class Process represents one process of the pddl file. It is composed by name, parameters, preconditions and effect.
    
    Parameters
    ----------
    node : antlr4 tree
        The tree containing the nodes with the process.
    
    OR
    
    name : str
        The name of the process. For example moving
    preconditions : list
        The list containing the objects Preconditions
    effects : list
        The list containing the ojects Effects
    '''

    def __init__(self, node=None, name=None, parameters=None, preconditions=None, effects=None):
        super().__init__(node, name, parameters, preconditions, effects)

    def ground(self, problem) -> List:
        groundOps: List = []
        for op in self.getGroundedOperations(problem):
            groundOps.append(
                Process(name=op.name, parameters=[], preconditions=op.preconditions, effects=op.effects))
        return groundOps
