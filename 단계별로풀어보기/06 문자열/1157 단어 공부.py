# s = input()
# S = s.upper()
# wordlist = [0 for i in range(0, 91)]
# for word in S:
#     for abc in range(ord('A'), ord('Z') + 1):
#         if word==chr(abc):
#             wordlist[abc] += 1
#
# if max(wordlist) > 1:
#     print('?')
# else:
#     print('a')
# #

word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[(cnt.index(max(cnt)))].upper())
