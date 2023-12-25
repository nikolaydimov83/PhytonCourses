budget=float(input())
priceFlourKilo=float(input())
priceOfEggs=priceFlourKilo*0.75
priceMilkKilo=priceFlourKilo*1.25
priceMilkDose=priceMilkKilo/4
loafsOfBread=0
egs=0
costOfBread=priceMilkDose+priceOfEggs+priceFlourKilo
while True:
    if (budget-costOfBread)>=0:
        loafsOfBread+=1
        egs+=3
        budget=budget-costOfBread
        if (loafsOfBread%3==0):
            egs=egs - (loafsOfBread-2)
    else:
        print(f"You made {loafsOfBread} loaves of Easter bread! Now you have {egs} eggs and {budget:2.2f}BGN left.")
        break