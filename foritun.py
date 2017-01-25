#Sigurður Axel
#25.1.2017
#Dæmi 1
tala1 = int(input("Sláðu inn fyrstu tölu"))
tala2 = int(input("Sláðu inn seinni tölu"))
summa = tala1 + tala2
marg = tala1 * tala2
print("Tölurnar lagðar saman:" , summa , "og margfaldaðar saman:" , marg)

#Dæmi 2
fornafn = input("Sláðu inn fornafn þitt ")
eftirnafn = input("Sláðu inn eftir nafn þitt ")
print("Halló" , fornafn , eftirnafn)

#Dæmi 3
ha = 0
la = 0
setning = input("Sláðu inn texta ")
for o in setning:
    if o.isupper():
        ha = ha +1
    else:
        la = la +1
print("Í þessum texta eru," , ha , "hástafir" , la , "lágstafir")