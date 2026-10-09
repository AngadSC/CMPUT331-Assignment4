#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 Angad Chahil
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 2 Student Solution
September 2026
Author: Angad Chahil
"""
import math
from typing import List

# grid code and the shaded box technique adapted from transpositionEncrypt.py
# and transpositionDecrypt.py, Al Sweigart, "Cracking Codes with Python"
# (No Starch Press, BSD licensed) https://www.nostarch.com/crackingcodes/
def decipherMessage(key: List[int], message: str) -> str:
    numOfColumns = len(key)
    numOfRows = math.ceil(len(message) / numOfColumns)

    numOfShadedBoxes = numOfColumns * numOfRows - len(message)
    # shaded boxes go in to the botom right and towards the left from there
    numOfFullColumns = numOfColumns - numOfShadedBoxes

    columns = [''] * numOfColumns
    currentIndex = 0

    for columnNumber in key:
        column = columnNumber - 1 

        if column < numOfFullColumns:
            columnLength = numOfRows

        else:
            columnLength = numOfRows - 1 

        columns[column] = message[currentIndex:currentIndex + columnLength]
        currentIndex += columnLength
# reads grid backwards row by row 
    plaintext = ''
    for row in range(numOfRows):
        for column in range(numOfColumns):
            if row < len(columns[column]):
                plaintext += columns[column][row]

    return plaintext


def test():
    assert decipherMessage([2, 4, 1, 5, 3], "IS HAUCREERNP F") == "CIPHERS ARE FUN"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
