# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:10:42 2023

@author: arangela

https://docs.python.org/es/3.12/tutorial/introduction.html

"""

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

2 + 2
#Out[5]: 4

50 - 5*6
#Out[6]: 20

(50 - 5*6) / 4
#Out[7]: 5.0

8 / 5  # division always returns a floating point number
#Out[8]: 1.6

17 / 3  # classic division returns a float
#Out[9]: 5.666666666666667

17 // 3  # floor division discards the fractional part
#Out[10]: 5

17 // 3  # floor division discards the fractional part
#Out[11]: 5

17 % 3  # the % operator returns the remainder of the division
#Out[12]: 2

5 * 3 + 2  # floored quotient * divisor + remainder
#Out[13]: 17

5 ** 2  # 5 squared
#Out[14]: 25

2 ** 7  # 2 to the power of 7
#Out[15]: 128

width = 20
height = 5 * 9
width * height
#Out[16]: 900

spam
#Out[19]: 1

4 * 3.75 - 1
#Out[20]: 14.0

tax = 12.5 / 100
price = 100.50
price * tax
#Out[21]: 12.5625

#price + _
#Out[22]: 113.0625

#round(_, 2)
#Out[23]: 113.06

'spam eggs'  # single quotes
'spam eggs'
"Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
'1975'  

'doesn\'t'  # use \' to escape the single quote...
"doesn't"
"doesn't"  # ...or use double quotes instead
"doesn't"
'"Yes," they said.'
'"Yes," they said.'
"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string
#Out[37]: 'First line.\nSecond line.'

print(s)  # with print(), special characters are interpreted, so \n produces new line
#First line.
#Second line.

print('C:\some\name')
#C:\some
#ame

print(r'C:\some\name')  # note the r before the quote
#C:\some\name

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
#Usage: thingy [OPTIONS]
#     -h                        Display this usage message
#     -H hostname               Hostname to connect to

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
#Out[42]: 'unununium'

'Py' 'thon'
#Out[43]: 'Python'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text
'Put several strings within parentheses to have them joined together.'

squares = [1, 4, 9, 16, 25]
squares

squares[0]  # indexing returns the item

squares[-1]

squares[-3:]  # slicing returns a new list

squares[:]

squares + [36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]  # something's wrong here

4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value

cubes

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters

letters[2:5] = ['C', 'D', 'E']
letters

letters[:] = []
letters

letters = ['a', 'b', 'c', 'd']
len(letters)


















