## H-Index

- https://programmers.co.kr/learn/courses/30/lessons/42746

~~~python
def solution(citations):
    
    l = len(citations)
    citations.sort() # 정렬후 해당 인덱스 
    
    for i in range(l):
        if citations[i]>=(l-i): #길이보다 크면 통과
            return l-i
    
    return 0
    
~~~



