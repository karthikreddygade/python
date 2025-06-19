import random

alphabets = ['a' ,'b' ,'c' ,'d', 'e', 'f', 'g', 'h' ,'i' , 'j', 'k','l' , 'm' , 'n', 'o', 'p' ,'q' ,'r', 's', 't' ,'u' ,'v' ,'w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0','1','2','3','4','5' ,'6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']
#password = ''
a = int(input("enter the no.of alphabets\n"))
n = int(input(f"enter the no.of numbers\n"))
s = int(input(f"enter the no.of symbols\n"))
#simple form
'''for i in range (0, a):
    passwords += random.choice(alphabets)
for i in range (0, n):
    passwords += random.choice(number)

for i in range (0, s):
    passwords += random.choice(symbols)
print(passwords)
'''
#hard form
passwords = []
for i in range (0, a):
    passwords += random.choice(alphabets)
for i in range (0, n):
    passwords += random.choice(number)

for i in range (0, s):
    passwords += random.choice(symbols)

random.shuffle(passwords)
#print(passwords)
password = ''
for char in passwords:
    password += char
print(f"Password is:{password}")
