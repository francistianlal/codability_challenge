# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:31:06 2020
first we create a function that can find the longest increasing sequence
then we duplicate and mirror the image of gates twice, this way we don can consider 
the turning process as 'crossing' the image boundry and goes into the mirror. We can get
the maximum gates crossed by counting the longest increasing sequence in the new plot
@author: frank
"""
import unittest

def Sequence(seq):
    smallest_end_value = [None] * (len(seq) + 1)
    smallest_end_value[0] = -1
    lic_length = 0
    for i in range(len(seq)):        
        lower = 0
        upper = lic_length
        while lower <= upper:
            mid = (upper + lower) // 2
            if seq[i] < smallest_end_value[mid]:
                upper = mid - 1
            elif seq[i] > smallest_end_value[mid]:
                lower = mid + 1

        if smallest_end_value[lower] == None:
            smallest_end_value[lower] = seq[i]
            lic_length += 1
        else:
            smallest_end_value[lower] = \
                min(smallest_end_value[lower], seq[i])
        
    return lic_length

def solution(A):
    bound = max(A) + 1
    multiverse = []
    index = []
    i = 0
    for point in A:
        multiverse.append(bound * 2 + point)
        index.append(12 - i)
        multiverse.append(bound * 2 - point)
        index.append(12 - i)
        multiverse.append(point)
        index.append(12 - i)
        i += 1
    return Sequence(multiverse)
                
            
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,5]
        self.assertEqual(solution(A), 2)

    def test_2(self):
        A = [15,13,5,7,4,10,12,8,2,11,6,9,3]
        self.assertEqual(solution(A), 8)

if __name__ == '__main__':
    unittest.main()



