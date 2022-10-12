from random import randint
numele=['Ana','Maria','Ion','Mihai','Alex']
print('Introdu numele elevului',numele)
x=input('introdu numele cautat')

def cautare():
    if x in numele:
        return True
    if x not in numele:
        return False
print('numele este in lista',cautare())