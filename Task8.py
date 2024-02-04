word = input()

for i in range(len(word)): 
  print("+" + "-" + "+")
  print("|" + word[i] + "|")
  if i == len(word) - 1:
    print("+" + "-" + "+")
