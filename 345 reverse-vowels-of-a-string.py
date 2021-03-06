class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)==0:
            return ''
        i=0
        j=len(s)-1
        aDict=['a','e','i','o','u','A','E','I','O','U']
        ans=list(s)
        while j>=i:
            if ans[i] in aDict:
                if ans[j] in aDict:
                    ans[i],ans[j]=ans[j],ans[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return ''.join(ans)
