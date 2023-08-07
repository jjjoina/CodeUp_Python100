n = int(input())
cnt = 1     # 2 3 4 5
sum = 0     # 1 3 6 10
while sum < n:
    sum += cnt
    cnt += 1
print(cnt-1)