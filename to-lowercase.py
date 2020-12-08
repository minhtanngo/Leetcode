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