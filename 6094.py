n = int(input())
arr = list(map(int, input().split()))
min_v = arr[0]
for num in arr:
    if min_v > num:
        min_v = num
print(min_v)