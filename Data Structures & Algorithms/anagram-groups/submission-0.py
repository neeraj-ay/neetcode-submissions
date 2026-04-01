class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for i in strs:
            count = [0] * 26
            for j in i:
                pos = ord(j) - ord('a')
                count[pos] += 1
            final = tuple(count)
            if final not in words:
                words[final] = []
            words[final].append(i)
        return list(words.values())