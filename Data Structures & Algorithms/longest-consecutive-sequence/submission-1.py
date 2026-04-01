class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in numset:
            if i - 1 not in numset:
                leader = i
                current = 1
                while leader + 1 in numset:
                    leader += 1
                    current += 1
                longest = max(longest, current)
        return longest

