Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+2
3
2-1
1
2*3
6
4/2
2.0
4//2
2
5%2
1
print("Hello")
Hello
1+2
3
2**3
8
4/2
2.0
4//2
2
5%9
5
print('marian\'s session "3 & 4"')
marian's session "3 & 4"
print("Marian"*5)
MarianMarianMarianMarianMarian
print("Marian1/nmarian2")
Marian1/nmarian2
print("Marian1//nmarian2")
Marian1//nmarian2
print("marian1"/n"marian2")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Marian1\nmarian2")

Marian1
marian2
print(r"marian1\nmarian2")
marian1\nmarian2



















































c = 'Marian'
c
'Marian'
c[0]
'M'
c[-1]
'n'
c[-1+0]
'n'

c[-2]
'a'
len()
KeyboardInterrupt
len(c)
6
c[7]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c[7]
IndexError: string index out of range
len(c)
6
c[0:2]
'Ma'
c[-1:4]
''
c[-1:2]
''
c[2:-1]
'ria'
c[-1:2:-1]
'nai'
c[0:2]
'Ma'
c[:]
'Marian'
c[:4] + c[:5]
'MariMaria'
c[1:4]
'ari'

c[2:]
'rian'
c[:5]
'Maria'
c[2:10]
'rian'
c[:]
'Marian'
c[::-1]
'nairaM'
c[-1:5:-1]
''
c[5:1:-1]
'nair'
a=1
b=5
a.b
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.b
AttributeError: 'int' object has no attribute 'b'
a>b
False
i = [5,6,7,7,8]
i
[5, 6, 7, 7, 8]
i[0]
5
i[1]
6
i[-1]
8
s = ["a","bc","cde"]
s[2][2]
'e'
c = [6.1,'TVM']
d = [8,6,7,1]
f = [c,d]
f
[[6.1, 'TVM'], [8, 6, 7, 1]]
[[6.1, 'TVM'], [8, 6, 7, 1]]
[[6.1, 'TVM'], [8, 6, 7, 1]]
n = [1,2,3,4,5]
n.append(10)
n
[1, 2, 3, 4, 5, 10]
n.insert(2,10)
n
[1, 2, 10, 3, 4, 5, 10]
n.remove(10)
n
[1, 2, 3, 4, 5, 10]
[1, 2, 3, 4, 5, 10]
[1, 2, 3, 4, 5, 10]

