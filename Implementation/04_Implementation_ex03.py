if __name__ == '__main__':

  data = input()

  column = ord(data[0]) - ord('a') + 1
  raw = int(data[1])
  cnt  = 0

  steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

  for step in steps:
    column_next = column + step[0]
    raw_next = raw + step[1]

    if (column_next >= 1 and column_next <= 8 and raw_next >= 1 and raw_next <= 8):
      cnt += 1

  print(cnt)