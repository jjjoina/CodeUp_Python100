arr = [list(map(int, input().split())) for _ in range(10)]
i, j = 1, 1
arr[i][j] = 9
while True:
    # 2를 찾거나 오른쪽,아래가 모두 1일 경우 break
    if arr[i][j] == 2 or (arr[i][j+1] == 1 and arr[i+1][j] == 1):
        arr[i][j] = 9
        break

    # 마킹
    arr[i][j] = 9

    # 오른쪽이 막힌 경우
    if arr[i][j+1] == 1:
        # 아래로 이동
        i += 1
    # 오른쪽이 뚫린 경우
    else:
        # 오른쪽으로 이동
        j += 1

for row in arr:
    print(*row)