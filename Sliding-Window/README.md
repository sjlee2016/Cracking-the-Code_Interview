
#Sliding window

Usually patterns used to solve problems dealing with contiguous subarrays of a given size.
for instance, find the maximum sum subarray of size K.

Array : [1,3,-6,8,2,8,-1,5], K = 3

If we were to find the solution using brute force algorithm, we will have to calculate the sum of every 3 contiguous elements. 
1+3-6 = -2
3-6+8 = 5
-6+8+2 = 4

the algorithm would be
