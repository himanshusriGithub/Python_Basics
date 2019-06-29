"""
Developer:
Version:0.1
Date:
Description: what it does in details

 """
# Why import
import re
# Input ...details
p, q = map(int, input().split())

result=''.join([''.join(va) for va in zip(*[input() for va in range(p)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', result))