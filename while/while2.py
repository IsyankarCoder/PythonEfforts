import random


x=1
while(x<10):
    print(x)
    x=x+1


listitem2 = [1,2,3,5,6,8,9,10,12,12,245,55]
t=1;
while(6 in listitem2):
    print("6 sayisi" ,t," kez hala sistemd")
    listitem2.pop()
    print(listitem2)
    t=t+1


for sayilar in list(range(0,30,5)) :
     print(sayilar)
    
print(random.random())
print(random.randint(1,500))

#from NumPy.random import randint
#for tamsayilar in randint(0,10,20): 
#     print(tamsayilar)





