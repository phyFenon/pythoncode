class Solution(object):
    def __init__(self,nums):
        self.nums=nums
        self.new=[]
        pass
    def removeDuplicates(self):
        """
        :type nums: List[int]
        :rtype: int
        """
        for a in self.nums:
            if a not in self.new:
                self.new.append(a)
        return self.new

s1=Solution([1,1,1,2,2,3,3,4,4,5,5,7,8])
print(s1.removeDuplicates())