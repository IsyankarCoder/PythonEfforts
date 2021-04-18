#kume ornegi

listkum= {("Adana",1),("Samsun",2),("Malatya",3)}
for sehir in listkum :
  print(sehir)

listkum2 = {("Adana",1),("Ssamsun",2),("Malatya",3),("Mardin",4)}
for(x,y)  in listkum2 : 
    print("key:",x)
print("value:",y)


#dictionary
sozluk1= {"ogr1":70,"ogr2":45,"ogr3":90,"ogr4":30,"ogr5":100}
for(key,value) in sozluk1.items() : 
     print(key,value)
print(value)


 #liste
ll = ["kirmizi"]
meyveler =["elma","muz","cilek"]
for x in ll:
    for y in meyveler:
     print(x," - ", y)
