month = int(input())
season = month // 3
if season == 1:
    print('spring')
elif season == 2:
    print('summer')
elif season == 3:
    print('fall')
else:
    print('winter')