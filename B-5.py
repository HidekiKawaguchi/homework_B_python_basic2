# リストの中で入力値を分割する「.split()」 => int型に変換 => input_number内に入れる
input_number = [int(s) for s in input('データを入力してください(スペース区切り) > ').split()]


def sum_num():  # 合計値の計算関数
    gokeichi = 0
    for i in input_number:
        gokeichi += i
    return gokeichi


print(f"合計値: {sum_num()}")  # 合計値の出力



def max_num(): # 最大値の計算
    saidaichi = input_number[0]
    for i in input_number:
        if saidaichi < i:
            saidaichi = i
    return saidaichi


print(f"最大値: {max_num()}")  # 最大値の出力



def min_num(): # 最小値の計算
    saisyouchi = input_number[0]
    for i in input_number:
        if i < saisyouchi:
            saisyouchi = i
    return saisyouchi


print(f"最小値: {min_num()}")  # 最小値の出力


def avg_num():  # 平均値の計算
    avg = input_number[0]
    for i in input_number:
        count = len(input_number)
        avg = sum_num() / count
    return avg


print(f"最小値: {avg_num()}")  # 平均値の出力
