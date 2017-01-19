#DEFINING INPUTS
cash = float(input("Please input value of cash: "))
price = float(input("Please input price of chocolate: "))
#CALCULATING CHANGE
change = (cash - price) * 10 #MULTIPLIED BY 10 BECAUSE DECIMALS ARE TERRIBLE TO DEAL WITH

#CALCULATING IF THERE IS SUFFICIENT FUNDS & IF CHANGE IS NEEDED
if change < 0:
    print "Insufficient funds, please enter", -change/10, "dollars."
elif change == 0:
    print "The price of chocolate is", price, "dollars."
    print "The amount paid is", cash, "dollars."
    print "No change is given."
else:
    print "The price of chocolate is", price, "dollars."
    print "The amount paid is", cash, "dollars."
    print "Change due is", change/10, "dollars."

#IF CHANGE IS NEEDED, LOOP CALCULATES WHICH COINS TO GIVE
    TenCentCoin = 0
    FiftyCentCoin = 0
    OneDollarCoin = 0
    TwoDollarCoin = 0
    FiveDollarCoin = 0
    TenDollarCoin = 0

    while change > 0:
        if change >= 100:
            change = change - 100
            TenDollarCoin = TenDollarCoin + 1

        elif change >= 50:
            change = change - 50
            FiveDollarCoin = FiveDollarCoin + 1

        elif change >= 20:
            change = change - 20
            TwoDollarCoin = TwoDollarCoin + 1

        elif change >= 10:
            change = change - 10
            OneDollarCoin = OneDollarCoin + 1

        elif change >= 5:
            change = change - 5
            FiftyCentCoin = FiftyCentCoin + 1

        elif change >= 1:
            change = change - 1
            TenCentCoin = TenCentCoin + 1

    print "You will recieve", TenDollarCoin, "10$ coin(s),", FiveDollarCoin, "5$ coin(s),", TwoDollarCoin, "2$ coin(s),", OneDollarCoin, "1$ coin(s),", FiftyCentCoin, "50 cent coin(s), and", TenCentCoin, "10 cent coin(s)."
