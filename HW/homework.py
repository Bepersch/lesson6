import re


s = "  Lorem Ipsum dolor sit amet  "

_ping = """number of bytes=32 time=46 ms TTL=54 
number of bytes=32 time=54 ms TTL=54 
number of bytes=32 time=52 ms TTL=54 
number of bytes=32 time=48 ms TTL=54"""


def task1_1(a):
    c = re.compile(r'\b([aeyuio]\w*)', flags=re.IGNORECASE)
    return c.findall(a)


def task1_2(a):
    c = re.compile(r'\b([qwrtpsdfghjklzxcvbnm]\w*)', flags=re.IGNORECASE)
    return c.findall(a)


def task2(a):
    c1 = re.compile(r'(\bnumber of bytes=\d+)')
    c2 = re.compile(r'(\btime=\d+ ms)')
    c3 = re.compile(r'(\bTTL=\d+)')
    return c1.findall(a), c2.findall(a), c3.findall(a)


print(task1_1(s))
print(task1_2(s))
print(task2(_ping))