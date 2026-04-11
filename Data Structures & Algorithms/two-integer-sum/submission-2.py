class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            if num in nums_dict:
                return [nums_dict[nums[i]],i]
            nums_dict[target - nums[i]] = i
            i = i+1
