import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
# + - × ÷ 개수의 위치는 항상 똑같다
oper_cnt = list(map(int, sys.stdin.readline().split()))
# 최소 -10억 ~ 최대 10억 -> 1e9로 표현가능
mx = -1e9
mi = 1e9

def backTracking(index, sum_value):
    # 재귀중에서도 사용 가능한 global 변수 선언
    global oper_cnt, mx, mi

    if index == n:
        mx = max(mx, sum_value)
        mi = min(mi, sum_value)
    else:
        # + 일 때
        if oper_cnt[0] > 0:
            oper_cnt[0] -= 1
            backTracking(index+1, sum_value + n_list[index])
            oper_cnt[0] += 1
        
        # - 일 때
        if oper_cnt[1] > 0:
            oper_cnt[1] -= 1
            backTracking(index+1, sum_value - n_list[index])
            oper_cnt[1] += 1
        
        # × 일 때
        if oper_cnt[2] > 0:
            oper_cnt[2] -= 1
            backTracking(index+1, sum_value * n_list[index])
            oper_cnt[2] += 1
        
        # ÷ 일 때
        if oper_cnt[3] > 0:
            oper_cnt[3] -= 1
            backTracking(index+1, int(sum_value / n_list[index]))
            oper_cnt[3] += 1

backTracking(1, n_list[0])
print(mx)
print(mi)