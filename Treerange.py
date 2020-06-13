# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:23:54 2020
only 18 percent rate
https://app.codility.com/programmers/task/tree_range/
@author: frank
"""
import unittest
N_range = range(2,1001)

def find_stops(T,a,b):
    stops = []
    start = a 
    end = b
    check = True
    while check:
        check = T[start] != end and T[end] != start
        stops.append(start)
        stops.append(end)
        start = T[start]
        end = T[end]
    return set(stops) 
    
def check_cross_village(stops,a,b):
    for number in stops:
        if number not in range(a,b+1):
            return False
    return True
    
def check_miss_fest(T,stops,a,b):
    start = a
    while start != b:
        stop = find_stops(T,start,start+1)
        for number in stop:
            if number not in stops and number not in range(a,b+1):
                return False
                break
        start += 1
    return True

    return True

def solution(T):
    count = len(T)
    for start in range(len(T)-1):
        for end in range(start+1,len(T)):
            stops = find_stops(T,start,end)
            print(start,end,check_cross_village(stops,start,end),check_miss_fest(T,stops,start,end))
            if check_cross_village(stops,start,end) and check_miss_fest(T,stops,start,end):
                count += 1

    return count
            
class testsolution(unittest.TestCase):
    def test_1(self):
        T = [2,0,2,2,1,0]
        self.assertEqual(solution(T), 12)

    def test_2(self):
        T = [2,2,2]
        self.assertEqual(solution(T), 5)

    def test_2(self):
        T = [0, 3, 1, 0, 0, 3, 5]
        self.assertEqual(solution(T), 14)

if __name__ == '__main__':
    unittest.main()



