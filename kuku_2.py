row_number = int(input('行数を入力してください: '))
col_number = int(input('列数を入力してください: '))

for r in range(row_number):
    for c in range(col_number):
        if (r+1)*(c+1) < 10:
            print(end=(''))
        print((r+1)*(c+1),end=(' '))
    print()