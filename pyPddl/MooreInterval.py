from __future__ import annotations


class MooreInterval:

    def __init__(self, lb: float = float("-inf"), ub: float = float("+inf")):
        self.lb = lb
        self.ub = ub

    def __add__(self, other: MooreInterval or float or int):
        if type(other) == float or type(other) == int:
            other = MooreInterval(other, other)
        return MooreInterval(self.lb + other.lb, self.ub + other.ub)

    def __sub__(self, other: MooreInterval or float or int):
        if type(other) == float or type(other) == int:
            other = MooreInterval(other, other)
        return MooreInterval(self.lb - other.ub, self.ub - other.lb)

    def __mul__(self, other: MooreInterval or float or int):
        if type(other) == float or type(other) == int:
            other = MooreInterval(other, other)

        lb = min(self.lb * other.lb, self.lb * other.ub, self.ub * other.lb, self.ub * other.ub)
        ub = max(self.lb * other.lb, self.lb * other.ub, self.ub * other.lb, self.ub * other.ub)

        return MooreInterval(lb, ub)

    def __truediv__(self, other: MooreInterval or float or int):
        if type(other) == float or type(other) == int:
            other = MooreInterval(other, other)

        if other.lb * other.ub <= 0:
            raise Exception(f"Division by zero when doing {self}/{other}")

        lb = min(self.lb / other.lb, self.lb / other.ub, self.ub / other.lb, self.ub / other.ub)
        ub = max(self.lb / other.lb, self.lb / other.ub, self.ub / other.lb, self.ub / other.ub)

        return MooreInterval(lb, ub)

    def merge(self, other: MooreInterval):
        return MooreInterval(min(self.lb, other.lb), max(self.ub, other.ub))

    def exists(self, operator: str, value: float):
        if operator == ">":
            return self.ub > value
        if operator == "<":
            return self.lb < value
        if operator == ">=":
            return self.ub >= value
        if operator == "<=":
            return self.lb <= value
        if operator == "=":
            return self.lb <= value <= self.ub
        if operator == "!=":
            return self.lb >= value >= self.ub

    def getExtended(self, eff) -> MooreInterval:
        if eff.value == float("+inf"):
            return self.merge(MooreInterval(self.lb, float("+inf")))
        if eff.value == float("-inf"):
            return self.merge(MooreInterval(float("-inf"), self.ub))
        return self.merge(MooreInterval(eff.value, eff.value))

    def __str__(self):
        return f"[{self.lb}, {self.ub}]"

    def __repr__(self):
        return str(self)
