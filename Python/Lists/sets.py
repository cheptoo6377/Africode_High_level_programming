# import sys
# import timeit
# tup = ('rop','joseph','michael','kipngeno','rop') 
# lst = ['rop','joseph','michael','kipngeno','rop'] 
# tup = tuple(lst)
# print(sys.getsizeof(tup))
# print(sys.getsizeof(lst))

# print(timeit.timeit(stmt="tup = ('rop','joseph','michael','kipngeno','rop') * 100", number=100)) 
# print(timeit.timeit(stmt="lst = ['rop','joseph','michael','kipngeno','rop']"
# " * 100", number=100)) 
# print(tup)
#access items in a tuple
# tup.

#methods available in tuples
# tup.index('rop')
# print(dir(tup))
# print(dir(tup))
# print(tup.index('rop'))
# print(tup.count('rop'))
# print(len(tup))
# print('ben' in tup)
# print('rop' in tup)
# print(sys.getsizeof(tup))
#sets
myset = {'rop','joseph','michael','kipngeno','rop' ,'michael'
 }
another_set = {'Enock','ben','joan',}
# combine = myset.union(another_set)
# myset.add('joan')
# myset.remove('joseph')
# print(myset)
print(myset.isdisjoint(another_set))
print(myset.issubset(another_set))
print(myset.issuperset(another_set))