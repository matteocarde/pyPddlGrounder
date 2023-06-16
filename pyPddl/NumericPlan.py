from typing import List, Tuple

from Action import Action
from Domain import GroundedDomain
from PDDLException import PDDLException
from Problem import Problem
from State import State


class NumericPlan:
    quality: float

    def __init__(self):
        self.__plan: List[Tuple[Action, int]] = list()
        self.__rolledPlan: List[Action] = list()
        self.quality: float
        self.optimal = False

    def __len__(self):
        return len(self.__rolledPlan)

    def addRepeatedAction(self, action: Action, repetitions: int):
        self.__plan.append((action, repetitions))
        for i in range(0, repetitions):
            self.__rolledPlan.append(action)

    def validate(self, problem: Problem, avoidRaising=False) -> bool:

        state = State.fromInitialCondition(problem.init)
        for action in self.__rolledPlan:
            if not state.satisfies(action.preconditions):
                if avoidRaising:
                    return False
                raise PDDLException.InvalidPlan(f"Plan doesn't satisfies action {action}")
            state = state.applyAction(action)

        if not state.satisfies(problem.goal):
            if avoidRaising:
                return False
            raise PDDLException.InvalidPlan(f"Plan doesn't satisfies goal")

        return True

    def __str__(self):
        return "\n".join([f"{a[0]} x{a[1]}" for a in self.__plan])

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.__rolledPlan)

    def print(self):
        print(str(self))

    def toValString(self):
        string = ""
        t = 0
        for a in self.__plan:
            for i in range(0, a[1]):
                string += f"{t}: ({a[0]})\n"
                t += 1
        return string

    def printWithRepetitions(self):
        print(self.toValString())

    def getMetric(self, problem: Problem):
        if not problem.metric:
            return len(self.__rolledPlan)

        raise Exception("Not yet implemented")
