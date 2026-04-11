from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = Counter(nums)

        sorted_list = frequency_map.most_common(k)

        result = []

        for i in range(k):
            result.append(sorted_list[i][0])
        
        return result
