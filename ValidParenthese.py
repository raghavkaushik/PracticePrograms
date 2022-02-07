#Link : https://leetcode.com/problems/valid-parentheses/

#This problem is based upon leetcode valid parentheses.

def valid(s:str):
    stack=[]
    for i in s:
        if i in ['[','{','(']:
            stack.append(i)
        if i == ')':
            if stack.pop()!='(':
                return False
        if i == ']':
            if stack.pop()!='[':
                return False
        if i == '}':
            if stack.pop()!='{':
                return False
    if len(stack)>0:
        return False
    return True

ab='()[][{}]'
output=valid(ab)
print(f"Valid Parantheses:{output}")
