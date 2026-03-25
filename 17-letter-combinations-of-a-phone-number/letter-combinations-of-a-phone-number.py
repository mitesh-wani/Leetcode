class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitLetter={
        "2":["a","b","c"],
        "3":["d","e","f"],
        "5":["j","k","l"],
        "4":["g","h","i"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}
        for d in digits:
            if d not in digitLetter:
                return []
                
        n=len(digits)
        res=[]
        combination=""
        def printLetterCombination(i,combination=""):
            if i>=n:
                res.append(combination)
                return
            possible_letter=digitLetter[digits[i]]
            for l in possible_letter:
                printLetterCombination(i+1,combination+l)
        printLetterCombination(0,"")
        return res

            