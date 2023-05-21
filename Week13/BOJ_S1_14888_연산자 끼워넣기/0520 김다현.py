import sys
input =sys.stdin.readline
n= int(input())
def back(cnt, num_lst, op_lst):
    if cnt==0:
        return max_val
    else:
        for i in range(4):
            if op_lst[i]!=0:
                op_lst[i]
                cnt-=1
for _ in range(n):
    num = list(map(num, input().strip().split(' ')))
    op  = list(map(num, input().strip().split(' ')))
    