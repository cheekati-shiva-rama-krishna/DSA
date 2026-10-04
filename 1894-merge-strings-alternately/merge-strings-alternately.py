class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        FinalWord = ""

        LongerString = max(len(word1), len(word2))

        for i in range(LongerString) : 
            if i < len(word1) : 
                FinalWord += word1[i]
            if i < len(word2) : 
                FinalWord += word2[i]
        return FinalWord