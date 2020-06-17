# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:47:00 2020
stupid solution, listed all possibility and count the rows
@author: frank
"""
import unittest
import itertools

#Possible characters
N_range = range(1,int(1e5+1))

def shift(I,A):
    B = A.copy()
    shift = list()
    count = 0
    for index, string in enumerate(I) :
        if string == 1:
            shift.append(index)
    
    for index in range(len(A)):
        case = B.copy()[index]
        for number in shift:
            case[number] = abs(case[number]-1)
        if sum(case) == 0 or sum(case) == len(B[0]):
            count += 1
        for number in shift:
            case[number] = abs(case[number]-1)
    return count

def solution(A):
    n = [0,1]
    l = len(A[0])
    count = 0
    r = list(itertools.product(n, repeat=l))
    for index in range(0,2**len(A[0])):
        
        count = max(count,shift(r[index],A))

    return count
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [[0,0,0,0],[0,1,0,0],[1,0,1,1]]
        self.assertEqual(solution(A), 2)

    def test_2(self):
        A = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]
        self.assertEqual(solution(A), 4)

    def test_3(self):
        A = [[1, 1], [1, 0]]
        self.assertEqual(solution(A), 1)

if __name__ == '__main__':
    unittest.main()





