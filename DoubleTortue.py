Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> Jacque = turtle.Pen()
>>> René = turtle.Pen()
>>> Jacque.forward(50)
>>> René.left(90)
>>> René.forward(50)
>>> Jacque.left(90)
>>> Jacque.forward(50)
>>> René.rigth(90)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    René.rigth(90)
AttributeError: 'Turtle' object has no attribute 'rigth'
>>> René.right(90)
>>> René.forward(25)
>>> Jacque.left(90)
>>> Jacque.forward(25)
>>> up
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    up
NameError: name 'up' is not defined
>>> turtle.up
<function up at 0x000002747FA97AF0>

>>> 