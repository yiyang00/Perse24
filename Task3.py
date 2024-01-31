s = input() 

moved = s[0:2]
w = s.replace(moved, '') + moved 
print(w)
