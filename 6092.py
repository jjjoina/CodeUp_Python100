n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 23
for num in arr:
    cnt[num-1] += 1
print(*cnt)