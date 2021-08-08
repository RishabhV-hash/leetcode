"""A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?"""
"""Solved using Memoisation of Dynamic Programming Time Complexity of O(m*n) and Space complexity of O(m+n)"""
"""What we have done with storing the results is called memoization. We are basically trading time for space (memory). However, space is negligible compared to the time saved by memoization."""

class Solution:
    def __init__(self):
        self.memo = {} #creating an object which has a key component in python it's a dictionary but the implementation varies according to the programming language
    def uniquePaths(self, m:int, n:int)->int:
        key = f'{m},{n}' #storing the values of the rows and colum as a string separated by a comma eg:3,2
        if m ==1 and n ==1: #this is a base case(where know what the output is going to be)
            return 1
        if m == 0 or n == 0: # this a case where the output is invalid also can be considered a base case
            return 0
        if key in self.memo:
            return self.memo[key] #if the key is found in the memo the value of the key in the object is returned
        else:
            self.memo[key]= self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        return self.memo[key]