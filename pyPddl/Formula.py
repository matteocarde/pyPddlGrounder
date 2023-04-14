from __future__ import annotations

from itertools import chain
from typing import Dict, Set

from pylatex import Document

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Literal import Literal
from Predicate import Predicate
from Utilities import Utilities
from antlr4_directory.pddlParser import pddlParser as p


class Formula:
    type: str
    conditions: [Formula or Predicate]

    def __init__(self):
        self.type = "AND"
        self.conditions = list()

    @classmethod
    def fromNode(cls, node) -> Formula:
        formula = cls()

        if isinstance(node.getChild(0), p.EmptyPreconditionContext):
            return formula

        clauses = []

        formulaComponent = node.getChild(0) if type(node) == p.PreconditionsContext else node
        formula.type = "OR" if type(formulaComponent) == p.OrClauseContext else "AND"
        if isinstance(formulaComponent, p.BooleanLiteralContext):
            clauses.append(formulaComponent)
        elif type(formulaComponent) in {p.ComparationContext, p.NegatedComparationContext}:
            clauses.append(formulaComponent)
        elif type(formulaComponent) in {p.AndClauseContext, p.OrClauseContext}:
            clauses = formulaComponent.children
        else:
            raise Exception("Unexpected clause in precondition")

        for clause in clauses:
            if type(clause) in {p.AndClauseContext, p.OrClauseContext}:
                formula.conditions.append(Formula.fromNode(clause))
            elif isinstance(clause, p.BooleanLiteralContext):
                formula.conditions.append(Literal.fromNode(clause.getChild(0)))
            elif type(clause) in {p.ComparationContext, p.NegatedComparationContext}:
                formula.conditions.append(BinaryPredicate.fromNode(clause))

        return formula

    @classmethod
    def fromString(cls, string: str) -> Formula:
        return Formula.fromNode(Utilities.getParseTree(string).preconditions())

    def ground(self, subs: Dict[str, str]):
        gFormula = Formula()
        gFormula.type = self.type
        for condition in self.conditions:
            gFormula.conditions.append(condition.ground(subs))
        return gFormula

    def getFunctions(self) -> Set[Atom]:
        functions = set()
        for c in self.conditions:
            if isinstance(c, Literal):
                continue
            functions |= c.getFunctions()
        return functions

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.conditions]))

    def substitute(self, subs: Dict[Atom, float], default=None) -> Formula:
        x = Formula()
        x.type = self.type
        x.conditions = [c.substitute(subs, default) for c in self.conditions]
        return x

    def __iter__(self):
        return iter(self.conditions)

    def __str__(self):
        return f"({self.type.lower()} {' '.join([str(c) for c in self.conditions])})"

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return str(self.conditions)

    def __add__(self, other):
        c = Formula()
        c.conditions = self.conditions + other
        return c

    def __len__(self):
        return len(self.conditions)

    def toLatex(self):
        if not self.conditions:
            return r"\emptyset"
        symbol = r"\wedge" if self.type == "AND" else r"\vee"
        return "(" + symbol.join([c.toLatex() for c in self.conditions]) + ")"
        pass
