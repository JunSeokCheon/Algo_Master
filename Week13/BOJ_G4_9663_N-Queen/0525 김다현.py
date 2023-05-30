import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input())
arr = [[0]*n for _ in range(n)]
dx = [-1,-1,-1,1,1,1,0,0]
dy = [0,1,-1,-1,1,0,-1,1]
answer=0
def dfs(x):
    global answer
    if x==n:
        answer+=1
        return
    for i in range(n):
        