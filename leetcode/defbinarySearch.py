def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (right - left) // 2 + left
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return False
print(binarySearch([0,1,2,3,4,5,6,7],7))