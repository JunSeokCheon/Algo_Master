n=int(input())
answer=[]
result=[]
cnt=1
for i in range(n):
    answer.append(int(input())) #정답지를 받아두기

stack = list(range(1,answer[0]+1)) #첫번째 원소는 무조건 받아야함
for _ in range(answer[0]):
    cnt+=1
    result.append('+')
while answer: #answer이 빈배열이 될때까지
    if stack[-1]==answer[0]:
        stack.pop()
        answer.pop(0)
        result.append('-')
    else:
        for i in range(cnt, answer[0]+1):
            result.append('+')
            cnt+=1
            stack.append(i)
        continue
if not stack:
    for i in result:
        print(i)
else:
    print('NO')
    
    