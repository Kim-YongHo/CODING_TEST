if __name__ == '__main__':

    n, m = map(int, input().split())  # 개수/공 최대 무게
    data = list(map(int, input().split()))
    data.sort()
    result = 0

    check = [0] * 11

    for cnt in data:
        check[cnt] += 1

    for i in range(1, m + 1):
        n -= check[i]
        result += n * check[i]

    print(result)