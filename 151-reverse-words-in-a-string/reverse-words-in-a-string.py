class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        print(words)
        
        return " ".join(words[::-1])