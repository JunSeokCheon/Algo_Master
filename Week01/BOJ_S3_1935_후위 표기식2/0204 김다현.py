n= int(input())
s=input()
stack=[]
num=[0]*n
#일단 A~E값을 담는다.
for i in range(n):
    num[i]= int(input()) 

#연산자들을 스택에 담아두고 
for i in s:
    if 'A' <= i <= 'Z': #피연산자라면 스택에 저장
        stack.append(num[ord(i)-ord('A')]) #i가 B라면 1
    else:
        st2 = stack.pop()
        st1 = stack.pop()
    if i =='+': #연산자라면 연산
        stack.append(st1+st2)
    elif i=='-':
        stack.append(st1-st2)
    elif i=='*':
        stack.append(st1*st2)
    elif i=='/':
        stack.append(st1/st2)
    
print('%.2f' %stack[0])