from typing import List, Tuple

from Action import Action


class NumericPlan:

    def __init__(self):
        self.__plan: List[Tuple[Action, int]] = list()

    def addRepeatedAction(self, action: Action, repetitions: int):
        self.__plan.append((action, repetitions))

    def __str__(self):
        return "\n".join([f"{a[0]}x{a[1]}" for a in self.__plan])

    def __repr__(self):
        return str(self)

    def print(self):
        print(str(self))

    def printWithRepetitions(self):
        string = ""
        for a in self.__plan:
            for i in range(0, a[1]):
                string += str(a[0]) + "\n"

        print(string)
