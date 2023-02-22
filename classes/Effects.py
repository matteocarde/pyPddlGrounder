from libs.pyGrounder.antlr4_directory.pddlParser import pddlParser
from libs.pyGrounder.classes.Conditions import Conditions


class Effects(Conditions):

    def __init__(self, node: pddlParser.EffectsContext):
        super().__init__(node)
