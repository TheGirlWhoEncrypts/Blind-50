# Qns: Given a string s, find the length of the longest substring without repeating characters.
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Technique: Sliding Window
# Time complexity: O(n)
def lengthOfLongestSubstring(s):
    charSet = set()
    left = maxLength = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength


# Testing
# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
s = "dvdf"
# s = ""
print(lengthOfLongestSubstring(s))
