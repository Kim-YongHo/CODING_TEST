##M번 더하고  K번 연속

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    data = []

    data = list(map(int, input().split()))

    data.sort(reverse=True)

    print(data)

    first = data[0]
    second = data[1]

    temp_first = (m // (k + 1) * k + m % (k + 1)) * first

    temp_second = m // (k + 1) * second

    print(temp_first + temp_second)








