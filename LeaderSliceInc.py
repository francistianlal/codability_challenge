# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:29:10 2020
stupid solution(55%)
@author: frank
"""
import unittest
N_range = range(1,int(1e5+1))

def A_manipulate(A,i,K,ref_slice,Min_can):
    if i+K > len(A):
        return False
    else:
        if A[i-1]+1 in ref_slice:
            ref_slice[A[i-1]+1] -= 1
            ref_slice[A[i-1]] += 1
        if A[i+K-1]+1 in ref_slice:
            ref_slice[A[i+K-1]+1] += 1
            ref_slice[A[i+K-1]] -= 1
        if A[i+K-1]+1 not in ref_slice:
            ref_slice[A[i+K-1]+1] = 1
            ref_slice[A[i+K-1]] -= 1
        for key in ref_slice:
            if ref_slice[key] >= Min_can:
                return key        
        
    return None
def solution(K,M,A):
    Min_can = len(A) // 2 + 1
    matrix = set()
    ref = {}
    for number in A:
        if number not in ref:
            ref[number] = 1
        else:
            ref[number] += 1
    
    for index in range(0,K):
        if A[index] in ref:
            ref[A[index]] -= 1
        if A[index] + 1 in ref:
            ref[A[index]+1] += 1
        if A[index] + 1 not in ref:
            ref[A[index]+1] = 1    
            
    for key in ref:
        if ref[key] >= Min_can:
            matrix.add(key)    
    
    ref_slice = ref
    
    for i in range(1,len(A)-K+1):
        new = A_manipulate(A.copy(),i,K,ref_slice,Min_can)

        if new != None:    
            matrix.add(new)
    return sorted(list(matrix))
                
    
class testsolution(unittest.TestCase):
    def test_1(self):
        K,M,A = 3,5,[2,1,3,1,2,2,3]
        self.assertEqual(solution(K,M,A), [2,3])

    def test_2(self):
        K,M,A = 4,2,[1,2,2,1,2]
        self.assertEqual(solution(K,M,A), [2,3])

    def test_3(self):
        K,M,A = 1, 3, [1, 2, 3]
        self.assertEqual(solution(K,M,A), [2,3])

if __name__ == '__main__':
    unittest.main()



