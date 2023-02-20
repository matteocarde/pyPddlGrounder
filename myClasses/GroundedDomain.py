from typing import Dict, List, Set

from libs.pyGrounder.myClasses.Action import Action
from libs.pyGrounder.myClasses.Domain import Domain
from libs.pyGrounder.myClasses.Event import Event
from libs.pyGrounder.myClasses.Operation import Operation
from libs.pyGrounder.myClasses.Problem import Problem
from libs.pyGrounder.myClasses.Process import Process
from libs.pyGrounder.myClasses.Variable import Variable


class GroundedDomain(Domain):
    __operationsDict: Dict[str, Operation] = dict()

    def __init__(self, domain: Domain, problem: Problem):

        constants = []
        for obj in problem.objects:
            objType = obj["objectType"]
            for instance in obj["objectInstances"]:
                constants.append(Variable(instance + "-" + objType))

        gActions: Set[Operation] = set([g for action in domain.actions for g in action.ground(problem)])
        gEvents: Set[Operation] = set([g for event in domain.events for g in event.ground(problem)])
        gProcesses: Set[Operation] = set([g for process in domain.processes for g in process.ground(problem)])

        for op in gActions.union(gEvents).union(gProcesses):
            self.__operationsDict[op.planName] = op

        super().__init__(name=domain.name, requirements=domain.requirements, types=domain.types,
                         constants=constants, actions=gActions, events=gEvents,
                         processes=gProcesses)

    def getOperationByPlanName(self, planName) -> Operation:
        return self.__operationsDict[planName]
