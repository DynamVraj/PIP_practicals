'''
    20CS059
    VRAJ PATEL
'''
n = int(input())
list = {}
for i in range(n):
    a = input()
    if a in list:
        list[a]+=1
    else:
        list[a] = 1
print(len(list))
for i in list:
    print(list[i], end=" ")