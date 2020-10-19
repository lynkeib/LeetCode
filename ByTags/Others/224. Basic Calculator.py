class Solution(object):
    def calculate(self, s):
        stack=[]
        num=0; res=0; sign=1
        for c in s:
            if c.isdigit():
                num=num*10+(ord(c)-ord('0'))
            elif c=='(':
                stack.append(res)
                stack.append(sign)
                res=0; sign=1
            else:
                res+=num*sign
                num=0
                if c=='+': sign=1
                elif c=='-': sign=-1
                elif c==')':
                    sign=1
                    res*=stack.pop()
                    res+=stack.pop()
        return res+num*sign