if __name__ == '__main__':

    n = int(input())
    data = list(map(int, input().split()))

    data.sort()

    goal = 1

    for check in data:
        if goal < check:
            break

        goal += check

    print(goal)
