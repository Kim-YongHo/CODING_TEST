if __name__ == '__main__':

  n = int(input())
  data = list(map(str, input().split()))

  w, l = 1, 1
  wd = [-1,1,0,0] # 뒤자리
  ld = [0,0,-1,1] # 앞자리
  direction = ['L','R','U','D']

  for step in data:
    for i in range(len(direction)):
      if step == direction[i]:
        temp_w = w + wd[i]
        temp_l = l + ld[i]
    if temp_w<1 or temp_w>n or temp_l<1 or temp_l>n:
      continue
    w = temp_w
    l = temp_l

  print(l, w)