
if __name__ == '__main__':

    n, k = map(int, input().split())

    dataA = list(map(int, input().split()))
    dataB = list(map(int, input().split()))

    result = 0

    dataA.sort()
    dataB.sort(reverse=True)

    for i in range(k):
        if dataA[i] < dataB[i]:
            dataA[i], dataB[i] = dataB[i], dataA[i]

    for i in range(n):
        result += dataA[i]

    print(result)