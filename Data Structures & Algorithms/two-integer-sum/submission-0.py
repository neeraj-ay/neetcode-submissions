class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mylist = {}
        
        for i, n in enumerate(nums):
            needed = target - n
            if needed in mylist:
                return [mylist[needed], i]

            mylist[n] = i


