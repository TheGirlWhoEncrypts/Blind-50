# Qns: Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


# Technique: Binary Search
# Time complexity: O(log n)

def findMin(nums):
    left, right = 0, len(nums) - 1

    # Min value when mid > mid + 1
    while left < right:
        # Find mid element
        mid = left + (right - left) // 2
        # RHS is sorted if nums[mid] < nums[right]
        if nums[mid] < nums[right]:
            right = mid
        # LHS is sorted if nums[left] < nums[mid]
        else:
            left = mid + 1

    return nums[left]


nums = [3, 4, 5, 1, 2]
print(findMin(nums))
