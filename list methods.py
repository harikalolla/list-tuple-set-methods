Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a =[2,5.6,"python",6+3j,True,False]
print(a)
[2, 5.6, 'python', (6+3j), True, False]
type(a)
<class 'list'>
b =2
type(b)
<class 'int'>
c=[3]
type(c)
<class 'list'>
#append
a =["python","c","dsa"]
a.append("c++")
a
['python', 'c', 'dsa', 'c++']
a.append["ml","ai"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append["ml","ai"]
TypeError: 'builtin_function_or_method' object is not subscriptable
#extend
a =["ml","ai"]
a.extend("flask","django")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.extend("flask","django")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["flask","django"])
a
['ml', 'ai', 'flask', 'django']
#insert
a =["tanuku","duvva"]
a.insert(1,"pervali")
a
['tanuku', 'pervali', 'duvva']
#index
a =["pink","black"]
a.index(0)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.index(0)
ValueError: list.index(x): x not in list
a.index("pink")
0
#copy
a.copy()
['pink', 'black']
b =a.copy()
b
['pink', 'black']
#count
b.count("black")
1
#sort
a =["mango","jackfurit","apple","grapes"]
a.sort()
a
['apple', 'grapes', 'jackfurit', 'mango']
b =[3,8,5,2,0,7,9]
b.sort()
>>> b
[0, 2, 3, 5, 7, 8, 9]
>>> #reverse
>>> a =["3,4,7,9,0,7"]
>>> a.reverse()
>>> a
['3,4,7,9,0,7']
>>> b =["html","css"]
>>> b.reverse()
>>> b
['css', 'html']
>>> #pop
>>> a =["c","c++","html","css"]
>>> a.pop()
'css'
>>> a
['c', 'c++', 'html']
>>> a.pop(1)
'c++'
>>> a
['c', 'html']
>>> #remove
>>> a.remove("html")
>>> a
['c']
>>> #len
>>> a =["pooja","priya","sweety"]
>>> len(a)
3
>>> b =["harika"]
>>> len(b)
1
>>> #clear
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
