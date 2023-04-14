from __future__ import annotations
from typing import Dict, Tuple, List

from Utilities import Utilities
from antlr4_directory.pddlParser import pddlParser
from Predicate import Predicate
from Type import Type


class TypedPredicate(Predicate):
    name: str
    parameters: List[Tuple[str, Type]]

    def __init__(self):
        super().__init__()

    @classmethod
    def fromNode(cls, node: pddlParser.PositiveLiteralContext, types: Dict[str, Type]) -> TypedPredicate:
        typedPredicate = cls()

        atomNode: pddlParser.AtomContext = node.getChild(1)
        typedPredicate.name = atomNode.getChild(0).getText()
        typedPredicate.parameters = []

        for parameterNode in atomNode.children[1:]:
            typedAtom = parameterNode.getChild(0)
            if not isinstance(typedAtom, pddlParser.TypedAtomParameterContext):
                raise f"Typed predicate {typedPredicate.name} is not types"
            paramName = typedAtom.getChild(0).getText()
            paramType = typedAtom.getChild(2).getText()
            typedPredicate.parameters.append((paramName, types[paramType]))

        return typedPredicate
