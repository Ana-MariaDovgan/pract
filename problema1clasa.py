from random import randint

numar=int(input('Introduceti numarul'))
numar -=1
max=randint(1,20)
while numar>0: 
    x=randint(1,20)
    if x>max:
        max=x
    numar -=1
print('Cea mai mare valoare este',max)
