import re
import os


os.getcwd()



r1 = re.search(r'ap..e', 'appleQ')
r1

r2 = re.search(r'ap*le', 'apppleQ')
r2

r3 = re.search(r'ap+le', 'appleQ')
r3

r3 = re.search(r'ap+le', 'appleQ')
r3

r4 = re.search(r'a[abp]ple', 'appleQ')
r4

r5 = re.search(r'a[a-z]ple', 'akpleQ')
r5

r6 = re.search(r'a[0-9]ple', 'a9pleQ')
r6


r7 = re.search(r'ap\?le', 'ap?leQ')
r7


r8 = re.search(r'ap{2}le', 'appleQ')
r8

r9 = re.search(r'a\d+le', 'a99leQ')
r9

r10 = re.search(r'^ap', 'Kapple')
r10

r11 = re.search(r'le$', 'appleQ')
r11

r12 = re.search(r'a[^2-5]+le', 'a9pleQ')
r12



r13 = re.search(r'\d+', '-32767')
r13

r14 = re.search(r'09[0-9]{8}', '0908568569999')
r14


r15 = re.search(r'[\w]+@[0-9a-zA-Z\._]+', 'flag@gmail.com//')
r15


r16 = re.search(r'https?://[0-9a-zA-Z\._/]+', 'http://www.flag.com.tw')
r16



m1 = re.match(r'[a-z]+', '123apple456')
m2 = re.match(r'[a-z]+', 'apple456')

print(m2.group())
m2.start()
m2.end()
m2.span()


s1 = re.search(r'[a-z]+', '123456')
s2 = re.search(r'[a-z]+', '123apple456')

s2
print(s2.group())
s2.start()
s2.end()
s2.span()


f1 = re.findall(r'[a-z]+', '123456')
f2 = re.findall(r'[a-z]+', '123apple456book')


f1
f2
print(f2)



s1 = re.sub(r'[a-zA-Z]+', '#English#', '123apple456')
print(s1)




















