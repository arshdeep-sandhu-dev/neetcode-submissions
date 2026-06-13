class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = []

        for letter in s:
            if letter.isalnum():
                string.append(letter.lower())
        return "".join(string) == "".join(string[::-1])