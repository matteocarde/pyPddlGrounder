from typing import List, Tuple

from Action import Action
from Domain import GroundedDomain
from PDDLException import PDDLException
from Problem import Problem
from State import State


class NumericPlan:

    def __init__(self):
        self.__plan: List[Tuple[Action, int]] = list()
        self.__rolledPlan: List[Action] = list()

    def addRepeatedAction(self, action: Action, repetitions: int):
        self.__plan.append((action, repetitions))
        for i in range(0, repetitions):
            self.__rolledPlan.append(action)

    def validate(self, problem: Problem) -> bool:

        state = State.fromInitialCondition(problem.init)
        for action in self.__rolledPlan:
            if not state.satisfies(action.preconditions):
                raise PDDLException.InvalidPlan(f"Plan doesn't satisfies action {action}")
            state = state.applyAction(action)

        if not state.satisfies(problem.goal):
            raise PDDLException.InvalidPlan(f"Plan doesn't satisfies goal")

        return True

    def __str__(self):
        return "\n".join([f"{a[0]}x{a[1]}" for a in self.__plan])

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(self.__rolledPlan)

    def print(self):
        print(str(self))

    def printWithRepetitions(self):
        string = ""
        for a in self.__plan:
            for i in range(0, a[1]):
                string += str(a[0]) + "\n"

        print(string)