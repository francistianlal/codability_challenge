# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:36:26 2020
There is sth wrong with this program
Also the question make it unclear what to do when N is odd like N = 5
@author: frank
"""
import unittest

N_range = range(2,int(26)+1)

    
def solution(N,S,T):
    # first decide the four areas
    size_block = (N // 2) ** 2
    # block spare area from I to IV
    Block_spare = [size_block] * 4
    def check_position(B,Block):
        row = int(B[0])
        column = int(ord(B[1]))
        if row in range(1, N//2 +1):
            if column in range(ord('A'),ord('A')+ N//2):
                Block[0] -= 1
            elif column in range(ord('A')+ N//2,ord('A')+ N):
                Block[1] -= 1
        if row in range(N//2 +1, N + 1):
            if column in range(ord('A'),ord('A')+ N//2):
                Block[2] -= 1
            elif column in range(ord('A')+ N//2,ord('A')+ N):
                Block[3] -= 1
                
            
    for barrel in S.split():
        # check the seat for dwarf in four sector
        check_position(barrel,Block_spare)
    # calculate the maximum number of dwarf possible and seats for
    # dwarf available
    I = min(Block_spare[0],Block_spare[3])
    II = min(Block_spare[1],Block_spare[2])
    Max_seated = [I,II,II,I]
    Empty_seats = [0] * 4
    for dwarf in T.split():
        check_position(dwarf,Empty_seats)
    # maximum seats
    count = 0
    for index in range(len(Max_seated)):
        if Max_seated[index] + Empty_seats[index] < 0 :
            return -1
        count += Max_seated[index] + Empty_seats[index]
    
    return count

class testsolution(unittest.TestCase):
    def test_1(self):
        N = 4 
        S = "1B 1C 4B 1D 2A"
        T = "3B 2D"
        self.assertEqual(solution(N,S,T), 6)
       
    def test_2(self):
        (N,S,T) = (4, '', '4D')
        self.assertEqual(solution(N,S,T), 15)     
    
    def test_3(self):
        N = 5 
        S = "1B 1C 4B 1D 2A"
        T = "3B 2D"
        self.assertEqual(solution(N,S,T), 6)    

    def test_4(self):
        N = 2 
        S = "1A 1B 2A 2B"
        T = ""
        self.assertEqual(solution(N,S,T), 0)    
        
if __name__ == '__main__':
    unittest.main()

