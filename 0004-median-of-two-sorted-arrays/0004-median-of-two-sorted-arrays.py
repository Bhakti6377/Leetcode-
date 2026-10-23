class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        x = []
        x = num1 + num2
        x.sort()
        if (len(x)%2)==0:
            return (x[len(x)//2]+x[len(x)//2-1])/2
        else:
            return x[len(x)//2]