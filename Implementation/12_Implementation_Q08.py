if __name__ == '__main__':

    data = input()

    result = []
    cnt = 0

    for s in data:
        if s.isalpha():
            result.append(s)
        else:
            cnt += int(s)

    result.sort()
    result.append(str(cnt))

    result = ''.join(result)

    print(result)

