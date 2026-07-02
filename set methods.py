Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set
#set
a ={5,8.9,"hari",True}
print(a)
{8.9, True, 5, 'hari'}
type(a)
<class 'set'>
#subset
a ={3,4,5,6}
b ={4,5}
b.issubset(a)
True
a.issubset(b)
False
#superset
a ={22,45,67,89}
b={89,67,45}
a.issuperset(b)
True
b.issuperset(a)
False
#union
a ={3,4,5,6,7,8}
b ={1,2,3,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
c ={5,8,9,9,8,6,5}
print(c)
{8, 9, 5, 6}
#intersection
a ={3,4,5,6,7}
b={4,8,6,7}
a.intersection(b)
{4, 6, 7}
#update
a ={ 1,2,3,4,5}
b ={4,5,6,7}
a
{1, 2, 3, 4, 5}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7}
b
{4, 5, 6, 7}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7}
#difference
a ={ 4,5,6,7,8}
b ={8,9,7,2,0,11}
a.difference(b)
{4, 5, 6}
b.difference(a)
{0, 9, 2, 11}
#symmetric
a ={3,4,5,6,7}
b ={1,2,3,4,8}
a.symmetric_difference(b)
{1, 2, 5, 6, 7, 8}
#intersection update
a ={1,2,3,4,5}
b ={8,9,7,5}
a.intersection_update(b)
a
{5}
b ={6,7,8,9,0}
b.intersection_update(a)
b
set()
a ={5,6,7}
b ={6,7,8,9}
a.difference_update(b)
a
{5}
b.difference_update(a)
a
{5}
b
{8, 9, 6, 7}
#symmetric update
a ={1 ,2,3}
b ={2,3,4,5}
a.symmetric_differences_update(b)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.symmetric_differences_update(b)
AttributeError: 'set' object has no attribute 'symmetric_differences_update'. Did you mean: 'symmetric_difference_update'?
a.symmetric_difference_update(b)
a
{1, 4, 5}
#pop
a ={4,5,6}
a.pop()
4
a.remove(6)
a
{5}
>>> #discard
>>> a ={1,2,4}
>>> a.discard()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.discard()
TypeError: set.discard() takes exactly one argument (0 given)
>>> a.discard(4)
>>> 
>>> a
{1, 2}
>>> #copy
>>> a.copy()
{1, 2}
>>> a.clear()
>>> a
set()
>>> b.add(2)
>>> b
{2, 3, 4, 5}
>>> a ={3,5,6}
>>> len(a)
3
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.count()
AttributeError: 'set' object has no attribute 'count'
>>> a.inex()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.inex()
AttributeError: 'set' object has no attribute 'inex'
>>> a ={3,4,5,6}
>>> b ={8,9,10,11}
>>> a.isdisjoint(b)
True
>>> a
{3, 4, 5, 6}
