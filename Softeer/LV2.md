## [21년 재직자 대회 예선] 전광판

```python
import sys

segment = { '0' : '1111011',
            '1' : '0010010',
            '2' : '0111101',
            '3' : '0110111',
            '4' : '1010110',
            '5' : '1100111',
            '6' : '1101111',
            '7' : '1110010',
            '8' : '1111111',
            '9' : '1110111',
            ' ' : '0000000 ' }

t = int(input())

for k in range(t):
    x, y = sys.stdin.readline().split()
    result = 0

    x = (5-len(x)) * (' ') + x
    y = (5-len(y)) * (' ') + y

    for i in range(5):
        for j in range(7):
            result += (segment[x[i]][j] != segment[y[i]][j])
    
    print(result)

```



## [21년 재직자 대회 예선] 회의실 예약

```python
import sys

roomCnt, reserveCnt = map(int, input().split()) # 회의실 갯수, 예약 횟수
roomList = [] # 회의실 이름

# print(roomCnt, reserveCnt)

# 회의실 별 예약 현황
state = [[False for i in range(9)] for i in range(roomCnt)]

# print(state)

# 회의실 명단 리스트
for i in range(roomCnt):
    roomList.append(input())

roomList.sort()

# 회의실 별 예약 현황 input
for i in range(reserveCnt):
    roomName, startTime, endTime = input().split()
    startTime = int(startTime) - 9
    endTime = int(endTime) - 9

    # 예약 현황에 정렬한 회의실명을 기준으로 예약 여부 기입
    for j in range(startTime, endTime):
        state[roomList.index(roomName)][j] = True # True = 예약

#print(state)

for i in range(roomCnt):
    print('Room ' + roomList[i] + ':')
    
    # 예약이 풀인 경우
    if False not in state[i]: # False = 예약X (전부 예약된 상태)
        print('Not available')

    else:
        checkTime = 0
        useTime = []

        while (checkTime < 9):
            reserveStart, reserveEnd = 0, 0
            if not state[i][checkTime]: # False이면 예약 가능해서
                reserveStart = checkTime

                while(checkTime<9 and not state[i][checkTime]):
                    checkTime += 1
                reserveEnd = checkTime -1
                useTime.append([reserveStart, reserveEnd])
            checkTime += 1
        print(len(useTime), 'available:')
        for time in useTime:
            print('{}-{}'.format(format(time[0] + 9, '02'), format(time[1] + 10, '02')))
    if i != roomCnt - 1:
        print('-----')
```



## 8단 변속기

```python
import sys

data = list(map(int, input().split()))

upCnt = 0
downCnt = 0
sameCnt = 0

for i in range(7):
    if (data[i] < data[i+1]):
        upCnt += 1 
    elif (data[i] > data[i+1]):
        downCnt += 1
    else:
        sameCnt += 1

if (upCnt == 7):
    print('ascending')
elif (downCnt == 7):
    print('descending')
else:
    print('mixed')
```







## 지도 자동 구축

~~~python
import sys
# 수열 문제

n = int(input())

result = (2**n) +1
print(result**2)
~~~



## 장애물 인식 프로그램

```python
import sys

# 상하좌우 확인
def find(x,y):
    #사용할 전역변수
    global cnt

    if(x<=-1 or x>=n or y<=-1 or y>=n):
        return False
    
    if (graph[x][y] == 1):
        graph[x][y] = 0 #중복확인 막기 위해

        cnt += 1

        #재귀함수로 반복작업
        find(x-1,y)
        find(x+1,y)
        find(x,y-1)
        find(x,y+1)

        return True


n = int(input())

graph = []
cnt = 0

for i in range(n):
    graph.append(list(map(int, input())))

totBolcks = 0
sepBolcks = []


for x in range(n):
    for y in range(n):
        if (find(x,y) == True):
            totBolcks += 1
            sepBolcks.append(cnt)
            cnt = 0
    

print(totBolcks)
sepBolcks.sort()
for num in sepBolcks:
    print(num)
```



## 금고털이

```python
import sys
# 배낭무게, 금속종류
# 금속무게, 금속가격

w, n = map(int, input().split())
data = []
for i in range(n):
    # data.append(list(map(int, input().split())))
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(reverse=True, key=lambda x: x[1])
cost = 0
i=0;
while (w>0):
    if (w > data[i][0]):
        w -= data[i][0]
        cost += (data[i][0]*data[i][1])
        i += 1
    else:
        cost += (w*data[i][1])
        break

print(cost)
```



## 바이러스

```python
import sys

k, p, n = map(int, input().split())

# print(k, p, n)

for i in range(n):
    k = k*p%1000000007

print(k)
```



## GBC

```python
import sys

n, m = map(int, input().split())

# print(n, m)

standard = []
realValue = []
result = []



for i in range(n):
    x, y = map(int, input().split())

    for j in range(x):
        standard.append(y)

for i in range(m):
    xx, yy = map(int, input().split())

    for j in range(xx):
        realValue.append(yy)


result = []
for i in range(100):
    result.append(realValue[i] - standard[i])

print(max(result))

```



## [21년 재직자 대회 예선] 비밀 메뉴

```python
## While문
import sys

m, n, k = sys.stdin.readline().split()

# print(m, n, k)

secretMunu = list(map(str, sys.stdin.readline().split()))
userSqe = list(map(str, input().split()))

secretMunu=''.join(secretMunu)
userSqe=''.join(userSqe)
i=0
sol = 0
while (i < (len(userSqe)+len(secretMunu))):
    if(secretMunu == userSqe[i:(i+len(secretMunu))]):
        sol += 1
        break
    else:
        i += 1

if(sol == 1):
    print('secret')
else:
    print('normal')

    
## For문
import sys

m, n, k = map(int, input().split())
# print(m,n,k)

seq = list(map(str, input().split())) #순서
# print(seq)
seq=''.join(seq) #145
# print(seq)

inputValues = list(map(str, input().split()))
inputValues = ''.join(inputValues)

cnt = 0 #10 -3 +1
# if seq in inputValues:
#     cnt += 1
for i in range(n-m+1):
    if(inputValues[i:i+m] == seq):
        
        cnt += 1
    # print(inputValues[i:i+m] , seq)

if cnt != 0:
    print('secret')
else:
    print('normal')

```

