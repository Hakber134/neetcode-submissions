class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_char = [char.lower() for char in s if char.isalnum()]
        
        return filtered_char == filtered_char[::-1]