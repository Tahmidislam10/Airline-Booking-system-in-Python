seatsleft=152
t_ad_s=0
t_ch_s=0
nam=[]
sur=[]
ads=[]
chs=[]
print("✈Welcome to Tahmid airlines✈")
while True:
    forname=str(input("what is your name"))
    surname=str(input("what is your surname"))
    aseats=int(input("how many adult seats?"))
    cseats=int(input("how many childe seats?"))
    nam.append(forname)
    sur.append(surname)
    ads.append(aseats)
    chs.append(cseats)
    test=aseats+cseats
    if seatsleft<test:
        print("flight is overbooked")
        seatsleft=152
        continue
    else:
        print("")
        
    
    
    adultprice=120
    childprice=60
    adultotal=adultprice*aseats
    childtotal=childprice*cseats
    totalprice=adultotal+childtotal
    seatsleft=seatsleft-test
    t_ad_s=t_ad_s+aseats
    t_ch_s=t_ch_s+cseats
    t_ss=t_ch_s+t_ch_s
    ttpricea=t_ad_s*adultprice
    ttpricec=t_ch_s*childprice
    ttprice=ttpricea+ttpricec
    
    

        
    
        
        
    print("the number of adult seats sold are",aseats)
    print("the number of child seats sold are",cseats)
    print("the total number of seats sold",test)
    print("price only for adult seats is",adultotal)
    print("price only for child seats is",childtotal)
    print("total price is",totalprice)
    print("currently avaliable seats are",seatsleft)
    more=str(input("would you like to purchase more seats?(press any key for no and type 'yes' for yes)")).lower()
    if more =="yes":
        continue
    else:
        break


print("total number of adult seats sold are",t_ad_s)
print("total number of child seats sold are",t_ch_s)
print("total number of seats sold are",t_ss)
print("total price for adult",ttpricea)
print("total price for child",ttpricec)
print("total price is",ttprice)
print("seats remaining",seatsleft)
print("name surname adult seats child seats")
print(nam, sur, ads, chs)


