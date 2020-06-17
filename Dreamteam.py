# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:02:27 2020

@author: frank
"""
import unittest
N_range = range(1,int(2e5+1))

def solution(A,B,F):
    dif = [] # the difference between A and B
    for index in range(len(A)):
        dif.append(A[index]-B[index])
    ref = sorted(range(len(dif)),key = dif.__getitem__)
    count = 0
    while  F != 0:
        count += A[ref.pop()]
        F -= 1
    while len(ref) != 0:
        count += B[ref.pop()]
    
    return count
               
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [4,2,1]
        B = [2,5,3]
        F = 2
        self.assertEqual(solution(A,B,F), 10)

    def test_2(self):
        A = [7,1,4,4]
        B = [5,3,4,3]
        F = 2
        self.assertEqual(solution(A,B,F), 18)

    def test_3(self):
        A = [5,5,5]
        B = [5,5,5]
        F = 1
        self.assertEqual(solution(A,B,F), 15)

if __name__ == '__main__':
    unittest.main()
