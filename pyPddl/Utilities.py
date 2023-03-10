import re
from antlr4 import *
from antlr4_directory.pddlLexer import pddlLexer
from antlr4_directory.pddlParser import pddlParser

class Utilities:

    @staticmethod
    def removeComments(string: str):
        return re.sub(r';.*', '', string)


    @staticmethod
    def getParseTree(string: str) -> pddlParser:
        input_stream = InputStream(string)
        lexer = pddlLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        return pddlParser(token_stream)