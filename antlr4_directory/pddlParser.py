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
        4,1,47,661,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,3,0,115,8,0,1,1,1,1,1,1,1,
        1,3,1,121,8,1,1,1,3,1,124,8,1,1,1,3,1,127,8,1,1,1,3,1,130,8,1,1,
        1,5,1,133,8,1,10,1,12,1,136,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,4,3,148,8,3,11,3,12,3,149,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,
        4,159,8,4,4,4,161,8,4,11,4,12,4,162,1,4,1,4,1,5,1,5,1,5,4,5,170,
        8,5,11,5,12,5,171,1,5,1,5,1,6,1,6,1,6,5,6,179,8,6,10,6,12,6,182,
        9,6,1,6,1,6,1,7,1,7,1,7,4,7,189,8,7,11,7,12,7,190,1,7,1,7,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,4,9,202,8,9,11,9,12,9,203,1,9,1,9,1,10,1,10,
        1,10,5,10,211,8,10,10,10,12,10,214,9,10,1,10,1,10,1,11,1,11,5,11,
        220,8,11,10,11,12,11,223,9,11,1,12,1,12,1,12,3,12,228,8,12,1,13,
        1,13,1,13,1,13,1,13,1,13,5,13,236,8,13,10,13,12,13,239,9,13,1,13,
        1,13,3,13,243,8,13,1,13,3,13,246,8,13,1,13,1,13,1,14,1,14,1,14,1,
        14,5,14,254,8,14,10,14,12,14,257,9,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,3,15,266,8,15,1,16,1,16,1,16,1,16,4,16,272,8,16,11,16,12,
        16,273,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,347,8,17,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,427,8,
        18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,435,8,19,10,19,12,19,438,9,
        19,1,19,1,19,3,19,442,8,19,1,19,3,19,445,8,19,1,19,1,19,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,455,8,20,10,20,12,20,458,9,20,1,20,1,20,
        3,20,462,8,20,1,20,3,20,465,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,
        21,3,21,474,8,21,1,21,1,21,1,21,3,21,479,8,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,4,24,496,
        8,24,11,24,12,24,497,1,24,1,24,1,25,4,25,503,8,25,11,25,12,25,504,
        1,25,1,25,1,25,1,26,1,26,1,26,5,26,513,8,26,10,26,12,26,516,9,26,
        1,26,1,26,1,27,1,27,4,27,522,8,27,11,27,12,27,523,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,1,29,1,29,3,29,536,8,29,1,30,1,30,1,30,
        1,30,1,30,1,30,3,30,544,8,30,1,31,1,31,1,32,1,32,1,33,1,33,1,33,
        1,34,1,34,4,34,555,8,34,11,34,12,34,556,1,34,4,34,560,8,34,11,34,
        12,34,561,3,34,564,8,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,
        1,36,1,37,1,37,3,37,577,8,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,
        1,41,1,42,1,42,1,43,1,43,3,43,591,8,43,1,44,1,44,1,44,3,44,596,8,
        44,1,45,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,
        47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,3,48,618,8,48,1,49,1,49,3,
        49,622,8,49,1,50,1,50,1,50,4,50,627,8,50,11,50,12,50,628,1,50,1,
        50,1,51,1,51,1,51,4,51,636,8,51,11,51,12,51,637,1,51,1,51,1,52,1,
        52,3,52,644,8,52,1,53,1,53,3,53,648,8,53,1,54,1,54,1,54,1,54,1,54,
        1,55,1,55,1,55,1,55,1,55,1,55,1,55,0,0,56,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,
        104,106,108,110,0,5,3,0,1,1,5,12,47,47,2,0,4,4,39,40,2,0,1,1,10,
        12,3,0,5,6,8,9,17,17,1,0,20,21,673,0,114,1,0,0,0,2,116,1,0,0,0,4,
        139,1,0,0,0,6,144,1,0,0,0,8,153,1,0,0,0,10,166,1,0,0,0,12,175,1,
        0,0,0,14,185,1,0,0,0,16,194,1,0,0,0,18,198,1,0,0,0,20,207,1,0,0,
        0,22,217,1,0,0,0,24,227,1,0,0,0,26,229,1,0,0,0,28,249,1,0,0,0,30,
        265,1,0,0,0,32,267,1,0,0,0,34,346,1,0,0,0,36,426,1,0,0,0,38,428,
        1,0,0,0,40,448,1,0,0,0,42,468,1,0,0,0,44,482,1,0,0,0,46,487,1,0,
        0,0,48,492,1,0,0,0,50,502,1,0,0,0,52,509,1,0,0,0,54,519,1,0,0,0,
        56,527,1,0,0,0,58,535,1,0,0,0,60,543,1,0,0,0,62,545,1,0,0,0,64,547,
        1,0,0,0,66,549,1,0,0,0,68,552,1,0,0,0,70,565,1,0,0,0,72,569,1,0,
        0,0,74,576,1,0,0,0,76,578,1,0,0,0,78,580,1,0,0,0,80,582,1,0,0,0,
        82,584,1,0,0,0,84,586,1,0,0,0,86,590,1,0,0,0,88,595,1,0,0,0,90,597,
        1,0,0,0,92,603,1,0,0,0,94,609,1,0,0,0,96,617,1,0,0,0,98,621,1,0,
        0,0,100,623,1,0,0,0,102,632,1,0,0,0,104,643,1,0,0,0,106,647,1,0,
        0,0,108,649,1,0,0,0,110,654,1,0,0,0,112,115,3,2,1,0,113,115,3,42,
        21,0,114,112,1,0,0,0,114,113,1,0,0,0,115,1,1,0,0,0,116,117,5,22,
        0,0,117,118,5,26,0,0,118,120,3,4,2,0,119,121,3,6,3,0,120,119,1,0,
        0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,124,3,8,4,0,123,122,1,0,
        0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,127,3,10,5,0,126,125,1,0,
        0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,130,3,18,9,0,129,128,1,0,
        0,0,129,130,1,0,0,0,130,134,1,0,0,0,131,133,3,24,12,0,132,131,1,
        0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,137,1,
        0,0,0,136,134,1,0,0,0,137,138,5,23,0,0,138,3,1,0,0,0,139,140,5,22,
        0,0,140,141,5,28,0,0,141,142,5,42,0,0,142,143,5,23,0,0,143,5,1,0,
        0,0,144,145,5,22,0,0,145,147,5,29,0,0,146,148,5,46,0,0,147,146,1,
        0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,151,1,
        0,0,0,151,152,5,23,0,0,152,7,1,0,0,0,153,154,5,22,0,0,154,160,5,
        30,0,0,155,158,5,42,0,0,156,157,5,1,0,0,157,159,5,42,0,0,158,156,
        1,0,0,0,158,159,1,0,0,0,159,161,1,0,0,0,160,155,1,0,0,0,161,162,
        1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,
        5,23,0,0,165,9,1,0,0,0,166,167,5,22,0,0,167,169,5,31,0,0,168,170,
        3,12,6,0,169,168,1,0,0,0,170,171,1,0,0,0,171,169,1,0,0,0,171,172,
        1,0,0,0,172,173,1,0,0,0,173,174,5,23,0,0,174,11,1,0,0,0,175,176,
        5,22,0,0,176,180,5,42,0,0,177,179,3,16,8,0,178,177,1,0,0,0,179,182,
        1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,180,
        1,0,0,0,183,184,5,23,0,0,184,13,1,0,0,0,185,186,5,22,0,0,186,188,
        5,42,0,0,187,189,3,16,8,0,188,187,1,0,0,0,189,190,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,5,23,0,0,193,15,
        1,0,0,0,194,195,5,43,0,0,195,196,5,1,0,0,196,197,5,42,0,0,197,17,
        1,0,0,0,198,199,5,22,0,0,199,201,5,32,0,0,200,202,3,20,10,0,201,
        200,1,0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,
        205,1,0,0,0,205,206,5,23,0,0,206,19,1,0,0,0,207,208,5,22,0,0,208,
        212,5,42,0,0,209,211,3,16,8,0,210,209,1,0,0,0,211,214,1,0,0,0,212,
        210,1,0,0,0,212,213,1,0,0,0,213,215,1,0,0,0,214,212,1,0,0,0,215,
        216,5,23,0,0,216,21,1,0,0,0,217,221,5,42,0,0,218,220,5,43,0,0,219,
        218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,
        23,1,0,0,0,223,221,1,0,0,0,224,228,3,26,13,0,225,228,3,38,19,0,226,
        228,3,40,20,0,227,224,1,0,0,0,227,225,1,0,0,0,227,226,1,0,0,0,228,
        25,1,0,0,0,229,230,5,22,0,0,230,231,5,33,0,0,231,232,5,42,0,0,232,
        233,5,34,0,0,233,237,5,22,0,0,234,236,3,16,8,0,235,234,1,0,0,0,236,
        239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,240,1,0,0,0,239,
        237,1,0,0,0,240,242,5,23,0,0,241,243,3,28,14,0,242,241,1,0,0,0,242,
        243,1,0,0,0,243,245,1,0,0,0,244,246,3,32,16,0,245,244,1,0,0,0,245,
        246,1,0,0,0,246,247,1,0,0,0,247,248,5,23,0,0,248,27,1,0,0,0,249,
        250,5,35,0,0,250,251,5,22,0,0,251,255,5,2,0,0,252,254,3,30,15,0,
        253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,
        256,258,1,0,0,0,257,255,1,0,0,0,258,259,5,23,0,0,259,29,1,0,0,0,
        260,261,5,22,0,0,261,262,3,22,11,0,262,263,5,23,0,0,263,266,1,0,
        0,0,264,266,3,36,18,0,265,260,1,0,0,0,265,264,1,0,0,0,266,31,1,0,
        0,0,267,268,5,36,0,0,268,269,5,22,0,0,269,271,5,2,0,0,270,272,3,
        34,17,0,271,270,1,0,0,0,272,273,1,0,0,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,275,1,0,0,0,275,276,5,23,0,0,276,33,1,0,0,0,277,278,
        5,22,0,0,278,279,3,22,11,0,279,280,5,23,0,0,280,347,1,0,0,0,281,
        282,5,22,0,0,282,283,5,3,0,0,283,284,5,22,0,0,284,285,3,22,11,0,
        285,286,5,23,0,0,286,287,5,23,0,0,287,347,1,0,0,0,288,289,5,22,0,
        0,289,290,5,4,0,0,290,291,5,22,0,0,291,292,3,22,11,0,292,293,5,23,
        0,0,293,294,5,44,0,0,294,295,5,23,0,0,295,347,1,0,0,0,296,297,5,
        22,0,0,297,298,5,39,0,0,298,299,5,22,0,0,299,300,3,22,11,0,300,301,
        5,23,0,0,301,302,5,44,0,0,302,303,5,23,0,0,303,347,1,0,0,0,304,305,
        5,22,0,0,305,306,5,40,0,0,306,307,5,22,0,0,307,308,3,22,11,0,308,
        309,5,23,0,0,309,310,5,44,0,0,310,311,5,23,0,0,311,347,1,0,0,0,312,
        313,5,22,0,0,313,314,5,4,0,0,314,315,5,22,0,0,315,316,3,22,11,0,
        316,317,5,23,0,0,317,318,3,36,18,0,318,319,5,23,0,0,319,347,1,0,
        0,0,320,321,5,22,0,0,321,322,5,39,0,0,322,323,5,22,0,0,323,324,3,
        22,11,0,324,325,5,23,0,0,325,326,3,36,18,0,326,327,5,23,0,0,327,
        347,1,0,0,0,328,329,5,22,0,0,329,330,5,40,0,0,330,331,5,22,0,0,331,
        332,3,22,11,0,332,333,5,23,0,0,333,334,3,36,18,0,334,335,5,23,0,
        0,335,347,1,0,0,0,336,337,5,22,0,0,337,338,5,4,0,0,338,339,5,22,
        0,0,339,340,3,22,11,0,340,341,5,23,0,0,341,342,5,22,0,0,342,343,
        3,22,11,0,343,344,5,23,0,0,344,345,5,23,0,0,345,347,1,0,0,0,346,
        277,1,0,0,0,346,281,1,0,0,0,346,288,1,0,0,0,346,296,1,0,0,0,346,
        304,1,0,0,0,346,312,1,0,0,0,346,320,1,0,0,0,346,328,1,0,0,0,346,
        336,1,0,0,0,347,35,1,0,0,0,348,349,5,22,0,0,349,350,7,0,0,0,350,
        351,5,22,0,0,351,352,3,22,11,0,352,353,5,23,0,0,353,354,5,44,0,0,
        354,355,5,23,0,0,355,427,1,0,0,0,356,357,5,22,0,0,357,358,7,0,0,
        0,358,359,5,44,0,0,359,360,5,22,0,0,360,361,3,22,11,0,361,362,5,
        23,0,0,362,363,5,23,0,0,363,427,1,0,0,0,364,365,5,22,0,0,365,366,
        7,0,0,0,366,367,5,44,0,0,367,368,5,44,0,0,368,427,5,23,0,0,369,370,
        5,22,0,0,370,371,7,0,0,0,371,372,5,22,0,0,372,373,3,22,11,0,373,
        374,5,23,0,0,374,375,5,22,0,0,375,376,3,22,11,0,376,377,5,23,0,0,
        377,378,5,23,0,0,378,427,1,0,0,0,379,380,5,22,0,0,380,381,7,0,0,
        0,381,382,5,22,0,0,382,383,3,22,11,0,383,384,5,23,0,0,384,385,3,
        36,18,0,385,386,5,23,0,0,386,427,1,0,0,0,387,388,5,22,0,0,388,389,
        7,0,0,0,389,390,3,36,18,0,390,391,5,22,0,0,391,392,3,22,11,0,392,
        393,5,23,0,0,393,394,5,23,0,0,394,427,1,0,0,0,395,396,5,22,0,0,396,
        397,7,0,0,0,397,398,5,44,0,0,398,399,3,36,18,0,399,400,5,23,0,0,
        400,427,1,0,0,0,401,402,5,22,0,0,402,403,7,0,0,0,403,404,3,36,18,
        0,404,405,3,36,18,0,405,406,5,23,0,0,406,427,1,0,0,0,407,408,5,22,
        0,0,408,409,7,0,0,0,409,410,3,36,18,0,410,411,5,44,0,0,411,412,5,
        23,0,0,412,427,1,0,0,0,413,414,5,22,0,0,414,415,5,3,0,0,415,416,
        3,36,18,0,416,417,5,23,0,0,417,427,1,0,0,0,418,419,5,22,0,0,419,
        420,5,3,0,0,420,421,5,22,0,0,421,422,3,22,11,0,422,423,5,23,0,0,
        423,424,5,23,0,0,424,427,1,0,0,0,425,427,5,44,0,0,426,348,1,0,0,
        0,426,356,1,0,0,0,426,364,1,0,0,0,426,369,1,0,0,0,426,379,1,0,0,
        0,426,387,1,0,0,0,426,395,1,0,0,0,426,401,1,0,0,0,426,407,1,0,0,
        0,426,413,1,0,0,0,426,418,1,0,0,0,426,425,1,0,0,0,427,37,1,0,0,0,
        428,429,5,22,0,0,429,430,5,37,0,0,430,431,5,42,0,0,431,432,5,34,
        0,0,432,436,5,22,0,0,433,435,3,16,8,0,434,433,1,0,0,0,435,438,1,
        0,0,0,436,434,1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,436,1,
        0,0,0,439,441,5,23,0,0,440,442,3,28,14,0,441,440,1,0,0,0,441,442,
        1,0,0,0,442,444,1,0,0,0,443,445,3,32,16,0,444,443,1,0,0,0,444,445,
        1,0,0,0,445,446,1,0,0,0,446,447,5,23,0,0,447,39,1,0,0,0,448,449,
        5,22,0,0,449,450,5,38,0,0,450,451,5,42,0,0,451,452,5,34,0,0,452,
        456,5,22,0,0,453,455,3,16,8,0,454,453,1,0,0,0,455,458,1,0,0,0,456,
        454,1,0,0,0,456,457,1,0,0,0,457,459,1,0,0,0,458,456,1,0,0,0,459,
        461,5,23,0,0,460,462,3,28,14,0,461,460,1,0,0,0,461,462,1,0,0,0,462,
        464,1,0,0,0,463,465,3,32,16,0,464,463,1,0,0,0,464,465,1,0,0,0,465,
        466,1,0,0,0,466,467,5,23,0,0,467,41,1,0,0,0,468,469,5,22,0,0,469,
        470,5,26,0,0,470,471,3,44,22,0,471,473,3,46,23,0,472,474,3,48,24,
        0,473,472,1,0,0,0,473,474,1,0,0,0,474,475,1,0,0,0,475,476,3,52,26,
        0,476,478,3,108,54,0,477,479,3,110,55,0,478,477,1,0,0,0,478,479,
        1,0,0,0,479,480,1,0,0,0,480,481,5,23,0,0,481,43,1,0,0,0,482,483,
        5,22,0,0,483,484,5,27,0,0,484,485,5,42,0,0,485,486,5,23,0,0,486,
        45,1,0,0,0,487,488,5,22,0,0,488,489,5,13,0,0,489,490,5,42,0,0,490,
        491,5,23,0,0,491,47,1,0,0,0,492,493,5,22,0,0,493,495,5,14,0,0,494,
        496,3,50,25,0,495,494,1,0,0,0,496,497,1,0,0,0,497,495,1,0,0,0,497,
        498,1,0,0,0,498,499,1,0,0,0,499,500,5,23,0,0,500,49,1,0,0,0,501,
        503,5,42,0,0,502,501,1,0,0,0,503,504,1,0,0,0,504,502,1,0,0,0,504,
        505,1,0,0,0,505,506,1,0,0,0,506,507,5,1,0,0,507,508,5,42,0,0,508,
        51,1,0,0,0,509,510,5,22,0,0,510,514,5,15,0,0,511,513,3,58,29,0,512,
        511,1,0,0,0,513,516,1,0,0,0,514,512,1,0,0,0,514,515,1,0,0,0,515,
        517,1,0,0,0,516,514,1,0,0,0,517,518,5,23,0,0,518,53,1,0,0,0,519,
        521,5,22,0,0,520,522,5,42,0,0,521,520,1,0,0,0,522,523,1,0,0,0,523,
        521,1,0,0,0,523,524,1,0,0,0,524,525,1,0,0,0,525,526,5,23,0,0,526,
        55,1,0,0,0,527,528,5,22,0,0,528,529,5,5,0,0,529,530,3,54,27,0,530,
        531,5,44,0,0,531,532,5,23,0,0,532,57,1,0,0,0,533,536,3,60,30,0,534,
        536,3,56,28,0,535,533,1,0,0,0,535,534,1,0,0,0,536,59,1,0,0,0,537,
        544,3,54,27,0,538,539,5,22,0,0,539,540,5,3,0,0,540,541,3,54,27,0,
        541,542,5,23,0,0,542,544,1,0,0,0,543,537,1,0,0,0,543,538,1,0,0,0,
        544,61,1,0,0,0,545,546,5,42,0,0,546,63,1,0,0,0,547,548,5,42,0,0,
        548,65,1,0,0,0,549,550,5,16,0,0,550,551,5,42,0,0,551,67,1,0,0,0,
        552,563,3,62,31,0,553,555,3,64,32,0,554,553,1,0,0,0,555,556,1,0,
        0,0,556,554,1,0,0,0,556,557,1,0,0,0,557,564,1,0,0,0,558,560,3,66,
        33,0,559,558,1,0,0,0,560,561,1,0,0,0,561,559,1,0,0,0,561,562,1,0,
        0,0,562,564,1,0,0,0,563,554,1,0,0,0,563,559,1,0,0,0,564,69,1,0,0,
        0,565,566,5,22,0,0,566,567,3,68,34,0,567,568,5,23,0,0,568,71,1,0,
        0,0,569,570,5,22,0,0,570,571,5,3,0,0,571,572,3,70,35,0,572,573,5,
        23,0,0,573,73,1,0,0,0,574,577,3,70,35,0,575,577,3,72,36,0,576,574,
        1,0,0,0,576,575,1,0,0,0,577,75,1,0,0,0,578,579,7,1,0,0,579,77,1,
        0,0,0,580,581,7,2,0,0,581,79,1,0,0,0,582,583,7,3,0,0,583,81,1,0,
        0,0,584,585,5,44,0,0,585,83,1,0,0,0,586,587,5,41,0,0,587,85,1,0,
        0,0,588,591,3,82,41,0,589,591,3,84,42,0,590,588,1,0,0,0,590,589,
        1,0,0,0,591,87,1,0,0,0,592,596,3,90,45,0,593,596,3,70,35,0,594,596,
        3,86,43,0,595,592,1,0,0,0,595,593,1,0,0,0,595,594,1,0,0,0,596,89,
        1,0,0,0,597,598,5,22,0,0,598,599,3,78,39,0,599,600,3,88,44,0,600,
        601,3,88,44,0,601,602,5,23,0,0,602,91,1,0,0,0,603,604,5,22,0,0,604,
        605,3,80,40,0,605,606,3,70,35,0,606,607,3,88,44,0,607,608,5,23,0,
        0,608,93,1,0,0,0,609,610,5,22,0,0,610,611,3,76,38,0,611,612,3,70,
        35,0,612,613,3,88,44,0,613,614,5,23,0,0,614,95,1,0,0,0,615,618,3,
        74,37,0,616,618,3,92,46,0,617,615,1,0,0,0,617,616,1,0,0,0,618,97,
        1,0,0,0,619,622,3,74,37,0,620,622,3,94,47,0,621,619,1,0,0,0,621,
        620,1,0,0,0,622,99,1,0,0,0,623,624,5,22,0,0,624,626,5,2,0,0,625,
        627,3,96,48,0,626,625,1,0,0,0,627,628,1,0,0,0,628,626,1,0,0,0,628,
        629,1,0,0,0,629,630,1,0,0,0,630,631,5,23,0,0,631,101,1,0,0,0,632,
        633,5,22,0,0,633,635,5,2,0,0,634,636,3,98,49,0,635,634,1,0,0,0,636,
        637,1,0,0,0,637,635,1,0,0,0,637,638,1,0,0,0,638,639,1,0,0,0,639,
        640,5,23,0,0,640,103,1,0,0,0,641,644,3,96,48,0,642,644,3,100,50,
        0,643,641,1,0,0,0,643,642,1,0,0,0,644,105,1,0,0,0,645,648,3,98,49,
        0,646,648,3,102,51,0,647,645,1,0,0,0,647,646,1,0,0,0,648,107,1,0,
        0,0,649,650,5,22,0,0,650,651,5,18,0,0,651,652,3,104,52,0,652,653,
        5,23,0,0,653,109,1,0,0,0,654,655,5,22,0,0,655,656,5,19,0,0,656,657,
        7,4,0,0,657,658,3,54,27,0,658,659,5,23,0,0,659,111,1,0,0,0,50,114,
        120,123,126,129,134,149,158,162,171,180,190,203,212,221,227,237,
        242,245,255,265,273,346,426,436,441,444,456,461,464,473,478,497,
        504,514,523,535,543,556,561,563,576,590,595,617,621,628,637,643,
        647
    ]

