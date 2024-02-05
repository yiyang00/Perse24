p1 = input()
p2 = input()
p3 = input()

if p2 != p1 and p3 != p1:
  print("BOTH MISMATCH")
elif p2 != p1 and p3 == p1: 
  print("ENTRY 2 MISMATCH")
elif p3 != p1 and p2 == p1:
  print("ENTRY 3 MISMATCH")
else: 
  print("OK")
