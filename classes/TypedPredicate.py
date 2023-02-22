from typing import Dict, Tuple, List

from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Predicate import Predicate
from libs.pyGrounder.classes.Type import Type


class TypedPredicate(Predicate):
    name: str
    parameters: List[Tuple[str, Type]]

    def __init__(self, node: pddlParser.PositiveLiteralContext, types: Dict[str, Type]):
        super().__init__()

        atomNode: pddlParser.AtomContext = node.getChild(1)
        self.name = atomNode.getChild(0).getText()
        self.parameters = []

        for parameterNode in atomNode.children[1:]:
            typedAtom = parameterNode.getChild(0)
            if not isinstance(typedAtom, pddlParser.TypedAtomParameterContext):
                raise f"Typed predicate {self.name} is not types"
            paramName = typedAtom.getChild(0).getText()
            paramType = typedAtom.getChild(2).getText()
            self.parameters.append((paramName, types[paramType]))
