# Generated from pddl.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,450,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,1,0,3,0,117,8,0,1,1,
        1,1,1,1,1,1,3,1,123,8,1,1,1,3,1,126,8,1,1,1,3,1,129,8,1,1,1,3,1,
        132,8,1,1,1,1,1,1,1,5,1,137,8,1,10,1,12,1,140,9,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,5,4,154,8,4,10,4,12,4,157,9,4,
        1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,5,7,168,8,7,10,7,12,7,171,9,
        7,1,8,1,8,1,8,4,8,176,8,8,11,8,12,8,177,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,4,12,189,8,12,11,12,12,12,190,1,12,1,12,1,12,1,13,
        1,13,3,13,198,8,13,1,14,1,14,5,14,202,8,14,10,14,12,14,205,9,14,
        1,15,1,15,5,15,209,8,15,10,15,12,15,212,9,15,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,3,19,229,
        8,19,1,20,1,20,1,20,4,20,234,8,20,11,20,12,20,235,1,20,1,20,1,21,
        1,21,1,21,4,21,243,8,21,11,21,12,21,244,1,21,1,21,1,22,1,22,1,23,
        1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,3,27,261,8,27,1,28,
        1,28,1,29,1,29,1,29,3,29,268,8,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,
        1,33,1,33,1,33,1,33,1,33,1,34,1,34,3,34,296,8,34,1,35,1,35,3,35,
        300,8,35,1,36,1,36,1,36,4,36,305,8,36,11,36,12,36,306,1,36,1,36,
        1,37,1,37,1,37,4,37,314,8,37,11,37,12,37,315,1,37,1,37,1,38,1,38,
        1,38,1,39,1,39,1,39,3,39,326,8,39,1,40,1,40,3,40,330,8,40,1,41,1,
        41,5,41,334,8,41,10,41,12,41,337,9,41,1,41,1,41,1,42,1,42,1,43,1,
        43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,46,1,46,1,46,3,46,356,
        8,46,1,46,3,46,359,8,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,3,47,
        368,8,47,1,47,3,47,371,8,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,3,
        48,380,8,48,1,48,3,48,383,8,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,
        1,49,3,49,393,8,49,1,49,1,49,1,49,3,49,398,8,49,1,49,1,49,1,50,1,
        50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,52,4,52,413,8,52,11,
        52,12,52,414,1,52,1,52,1,52,1,53,1,53,1,53,4,53,423,8,53,11,53,12,
        53,424,1,53,1,53,1,54,1,54,1,54,1,54,4,54,433,8,54,11,54,12,54,434,
        1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,56,1,56,
        1,56,0,0,57,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,0,5,1,0,3,
        8,1,0,15,17,2,0,10,10,18,20,1,0,21,25,1,0,40,41,433,0,116,1,0,0,
        0,2,118,1,0,0,0,4,143,1,0,0,0,6,148,1,0,0,0,8,150,1,0,0,0,10,160,
        1,0,0,0,12,163,1,0,0,0,14,165,1,0,0,0,16,172,1,0,0,0,18,181,1,0,
        0,0,20,183,1,0,0,0,22,185,1,0,0,0,24,188,1,0,0,0,26,197,1,0,0,0,
        28,199,1,0,0,0,30,206,1,0,0,0,32,213,1,0,0,0,34,217,1,0,0,0,36,221,
        1,0,0,0,38,228,1,0,0,0,40,230,1,0,0,0,42,239,1,0,0,0,44,248,1,0,
        0,0,46,250,1,0,0,0,48,252,1,0,0,0,50,254,1,0,0,0,52,256,1,0,0,0,
        54,260,1,0,0,0,56,262,1,0,0,0,58,267,1,0,0,0,60,269,1,0,0,0,62,275,
        1,0,0,0,64,281,1,0,0,0,66,287,1,0,0,0,68,295,1,0,0,0,70,299,1,0,
        0,0,72,301,1,0,0,0,74,310,1,0,0,0,76,319,1,0,0,0,78,325,1,0,0,0,
        80,329,1,0,0,0,82,331,1,0,0,0,84,340,1,0,0,0,86,342,1,0,0,0,88,345,
        1,0,0,0,90,348,1,0,0,0,92,351,1,0,0,0,94,363,1,0,0,0,96,375,1,0,
        0,0,98,387,1,0,0,0,100,401,1,0,0,0,102,406,1,0,0,0,104,412,1,0,0,
        0,106,419,1,0,0,0,108,428,1,0,0,0,110,438,1,0,0,0,112,443,1,0,0,
        0,114,117,3,2,1,0,115,117,3,98,49,0,116,114,1,0,0,0,116,115,1,0,
        0,0,117,1,1,0,0,0,118,119,5,42,0,0,119,120,5,1,0,0,120,122,3,4,2,
        0,121,123,3,8,4,0,122,121,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,
        0,124,126,3,16,8,0,125,124,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,
        0,127,129,3,40,20,0,128,127,1,0,0,0,128,129,1,0,0,0,129,131,1,0,
        0,0,130,132,3,42,21,0,131,130,1,0,0,0,131,132,1,0,0,0,132,138,1,
        0,0,0,133,137,3,92,46,0,134,137,3,94,47,0,135,137,3,96,48,0,136,
        133,1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,140,1,0,0,0,138,
        136,1,0,0,0,138,139,1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,
        142,5,43,0,0,142,3,1,0,0,0,143,144,5,42,0,0,144,145,5,2,0,0,145,
        146,5,45,0,0,146,147,5,43,0,0,147,5,1,0,0,0,148,149,7,0,0,0,149,
        7,1,0,0,0,150,151,5,42,0,0,151,155,5,9,0,0,152,154,3,6,3,0,153,152,
        1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,158,
        1,0,0,0,157,155,1,0,0,0,158,159,5,43,0,0,159,9,1,0,0,0,160,161,5,
        10,0,0,161,162,3,12,6,0,162,11,1,0,0,0,163,164,5,45,0,0,164,13,1,
        0,0,0,165,169,3,12,6,0,166,168,3,10,5,0,167,166,1,0,0,0,168,171,
        1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,15,1,0,0,0,171,169,1,
        0,0,0,172,173,5,42,0,0,173,175,5,11,0,0,174,176,3,14,7,0,175,174,
        1,0,0,0,176,177,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,179,
        1,0,0,0,179,180,5,43,0,0,180,17,1,0,0,0,181,182,5,45,0,0,182,19,
        1,0,0,0,183,184,5,45,0,0,184,21,1,0,0,0,185,186,5,44,0,0,186,23,
        1,0,0,0,187,189,3,22,11,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,5,10,0,0,193,194,
        3,12,6,0,194,25,1,0,0,0,195,198,3,22,11,0,196,198,3,20,10,0,197,
        195,1,0,0,0,197,196,1,0,0,0,198,27,1,0,0,0,199,203,3,18,9,0,200,
        202,3,26,13,0,201,200,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,
        204,1,0,0,0,204,29,1,0,0,0,205,203,1,0,0,0,206,210,3,18,9,0,207,
        209,3,24,12,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,
        211,1,0,0,0,211,31,1,0,0,0,212,210,1,0,0,0,213,214,5,42,0,0,214,
        215,3,28,14,0,215,216,5,43,0,0,216,33,1,0,0,0,217,218,5,42,0,0,218,
        219,3,30,15,0,219,220,5,43,0,0,220,35,1,0,0,0,221,222,5,42,0,0,222,
        223,5,12,0,0,223,224,3,32,16,0,224,225,5,43,0,0,225,37,1,0,0,0,226,
        229,3,32,16,0,227,229,3,36,18,0,228,226,1,0,0,0,228,227,1,0,0,0,
        229,39,1,0,0,0,230,231,5,42,0,0,231,233,5,13,0,0,232,234,3,34,17,
        0,233,232,1,0,0,0,234,235,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,
        0,236,237,1,0,0,0,237,238,5,43,0,0,238,41,1,0,0,0,239,240,5,42,0,
        0,240,242,5,14,0,0,241,243,3,34,17,0,242,241,1,0,0,0,243,244,1,0,
        0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,246,1,0,0,0,246,247,5,43,
        0,0,247,43,1,0,0,0,248,249,7,1,0,0,249,45,1,0,0,0,250,251,7,2,0,
        0,251,47,1,0,0,0,252,253,7,3,0,0,253,49,1,0,0,0,254,255,5,47,0,0,
        255,51,1,0,0,0,256,257,5,26,0,0,257,53,1,0,0,0,258,261,3,50,25,0,
        259,261,3,52,26,0,260,258,1,0,0,0,260,259,1,0,0,0,261,55,1,0,0,0,
        262,263,3,50,25,0,263,57,1,0,0,0,264,268,3,60,30,0,265,268,3,32,
        16,0,266,268,3,54,27,0,267,264,1,0,0,0,267,265,1,0,0,0,267,266,1,
        0,0,0,268,59,1,0,0,0,269,270,5,42,0,0,270,271,3,46,23,0,271,272,
        3,58,29,0,272,273,3,58,29,0,273,274,5,43,0,0,274,61,1,0,0,0,275,
        276,5,42,0,0,276,277,5,25,0,0,277,278,3,32,16,0,278,279,3,56,28,
        0,279,280,5,43,0,0,280,63,1,0,0,0,281,282,5,42,0,0,282,283,3,48,
        24,0,283,284,3,58,29,0,284,285,3,58,29,0,285,286,5,43,0,0,286,65,
        1,0,0,0,287,288,5,42,0,0,288,289,3,44,22,0,289,290,3,32,16,0,290,
        291,3,58,29,0,291,292,5,43,0,0,292,67,1,0,0,0,293,296,3,38,19,0,
        294,296,3,64,32,0,295,293,1,0,0,0,295,294,1,0,0,0,296,69,1,0,0,0,
        297,300,3,38,19,0,298,300,3,66,33,0,299,297,1,0,0,0,299,298,1,0,
        0,0,300,71,1,0,0,0,301,302,5,42,0,0,302,304,5,27,0,0,303,305,3,68,
        34,0,304,303,1,0,0,0,305,306,1,0,0,0,306,304,1,0,0,0,306,307,1,0,
        0,0,307,308,1,0,0,0,308,309,5,43,0,0,309,73,1,0,0,0,310,311,5,42,
        0,0,311,313,5,27,0,0,312,314,3,70,35,0,313,312,1,0,0,0,314,315,1,
        0,0,0,315,313,1,0,0,0,315,316,1,0,0,0,316,317,1,0,0,0,317,318,5,
        43,0,0,318,75,1,0,0,0,319,320,5,42,0,0,320,321,5,43,0,0,321,77,1,
        0,0,0,322,326,3,68,34,0,323,326,3,72,36,0,324,326,3,76,38,0,325,
        322,1,0,0,0,325,323,1,0,0,0,325,324,1,0,0,0,326,79,1,0,0,0,327,330,
        3,70,35,0,328,330,3,74,37,0,329,327,1,0,0,0,329,328,1,0,0,0,330,
        81,1,0,0,0,331,335,5,42,0,0,332,334,3,24,12,0,333,332,1,0,0,0,334,
        337,1,0,0,0,335,333,1,0,0,0,335,336,1,0,0,0,336,338,1,0,0,0,337,
        335,1,0,0,0,338,339,5,43,0,0,339,83,1,0,0,0,340,341,5,45,0,0,341,
        85,1,0,0,0,342,343,5,28,0,0,343,344,3,82,41,0,344,87,1,0,0,0,345,
        346,5,29,0,0,346,347,3,78,39,0,347,89,1,0,0,0,348,349,5,30,0,0,349,
        350,3,80,40,0,350,91,1,0,0,0,351,352,5,42,0,0,352,353,5,31,0,0,353,
        355,3,84,42,0,354,356,3,86,43,0,355,354,1,0,0,0,355,356,1,0,0,0,
        356,358,1,0,0,0,357,359,3,88,44,0,358,357,1,0,0,0,358,359,1,0,0,
        0,359,360,1,0,0,0,360,361,3,90,45,0,361,362,5,43,0,0,362,93,1,0,
        0,0,363,364,5,42,0,0,364,365,5,32,0,0,365,367,3,84,42,0,366,368,
        3,86,43,0,367,366,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,371,
        3,88,44,0,370,369,1,0,0,0,370,371,1,0,0,0,371,372,1,0,0,0,372,373,
        3,90,45,0,373,374,5,43,0,0,374,95,1,0,0,0,375,376,5,42,0,0,376,377,
        5,33,0,0,377,379,3,84,42,0,378,380,3,86,43,0,379,378,1,0,0,0,379,
        380,1,0,0,0,380,382,1,0,0,0,381,383,3,88,44,0,382,381,1,0,0,0,382,
        383,1,0,0,0,383,384,1,0,0,0,384,385,3,90,45,0,385,386,5,43,0,0,386,
        97,1,0,0,0,387,388,5,42,0,0,388,389,5,1,0,0,389,390,3,100,50,0,390,
        392,3,102,51,0,391,393,3,106,53,0,392,391,1,0,0,0,392,393,1,0,0,
        0,393,394,1,0,0,0,394,395,3,108,54,0,395,397,3,110,55,0,396,398,
        3,112,56,0,397,396,1,0,0,0,397,398,1,0,0,0,398,399,1,0,0,0,399,400,
        5,43,0,0,400,99,1,0,0,0,401,402,5,42,0,0,402,403,5,34,0,0,403,404,
        5,45,0,0,404,405,5,43,0,0,405,101,1,0,0,0,406,407,5,42,0,0,407,408,
        5,35,0,0,408,409,5,45,0,0,409,410,5,43,0,0,410,103,1,0,0,0,411,413,
        3,20,10,0,412,411,1,0,0,0,413,414,1,0,0,0,414,412,1,0,0,0,414,415,
        1,0,0,0,415,416,1,0,0,0,416,417,5,10,0,0,417,418,3,12,6,0,418,105,
        1,0,0,0,419,420,5,42,0,0,420,422,5,36,0,0,421,423,3,104,52,0,422,
        421,1,0,0,0,423,424,1,0,0,0,424,422,1,0,0,0,424,425,1,0,0,0,425,
        426,1,0,0,0,426,427,5,43,0,0,427,107,1,0,0,0,428,429,5,42,0,0,429,
        432,5,37,0,0,430,433,3,32,16,0,431,433,3,62,31,0,432,430,1,0,0,0,
        432,431,1,0,0,0,433,434,1,0,0,0,434,432,1,0,0,0,434,435,1,0,0,0,
        435,436,1,0,0,0,436,437,5,43,0,0,437,109,1,0,0,0,438,439,5,42,0,
        0,439,440,5,38,0,0,440,441,3,78,39,0,441,442,5,43,0,0,442,111,1,
        0,0,0,443,444,5,42,0,0,444,445,5,39,0,0,445,446,7,4,0,0,446,447,
        3,60,30,0,447,448,5,43,0,0,448,113,1,0,0,0,38,116,122,125,128,131,
        136,138,155,169,177,190,197,203,210,228,235,244,260,267,295,299,
        306,315,325,329,335,355,358,367,370,379,382,392,397,414,424,432,
        434
    ]

