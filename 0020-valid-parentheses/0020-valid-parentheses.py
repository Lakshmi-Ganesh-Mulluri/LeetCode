class Solution(object):
    def isValid(self, s):
        a=[]
        for i in s:
            if i=="(":
                a.append(")")
            elif i=="{":
                a.append("}")
            elif i=="[":
                a.append("]")
            elif a!=[] and i==a[-1]:
                a.pop()
            else:
                return False
        if a==[]:
            return True
        else:
            return False