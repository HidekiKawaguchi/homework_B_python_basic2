import random

dice_num = int(input('サイコロの面の数は?: '))
dice_times = int(input('何回振りますか?: '))

result_list = []

for i in range(0, dice_times):
    result_list.append(random.randint(1, dice_num))
print(result_list)
