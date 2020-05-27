# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:59:34 2020

@author: frank
"""
import unittest

N_range = range(0,int(1e5+1))
X_range = range(1,int(1e9+1))
element_range = range(1,int(1e9+1))

    
def solution(A,X):
    barn = {}
    count = 0
    for number in A:
        if number not in barn:
            barn[number] = 1
        else:
            barn[number] += 1
    # sort the barn and rule out the useless one
    useful = []
    for key in barn:
        if barn[key] < 2:
            continue
        elif barn[key] < 4:
            useful.append(key)
        else:
            useful.append(key)
            # count the number of fence built with one length of wood
            if key ** 2 >=X:
                count += 1

    useful.sort()
    # use binary search to find the rest
    
    for i in range(len(useful)):
        begin = i + 1
        end = len(useful) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if useful[mid] * useful[i] >= X:
                end = mid - 1
            else:
                begin = mid + 1
        # python index start with 0
        num = len(useful) - 1 - end
        count += num
            
            
    if count > int(1e9):
        return -1
    return count
             
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,2,5,1,1,2,3,5,1]
        X = 5
        self.assertEqual(solution(A,X), 2)
        
    def test_2(self):
        A = []
        X = 1
        self.assertEqual(solution(A,X), 0)
        
if __name__ == '__main__':
    unittest.main()

