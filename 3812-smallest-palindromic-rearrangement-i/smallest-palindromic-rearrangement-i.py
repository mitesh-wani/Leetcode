class Solution:
    def smallestPalindrome(self, s: str) -> str:
        size=len(s)
        if size==1 or size==2:
            return s
        def sort_join(s):
            half_size=len(s)//2
            sorted_str="".join(sorted(s[:half_size]))
            reverse_str="".join(sorted(s[:half_size],reverse=True))
            return sorted_str,reverse_str

        if size%2==0:
            sorted_str,reverse_str=sort_join(s)
            return sorted_str+reverse_str
        else:
            sorted_str,reverse_str=sort_join(s)
            return sorted_str+(s[size//2])+reverse_str

        