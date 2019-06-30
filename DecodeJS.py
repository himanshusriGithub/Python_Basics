"""
Developer:Himanshu
Version:0.1
Date:29/06/19
Description: Decode the given Matrix Script
Problem Statement: https://www.hackerrank.com/challenges/matrix-script/problem
 """
# re is Regular Expression,in which it import the library re from regular expression.

import re


# p is row number and q is column number where p,q takes input from user.

print("Enter number of row and column  and then enter values in next line ")
p, q = map(int, input().split())

# In this interpreter reads all values from columnwise and arrange the value in  rowwise.
#  'va' is reading values from given range of row and then arranges values
#  through 'zip'.join is used to join all values of 'va'.

result=''.join([''.join(va) for va in zip(*[input() for va in range(p)])])

# 're' is regular expression which imported from re.
# '\b' is start boundary
# ^a-zA-Z0-9 means that it will takes only starting value a-zA-Z0-9
# and if value except these then it will print whitespace.

print(re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', result))