n.append(5)
n
[1, 2, 3, 4, 5, 10, 5]
del n(5)
SyntaxError: cannot delete function call
del n[5]
n
[1, 2, 3, 4, 5, 5]
del n[3:]
n
[1, 2, 3]
n.pop(1)
2
n
[1, 3]
n.pop()
3
n
[1]
n.append([1,2,3,4,5])
n
[1, [1, 2, 3, 4, 5]]
n.pop()
[1, 2, 3, 4, 5]
n.extend([1,2,3,4,5,])
n
[1, 1, 2, 3, 4, 5]
del n[0]
n
[1, 2, 3, 4, 5]
n = [2,1,4,3]
nm
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    nm
NameError: name 'nm' is not defined. Did you mean: 'n'?
n
[2, 1, 4, 3]
min(n)
1
max(n)
4
sum(n)
10
sort(n)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    sort(n)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
n.sort()
n
[1, 2, 3, 4]
n.sort(reverse=True)
n[::-1]
[1, 2, 3, 4]
str = ['Tech','Tvm','MARIAN']
min(str)
'MARIAN'
max(str)
'Tvm'
sum(str)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    sum(str)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
str.sort()
str
['MARIAN', 'Tech', 'Tvm']
com = [2,'b','a',1]
min(com)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    min(com)
TypeError: '<' not supported between instances of 'str' and 'int'
max(com)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    max(com)
TypeError: '>' not supported between instances of 'str' and 'int'
sum(com)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    sum(com)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
com.sort()
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    com.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
l = ['a','A','Z','z']
l.sort()
l
['A', 'Z', 'a', 'z']
l = ['1a','2A','0z']
l.sort()
l'
SyntaxError: unterminated string literal (detected at line 1)
l
['0z', '1a', '2A']
min(l)
'0z'
max(l)
'2A'
sum(l)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    sum(l)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
t = (0,2,1,3)
t.append(2)'
SyntaxError: unterminated string literal (detected at line 1)
t.append(2)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    t.append(2)
AttributeError: 'tuple' object has no attribute 'append'
t.sort()
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
max(t)
3
t[2]
1
t[3]
3
min(t)
0
max(t)
3
t= ('a','A','b','B')
t.(0,1,2,1,3,1)
SyntaxError: invalid syntax
t = (0,1,2,1,3,1)
t.count(1)
3
t = ('a',1)
t
('a', 1)
\
t = ('a',1,'b',1)
t.count(1)
2
t.count('a')
1
t.count(a)
2
s = {4,2,1,3,1,3}
s
{1, 2, 3, 4}
s
{1, 2, 3, 4}
s={0,2,1,3}
s
{0, 1, 2, 3}
min(s)
0
max(s)
3
s.sort()
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    s.sort()
AttributeError: 'set' object has no attribute 'sort'
sum(s)
6
s[2]
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
s.add(5)
s
{0, 1, 2, 3, 5}
s.remove(2)
s
{0, 1, 3, 5}
s
s.pop()
0
s.pop()
1
s = {'a','A','b','B'}
min(s)
'A'
max(s)
'b'
count(s)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    count(s)
NameError: name 'count' is not defined. Did you mean: 'round'?
s.sort()
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    s.sort()
AttributeError: 'set' object has no attribute 'sort'
s.sum()
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    s.sum()
AttributeError: 'set' object has no attribute 'sum'
sum(s)
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    sum(s)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
s.append('c')
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    s.append('c')
AttributeError: 'set' object has no attribute 'append'
s
{'a', 'B', 'A', 'b'}
range(5)
range(0, 5)
print(range(5))
range(0, 5)
list(range(5))
[0, 1, 2, 3, 4]
set(range(5))
{0, 1, 2, 3, 4}
a = set(range(5))
a[2]
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    a[2]
TypeError: 'set' object is not subscriptable
list(range(2,5))
[2, 3, 4]
list(range(0,10,3))
[0, 3, 6, 9]
list(range(0,12,3))
[0, 3, 6, 9]
a=0
b=13
c = 3
list(range(a,b,c))
[0, 3, 6, 9, 12]
range()
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    range()
TypeError: range expected at least 1 argument, got 0
type(range(5))
<class 'range'>
a = 2
list(range(2,15,a))
[2, 4, 6, 8, 10, 12, 14]
a = 3
list(range(2,15,a))
[2, 5, 8, 11, 14]
 a = list[range(1,10,2)]
...  
SyntaxError: unexpected indent
>>> a = list[range(1,10,2)]
>>> b = list[range(10,20,2)]
>>> l = [a,b]
>>> l
[list[range(1, 10, 2)], list[range(10, 20, 2)]]
>>> [list[range(1, 10, 2)], list[range(10, 20, 2)]]
[list[range(1, 10, 2)], list[range(10, 20, 2)]]
>>> r = []
>>> r.append(a,b)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    r.append(a,b)
TypeError: list.append() takes exactly one argument (2 given)
>>>  l
...  
SyntaxError: unexpected indent
>>> l
[list[range(1, 10, 2)], list[range(10, 20, 2)]]
>>> list(range(a,a*a*a*a,a+1))
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    list(range(a,a*a*a*a,a+1))
TypeError: unsupported operand type(s) for *: 'types.GenericAlias' and 'types.GenericAlias'
>>> list(range(a,a*a*a*a,a+1))
... 
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    list(range(a,a*a*a*a,a+1))
TypeError: unsupported operand type(s) for *: 'types.GenericAlias' and 'types.GenericAlias'
>>> a = 2
>>> list(range(a,a*a*a*a,a+1))
... 
[2, 5, 8, 11, 14]
>>> a = list(range(1,10,2))
>>> b = list(range(10,20,2))
... 
>>> c = [a,b]
>>> c
[[1, 3, 5, 7, 9], [10, 12, 14, 16, 18]]
>>> k = {1:'a',2:'a',2:1}
>>> k[2]
1
>>> x,y = 1,2
>>> x
1
>>> y
2
