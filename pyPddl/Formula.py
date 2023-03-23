from __future__ import annotations

from itertools import chain
from typing import Dict, Set

from Atom import Atom
from BinaryPredicate import BinaryPredicate
from Literal import Literal
from Predicate import Predicate
from antlr4_directory.pddlParser import pddlParser as p


class Formula:
    type: str
    conditions: [Formula or Predicate]

    def __init__(self):
        self.conditions = list()

    @classmethod
    def fromNode(cls, node) -> Formula:
        formula = cls()

        if isinstance(node.getChild(0), p.EmptyPreconditionContext):
            return formula

        clauses = []

        formulaComponent = node.getChild(0) if type(node) == p.PreconditionsContext else node
        if isinstance(formulaComponent, p.BooleanLiteralContext):
            clauses.append(formulaComponent.getChild(0))
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
                formula.conditions.append(Literal.fromNode(clause))
            elif type(clause) in {p.ComparationContext, p.NegatedComparationContext}:
                formula.conditions.append(BinaryPredicate.fromNode(clause))

        return formula

    def ground(self, subs: Dict[str, str]):
        groundFormula = Formula()
        for condition in self.conditions:
            groundFormula.conditions.append(condition.ground(subs))
        return groundFormula

    def getFunctions(self) -> Set[Atom]:
        functions = set()
        for c in self.conditions:
            if isinstance(c, Literal):
                continue
            functions |= c.getFunctions()
        return functions

    def getPredicates(self):
        return set(chain.from_iterable([c.getPredicates() for c in self.conditions]))

    def __iter__(self):
        return iter(self.conditions)

    def __str__(self):
        return str(self.conditions)

    def __repr__(self):
        return str(self.conditions)

    def __add__(self, other):
        c = Formula()
        c.conditions = self.conditions + other
        return c
