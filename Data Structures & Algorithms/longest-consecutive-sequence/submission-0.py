class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_of_nums = set(nums)
        current_length = 0
        longest_length = 0

        for number in set_of_nums:
            current_length = 1
            if (number-1) in set_of_nums:
                continue
            else:
                i=1
                while number+i in set_of_nums:
                    i += 1
                    current_length += 1
                if current_length > longest_length:
                    longest_length = current_length
        
        return longest_length