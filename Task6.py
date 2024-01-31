import random 

done = False
while not done: 
  u = random.randint(1,5)
  c += u
  if c == 12: 
    done = True
    print("0")
  else: 
    done = True
    spill = c - 12
    print(spill) 
