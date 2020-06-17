# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:10:59 2020
77% perfromance only
https://app.codility.com/programmers/task/max_path_from_the_left_top_corner/
@author: frank
"""
import unittest
N_range = range(1,int(1e3+1))

def retrive_B(A_size,Pixel):
    i = Pixel[0]
    j = Pixel[1]
    if i == A_size[0]:
        return False
    else:
        i += 1
    Pixel_new=[i,j]
    return Pixel_new

def retrive_R(A_size,Pixel):
    i = Pixel[0]
    j = Pixel[1]
    if j == A_size[1]:   
        return False
    else:
        j += 1
    Pixel_new=[i,j]
    return Pixel_new

def solution(A):
    A_size = [len(A)-1,len(A[0])-1]
    i = j = 0
    number = str(A[i][j])
    Pixel_sto = [[i,j]]
    value_sto = 0
    Pixel_sto_before = [[i,j]]
    while number[-1] != '0' :
        for index in range(len(Pixel_sto_before)):
            Pixel = Pixel_sto_before[index]
            P_new_bottom = retrive_B(A_size, Pixel)
            if P_new_bottom != False:
                if len(Pixel_sto) == 0:
                    Pixel_sto.append(P_new_bottom)
                    value_sto = (A[P_new_bottom[0]][P_new_bottom[1]])
                else:
                    if A[P_new_bottom[0]][P_new_bottom[1]] == value_sto:
                        Pixel_sto.append(P_new_bottom)
                    elif A[P_new_bottom[0]][P_new_bottom[1]] > (value_sto):
                        value_sto = A[P_new_bottom[0]][P_new_bottom[1]]
                        Pixel_sto = [P_new_bottom]
            
            P_new_right = retrive_R(A_size, Pixel)
            if P_new_right != False:    
                P_new_right = retrive_R(A_size,Pixel)
                if len(Pixel_sto) == 0:
                    Pixel_sto.append(P_new_right)
                    value_sto = (A[P_new_right[0]][P_new_right[1]])
                else: 
                    if A[P_new_right[0]][P_new_right[1]] == (value_sto):
                       Pixel_sto.append(P_new_right)
                    elif A[P_new_right[0]][P_new_right[1]] > (value_sto):
                           Pixel_sto = [P_new_right]
                           value_sto = A[P_new_right[0]][P_new_right[1]]
                           
        number += str(value_sto)
        Pixel_sto_before = Pixel_sto
        Pixel_sto = []
        value_sto = 0
    
    number = number[:-1]
    return number
                
    
class testsolution(unittest.TestCase):
    def test_1(self):
        A = [[9,9,7],[9,7,2],[6,9,5],[9,1,2]]
        self.assertEqual(solution(A), '997952')

    def test_1(self):
        A = [[1]]
        self.assertEqual(solution(A), '1')

if __name__ == '__main__':
    unittest.main()



