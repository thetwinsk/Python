#1. Slicing
#s = '    hello    '
#s = s[:]
#s = s[3:8]

#2. STRIP()
#s = '    hello    '.strip()
s = '####hello####'.strip('#')
#strip() removes white spaces or other special characters
s = ' \n \t hello\n'.strip('\n')
s = 'www.example.com'.strip('cmow.')

#3. LSTRIP() #4. RSTRIP()
#s = '    hello    '.lstrip() #only remove leading white spaces
#s = '    hello    '.rstrip()

#5. #6.
#s = 'Arthur: three!'.lstrip('Arthur: ')
#s = 'Arthur: three!'.removeprefix('Arthur: ')
#s = 'HelloPython'.removesuffix('Python')

#7. REPLACE()
#s = 'string methods in Python'.replace(' ', '-')
s = 'string    methods in Python'
s2 = s.replace(' ', '-')

#8. RE.SUB()
import re
s2 = re.sub('\s+', "-", s)
#print(s2)

#9. SPLIT()
s = 'string methods in Python'.split()
s = 'string methods in Python'.split(',')
s = 'string methods in Python'.split(' ', maxsplit=1)

#10. RSPLIT()
s = 'string methods in Python'.rsplit(' ', maxsplit=1)

#11. JOIN()
list_of_strings = ['string', 'methods', 'in', 'Python']
s = '-'.join(list_of_strings)

#12. UPPER()
s = 'python is awesome!'.upper()

#13. LOWER()
s = 'PYTHON IS AWESOME!'.lower()

#14. CAPITALIZE()
s = 'python is awesome!'.capitalize()
#print(s)

#15. ISLOWER()
# print('PYTHON IS AWESOME!'.islower())
# print('python is awesome!'.islower())

#16. ISUPPER()
# print('PYTHON IS AWESOME!'.isupper())
# print('python is awesome!'.isupper())

#17. ISALPHA() #18. ISNUMERIC() #19. ISALNUM()
s = 'python'
s = '123'
s = 'python123'
s = 'python-123'
#print(s.isalpha(), s.isnumeric(), s.isalnum())

#20. COUNT()
n = 'hello world'.count('o')
#print(n)

#21. FIND()
s = 'Machine Learning'
idx = s.find('a', 2)
# print(idx)
# print(s[idx:])

#23. STARTSWITH() #24. ENDSWITH()
# print('Patrick'.startswith('P'))
# print('Patrick'.endswith('ck'))

#25. PARTITION()
s = 'Python is awesome!'
parts = s.partition('awesome')
#print(parts)

#26. CENTER() #27. LJUST() #28.
#s = s.center(30, '-')
#s = s.ljust(30, '-')
s = s.rjust(30, '-')

#29. f-Strings
num = 1
language = 'Python'
s = f'{language} is the number {num} in Python!'

#30. SWAPCASE()
s = 'HELLO world'
s = s.swapcase()

#31. ZFILL()
s = '42'.zfill(5) #fill zero from the left size
s = '-42'.zfill(5)

print(s)











