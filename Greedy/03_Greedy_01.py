if __name__ == '__main__':

    price = int(input())
    coin = [500, 100, 50, 10]
    tot_cnt = 0

    for n in coin:
        count = price // n
        price %= n

        tot_cnt += count

    print(tot_cnt)