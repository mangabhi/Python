#Description : Please write a program which count and print the numbers of each character in a string input by console.

dic = {}
s=input()
for s in s:
    dic[s] = dic.get(s,0)+1
print ('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
