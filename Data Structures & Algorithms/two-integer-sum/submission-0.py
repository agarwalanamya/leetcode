class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                if i < seen.get(complement):
                    return [i, seen.get(complement)]
                else:
                    return [seen.get(complement), i]

            seen[num] = i        
        