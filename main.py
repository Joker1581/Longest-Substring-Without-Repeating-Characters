'''
from typing import List
class Solution(object):
    def rec(self, s_dict, new_s, nums: List(int)):
        num = 1
        for i in range(len(new_s)):
            if i == len(new_s) - 1:
                nums.append(num)
                return nums
            if s_dict[new_s[i+1]] - s_dict[new_s[i]] == 1:
                num += 1
            else:
                nums.append(num)
                self.rec(s_dict, new_s[(i+1):])
    def lengthOfLongestSubstring(self, s):
        s_dict = dict()
        for i in range(len(s)):
            s_dict[s[i]] = i
        new_s = []
        for i in s:
            if i not in new_s:
                new_s.append(i)
        nums = []
        res = self.rec(s_dict, new_s, nums)
        return max(res) 
'''
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    max_length = 0
    i = 0
    j = 0
    while (j < len(s)):
        if s[j] not in char_set:
            char_set.add(s[j])
            j += 1
            max_length = max(max_length, j - i)
        else:
            char_set.remove(s[i])
            i += 1
        print(char_set, max_length, i, j)
    return max_length

if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))