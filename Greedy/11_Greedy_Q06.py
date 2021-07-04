
if __name__ == '__main__':

    n, m = map(int, input().split())
    temp = []

    for i in range(n):

        data = list(map(int, input().split()))

        data.sort()
        temp.append(data[0])

        data = []

    ##temp.sort(reverse=True)
    print(temp[0])
