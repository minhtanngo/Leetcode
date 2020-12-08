## Description

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
```
Example 1:
Input: "Hello"
Output: "hello"
```
```
Example 2:
Input: "here"
Output: "here"
```
```
Example 3:

Input: "LOVELY"
Output: "lovely"
```
    
## Solution
Python code
```
class Solution:
    def toLowerCase(self, str: 'str') -> 'str':
        l1 = [] 
        for c in str:
            if "A" <= c <= "Z":
                unicode = ord(c) + 32  
                char = chr (unicode) 
                l1.append(char)
            else:
                l1.append(c) 
        return ( "".join( l1 ) )
 ```
