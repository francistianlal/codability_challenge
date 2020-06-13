# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:17:15 2020
https://app.codility.com/programmers/task/replacing_books/
53%
@author: frank
"""
import unittest

N_range = range(1,int(1e5+1))
A_range = range(1,int(1e5+1))

def left_shift(index,ref_n,ref_v):
    if index == 0:
        return [ref_n[0],ref_n,ref_v]
    else:
        ref_n[index - 1] -= 1
        ref_n[index] += 1
        if ref_n[index - 1] == 0:
            del ref_v[index -1],ref_n[index - 1]
        if index > 1:
            if ref_v [index - 1] == ref_v [index - 2]:
                ref_n[index - 1] += ref_n[index - 2]
                del ref_n[index - 2],ref_v[index-2]
        max_length = max(ref_n)        
        return [max_length,ref_n,ref_v]

def right_shift(index,ref_n,ref_v):
    if index == len(ref_n) - 1:
        return [ref_n[index],ref_n,ref_v]
    else:
        ref_n[index + 1] -= 1
        ref_n[index] += 1
        if ref_n[index + 1] == 0:
            del ref_v[index + 1],ref_n[index + 1]
        if index < len(ref_n) - 3:
            if ref_v [index] == ref_v [index + 1]:
                ref_n[index] += ref_n[index + 1]
                del ref_n[index + 1],ref_v[index + 1]
        max_length = max(ref_n)        
        return [max_length,ref_n,ref_v]

def solution(A,K):
    ref_value = [A[0]]
    ref_number = [1]
    for index in range(1,len(A)):
        if A[index] == ref_value[-1]:
            ref_number[-1] += 1
        else:
            ref_value.append(A[index])
            ref_number.append(1)
    max_length,max_n,max_v = max(ref_number),ref_number.copy(),ref_value.copy()
    occurence_max = max_length  
    while K != 0:
        for index in range(len(ref_number)):
            fi = index,ref_number,ref_value
            if ref_number[index] == occurence_max:
                max_length,max_n,max_v = max([max_length,max_n,max_v],left_shift(fi[0],fi[1].copy(),fi[2].copy()),right_shift(fi[0],fi[1].copy(),fi[2].copy()))
        # update the references
        
        ref_number,ref_value = max_n,max_v
        occurence_max = max_length
        K -= 1
    
    return max_length
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [1,1,3,4,3,3,4]
        K = 2
        self.assertEqual(solution(A,K), 5)

    def test_2(self):
        A = [4, 5, 5, 4, 2, 2, 4]
        K = 0
        self.assertEqual(solution(A,K), 2)

    def test_3(self):
        A = [1, 3, 3, 2]
        K = 2
        self.assertEqual(solution(A,K), 4)

if __name__ == '__main__':
    unittest.main()





