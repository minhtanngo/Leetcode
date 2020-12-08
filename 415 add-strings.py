#Leetcode link: https://leetcode.com/problems/add-strings/
#Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#The length of both num1 and num2 is < 5100.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = ''
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while (i >= 0) or (j>=0) or (carry > 0):
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            l += str(carry%10)
            carry = carry //10
        return l[::-1]
