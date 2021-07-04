if __name__ == '__main__':

    s = input()
    temp = []
    tot = 0

    for i in range(len(s)):
        data = int(s[i])
        temp.append(data)

    result = temp[0]

    for i in range(1, len(temp)):
        if (result <= 1 or temp[i] <= 1):
            result += temp[i]
        else:
            result *= temp[i]

    print(result)
