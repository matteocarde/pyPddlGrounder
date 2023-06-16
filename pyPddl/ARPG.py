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

    def __init__(self, actions: List[Action], problem: Problem):
        self.supporterLevels = list()
        self.stateLevels = list()
        self.actions: List[Action] = actions

        self.originalOrder = dict([(action, i) for (i, action) in enumerate(self.actions)])

        supporters: Set[Supporter] = set()
        for a in actions:
            supporters |= a.getSupporters()

        state: RelaxedIntervalState = RelaxedIntervalState.fromInitialCondition(problem.init)
        activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

        self.supporterLevels.append(activeSupporters)
        self.stateLevels.append(state)

        fullBooleanGoal = len(problem.goal.getFunctions()) == 0

        while activeSupporters and (fullBooleanGoal or not state.satisfies(problem.goal)):
            supporters = supporters - activeSupporters
            state = state.applySupporters(activeSupporters)
            activeSupporters = {s for s in supporters if s.isSatisfiedBy(state)}

            self.supporterLevels.append(activeSupporters)
            self.stateLevels.append(state)

        if not fullBooleanGoal and not state.satisfies(problem.goal):
            raise PDDLException.GoalNotReachable()

    def __getPurelyBoolean(self) -> List[Action]:
        order: List[Action] = list()
        for action in self.actions:
            if not action.getFunctions():
                order.append(action)
        return order

    def getActionsOrder(self) -> List[Action]:
        order: List[Action] = self.__getPurelyBoolean()
        usedActions: Set[Action] = set(order)
        for supporters in self.supporterLevels:
            partialOrder = set()
            for supporter in supporters:
                if supporter.originatingAction not in usedActions:
                    partialOrder.add(supporter.originatingAction)
                usedActions.add(supporter.originatingAction)
            order += sorted(partialOrder, key=lambda x: self.originalOrder[x])
        leftActions = set(self.actions) - usedActions
        order += sorted(leftActions, key=lambda x: self.originalOrder[x])
        return order

    def getConstantAtoms(self) -> Dict[Atom, float]:
        if len(self.stateLevels) < 2:
            return dict()
        lastLevel: RelaxedIntervalState = self.stateLevels[-1]
        subs: Dict[Atom, float] = dict()
        for (atom, interval) in lastLevel.intervals.items():
            if interval.lb == interval.ub:
                subs[atom] = interval.lb
        return subs
