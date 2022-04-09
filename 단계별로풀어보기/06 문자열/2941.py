word = input()
wordset = ['c=','c-','dz=','d-','lj','nj','s=','z=']
print(len(word)-sum(map(word.count, wordset)))