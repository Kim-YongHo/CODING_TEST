
if __name__ == '__main__':

  n, m, k = map(int, input().split())
  data = list(map(int, input().split()))

  data.sort(reverse = True)
  first = data[0]
  second = data[1]

  s_count = m//(k+1) ##최대값 횟수 일부, 2번째 값 횟수
  f_count = (s_count)*k + m%(k+1)

  total = (s_count*second) + (f_count*first)

  print(total)