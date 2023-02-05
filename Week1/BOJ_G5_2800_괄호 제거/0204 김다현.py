from itertools import combinations
s= list(input().strip())
stack=[]
tmp=[]
answer=[]
for idx, i in enumerate(s):
    if i=='(':
        stack.append(idx)
    elif i==')':
        tmp.append((stack.pop() , idx))
for i in range(1,len(tmp)+1):
    c=combinations(tmp, i)
    for j in c: #j는 조합들의 list [(3,5),(0,6)]
        target = s
        #괄호제거
        for k in j: #(3,5)
            target[k[0]]=""
            target[k[1]]=""
        answer.append(''.join(target))
for ans in sorted(list(answer)):
    print(ans)