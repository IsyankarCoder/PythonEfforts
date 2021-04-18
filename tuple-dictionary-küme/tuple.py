tuple2= ("Ankara","Samsun","Corum",98,54.0,12)
print(tuple2[0])
print(tuple2[4])
a,b,c,d,e,f = tuple2
print(a,b,c,d,e,f)
print(d)



#kume
listitem = [1,2,3,3,4]
my_set = set(listitem)
print(type(my_set))

set2= {15,35,55}
print(type(set2))


alisveris = {'ekmek','sut','yumurta','peynir','yag','yogurt'}
alisveris.add('tavuk')

ekliste = {'hosaf','corba','pilav'}

alisveris.update(ekliste)




alisveris.discard('ekmek')
alisveris.pop()
print(alisveris)

#--------------------------
#dicitonary

model=["A","B","C","D","E"]
fiyat=[15.70,19.59,25.70,17.15,23.45]
modelfiyat_sozluk1= {'A':15.7,'B':19.59,'C':25.7,'D':17.15,'E':23.45}
print(type(modelfiyat_sozluk1))

modelfiyat_sozluk2= dict([('A',15.7),('B',19.59),('C',25.7),('D',17.15),('E',23.45)])
print(modelfiyat_sozluk2)
print(modelfiyat_sozluk2.keys())
print(modelfiyat_sozluk2.values())
modelfiyat_sozluk2['A']=11
print(modelfiyat_sozluk2.values())
modelfiyat_sozluk3={'F':55,'G':44}
modelfiyat_sozluk2.update(modelfiyat_sozluk3)
print(modelfiyat_sozluk2)
print(modelfiyat_sozluk2.items())
#son elemani siler
modelfiyat_sozluk2.popitem() 
#B elemani siler
modelfiyat_sozluk2.pop("B")
print(modelfiyat_sozluk2.items())





#--------------------------


