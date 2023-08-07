# 1-i
arr = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(19):
        arr[x-1][i] = 1 - arr[x-1][i]
        arr[i][y-1] = 1 - arr[i][y-1]
for row in arr:
    print(*row)