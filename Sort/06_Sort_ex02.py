
if __name__ == '__main__':

    n = int(input())

    data = []

    for i in range(n):
        data.append(int(input()))

    data.sort(reverse=True)

    for i in range(len(data)):
        print(data[i], end=' ')