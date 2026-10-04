class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                l.append(i)

            elif len(l) != 0 and i==')' and l[len(l)-1]=='(':
                l.pop()
            
            elif len(l) != 0 and i==']' and l[len(l)-1]=='[':
                l.pop()

            elif len(l) != 0 and i=='}' and l[len(l)-1]=='{':
                l.pop()

            else:
                return False

        if len(l) == 0:
            return True

        else:
            return False