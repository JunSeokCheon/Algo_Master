#  스택을 사용
# 1. 피연산자는 스택에 삽입
# 2. 연산자는 스택에서 두 개의 값을 삭제하고 그 값을 다시 스택에 삽입
# 3. 스택에 하나의 값이 남아 있을 때 그 수가 최종 답

N = int(input())
postfix = input()
result = []
alpha = [int(input()) for i in range(N)]


for i in range(len(postfix)):
    token = postfix[i]
    if token.isalpha():
        result.append(alpha[ord(token)-65])
    else:
        op2 = result.pop()
        op1 = result.pop()
        if token == "+":
            result.append(op1+op2)
        elif token == "-":
            result.append(op1-op2)
        elif token == "*":
            result.append(op1*op2)
        elif token == "/":
            result.append(op1/op2)

print(format(result[0], ".2f"))