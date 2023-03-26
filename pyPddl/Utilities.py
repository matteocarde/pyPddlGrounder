import operator
import re

from antlr4 import *

from antlr4_directory.pddlLexer import pddlLexer
from antlr4_directory.pddlParser import pddlParser

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

COMPARATORS = {
    ">=": operator.ge,
    "<=": operator.le,
    ">": operator.gt,
    "<": operator.lt,
    "=": operator.eq,
    "!=": operator.ne
}

INVERSE_COMPARATORS = {
    ">=": "<",
    "<=": ">",
    ">": "<=",
    "<": ">=",
    "=": "!=",
    "!=": "="
}


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

    @staticmethod
    def op(op: str, left, right):
        return OPERATORS[op](left, right)

    @staticmethod
    def compare(op: str, left, right):
        return COMPARATORS[op](left, right)

    @classmethod
    def inverted(cls, op: str):
        return INVERSE_COMPARATORS[op]

