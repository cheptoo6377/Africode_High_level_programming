#slicing
fruits = ['apple','banana','cherry','dates','fig','grape']
# print(fruits[1:4])
#omitting indice
# print(fruits[:4])
#
#step value
# print(fruits[::2])
#change items
fruits[2 ]= 'maize'
# print(fruits)
fruits[2:3] = ['orange','pineapple']
# print(fruits)
words = ['A','B','F','a','b']
#****sort
words.sort()
# print(words)
# fruits.sort(reverse=True)
# print(fruits)
#*sorted ceates a copy of original list SORT directly sorts the original list
# sorted_fruits = sorted(fruits)
# print(sorted_fruits)
# fruits.reverse()
# print(fruits)
#count

# counts = fruits.count('banana')
# print(counts)
banana_index = fruits.index("cherry")
print(banana_index)