# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:26:52 2020

@author: frank
"""
import unittest

N_range = range(0,int(1e5+1))

from bisect import bisect
 
def solution(A):

    array = []
    count = 0
    for index, number in enumerate(A):
        pos = bisect(array, number)
        count += len(array) - pos
        array.insert(pos, number)


            
        
    if count > int(1e9):
        return -1
    return count
             
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [-1,6,3,4,7,4]
        self.assertEqual(solution(A), 4)

    def test_2(self):
        A = [5, 4, 3, 2, 1]
        self.assertEqual(solution(A), 10)
if __name__ == '__main__':
    unittest.main()


