# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Solution #1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Solution #2
        nums_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_dict:
                return [i, nums_dict[target-nums[i]]]
            nums_dict[nums[i]] = i