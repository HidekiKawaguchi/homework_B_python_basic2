def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています

    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]

    # 個人メモ_1：上記はPythonで辞書のリストから特定のキーの値のリスト。

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # 個人メモ_2：辞書のリストから特定のキーの値のリストをすべて取得
    weather_information_temperature = [d.get('temperature') for d in weather_information]
    # print(weather_information_temperature)
    # print結果 => [6.5, 7.0, 7.5, 8.2, 9.3, 9.5, 13.0, 15.0]

    # 個人メモ_3： 上記で取得した値の総和
    weather_information_temperature_total = sum(weather_information_temperature)
    # print(weather_information_temperature_total)
    # print結果 => 76.0

    # 個人メモ_4：リストの個数計算
    weather_information_count = len(weather_information)
    # print(weather_information_count)
    # print結果 => 8

    # 個人メモ_5：最後に平均を算出
    weather_information_avg = weather_information_temperature_total / weather_information_count
    print(weather_information_avg)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_station = [d.get('station') for d in weather_information if d['prefecture']=='大阪府']
    print(osaka_station)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_total_temp = [d.get('temperature') for d in weather_information if d['prefecture'] == '福岡県']
    # print(fukuoka_total_temp)
    # [13.0, 15.0]

    fukuoka_total_temp_sum = sum(fukuoka_total_temp)
    # print(fukuoka_total_temp_sum)
    # 28.0

    fukuoka_pref = [d.get('prefecture') for d in weather_information if d['prefecture'] == '福岡県']
    fukuoka_pref_len = len(fukuoka_pref)
    # print(fukuoka_pref_len)
    # 2

    fukuoka_temp_avg = fukuoka_total_temp_sum / fukuoka_pref_len
    print(fukuoka_temp_avg)


if __name__ == '__main__':
    main()
