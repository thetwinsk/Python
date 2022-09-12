#source: https://www.youtube.com/watch?v=AEE9ecgLgdQ&t=1s
import re

#test_string = '123abc456789abc123ABC'

# pattern = re.compile(r"ABC$")
# matches = pattern.finditer(test_string)

#matches = re.finditer(r"abc", test_string)

# a = r"\tHello"
# print(a)

#match(), search(), findall(), finditer()
# matches = pattern.findall(test_string)
#for match in matches:
    #print(match.span(), match.start(), match.end())
    #print(match) #get actual values

# pattern = re.compile(r"ABC")
# match = pattern.search(test_string)
#match must be at the beginning of the string while search can be work at any position
#print(match)

# test_string = 'hello_123'
#
# pattern = re.compile(r'\d{1,3}')
# matches = pattern.finditer(test_string)
#
# for match in matches:
#     print(match)

dates = """
hello
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
"""

pattern = re.compile(r'\d{4}[-/]0[5-7][-/]\d{2}')
matches = pattern.finditer(dates)

my_string = """
hello world
123
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')
pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z0-9-]+)\.([a-zA-Z]+)') #(com|de|org)
matches = pattern.finditer(my_string)
# for match in matches:
#     #print(match.group(0))
#     print(match.group(1))
#     #print(match.group(2))
#     #print(match.group(3))


#split, sub
# test_string = '123abc456789abc123abc'
# pattern = re.compile(r'123')
# splitted = pattern.split(test_string)
# print(splitted)

# test_string = 'hello world, you are the best world'
# pattern = re.compile(r'world')
# subbed_string = pattern.sub('planet', test_string)
# print(subbed_string)

urls = """
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net
"""
# pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(1))

# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)

#Compilation Flags
my_string = 'Hello World'
pattern = re.compile(r'world', re.I) #IGNORECASE
matches = pattern.finditer(my_string)
for match in matches:
    print(match)


