for r in range(9):
    for c in range(9):
        if (r+1)*(c+1) < 10:
            print(end=(''))
        print((r+1)*(c+1),end=(' '))
    print()