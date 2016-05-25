
# coding: utf-8

# ## MAP function

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]

print(list(map(lambda x, y: x*y, list1, list2)))

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]
list3 = [1,  0,  1,  0,  1]

a = map(lambda x, y, z: x*y*z, list1, list2, list3)
print (type(a))
print (list(a))

list3 = [1,  0,  1,  0,  1]
list4 = [1,  2,  3,  1, -1,  5]

print(list(map(lambda a, b: a + b, list3, list4)))

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 0}

print (dict1)
print (dict2)
print (list(map(lambda a, b: a + b, dict1, dict2)))
print (list(map(lambda a, b: a * b, dict1, dict2)))

dict3 = {3: 1, 1: 2}
dict4 = {'a': 1, 'b': 2}

print(list(map(lambda a, b: a + b, dict3, dict4)))

dict3 = {3: 1, 1: 2}
dict5 = {5: 1, 7: 2}

print (dict3)
print (dict5)
result = map(lambda a, b: a + b, dict3, dict5)
print (list(result))
print (type(result))

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 3, 'c': 0}

print (dict1)
print (dict2)
print (list(map(lambda a, b: a * b, dict1.values(), dict2.values())))

str1 = "abcd"
str2 = "thus"

print (list(map(lambda a, b: a + b, str1, str2)))

tuple1 = ((2, 'a'), (1, 'b'))
tuple2 = ((3, 's'), (0, 'f'))

print (list(map(lambda a, b: a + b, tuple1, tuple2)))
print (list(map(lambda a, b: a * b, tuple1, tuple2)))

set1 = set([2, 1, 4, 0])
set2 = set([4, 1, 6, 3])

print (set1)
print (set2)
print (list(map(lambda a, b: a * b, set1, set2)))

set3 = set('hello')
set4 = set('cake')

print (set3)
print (set4)
print (list(map(lambda a, b: a + b, set3, set4)))

# ## ZIP function

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]

for x, y in zip(list1, list2):
    print (x*y)

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]

print ([x*y for x, y in zip(list1, list2)])

list1 = [2,  2,  3, 10,  1]
list2 = [1, -1,  5,  4, -6]
list3 = [1,  0,  1,  0,  1]

a = [x*y*z for x, y, z in zip(list1, list2, list3)]
print (type(a))
print (list(a))

list3 = [1,  0,  1,  0,  1]
list4 = [1,  2,  3,  1, -1,  5, 6]

print ([x*y for x, y in zip(list3, list4)])

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 0}

print (dict1)
print (dict2)
print ([a + b for a, b in zip(dict1, dict2)])
print ([a * b for a, b in zip(dict1, dict2)])

dict3 = {3: 1, 1: 2}
dict4 = {'a': 1, 'b': 2}

print ([a + b for a, b in zip(dict3, dict4)])

dict3 = {3: 1, 1: 2}
dict5 = {5: 1, 7: 2}

print (dict3)
print (dict5)
result = [a + b for a, b in zip(dict3, dict5)]
print (result)
print (type(result))

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 3, 'c': 0}

print (dict1)
print (dict2)
print ([a * b for a, b in zip(dict1.values(), dict2.values())])

str1 = "abcd"
str2 = "thus"

print ([a + b for a, b in zip(str1, str2)])

tuple1 = ((2, 'a'), (1, 'b'))
tuple2 = ((3, 's'), (0, 'f'))

print ([a + b for a, b in zip(tuple1, tuple2)])
print ([a * b for a, b in zip(tuple1, tuple2)])

set1 = set([2, 1, 4, 0])
set2 = set([4, 1, 6, 3, 9])

print (set1)
print (set2)
print ([a * b for a, b in zip(set1, set2)])

set3 = set('hello')
set4 = set('cake')

print (set3)
print (set4)
print ([a + b for a, b in zip(set3, set4)])



