#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 <<Angad Chahil>>
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
CMPUT 331 Assignment 1 Student Solution
September 2026
Author: Angad Chahil
"""


from sys import flags
import a1p1
from a1p1 import encrypt, decrypt
a1p1.SHIFTDICT, a1p1.LETTERDICT = a1p1.get_map()



LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def crack_caesar(ciphertext, val_words):
    candidates = []
    for key in LETTERS:
        plaintext = decrypt(ciphertext, key)
        words = [''.join(c for c in w if c in LETTERS) for w in plaintext.split()]
        words = [w for w in words if w]
        if words and all(w in val_words for w in words):
            candidates.append((plaintext, key))
    return min(candidates) if candidates else (None, None)
#gets the plain text by brute forcing caesar by going throuhg everyy possuible keys, 
# see if all the words arein the set of all words 

def form_dictionary(text_address='carroll-alice.txt'):
    val_words = set()
    with open(text_address) as text_file:
        for word in text_file.read().upper().split():
            word = ''.join(c for c in word if c in LETTERS)
            if word:
                val_words.add(word)
    return val_words

#read file and returns a set of thw words it contained, has no du0plicates 

def test():
    assert crack_caesar('TBIZLJB QL TLKABOIXKA', form_dictionary()) == ('WELCOME TO WONDERLAND', 'X')


if __name__ == "__main__" and not flags.interactive:
    test()