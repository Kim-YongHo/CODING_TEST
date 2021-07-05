if __name__ == '__main__':

    s = input()

    result = int(s[0])

    for i in range(1, len(s)):

        temp = int(s[i])
        if (temp <= 1) or (result <= 1):
            result += temp
        else:
            result *= temp

    print(result)