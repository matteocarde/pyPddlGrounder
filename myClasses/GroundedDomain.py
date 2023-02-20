from typing import Dict, List

from libs.pyGrounder.myClasses.Action import Action
from libs.pyGrounder.myClasses.Domain import Domain
from libs.pyGrounder.myClasses.Event import Event
from libs.pyGrounder.myClasses.Operation import Operation
from libs.pyGrounder.myClasses.Problem import Problem
from libs.pyGrounder.myClasses.Process import Process
from libs.pyGrounder.myClasses.Variable import Variable


class GroundedDomain(Domain):
    def __init__(self, domain: Domain, problem: Problem):

        constants = []
        for object in problem.objects:
            objType = object["objectType"]
            for instance in object["objectIstances"]:
                constants.append(Variable(instance + "-" + objType))

        gActions: List[Action] = [gAction for action in domain.actions for gAction in action.ground(problem)]
        gEvents: List[Event] = [gEvent for event in domain.events for gEvent in event.ground(problem)]
        gProcesses: List[Process] = [gProcess for process in domain.processes for gProcess in process.ground(problem)]

        super().__init__(name=domain.name, requirements=domain.requirements, types=domain.types,
                              constants=constants, actions=gActions, events=gEvents,
                              processes=gProcesses)


def __createOperationsDict(self) -> Dict[str, Operation]:
    operationsDict: Dict[str, Operation] = dict()
    for action in self.__actions:
        operationsDict[action.getPlanName()] = action
    for event in self.__events:
        operationsDict[event.getPlanName()] = event
    for process in self.__processes:
        operationsDict[process.getPlanName()] = process

    return operationsDict
