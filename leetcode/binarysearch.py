class bisearch:
    def binarySearch(self, nums, target):
        self.nums=nums
        self.target=target
        left, right = 0, len(self.nums)-1
        while left <= right:
            mid = (right -left) // 2 + left # the integer devision
            if self.nums[mid] == target:
                return mid
            elif self.nums[mid] < self.target:
               left = mid + 1
            elif self.nums[mid] >target:
               right =mid - 1
        return False

b1=bisearch()
b1resul=b1.binarySearch([1,2,3,7,9,10],3)
print(b1resul)
b2=bisearch()    
print(b2.binarySearch([0,2,3,7,9,10,20,40,50,60,70,80,100,120,200],60))
    


