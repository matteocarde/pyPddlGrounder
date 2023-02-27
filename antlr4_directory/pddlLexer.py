# Generated from pddl.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 0, 48, 459, 6, -1, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5,
        2, 6, 7, 6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2,
        13, 7, 13, 2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7,
        19, 2, 20, 7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2,
        26, 7, 26, 2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 2, 32, 7,
        32, 2, 33, 7, 33, 2, 34, 7, 34, 2, 35, 7, 35, 2, 36, 7, 36, 2, 37, 7, 37, 2, 38, 7, 38, 2,
        39, 7, 39, 2, 40, 7, 40, 2, 41, 7, 41, 2, 42, 7, 42, 2, 43, 7, 43, 2, 44, 7, 44, 2, 45, 7,
        45, 2, 46, 7, 46, 2, 47, 7, 47, 2, 48, 7, 48, 2, 49, 7, 49, 2, 50, 7, 50, 1, 0, 1, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3,
        1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4,
        1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 7, 1, 7,
        1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7,
        1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 9, 1, 9,
        1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1, 12,
        1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13,
        1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14,
        1, 14, 1, 14, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 16, 1, 16,
        1, 16, 1, 16, 1, 16, 1, 16, 1, 16, 1, 16, 1, 16, 1, 17, 1, 17, 1, 18, 1, 18, 1, 19, 1, 19,
        1, 20, 1, 20, 1, 21, 1, 21, 1, 21, 1, 22, 1, 22, 1, 22, 1, 23, 1, 23, 1, 24, 1, 24, 1, 25,
        1, 25, 1, 25, 1, 26, 1, 26, 1, 26, 1, 26, 1, 27, 1, 27, 1, 27, 1, 27, 1, 27, 1, 27, 1, 27,
        1, 27, 1, 27, 1, 27, 1, 27, 1, 27, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28,
        1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 29, 1, 29, 1, 29, 1, 29, 1, 29, 1, 29, 1, 29,
        1, 29, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 31, 1, 31, 1, 31, 1, 31,
        1, 31, 1, 31, 1, 31, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 33,
        1, 33, 1, 33, 1, 33, 1, 33, 1, 33, 1, 33, 1, 33, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34,
        1, 34, 1, 34, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 36, 1, 36,
        1, 36, 1, 36, 1, 36, 1, 36, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 38, 1, 38, 1, 38,
        1, 38, 1, 38, 1, 38, 1, 38, 1, 38, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39,
        1, 39, 1, 40, 1, 40, 1, 40, 1, 40, 1, 40, 1, 40, 1, 40, 1, 40, 1, 40, 1, 41, 1, 41, 1, 42,
        1, 42, 1, 43, 1, 43, 1, 43, 1, 44, 1, 44, 5, 44, 417, 8, 44, 10, 44, 12, 44, 420, 9, 44,
        1, 45, 1, 45, 1, 46, 1, 46, 3, 46, 426, 8, 46, 1, 47, 1, 47, 1, 47, 1, 48, 1, 48, 1, 49,
        3, 49, 434, 8, 49, 1, 49, 4, 49, 437, 8, 49, 11, 49, 12, 49, 438, 1, 49, 1, 49, 4, 49,
        443, 8, 49, 11, 49, 12, 49, 444, 3, 49, 447, 8, 49, 1, 49, 1, 49, 3, 49, 451, 8, 49, 1,
        50, 4, 50, 454, 8, 50, 11, 50, 12, 50, 455, 1, 50, 1, 50, 0, 0, 51, 1, 1, 3, 2, 5, 3, 7,
        4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21, 11, 23, 12, 25, 13, 27, 14, 29, 15, 31,
        16, 33, 17, 35, 18, 37, 19, 39, 20, 41, 21, 43, 22, 45, 23, 47, 24, 49, 25, 51, 26, 53,
        27, 55, 28, 57, 29, 59, 30, 61, 31, 63, 32, 65, 33, 67, 34, 69, 35, 71, 36, 73, 37, 75,
        38, 77, 39, 79, 40, 81, 41, 83, 42, 85, 43, 87, 44, 89, 45, 91, 0, 93, 0, 95, 46, 97,
        0, 99, 47, 101, 48, 1, 0, 3, 2, 0, 65, 90, 97, 122, 3, 0, 45, 45, 48, 57, 95, 95, 3, 0,
        9, 10, 13, 13, 32, 32, 463, 0, 1, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 7, 1, 0,
        0, 0, 0, 9, 1, 0, 0, 0, 0, 11, 1, 0, 0, 0, 0, 13, 1, 0, 0, 0, 0, 15, 1, 0, 0, 0, 0, 17, 1, 0,
        0, 0, 0, 19, 1, 0, 0, 0, 0, 21, 1, 0, 0, 0, 0, 23, 1, 0, 0, 0, 0, 25, 1, 0, 0, 0, 0, 27, 1, 0,
        0, 0, 0, 29, 1, 0, 0, 0, 0, 31, 1, 0, 0, 0, 0, 33, 1, 0, 0, 0, 0, 35, 1, 0, 0, 0, 0, 37, 1, 0,
        0, 0, 0, 39, 1, 0, 0, 0, 0, 41, 1, 0, 0, 0, 0, 43, 1, 0, 0, 0, 0, 45, 1, 0, 0, 0, 0, 47, 1, 0,
        0, 0, 0, 49, 1, 0, 0, 0, 0, 51, 1, 0, 0, 0, 0, 53, 1, 0, 0, 0, 0, 55, 1, 0, 0, 0, 0, 57, 1, 0,
        0, 0, 0, 59, 1, 0, 0, 0, 0, 61, 1, 0, 0, 0, 0, 63, 1, 0, 0, 0, 0, 65, 1, 0, 0, 0, 0, 67, 1, 0,
        0, 0, 0, 69, 1, 0, 0, 0, 0, 71, 1, 0, 0, 0, 0, 73, 1, 0, 0, 0, 0, 75, 1, 0, 0, 0, 0, 77, 1, 0,
        0, 0, 0, 79, 1, 0, 0, 0, 0, 81, 1, 0, 0, 0, 0, 83, 1, 0, 0, 0, 0, 85, 1, 0, 0, 0, 0, 87, 1, 0,
        0, 0, 0, 89, 1, 0, 0, 0, 0, 95, 1, 0, 0, 0, 0, 99, 1, 0, 0, 0, 0, 101, 1, 0, 0, 0, 1, 103, 1,
        0, 0, 0, 3, 110, 1, 0, 0, 0, 5, 117, 1, 0, 0, 0, 7, 125, 1, 0, 0, 0, 9, 148, 1, 0, 0, 0, 11,
        154, 1, 0, 0, 0, 13, 163, 1, 0, 0, 0, 15, 168, 1, 0, 0, 0, 17, 186, 1, 0, 0, 0, 19, 200,
        1, 0, 0, 0, 21, 202, 1, 0, 0, 0, 23, 209, 1, 0, 0, 0, 25, 213, 1, 0, 0, 0, 27, 225, 1, 0,
        0, 0, 29, 236, 1, 0, 0, 0, 31, 243, 1, 0, 0, 0, 33, 252, 1, 0, 0, 0, 35, 261, 1, 0, 0, 0,
        37, 263, 1, 0, 0, 0, 39, 265, 1, 0, 0, 0, 41, 267, 1, 0, 0, 0, 43, 269, 1, 0, 0, 0, 45, 272,
        1, 0, 0, 0, 47, 275, 1, 0, 0, 0, 49, 277, 1, 0, 0, 0, 51, 279, 1, 0, 0, 0, 53, 282, 1, 0,
        0, 0, 55, 286, 1, 0, 0, 0, 57, 298, 1, 0, 0, 0, 59, 312, 1, 0, 0, 0, 61, 320, 1, 0, 0, 0,
        63, 328, 1, 0, 0, 0, 65, 335, 1, 0, 0, 0, 67, 344, 1, 0, 0, 0, 69, 352, 1, 0, 0, 0, 71, 360,
        1, 0, 0, 0, 73, 369, 1, 0, 0, 0, 75, 375, 1, 0, 0, 0, 77, 381, 1, 0, 0, 0, 79, 389, 1, 0,
        0, 0, 81, 398, 1, 0, 0, 0, 83, 407, 1, 0, 0, 0, 85, 409, 1, 0, 0, 0, 87, 411, 1, 0, 0, 0,
        89, 414, 1, 0, 0, 0, 91, 421, 1, 0, 0, 0, 93, 425, 1, 0, 0, 0, 95, 427, 1, 0, 0, 0, 97, 430,
        1, 0, 0, 0, 99, 450, 1, 0, 0, 0, 101, 453, 1, 0, 0, 0, 103, 104, 5, 100, 0, 0, 104, 105,
        5, 101, 0, 0, 105, 106, 5, 102, 0, 0, 106, 107, 5, 105, 0, 0, 107, 108, 5, 110, 0, 0,
        108, 109, 5, 101, 0, 0, 109, 2, 1, 0, 0, 0, 110, 111, 5, 100, 0, 0, 111, 112, 5, 111,
        0, 0, 112, 113, 5, 109, 0, 0, 113, 114, 5, 97, 0, 0, 114, 115, 5, 105, 0, 0, 115, 116,
        5, 110, 0, 0, 116, 4, 1, 0, 0, 0, 117, 118, 5, 58, 0, 0, 118, 119, 5, 116, 0, 0, 119, 120,
        5, 121, 0, 0, 120, 121, 5, 112, 0, 0, 121, 122, 5, 105, 0, 0, 122, 123, 5, 110, 0, 0,
        123, 124, 5, 103, 0, 0, 124, 6, 1, 0, 0, 0, 125, 126, 5, 58, 0, 0, 126, 127, 5, 100, 0,
        0, 127, 128, 5, 117, 0, 0, 128, 129, 5, 114, 0, 0, 129, 130, 5, 97, 0, 0, 130, 131, 5,
        116, 0, 0, 131, 132, 5, 105, 0, 0, 132, 133, 5, 111, 0, 0, 133, 134, 5, 110, 0, 0, 134,
        135, 5, 45, 0, 0, 135, 136, 5, 105, 0, 0, 136, 137, 5, 110, 0, 0, 137, 138, 5, 101, 0,
        0, 138, 139, 5, 113, 0, 0, 139, 140, 5, 117, 0, 0, 140, 141, 5, 97, 0, 0, 141, 142, 5,
        108, 0, 0, 142, 143, 5, 105, 0, 0, 143, 144, 5, 116, 0, 0, 144, 145, 5, 105, 0, 0, 145,
        146, 5, 101, 0, 0, 146, 147, 5, 115, 0, 0, 147, 8, 1, 0, 0, 0, 148, 149, 5, 58, 0, 0, 149,
        150, 5, 116, 0, 0, 150, 151, 5, 105, 0, 0, 151, 152, 5, 109, 0, 0, 152, 153, 5, 101,
        0, 0, 153, 10, 1, 0, 0, 0, 154, 155, 5, 58, 0, 0, 155, 156, 5, 102, 0, 0, 156, 157, 5,
        108, 0, 0, 157, 158, 5, 117, 0, 0, 158, 159, 5, 101, 0, 0, 159, 160, 5, 110, 0, 0, 160,
        161, 5, 116, 0, 0, 161, 162, 5, 115, 0, 0, 162, 12, 1, 0, 0, 0, 163, 164, 5, 58, 0, 0,
        164, 165, 5, 97, 0, 0, 165, 166, 5, 100, 0, 0, 166, 167, 5, 108, 0, 0, 167, 14, 1, 0,
        0, 0, 168, 169, 5, 58, 0, 0, 169, 170, 5, 100, 0, 0, 170, 171, 5, 117, 0, 0, 171, 172,
        5, 114, 0, 0, 172, 173, 5, 97, 0, 0, 173, 174, 5, 116, 0, 0, 174, 175, 5, 105, 0, 0, 175,
        176, 5, 118, 0, 0, 176, 177, 5, 101, 0, 0, 177, 178, 5, 45, 0, 0, 178, 179, 5, 97, 0,
        0, 179, 180, 5, 99, 0, 0, 180, 181, 5, 116, 0, 0, 181, 182, 5, 105, 0, 0, 182, 183, 5,
        111, 0, 0, 183, 184, 5, 110, 0, 0, 184, 185, 5, 115, 0, 0, 185, 16, 1, 0, 0, 0, 186, 187,
        5, 58, 0, 0, 187, 188, 5, 114, 0, 0, 188, 189, 5, 101, 0, 0, 189, 190, 5, 113, 0, 0, 190,
        191, 5, 117, 0, 0, 191, 192, 5, 105, 0, 0, 192, 193, 5, 114, 0, 0, 193, 194, 5, 101,
        0, 0, 194, 195, 5, 109, 0, 0, 195, 196, 5, 101, 0, 0, 196, 197, 5, 110, 0, 0, 197, 198,
        5, 116, 0, 0, 198, 199, 5, 115, 0, 0, 199, 18, 1, 0, 0, 0, 200, 201, 5, 45, 0, 0, 201,
        20, 1, 0, 0, 0, 202, 203, 5, 58, 0, 0, 203, 204, 5, 116, 0, 0, 204, 205, 5, 121, 0, 0,
        205, 206, 5, 112, 0, 0, 206, 207, 5, 101, 0, 0, 207, 208, 5, 115, 0, 0, 208, 22, 1, 0,
        0, 0, 209, 210, 5, 110, 0, 0, 210, 211, 5, 111, 0, 0, 211, 212, 5, 116, 0, 0, 212, 24,
        1, 0, 0, 0, 213, 214, 5, 58, 0, 0, 214, 215, 5, 112, 0, 0, 215, 216, 5, 114, 0, 0, 216,
        217, 5, 101, 0, 0, 217, 218, 5, 100, 0, 0, 218, 219, 5, 105, 0, 0, 219, 220, 5, 99, 0,
        0, 220, 221, 5, 97, 0, 0, 221, 222, 5, 116, 0, 0, 222, 223, 5, 101, 0, 0, 223, 224, 5,
        115, 0, 0, 224, 26, 1, 0, 0, 0, 225, 226, 5, 58, 0, 0, 226, 227, 5, 102, 0, 0, 227, 228,
        5, 117, 0, 0, 228, 229, 5, 110, 0, 0, 229, 230, 5, 99, 0, 0, 230, 231, 5, 116, 0, 0, 231,
        232, 5, 105, 0, 0, 232, 233, 5, 111, 0, 0, 233, 234, 5, 110, 0, 0, 234, 235, 5, 115,
        0, 0, 235, 28, 1, 0, 0, 0, 236, 237, 5, 97, 0, 0, 237, 238, 5, 115, 0, 0, 238, 239, 5,
        115, 0, 0, 239, 240, 5, 105, 0, 0, 240, 241, 5, 103, 0, 0, 241, 242, 5, 110, 0, 0, 242,
        30, 1, 0, 0, 0, 243, 244, 5, 105, 0, 0, 244, 245, 5, 110, 0, 0, 245, 246, 5, 99, 0, 0,
        246, 247, 5, 114, 0, 0, 247, 248, 5, 101, 0, 0, 248, 249, 5, 97, 0, 0, 249, 250, 5, 115,
        0, 0, 250, 251, 5, 101, 0, 0, 251, 32, 1, 0, 0, 0, 252, 253, 5, 100, 0, 0, 253, 254, 5,
        101, 0, 0, 254, 255, 5, 99, 0, 0, 255, 256, 5, 114, 0, 0, 256, 257, 5, 101, 0, 0, 257,
        258, 5, 97, 0, 0, 258, 259, 5, 115, 0, 0, 259, 260, 5, 101, 0, 0, 260, 34, 1, 0, 0, 0,
        261, 262, 5, 43, 0, 0, 262, 36, 1, 0, 0, 0, 263, 264, 5, 42, 0, 0, 264, 38, 1, 0, 0, 0,
        265, 266, 5, 47, 0, 0, 266, 40, 1, 0, 0, 0, 267, 268, 5, 62, 0, 0, 268, 42, 1, 0, 0, 0,
        269, 270, 5, 62, 0, 0, 270, 271, 5, 61, 0, 0, 271, 44, 1, 0, 0, 0, 272, 273, 5, 60, 0,
        0, 273, 274, 5, 61, 0, 0, 274, 46, 1, 0, 0, 0, 275, 276, 5, 60, 0, 0, 276, 48, 1, 0, 0,
        0, 277, 278, 5, 61, 0, 0, 278, 50, 1, 0, 0, 0, 279, 280, 5, 35, 0, 0, 280, 281, 5, 116,
        0, 0, 281, 52, 1, 0, 0, 0, 282, 283, 5, 97, 0, 0, 283, 284, 5, 110, 0, 0, 284, 285, 5,
        100, 0, 0, 285, 54, 1, 0, 0, 0, 286, 287, 5, 58, 0, 0, 287, 288, 5, 112, 0, 0, 288, 289,
        5, 97, 0, 0, 289, 290, 5, 114, 0, 0, 290, 291, 5, 97, 0, 0, 291, 292, 5, 109, 0, 0, 292,
        293, 5, 101, 0, 0, 293, 294, 5, 116, 0, 0, 294, 295, 5, 101, 0, 0, 295, 296, 5, 114,
        0, 0, 296, 297, 5, 115, 0, 0, 297, 56, 1, 0, 0, 0, 298, 299, 5, 58, 0, 0, 299, 300, 5,
        112, 0, 0, 300, 301, 5, 114, 0, 0, 301, 302, 5, 101, 0, 0, 302, 303, 5, 99, 0, 0, 303,
        304, 5, 111, 0, 0, 304, 305, 5, 110, 0, 0, 305, 306, 5, 100, 0, 0, 306, 307, 5, 105,
        0, 0, 307, 308, 5, 116, 0, 0, 308, 309, 5, 105, 0, 0, 309, 310, 5, 111, 0, 0, 310, 311,
        5, 110, 0, 0, 311, 58, 1, 0, 0, 0, 312, 313, 5, 58, 0, 0, 313, 314, 5, 101, 0, 0, 314,
        315, 5, 102, 0, 0, 315, 316, 5, 102, 0, 0, 316, 317, 5, 101, 0, 0, 317, 318, 5, 99, 0,
        0, 318, 319, 5, 116, 0, 0, 319, 60, 1, 0, 0, 0, 320, 321, 5, 58, 0, 0, 321, 322, 5, 97,
        0, 0, 322, 323, 5, 99, 0, 0, 323, 324, 5, 116, 0, 0, 324, 325, 5, 105, 0, 0, 325, 326,
        5, 111, 0, 0, 326, 327, 5, 110, 0, 0, 327, 62, 1, 0, 0, 0, 328, 329, 5, 58, 0, 0, 329,
        330, 5, 101, 0, 0, 330, 331, 5, 118, 0, 0, 331, 332, 5, 101, 0, 0, 332, 333, 5, 110,
        0, 0, 333, 334, 5, 116, 0, 0, 334, 64, 1, 0, 0, 0, 335, 336, 5, 58, 0, 0, 336, 337, 5,
        112, 0, 0, 337, 338, 5, 114, 0, 0, 338, 339, 5, 111, 0, 0, 339, 340, 5, 99, 0, 0, 340,
        341, 5, 101, 0, 0, 341, 342, 5, 115, 0, 0, 342, 343, 5, 115, 0, 0, 343, 66, 1, 0, 0, 0,
        344, 345, 5, 112, 0, 0, 345, 346, 5, 114, 0, 0, 346, 347, 5, 111, 0, 0, 347, 348, 5,
        98, 0, 0, 348, 349, 5, 108, 0, 0, 349, 350, 5, 101, 0, 0, 350, 351, 5, 109, 0, 0, 351,
        68, 1, 0, 0, 0, 352, 353, 5, 58, 0, 0, 353, 354, 5, 100, 0, 0, 354, 355, 5, 111, 0, 0,
        355, 356, 5, 109, 0, 0, 356, 357, 5, 97, 0, 0, 357, 358, 5, 105, 0, 0, 358, 359, 5, 110,
        0, 0, 359, 70, 1, 0, 0, 0, 360, 361, 5, 58, 0, 0, 361, 362, 5, 111, 0, 0, 362, 363, 5,
        98, 0, 0, 363, 364, 5, 106, 0, 0, 364, 365, 5, 101, 0, 0, 365, 366, 5, 99, 0, 0, 366,
        367, 5, 116, 0, 0, 367, 368, 5, 115, 0, 0, 368, 72, 1, 0, 0, 0, 369, 370, 5, 58, 0, 0,
        370, 371, 5, 105, 0, 0, 371, 372, 5, 110, 0, 0, 372, 373, 5, 105, 0, 0, 373, 374, 5,
        116, 0, 0, 374, 74, 1, 0, 0, 0, 375, 376, 5, 58, 0, 0, 376, 377, 5, 103, 0, 0, 377, 378,
        5, 111, 0, 0, 378, 379, 5, 97, 0, 0, 379, 380, 5, 108, 0, 0, 380, 76, 1, 0, 0, 0, 381,
        382, 5, 58, 0, 0, 382, 383, 5, 109, 0, 0, 383, 384, 5, 101, 0, 0, 384, 385, 5, 116, 0,
        0, 385, 386, 5, 114, 0, 0, 386, 387, 5, 105, 0, 0, 387, 388, 5, 99, 0, 0, 388, 78, 1,
        0, 0, 0, 389, 390, 5, 109, 0, 0, 390, 391, 5, 97, 0, 0, 391, 392, 5, 120, 0, 0, 392, 393,
        5, 105, 0, 0, 393, 394, 5, 109, 0, 0, 394, 395, 5, 105, 0, 0, 395, 396, 5, 122, 0, 0,
        396, 397, 5, 101, 0, 0, 397, 80, 1, 0, 0, 0, 398, 399, 5, 109, 0, 0, 399, 400, 5, 105,
        0, 0, 400, 401, 5, 110, 0, 0, 401, 402, 5, 105, 0, 0, 402, 403, 5, 109, 0, 0, 403, 404,
        5, 105, 0, 0, 404, 405, 5, 122, 0, 0, 405, 406, 5, 101, 0, 0, 406, 82, 1, 0, 0, 0, 407,
        408, 5, 40, 0, 0, 408, 84, 1, 0, 0, 0, 409, 410, 5, 41, 0, 0, 410, 86, 1, 0, 0, 0, 411,
        412, 5, 63, 0, 0, 412, 413, 3, 89, 44, 0, 413, 88, 1, 0, 0, 0, 414, 418, 3, 91, 45, 0,
        415, 417, 3, 93, 46, 0, 416, 415, 1, 0, 0, 0, 417, 420, 1, 0, 0, 0, 418, 416, 1, 0, 0,
        0, 418, 419, 1, 0, 0, 0, 419, 90, 1, 0, 0, 0, 420, 418, 1, 0, 0, 0, 421, 422, 7, 0, 0, 0,
        422, 92, 1, 0, 0, 0, 423, 426, 3, 91, 45, 0, 424, 426, 7, 1, 0, 0, 425, 423, 1, 0, 0, 0,
        425, 424, 1, 0, 0, 0, 426, 94, 1, 0, 0, 0, 427, 428, 5, 63, 0, 0, 428, 429, 3, 89, 44,
        0, 429, 96, 1, 0, 0, 0, 430, 431, 2, 48, 57, 0, 431, 98, 1, 0, 0, 0, 432, 434, 5, 45, 0,
        0, 433, 432, 1, 0, 0, 0, 433, 434, 1, 0, 0, 0, 434, 436, 1, 0, 0, 0, 435, 437, 3, 97, 48,
        0, 436, 435, 1, 0, 0, 0, 437, 438, 1, 0, 0, 0, 438, 436, 1, 0, 0, 0, 438, 439, 1, 0, 0,
        0, 439, 446, 1, 0, 0, 0, 440, 442, 5, 46, 0, 0, 441, 443, 3, 97, 48, 0, 442, 441, 1, 0,
        0, 0, 443, 444, 1, 0, 0, 0, 444, 442, 1, 0, 0, 0, 444, 445, 1, 0, 0, 0, 445, 447, 1, 0,
        0, 0, 446, 440, 1, 0, 0, 0, 446, 447, 1, 0, 0, 0, 447, 451, 1, 0, 0, 0, 448, 449, 5, 35,
        0, 0, 449, 451, 5, 116, 0, 0, 450, 433, 1, 0, 0, 0, 450, 448, 1, 0, 0, 0, 451, 100, 1,
        0, 0, 0, 452, 454, 7, 2, 0, 0, 453, 452, 1, 0, 0, 0, 454, 455, 1, 0, 0, 0, 455, 453, 1,
        0, 0, 0, 455, 456, 1, 0, 0, 0, 456, 457, 1, 0, 0, 0, 457, 458, 6, 50, 0, 0, 458, 102, 1,
        0, 0, 0, 9, 0, 418, 425, 433, 438, 444, 446, 450, 455, 1, 6, 0, 0
    ]


class pddlLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    LP = 42
    RP = 43
    VAR = 44
    NAME = 45
    VARIABLE = 46
    NUMBER = 47
    WS = 48

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'define'", "'domain'", "':typing'", "':duration-inequalities'",
                    "':time'", "':fluents'", "':adl'", "':durative-actions'", "':requirements'",
                    "'-'", "':types'", "'not'", "':predicates'", "':functions'",
                    "'assign'", "'increase'", "'decrease'", "'+'", "'*'", "'/'",
                    "'>'", "'>='", "'<='", "'<'", "'='", "'#t'", "'and'", "':parameters'",
                    "':precondition'", "':effect'", "':action'", "':event'", "':process'",
                    "'problem'", "':domain'", "':objects'", "':init'", "':goal'",
                    "':metric'", "'maximize'", "'minimize'", "'('", "')'"]

    symbolicNames = ["<INVALID>",
                     "LP", "RP", "VAR", "NAME", "VARIABLE", "NUMBER", "WS"]

    ruleNames = ["T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6",
                 "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13",
                 "T__14", "T__15", "T__16", "T__17", "T__18", "T__19",
                 "T__20", "T__21", "T__22", "T__23", "T__24", "T__25",
                 "T__26", "T__27", "T__28", "T__29", "T__30", "T__31",
                 "T__32", "T__33", "T__34", "T__35", "T__36", "T__37",
                 "T__38", "T__39", "T__40", "LP", "RP", "VAR", "NAME",
                 "LETTER", "ANY_CHAR", "VARIABLE", "DIGIT", "NUMBER", "WS"]

    grammarFileName = "pddl.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
