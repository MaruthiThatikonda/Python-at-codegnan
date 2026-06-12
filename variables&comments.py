Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1,num2,num3=10,20,30
print(num1)
10
print(num2)
20
print(num3)
30
num1= num2 = num3=10
print(num1)
10
>>> print(num2,num3)
10 10
>>> print(id(num1))
140731358241992
>>> print(id(num2,num3))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(id(num2,num3))
TypeError: id() takes exactly one argument (2 given)
>>> print(id(num2))
140731358241992
>>> a,b=10,20
>>> print(id(a),id(b))
140731358241992 140731358242312
>>> a,b=256,256
>>> print(id(a),id(b))
140731358249864 140731358249864
>>> a,b=259,258
>>> print(id(a),id(b))
2495894167024 2495894166960
>>> #swap of values
>>> a=10,b=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=10,b=20
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a,b=10,20
>>> print(id(a),id(b))
140731358241992 140731358242312
>>> a,b=b,a
>>> print(id(a),id(b))
140731358242312 140731358241992
>>> print(a,b)
20 10
>>> a,b=5,10
>>> a,b=b,a
>>> print(a,b)
10 5
