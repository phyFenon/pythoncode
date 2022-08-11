'''
Find the solution of summation of two numbers in a set.
This method is adapted for multiple solutions.
The time complexitity of this method is O(n^2).
Question: what is the Hash map? Hashtable is the dict in python.
'''
class Solution:
    result=[]
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums=nums
        self.target=target
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.target==self.nums[i]+self.nums[j]:
                    self.result.append([i,j]) 
        return self.result
            
   
                
set1=Solution() # instantiate the case                
print(set1.twoSum([1,2,3,4,5,6],10))
set2=Solution()
print(set2.twoSum([0,0,1,2,3],1))