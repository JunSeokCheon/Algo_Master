# 만약 대기열의 수가 stack의 head의 수보다 크면 그 사잇값 push
# 대기열의 수가 stack의 head의 수와 같으면 pop
# 대기열의 수가 stack의 head의 수 보다 작으면 불가능

N = int(input())

stack = []
result = []

head = 1

for i in range(N):
    waiting = int(input())

    while head <= waiting:
        stack.append(head)
        result.append('+')
        head += 1

    if waiting == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        result.append("NO")
        break

if "NO" in result:
    print("NO")
else:
    for i in result:
        print(i)