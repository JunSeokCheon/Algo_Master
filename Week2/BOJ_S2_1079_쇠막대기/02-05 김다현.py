s=list(input())
stack=[]
tmp=0

for num, i in enumerate(s):
    print(f'stack:{stack}')
    print(f'tmp:{tmp}')
    if i=='(': 
        stack.append(i)
    
    elif  s[num-1]=='(' and i==')': #레이터일때 
        stack.pop()
        tmp+=len(stack)
    else:    
        stack.pop()
        tmp+=1 #괄호의 쌍이니까
print(tmp)