class pddlParser ( Parser ):

    grammarFileName = "pddl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'and'", "'not'", "'assign'", "'='", 
                     "'<'", "'=<'", "'>='", "'>'", "'+'", "'*'", "'/'", 
                     "':domain'", "':objects'", "':init'", "'?'", "'<='", 
                     "':goal'", "':metric'", "'maximize'", "'minimize'", 
                     "'('", "')'", "'\"'", "','", "'define'", "'problem'", 
                     "'domain'", "':requirements'", "':types'", "':predicates'", 
                     "':functions'", "':action'", "':parameters'", "':precondition'", 
                     "':effect'", "':process'", "':event'", "'increase'", 
                     "'decrease'", "'#t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LP", "RP", "QUOTE", "COMMA", 
                      "DEFINE", "PROBLEM", "DOMAIN", "REQUIREMENTS", "TYPES", 
                      "PREDICATES", "FUNCTIONS", "ACTION", "PARAMETERS", 
                      "PRECONDITION", "EFFECT", "PROCESS", "EVENT", "INCREASE", 
                      "DECREASE", "DELTA", "NAME", "VARIABLE", "NUMBER", 
                      "WS", "REQUIRE_KEY", "OPERATION" ]

    RULE_pddlDoc = 0
    RULE_domain = 1
    RULE_domainName = 2
    RULE_requireDef = 3
    RULE_typesDef = 4
    RULE_predicatesDef = 5
    RULE_predicate = 6
    RULE_atomicFormulaSkeleton = 7
    RULE_typedVariable = 8
    RULE_functionsDef = 9
    RULE_function = 10
    RULE_predicatedVariables = 11
    RULE_structureDef = 12
    RULE_actionDef = 13
    RULE_precondition = 14
    RULE_precondition_formula = 15
    RULE_effect = 16
    RULE_effect_formula = 17
    RULE_operation = 18
    RULE_processDef = 19
    RULE_eventDef = 20
    RULE_problem = 21
    RULE_problemDecl = 22
    RULE_problemDomain = 23
    RULE_objectDecl = 24
    RULE_sameTypeNamesList = 25
    RULE_init = 26
    RULE_atomicNameFormula = 27
    RULE_equalLiteral = 28
    RULE_initEl = 29
    RULE_nameLiteral = 30
    RULE_atomName = 31
    RULE_groundAtomParameter = 32
    RULE_liftedAtomParameter = 33
    RULE_atom = 34
    RULE_positiveLiteral = 35
    RULE_negativeLiteral = 36
    RULE_booleanLiteral = 37
    RULE_modificator = 38
    RULE_operator = 39
    RULE_comparator = 40
    RULE_number = 41
    RULE_delta = 42
    RULE_constant = 43
    RULE_operationSide = 44
    RULE_nOperation = 45
    RULE_comparation = 46
    RULE_modification = 47
    RULE_nPrecondition = 48
    RULE_nEffect = 49
    RULE_andPrecondition = 50
    RULE_andEffect = 51
    RULE_preconditions = 52
    RULE_effects = 53
    RULE_goal = 54
    RULE_metric = 55

    ruleNames =  [ "pddlDoc", "domain", "domainName", "requireDef", "typesDef", 
                   "predicatesDef", "predicate", "atomicFormulaSkeleton", 
                   "typedVariable", "functionsDef", "function", "predicatedVariables", 
                   "structureDef", "actionDef", "precondition", "precondition_formula", 
                   "effect", "effect_formula", "operation", "processDef", 
                   "eventDef", "problem", "problemDecl", "problemDomain", 
                   "objectDecl", "sameTypeNamesList", "init", "atomicNameFormula", 
                   "equalLiteral", "initEl", "nameLiteral", "atomName", 
                   "groundAtomParameter", "liftedAtomParameter", "atom", 
                   "positiveLiteral", "negativeLiteral", "booleanLiteral", 
                   "modificator", "operator", "comparator", "number", "delta", 
                   "constant", "operationSide", "nOperation", "comparation", 
                   "modification", "nPrecondition", "nEffect", "andPrecondition", 
                   "andEffect", "preconditions", "effects", "goal", "metric" ]

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
    LP=22
    RP=23
    QUOTE=24
    COMMA=25
    DEFINE=26
    PROBLEM=27
    DOMAIN=28
    REQUIREMENTS=29
    TYPES=30
    PREDICATES=31
    FUNCTIONS=32
    ACTION=33
    PARAMETERS=34
    PRECONDITION=35
    EFFECT=36
    PROCESS=37
    EVENT=38
    INCREASE=39
    DECREASE=40
    DELTA=41
    NAME=42
    VARIABLE=43
    NUMBER=44
    WS=45
    REQUIRE_KEY=46
    OPERATION=47

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
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.domain()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
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

        def DEFINE(self):
            return self.getToken(pddlParser.DEFINE, 0)

        def domainName(self):
            return self.getTypedRuleContext(pddlParser.DomainNameContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def requireDef(self):
            return self.getTypedRuleContext(pddlParser.RequireDefContext,0)


        def typesDef(self):
            return self.getTypedRuleContext(pddlParser.TypesDefContext,0)


        def predicatesDef(self):
            return self.getTypedRuleContext(pddlParser.PredicatesDefContext,0)


        def functionsDef(self):
            return self.getTypedRuleContext(pddlParser.FunctionsDefContext,0)


        def structureDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.StructureDefContext)
            else:
                return self.getTypedRuleContext(pddlParser.StructureDefContext,i)


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
            self.state = 116
            self.match(pddlParser.LP)
            self.state = 117
            self.match(pddlParser.DEFINE)
            self.state = 118
            self.domainName()
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 119
                self.requireDef()


            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 122
                self.typesDef()


            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 125
                self.predicatesDef()


            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 128
                self.functionsDef()


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 131
                self.structureDef()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
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

        def DOMAIN(self):
            return self.getToken(pddlParser.DOMAIN, 0)

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
            self.state = 139
            self.match(pddlParser.LP)
            self.state = 140
            self.match(pddlParser.DOMAIN)
            self.state = 141
            self.match(pddlParser.NAME)
            self.state = 142
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def REQUIREMENTS(self):
            return self.getToken(pddlParser.REQUIREMENTS, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def REQUIRE_KEY(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.REQUIRE_KEY)
            else:
                return self.getToken(pddlParser.REQUIRE_KEY, i)

        def getRuleIndex(self):
            return pddlParser.RULE_requireDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequireDef" ):
                listener.enterRequireDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequireDef" ):
                listener.exitRequireDef(self)




    def requireDef(self):

        localctx = pddlParser.RequireDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_requireDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(pddlParser.LP)
            self.state = 145
            self.match(pddlParser.REQUIREMENTS)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.match(pddlParser.REQUIRE_KEY)
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==46):
                    break

            self.state = 151
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def TYPES(self):
            return self.getToken(pddlParser.TYPES, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.NAME)
            else:
                return self.getToken(pddlParser.NAME, i)

        def getRuleIndex(self):
            return pddlParser.RULE_typesDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesDef" ):
                listener.enterTypesDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesDef" ):
                listener.exitTypesDef(self)




    def typesDef(self):

        localctx = pddlParser.TypesDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typesDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(pddlParser.LP)
            self.state = 154
            self.match(pddlParser.TYPES)
            self.state = 160 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.match(pddlParser.NAME)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 156
                    self.match(pddlParser.T__0)
                    self.state = 157
                    self.match(pddlParser.NAME)


                self.state = 162 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 164
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicatesDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def PREDICATES(self):
            return self.getToken(pddlParser.PREDICATES, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.PredicateContext)
            else:
                return self.getTypedRuleContext(pddlParser.PredicateContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_predicatesDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicatesDef" ):
                listener.enterPredicatesDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicatesDef" ):
                listener.exitPredicatesDef(self)




    def predicatesDef(self):

        localctx = pddlParser.PredicatesDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predicatesDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(pddlParser.LP)
            self.state = 167
            self.match(pddlParser.PREDICATES)
            self.state = 169 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 168
                self.predicate()
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 173
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
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

        def typedVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedVariableContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedVariableContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = pddlParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(pddlParser.LP)
            self.state = 176
            self.match(pddlParser.NAME)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 177
                self.typedVariable()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicFormulaSkeletonContext(ParserRuleContext):
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

        def typedVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedVariableContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedVariableContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_atomicFormulaSkeleton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicFormulaSkeleton" ):
                listener.enterAtomicFormulaSkeleton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicFormulaSkeleton" ):
                listener.exitAtomicFormulaSkeleton(self)




    def atomicFormulaSkeleton(self):

        localctx = pddlParser.AtomicFormulaSkeletonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atomicFormulaSkeleton)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(pddlParser.LP)
            self.state = 186
            self.match(pddlParser.NAME)
            self.state = 188 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 187
                self.typedVariable()
                self.state = 190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==43):
                    break

            self.state = 192
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(pddlParser.VARIABLE, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_typedVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedVariable" ):
                listener.enterTypedVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedVariable" ):
                listener.exitTypedVariable(self)




    def typedVariable(self):

        localctx = pddlParser.TypedVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typedVariable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(pddlParser.VARIABLE)
            self.state = 195
            self.match(pddlParser.T__0)
            self.state = 196
            self.match(pddlParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def FUNCTIONS(self):
            return self.getToken(pddlParser.FUNCTIONS, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.FunctionContext)
            else:
                return self.getTypedRuleContext(pddlParser.FunctionContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_functionsDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionsDef" ):
                listener.enterFunctionsDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionsDef" ):
                listener.exitFunctionsDef(self)




    def functionsDef(self):

        localctx = pddlParser.FunctionsDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionsDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(pddlParser.LP)
            self.state = 199
            self.match(pddlParser.FUNCTIONS)
            self.state = 201 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 200
                self.function()
                self.state = 203 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 205
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
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

        def typedVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedVariableContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedVariableContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = pddlParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(pddlParser.LP)
            self.state = 208
            self.match(pddlParser.NAME)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 209
                self.typedVariable()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicatedVariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.VARIABLE)
            else:
                return self.getToken(pddlParser.VARIABLE, i)

        def getRuleIndex(self):
            return pddlParser.RULE_predicatedVariables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicatedVariables" ):
                listener.enterPredicatedVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicatedVariables" ):
                listener.exitPredicatedVariables(self)




    def predicatedVariables(self):

        localctx = pddlParser.PredicatedVariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_predicatedVariables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(pddlParser.NAME)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 218
                self.match(pddlParser.VARIABLE)
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructureDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionDef(self):
            return self.getTypedRuleContext(pddlParser.ActionDefContext,0)


        def processDef(self):
            return self.getTypedRuleContext(pddlParser.ProcessDefContext,0)


        def eventDef(self):
            return self.getTypedRuleContext(pddlParser.EventDefContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_structureDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructureDef" ):
                listener.enterStructureDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructureDef" ):
                listener.exitStructureDef(self)




    def structureDef(self):

        localctx = pddlParser.StructureDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structureDef)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.actionDef()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.processDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.eventDef()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def ACTION(self):
            return self.getToken(pddlParser.ACTION, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def PARAMETERS(self):
            return self.getToken(pddlParser.PARAMETERS, 0)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def typedVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedVariableContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedVariableContext,i)


        def precondition(self):
            return self.getTypedRuleContext(pddlParser.PreconditionContext,0)


        def effect(self):
            return self.getTypedRuleContext(pddlParser.EffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_actionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionDef" ):
                listener.enterActionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionDef" ):
                listener.exitActionDef(self)




    def actionDef(self):

        localctx = pddlParser.ActionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_actionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(pddlParser.LP)
            self.state = 230
            self.match(pddlParser.ACTION)
            self.state = 231
            self.match(pddlParser.NAME)
            self.state = 232
            self.match(pddlParser.PARAMETERS)
            self.state = 233
            self.match(pddlParser.LP)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 234
                self.typedVariable()
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 240
            self.match(pddlParser.RP)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 241
                self.precondition()


            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 244
                self.effect()


            self.state = 247
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

        def PRECONDITION(self):
            return self.getToken(pddlParser.PRECONDITION, 0)

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def precondition_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.Precondition_formulaContext)
            else:
                return self.getTypedRuleContext(pddlParser.Precondition_formulaContext,i)


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
        self.enterRule(localctx, 28, self.RULE_precondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(pddlParser.PRECONDITION)
            self.state = 250
            self.match(pddlParser.LP)
            self.state = 251
            self.match(pddlParser.T__1)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==44:
                self.state = 252
                self.precondition_formula()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Precondition_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def predicatedVariables(self):
            return self.getTypedRuleContext(pddlParser.PredicatedVariablesContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def operation(self):
            return self.getTypedRuleContext(pddlParser.OperationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_precondition_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecondition_formula" ):
                listener.enterPrecondition_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecondition_formula" ):
                listener.exitPrecondition_formula(self)




    def precondition_formula(self):

        localctx = pddlParser.Precondition_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_precondition_formula)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(pddlParser.LP)
                self.state = 261
                self.predicatedVariables()
                self.state = 262
                self.match(pddlParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.operation()
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

        def EFFECT(self):
            return self.getToken(pddlParser.EFFECT, 0)

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def effect_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.Effect_formulaContext)
            else:
                return self.getTypedRuleContext(pddlParser.Effect_formulaContext,i)


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
        self.enterRule(localctx, 32, self.RULE_effect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(pddlParser.EFFECT)
            self.state = 268
            self.match(pddlParser.LP)
            self.state = 269
            self.match(pddlParser.T__1)
            self.state = 271 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 270
                self.effect_formula()
                self.state = 273 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 275
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Effect_formulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def predicatedVariables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.PredicatedVariablesContext)
            else:
                return self.getTypedRuleContext(pddlParser.PredicatedVariablesContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def NUMBER(self):
            return self.getToken(pddlParser.NUMBER, 0)

        def INCREASE(self):
            return self.getToken(pddlParser.INCREASE, 0)

        def DECREASE(self):
            return self.getToken(pddlParser.DECREASE, 0)

        def operation(self):
            return self.getTypedRuleContext(pddlParser.OperationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_effect_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_formula" ):
                listener.enterEffect_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_formula" ):
                listener.exitEffect_formula(self)




    def effect_formula(self):

        localctx = pddlParser.Effect_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_effect_formula)
        try:
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(pddlParser.LP)
                self.state = 278
                self.predicatedVariables()
                self.state = 279
                self.match(pddlParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(pddlParser.LP)
                self.state = 282
                self.match(pddlParser.T__2)
                self.state = 283
                self.match(pddlParser.LP)
                self.state = 284
                self.predicatedVariables()
                self.state = 285
                self.match(pddlParser.RP)
                self.state = 286
                self.match(pddlParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 288
                self.match(pddlParser.LP)
                self.state = 289
                self.match(pddlParser.T__3)
                self.state = 290
                self.match(pddlParser.LP)
                self.state = 291
                self.predicatedVariables()
                self.state = 292
                self.match(pddlParser.RP)
                self.state = 293
                self.match(pddlParser.NUMBER)
                self.state = 294
                self.match(pddlParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.match(pddlParser.LP)
                self.state = 297
                self.match(pddlParser.INCREASE)
                self.state = 298
                self.match(pddlParser.LP)
                self.state = 299
                self.predicatedVariables()
                self.state = 300
                self.match(pddlParser.RP)
                self.state = 301
                self.match(pddlParser.NUMBER)
                self.state = 302
                self.match(pddlParser.RP)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 304
                self.match(pddlParser.LP)
                self.state = 305
                self.match(pddlParser.DECREASE)
                self.state = 306
                self.match(pddlParser.LP)
                self.state = 307
                self.predicatedVariables()
                self.state = 308
                self.match(pddlParser.RP)
                self.state = 309
                self.match(pddlParser.NUMBER)
                self.state = 310
                self.match(pddlParser.RP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 312
                self.match(pddlParser.LP)
                self.state = 313
                self.match(pddlParser.T__3)
                self.state = 314
                self.match(pddlParser.LP)
                self.state = 315
                self.predicatedVariables()
                self.state = 316
                self.match(pddlParser.RP)
                self.state = 317
                self.operation()
                self.state = 318
                self.match(pddlParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 320
                self.match(pddlParser.LP)
                self.state = 321
                self.match(pddlParser.INCREASE)
                self.state = 322
                self.match(pddlParser.LP)
                self.state = 323
                self.predicatedVariables()
                self.state = 324
                self.match(pddlParser.RP)
                self.state = 325
                self.operation()
                self.state = 326
                self.match(pddlParser.RP)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 328
                self.match(pddlParser.LP)
                self.state = 329
                self.match(pddlParser.DECREASE)
                self.state = 330
                self.match(pddlParser.LP)
                self.state = 331
                self.predicatedVariables()
                self.state = 332
                self.match(pddlParser.RP)
                self.state = 333
                self.operation()
                self.state = 334
                self.match(pddlParser.RP)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 336
                self.match(pddlParser.LP)
                self.state = 337
                self.match(pddlParser.T__3)
                self.state = 338
                self.match(pddlParser.LP)
                self.state = 339
                self.predicatedVariables()
                self.state = 340
                self.match(pddlParser.RP)
                self.state = 341
                self.match(pddlParser.LP)
                self.state = 342
                self.predicatedVariables()
                self.state = 343
                self.match(pddlParser.RP)
                self.state = 344
                self.match(pddlParser.RP)
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

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def predicatedVariables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.PredicatedVariablesContext)
            else:
                return self.getTypedRuleContext(pddlParser.PredicatedVariablesContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.NUMBER)
            else:
                return self.getToken(pddlParser.NUMBER, i)

        def OPERATION(self):
            return self.getToken(pddlParser.OPERATION, 0)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.OperationContext)
            else:
                return self.getTypedRuleContext(pddlParser.OperationContext,i)


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
        self.enterRule(localctx, 36, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(pddlParser.LP)
                self.state = 349
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 350
                self.match(pddlParser.LP)
                self.state = 351
                self.predicatedVariables()
                self.state = 352
                self.match(pddlParser.RP)
                self.state = 353
                self.match(pddlParser.NUMBER)
                self.state = 354
                self.match(pddlParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(pddlParser.LP)
                self.state = 357
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 358
                self.match(pddlParser.NUMBER)
                self.state = 359
                self.match(pddlParser.LP)
                self.state = 360
                self.predicatedVariables()
                self.state = 361
                self.match(pddlParser.RP)
                self.state = 362
                self.match(pddlParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.match(pddlParser.LP)
                self.state = 365
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.match(pddlParser.NUMBER)
                self.state = 367
                self.match(pddlParser.NUMBER)
                self.state = 368
                self.match(pddlParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 369
                self.match(pddlParser.LP)
                self.state = 370
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 371
                self.match(pddlParser.LP)
                self.state = 372
                self.predicatedVariables()
                self.state = 373
                self.match(pddlParser.RP)
                self.state = 374
                self.match(pddlParser.LP)
                self.state = 375
                self.predicatedVariables()
                self.state = 376
                self.match(pddlParser.RP)
                self.state = 377
                self.match(pddlParser.RP)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self.match(pddlParser.LP)
                self.state = 380
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                self.match(pddlParser.LP)
                self.state = 382
                self.predicatedVariables()
                self.state = 383
                self.match(pddlParser.RP)
                self.state = 384
                self.operation()
                self.state = 385
                self.match(pddlParser.RP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 387
                self.match(pddlParser.LP)
                self.state = 388
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 389
                self.operation()
                self.state = 390
                self.match(pddlParser.LP)
                self.state = 391
                self.predicatedVariables()
                self.state = 392
                self.match(pddlParser.RP)
                self.state = 393
                self.match(pddlParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 395
                self.match(pddlParser.LP)
                self.state = 396
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 397
                self.match(pddlParser.NUMBER)
                self.state = 398
                self.operation()
                self.state = 399
                self.match(pddlParser.RP)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 401
                self.match(pddlParser.LP)
                self.state = 402
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 403
                self.operation()
                self.state = 404
                self.operation()
                self.state = 405
                self.match(pddlParser.RP)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 407
                self.match(pddlParser.LP)
                self.state = 408
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488363490) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 409
                self.operation()
                self.state = 410
                self.match(pddlParser.NUMBER)
                self.state = 411
                self.match(pddlParser.RP)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 413
                self.match(pddlParser.LP)
                self.state = 414
                self.match(pddlParser.T__2)
                self.state = 415
                self.operation()
                self.state = 416
                self.match(pddlParser.RP)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 418
                self.match(pddlParser.LP)
                self.state = 419
                self.match(pddlParser.T__2)
                self.state = 420
                self.match(pddlParser.LP)
                self.state = 421
                self.predicatedVariables()
                self.state = 422
                self.match(pddlParser.RP)
                self.state = 423
                self.match(pddlParser.RP)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 425
                self.match(pddlParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def PROCESS(self):
            return self.getToken(pddlParser.PROCESS, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def PARAMETERS(self):
            return self.getToken(pddlParser.PARAMETERS, 0)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def typedVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedVariableContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedVariableContext,i)


        def precondition(self):
            return self.getTypedRuleContext(pddlParser.PreconditionContext,0)


        def effect(self):
            return self.getTypedRuleContext(pddlParser.EffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_processDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessDef" ):
                listener.enterProcessDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessDef" ):
                listener.exitProcessDef(self)




    def processDef(self):

        localctx = pddlParser.ProcessDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_processDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(pddlParser.LP)
            self.state = 429
            self.match(pddlParser.PROCESS)
            self.state = 430
            self.match(pddlParser.NAME)
            self.state = 431
            self.match(pddlParser.PARAMETERS)
            self.state = 432
            self.match(pddlParser.LP)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 433
                self.typedVariable()
                self.state = 438
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 439
            self.match(pddlParser.RP)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 440
                self.precondition()


            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 443
                self.effect()


            self.state = 446
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.LP)
            else:
                return self.getToken(pddlParser.LP, i)

        def EVENT(self):
            return self.getToken(pddlParser.EVENT, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def PARAMETERS(self):
            return self.getToken(pddlParser.PARAMETERS, 0)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.RP)
            else:
                return self.getToken(pddlParser.RP, i)

        def typedVariable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.TypedVariableContext)
            else:
                return self.getTypedRuleContext(pddlParser.TypedVariableContext,i)


        def precondition(self):
            return self.getTypedRuleContext(pddlParser.PreconditionContext,0)


        def effect(self):
            return self.getTypedRuleContext(pddlParser.EffectContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_eventDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventDef" ):
                listener.enterEventDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventDef" ):
                listener.exitEventDef(self)




    def eventDef(self):

        localctx = pddlParser.EventDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_eventDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(pddlParser.LP)
            self.state = 449
            self.match(pddlParser.EVENT)
            self.state = 450
            self.match(pddlParser.NAME)
            self.state = 451
            self.match(pddlParser.PARAMETERS)
            self.state = 452
            self.match(pddlParser.LP)
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 453
                self.typedVariable()
                self.state = 458
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 459
            self.match(pddlParser.RP)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 460
                self.precondition()


            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 463
                self.effect()


            self.state = 466
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

        def DEFINE(self):
            return self.getToken(pddlParser.DEFINE, 0)

        def problemDecl(self):
            return self.getTypedRuleContext(pddlParser.ProblemDeclContext,0)


        def problemDomain(self):
            return self.getTypedRuleContext(pddlParser.ProblemDomainContext,0)


        def init(self):
            return self.getTypedRuleContext(pddlParser.InitContext,0)


        def goal(self):
            return self.getTypedRuleContext(pddlParser.GoalContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def objectDecl(self):
            return self.getTypedRuleContext(pddlParser.ObjectDeclContext,0)


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
        self.enterRule(localctx, 42, self.RULE_problem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(pddlParser.LP)
            self.state = 469
            self.match(pddlParser.DEFINE)
            self.state = 470
            self.problemDecl()
            self.state = 471
            self.problemDomain()
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 472
                self.objectDecl()


            self.state = 475
            self.init()
            self.state = 476
            self.goal()
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 477
                self.metric()


            self.state = 480
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProblemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def PROBLEM(self):
            return self.getToken(pddlParser.PROBLEM, 0)

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_problemDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProblemDecl" ):
                listener.enterProblemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProblemDecl" ):
                listener.exitProblemDecl(self)




    def problemDecl(self):

        localctx = pddlParser.ProblemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_problemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(pddlParser.LP)
            self.state = 483
            self.match(pddlParser.PROBLEM)
            self.state = 484
            self.match(pddlParser.NAME)
            self.state = 485
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
        self.enterRule(localctx, 46, self.RULE_problemDomain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(pddlParser.LP)
            self.state = 488
            self.match(pddlParser.T__12)
            self.state = 489
            self.match(pddlParser.NAME)
            self.state = 490
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def sameTypeNamesList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.SameTypeNamesListContext)
            else:
                return self.getTypedRuleContext(pddlParser.SameTypeNamesListContext,i)


        def getRuleIndex(self):
            return pddlParser.RULE_objectDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectDecl" ):
                listener.enterObjectDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectDecl" ):
                listener.exitObjectDecl(self)




    def objectDecl(self):

        localctx = pddlParser.ObjectDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_objectDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(pddlParser.LP)
            self.state = 493
            self.match(pddlParser.T__13)
            self.state = 495 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 494
                self.sameTypeNamesList()
                self.state = 497 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 499
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SameTypeNamesListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.NAME)
            else:
                return self.getToken(pddlParser.NAME, i)

        def getRuleIndex(self):
            return pddlParser.RULE_sameTypeNamesList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSameTypeNamesList" ):
                listener.enterSameTypeNamesList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSameTypeNamesList" ):
                listener.exitSameTypeNamesList(self)




    def sameTypeNamesList(self):

        localctx = pddlParser.SameTypeNamesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sameTypeNamesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 501
                self.match(pddlParser.NAME)
                self.state = 504 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 506
            self.match(pddlParser.T__0)
            self.state = 507
            self.match(pddlParser.NAME)
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

        def initEl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.InitElContext)
            else:
                return self.getTypedRuleContext(pddlParser.InitElContext,i)


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
        self.enterRule(localctx, 52, self.RULE_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(pddlParser.LP)
            self.state = 510
            self.match(pddlParser.T__14)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 511
                self.initEl()
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 517
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomicNameFormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(pddlParser.NAME)
            else:
                return self.getToken(pddlParser.NAME, i)

        def getRuleIndex(self):
            return pddlParser.RULE_atomicNameFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicNameFormula" ):
                listener.enterAtomicNameFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicNameFormula" ):
                listener.exitAtomicNameFormula(self)




    def atomicNameFormula(self):

        localctx = pddlParser.AtomicNameFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atomicNameFormula)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(pddlParser.LP)
            self.state = 521 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 520
                self.match(pddlParser.NAME)
                self.state = 523 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

            self.state = 525
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def atomicNameFormula(self):
            return self.getTypedRuleContext(pddlParser.AtomicNameFormulaContext,0)


        def NUMBER(self):
            return self.getToken(pddlParser.NUMBER, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_equalLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualLiteral" ):
                listener.enterEqualLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualLiteral" ):
                listener.exitEqualLiteral(self)




    def equalLiteral(self):

        localctx = pddlParser.EqualLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_equalLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(pddlParser.LP)
            self.state = 528
            self.match(pddlParser.T__4)
            self.state = 529
            self.atomicNameFormula()
            self.state = 530
            self.match(pddlParser.NUMBER)
            self.state = 531
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitElContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameLiteral(self):
            return self.getTypedRuleContext(pddlParser.NameLiteralContext,0)


        def equalLiteral(self):
            return self.getTypedRuleContext(pddlParser.EqualLiteralContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_initEl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitEl" ):
                listener.enterInitEl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitEl" ):
                listener.exitInitEl(self)




    def initEl(self):

        localctx = pddlParser.InitElContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_initEl)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.nameLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 534
                self.equalLiteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomicNameFormula(self):
            return self.getTypedRuleContext(pddlParser.AtomicNameFormulaContext,0)


        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def RP(self):
            return self.getToken(pddlParser.RP, 0)

        def getRuleIndex(self):
            return pddlParser.RULE_nameLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameLiteral" ):
                listener.enterNameLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameLiteral" ):
                listener.exitNameLiteral(self)




    def nameLiteral(self):

        localctx = pddlParser.NameLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_nameLiteral)
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.atomicNameFormula()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.match(pddlParser.LP)
                self.state = 539
                self.match(pddlParser.T__2)
                self.state = 540
                self.atomicNameFormula()
                self.state = 541
                self.match(pddlParser.RP)
                pass


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
        self.enterRule(localctx, 62, self.RULE_atomName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
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
        self.enterRule(localctx, 64, self.RULE_groundAtomParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
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

        def NAME(self):
            return self.getToken(pddlParser.NAME, 0)

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
        self.enterRule(localctx, 66, self.RULE_liftedAtomParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(pddlParser.T__15)
            self.state = 550
            self.match(pddlParser.NAME)
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


        def groundAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.GroundAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.GroundAtomParameterContext,i)


        def liftedAtomParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.LiftedAtomParameterContext)
            else:
                return self.getTypedRuleContext(pddlParser.LiftedAtomParameterContext,i)


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
        self.enterRule(localctx, 68, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.atomName()
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 554 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 553
                    self.groundAtomParameter()
                    self.state = 556 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==42):
                        break

                pass
            elif token in [16]:
                self.state = 559 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 558
                    self.liftedAtomParameter()
                    self.state = 561 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==16):
                        break

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


    class PositiveLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(pddlParser.LP, 0)

        def atom(self):
            return self.getTypedRuleContext(pddlParser.AtomContext,0)


        def RP(self):
            return self.getToken(pddlParser.RP, 0)

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
        self.enterRule(localctx, 70, self.RULE_positiveLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(pddlParser.LP)
            self.state = 566
            self.atom()
            self.state = 567
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
        self.enterRule(localctx, 72, self.RULE_negativeLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(pddlParser.LP)
            self.state = 570
            self.match(pddlParser.T__2)
            self.state = 571
            self.positiveLiteral()
            self.state = 572
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
        self.enterRule(localctx, 74, self.RULE_booleanLiteral)
        try:
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.positiveLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.negativeLiteral()
                pass


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

        def INCREASE(self):
            return self.getToken(pddlParser.INCREASE, 0)

        def DECREASE(self):
            return self.getToken(pddlParser.DECREASE, 0)

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
        self.enterRule(localctx, 76, self.RULE_modificator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1649267441680) != 0)):
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
        self.enterRule(localctx, 78, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7170) != 0)):
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
        self.enterRule(localctx, 80, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 131936) != 0)):
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
        self.enterRule(localctx, 82, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
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

        def DELTA(self):
            return self.getToken(pddlParser.DELTA, 0)

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
        self.enterRule(localctx, 84, self.RULE_delta)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(pddlParser.DELTA)
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
        self.enterRule(localctx, 86, self.RULE_constant)
        try:
            self.state = 590
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.number()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 589
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


    class OperationSideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nOperation(self):
            return self.getTypedRuleContext(pddlParser.NOperationContext,0)


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
        self.enterRule(localctx, 88, self.RULE_operationSide)
        try:
            self.state = 595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 592
                self.nOperation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
                self.positiveLiteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 594
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NOperationContext(ParserRuleContext):
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
            return pddlParser.RULE_nOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNOperation" ):
                listener.enterNOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNOperation" ):
                listener.exitNOperation(self)




    def nOperation(self):

        localctx = pddlParser.NOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_nOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.match(pddlParser.LP)
            self.state = 598
            self.operator()
            self.state = 599
            self.operationSide()
            self.state = 600
            self.operationSide()
            self.state = 601
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


        def positiveLiteral(self):
            return self.getTypedRuleContext(pddlParser.PositiveLiteralContext,0)


        def operationSide(self):
            return self.getTypedRuleContext(pddlParser.OperationSideContext,0)


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
        self.enterRule(localctx, 92, self.RULE_comparation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            self.match(pddlParser.LP)
            self.state = 604
            self.comparator()
            self.state = 605
            self.positiveLiteral()
            self.state = 606
            self.operationSide()
            self.state = 607
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
        self.enterRule(localctx, 94, self.RULE_modification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(pddlParser.LP)
            self.state = 610
            self.modificator()
            self.state = 611
            self.positiveLiteral()
            self.state = 612
            self.operationSide()
            self.state = 613
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NPreconditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def comparation(self):
            return self.getTypedRuleContext(pddlParser.ComparationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_nPrecondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNPrecondition" ):
                listener.enterNPrecondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNPrecondition" ):
                listener.exitNPrecondition(self)




    def nPrecondition(self):

        localctx = pddlParser.NPreconditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_nPrecondition)
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.comparation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NEffectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanLiteral(self):
            return self.getTypedRuleContext(pddlParser.BooleanLiteralContext,0)


        def modification(self):
            return self.getTypedRuleContext(pddlParser.ModificationContext,0)


        def getRuleIndex(self):
            return pddlParser.RULE_nEffect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNEffect" ):
                listener.enterNEffect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNEffect" ):
                listener.exitNEffect(self)




    def nEffect(self):

        localctx = pddlParser.NEffectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_nEffect)
        try:
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.booleanLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
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

        def nPrecondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.NPreconditionContext)
            else:
                return self.getTypedRuleContext(pddlParser.NPreconditionContext,i)


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
        self.enterRule(localctx, 100, self.RULE_andPrecondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(pddlParser.LP)
            self.state = 624
            self.match(pddlParser.T__1)
            self.state = 626 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 625
                self.nPrecondition()
                self.state = 628 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 630
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

        def nEffect(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pddlParser.NEffectContext)
            else:
                return self.getTypedRuleContext(pddlParser.NEffectContext,i)


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
        self.enterRule(localctx, 102, self.RULE_andEffect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(pddlParser.LP)
            self.state = 633
            self.match(pddlParser.T__1)
            self.state = 635 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 634
                self.nEffect()
                self.state = 637 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==22):
                    break

            self.state = 639
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

        def nPrecondition(self):
            return self.getTypedRuleContext(pddlParser.NPreconditionContext,0)


        def andPrecondition(self):
            return self.getTypedRuleContext(pddlParser.AndPreconditionContext,0)


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
        self.enterRule(localctx, 104, self.RULE_preconditions)
        try:
            self.state = 643
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                self.nPrecondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self.andPrecondition()
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

        def nEffect(self):
            return self.getTypedRuleContext(pddlParser.NEffectContext,0)


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
        self.enterRule(localctx, 106, self.RULE_effects)
        try:
            self.state = 647
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 645
                self.nEffect()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
                self.andEffect()
                pass


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
        self.enterRule(localctx, 108, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(pddlParser.LP)
            self.state = 650
            self.match(pddlParser.T__17)
            self.state = 651
            self.preconditions()
            self.state = 652
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

        def atomicNameFormula(self):
            return self.getTypedRuleContext(pddlParser.AtomicNameFormulaContext,0)


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
        self.enterRule(localctx, 110, self.RULE_metric)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(pddlParser.LP)
            self.state = 655
            self.match(pddlParser.T__18)
            self.state = 656
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 657
            self.atomicNameFormula()
            self.state = 658
            self.match(pddlParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





