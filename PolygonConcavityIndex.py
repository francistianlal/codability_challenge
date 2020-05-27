# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:44:56 2020

@author: frank
"""
import unittest

N_range = range(3,int(1e4+1))

class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
import  math
 
def whatturn(P, Q, R):
    v_1 = (Q.x - P.x, Q.y - P.y)
    v_2 = (R.x - Q.x, R.y - Q.y)
    numerator = (v_1[0]*v_2[0] + v_1[1]*v_2[1])
    length_v1 = math.sqrt(v_1[0]**2 + v_1[1]**2)
    length_v2 = math.sqrt(v_2[0]**2 + v_2[1]**2)
    denominator = length_v1 * length_v2
    quotient = numerator/denominator
    if quotient < -1: quotient = -1 # this caps off the error of
    if quotient > 1: quotient = 1 # the floating-point number and
    angle = math.acos(quotient)# avoids going out of the acos domain
 
    if v_1[0] == 0:
        if v_1[1] > 0:
            if R.x < Q.x:
                return ('l', angle)
            elif R.x > Q.x:
                return ('r', angle)
            else:
                return ('s', angle)
        else:# Assume v_1[1] != 0 (no duplicate points in A)
            if R.x < Q.x:
                return ('r', angle)
            elif R.x > Q.x:
                return ('l', angle)
            else:
                return ('s', angle)
    else:
        constant = v_1[1]*P.x - v_1[0]*P.y
        value = v_1[1]*R.x - v_1[0]*R.y
        if v_1[0] > 0:
            if value < constant:
                return ('l', angle)
            elif value > constant:
                return ('r', angle)
            else:
                return ('s', angle)
        else:
            if value < constant:
                return ('l', angle)
            elif value > constant:
                return ('r', angle)
            else:
                return ('s', angle)
             
def solution(A):
     
    array = []
    for i in range(len(A)-1):
        array.append(whatturn(A[i-1], A[i], A[i+1]))
    array.append(whatturn(A[-2], A[-1], A[0]))
     
    total_angles = 0
    for i in range(len(A)):
        if array[i][0] == 'r':
            total_angles += array[i][1]
        else:
            total_angles -= array[i][1]
    # "total_angles" should now be 360 degrees or -360 degrees,
    # depending on what side is the interior of the polygon on. 
    if total_angles > 0:
        exterior_side = 'l'
    else:
        exterior_side = 'r'
         
    for j in range(len(A)):
        if array[j][0] == exterior_side:
            return j
    return -1
                

class test_solution(unittest.TestCase):
    def test_1(self):
        A_x = [-1,1,3,0,-2]
        A_y = [3,2,1,-1,1]
        A = []
        for index in range(len(A_x)):
            A.append(Point2D(A_x[index],A_y[index]))
        self.assertEqual(solution(A), -1)

    def test_2(self):
        A_x = [-1,1,1,3,0,-2,-1]
        A_y = [3,2,1,1,-1,1,2]
        A = []
        for index in range(len(A_x)):
            A.append(Point2D(A_x[index],A_y[index]))
        self.assertIn(solution(A), [2,6])
        
    def test_3(self):
        A_xy = [[0, 0], [1, 0], [1, 1]]
        A = []
        for index in range(len(A_xy)):
            A.append(Point2D(A_xy[index][0], A_xy[index][1]))
        self.assertIn(solution(A), [-1])


if __name__ == '__main__':
    unittest.main()