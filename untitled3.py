
import calendar 

y=int(input("Lütfen bir yıl giriniz: "))
x=int(input("Lütfen herhangi bir ayı sayısal değer olarak giriniz: "))

if x<=12 and x>=1:
    gun_sayisi = calendar.monthrange(y, x)[1]
    print("{} yılının {}.ayı {} gün çekmektedir.".format(y, x, gun_sayisi))
    

    
else:
    print("Hatalı değer girdiniz.")
    

    


