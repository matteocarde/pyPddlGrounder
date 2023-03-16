from typing import Set, List

from Action import Action
from Domain import Domain
from PDDLException import PDDLException
from Problem import Problem
from RelaxedIntervalState import RelaxedIntervalState
from Supporter import Supporter


class ARPG:
    __supporterLevels: List[Set[Supporter]]
    __stateLevels: List[RelaxedIntervalState]

    def __init__(self, actions: Set[Action], problem: Problem):
        self.__supporterLevels = list()
        self.__stateLevels = list()

        supporters: Set[Supporter] = set()
        for a in actions:
            supporters |= a.getSupporters()

        state: RelaxedIntervalState = RelaxedIntervalState.fromInitialCondition(problem.init)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

        self.__supporterLevels.append(activeSupporters)
        self.__stateLevels.append(state)

        while activeSupporters and not state.satisfies(problem.goal):
            supporters = supporters - activeSupporters
            state = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

            self.__supporterLevels.append(activeSupporters)
            self.__stateLevels.append(state)

        if not state.satisfies(problem.goal):
            raise PDDLException.GoalNotReachable()

    def getActionsOrder(self) -> List[Action]:
        order: List[Action] = list()
        usedActions: Set[Action] = set()
        for supporters in self.__supporterLevels:
            for supporter in supporters:
                if supporter.originatingAction not in usedActions:
                    order.append(supporter.originatingAction)
                usedActions.add(supporter.originatingAction)

        return order
