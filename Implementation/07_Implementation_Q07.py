if __name__ == '__main__':

    n = input()
    l = len(n)

    left, right = 0, 0

    for i in range(l // 2):
        left += int(n[i])
    for i in range((l // 2), l):
        right += int(n[i])

    if left == right:
        print('LUCKY')
    else:
        print('READY')
