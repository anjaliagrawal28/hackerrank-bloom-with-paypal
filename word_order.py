n = int(input())
counter = {}
words = []

for i in range(n):
  wd = input()
  words.append(wd)
  if wd in counter:
    counter[wd] += 1
  else:
    counter[wd] = 1
    
print(len(counter))
print(' '.join([str(counter[wd]) for wd in counter]))
