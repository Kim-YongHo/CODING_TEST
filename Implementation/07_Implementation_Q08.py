if __name__ == '__main__':

    s = input()
    l = len(s)
    temp_num = []
    temp_s = []
    sum = 0

    for i in range(l):
        if (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            temp_num.append(s[i])
        else:
            temp_s.append(s[i])

    for i in range(len(temp_num)):
        sum += int(temp_num[i])

    temp_s.sort()
    temp_s.append(str(sum))

    temp_s = ''.join(temp_s)

    print(temp_s)