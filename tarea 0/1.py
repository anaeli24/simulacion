Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 3*5
15
>>> x=14
>>> y=5
>>> x*y
70
>>> x**y
537824
>>> x/y
2.8
>>> x//y
2
>>> x%y
4
>>> x="hola"
>>> y*x
'holaholaholaholahola'
>>> y
5
>>> x*y
'holaholaholaholahola'
>>> x-y
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> x+y
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x+y
TypeError: can only concatenate str (not "int") to str
>>> x+srt(y)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x+srt(y)
NameError: name 'srt' is not defined
>>> x + str (y)
'hola5'
>>> lista=[1,3,4,2,4,1,"hola"]
>>> lista
[1, 3, 4, 2, 4, 1, 'hola']
>>> lista[0]
1
>>> lista[*3]
SyntaxError: invalid syntax
>>> lista[:3]
[1, 3, 4]
>>> lista[-3:]
[4, 1, 'hola']
>>> lista[1-:1¨]
SyntaxError: invalid syntax
>>> min(lista)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    min(lista)
TypeError: '<' not supported between instances of 'str' and 'int'
>>> min(lista[:-1])
1
>>> lista
[1, 3, 4, 2, 4, 1, 'hola']
>>> max(lista[:-1])
4
>>> len(lista)
7
>>> sorted(lista[:-1])
[1, 1, 2, 3, 4, 4]
>>> import math
>>> math.phi
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    math.phi
AttributeError: module 'math' has no attribute 'phi'
>>> importmath
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    importmath
NameError: name 'importmath' is not defined
>>> import math
>>> math.pi
3.141592653589793
>>> sin(1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    sin(1)
NameError: name 'sin' is not defined
>>> sin(1.0)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sin(1.0)
NameError: name 'sin' is not defined
>>> math.sin(1.0)
0.8414709848078965
>>> from math import sin,cos
>>> math.sin(1.0)
0.8414709848078965
>>> math.cos81.0)
SyntaxError: invalid syntax
>>> math.com(1.0)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    math.com(1.0)
AttributeError: module 'math' has no attribute 'com'
>>> math.cos(1.0)
0.5403023058681398
>>> math.log(1.0)
0.0
>>> log(3.0)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    log(3.0)
NameError: name 'log' is not defined
>>> math.log(3.2)
1.1631508098056809
>>> nombredevariablelarga=13
>>> nombredevariablelarga*2
26
>>> nombredevariablelarga-36
-23
>>> a=12
>>> b=13
>>> elrolloquesea=3.2
>>> elrolloquesea
3.2
>>> nombredevariablelarga*elrolloquesea
41.6
>>> from math import exp
>>> def doble(x):
	    return2*x

	    
>>> doble(3)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    doble(3)
  File "<pyshell#56>", line 2, in doble
    return2*x
NameError: name 'return2' is not defined
>>> def doble(x):
	    return 2*x

	
>>> doble(3)
6
>>> from random import random
>>> random()
0.751368568718999
>>> random()
0.4947217514850921
>>> random(9

random()
       
SyntaxError: invalid syntax
>>> random()
0.9926296101041663
>>> random()
0.07902312114228849
>>> random()
0.06892459469017209
>>> random(9
       random()
       
SyntaxError: invalid syntax
>>> random()
0.514646809468796
>>> muchos=[random() for i in range(2000)]
>>> len(muchos)
2000
>>> muchos

>>> min(muchos)
0.0004326731956950658
>>> max(muchos)
0.9999329988014357
>>> sum(muchos)
990.0808301367495
>>> sum(muchos)/len(muchos)
0.4950404150683747
>>> muchos=random() for i in range(20000)]
SyntaxError: invalid syntax
>>> muchos=[random()for i in range(20000)]
>>> len(muchos)
20000
>>> muchos

,ac
>>> max(muchos)
0.999985581088759
>>> min(muchos)
0.00010388125136240323
>>> sum(muchos)
9976.713398144722
>>> sum(muchos)/len(muchos)
0.4988356699072361
>>> exp(1)
2.718281828459045
>>> muchos=random() for i in range(2000000)]
SyntaxError: invalid syntax
>>> muchos=random() for i in ranfe(200000000)]
SyntaxError: invalid syntax
>>> x=12
>>> y=8
>>> if x <y:
	print'x es menor')
	
SyntaxError: invalid syntax
>>> print('x es menor')
x es menor
>>> else:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> print('x no es menor')
x no es menor
>>> x
12
>>> def menor(x,y):
	if x <y:
		return x
	else_
	return y:
		
SyntaxError: invalid syntax
>>> menor(2,3)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    menor(2,3)
NameError: name 'menor' is not defined
>>> x=12
>>> y=8
>>> if x < y:
	   print('x es menor')
	   else:
		   
SyntaxError: invalid syntax
>>> if x < y:
	    print('x es menor')
	    else:
		    
SyntaxError: invalid syntax
>>>     print('x es menor')
    
SyntaxError: unexpected indent
>>> else:
	
SyntaxError: invalid syntax
>>>     print('x no es menor')
    
SyntaxError: unexpected indent
>>> if x < y:
	print('x es menor')
	    else:
		    
SyntaxError: unexpected indent
>>>    else:
	   
SyntaxError: unexpected indent
>>> else:
	
SyntaxError: invalid syntax
>>> return x
SyntaxError: 'return' outside function
>>> return y
SyntaxError: 'return' outside function
>>> for elemento in lista
SyntaxError: invalid syntax
>>> for elemento (in lista)
SyntaxError: invalid syntax
>>> for elemento in lista:
	print(2**elemento)

	
2
8
16
4
16
2
Traceback (most recent call last):
  File "<pyshell#131>", line 2, in <module>
    print(2**elemento)
TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
>>> ir x < y:
	
SyntaxError: invalid syntax
>>> if x < y:
	print('x es menor)
	      
SyntaxError: EOL while scanning string literal
>>> print('x es menor):
      
SyntaxError: EOL while scanning string literal
>>> x=12
>>> y=8
>>> if x < y:
	    return x
	
SyntaxError: 'return' outside function
>>>    else
   
SyntaxError: unexpected indent
>>> if x < y:
	print('x es menor')
	else:
		
SyntaxError: invalid syntax
>>>    else:
	   
SyntaxError: unexpected indent
>>> print ('x no es menor')
x no es menor
>>> def menor(x,y):
	if x < y:
		return x
	else:
		return y

	
>>> menor(2,3)
2
>>> menor5,7)
SyntaxError: unmatched ')'
>>> menor(5,6)
5
>>> mayor(4,6)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    mayor(4,6)
NameError: name 'mayor' is not defined
>>> 12 < 33
True
>>> 12 > 33
False
>>> 52 < 667
True
>>> lista =[ 1,4,7]
>>> for elemento in lista:
	print(2**elemento)

	
2
16
128
>>> quit()
>>> 