class pddlParser ( Parser ):

    grammarFileName = "pddl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'define'", "'domain'", "':typing'", "':duration-inequalities'", 
                     "':time'", "':fluents'", "':adl'", "':durative-actions'", 
                     "':requirements'", "'-'", "':types'", "'not'", "':predicates'", 
                     "':functions'", "'assign'", "'increase'", "'decrease'", 
                     "'+'", "'*'", "'/'", "'>'", "'>='", "'<='", "'<'", 
                     "'='", "'#t'", "'and'", "':parameters'", "':precondition'", 
                     "':effect'", "':action'", "':event'", "':process'", 
                     "'problem'", "':domain'", "':objects'", "':init'", 
                     "':goal'", "':metric'", "'maximize'", "'minimize'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LP", "RP", "VAR", "NAME", 
                      "VARIABLE", "NUMBER", "WS" ]

    RULE_pddlDoc = 0
    RULE_domain = 1
    RULE_domainName = 2
    RULE_requireKey = 3
    RULE_requirements = 4
    RULE_parentType = 5
    RULE_typeName = 6
    RULE_type = 7
    RULE_types = 8
    RULE_atomName = 9
    RULE_groundAtomParameter = 10
    RULE_liftedAtomParameter = 11
    RULE_typedAtomParameter = 12
    RULE_atomParameter = 13
    RULE_atom = 14
    RULE_typedAtom = 15
    RULE_positiveLiteral = 16
    RULE_typedPositiveLiteral = 17
    RULE_negativeLiteral = 18
    RULE_booleanLiteral = 19
    RULE_predicates = 20
    RULE_functions = 21
    RULE_modificator = 22
    RULE_operator = 23
    RULE_comparator = 24
    RULE_number = 25
    RULE_delta = 26
    RULE_constant = 27
    RULE_assignmentSide = 28
    RULE_operationSide = 29
    RULE_operation = 30
    RULE_assignment = 31
    RULE_comparation = 32
    RULE_modification = 33
    RULE_precondition = 34
    RULE_effect = 35
    RULE_andPrecondition = 36
    RULE_andEffect = 37
    RULE_emptyPrecondition = 38
    RULE_preconditions = 39
    RULE_effects = 40
    RULE_parameters = 41
    RULE_opName = 42
    RULE_opParameters = 43
    RULE_opPrecondition = 44
    RULE_opEffect = 45
    RULE_action = 46
    RULE_event = 47
    RULE_process = 48
    RULE_problem = 49
    RULE_problemName = 50
    RULE_problemDomain = 51
    RULE_typedObjects = 52
    RULE_objects = 53
    RULE_init = 54
    RULE_goal = 55
    RULE_metric = 56

    ruleNames =  [ "pddlDoc", "domain", "domainName", "requireKey", "requirements", 
                   "parentType", "typeName", "type", "types", "atomName", 
                   "groundAtomParameter", "liftedAtomParameter", "typedAtomParameter", 
                   "atomParameter", "atom", "typedAtom", "positiveLiteral", 
                   "typedPositiveLiteral", "negativeLiteral", "booleanLiteral", 
                   "predicates", "functions", "modificator", "operator", 
                   "comparator", "number", "delta", "constant", "assignmentSide", 
                   "operationSide", "operation", "assignment", "comparation", 
                   "modification", "precondition", "effect", "andPrecondition", 
                   "andEffect", "emptyPrecondition", "preconditions", "effects", 
                   "parameters", "opName", "opParameters", "opPrecondition", 
                   "opEffect", "action", "event", "process", "problem", 
                   "problemName", "problemDomain", "typedObjects", "objects", 
                   "init", "goal", "metric" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    LP=42
    RP=43
    VAR=44
    NAME=45
    VARIABLE=46
    NUMBER=47
    WS=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PddlDocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def domain(self):
            return self.getTypedRuleContext(pddlParser.DomainContext,0)


        def problem(self):
            return self.getTypedRuleContext(pddlParser.ProblemContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_pddlDoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPddlDoc" ):
                listener.enterPddlDoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPddlDoc" ):
                listener.exitPddlDoc(self)




    def pddlDoc(self):

        localctx = pddlParser.PddlDocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pddlDoc)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.domain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.problem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def domainName(self):
            return self.getTypedRuleContext(pddlParser.DomainNameContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def requirements(self):
            return self.getTypedRuleContext(pddlParser.RequirementsContext,0)


        def types(self):
            return self.getTypedRuleContext(pddlParser.TypesContext,0)


        def predicates(self):
            return self.getTypedRuleContext(pddlParser.PredicatesContext,0)


        def functions(self):
            return self.getTypedRuleContext(pddlParser.FunctionsContext,0)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ActionContext)
            else:
                return self.getTypedRuleContext(pddlParser.ActionContext,i)


        def event(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.EventContext)
            else:
                return self.getTypedRuleContext(pddlParser.EventContext,i)


        def process(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ProcessContext)
            else:
                return self.getTypedRuleContext(pddlParser.ProcessContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)




    def domain(self):

        localctx = pddlParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_domain)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(pddlParser.LP)
            self.state = 119
            self.match(pddlParser.T__0)
            self.state = 120
            self.domainName()
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 121
                self.requirements()


            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 124
                self.types()


            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 127
                self.predicates()


            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 130
                self.functions()


            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 136
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 133
                    self.action()
                    pass

                elif la_ == 2:
                    self.state = 134
                    self.event()
                    pass

                elif la_ == 3:
                    self.state = 135
                    self.process()
                    pass


                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_domainName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomainName" ):
                listener.enterDomainName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomainName" ):
                listener.exitDomainName(self)




    def domainName(self):

        localctx = pddlParser.DomainNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_domainName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(pddlParser.LP)
            self.state = 144
            self.match(pddlParser.T__1)
            self.state = 145
            self.match(pddlParser.NAME)
            self.state = 146
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_requireKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireKey" ):
                listener.enterRequireKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireKey" ):
                listener.exitRequireKey(self)




    def requireKey(self):

        localctx = pddlParser.RequireKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_requireKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequirementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def requireKey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.RequireKeyContext)
            else:
                return self.getTypedRuleContext(pddlParser.RequireKeyContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_requirements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirements" ):
                listener.enterRequirements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirements" ):
                listener.exitRequirements(self)




    def requirements(self):

        localctx = pddlParser.RequirementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_requirements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(pddlParser.LP)
            self.state = 151
            self.match(pddlParser.T__8)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0):
                self.state = 152
                self.requireKey()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParentTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_parentType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentType" ):
                listener.enterParentType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentType" ):
                listener.exitParentType(self)




    def parentType(self):

        localctx = pddlParser.ParentTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(pddlParser.T__9)
            self.state = 161
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = pddlParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def parentType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.ParentTypeContext)
            else:
                return self.getTypedRuleContext(pddlParser.ParentTypeContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = pddlParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.typeName()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 166
                self.parentType()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypeContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypeContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)




    def types(self):

        localctx = pddlParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(pddlParser.LP)
            self.state = 173
            self.match(pddlParser.T__10)
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.type_()
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==45):
                    break

            self.state = 179
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_atomName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomName" ):
                listener.enterAtomName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomName" ):
                listener.exitAtomName(self)




    def atomName(self):

        localctx = pddlParser.AtomNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atomName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroundAtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_groundAtomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroundAtomParameter" ):
                listener.enterGroundAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroundAtomParameter" ):
                listener.exitGroundAtomParameter(self)




    def groundAtomParameter(self):

        localctx = pddlParser.GroundAtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_groundAtomParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiftedAtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(pddlParser.VAR, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_liftedAtomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiftedAtomParameter" ):
                listener.enterLiftedAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiftedAtomParameter" ):
                listener.exitLiftedAtomParameter(self)




    def liftedAtomParameter(self):

        localctx = pddlParser.LiftedAtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_liftedAtomParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(pddlParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedAtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def liftedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.LiftedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_typedAtomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedAtomParameter" ):
                listener.enterTypedAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedAtomParameter" ):
                listener.exitTypedAtomParameter(self)




    def typedAtomParameter(self):

        localctx = pddlParser.TypedAtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typedAtomParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 187
                self.liftedAtomParameter()
                self.state = 190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==44):
                    break

            self.state = 192
            self.match(pddlParser.T__9)
            self.state = 193
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def liftedAtomParameter(self):
            return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,0)


        def groundAtomParameter(self):
            return self.getTypedRuleContext(pddlParser.GroundAtomParameterContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_atomParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomParameter" ):
                listener.enterAtomParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomParameter" ):
                listener.exitAtomParameter(self)




    def atomParameter(self):

        localctx = pddlParser.AtomParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_atomParameter)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.liftedAtomParameter()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.groundAtomParameter()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomName(self):
            return self.getTypedRuleContext(pddlParser.AtomNameContext,0)


        def atomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.AtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = pddlParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.atomName()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44 or _la==45:
                self.state = 200
                self.atomParameter()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomName(self):
            return self.getTypedRuleContext(pddlParser.AtomNameContext,0)


        def typedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_typedAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedAtom" ):
                listener.enterTypedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedAtom" ):
                listener.exitTypedAtom(self)




    def typedAtom(self):

        localctx = pddlParser.TypedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typedAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.atomName()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 207
                self.typedAtomParameter()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositiveLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def atom(self):
            return self.getTypedRuleContext(pddlParser.AtomContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_positiveLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositiveLiteral" ):
                listener.enterPositiveLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositiveLiteral" ):
                listener.exitPositiveLiteral(self)




    def positiveLiteral(self):

        localctx = pddlParser.PositiveLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_positiveLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(pddlParser.LP)

            self.state = 214
            self.atom()
            self.state = 215
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedPositiveLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedAtom(self):
            return self.getTypedRuleContext(pddlParser.TypedAtomContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_typedPositiveLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedPositiveLiteral" ):
                listener.enterTypedPositiveLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedPositiveLiteral" ):
                listener.exitTypedPositiveLiteral(self)




    def typedPositiveLiteral(self):

        localctx = pddlParser.TypedPositiveLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_typedPositiveLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(pddlParser.LP)

            self.state = 218
            self.typedAtom()
            self.state = 219
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegativeLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_negativeLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativeLiteral" ):
                listener.enterNegativeLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativeLiteral" ):
                listener.exitNegativeLiteral(self)




    def negativeLiteral(self):

        localctx = pddlParser.NegativeLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_negativeLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(pddlParser.LP)
            self.state = 222
            self.match(pddlParser.T__11)
            self.state = 223
            self.positiveLiteral()
            self.state = 224
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def negativeLiteral(self):
            return self.getTypedRuleContext(pddlParser.NegativeLiteralContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)




    def booleanLiteral(self):

        localctx = pddlParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_booleanLiteral)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.positiveLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.negativeLiteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicatesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedPositiveLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedPositiveLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedPositiveLiteralContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_predicates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicates" ):
                listener.enterPredicates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicates" ):
                listener.exitPredicates(self)




    def predicates(self):

        localctx = pddlParser.PredicatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_predicates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(pddlParser.LP)
            self.state = 231
            self.match(pddlParser.T__12)
            self.state = 233 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 232
                self.typedPositiveLiteral()
                self.state = 235 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 237
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedPositiveLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedPositiveLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedPositiveLiteralContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = pddlParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(pddlParser.LP)
            self.state = 240
            self.match(pddlParser.T__13)
            self.state = 242 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 241
                self.typedPositiveLiteral()
                self.state = 244 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 246
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModificatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_modificator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModificator" ):
                listener.enterModificator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModificator" ):
                listener.exitModificator(self)




    def modificator(self):

        localctx = pddlParser.ModificatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_modificator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = pddlParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1836032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = pddlParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65011712) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(pddlParser.NUMBER, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = pddlParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(pddlParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeltaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pddlParser.RULE_delta

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelta" ):
                listener.enterDelta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelta" ):
                listener.exitDelta(self)




    def delta(self):

        localctx = pddlParser.DeltaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_delta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(pddlParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(pddlParser.NumberContext,0)


        def delta(self):
            return self.getTypedRuleContext(pddlParser.DeltaContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = pddlParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_constant)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.number()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.delta()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(pddlParser.NumberContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_assignmentSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentSide" ):
                listener.enterAssignmentSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentSide" ):
                listener.exitAssignmentSide(self)




    def assignmentSide(self):

        localctx = pddlParser.AssignmentSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignmentSide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self):
            return self.getTypedRuleContext(pddlParser.OperationContext,0)


        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def constant(self):
            return self.getTypedRuleContext(pddlParser.ConstantContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_operationSide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationSide" ):
                listener.enterOperationSide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationSide" ):
                listener.exitOperationSide(self)




    def operationSide(self):

        localctx = pddlParser.OperationSideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_operationSide)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.positiveLiteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def operator(self):
            return self.getTypedRuleContext(pddlParser.OperatorContext,0)


        def operationSide(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OperationSideContext)
            else:
                return self.getTypedRuleContext(pddlParser.OperationSideContext,i)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = pddlParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(pddlParser.LP)
            self.state = 270
            self.operator()
            self.state = 271
            self.operationSide()
            self.state = 272
            self.operationSide()
            self.state = 273
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def assignmentSide(self):
            return self.getTypedRuleContext(pddlParser.AssignmentSideContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = pddlParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(pddlParser.LP)
            self.state = 276
            self.match(pddlParser.T__24)
            self.state = 277
            self.positiveLiteral()
            self.state = 278
            self.assignmentSide()
            self.state = 279
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def comparator(self):
            return self.getTypedRuleContext(pddlParser.ComparatorContext,0)


        def operationSide(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OperationSideContext)
            else:
                return self.getTypedRuleContext(pddlParser.OperationSideContext,i)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_comparation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparation" ):
                listener.enterComparation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparation" ):
                listener.exitComparation(self)




    def comparation(self):

        localctx = pddlParser.ComparationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_comparation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(pddlParser.LP)
            self.state = 282
            self.comparator()
            self.state = 283
            self.operationSide()
            self.state = 284
            self.operationSide()
            self.state = 285
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def modificator(self):
            return self.getTypedRuleContext(pddlParser.ModificatorContext,0)


        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def operationSide(self):
            return self.getTypedRuleContext(pddlParser.OperationSideContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_modification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModification" ):
                listener.enterModification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModification" ):
                listener.exitModification(self)




    def modification(self):

        localctx = pddlParser.ModificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_modification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(pddlParser.LP)
            self.state = 288
            self.modificator()
            self.state = 289
            self.positiveLiteral()
            self.state = 290
            self.operationSide()
            self.state = 291
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_precondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecondition" ):
                listener.enterPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecondition" ):
                listener.exitPrecondition(self)




    def precondition(self):

        localctx = pddlParser.PreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_precondition)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.comparation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_effect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect" ):
                listener.enterEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect" ):
                listener.exitEffect(self)




    def effect(self):

        localctx = pddlParser.EffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_effect)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.modification()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndPreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def precondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.PreconditionContext)
            else:
                return self.getTypedRuleContext(pddlParser.PreconditionContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andPrecondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndPrecondition" ):
                listener.enterAndPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndPrecondition" ):
                listener.exitAndPrecondition(self)




    def andPrecondition(self):

        localctx = pddlParser.AndPreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_andPrecondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(pddlParser.LP)
            self.state = 302
            self.match(pddlParser.T__26)
            self.state = 304 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 303
                self.precondition()
                self.state = 306 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 308
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def effect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.EffectContext)
            else:
                return self.getTypedRuleContext(pddlParser.EffectContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_andEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndEffect" ):
                listener.enterAndEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndEffect" ):
                listener.exitAndEffect(self)




    def andEffect(self):

        localctx = pddlParser.AndEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_andEffect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(pddlParser.LP)
            self.state = 311
            self.match(pddlParser.T__26)
            self.state = 313 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 312
                self.effect()
                self.state = 315 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 317
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyPreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_emptyPrecondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyPrecondition" ):
                listener.enterEmptyPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyPrecondition" ):
                listener.exitEmptyPrecondition(self)




    def emptyPrecondition(self):

        localctx = pddlParser.EmptyPreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_emptyPrecondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(pddlParser.LP)
            self.state = 320
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreconditionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precondition(self):
            return self.getTypedRuleContext(pddlParser.PreconditionContext,0)


        def andPrecondition(self):
            return self.getTypedRuleContext(pddlParser.AndPreconditionContext,0)


        def emptyPrecondition(self):
            return self.getTypedRuleContext(pddlParser.EmptyPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_preconditions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreconditions" ):
                listener.enterPreconditions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreconditions" ):
                listener.exitPreconditions(self)




    def preconditions(self):

        localctx = pddlParser.PreconditionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_preconditions)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.precondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.andPrecondition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.emptyPrecondition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EffectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effect(self):
            return self.getTypedRuleContext(pddlParser.EffectContext,0)


        def andEffect(self):
            return self.getTypedRuleContext(pddlParser.AndEffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_effects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffects" ):
                listener.enterEffects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffects" ):
                listener.exitEffects(self)




    def effects(self):

        localctx = pddlParser.EffectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_effects)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.effect()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.andEffect()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = pddlParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(pddlParser.LP)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 332
                self.typedAtomParameter()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 338
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_opName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpName" ):
                listener.enterOpName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpName" ):
                listener.exitOpName(self)




    def opName(self):

        localctx = pddlParser.OpNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_opName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(pddlParser.ParametersContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpParameters" ):
                listener.enterOpParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpParameters" ):
                listener.exitOpParameters(self)




    def opParameters(self):

        localctx = pddlParser.OpParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_opParameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(pddlParser.T__27)
            self.state = 343
            self.parameters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpPreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preconditions(self):
            return self.getTypedRuleContext(pddlParser.PreconditionsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opPrecondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpPrecondition" ):
                listener.enterOpPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpPrecondition" ):
                listener.exitOpPrecondition(self)




    def opPrecondition(self):

        localctx = pddlParser.OpPreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_opPrecondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(pddlParser.T__28)
            self.state = 346
            self.preconditions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effects(self):
            return self.getTypedRuleContext(pddlParser.EffectsContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_opEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpEffect" ):
                listener.enterOpEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpEffect" ):
                listener.exitOpEffect(self)




    def opEffect(self):

        localctx = pddlParser.OpEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_opEffect)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(pddlParser.T__29)
            self.state = 349
            self.effects()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opEffect(self):
            return self.getTypedRuleContext(pddlParser.OpEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opPrecondition(self):
            return self.getTypedRuleContext(pddlParser.OpPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = pddlParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(pddlParser.LP)
            self.state = 352
            self.match(pddlParser.T__30)
            self.state = 353
            self.opName()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 354
                self.opParameters()


            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 357
                self.opPrecondition()


            self.state = 360
            self.opEffect()
            self.state = 361
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opEffect(self):
            return self.getTypedRuleContext(pddlParser.OpEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opPrecondition(self):
            return self.getTypedRuleContext(pddlParser.OpPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_event

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent" ):
                listener.enterEvent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent" ):
                listener.exitEvent(self)




    def event(self):

        localctx = pddlParser.EventContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_event)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(pddlParser.LP)
            self.state = 364
            self.match(pddlParser.T__31)
            self.state = 365
            self.opName()
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 366
                self.opParameters()


            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 369
                self.opPrecondition()


            self.state = 372
            self.opEffect()
            self.state = 373
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def opName(self):
            return self.getTypedRuleContext(pddlParser.OpNameContext,0)


        def opEffect(self):
            return self.getTypedRuleContext(pddlParser.OpEffectContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def opParameters(self):
            return self.getTypedRuleContext(pddlParser.OpParametersContext,0)


        def opPrecondition(self):
            return self.getTypedRuleContext(pddlParser.OpPreconditionContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_process

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcess" ):
                listener.enterProcess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcess" ):
                listener.exitProcess(self)




    def process(self):

        localctx = pddlParser.ProcessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(pddlParser.LP)
            self.state = 376
            self.match(pddlParser.T__32)
            self.state = 377
            self.opName()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 378
                self.opParameters()


            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 381
                self.opPrecondition()


            self.state = 384
            self.opEffect()
            self.state = 385
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def problemName(self):
            return self.getTypedRuleContext(pddlParser.ProblemNameContext,0)


        def problemDomain(self):
            return self.getTypedRuleContext(pddlParser.ProblemDomainContext,0)


        def init(self):
            return self.getTypedRuleContext(pddlParser.InitContext,0)


        def goal(self):
            return self.getTypedRuleContext(pddlParser.GoalContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def objects(self):
            return self.getTypedRuleContext(pddlParser.ObjectsContext,0)


        def metric(self):
            return self.getTypedRuleContext(pddlParser.MetricContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_problem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblem" ):
                listener.enterProblem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblem" ):
                listener.exitProblem(self)




    def problem(self):

        localctx = pddlParser.ProblemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_problem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(pddlParser.LP)
            self.state = 388
            self.match(pddlParser.T__0)
            self.state = 389
            self.problemName()
            self.state = 390
            self.problemDomain()
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 391
                self.objects()


            self.state = 394
            self.init()
            self.state = 395
            self.goal()
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 396
                self.metric()


            self.state = 399
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_problemName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemName" ):
                listener.enterProblemName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemName" ):
                listener.exitProblemName(self)




    def problemName(self):

        localctx = pddlParser.ProblemNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_problemName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(pddlParser.LP)
            self.state = 402
            self.match(pddlParser.T__33)
            self.state = 403
            self.match(pddlParser.NAME)
            self.state = 404
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemDomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_problemDomain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemDomain" ):
                listener.enterProblemDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemDomain" ):
                listener.exitProblemDomain(self)




    def problemDomain(self):

        localctx = pddlParser.ProblemDomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_problemDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(pddlParser.LP)
            self.state = 407
            self.match(pddlParser.T__34)
            self.state = 408
            self.match(pddlParser.NAME)
            self.state = 409
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedObjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(pddlParser.TypeNameContext,0)


        def groundAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.GroundAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.GroundAtomParameterContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_typedObjects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedObjects" ):
                listener.enterTypedObjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedObjects" ):
                listener.exitTypedObjects(self)




    def typedObjects(self):

        localctx = pddlParser.TypedObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_typedObjects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 411
                self.groundAtomParameter()
                self.state = 414 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==45):
                    break

            self.state = 416
            self.match(pddlParser.T__9)
            self.state = 417
            self.typeName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def typedObjects(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedObjectsContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedObjectsContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_objects

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjects" ):
                listener.enterObjects(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjects" ):
                listener.exitObjects(self)




    def objects(self):

        localctx = pddlParser.ObjectsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_objects)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(pddlParser.LP)
            self.state = 420
            self.match(pddlParser.T__35)
            self.state = 422 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 421
                self.typedObjects()
                self.state = 424 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==45):
                    break

            self.state = 426
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def positiveLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.PositiveLiteralContext)
            else:
                return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,i)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(pddlParser.AssignmentContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)




    def init(self):

        localctx = pddlParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(pddlParser.LP)
            self.state = 429
            self.match(pddlParser.T__36)
            self.state = 432 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 432
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 430
                    self.positiveLiteral()
                    pass

                elif la_ == 2:
                    self.state = 431
                    self.assignment()
                    pass


                self.state = 434 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 436
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def preconditions(self):
            return self.getTypedRuleContext(pddlParser.PreconditionsContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal" ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal" ):
                listener.exitGoal(self)




    def goal(self):

        localctx = pddlParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(pddlParser.LP)
            self.state = 439
            self.match(pddlParser.T__37)
            self.state = 440
            self.preconditions()
            self.state = 441
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetricContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def operation(self):
            return self.getTypedRuleContext(pddlParser.OperationContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_metric

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetric" ):
                listener.enterMetric(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetric" ):
                listener.exitMetric(self)




    def metric(self):

        localctx = pddlParser.MetricContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_metric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(pddlParser.LP)
            self.state = 444
            self.match(pddlParser.T__38)
            self.state = 445
            _la = self._input.LA(1)
            if not(_la==40 or _la==41):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 446
            self.operation()
            self.state = 447
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





