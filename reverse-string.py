#Link leetcode: https://leetcode.com/problems/reverse-string/

#Write a function that reverses a string. The input string is given as an array of characters char[].
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)
        for i in range(1,l//2 +1):
            s[i-1],s[-i]=s[-i],s[i-1]
        return s
