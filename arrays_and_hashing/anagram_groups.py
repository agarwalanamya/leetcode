class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        solution_dict ={}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in solution_dict:
                solution_dict[sorted_word].append(word)
            else:
                solution_dict[sorted_word] = [word]
        
        return list(solution_dict.values())
