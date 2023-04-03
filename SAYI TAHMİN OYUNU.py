




import random 

maxtahsayi=12
tensayac=0
sixsayac=0
foursayac=0
nettahminsayi=0
sayiDyerD=0
sayiDyerY=0


tenlist=[]
sixchoicelist=[]
fourchoicelist=[]

while tensayac<10:
    tennumgen=int(random.random()*10)
    tenlist.append(tennumgen)
    tensayac+=1
    
while sixsayac<6:
    sixchoice=random.choice(tenlist)
    sixchoicelist.append(sixchoice)
    sixsayac+=1
    
    
while foursayac<4:
    fourchoice=random.choice(sixchoicelist)
    if fourchoicelist.count(fourchoice)==0:
        fourchoicelist.append(fourchoice)
        foursayac+=1    
    
    
    
    

print("Seçilen 10 rakam: ", tenlist)
print("Seçilen 6 rakam: " ,sixchoicelist)
print("Seçilen 4 rakam: ", fourchoicelist)



    
    
while nettahminsayi < maxtahsayi:
    try:
        sayitahmin=int(input("lütfen sayıyı tahmin ediniz : "))
    except:
        print("Lütfen sayı giriniz.")
        break 
    try:
        yertahmin =int(input("lütfen yerini tahmin ediniz : "))
    except:
        print("Lütfen yerini sayı ile belirtiniz.")
    print("{} tahmin hakkınız kaldı".format(maxtahsayi - nettahminsayi))
    nettahminsayi+=1
    
    
    
    
    sayitahsayac=fourchoicelist.count(sayitahmin)
   
    try:
         yertahminsayac=fourchoicelist.index(sayitahmin)
        
    except:
        print("Girdiğiniz iki değer de yanlış.")



    if sayitahsayac > 0 and yertahminsayac == yertahmin:
        sayiDyerD += 1

    elif sayitahsayac > 0 and yertahminsayac != yertahmin:
        sayiDyerY +=1
        
        
    print("D: ", sayiDyerD)
    print("Y: ", sayiDyerY)      
    
 




























