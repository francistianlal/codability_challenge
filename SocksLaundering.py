# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:30:13 2020

@author: frank
"""
import unittest

K_range = range(0,51)
CD_range = range(1,51) 
 
def solution(K,C,D):
    
    sock_sort = {}
    count = 0
    for sock in C:
        if sock not in sock_sort:
            sock_sort[sock] = 1
        else:
            del sock_sort[sock]
            count += 1
    dirty_sock_sort = {}
    dirty_pair = 0
    for smelly in D:
        if K == 0:
            break
        else:
            if smelly in sock_sort:
                # if there is a pair wash the dirty one
                del sock_sort[smelly]
                K -= 1
                count += 1
            else:
                if smelly not in dirty_sock_sort:
                    dirty_sock_sort[smelly] = 1
                else:
                    del dirty_sock_sort[smelly]
                    dirty_pair += 1
    if K != 0:
        count += min(K//2,dirty_pair)
    
    return count
             
class testsolution(unittest.TestCase):
    def test_1(self):
        K,C,D = 2,[1,2,1,1],[1,4,3,2,4]
        self.assertEqual(solution(K,C,D), 3)

if __name__ == '__main__':
    unittest.main()
