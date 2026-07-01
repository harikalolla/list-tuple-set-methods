Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a =(4,8.9,"Code",True,5+2j)
>>> print(a)
(4, 8.9, 'Code', True, (5+2j))
>>> type(a)
<class 'tuple'>
>>> a.count(5+2j)
1
>>> a.index(True)
3
>>> a.len()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.len()
AttributeError: 'tuple' object has no attribute 'len'
>>> len(a)
5
