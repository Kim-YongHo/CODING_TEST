if __name__ == '__main__':
    n = 1260
    count = 0
    rest = n
    # 500, 100, 50, 10

    coin_type = [500, 100, 50, 10]

    for i in coin_type:
        temp = rest // i
        rest %= i
        count += temp

    print(count)

