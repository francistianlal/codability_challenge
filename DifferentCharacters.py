# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:32:34 2020
score 57% 
the problem can be seem in the comment, line 62
@author: frank
"""
import unittest
N_range = range(1,int(2e5+1))

def eatleft(Storage,Slice):
    letter = Slice[0]
    Storage.append(letter)
    while True:
        trigger = 0
        if len(Slice) == 0:
            break
        if Slice[0] in Storage:
            Slice = Slice[1:]
            trigger = 1
        if len(Slice) != 0 and Slice[-1] in Storage:
            Slice = Slice[:-1]
            trigger = 1
        if trigger == 0:
            break
    length = len(Slice)
    return [length, letter, Slice]

def eatright(Storage,Slice):
    letter = Slice[-1]
    Storage.append(letter)
    while True:
        trigger = 0
        if len(Slice) == 0:
            break
        if Slice[0] in Storage:
            Slice = Slice[1:]
            trigger = 1
        if len(Slice) != 0 and Slice[-1] in Storage:
            Slice = Slice[:-1]
            trigger = 1
        if trigger == 0:
            break
    length = len(Slice)
    return [length, letter, Slice]


def solution(S,K):
    L_sto = []
    for string in S:
        if string not in L_sto:            
            L_sto.append(string)
    if len(L_sto) < K:
        return -1
    L_sto = []
    while K != 0:
        [L_1,letter_1,S_1] = eatleft(L_sto.copy(),S)
        [L_2,letter_2,S_2] = eatright(L_sto.copy(),S)  
        ## the following is a test code
        if L_1 == L_2 and S[0] != S[-1]:
            return False
        # it seems its possible that eating from the left and right give different slice with the same length
        # Not sure how to solve this
        L, letter, S = min([L_1,letter_1,S_1],[L_2,letter_2,S_2])
        L_sto.append(letter)
        K -= 1
    return len(S)
               
    
class testsolution(unittest.TestCase):
    def test_1(self):
        S = "abaacbca"
        K = 2
        self.assertEqual(solution(S,K), 3)

    def test_2(self):
        S = "aabcabc"
        K = 1
        self.assertEqual(solution(S,K), 5)

    def test_3(self):
        S = "zaaaa"
        K = 1
        self.assertEqual(solution(S,K), 1)

    def test_4(self):
        S = "aaaa"
        K = 2
        self.assertEqual(solution(S,K), -1)
    
    def test_5(self):
        S = "b"
        K = 1
        self.assertEqual(solution(S,K), 0)
if __name__ == '__main__':
    unittest.main()


