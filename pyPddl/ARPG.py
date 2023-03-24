from typing import Set, List, Dict

from Action import Action
from Atom import Atom
from Domain import Domain
from PDDLException import PDDLException
from Problem import Problem
from RelaxedIntervalState import RelaxedIntervalState
from Supporter import Supporter


class ARPG:
    supporterLevels: List[Set[Supporter]]
    stateLevels: List[RelaxedIntervalState]

    def __init__(self, actions: Set[Action], problem: Problem):
        self.supporterLevels = list()
        self.stateLevels = list()

        supporters: Set[Supporter] = set()
        for a in actions:
            supporters |= a.getSupporters()

        state: RelaxedIntervalState = RelaxedIntervalState.fromInitialCondition(problem.init)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

        self.supporterLevels.append(activeSupporters)
        self.stateLevels.append(state)

        while activeSupporters and not state.satisfies(problem.goal):
            supporters = supporters - activeSupporters
            state = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

            self.supporterLevels.append(activeSupporters)
            self.stateLevels.append(state)

        if not state.satisfies(problem.goal):
            raise PDDLException.GoalNotReachable()

    def getActionsOrder(self) -> List[Action]:
        order: List[Action] = list()
        usedActions: Set[Action] = set()
        for supporters in self.supporterLevels:
            for supporter in supporters:
                if supporter.originatingAction not in usedActions:
                    order.append(supporter.originatingAction)
                usedActions.add(supporter.originatingAction)

        return order

    def getConstantAtoms(self) -> Dict[Atom, float]:
        lastLevel: RelaxedIntervalState = self.stateLevels[-1]
        subs: Dict[Atom, float] = dict()
        for (atom, interval) in lastLevel.intervals.items():
            if interval.lb == interval.ub:
                subs[atom] = interval.lb
        return subs
