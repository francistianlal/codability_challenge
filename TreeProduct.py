# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:19:25 2020
Using brute force to find the best cut.
only 38% performance
@author: frank
"""
import unittest

N_range = range(1,int(5e4))

# make a tree link dict, the bridge cut must happen in places with the most link
def tree_generator(A,B):   
    tree_ref = {}
    for index in range(len(A)):
        if A[index] in tree_ref:
            tree_ref[A[index]].append(B[index])
        else:
            tree_ref[A[index]] = [B[index]]
        
        if B[index] in tree_ref:
            tree_ref[B[index]].append(A[index])
        else:
            tree_ref[B[index]] = [A[index]]

    return tree_ref

def check_in_set(keys,values,Set):
    if keys in Set:
        return True
    for number in values:
        if number in Set:
            return True
    return False
            

def solution(A, B):

    def two_cut():
        result = 0
        for i in range(len(A)-1):
            j = i + 1
            while j < len(A):
                A_copy = A.copy()
                B_copy = B.copy()
                # cut two bridge
                del A_copy[j],A_copy[i],B_copy[j],B_copy[i]
                j += 1
    
                tree = tree_generator(A_copy, B_copy)
                # create three branch
                I = {A_copy[0]}
                II= set()
                III= set()
                for key in tree:
                    if check_in_set(key,tree[key],I):
                        I.add(key)
                        I.add(tree[key][0])
                    else:
                        if check_in_set(key,tree[key],II):
                            II.add(key)
                            II.add(tree[key][0])
                        elif len(II) == 0:
                            II.add(key)
                            II.add(tree[key][0])
                        else:
                            if check_in_set(key,tree[key],III):
                                III.add(key)
                                III.add(tree[key][0])
                            elif len(III) == 0:
                                III.add(key)
                                III.add(tree[key][0])
                            else:
                                continue
                if len(III) == 0:
                    count_III = 1
                else:    
                    count_III = len(III)                
                if len(II) == 0:
                    count_II = 1
                else:
                    count_II = len(II)
                count_I = len(I)
                result = max(result, count_I*count_II*count_III)
        return result
        
    def one_cut():
        result = 0
        for i in range(len(A)):

                A_copy = A.copy()
                B_copy = B.copy()
                # cut one bridge
                del A_copy[i],B_copy[i]
                tree = tree_generator(A_copy, B_copy)
                # create two branch
                I = {A_copy[0]}
                II= set()
                for key in tree:
                    if check_in_set(key,tree[key],I):
                        I.add(key)
                        I.add(tree[key][0])
                    else:
                        if check_in_set(key,tree[key],II):
                            II.add(key)
                            II.add(tree[key][0])
                        elif len(II) == 0:
                            II.add(key)
                            II.add(tree[key][0])
                        else:
                            raise TypeError('more than three branch')
                if len(II) == 0:
                    count_II = 1
                else:
                    count_II = len(II)
                count_I = len(I)
                result = max(result, count_I*count_II)
        return result

    two_cut_max = one_cut_max = no_cut = 0
    if len(A) > 2:
        two_cut_max = two_cut()
    if len(A) > 1:
        one_cut_max = one_cut()
    
    no_cut = len(A) + 1
    
    defence = max(two_cut_max,one_cut_max,no_cut)
    
    return str(defence)
                
            
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [0,1,1,3,3,6,7]
        B = [1,2,3,4,5,3,5]
        self.assertEqual(solution(A,B), '18')

    def test_2(self):
        A = [0,1]
        B = [1,2]
        self.assertEqual(solution(A,B), '3')

    def test_3(self):
        A = [0]
        B = [1]
        self.assertEqual(solution(A,B), '2')
        
    def test_4(self):
        A = [0,1,2,3]
        B = [1,2,3,4]
        self.assertEqual(solution(A,B), '6')
if __name__ == '__main__':
    unittest.main()
