a, b, c = map(int, input().split())
n = 1
while True:
    if n % a == 0 and n % b == 0 and n % c == 0:
        break
    n += 1
print(n)