
if __name__ == '__main__':

  n = int(input())
  data = list(map(int, input().split()))

  data.sort(reverse=True)
  temp = data[0]
  check = len(data)
  count = 0


  while True:
    if check < 0:
      break
    check -= temp
    temp = data[temp]
    count += 1

  print(count-1)
