# -*- coding: utf-8 -*-
"""
Created on Sun May 24 22:57:40 2020

@author: frank
"""
import unittest

N_range = range(0,int(2e6))

def solution(S):
    # build a stack and pop them one by one
    if len(S) == 1:
        return 0
    if len(S) % 2 == 0:
        return -1  
    for index in range(0,(len(S))//2):
        if S[index] != S[len(S)-index-1]:
            return -1
    return len(S)//2
                

class test_solution(unittest.TestCase):
    def test_1(self):
        S = "x"
        self.assertEqual(solution(S), 0)

    def test_2(self):
        S = "racecar"
        self.assertEqual(solution(S), 3)

    def test_3(self):
        S = ""
        self.assertEqual(solution(S), -1)

    def test_4(self):
        S = "abc"
        self.assertEqual(solution(S), -1)


if __name__ == '__main__':
    unittest.main()

