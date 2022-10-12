from random import randint
nr=int(input('Introduceti numarul'))
bilealbe,bilenegre=0,0
while nr>0:
    x=randint(1,2)
    if x==1:
        bilealbe +=1
    else:
        bilenegre+=1
    nr -=1
    print('Bile albe au fost extrase',bilealbe)
    print('Bile negre au fost extrase',bilenegre)

