if __name__ == '__main__':

    n, m, k = map(int, input().split())
    data = list(map(int, input().split()))

    total = 0

    data.sort()
    data.reverse()

    print(data)

    first = data[0]
    second = data[1]

    while True:
        for i in range(k):
            total += first
            m -= 1
            if m == 0:
                break
        total += second
        m -= 1
        if m == 0:
            break

    print(total)



