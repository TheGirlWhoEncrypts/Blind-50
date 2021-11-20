# Qns: Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Link: https://leetcode.com/problems/container-with-most-water/


# Solution 1
# Time complexity = O(N^2)
# Remarks: Time exceeded
def maxArea1(height):
    noOfVerticalLines = len(height)
    area = 0

    for x in range(noOfVerticalLines):
        for y in range(x + 1, noOfVerticalLines):
            # Calculate the max area = max(current max area, vertical * horizaontal)
            area = max(area, min(height[x], height[y]) * (y - x))
    return area


# Solution 2
# Time complexity = O(N)
def maxArea2(height):
    area = 0
    left, right = 0, len(height) - 1

    while left < right:
        # Calculate the max area = max(current max area, vertical * horizaontal)
        area = max(area, min(height[left], height[right]) * (right - left))

        # Update: If height[left] > height[right] then update right as (right – 1) else update left as (left + 1)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return area


# Testing
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea1(height))
print(maxArea2(height))
