# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:38:03 2020

@author: frank
"""
import unittest

PC_range = range(1,int(3e4+1))

def solution(P,C):
    
    return min(C,P//2)
             
class testsolution(unittest.TestCase):
    def test_1(self):
        P,C = 10,3
        self.assertEqual(solution(P,C), 3)
        
    def test_2(self):
        P,C = 5,3
        self.assertEqual(solution(P,C), 2)


if __name__ == '__main__':
    unittest.main()




