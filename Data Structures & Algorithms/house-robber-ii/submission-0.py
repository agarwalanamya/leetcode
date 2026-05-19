class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(self.straightLineRob(nums[1:]), self.straightLineRob(nums[:len(nums)-1]))


    def straightLineRob (self, nums: List[int]) -> int:
        
        rob1 = 0
        rob2 = 0
        
        for number in nums:
            current_max = max(rob1 + number, rob2)
            rob1 = rob2
            rob2 = current_max
        
        return current_max