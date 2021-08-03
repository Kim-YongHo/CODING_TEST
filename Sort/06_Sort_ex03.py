
if __name__ == '__main__':

    n = int(input())
    students = []

    for i in range(n):
        data = input().split()
        students.append((data[0], int(data[1])))

    students.sort(key=lambda x: x[1])

    for student in students:
        print(student[0], end=' ')
