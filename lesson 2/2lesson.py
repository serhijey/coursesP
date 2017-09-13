d = {1:0}
print(d[1])

print(5 and 1.5 and [] and {} and '')

l = [1]
print(l[0])

w = [1, 6, 66, [4, {'r':['abc', True]}, 0.0]]

print(w[3][1]['r'][0][1])

print(3 ^ 7) #4
print(1 ^ 2) #3
print(2 ^ 4) #6
print(4 ^ 8) #12
'''
0  000
1  001
2  010
3  011
4  100
5  101
6  110
7  111
'''

print(range(5))
#print(xrange(5))

print(list(range(5)))

print('\n\r')
print('asd')

print(list(range(1, 5, 2)))

print('===================================================')
#LOOPs
'''n = 5
while n > 0:
    print(n)
    n -= 1'''

'''a = 0
b = 5
c = 1
while a < b:
    print(a, end=' ')
    a += c'''

'''l = range(5)
a = 0
b = 5
while a < b:
    print(l[a]**2, end=' ')
    a += 1'''


for i in range(5):
    print(i)



l2 = []
for i in range(7):
    l2.append(i**2)
print(l2)

l2 = []
for i in range(7):
    for j in range(4):
        l2.append(i**2)
print(l2)

a = 5
n = 1
print('#{x} value: {y}'.format(x=n, y=a))

#HW: вывести таблицу умножения используя метод - формат (два цыкла for)
# 1234
# 0123
# 0012
# 0001




















    

