# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:06:03 2020

@author: frank

"""
import unittest

N_range = range(0,int(1e3+1))
class Tree:
    def __init__(self,node):
        (origin,left,right) = node
        self.o = origin
        if left != None:    
            self.l = Tree(left)
        else:
            self.l = None
        if right != None:
            self.r = Tree(right)
        else:
            self.r = None

def solution(T):
    if T.l == None and T.r == None:
        return 0
    elif T.l == None:
        return 1 + solution(T.r)
    elif T.r == None:
        return 1 + solution(T.l)
    else:
        return 1 + max(solution(T.l), solution(T.r))

class test_solution(unittest.TestCase):
    def test_1(self):
        branches = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
        T = Tree(branches)
        self.assertEqual(solution(T), 2)

if __name__ == '__main__':
    unittest.main()