import sys
import io

_INPUT = """\
    A91278C
"""

sys.stdin = io.StringIO(_INPUT)
# ------------------------------------------------
import re
input = sys.stdin.readline

n= input().split()

content=n[0]
pattern='[A-Z]\d{6}[A-Z]'
p=re.compile(pattern)
result = p.fullmatch(content)

if(result!=None):
    num=content[1:len(content)-1]
    if((int(num) >= 100000)&(int(num) <= 999999)):
        print("Yes")
    else:
        print("No")
else:
    print("No")

