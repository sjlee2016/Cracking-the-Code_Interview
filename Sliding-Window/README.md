
#Sliding window

Usually a pattern used to solve problems dealing with contiguous subarrays of a given size.
for instance, find the maximum sum subarray of size K.

``
Array : [1,3,-6,8,2,8,-1,5], K = 3
``
If we were to find the solution using brute force algorithm, we will have to calculate the sum of every 3 contiguous elements. 

1+3-6 = -2

3-6+8 = 5

-6+8+2 = 4

the algorithm would be
```python
def find_sum(K,arr):
    result = []
    for i in range(len(arr-K+1)) :
        s = 0
        for j in range(i,i+K) :
            s += arr[j]
        result.append(s)
```

###Time Complexity : O(N*K)
the problem with this algorithm is that we have to calculate the sum of N elements multiple times. Imagine if this N is a very big number like 10,000. 
There is an overlapping part of any two consectuive subarrays of size *K*. And this overlapping part has *K-1* elements. So techinally, this problem deals with a moving window of size *K*. Every time this window moves, an element going out of the window gets subtracted and an element going in will be added. 


```python
def sliding_window(K,arr):
    result = []
    windowStart = 0
    s = 0
    for windowEnd in range(len(arr)) :
        s+= arr[windowEnd]
        if windowEnd >= K-1 :
            result.append(windowSum)
            windowSum-= arr[windowStart]
            windowStart+=1
    return result        
```
