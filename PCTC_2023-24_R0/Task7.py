total = int(input()) 

days = total // 5 + 1
learn = 0 
while True: 
  if days > 0:
    learn += days * 5 
    days = days - 1
  else: 
    learn += total % 5 - 5
    print(learn)
    break 
