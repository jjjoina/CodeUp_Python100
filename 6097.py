h, w = map(int, input().split())
arr = [[0] * w for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    for i in range(l):
        if d == 0:  # 가로
            arr[x-1][y-1+i] = 1
        else:       # 세로
            arr[x-1+i][y-1] = 1
for row in arr:
    print(*row)