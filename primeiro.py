Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count_digits(1234567890)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    count_digits(1234567890)
NameError: name 'count_digits' is not defined
>>> count_digit(123)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    count_digit(123)
NameError: name 'count_digit' is not defined
>>> count_digits(12345)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    count_digits(12345)
NameError: name 'count_digits' is not defined
>>> x = "hello"
>>> print(x.upper())
HELLO
>>> f = x.upper()
>>> print(f())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(f())
TypeError: 'str' object is not callable
>>> f()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    f()
TypeError: 'str' object is not callable
>>> f
'HELLO'
>>> istrcmp('python', 'Python')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    istrcmp('python', 'Python')
NameError: name 'istrcmp' is not defined
>>> print(x)
hello
>>> istrcmp('a', 'b')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    istrcmp('a', 'b')
NameError: name 'istrcmp' is not defined
>>> istrcmp('python', 'Python')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    istrcmp('python', 'Python')
NameError: name 'istrcmp' is not defined
>>> 2<3
True
>>> 2>3
False
>>> x=5
>>> 2<x>10
False
>>> 2<x<10
True
>>> 2<3<4<5<6
True
>>> 'python'>'perl'
True
>>> 'python'<'perl'
False
>>> 'Python'>'Java'
True
>>> 'Python'=='python'
False
>>> 'Python'!='python'
True
>>> a=true
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a = True
>>> b = False
>>> a and b
False
>>> a or b
True
>>> not a
False
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> False or False
False
>>> not False
True
>>> 
>>> not True
False
>>> 2<3 and 5>4
True
>>> 2<3 or 5>4
True
>>> 2<3 and 5<4
False
>>> print(2<3 and 3>1)
True
>>> print(2<3 or 3>1)
True
>>> print(2>3 or not 3>1)
False
>>> print(2>3 and not 3>1)
False
>>> x=4
>>> y=5
>>> p=x<y or x>z
>>> print(p)
True
>>> 
>>> 
>>> *963,,,3698/
SyntaxError: invalid syntax
>>> x=42
>>> if x%2==0:print('Even')

Even
>>> x=3
>>> if x%2==0:
	print('even')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> x=3
>>> if x%2==0:
	print('even')
    else
    
SyntaxError: unindent does not match any outer indentation level
>>> x=3
>>> if x%2==0:
	print('even')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> x=3
>>> if x%2==0:
	print('even')
	else:
		
SyntaxError: invalid syntax
>>> x=3
>>> if x%2==0: print('even')
else: print('odd')

odd
>>> x=42
>>> if x<10:print('one digit number')
elif x<100:print('two digit number')
else: print(big number)
SyntaxError: invalid syntax
>>> x=42
>>> if x<10:print('one digit number')
elif x<100:print('two digits number')
else: print('big number')

two digits number
>>> x=2
>>> if x==2:print(x)
else:print(y)

2
>>> x=2
>>> if x==2:print(x)
else: x+
SyntaxError: invalid syntax
>>> x=[1,2,3]
>>> len(x)
3
>>> x[1]
2
>>> x[0]
1
>>> x[2]
3
>>> x[1]=4
>>> x[1]
4
>>> x[0]
1
>>> x[1]
4
>>> x[2]
3
>>> import time
>>> time.asctime()
'Sun May  9 15:36:03 2021'
>>> import sys
>>> print(sys.argv[1])
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    print(sys.argv[1])
IndexError: list index out of range
>>> print(sys.argv[0])

>>> 