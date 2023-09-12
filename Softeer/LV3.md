## 성적 평균

```python
import sys

n, k = map(int, sys.stdin.readline().split())

score = list(map(int, sys.stdin.readline().split()))

# print(n, k)
# print(score)

for i in range(k):
    start, end = map(int, sys.stdin.readline().split())
    avg = sum(score[(start-1):end])/(end-start+1)
    print("%0.2f" %avg )
```



## 슈퍼바이러스

```python
import sys

k, p, n = map(int, input().split())

# print(k, p, n)


result = (k*pow(p, n*10,1000000007)) % 1000000007



print(result)
```



## 징검다리

```python
import sys

n = int(input())

rockHeight = list(map(int, sys.stdin.readline().split()))

# print(n)
# print(rockHeight)

result = [1] * n

for i in range(n):
    for j in range(i):
        if (rockHeight[i] > rockHeight[j]): # 인덱스 i>j and i의 높이가 더 높아야함 
            result[i] = max(result[i], result[j]+1 ) # +1의 의미는 자기 자신을 밟는 것을 의미

print(max(result))

```



## 택배 마스터 광우

```
import sys
import itertools

## 레일 순서 조작 가능

## 경우의 수 계산
def calCase(case):
    total = 0
    currentWeight = case[0]
    nextWeight = 0
    cnt = 0
    index = 0

    while (cnt<k): ## 실행횟수 K를 만족시키기 위해서

        nextWeight = case[(index+1)%n]

        if((currentWeight + nextWeight) > m): ##현재와 다음 무게를 합쳐 허용 무게 확인
            total += currentWeight
            currentWeight = nextWeight
            cnt += 1
        else:
            currentWeight += nextWeight ## 무게를 더해서 묶어주기
        
        index += 1
    
    return total


## n: 레일 개수
## m: 택배 바구니 허용 무게
## k: 일 실행 횟수

n, m, k = map(int, sys.stdin.readline().split())
# print(n, m ,k)

rails = list(map(int, sys.stdin.readline().split()))
# print(rails)

## 레일 순서 가능 경우 
rasilsCase = list(itertools.permutations(rails, n))
result = []

for caseOne in rasilsCase:
    #함수 호출해서 비교
    result.append(calCase(caseOne))

print(min(result))
```

