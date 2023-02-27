import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
trash = []

for i in range(K):
    r, c = map(int, input().split())
    trash.append((r, c))



