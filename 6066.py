a, b, c = map(int, input().split())
for n in [a, b, c]:
    if n % 2:
        print('odd')
    else:
        print('even')