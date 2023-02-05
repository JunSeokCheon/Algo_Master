s=list(input())
tmp=1
res=0
stack=[]

for num, i in enumerate(s):
    if i=='(':
        tmp*=2
        stack.append(i)
    elif i=='[':
        tmp*=3
        stack.append(i)
    elif i==')':
        if not stack or stack[-1]=='[': #올바르지 못한 문자열
            res=0
            break
        if s[num-1]=='(':
            res+=tmp
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1]=='(': #올바르지 못한 문자열
            res=0
            break
        if s[num-1]=='[':
            res+=tmp
        stack.pop()
        tmp //=3
if stack:
    print(0)
else:
    print(res)